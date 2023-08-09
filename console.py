#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
"""
console module
"""


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand instance is our python shell """
    prompt = '(hbnb) '
    models = {'BaseModel': BaseModel()}

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """End-of-file (EOF) is also used to exit the program
        """
        return True

    def emptyline(self):
        pass

    # def process_batch_input(self, line):
    #     commands = line.split(' ')
    #     for command in commands:
    #         self.onecmd(command)
    def do_create(self, line):
        if line is None:
            print('class name missing')
        elif line not in HBNBCommand.models:
            print('class doesn\'t exist')
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)

    # def do_show(self, line):
    #     commands = line.split(' ')
    #     if commands[0] is None:
    #         print('class name missing')
    #     elif commands[0] not in HBNBCommand.models:
    #         print('class dosen\'t exist')
    #     elif commands[1] is None:
    #         print("instance id missing")
    #     elif
    #
    #         if commands[0] in

def parse(line):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, line.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
