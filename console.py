#!/usr/bin/python3
''' Console interpreter CMD for python '''

import cmd
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review
import models


posi = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
content = models.storage.all()
saving = models.storage.save()
dictclass = {'BaseModel': BaseModel, 'User': User, 'State': State,
             'City': City, 'Amenity': Amenity, 'Place': Place,
             'Review': Review}


class HBNBCommand(cmd.Cmd):
    ''' class HBNBCommand, commands '''
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """
        Command quit to close and exit the program
        """
        return True

    def do_EOF(self, arg):
        """ Command EOF to close and exit the program
        """
        return True

    def emptyline(self):
        """ Command emptyline to pass in empty line
        """
        pass

    def do_create(self, args):
        """
        Create instances from a given argument
        Usage: create <class name>

        """
        arg = args.split(" ")
        if len(arg) < 1:
            print("** class name missing **")
        elif not arg[0] in posi:
            print("** class doesn't exist **")
        else:
            clase = arg[0]
            modelito = dictclass[clase]()
            modelito.save()
            print(modelito.id)

    def do_show(self, arg):
        """
        Shows dictionary representation of an object
        Usage : show <class name> <instance id>
        """
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        else:
            if not arg[0] in posi:
                print("** class doesn't exist **")
            elif len(arg) != 2:
                print("** instance id missing **")
            else:
                key = str(arg[0]) + '.' + str(arg[1])
                if key in content:
                    print(content[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """
        Destroys instances which are stored in the json file
        Usage : destroy <class name> <instance id>

        """
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif not arg[0] in posi:
            print("** class doesn't exist **")
        elif len(arg) != 2:
            print("** no instance found **")
        else:
            key = str(arg[0]) + "." + str(arg[1])
            if key in content:
                del content[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not
        in class name

        Usage: all
               all <class name>
        """
        arg = arg.split()
        aux = []
        if len(arg) == 0:
            for key, value in content.items():
                aux.append(str(value))
            print(aux)
        else:
            if not arg[0] in posi:
                print("** class doesn't exist **")
            else:
                for key, value in content.items():
                    if arg[0] in key:
                        aux.append(str(value))
                print(aux)

    def do_update(self, arg):
        """
        Updates attributes of a given class.

        Usage: update <class name> <class attribute> <attribute value
        """
        arg = arg.split(" ")
        intfields = ["my_number", "number_rooms", "number_bathrooms",
                     "max_guest", "price_by_night"]
        floatfields = ["latitude", "longitude"]
        if len(arg) == 0:
            print("** class name missing **")
            return
        if not arg[0] in posi:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        else:
            llave = str(arg[0]) + '.' + str(arg[1])
            if llave not in content:
                print("** no instance found **")
                return
            elif len(arg) < 3:
                print("** attribute name missing **")
                return
            elif len(arg) < 4:
                print("** value missing **")
                return
            else:
                if arg[2] in intfields:
                    value = int(arg[3])
                elif arg[2] in floatfields:
                    value = float(arg[3])
                else:
                    value = arg[3]
            setattr(content[llave], arg[2], value)
            saving
if __name__ == '__main__':
    HBNBCommand().cmdloop()
