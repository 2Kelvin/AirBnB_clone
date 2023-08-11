# `AirBnB` clone website made from scratch
## Project Description
This project is about deploying a simple copy of the AirBnB website to a web server. Although all the code for deploying the cloned AirBnB website is not provided at once in this repository. A command interpreter (python console) to manipulate data, essential data models has been created, as well as a json file for storing the data.

## Command Interpreter
The command interpreter is a command line interpreter that permits management of the AirBnB objects. It can be used to create, update, destroy, show and all objects used for the project. The command interpreter is also used to manage the storage of the project.
### How to start it
The command interpreter can be used in both interactive and non-interactive mode. To start the interactive mode, run the following command:
```./console.py``` or ```./console```
The non-interactive mode is used by piping commands into the command interpreter as shown below:
```echo "help" | ./console.py```
### How to use it
The command interpreter supports the following commands:
#### Commands
The command interpreter supports the following commands:
* ```create``` - Creates a new instance of a class
* ```show``` - Prints the string representation of an instance based on the class name and id
* ```destroy``` - Deletes an instance based on the class name and id
* ```all``` - Prints all string representation of all instances based or not on the class name
* ```update``` - Updates an instance based on the class name and id by adding or updating attribute

**create command syntax:**
```(hbnb) create <class name>```
example:
```(hbnb) create BaseModel```

**show command syntax:**
```(hbnb) show <class name> <id>```
example:
```(hbnb) show BaseModel 1234-1234-1234```


**destroy command syntax:**
```(hbnb) destroy <class name> <id>```
example:
```(hbnb) destroy BaseModel 1234-1234-1234```


**all command syntax:**
```(hbnb) all <class name>``` or ```(hbnb) all```
example:
```(hbnb) all BaseModel``` or ```(hbnb) all```

**update command syntax:**
```(hbnb) update <class name> <id> <attribute name> "<attribute value>"```
example:
```(hbnb) update BaseModel 1234-1234-1234 email "abc@gmail.com"```

#### Classes
The command interpreter supports the following classes:
* ```BaseModel``` - Defines all common attributes/methods for other classes
* ```User``` - Inherits from ```BaseModel```
* ```State``` - Inherits from ```BaseModel```
* ```City``` - Inherits from ```BaseModel```
* ```Amenity``` - Inherits from ```BaseModel```
* ```Place``` - Inherits from ```BaseModel```
* ```Review``` - Inherits from ```BaseModel```

#### Other Built-in commands:
* ```quit``` - Exits the command interpreter
* ```EOF``` - Exits the command interpreter
* ```help``` - Displays the documented commands
example:
```(hbnb) help```
```(hbnb) help create```
