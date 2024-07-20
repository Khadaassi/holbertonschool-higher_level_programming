<p align="center">
    <img [Python - Exceptions] src="https://files.realpython.com/media/Raising-Exceptions-Manually-in-Python.-Best-Practices_Watermarked.ef77e2f3902b.jpg">
</p>

----------

# <p align="center">Python - Exceptions</p>

----------

## ➤ Menu:

* [➤ Description](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-exceptions#-description)
* [➤ Resources](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-exceptions#-resources)
* [➤ General](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-exceptions#-general)
* [➤ Requirements](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-exceptions#-requirements)
* [➤ Tasks](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-exceptions#-tasks)
* [➤ Author](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-exceptions#-author)

----------

## ➤ Description:

In Python programming, exceptions are events or conditions that occur during the execution of a program and can disrupt the normal flow of execution. Exceptions provide a mechanism to handle these exceptional situations in a controlled manner. Here is a detailed description of concepts related to exceptions in Python:

**Raising an Exception (raise):** Exceptions are raised using the raise keyword. This signals that an exceptional condition has occurred and interrupts the normal flow of the program.

```python
raise ValueError("This is a ValueError exception.")
try, except, else, finally Block: To handle exceptions, try and except blocks are used. Potentially problematic code is placed in the try block, and code to execute in case of an exception is specified in the except block. You can also use else (code to execute if no exception is raised) and finally (code to execute regardless of whether an exception is raised or not) blocks.
```

```python
try:
    # Potentially problematic code
except ValueError as error:
    print(f"Error: {error}")
else:
    print("No exception was raised.")
finally:
    print("This code will always be executed.")
```

**Types of Built-in Exceptions:** Python provides many built-in exceptions such as ValueError, TypeError, FileNotFoundError, etc., which are specific to certain situations. These exceptions can be used to detect and handle particular errors.

**Error Handling:** Error handling involves anticipating potential errors, detecting them, and responding appropriately. This improves code robustness by avoiding unexpected program halts.

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Error: Please enter an integer for age.")
```

**Exception Propagation:** If an exception is not handled locally within a try/except block, it is propagated up the call stack until it is handled or until the program stops in the absence of handling.

**Creating Custom Exceptions:** Developers can create their own custom exceptions by defining classes that inherit from the Exception class. This allows for raising exceptions specific to the application.

```python
class MyCustomException(Exception):
    pass

raise MyCustomException("This is my own exception.")
```

In summary, exceptions in Python are an essential mechanism for handling exceptional situations in a controlled way, enhancing the robustness, reliability, and maintainability of programs.

----------

## ➤ Resources:

Read or watch:

* [Errors and Exceptions](https://intranet.hbtn.io/rltoken/WxV68L6c_WRMEzZt8P7oIA)
* [Learn to Program 11 Static & Exception Handling (starting at minute 7)](https://intranet.hbtn.io/rltoken/OTYmJ8UpJotqIVyrVgSL4A)

----------

## ➤ General:

* Why Python programming is awesome ?
* What’s the difference between errors and exceptions ?
* What are exceptions and how to use them ?
* When do we need to use exceptions ?
* How to correctly handle an exception ?
* What’s the purpose of catching exceptions ?
* How to raise a builtin exception ?
* When do we need to implement a clean-up action after an exception ?

## ➤ Requirements:

General

* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using `wc`

----------

## ➤ Tasks:

### 0. Safe list printing

Write a function that prints x elements of a list.

* Prototype: def safe_print_list(my_list=[], x=0):
* my_list can contain any type (integer, string, etc.)
* All elements must be printed on the same line followed by a new line.
* x represents the number of elements to print
* x can be bigger than the length of my_list
* Returns the real number of elements printed
* You have to use try: / except:
* You are not allowed to import any module
* You are not allowed to use len()

<details>
<summary>Tests</summary>

```python
amandine@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

amandine@ubuntu:~/$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
amandine@ubuntu:~/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-exceptions
* File: 0-safe_print_list.py

----------
  
### 1. Safe printing of an integers list

Write a function that prints an integer with `"{:d}".format()`.

* Prototype: `def safe_print_integer(value):`
* `value` can be any type (integer, string, etc.)
* The integer should be printed followed by a new line
* Returns `True` if `value` has been correctly printed (it means the `value` is an integer)
* Otherwise, returns `False`
* You have to use `try: / except:`
* You have to use `"{:d}".format()` to print as integer
* You are not allowed to import any module
* You are not allowed to use `type()`

<details>
<summary>Tests</summary>

```python
amandine@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

amandine@ubuntu:~/$ ./1-main.py
89
-89
School is not an integer
amandine@ubuntu:~/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-exceptions
* File: 1-safe_print_integer.py

----------
  
### 2. Print and count integers

Write a function that prints the first x elements of a list and only integers.

* Prototype: `def safe_print_list_integers(my_list=[], x=0):`
* `my_list` can contain any type (integer, string, etc.)
* All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
* `x` represents the number of elements to access in `my_list`
* `x` can be bigger than the length of `my_list` - if it’s the case, an exception is expected to occur
* Returns the real number of integers printed
* You have to use `try: / except:`
* You have to use `"{:d}".format()` to print an integer
* You are not allowed to import any module
* You are not allowed to use `len()`

<details>
<summary>Tests</summary>

```python
amandine@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

amandine@ubuntu:~/$ ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "//2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
amandine@ubuntu:~/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-exceptions
* File: 2-safe_print_list_integers.py

----------
  
### 3. Integers division with debug

Write a function that divides 2 integers and prints the result.

* Prototype: def safe_print_division(a, b):
* You can assume that a and b are integers
* The result of the division should print on the finally: section preceded by Inside result:
* Returns the value of the division, otherwise: None
* You have to use try: / except: / finally:
* You have to use "{}".format() to print the result
* You are not allowed to import any module

<details>
<summary>Tests</summary>

```python
amandine@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

amandine@ubuntu:~/$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
amandine@ubuntu:~/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-exceptions
* File: 3-safe_print_division.py

----------
  
### 4. Divide a list

Write a function that divides element by element 2 lists.

* Prototype: `def list_division(my_list_1, my_list_2, list_length):`
* `my_list_1` and `my_list_2` can contain any type (integer, string, etc.)
* `list_length` can be bigger than the length of both lists
* Returns a new list (length = `list_length`) with all divisions
* If 2 elements can’t be divided, the division result should be equal to `0`
* If an element is not an integer or float:
 * print: `wrong type`
* If the division can’t be done (`/0`):
 * print: `division by 0`
* If `my_list_1` or `my_list_2` is too short
 * print: `out of range`
* You have to use `try: / except: / finally:`
* You are not allowed to import any module

<details>
<summary>Tests</summary>

```python
amandine@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

amandine@ubuntu:~/$ ./4-main.py
[5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]
amandine@ubuntu:~/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-exceptions
* File: 4-list_division.py

----------
  
### 5. Raise exception

Write a function that raises a type exception.

* Prototype: `def raise_exception():`
* You are not allowed to import any module

<details>
<summary>Tests</summary>

```python
amandine@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

amandine@ubuntu:~/$ ./5-main.py
Exception raised
amandine@ubuntu:~/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-exceptions
* File: 5-raise_exception.py

----------

### 6. Raise a message

Write a function that raises a name exception with a message.

* Prototype: `def raise_exception_msg(message=""):`
* You are not allowed to import any module

<details>
<summary>Tests</summary>

```python
amandine@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)

amandine@ubuntu:~/$ ./6-main.py
C is fun
amandine@ubuntu:~/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-exceptions
* File: 6-raise_exception_msg.py

----------

## ➤ Author:

- Khadija AASSI