#!/usr/bin/python3
"""
This module contains code to start a console that sees to data storage and
manipulation of AIRBnB project
"""
import cmd
from models import storage
import sys


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand instance is our python console """
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else '(hbnb)'
    models = storage.airbnbClasses()

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """End-of-file (EOF) is also used to exit the program
        """
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """This function creates a new instance of the class model supplied
        """
        if not line:
            print('class name missing')
        elif line not in HBNBCommand.models:
            print('class doesn\'t exist')
        else:
            instance = HBNBCommand.models[line]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """show command is used to Prints the string representation of an\
 instance based on the class name and id
        """
        if not line:
            print('class name missing')
            return
        commands = line.split(' ')
        if commands[0] not in self.models:
            print("class dosen't exist")
        try:
            id = commands[1]
        except IndexError:
            print("instance id missing")
            return
        key = commands[0] + '.' + commands[1]
        if key not in storage.all():
            print('no instance found')
        else:
            print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        if not line:
            print('class name missing')
            return
        commands = line.split(' ')
        if commands[0] not in self.models:
            print("class dosen't exist")
        try:
            id = commands[1]
        except IndexError:
            print("instance id missing")
            return
        key = commands[0] + '.' + commands[1]
        if key not in storage.all():
            print('no instance found')
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not on\
 the class name
        """
        result = []
        if not line:
            for value in storage.all().values():
                result.append(str(value))
            print(result)
        elif line not in self.models:
            print("class dosen't exist")
        else:
            model = line.split(' ')[0]
            for key, vl in storage.all().items():
                if line == key.split('.')[0]:
                    result.append(str(vl))
            print(result)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or\
 updating attribute
        """
        if not line:
            print('class name missing')
            return
        lst = line.split(" ")
        model = lst[0]
        if model not in self.models:
            print('class dosen\'t exist')
            return
        try:
            id = lst[1]
        except IndexError:
            print('instance id missing')
            return
        try:
            attribute = lst[2]
        except IndexError:
            print("attribute name missing")
            return
        try:
            value = lst[3]
        except IndexError:
            print('value missing')
            return

        key = model + '.' + id
        if key not in storage.all():
            print('no instance found')
            return

        if value.isdigit():
            value = int(value)
        else:
            try:
                value = float(value)
            except ValueError:
                pass
        setattr(storage.all()[key], attribute, value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
