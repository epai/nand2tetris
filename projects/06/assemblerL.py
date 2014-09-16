### 
### Eric Pai
### Translates code written in Hack assembly language
### into Hack Machine language
###

from ucb import main
from parser import *
from code import *

"""
--- Assembler (Symbol-less) ---
Translates assembly programs without symbols to Hack machine language
"""

@main
def run(filename):
	hack = open(filename[:-4] + '.hack', 'w')
	p = Parser(filename)
	while p.has_more_commands:
		if p.command_type == 'A':
			new_line = '0' + '{0:015b}'.format(int(p.symbol))
			hack.write(new_line + '\n')
		elif p.command_type == 'C':
			new_line = '111' + comp(p.comp) + dest(p.dest) + jump(p.jump)
			hack.write(new_line + '\n')
		p.advance()
	hack.close()
