#!/usr/bin/python3
"""
This module contains code to start a console that seeks to store data and
manipulate our AIRBnB project
"""
import cmd
from models import storage
import sys


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand instance is our python console """

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else '(hbnb)'
    models = storage.airbnbClasses()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Custom help docstring for quit()"""
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """End-of-file (EOF) used to exit the program"""
        return True

    def help_EOF(self):
        """Custom help docstring for EOF()"""
        print("End-of-file (EOF) used to exit the program\n")

    def emptyline(self):
        """Overrides default emptyline()"""
        pass

    def do_create(self, line):
        """Creates a new instance of the class model supplied"""
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.models:
            print("** class doesn't exist **")
        else:
            instance = HBNBCommand.models[line]()
            instance.save()
            print(instance.id)

    def help_create(self):
        """Custom create() help doc"""
        s1 = "Creates a new instance of the class passed,"
        s2 = "saves it to a JSON file"
        s3 = "and prints its id\n"
        print(" ".join([s1, s2, s3]))

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if not line:
            print("** class name missing **")
            return
        commands = line.split(' ')
        if commands[0] not in self.models:
            print("** class doesn't exist **")
        try:
            id = commands[1]
        except IndexError:
            print("** instance id missing **")
            return
        key = commands[0] + '.' + commands[1]
        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def help_show(self):
        """Custom show() help doc"""
        s1 = "Prints the string representation of an instance"
        s2 = "based on the class name and id\n"
        print(" ".join([s1, s2]))

    def do_destroy(self, line):
        """Deletes an instance"""
        if not line:
            print("** class name missing **")
            return
        commands = line.split(' ')
        if commands[0] not in self.models:
            print("** class doesn't exist **")
        try:
            id = commands[1]
        except IndexError:
            print("** instance id missing **")
            return
        key = commands[0] + '.' + commands[1]
        if key not in storage.all():
            print("** no instance found ** ")
        else:
            del storage.all()[key]
            storage.save()

    def help_destroy(self):
        """Custom destroy() help doc"""
        s1 = "Deletes an instance based on"
        s2 = "the class name and id and"
        s3 = "saves the change into the JSON file\n"
        print(" ".join([s1, s2, s3]))

    def do_all(self, line):
        """Prints all class instances"""
        result = []
        if not line:
            for value in storage.all().values():
                result.append(str(value))
            print(result)
        elif line not in self.models:
            print("** class doesn't exist **")
        else:
            model = line.split(' ')[0]
            for key, vl in storage.all().items():
                if line == key.split('.')[0]:
                    result.append(str(vl))
            print(result)

    def help_all(self):
        """Custom all() help doc"""
        s1 = "Prints all string representations of all instances"
        s2 = "based on the classname\n"
        print(" ".join([s1, s2]))

    def do_update(self, line):
        """Updates an instance"""
        if not line:
            print("** class name missing **")
            return
        lst = line.split(" ")
        model = lst[0]
        if model not in self.models:
            print("** class doesn't exist **")
            return
        try:
            id = lst[1]
        except IndexError:
            print("** instance id missing **")
            return
        try:
            attribute = lst[2]
        except IndexError:
            print("** attribute name missing **")
            return
        try:
            value = lst[3]
        except IndexError:
            print("** value missing **")
            return

        key = model + '.' + id
        if key not in storage.all():
            print("** no instance found **")
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

    def help_update(self):
        """Custom update() help doc"""
        s1 = "Updates an instance based on the class name"
        s2 = "and id by adding or updating attribute\n"
        print(" ".join([s1, s2]))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
