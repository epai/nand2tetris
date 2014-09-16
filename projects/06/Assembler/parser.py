### 
### Eric Pai
### Translates code written in Hack assembly language
### into Hack Machine language
###

from ucb import main

"""
--- Parser Module ---
encapsulates access to input code.  reads an assembly language
command, parses it, and provides convenient access to the
command's components (fields and symbols).  In addition, removes
all white space and comments.
"""
class Parser:
	def __init__(self, filename):
		"""Opens file and determines the current command"""
		self.file = open(filename, 'r')
		self.has_more_commands = True
		# self.next_command = None
		self.advance()

	def get_current_command(self):
		"""Returns the next command with proper formatting."""
		curr = self.file.readline().replace(' ', '')
		if curr == '\n':
			return ' '
		comment_index = curr.find('//')
		if comment_index != -1:
			curr = curr[:comment_index]
			return curr if curr else ' '
		if curr.endswith('\n'):
			return curr[:-1]
		else:
			self.has_more_commands = False
			self.file.close()
			return curr

	def advance(self):
		"""Reads the next command from the input and makes it the current
		   command.  Should be called only if has_more_commands is true."""
		if self.has_more_commands:
			# if not self.next_command:
			# 	self.next_command = self.get_current_command()
			# 	while self.next_command == ' ':
			# 		self.next_command = self.get_current_command()
			# self.current_command = self.next_command
			self.current_command = self.get_current_command()
			while self.current_command == ' ':
				self.current_command = self.get_current_command()

	@property
	def command_type(self):
		"""Propert method that returns the type of the current command"""
		first = self.current_command[0]
		if first == '@':
			return 'A'
		elif first == '(':
			return 'L'
		return 'C'

	@property
	def symbol(self):
		"""Returns the symbol or decimal XXX of the current A or L command"""
		if self.command_type == 'A':
			return self.current_command[1:]
		elif self.command_type == 'L':
			return self.current_command[1:-1]

	@property
	def jump(self):
		"""Returns the jump mnemonic in the current C-command"""
		if self.command_type == 'C':
			index = self.current_command.find(';')
			if index != -1:
				return self.current_command[index + 1:]

	@property
	def comp(self):
		"""Returns the comp mnemonic in the current C-command"""
		if self.command_type == 'C':
			index = self.current_command.find(';')
			if index != -1:
				return self.current_command[:index]
			index = self.current_command.find('=')
			if index != -1:
				return self.current_command[index + 1:]

	@property
	def dest(self):
		"""Returns the dest mnemonic in the current C-command"""
		if self.command_type == 'C':
			index = self.current_command.find('=')
			if index != -1:
				return self.current_command[:index]

# @main
# def run(filename):
# 	f = Parser(filename)
# 	for line in f.file:
# 		print(line)
# 	f.close()


