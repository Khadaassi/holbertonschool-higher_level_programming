<p align="center">
    <img [Python - Data Structures: Lists, Tuples] src="https://cdn.educba.com/academy/wp-content/uploads/2019/06/Python-Tuple-vs-List.jpg">
</p>

----------

# <p align="center">Python - Data Structures: Lists, Tuples</p>

----------

## ➤ Menu:

* [➤ Description](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-data_structures#-description)
* [➤ Resources](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-data_structures#-resources)
* [➤ General](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-data_structures#-general)
* [➤ Requirements](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-data_structures#-requirements)
* [➤ Tasks](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-data_structures#-tasks)
* [➤ Author](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/python-data_structures#-author)

----------

## ➤ Description:

**Lists:**

Definition: A list is an ordered, mutable data structure that can contain a collection of elements of different types.

Syntax: Defined using square brackets [], with elements separated by commas.

**Features:

Mutable: The elements of a list can be modified after its creation.
Indexing: List elements can be accessed by their index, starting with 0.
Operations: Supports various operations such as adding, deleting, concatenating and trimming.

Use: Lists are commonly used to represent collections of elements where order and mutability are important. They are versatile and flexible.


**Tuples:**

Definition: A tuple is an ordered, immutable data structure that can contain a collection of elements of different types.

Syntax: Defined using parentheses (), with elements separated by commas.

**Features:

Immutable: Once created, a tuple cannot be modified.
Indexing: Tuple elements can be accessed by their index, starting with 0.
Limited operations: Due to their immutability, operations on tuples are limited compared with lists.

Use: Tuples are often used to represent fixed data records, coordinates, or any other context where immutability is desirable.

In short, lists are suitable when you have a collection of items that may change over time, while tuples are appropriate for immutable data records. The choice between the two depends on the specific needs of your application.

----------

## ➤ Resources:

Read or watch:

* [3.1.3. Lists](https://intranet.hbtn.io/rltoken/UCQlbIrhZJVRfxndAcskkw)
* [Data structures (until 5.3. Tuples and Sequences included)](https://intranet.hbtn.io/rltoken/89W42byWTSM4e25VSPKMRg)
* [Learn to Program 6 : Lists](https://intranet.hbtn.io/rltoken/JNLdadDW7IWjwW9dbcEyhg)

----------

## ➤ General:

* What are lists and how to use them ?
* What are the differences and similarities between strings and lists ?
* What are the most common methods of lists and how to use them ?
* How to use lists as stacks and queues ?
* What are list comprehensions and how to use them ?
* What are tuples and how to use them ?
* When to use tuples versus lists ?
* What is a sequence ?
* What is tuple packing ?
* What is sequence unpacking ?
* What is the del statement and how to use it ?

----------

## ➤ Requirements:

Python Scripts

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

### 0. Import a simple function from a simple file

0. Print a list of integers

Write a function that prints all integers of a list.

* Prototype: `def print_list_integer(my_list=[]):`
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

khadija@ubuntu:~/$ ./0-main.py
1
2
3
4
5
khadija@ubuntu:~/$
```
</details>


Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-data_structures
* File: 0-print_list_integer.py

----------
 
### 1. Secure access to an element in a list
mandatory
Write a function that retrieves an element from a list.

Prototype: `def element_at(my_list, idx):`
If `idx` is negative, the function should return `None`
If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
You are not allowed to import any module
You are not allowed to use `try/except`

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

khadija@ubuntu:~/$ ./1-main.py
Element at index 3 is 4
khadija@ubuntu:~/$
```
</details>


Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-data_structures
* File: 1-element_at.py

----------
 
### 2. Replace element

Write a function that replaces an element of a list at a specific position.

* Prototype: `def replace_in_list(my_list, idx, element):`
* If `idx` is negative, the function should not modify anything, and returns the original list
* If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
* You are not allowed to import any module
* You are not allowed to use `try/except`

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

khadija@ubuntu:~/$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
khadija@ubuntu:~/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-data_structures
* File: 2-replace_in_list.py
 
### 3. Print a list of integers... in reverse!

----------

Write a function that prints all integers of a list, in reverse order.

* Prototype: `def print_reversed_list_integer(my_list=[]):`
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

khadija@ubuntu:~/$ ./3-main.py
5
4
3
2
1
khadija@ubuntu:~/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-data_structures
* File: 3-print_reversed_list_integer.py

----------
 
4. Replace in a copy

Write a function that replaces an element in a list at a specific position without modifying the original list.

* Prototype: `def new_in_list(my_list, idx, element):`
* If `idx` is negative, the function should return a copy of the original `list`
* If `idx` is out of range (> of number of element in `y_list`), the function should return a copy of the original `list`
* You are not allowed to import any module
* You are not allowed to use `try/except`

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

khadija@ubuntu:~/$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
khadija@ubuntu:~/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-data_structures
* File: 4-new_in_list.py

----------
 
### 5. Can you C me now?

Write a function that removes all characters `c` and `C` from a string.

* Prototype: `def no_c(my_string):`
* The function should return the new string
* You are not allowed to import any module
* You are not allowed to use `str.replace()`

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

khadija@ubuntu:~/$ ./5-main.py
Best Shool
hiago
 is fun!
khadija@ubuntu:~/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-data_structures
* File: 5-no_c.py

----------
 
### 6. Lists of lists = Matrix

Write a function that prints a matrix of integers.

* Prototype: `def print_matrix_integer(matrix=[[]]):`
* Format: see example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

khadija@ubuntu:~/$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
khadija@ubuntu:~/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-data_structures
* File: 6-print_matrix_integer.py

----------
 
### 7. Tuples addition

Write a function that adds 2 tuples.

* Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
* Returns a tuple with 2 integers:
 * The first element should be the addition of the first element of each argument
 * The second element should be the addition of the second element of each argument
* You are not allowed to import any module
* You can assume that the two tuples will only contain integers
* If a tuple is smaller than 2, use the value `0` for each missing integer
* If a tuple is bigger than 2, use only the first 2 integers

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

khadija@ubuntu:~/$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
khadija@ubuntu:~/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-data_structures
* File: 7-add_tuple.py

----------
 
### 8. More returns!

Write a function that returns a tuple with the length of a string and its first character.

* Prototype: `def multiple_returns(sentence):`
* If the sentence is empty, the first character should be equal to `None`
* You are not allowed to import any module

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

khadija@ubuntu:~/$ ./8-main.py
Length: 22 - First character: A
khadija@ubuntu:~/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-data_structures
* File: 8-multiple_returns.py

----------
 
### 9. Find the max

Write a function that finds the biggest integer of a list.

* Prototype: `def max_integer(my_list=[]):`
* If the list is empty, return `None`
* You can assume that the list only contains integers
* You are not allowed to import any module
* You are not allowed to use the builtin max()

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

khadija@ubuntu:~/$ ./9-main.py
Max: 90
khadija@ubuntu:~/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-data_structures
* File: 9-max_integer.py

----------
 
### 10. Only by 2

Write a function that finds all multiples of 2 in a list.

* Prototype: `def divisible_by_2(my_list=[]):`
* Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
* The new list should have the same size as the original list
* You are not allowed to import any module

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/$ cat 10-main.py
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

khadija@ubuntu:~/$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
khadija@ubuntu:~/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-data_structures
* File: 10-divisible_by_2.py

----------
 
### 11. Delete at

Write a function that deletes the item at a specific position in a list.

* Prototype: `def delete_at(my_list=[], idx=0):`
* If `idx` is negative or out of range, nothing change (returns the same list)
* You are not allowed to use `pop()`
* You are not allowed to import any module

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/$ cat 11-main.py
#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

khadija@ubuntu:~/$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
khadija@ubuntu:~/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-data_structures
* File: 11-delete_at.py

----------
 
### 12. Switch

Complete the source code in order to switch value of `a` and `b`

* You can find the source code [here](https://intranet.hbtn.io/rltoken/9viUCbnIwdfsOPV_UrvIRA)
* Your code should be inserted where the comment is (line 4)
* Your program should be exactly 5 lines long

<details>
<summary>Tests</summary>

```python
khadija@ubuntu:~/py/$ ./12-switch.py
a=10 - b=89
khadija@ubuntu:~/py/$ wc -l 12-switch.py
5 12-switch.py
khadija@ubuntu:~/py/$
```
</details>

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: python-data_structures
* File: 12-switch.py

----------

## ➤ Author:

- Khadija AASSI