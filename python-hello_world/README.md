![Python - Hello, World](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFjbX8IXMiGZrzUlNI2ipKtdAdLApDDL7KkA&usqp=CAU)

----------

# <p align="center">Python - Hello, World</p>

----------

## ➤ Menu:

* [➤ Description](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-hello_world#-description)
* [➤ Author’s disclaimer](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-hello_world#-authors-disclaimer)
* [➤ Resources](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-hello_world#-resources)
* [➤ Requirements](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-hello_world#-requirements)
* [➤ More Info](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-hello_world#-more-info)
* [➤ Tasks](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-hello_world#-tasks)
* [➤ Author](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-hello_world#-author)

----------

### ➤ Author’s disclaimer:

Welcome to the Python world!

You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Python has a linter / style guide, called PEP8, also now known as PyCode. At Holberton, we won't start off with using PyCode, because it's much more strict compared to PEP8. Don't worry if you see a warning when you are running PEP8, you can ignore it.

Enjoy!

Guillaume

----------

## ➤ Resources:

Read or watch:

Use this playlist as long as you are learning Python:

* [Learn to Program](https://intranet.hbtn.io/rltoken/n9ts_nUw1YtCR9BZtGrHdQ)

* [Whetting Your Appetite](https://intranet.hbtn.io/rltoken/9w2S6R8vtwlmQcPg33445w)

* [Using the Python Interpreter](https://intranet.hbtn.io/rltoken/O87tA-o6pQ8HXAl93xxGGA)

* [An Informal Introduction to Python(Read up until “3.1.2. Strings” included)](https://intranet.hbtn.io/rltoken/x1m4AhQ1Vy9eUBaXFLRHPQ)

* [How To Use String Formatters in Python 3](https://intranet.hbtn.io/rltoken/dd7bIKsC3_0wb3Np_8URUA)

* [Pycodestyle – Style Guide for Python Code](https://intranet.hbtn.io/rltoken/qHCPZY23PoEBaDVce2P0nw)

----------

## ➤ General:

* How to use the Python interpreter ?
To use the Python interpreter :

Install Python: Download and install the latest version from https://www.python.org/downloads/.

Open the terminal: Launch the terminal (or command prompt) and type python or python3.

Python prompt: The >>> prompt indicates that you are in the Python interpreter.

Enter commands: Enter Python commands such as print("Hello, World!").

Exit the interpreter: Type exit() or quit(), or use Ctrl + Z (Windows) or Ctrl + D (Linux/Mac).

The Python interpreter lets you quickly execute commands to test code ideas.

* How to print text and variables using print ?
To print text and variables in Python with `print` :

1. Use `print("Hello")` to display text.

2. Use commas to print variables with text, such as `print("Hello", name)`.

3. Concatenate strings with `+`, for example `print("I'm " + str(age) + " years old")`.

4. Use f-strings to embed variables in a string, like `print(f "Hi, {firstname}")`.

* How to use strings ?
Using strings in Python :

1. **Create :** Use ' ', " ", or ''' ''' to define strings.

2. **Access :** Index for characters, e.g. `mot[0]` for 'P'.

3. **Splitting:** Splitting notation, e.g. `phrase[8:14]` for "Python".

4. **Concatenation :** `+` to join strings, e.g. `firstname + " " + lastname`.

5. **Length :** `len()` for length, e.g. `len("Python")` for 6.

6. **Methods :** Use methods such as `upper()`, `lower()`, etc.

* What are indexing and slicing in Python ?
In Python, indexing allows access to a specific element in a sequence with `sequence[index]`, while slicing extracts a portion with `sequence[start:end]`. These techniques are crucial for manipulating sequences such as strings, lists and tuples. Indexing starts at 0, negative indices count from the end, and slicing uses a range (inclusive:exclusive). Understanding these concepts is essential for working efficiently with sequential data in Python.

* What is the official Python coding style and how to check your code with pycodestyle ?
The official Python coding style, defined in PEP 8, recommends the use of four-space indentation, limiting line width to 79 characters for code and 72 characters for comments and docstrings, organized imports, spaces around operators, and the use of docstrings for documentation.

To check compliance with PEP 8 style, use `pycodestyle` :
1. Install `pycodestyle` with `pip install pycodestyle`.
2. Check a file or directory with `pycodestyle path_to_your_code`.

Respecting this style contributes to the consistency and readability of Python code, facilitating collaboration within the development community. shorter summary

* What is the "Zen of Python"?
The this in Python module contains the "Zen of Python", a series of language design principles. These principles, written by Tim Peters, guide developers towards the creation of readable, elegant and efficient Python code. To display these principles, use import this in a Python script.

## ➤ Requirements:

**Python Scripts**

* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.*)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file at the root of the repo, containing a description of the repository
* A `README.md` file, at the root of the folder of this project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using `wc`

----------

## ➤ More Info:

**Pycodestyle**

`Pycodestyle` is now the [new standard of Python style code](https://intranet.hbtn.io/rltoken/-kju7-n2p8pzvgvgbmAyPw)

----------

## ➤ Tasks:

### 0. Hello, print

Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

* Use the function print

<details>
<summary>Tests</summary>

```python

khadija@ubuntu:~/py/$ ./2-print.py 
"Programming is like building a multilingual puzzle
khadija@ubuntu:~/py/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-hello_world
* File: 2-print.py

----------

### 1. Print integer

Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

* You can find the source code here
* The output of the script should be:
 * the number, followed by Battery street,
 * followed by a new line
* You are not allowed to cast the variable number into a string
* Your code must be 3 lines long
* You have to use f-strings tips

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
khadija@ubuntu:~/py/0x00$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-hello_world
* File: 3-print_number.py

----------

### 2. Print float

Complete the source code in order to print the float stored in the variable `number` with a precision of 2 digits.

* You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/4-print_float.py)
* The output of the program should be:
 * `Float:`, followed by the float with only 2 digits
 * followed by a new line
* You are not allowed to cast `number` to string
* You have to use f-strings

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
khadija@ubuntu:~/py/0x00$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-hello_world
* File: 4-print_float.py

----------

### 3. Print string

Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

* You can find the source code here
* The output of the program should be:
 * 3 times the value of str
 * followed by a new line
 * followed by the 9 first characters of str
 * followed by a new line
* You are not allowed to use any loops or conditional statement
* Your program should be maximum 5 lines long

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/py/$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
khadija@ubuntu:~/py/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-hello_world
* File: 5-print_string.py

----------

### 4. Play with strings

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/6-concat.py) to print `Welcome to Holberton School!`

* You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/6-concat.py)
* You are not allowed to use any loops or conditional statements.
* You have to use the variables `str1` and `str2` in your new line of code
* Your program should be exactly 5 lines long

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/py/$ ./6-concat.py
Welcome to Holberton School!
khadija@ubuntu:~/py/$ wc -l 6-concat.py
5 6-concat.py
khadija@ubuntu:~/py/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-hello_world
* File: 6-concat.py

----------

### 5. Copy - Cut - Paste

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/7-edges.py)

* You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/7-edges.py)
* You are not allowed to use any loops or conditional statements
* Your program should be exactly 8 lines long
* `word_first_3` should contain the first 3 letters of the variable `word`
* `word_last_2` should contain the last 2 letters of the variable `word`
* `middle_word` should contain the value of the variable `word` without the first and last letters

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/py/$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
khadija@ubuntu:~/py/$ wc -l 7-edges.py
8 7-edges.py
khadija@ubuntu:~/py/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-hello_world
* File: 7-edges.py

----------

### 6. Create a new sentence

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/8-concat_edges.py) to print `object-oriented programming with Python`, followed by a new line. 

* You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/8-concat_edges.py)
* You are not allowed to use any loops or conditional statements
* Your program should be exactly 5 lines long
* You are not allowed to create new variables
* You are not allowed to use string literals

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/py/$ ./8-concat_edges.py
object-oriented programming with Python
khadija@ubuntu:~/py/$ wc -l 8-concat_edges.py
5 8-concat_edges.py
khadija@ubuntu:~/py/$
```
</details>

Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: python-hello_world
File: 8-concat_edges.py

----------

### 7. Easter Egg

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

* Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/py/$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
khadija@ubuntu:~/py/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-hello_world
* File: 9-easter_egg.py


----------

## ➤ Author:

- Khadija AASSI