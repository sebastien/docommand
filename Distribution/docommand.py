#8< ---[docommand.py]---
#!/usr/bin/env python
import sys
__module__ = sys.modules[__name__]
import re
import os
__module_name__ = 'docommand'
__version__ = '0.1.0'
ERR_MISSING_ARGUMENTS = 'Missing arguments'
class Command:
	RE_ARGUMENT = re.compile('\\${(\\d+)(([\\:=])([^}]+))?}')
	def __init__ (self, name, expression):
		self.name = ''
		self.expression = ''
		self.parsedExpression = []
		self.arguments = []
		self.name = name
		self.expression = expression
		self.parsedExpression = self._parseExpression(expression)
	
	def _parseExpression(self, expression):
		res=[]
		offset=0
		while (offset < len(expression)):
			match=self.__class__.RE_ARGUMENT.search(expression, offset)
			if match:
				argument_number = int(match.group(1))
				default_argument = match.group(4)
				default_argument_type = match.group(3)
				res.append(['T', expression[offset:match.start()]])
				if default_argument:
					res.append(['O', argument_number, default_argument_type, default_argument])
				elif True:
					res.append(['A', argument_number, None, None])
				offset = match.end()
			elif True:
				res.append(['T', expression[offset:]])
				offset = len(expression)
		return res
	
	def addArgument(self, defaultValue):
		self.arguments.append((defaultValue or ''))
	
	def getArguments(self, arguments=None):
		"""Returns a list representing the initialized arguments from the given
		(optional list of argument). When no argument is given, the the default
		argument values are returned."""
		if arguments is None: arguments = []
		res=[]
		for a in arguments:
			res.append(a)
		while (res.length() < self.arguments.length()):
			res.append(self.arguments[(res.length() - 1)])
		return res
	
	def getArity(self):
		pass
	
	def fill(self, arguments):
		"""Fills the command template with the given arguments and returns the filled
		expression as a string."""
		res=[]
		offset=0
		arg_count=0
		for element in self.parsedExpression:
			if (element[0] == 'T'):
				res.append(element[1])
			elif (element[0] == 'A'):
				arg_number=element[1]
				if (len(arguments) <= arg_number):
					raise ERR_MISSING_ARGUMENTS
				elif True:
					res.append(arguments[arg_number])
			elif (element[0] == 'O'):
				arg_number=element[1]
				if (len(arguments) <= arg_number):
					if (element[2] == ':'):
						result=os.popen(element[3]).read()
						if (result and (result[-1] == '\n')):
							result = result[0:-1]
						res.append(result)
					elif True:
						res.append(element[3])
				elif True:
					res.append(arguments[arg_number])
		return ''.join(res)
	
	def describe(self):
		return ' '.join([self.name, '\t', self.expression])
	

class Parser:
	"""Parses the '~/.docommand' file and returns a list of Command objects that can
	be used by the interpreter."""
	def parseFile(self, path):
		fd=file(path)
		commands=[]
		for line in fd.readlines():
			line = line.strip()
			if (line and (line[0] != '#')):
				name_desc=line.split(':', 1)
				command_name=name_desc[0]
				command_desc=name_desc[1]
				command_name = command_name.replace('\t', '').strip()
				command_desc = command_desc.strip()
				commands.append(Command(command_name, command_desc))
		return commands
	

class Interpreter:
	def __init__ (self, configuration=None):
		self.parser = Parser()
		self.commands = []
		if configuration is None: configuration = '~/.docommands'
		self.commands = self.parser.parseFile(os.path.expanduser(configuration))
	
	def commandWithName(self, name):
		for command in self.commands:
			if (command.name == name):
				return command
		raise Exception('Command not found')
	
	def run(self, arguments):
		command_name=arguments[0]
		command=self.commandWithName(command_name)
		script=command.fill(arguments[1:])
		print (('do:' + script))
		os.system(script)
	
	def listCommands(self):
		for c in self.commands:
			print (c.describe())
	

def __main__ (args):
	self=__module__
	i=Interpreter()
	if (len(args) == 1):
		i.listCommands()
	elif True:
		i.run(args[1:])


if __name__ == "__main__":
	import sys
	sys.exit(__main__(sys.argv))
