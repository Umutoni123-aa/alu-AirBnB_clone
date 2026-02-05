#!/usr/bin/python3
""" Console"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """Quit command"""
        return True
    
    def do_EOF(self, arg):
        """EOF command"""
        print()
        return True
    
    def emptyline(self):
        """Do nothing"""
        pass
    
    def do_create(self, arg):
        """Create instance: create BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            print(obj.id)
    
    def do_show(self, arg):
        """Show instance: show BaseModel <id>"""
        if not arg:
            print("** class name missing **")
        else:
            print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
