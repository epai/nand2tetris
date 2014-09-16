### 
### Eric Pai
### Translates code written in Hack assembly language
### into Hack Machine language
###

from ucb import main
from Assembler_parser import *
from Assembler_code import *

"""
--- Assembler (Symbol-less) ---
Translates ALL assembly programs to Hack machine language

Works in a three step process:
1)  Initializes all built in symbols to their corresponding
    memory addresses
2)  Passes through the assembly code and converts all goto labels
    into ROM memory locations
3)  Passes through the assembly code once more and translates
	each assembly command into Hack machine language, handling
	variables along the way.
"""

#Initialization of built in symbols
symbol_table = {
	'SP':0, 'LCL':1, 'ARG':2, 'THIS':3, 'THAT':4,
	'R0':0, 'R1':1, 'R2':2, 'R3':3, 'R4':4, 'R5':5,
	'R6':6, 'R7':7, 'R8':8, 'R9':9, 'R10':10, 'R11':11,
	'R12':12, 'R13':13, 'R14':14, 'R15':15, 
	'SCREEN':16384, 'KBD':24576
}

@main
def run(filename):
	hack = open(filename[:-4] + '.hack', 'w')
	#first pass
	p1 = Parser(filename)
	counter = 0
	while p1.has_more_commands:
		if p1.command_type == 'C' or p1.command_type == 'A':
			counter += 1
		else: #command_type == 'L'
			symbol_table[p1.symbol] = counter
		p1.advance()
	#second pass
	p2 = Parser(filename)
	next_RAM_address = 16
	while p2.has_more_commands:
		if p2.command_type == 'A':
			address = p2.symbol
			if not p2.symbol.isdigit():
				if p2.symbol not in symbol_table:
					symbol_table[p2.symbol] = next_RAM_address
					next_RAM_address += 1
				address = symbol_table[p2.symbol]
			new_line = '0' + '{0:015b}'.format(int(address))
			hack.write(new_line + '\n')
		elif p2.command_type == 'C':
			new_line = '111' + comp(p2.comp) + dest(p2.dest) + jump(p2.jump)
			hack.write(new_line + '\n')
		p2.advance()
	#finish translation
	hack.close()
