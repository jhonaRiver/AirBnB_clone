#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

	prompt = "(hbnb) "
	allowed_classes = ['BaseModel']
	
	def do_quit(self, arg):
		'''Quit command to exit the program'''
		return True

	def do_EOF(self, arg):
		''' End of File '''
		print("")
		return True

	def help(self):
		''' help command '''
		return True

	def emptyline(self):
		''' registers an empty line and does a pass '''
		pass

	def do_create(self, line):
		''' creates a new class instance of BaseModel'''
		command = self.parseline(line)[0]
		if command is None:
			print('** class name is missing **')
		elif command not in self.allowed_classes:
			print("** class doesn't exist **")
		else:
			new_obj = eval(command)()
			print(new_obj.id)

	def do_show(self, line):
		'''Prints the string representation of an instance based on the class name and id'''
		command = self.parseline(line)[0]
		arg = self.parseline(line)[1]
		if command is None:
			print('** class name is missing **')
		elif command not int self.allowed_classes:
			print("** class doesn't exist **")
		elif arg == '':
			print('** instance id missing **')

if __name__ == '__main__':
	HBNBCommand().cmdloop()
