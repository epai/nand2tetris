### 
### Eric Pai
### Translates code written in VM language
### into Hack assembly language
###

"""
--- VM Parser Module ---
Handles the parsing of a SINGLE .vm file, and encapsulates access to the
input code.  It reads VM commands, parse them, and provides convenient
access to their components.  In addition, it removes all white space and
comments.

Part 1 (Ch 7)
-- handle stack arithmetic
-- handle memory access commands

Part 2 (Ch 8)
-- 
"""

class Parser:
	def __init__(self, vmfile):
		"""Opens the input file/stream and gets ready to parse it."""
		self.file = open(vmfile, 'r')
		self.has_more_commands = True
		self.advance()

	def get_next_command(self):
		"""Within a .vm file, each VM command appears in a separate line, and in
		one of the following formats:  command, command arg, command arg1 arg2.
		The arguments are separated from each other and from the command part
		by one or more spaces.  '//' comments can appear at the end of any line
		and are ignored.  Blank lines are permitted and ignored."""
		curr = self.file.readline()
		if not curr.endswith('\n'):
			self.has_more_commands = False
			self.file.close()
		comment_index = curr.find('//')
		if comment_index != -1:
			curr = curr[:comment_index]
			if not curr:
				curr = curr + '\n'
		if curr == '\n':
			return ' '
		return curr[:-1].split() if curr.endswith('\n') else curr.split()
		# # blank line handling
		# if curr == '\n':
		# 	return ' '
		# # comment handling
		# comment_index = curr.find('//')
		# if comment_index != -1:
		# 	curr = curr[:comment_index]
		# 	if not curr: # if the line is just a comment, ignore it
		# 		return ' '
		# 	curr = curr + '\n'
		# # parse remaining command
		# if curr.endswith('\n'):
		# 	return curr[:-1].split()
		# else:
		# 	self.has_more_commands = False
		# 	self.file.close()
		# 	return curr.split()

	def advance(self):
		"""Reads the next command from the input and makes it the current
		command.  Should be called only if has_more_commands is true."""
		self.parts = self.get_next_command()
		while self.parts == ' ':
			self.parts = self.get_next_command()

	@property
	def command_type(self):
		"""Returns the type of the current VM command.  C_ARITHMETIC
		is returned for all arithmetic commands."""
		if self.command in 'add,sub,neg,eq,gt,lt,and,or,not':
			return 'C_ARITHMETIC'
		elif self.command == 'push':
			return 'C_PUSH'
		elif self.command == 'pop':
			return 'C_POP'
		elif self.command == 'label':
			return 'C_LABEL'
		elif self.command == 'call':
			return 'C_CALL'
		elif self.command == 'return':
			return 'C_RETURN'
		elif self.command == 'function':
			return 'C_FUNCTION'
		elif self.command == 'goto':
			return 'C_GOTO'
		elif self.command == 'if-goto':
			return 'C_IF'
		else:
			raise SyntaxError('invalid command')

	@property
	def command(self):
		"""Returns the current command."""
		return self.parts[0]

	@property
	def arg1(self):
		"""Returns the first argument of the current command.  In the case
		of C_ARITHMETIC, the command itself (add, sub, etc.) is returned.
		Should not be called if the current command is C_RETURN."""
		if self.command_type != 'C_RETURN':
			if self.command_type == 'C_ARITHMETIC':
				return self.command
			return self.parts[1]

	@property
	def arg2(self):
		"""Returns the second argument of the current command.  Should be
		called only if the current command is C_PUSH, C_POP, C_FUNCTION, or
		C_CALL."""
		if self.command_type in 'C_PUSH,C_POP,C_FUNCTION,C_CALL':
			return int(self.parts[2])

