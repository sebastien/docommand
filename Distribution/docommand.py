#8< ---[docommand.py]---
import sys
__module__ = sys.modules[__name__]
import re
import os
__module_name__ = 'docommand'
__version__ = '0.1.0'
ERR_MISSING_ARGUMENTS = "Missing arguments"
class Command(object):
	RE_ARGUMENT = re.compile("\${(\d+)([\:=]([^}]+))?}")
	def __init__ (self, name, expression):
		self.name = ""
		self.expression = ""
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
				default_argument = match.group(3)
				default_argument_type = match.group(2)
				self_1187969458_7189=res
				self_1187969458_7189.append(["T", expression[offset:match.start()]])
				if default_argument:
					self_1187969458_713=res
					self_1187969458_713.append(["O", argument_number, default_argument_type, default_argument])
				elif True:
					self_1187969458_7126=res
					self_1187969458_7126.append(["A", argument_number, None, None])
				offset = match.end()
			elif True:
				self_1187969458_7231=res
				self_1187969458_7231.append(["T", expression[offset:]])
				offset = len(expression)
		return res
	
	def addArgument(self, defaultValue):
		self_1187969458_7212=self.arguments
		self_1187969458_7212.append((defaultValue or ""))
	
	"""Returns a list representing the initialized arguments from the given
	(optional list of argument). When no argument is given, the the default
	argument values are returned."""
	def getArguments(self, arguments=None):
		if arguments is None: arguments = []
		res=[]
		for a in arguments:
			self_1187969458_7253=res
			self_1187969458_7253.append(a)
		while (len(res) < len(self.arguments)):
			self_1187969458_7325=res
			self_1187969458_7325.append(self.arguments[(len(res) - 1)])
		return res
	
	def getArity(self):
		pass
	
	"""Fills the command template with the given arguments and returns the filled
	expression as a string."""
	def fill(self, arguments):
		res=[]
		offset=0
		arg_count=0
		for element in self.parsedExpression:
			if (element[0] == "T"):
				self_1187969458_7396=res
				self_1187969458_7396.append(element[1])
			elif (element[0] == "A"):
				arg_number=element[1]
				if (len(arguments) <= arg_number):
					raise ERR_MISSING_ARGUMENTS
				elif True:
					self_1187969458_7319=res
					self_1187969458_7319.append(arguments[arg_number])
			elif (element[0] == "O"):
				arg_number=element[1]
				if (len(arguments) <= arg_number):
					if (element[2] == ":"):
						self_1187969458_74100=res
						self_1187969458_74100.append((("`" + element[3]) + "`"))
					elif True:
						self_1187969458_7425=res
						self_1187969458_7425.append(element[3])
				elif True:
					self_1187969458_7433=res
					self_1187969458_7433.append(arguments[arg_number])
		return "".join(res)
	
	def describe(self):
		return " ".join([self.name, "\t", self.expression])
	

class Parser(object):
	"""Parses the '~/.docommand' file and returns a list of Command objects that can
	be used by the interpreter."""
	def parseFile(self, path):
		fd=file(path)
		commands=[]
		for line in fd.readlines():
			line = line.strip()
			if (line and (line[0] != "#")):
				command_name=line.split(":", 1)[0]
				command_desc=line.split(":", 1)[1]
				command_name = command_name.replace("\t", "").strip()
				command_desc = command_desc.strip()
				self_1187969458_7537=commands
				self_1187969458_7537.append(Command(command_name, command_desc))
		return commands
	

class Interpreter(object):
	def __init__ (self, configuration=None):
		self.parser = Parser()
		self.commands = []
		if configuration is None: configuration = "~/.docommands"
		self.commands = self.parser.parseFile(os.path.expanduser(configuration))
	
	def commandWithName(self, name):
		for command in self.commands:
			if (command.name == name):
				return command
		raise Exception("Command not found")
	
	def run(self, arguments):
		command_name=arguments[0]
		command=self.commandWithName(command_name)
		script=command.fill(arguments[1:])
		print (("do:" + script))
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
