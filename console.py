#!/usr/bin/python3
"""
This module contains code to start a console that sees to data storage and manipulation of AIRBnB project
"""
import cmd
from models.engine import file_storage
from models import base_model


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand instance is our python console """
    prompt = '(hbnb) '
    models = file_storage.FileStorage.airbnbClasses()

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """End-of-file (EOF) is also used to exit the program
        """
        return True

    def emptyline(self):
        """This function prevents running the previous command if enter key is pressed on blank line
        """
        pass

    def do_create(self, line):
        """This function creates a new instance of the class model supplied
        """
        if line is None:
            print('class name missing')
        elif line not in HBNBCommand.models:
            print('class doesn\'t exist')
        else:
            instance = HBNBCommand.models[line]() 
            instance.save()
            print(instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

