#!/usr/bin/python3
"""
module holds entry point of command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNH Console
    """
    prompt = "(hbnb) "

    allowed_classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Place': Place,
        'Amenity': Amenity,
        'Review': Review
    }

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF signal to exit the program
        """
        print("")
        return True

    def help(self):
        """
        help command
        """
        return True

    def emptyline(self):
        """
        registers an empty line and does a pass
        """
        pass

    def do_create(self, line):
        """
        creates a new class instance of BaseModel
        """
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
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        command = line.partition(" ")
        class_name = command[0]
        class_id = command[2]

        if not class_name:
            print('** class name is missing **')
            return False

        elif class_name not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
            return False

        elif not class_id:
            print('** instance id missing **')
            return False

        key = class_name + '.' + class_id

        try:
            print(storage._FileStorage__objects[key])

        except KeyError:
            print("** no instance found **")
            return False

    def do_destroy(self, line):
        """
        deletes an instance specified by user
        """
        command = line.partition(" ")
        class_name = command[0]
        class_id = command[2]

        if not class_name:
            print("** class name missing **")
            return False

        elif class_name not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
            return False

        elif class_id is None:
            print("** instance id is missing **")
            return False

        key = class_name + '.' + class_id

        try:
            del(storage.all()[key])
            storage.save()

        except KeyError:
            print("** no instance found **")
            return False

    def do_all(self, line):
        """
        prints all string rep of instance
        based or not in the class name
        """
        all_list = []

        if line:
            split = line.split(" ")[0]
            if line not in HBNBCommand.allowed_classes:
                print("** class doesn't exist **")
                return False
            for key, value in storage._FileStorage__objects.items():
                all_list.append(str(value))
        else:
            for key, value in storage._FileStorage__objects.items():
                all_list.append(str(value))

        print(all_list)

    def do_update(self, line):
        """
        Updates an instance based or not in the class name
        """
        command = line.partition(" ")
        class_name = command[0]
        class_id = command[2]
        id_part = class_id.partition(" ")
        email = id_part[2].partition(" ")

        if not class_name:
            print("** class name missing **")
            return False

        elif class_name not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
            return False

        elif id_part[0] is None:
            print("** instance id missing **")
            return False

        elif email[0] is None:
            print("** attribute name missing **")
            return False

        elif email[2] is None:
            print("** value missing **")
            return False

        if email[2]:
            setattr(self, email[0], str(email[2]))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
