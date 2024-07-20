<p align="center">
    <img [Python - Test-driven development] src="https://ik.imagekit.io/6fmwjfqof/blogs/post_1682753333.jpeg?tr=w-600">
</p>

----------

# <p align="center">Python - Test-driven development
</p>

----------

## ➤ Menu:

* [➤ Description](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/tests#-description)
* [➤ Resources](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/tests#-resources)
* [➤ General](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/tests#-general)
* [➤ Requirements](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/tests#-requirements)
* [➤ Tasks](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/tests#-tasks)
* [➤ Author](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/tests#-author)

----------

## ➤ Description:

Test-Driven Development (TDD):

- Design methodology focused on writing tests during code implementation.
- Enables validation, regression prevention and documentation.
- Incremental baby-step design with unit tests for each expected behavior.
- Focus on writing the minimum code to pass tests successfully.
- Promotes improved code quality.

Refactoring :

- Continuous process of improving code without changing its external behavior.
- Promotes clean code with clear naming, detection and correction of code smells, application of design patterns, etc.

Difficulties :

- Testability of project architecture, discipline required, etc.
- Kata" discipline to practice and improve skills.

Advantages:

- Better testability of implementation.
- Reduced mental workload.
- More fun and rewarding.

The three A's - Arrange, Act, Assert - are fundamental principles of unit testing methodology, often used in software development to guarantee code quality. Here is a detailed explanation of each step (starting with the last and ending with the first).

* **3. Arrange (Given - Prepare)** :
    - This step involves setting up the initial conditions required to run the test. This may include initializing variables, configuring the test environment, creating objects or data structures, etc. The aim is to ensure that the code to be tested is placed in a predictable and controlled context.
* **2. Act (When)** :
    - Once the test environment is ready, this step involves executing the specific action or behavior you wish to test. This could be calling a function, manipulating data, interacting with a user interface, or any other operation that the code is expected to perform under normal conditions of use.
* **1. Assert (Then - Affirm)** :
    - In this last step, you check the results of the action performed in the previous step. You compare the results obtained with the expected results to ensure that the code's behavior is as expected. If the results match, the test is considered successful. If not, there's probably a problem in the code that needs to be corrected.

- Fake it till you make it: Write minimal code that passes the tests, even if it's not correct. Then iterate to improve it until the test passes.
- Assert first: Start by writing the assertion (verification of expected results) before writing the code under test.
- Triangulate: Add additional test cases to clarify expected behavior and guide code implementation.


----------

## ➤ Resources:

Read or watch:

* [doctest — Test interactive Python examples](https://intranet.hbtn.io/rltoken/Hmd_LI8NZ-F2ymDxue5HCg) (until “26.2.3.7. Warnings” included)
* [doctest – Testing through documentation](https://intranet.hbtn.io/rltoken/fbFfGNFU07L2yD0D1uc-Xg)
* [Unit Tests in Python](https://intranet.hbtn.io/rltoken/LhbdUZYzqiP7cjxjE3rG3w)

----------

## ➤ General:

* Why Python programming is awesome
* What’s an interactive test
* Why tests are important
* How to write Docstrings to create tests
* How to write documentation for each module and function
* What are the basic option flags to create tests
* How to find edge cases

## ➤ Requirements:

**Python Scripts**

* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using `wc`

**Python Test Cases**

* Allowed editors: `vi`, `vim`, `emacs`
* All your files should end with a new line
* All your test files should be inside a folder `tests`
* All your test files should be text files (extension: .txt)
* All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!

----------

## ➤ Tasks:

### 0. Integers addition

Write a function that adds 2 integers.

* Prototype: `def add_integer(a, b=98):`
* `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
* `a` and `b` must be first casted to integers if they are float
* Returns an integer: the addition of `a` and `b`
* You are not allowed to import any module

<details>
<summary>Tests</summary>

```python
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
guillaume@ubuntu:~/$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
guillaume@ubuntu:~/$
```

</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-test_driven_development
* File: 0-add_integer.py, tests/0-add_integer.txt

----------
  
### 1. Divide a matrix

Write a function that divides all elements of a matrix.

* Prototype: `def matrix_divided(matrix, div):`
* `matrix` must be a list of lists of integers or floats, otherwise raise a `TypeError` exception with the message matrix must be a `matrix (list of lists) of integers/floats`
* Each row of the `matrix` must be of the same size, otherwise raise a `TypeError` exception with the message `Each row of the matrix must have the same size`
* `div` must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
* `div` can’t be equal to `0`, otherwise raise a `ZeroDivisionError` exception with the message `division by zero`
* All elements of the matrix should be divided by `div`, rounded to 2 decimal places
* Returns a new matrix
* You are not allowed to import any module

<details>
<summary>Tests</summary>

```python
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

guillaume@ubuntu:~/$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/$
```

</details>

Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-test_driven_development
* File: 2-matrix_divided.py, tests/2-matrix_divided.txt

----------
  
### 2. Say my name

Write a function that prints `My name is <first name> <last name>`

* Prototype: `def say_my_name(first_name, last_name=""):`
* `first_name` and `last_name` must be strings otherwise, raise a `TypeError` exception with the message `first_name must be a string` or `last_name must be a string`
* You are not allowed to import any module

<details>
<summary>Tests</summary>

```python
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/$
```

</details>

Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-test_driven_development
* File: 3-say_my_name.py, tests/3-say_my_name.txt

----------
  
### 3. Print square

Write a function that prints a square with the character #.

* Prototype: `def print_square(size):`
* `size` is the size length of the square
* `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
* if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* if `size` is a float and is less than 0, raise a `TypeError` exception with the message `size must be an integer`
* You are not allowed to import any module

<details>
<summary>Tests</summary>

```python
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")

guillaume@ubuntu:~/$ ./4-main.py
####
####
####
####

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


#

size must be >= 0

guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/4-print_square.txt
guillaume@ubuntu:~/$
```

</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-test_driven_development
* File: 4-print_square.py, tests/4-print_square.txt
  
----------

### 4. Text indentation

Write a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`

* Prototype: `def text_indentation(text):`
* `text` must be a string, otherwise raise a `TypeError` exception with the message `text must be a string`
* There should be no space at the beginning or at the end of each printed line
* You are not allowed to import any module

<details>
<summary>Tests</summary>

```python
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

guillaume@ubuntu:~/$ ./5-main.py | cat -e
Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
Quonam modo?$
$
Utrum igitur tibi litteram videor an totas paginas commovere?$
$
Non autem hoc:$
$
igitur ne illud quidem.$
$
Fortasse id optimum, sed ubi illud:$
$
Plus semper voluptatis?$
$
Teneo, inquit, finem illi videri nihil dolere.$
$
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
Si id dicis, vicimus.$
$
Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
Sin aliud quid voles, postea.$
$
Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
Utinam quidem dicerent alium alio beatiorem! Iam ruinas videresguillaume@ubuntu:~/$
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/5-text_indentation.txt
guillaume@ubuntu:~/$
```

</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-test_driven_development
* File: 5-text_indentation.py, tests/5-text_indentation.txt
  
----------

### 5. Max integer - Unittest

Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function `def max_integer(list=[]):`.

* Your test file should be inside a folder `tests`
* You have to use the [unittest module](https://intranet.hbtn.io/rltoken/0a3DSCMIMni_V7pgq1myLQ)
* nYour test file should be python files (extension: `.py`)
* Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`
* All tests you make must be passable by the function below
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

<details>
<summary>Tests</summary>

```python
guillaume@ubuntu:~/$ cat 6-max_integer.py
#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ ./6-main.py
4
4
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1
OK
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ head -7 tests/6-max_integer_test.py 
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
guillaume@ubuntu:~/$
```

</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-test_driven_development
* File: tests/6-max_integer_test.py

----------

## ➤ Author:

- Khadija AASSI