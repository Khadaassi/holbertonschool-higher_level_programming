<p align="center">
    <img [Python - Classes and Objects] src="https://www.askpython.com/wp-content/uploads/2019/09/Python-Classes-and-Objects-Thumbnail-1024x512.png.webp">
</p>

----------

# <p align="center">Python - Classes and Objects</p>

----------

## ➤ Menu:

* [➤ Description](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-classes#-description)
* [➤ Resources](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-classes#-resources)
* [➤ General](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-classes#-general)
* [➤ Requirements](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-classes#-requirements)
* [➤ Tasks](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-classes#-tasks)
* [➤ Author](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-classes#-author)

----------

## ➤ Description:

classes and objects are fundamental elements of object-oriented programming (OOP). Here's a description of each:

**Classes:**

* A class is a blueprint for creating objects.
* It defines the common characteristics that objects, which are instances of it, possess.
* Classes are declared using the `class` keyword followed by the class name, and they can contain attributes and methods.

**Objects:**

* An object is an instance of a class.
* It is created based on the model provided by the class and has its own values for the class attributes.
* Objects are created by invoking the class name followed by parentheses (similar to calling a function), which calls the class constructor to create a new instance.


Example of a simple class and object in Python:

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

# Creating an object (instance of the Car class)
car1 = Car("Toyota", "blue")

# Accessing object attributes
print(car1.brand)   # Output: Toyota
print(car1.color)   # Output: blue
```

In this example, `Car` is a class that defines the common properties of cars, such as brand and color. The object `car1` is an instance of this class with the specified values for brand and color. Object attributes are accessed using dot notation (`obj.attribute_name`).

----------

## ➤ Resources:

Read or watch:

* [Object Oriented Programming](https://intranet.hbtn.io/rltoken/5envVBirO286MdSZgZ4DoQ) (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, classmethod and staticmethod yet)
* [Object-Oriented Programming](https://intranet.hbtn.io/rltoken/sCdUrEsHLFH2NpUzI5Xx8w) (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The __init__ Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)
* [Properties vs. Getters and Setters](https://intranet.hbtn.io/rltoken/3B0RWILA_kSjK5udEbFt-A)
* [Learn to Program 9 : Object Oriented Programming](https://intranet.hbtn.io/rltoken/5u8UhnaTWX2A-G7LICKCDw)
* [Python Classes and Objects](https://intranet.hbtn.io/rltoken/cwqg7Ud04LTDsatPT17CaQ)
* [Object Oriented Programming](https://intranet.hbtn.io/rltoken/6cZhWLe083CJERYLjAM0BQ)

----------

## ➤ General:

* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is `self`
* What is a method
* What is the special `__init__` method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is the `__dict__` of a class and/or instance of a class and what does it contain
* How does Python find the attributes of an object or class
* How to use the `getattr` function

----------

## ➤ Requirements:

General

* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

----------

## ➤ Tasks:

### 0. My first square

Write an empty class `Square` that defines a square:

* You are not allowed to import any module

<details>
<summary>Tests</summary>

```python
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/$
```

</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-classes
* File: 0-square.py

----------
  
### 1. Square with size

Write a class `Square` that defines a square by: (based on `0-square.py`)

* Private instance attribute: `size`
* Instantiation with `size` (no type/value verification)
* You are not allowed to import any module

**Why?**

Why `size` is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

<details>
<summary>Tests</summary>

```python
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
guillaume@ubuntu:~/$
```

</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-classes
* File: 1-square.py

----------
  
### 2. Size validation

Write a class `Square` that defines a square by: (based on `1-square.py`)

* Private instance attribute: `size`
* Instantiation with optional `size`: `def __init__(self, size=0):`
 * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
 * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* You are not allowed to import any module

<details>
<summary>Tests</summary>

```python
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
guillaume@ubuntu:~/$
```

</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-classes
* File: 2-square.py

----------
  
### 3. Area of a square

Write a class `Square` that defines a square by: (based on `2-square.py`)

* Private instance attribute: `size`
* Instantiation with optional `size`: `def __init__(self, size=0):`
 * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
 * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* Public instance method: `def area(self):` that returns the current square area
* You are not allowed to import any module

<details>
<summary>Tests</summary>

```python
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

guillaume@ubuntu:~/$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
guillaume@ubuntu:~/$
```

</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-classes
* File: 3-square.py

----------
  
### 4. Access and update private attribute

Write a class `Square` that defines a square by: (based on `3-square.py`)

* Private instance attribute: `size`:
 * property `def size(self):` to retrieve it
 * property setter `def size(self, value):` to set it:
  * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
  * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* Instantiation with optional `size: def __init__(self, size=0):`
* Public instance method: `def area(self):` that returns the current square area
* You are not allowed to import any module

**Why?**

Why a getter and setter?

Reminder: `size` is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

<details>
<summary>Tests</summary>

```python
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
guillaume@ubuntu:~/$
```

</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-classes
* File: 4-square.py

----------
  
### 5. Printing a square

Write a class `Square` that defines a square by: (based on `4-square.py`)

* Private instance attribute: `size`:
  * property `def size(self)`: to retrieve it
  * property setter `def size(self, value)`: to set it:
   * size must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
   * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* Instantiation with optional `size: def __init__(self, size=0):`
* Public instance method: `def area(self):` that returns the current square area
* Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
  * if `size` is equal to 0, print an empty line
* You are not allowed to import any module

<details>
<summary>Tests</summary>

```python
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

guillaume@ubuntu:~/$ ./5-main.py
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
guillaume@ubuntu:~/$
```

</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-classes
* File: 5-square.py

----------
  
### 6. Coordinates of a square

Write a class `Square` that defines a square by: (based on `5-square.py`)

* Private instance attribute: `size`:
  * property `def size(self):` to retrieve it
  * property setter `def size(self, value):` to set it:
   * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
   * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* Private instance attribute: `position`:
  * property `def position(self):` to retrieve it
  * property setter `def position(self, value):` to set it:
   * `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`
* Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
* Public instance method: `def area(self):` that returns the current square area
* Public instance method: `def my_print(self):` that prints in stdout the square with the character #:
  * if `size` is equal to 0, print an empty line
  * `position` should be use by using space - **Don’t fill lines by spaces** when `position[1] > 0`
* You are not allowed to import any module

<details>
<summary>Tests</summary>

```python
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

guillaume@ubuntu:~/$ ./6-main.py | tr " " "_" | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
guillaume@ubuntu:~/$
```

</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-classes
* File: 6-square.py


----------

## ➤ Author:

- Khadija AASSI