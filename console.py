#!/usr/bin/python3
import cmd

from models.base_model import BaseModel
from models.__init__ import storage
from models.engine.file_storage import FileStorage
from models.user import User


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    allowed_classes = {
        'BaseModel',
        'User',
        'State',
        'City',
        'Place',
        'Amenity',
        'Review'
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
            print(storage._FileStorage__objects[key])

        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):

        command = line.partition(" ")
        class_name = command[0]
        class_id = command[2]

        if class_name is None:
            print("** class name is missing **")

        elif class_name not in HBNBCommand.allowed_classes:
            print("** class  doesn't exist **")

        elif class_id is None:
            print("** instance id is missing **")

        key = class_name + '.' + class_id

        try:
            del(storage.all()[key])
            storage.save()

        except KeyError:
            print("** no instance found **")

    def do_all(self, line):

        command = line.partition(" ")
        class_name = command[0]
        cmdlen = len(command)
        all_list = []

        if cmdlen > 0 and class_name not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")

        else:
            for key, value in storage._FileStorage__objects.items():
                all_list.append(str(value))

        print(all_list)

    def do_update(self, line):

        command = line.partition(" ")
        class_name = command[0]
        class_id = command[2]
        cmdlen = len(command)

        if class_name is None:
            print("** class name is missing **")
            return False

        if class_name not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
            return False

        if class_id is None:
            print("** instance id is missing **")
            return False

        key = class_name + '.' + class_id

        try:
            print(storage._FileStorage__objects[key])

        except KeyError:
            print("** no instance found **")
            return False

        if cmdlen == 2:
            print("** attribute name missing **")
            return False

        if cmdlen == 3:
            try:
                type(eval(class_id)) != dict
            except NameError:
                print("** value missing **")
                return False

        if cmdlen == 4:
            key = class_name + '.' + class_id
            if class_id in FileStorage.__objects.__dict__.keys():
                value_type = type(FileStorage.__objects.__dict__[class_id])
                FileStorage.__dict__[class_id] = value_type(cmdlen[3])

            else:
                FileStorage.__dict__[class_id] = cmdlen[3]

        elif type(eval(class_id)) == dict:
            key = class_name + '.' + class_id

            for key, value in eval(class_id).items():
                if key in FileStorage.__objects.__dict__.keys() and type(FileStorage.__objects.__dict__[key]) in {str, int, float}:
                    value_type = type(FileStorage.__objects.__dict__[key])
                    FileStorage.__dict__[key] = value_type(value)

                else:
                    FileStorage.__dict__[key] = value

        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
