### 
### Eric Pai
### Translates code written in VM language
### into Hack assembly language
###

"""
--- VM Code Writer Module ---
Translates VM commands into Hack assembly language. 

Part 1 (Ch 7)
-- handle stack arithmetic
-- handle memory access commands

Part 2 (Ch 8)
-- 
"""

class CodeWriter:
	def __init__(self, asmfile):
		"""Opens the output file/stream and gets ready to write into it."""
		self.file = open(asmfile, 'w')
		self.bool_label_counter = 0
		self.return_counter = 0

	def set_file_name(self, filename):
		self.filename = filename

	def write_arithmetic(self, command):
		"""Writes the assembly code that is the translation of the given
		arithmetic command."""
		if command in 'neg,not':
			op = '-' if command == 'neg' else '!'
			lines = ('@SP',
					 'A=M-1',
				     'D=M',
				     '@SP',
				     'A=M-1',
				     'M={0}D'.format(op))

		elif command in 'add,sub,and,or':
			op = '+' if command == 'add' else \
			     '-' if command == 'sub' else \
			     '&' if command == 'and' else \
			     '|'
			lines = ('@SP',
					 'D=M',
					 '@2',
					 'A=D-A',
				     'D=M',
				     '@SP',
				     'A=M-1',
				     'D=D{0}M'.format(op),
				     '@R13',
				     'M=D',
				     '@SP',
				     'D=M',
				     '@2',
				     'D=D-A',
				     '@R14',
				     'M=D',
				     '@R13',
				     'D=M',
				     '@R14',
				     'A=M',
				     'M=D',
				     '@SP',
				     'M=M-1')

		else: # command is either eq, >, or <
			op = 'JEQ' if command == 'eq' else \
				 'JLT' if command == 'lt' else \
				 'JGT'
			lines = ('@SP',
					 'D=M',
					 '@2',
					 'A=D-A',
				     'D=M',
				     '@SP',
				     'A=M-1',
				     'D=D-M',
				     '@TRUE{0}'.format(self.bool_label_counter),
				     'D;{0}'.format(op),
				     '@FALSE{0}'.format(self.bool_label_counter),
				     '0;JMP',
				     '(TRUE{0})'.format(self.bool_label_counter),
				     'D=-1',
				     '@END{0}'.format(self.bool_label_counter),
				     '0;JMP',
				     '(FALSE{0})'.format(self.bool_label_counter),
				     'D=0',
				     '@END{0}'.format(self.bool_label_counter),
				     '0;JMP',
				     '(END{0})'.format(self.bool_label_counter),
				     '@R13',
				     'M=D',
				     '@SP',
				     'D=M',
				     '@2',
				     'D=D-A',
				     '@R14',
				     'M=D',
				     '@R13',
				     'D=M',
				     '@R14',
				     'A=M',
				     'M=D',
				     '@SP',
				     'M=M-1')
			self.bool_label_counter += 1
		for line in lines:
			self.file.write(line + '\n')

	def write_push_pop(self, command, segment, index):
		"""Writes the assembly code that is the translation of the given
		command, where the command is either C_PUSH or C_POP"""
		if command == 'push':
			if segment == 'constant':
				lines = ('@{0}'.format(index),
						 'D=A',
						 '@SP',
						 'A=M',
						 'M=D',
						 '@SP',
						 'M=M+1')
			elif segment == 'temp':
				lines = ('@R{0}'.format(5 + index),
						 'D=M',
						 '@SP',
						 'A=M',
						 'M=D',
						 '@SP',
						 'M=M+1')
			elif segment == 'pointer':
				seg = 'THIS' if index == 0 else 'THAT'
				lines = ('@{0}'.format(seg),
						 'D=M',
						 '@SP',
						 'A=M',
						 'M=D',
						 '@SP',
						 'M=M+1')
			elif segment == 'static':
				lines = ('@{0}.{1}'.format(self.filename, index),
						 'D=M',
						 '@SP',
						 'A=M',
						 'M=D',
						 '@SP',
						 'M=M+1')
			else:
				seg = 'LCL' if segment == 'local' else \
					  'ARG' if segment == 'argument' else \
					  'THIS' if segment == 'this' else \
					  'THAT'
				lines = ('@{0}'.format(seg),
						 'D=M',
						 '@{0}'.format(index),
						 'A=D+A',
						 'D=M',
						 '@SP',
						 'A=M',
						 'M=D',
						 '@SP',
						 'M=M+1')
		else: # command == 'pop'
			if segment == 'temp':
				lines = ('@SP',
						 'M=M-1',
						 '@SP',
						 'A=M',
						 'D=M',
						 '@R{0}'.format(5 + index),
						 'M=D')
			elif segment == 'pointer':
				seg = 'THIS' if index == 0 else 'THAT'
				lines = ('@SP',
						 'M=M-1',
						 '@SP',
						 'A=M',
						 'D=M',
						 '@{0}'.format(seg),
						 'M=D')
			elif segment == 'static':
				lines = ('@SP',
						 'M=M-1',
						 '@SP',
						 'A=M',
						 'D=M',
						 '@{0}.{1}'.format(self.filename,index),
						 'M=D')
			else:
				seg = 'LCL' if segment == 'local' else \
						  'ARG' if segment == 'argument' else \
						  'THIS' if segment == 'this' else \
						  'THAT'
				lines = ('@SP',
						 'M=M-1',
						 '@{0}'.format(seg),
						 'D=M',
						 '@{0}'.format(index),
						 'D=D+A',
						 '@R13',
						 'M=D',
						 '@SP',
						 'A=M',
						 'D=M',
						 '@R13',
						 'A=M',
						 'M=D')
		for line in lines:
			self.file.write(line + '\n')

	#############################
	#### Chapter 8 Extensions ###
	#############################
	def write_init(self):
		"""Writes assembly code that effects the VM initialization, also
		called bootstrap code.  This code must be placed at the beginning
		of the output file."""
		lines = ('@256',
				 'D=A',
				 '@SP',
				 'M=D')
		for line in lines:
			self.file.write(line + '\n')
		self.write_call('Sys.init', 0)

	def write_label(self, label):
		"""Writes assembly code that effects the 'label' command"""
		self.file.write('({0}${1})'.format(self.filename, label) + '\n')

	def write_goto(self, label):
		"""Writes assembly code that effects the 'goto' command"""
		lines = ('@{0}${1}'.format(self.filename, label),
				 '0;JMP')
		for line in lines:
			self.file.write(line + '\n')

	def write_if(self, label):
		"""Writes assembly code that effects the 'if-goto' command."""
		lines = ('@SP',
				 'M=M-1',
				 '@SP',
				 'A=M',
				 'D=M',
				 '@{0}${1}'.format(self.filename, label),
				 'D;JNE')
		for line in lines:
			self.file.write(line + '\n')

	def write_call(self, function_name, num_args):
		"""Writes assembly code that effects the 'call' command"""
		lines = ('@return-address{0}'.format(self.return_counter), #push return-address
				 'D=A',
				 '@SP',
				 'A=M',
				 'M=D',
				 '@SP',
				 'M=M+1',
				 '@LCL', #push LCL
				 'D=M',
				 '@SP',
				 'A=M',
				 'M=D',
				 '@SP',
				 'M=M+1',
				 '@ARG', #push ARG
				 'D=M',
				 '@SP',
				 'A=M',
				 'M=D',
				 '@SP',
				 'M=M+1',
				 '@THIS', #push THIS
				 'D=M',
				 '@SP',
				 'A=M',
				 'M=D',
				 '@SP',
				 'M=M+1',
				 '@THAT', #push THAT
				 'D=M',
				 '@SP',
				 'A=M',
				 'M=D',
				 '@SP',
				 'M=M+1',
				 '@SP', #ARG = SP-n-5
				 'D=M',
				 '@5',
				 'D=D-A',
				 '@{0}'.format(num_args),
				 'D=D-A',
				 '@ARG',
				 'M=D',
				 '@SP', #LCL = SP
				 'D=M',
				 '@LCL',
				 'M=D',
				 '@{0}'.format(function_name), #goto f
				 '0;JMP',
				 '(return-address{0})'.format(self.return_counter))
		self.return_counter += 1
		for line in lines:
			self.file.write(line + '\n')

	def write_return(self):
		"""Writes assembly code that effects the return command."""
		lines = ('@LCL', #FRAME = LCL
				 'D=M',
				 '@R14',
				 'M=D',
				 '@5', #RET = *(FRAME-5)
				 'A=D-A',
				 'D=M',
				 '@R15',
				 'M=D',
				 '@SP', #*ARG = pop()
				 'A=M-1',
				 'D=M',
				 '@ARG',
				 'A=M',
				 'M=D',
				 '@ARG',
				 'D=M',
				 '@SP', #SP = ARG+1
				 'M=D+1',
				 '@R14', #THAT = *(FRAME-1)
				 'A=M-1',
				 'D=M',
				 '@THAT',
				 'M=D',
				 '@R14', #THIS = *(FRAME-2)
				 'A=M-1',
				 'A=A-1',
				 'D=M',
				 '@THIS',
				 'M=D',
				 '@R14', #ARG = *(FRAME-3)
				 'D=M',
				 '@3',
				 'A=D-A',
				 'D=M',
				 '@ARG',
				 'M=D',
				 '@R14', #LCL = *(FRAME-4)
				 'D=M',
				 '@4',
				 'A=D-A',
				 'D=M',
				 '@LCL',
				 'M=D',
				 '@R15', #goto RET
				 'A=M',
				 '0;JMP')
		for line in lines:
			self.file.write(line + '\n')

	def write_function(self, function_name, num_locals):
		"""Writes assembly code that effects the function command."""
		lines = ('({0})'.format(function_name),
				 '@{0}'.format(num_locals),
				 'D=A',
				 '@{0}.COUNTER'.format(function_name),
				 'M=D',
				 '({0}.LOOP)'.format(function_name),
				 '@{0}.COUNTER'.format(function_name),
				 'D=M',
				 '@{0}.END'.format(function_name),
				 'D;JEQ',
				 '@SP',
				 'A=M',
				 'M=0',
				 '@SP',
				 'M=M+1',
				 '@{0}.COUNTER'.format(function_name),
				 'M=M-1',
				 '@{0}.LOOP'.format(function_name),
				 '0;JMP',
				 '({0}.END)'.format(function_name)) 
		for line in lines:
			self.file.write(line + '\n')

	def write_breakpoint(self):
		self.file.write('@22222\n')

	def close(self):
		self.file.close()












