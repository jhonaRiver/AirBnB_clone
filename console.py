#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    allowed_classes = {
        'BaseModel'
    }

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, arg):
        ''' EOF signal to exit the program '''
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
        elif command not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(command)()
            print(new_obj.id)
            storage.save()

    def do_show(self, line):
        '''Prints the string representation of an instance based on the class name and id'''
        command = line.partition(" ")
        class_name = command[0]
        class_id = command[2]
        if class_name is None:
            print('** class name is missing **')
        elif class_name not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
        elif class_id is None:
            print('** instance id missing **')
        key = class_name + '.' + class_id
        try:
            print(storage._FileStorage.__objects[key])
        except KeyError:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
