### 
### Eric Pai
### Translates code written in VM language
### into Hack assembly language
###

"""
--- VM Code Writer Module ---
Marches through VM commands in the input file(s) and generates assembly
code for each (of them)

Part 1 (Ch 7)
-- handle stack arithmetic
-- handle memory access commands

Part 2 (Ch 8)
-- 
"""

from ucb import main
from os import listdir, chdir
from os.path import isdir, isfile
from VMparser import *
from VMcode_writer import *

@main
def run(source):
	if isfile(source) and source[-3:] == '.vm':
		p = Parser(source)
		cw = CodeWriter(source[:-3] + '.asm')
		cw.set_file_name(source[:-3])
		cw.write_init()
		while p.has_more_commands:
			#cw.write_breakpoint()
			if p.command_type == 'C_ARITHMETIC':
				cw.write_arithmetic(p.command)
			elif p.command_type == 'C_PUSH' or p.command_type == 'C_POP':
				cw.write_push_pop(p.command, p.arg1, p.arg2)
			elif p.command_type == 'C_LABEL':
				cw.write_label(p.arg1)
			elif p.command_type == 'C_GOTO':
				cw.write_goto(p.arg1)
			elif p.command_type == 'C_IF':
				cw.write_if(p.arg1)
			elif p.command_type == 'C_FUNCTION':
				cw.write_function(p.arg1, p.arg2)
			elif p.command_type == 'C_RETURN':
				cw.write_return()
			elif p.command_type == 'C_CALL':
				cw.write_call(p.arg1, p.arg2)
			p.advance()
		cw.close()
	elif isdir(source):
		seq = listdir(source)
		chdir(source)
		cw = CodeWriter(source + '.asm') # write one output file per directory
		cw.write_init()
		for f in seq:
			if isfile(f) and f[-3:] == '.vm':
				p = Parser(f) #f is a .vm file
				cw.set_file_name(f[:-3])
				while p.has_more_commands:
					#cw.write_breakpoint()
					if p.command_type == 'C_ARITHMETIC':
						cw.write_arithmetic(p.command)
					elif p.command_type == 'C_PUSH' or p.command_type == 'C_POP':
						cw.write_push_pop(p.command, p.arg1, p.arg2)
					elif p.command_type == 'C_LABEL':
						cw.write_label(p.arg1)
					elif p.command_type == 'C_GOTO':
						cw.write_goto(p.arg1)
					elif p.command_type == 'C_IF':
						cw.write_if(p.arg1)
					elif p.command_type == 'C_FUNCTION':
						cw.write_function(p.arg1, p.arg2)
					elif p.command_type == 'C_RETURN':
						cw.write_return()
					elif p.command_type == 'C_CALL':
						cw.write_call(p.arg1, p.arg2)
					p.advance()
		cw.close()
