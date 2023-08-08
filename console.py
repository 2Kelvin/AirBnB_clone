#!/usr/bin/python3
import cmd
import uuid
"""
console module
"""
class HBNBCommand(cmd.Cmd):
    """ """
    file = 'storage.json'
    prompt = '(hbnb) '
    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """End-of-file (EOF) is also used to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        if line is None:
            print('class name missing')
        else:
            instance = line()
            my_uuid = uuid.uuid4()
            with open(self.file, 'a') as f:
                f.write(JSON.dumps(a.to_json()))
            


if __name__ == '__main__':
        HBNBCommand().cmdloop()
