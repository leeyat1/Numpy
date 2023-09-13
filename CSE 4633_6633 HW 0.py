#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!
# 
# In this notebook, you will learn what jupyter notebooks are, get a refresher on python and learn some libraries/frameworks which may be useful for future assignments. At the end of the notebook you will complete some simple functions as a practice assignment.

# # Table of contents
# 
# 0. [Setup](#setup)
# 1. [What is Jupyter?](#jupyter)
# 2. [Interface and Hotkeys](#interface)
# 3. [Python Refresher](#python)
# 4. [Numpy Basics](#numpy)
# 5. [Practice Questions](#practice)
# 6. [Acknowledgements](#acknowledgements)

# <a name="setup"/></a> <!-- link used in table of contents -->
# ## Setup
# 
# There are a few options that you can consider to develop and run AI code using Jupyter notebooks. First, make sure that you have watched the tutorial videos on Canvas (Jupyter notebook tutorial and Google Colab tutorial). Then, you may proceed with one of the setup options below: 
# 
# 1. Local installation
# 
# The Jupyter notebook environment can be installed on your personal computer by following the instructions here: https://jupyter.org/install
# 
# To run one of the Jupyter notebook homework assignments given in this class, start the Jupyter notebook server by executing the command "jupyter notebook" on your terminal / command prompt, then select your notebook file on your web browser interface.
# 
# 2. Google Colaboratory
# 
# Google Colaboratory (Google Colab) is a free Jupyter notebook environment that requires no setup and runs entirely in the cloud. With Colaboratory you can write and execute code, save and share your analyses, and access powerful computing resources, all for free from your browser. Here is an example notebook that can be run on Google Colab: https://colab.research.google.com/drive/16pBJQePbqkz3QFV54L4NIkOn1kwpuRrj. To run one of the Jupyter notebook homework assignments given in this class, simply upload it to your Google Drive, and select "Open with" -> "Google Colaboratory".

# <a name="jupyter"/></a> <!-- <-this link used in table of contents -->
# ## What are Jupyter notebooks?

# ![Jupyter Logo](https://raw.githubusercontent.com/jupyter/jupyter.github.io/master/assets/share.png)
# 
# Jupyter notebooks are an interactive tool for iterative development and prototyping. When learning new concepts it is helpful to be able to look at intermediary results, take notes in Markdown/LaTeX, and have visualizations. All this is possible to achieve using jupyter notebooks.

# In some of the future assignments, notebooks will be used to guide you through the assignment. The main purpose of using notebooks is to reduce the steep learning curve, help you get started quickly by walking you through basic examples, and expose you to APIs used in the assignments. This way, you can focus on understanding the concepts rather than digging down into the implementation details of unrelated bits of code. Jupyter is also very useful when you are debugging things, since you can easily check/modify the content of your variables, without having to rerun all of your code.

#  

# ### Cell types 
# Every jupyter notebook consists of cells. Cells come in different types. For the most part, you need to just know two types of cells: Markdown and Code. You can change the type of a cell by clicking on the cell and selecting the type in the toolbar above (Cell>Cell Type). By default all new cells are `Code` type.

# In **Markdown** cells you can provide comments, format them, and write LaTeX. This cell you are reading right now is a [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) cell. To edit it, you can select it and press 'Enter' or just double click it with your mouse. Once you are done editing it, you can press `⇧↩` (Shift + Enter) to render it as Markdown.

# In **Code** cells you can write code. You can write single or multiple lines of code and you can execute them by pressing `⇧↩` (Shift + Enter).

#  

# ### Basic example
# 
# Now, let's start with some simple examples and write some basic python. Use `⇧↩` (Shift + Enter) to run the cells below. You can either use a mouse to select the cells or use arrow keys to move the selection window consecutively over cells (you will learn more about how to navigate soon).

# In[ ]:


1+1


# In[ ]:


a = 10


# In[ ]:


a


# In[ ]:


a + 5


# In[ ]:


a


# Note that you don't need to write
# ```python
# print(a)
# ```
# Simply executing the variable will output its value. This only works for the last variable name written. To print multiple variables, you need to explicitly use print.

# In[ ]:


x = 1
y = 2
z = 3
x
y
z


# In[ ]:


print(x)
print(y)
print(z)


# One important aspect of jupyter notebooks is that cells can be executed out-of-order. This can be confusing to newcomers. 
# 
# Let's walk through a simple example:

# In[ ]:


# Initialize counter to zero
counter = 0


# Run the `counter += 1` cell multiple times:

# In[ ]:


# Run this cell multiple times
counter += 1


# Let's see what's the counter is now:

# In[ ]:


counter


# Thus, it is not the order that the cells are presented in, but rather the order in which cells are executed that determines the current variable state. Now let's talk about what the kernel does, and what saving the notebook means.

#  

# ### Kernels
# 
# The Kernel is a computational engine which runs behind the notebook and executes code. Jupyter supports over 40 programming languages, including Python, R, Julia, and Scala. The associated kernels can be setup separately and you can also switch between the different kernels, but we won't need to do it in this class as we will only use the Python kernel.

# In the Kernel tab in the toolbar above you should be able to see multiple commands that you can send to the kernel. Here are descriptions of some of them:
# 
# * **Interrupt** - stops the execution of the code (helpful when you have a long operation but forget to change some parameter, or in case you have an infinite loop)
# * **Restart** - clears up all of the variables and releases memory
# * **Restart & Clear Output** - restarts the kernel + clears all of the cell outputs in the notebook
# * **Restart & Run All** - restarts the kernel + executes all of the cells

# It's important to note that kernel state can not be saved, i.e. if you stop/restart the kernel you will need to rerun all of the cells to define the variables. **Restart & Clear Output** is often the best option for beginners to use when restarting the kernel, since it is easy to get confused by the previous outputs. 

# For example, consider the following situation:
# 
# <img src="./misc/uncleared_cell.png" alt="uncleared_cell" width="700"/>
# 
# Here, the first cell containing the variable declaration was executed before the kernel was restarted. However, the output associated with the previous kernel state was not cleared when restarting. Once the kernel was restarted, running the second cell produced an error despite the first cell's output indicating that the variable was defined. In order to access any variable you need to make sure the variable is defined in the current kernel state, even if you see some output associated with the cell that defines the variable.

# ---

# ### Signatures and Docstrings
# 
# Here are a couple of other things you can do in jupyter. You will find these particularly handy when you will start working on the assignments and want to learn the signatures, docstrings and/or source code of certain classes or functions.

# Run the next two cells:

# In[ ]:


# Let's define a function
def print_something(n_times=2):
    """This function shows a greeting message!"""
    assert n_times > 0
    for _ in range(n_times):
        print("Hello from Jupyter!")


# In[ ]:


# Add ? at the end of the function to see its docstring
get_ipython().run_line_magic('pinfo', 'print_something')


# In[ ]:


# Same could be achieved if you place the cursor at the end of function name and press ⇧⇥ (Shift + Tab)
print_something


# There are times you might want to look into the source code of a class/function. You can do it by adding `??` after the class/function name.

# In[ ]:


get_ipython().run_line_magic('pinfo2', 'print_something')


# It also works for any classes/functions defined outside the notebook.

# In[ ]:


import numpy as np
get_ipython().run_line_magic('pinfo2', 'np.ones')


# In[ ]:


# Another way is to place a cursor at the end of the function/class name 
# and press ⇧⇥⇥ (Shift + Tab + Tab) to show you the docstring
np.ones


# ---
# 
# ### Magic commands
# 
# Jupyter has a number of [magic commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html) you can use (to list all of the magic functions run: `%lsmagic`). You already used one of them above. It was `%run script_name`, which can be used to run `*.py` scripts inside the notebook. This is equivalent to running ``python script_name`` in the terminal. 

# Let's try out the `%time` magic command, which measures the execution time of a cell or line of code. It will be useful in future assignments. For example if you are optimizing the execution speed of your code, you can use this magic command to time different approaches. Here are two ways you can use `%time`:
# 
# * `%time` - to time a single line of code; **OR**
# * `%%time` - to time the whole cell
# 
# Here is an example detailing how `%time` can be used:

# In[ ]:


import random


# Let's create an array of random integers and time it:

# In[ ]:


get_ipython().run_cell_magic('time', '', '# will time whole cell\nrandom_integers = []\nfor _ in range(10000):\n    random_integers.append(random.randint(0,100))\n')


# Now, let's time the same operation using list comprehension instead:

# In[ ]:


get_ipython().run_line_magic('time', 'random_integers = [random.randint(0,100) for _ in range(10000)] # will time only this line')


# In the next example, we use `%timeit` to compare a standard python vs numpy implementation of scalar multiplication operation on a 1D array. Note that `%timeit` and `%time` are slightly different. You can read about the differences and about other magic commands [here](https://ipython.readthedocs.io/en/stable/interactive/magics.html).

# In[ ]:


n_items = 1000000
# Create two identical arrays
integer_list = list(range(n_items))
integer_array = np.arange(n_items)
# make sure both 1D arrays are exactly the same
assert np.allclose(integer_list, integer_array, rtol=0.0)


# In[ ]:


def scalar_mult_1D(somelist):
    # inplace operation
    for index, value in enumerate(somelist):
        somelist[index] = 2 * value
    return somelist


# In[ ]:


def np_scalar_mult_1D(nplist):
    return 2*nplist


# In[ ]:


get_ipython().run_line_magic('timeit', 'scalar_mult_1D(integer_list)')


# In[ ]:


get_ipython().run_line_magic('timeit', 'np_scalar_mult_1D(integer_array)')


# In[ ]:


integer_list = list(range(n_items))
integer_array = np.arange(n_items)
integer_list_2x = scalar_mult_1D(integer_list)
integer_array_x2 = np_scalar_mult_1D(integer_array)
# make sure the resultant arrays are the same
assert np.allclose(integer_list, integer_array_x2, rtol=0.0)


# As you can see, for this simple task python arrays are ~100x slower. You will learn more about numpy later on in the class. For now, we will stick to standard python.

# ---

# <a name="interface"/></a> <!-- <-this link used in table of contents -->
# # Interface and Hotkeys
# 
# To learn more about the interface and about jupyter notebooks in general, check out the `Help` section in the menu.
# 
# Here is the TL;DR version of what you should know.

# ---
# ## Modal editor
# 
# There are two modes in the jupyter: edit mode and command mode.
# 

# ### Edit
# Edit mode is indicated by a green cell border and a prompt showing in the editor area:
# 
# ![edit_image.png](https://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/images/edit_mode.png)
# 
# You can press **Enter** to enter edit mode or click with a mouse in the editable area.

# ### Command
# Command mode is indicated by a grey cell border:
# 
# ![command_image.png](https://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/images/command_mode.png)
# 
# Use **Esc** to enable command mode or click outside the editable area of a cell with a mouse.
# 
# When you are in command mode, you can edit the notebook as a whole, but you cannot type into individual cells. Most importantly, the keyboard is mapped to a set of shortcuts that let you perform notebook and cell actions efficiently. For example, if you are in command mode and you press `c`, you will copy the current cell - no modifier is needed.
# 

# ## Hotkeys
# 
# There are a lot of useful hotkeys in jupyter. You can see them all in (Help > Keyboard Shortcuts).
# 
# Here is a list of the ones that will save you the most time. You can use these in both command and edit mode and they will perform the same action.
# 
# * **Shift + Enter** - Run cell + select next cell
# * **Alt + Enter** - Run cell + insert new cell below
# 
# Here are hotkeys you can use in command mode only.
# * **a** - Insert cell above
# * **b** - Insert cell below
# * **Shift + Up-Down Arrow key** or **Shift + mouse click cells** - select multiple cells.
# * **x** - Cut the selected cell(s)
# * **c** - Copy the selected cell(s)
# * **v** - Paste the selected cell(s)
# * **m** - Convert the cell to markdown (after your run the markdown cell, you can double click it to edit)
# * **y** - Convert the cell back to code

# <a name="python"/></a> <!-- link used in table of contents -->
# ## Python
# 
# If you are not at all familiar with Python, start learning! Although you can use any tutorial you like, here are a couple to get you started:
# * [A beginner’s guide](https://wiki.python.org/moin/BeginnersGuide)
# * [An interactive track in CodeAcademy](https://www.codecademy.com/learn/learn-python-3)
# 
# Below are a number of cells you can run to get a quick refresher on Python.

# ####variable names

# Variable names in Python can contain alphanumerical characters a-z, A-Z, 0-9 and some special characters such as _. Normal variable names must start with a letter.
# 
# By convention, variable names start with a lower-case letter, and Class names start with a capital letter.
# 
# In addition, there are a number of Python keywords that cannot be used as variable names. These keywords are:
# 
# `and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield`
# 
# 

# The assignment operator in Python is =. Python is a dynamically typed language, so we do not need to specify the type of a variable when we create one. Assigning a value to a variable name creates the variable. If we assign a new value to a variable, its type can change.

# #### int/float operations

# In[ ]:


some_int = 2
some_float = 4.
print(type(some_int))
print(type(some_float))


# In[ ]:


some_int + some_float


# In[ ]:


some_int * some_float


# In[ ]:


some_int / some_float


# In[ ]:


# note that in Python 3, division with / results in float
2/4 


# In[ ]:


# integer division can be done with //
2 // 4


# In[ ]:


# other mathematical operators

# modulo / remainder
print(5 % 2) # remainder of 5 divided by 2

# exponent
print(5 ** 3) # 5 to the power of 3


# ####boolean operations

# In[ ]:


# boolean
b1 = True
b2 = False
type(b1)


# In[ ]:


# boolean operators
print(b1 and b2)
print(b1 or b2)
print(not b1)


# In[ ]:


# comparison operations result in boolean values
print(2 > 1)
print(2 < 1)
print(2 >= 2)
print(2 <= 2)
print([1,2] == [1,2])


# #### string operations

# In[ ]:


# strings can be created by enclosing text in single quotes or double quotes
some_string = "Hello "
print(type(some_string))


# In[ ]:


some_string + "world!" # you can concatenate strings with + operator


# In[ ]:


some_string


# We can extract a part of a string using the syntax [start:stop], which extracts characters between index start and stop -1 (the character at index stop is not included). If we omit either (or both) of start or stop from [start:stop], the default is the beginning and the end of the string, respectively. Note that Python indexing always starts from 0.

# In[ ]:


some_string[:2]


# In[ ]:


some_string[-2:]


# In[ ]:


some_string[-3:-1]


# In[ ]:


# C-style string formatting
print('%s %10s %d %.3f' % ('hello', 'world', 12, -3.501924))  


# In[ ]:


# Python-style string formatting
print('value1 = {0}, value2 = {1}'.format(3.1415, 1.5)) 
print('Hey {name}, there is a 0x{errno:x} error!'.format(name='Bob', errno=1235019))


# In[ ]:


# f-Strings (Python 3.6+)
a = 5
b = 10
print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')


# #### Array/List operations

# In[ ]:


some_array = [] # new empty array/list


# In[ ]:


some_array


# In[ ]:


some_array.append(11)
some_array.append(12)
some_array.append(13)
some_array.append(20)


# In[ ]:


some_array


# In[ ]:


some_array.pop()


# In[ ]:


some_array


# In[ ]:


some_array[1] # indexing lists starts from 0


# In[ ]:


some_array[1] = 22


# In[ ]:


some_array # lists are mutable


# We can use the same indexing techniques to manipulate lists as we could use on strings

# In[ ]:


some_array[1:3]


# Lists play a very important role in Python. For example they are used in loops and other flow control structures (discussed below). There are a number of convenient functions for generating lists of various types, for example the range function. Note that in Python 3 range generates an interator, which can be converted to a list using 'list(...)'.

# In[ ]:


print(range(10))
print(list(range(10)))
print(list(range(5, 10)))
# start = 10, stop = 30, step = 2
print(list(range(10, 30, 2)))


# #### tuples
# 
# The key difference between tuples and lists is that while tuples are immutable objects, lists are mutable. This means that tuples cannot be changed while lists can be modified. Tuples are fixed-sized whereas lists can dynamically grow / shrink.

# In[ ]:


some_tuple = (1,2,3) 


# In[ ]:


some_tuple[1]


# In[ ]:


some_tuple[1] = 123 # tuples are immutable (you will get an error)


# In[ ]:


# The only way to modify tuple is to convert it to array/list and then back to tuple
temp_list = list(some_tuple)
temp_list[1] = 123
some_tuple = tuple(temp_list)
some_tuple


# ####set
# A set is an unordered collection of distinct elements. 

# In[ ]:


animals = {'cat', 'dog'}
print(type(animals))
print('cat' in animals)   # Check if an element is in a set; prints "True"
print('fish' in animals)  # prints "False"
animals.add('fish')       # Add an element to a set
print('fish' in animals)  # Prints "True"
print(len(animals))       # Number of elements in a set; prints "3"
animals.add('cat')        # Adding an element that is already in the set does nothing
print(len(animals))       # Prints "3"
animals.remove('cat')     # Remove an element from a set
print(len(animals))       # Prints "2"


# #### dictionaries
# 
# Dictionaries are Python's implementation of a data structure that is more generally known as an associative array. A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value

# In[ ]:


some_dict = {}
some_dict['name'] = "Alice"
some_dict['age'] = "21"
some_dict


# In[ ]:


some_dict['name']


# In[ ]:


some_dict.keys()


# In[ ]:


some_dict.values()


# In[ ]:


for key, value in some_dict.items():
    print(f"{key} - {value}")


# ####control flow
# 
# The Python syntax for conditional execution of code uses the keywords if, elif (else if), else.

# In[ ]:


statement1 = False
statement2 = False

if statement1:
    print("statement1 is True")
    
elif statement2:
    print("statement2 is True")
    
else:
    print("statement1 and statement2 are False")


# One very important aspect of Python to note is that program blocks are defined by their **indentation level**. Refer to how the print statements are indented in the code cell above. This is also relevant for loops and functions which we will see later. In languages such as C/C++ the level of indentation (white space before the code statements) does not matter (completely optional). But in Python, the extent of a code block is defined by the indentation level (usually a tab or say four white spaces). This means that we have to be careful to indent our code correctly, or else we will get syntax errors.

# #### loops

# The for loop iterates over the elements of the supplied object, and executes the containing block once for each element. Any kind of iterable object (e.g. list, tuple, dictionary) can be used in the for loop.

# In[ ]:


# For loops
for i in [10,20,30,40]:
    print(i)


# In[ ]:


# More for loops
for i in range(5):
    print(f"square of {i} is {i**2}")


# In[ ]:


some_dict = {1:"one", 2:"two"}
for i in some_dict:
  print(i, some_dict[i])


# In[ ]:


# While loops
i=0
while i < 5:
    print(f"square of {i} is {i**2}")
    i+=1


# In[ ]:


some_array = []
for i in range(5):
    some_array.append(i**3)
some_array


# #### list comprehensions
# 
# List comprehensions can be used to make for loops more concise

# In[ ]:


some_array = [i**3 for i in range(5)]
some_array


# In[ ]:


# List comprehensions can also contain conditions
even_numbers = [i for i in range(25) if i%2 == 0]
even_numbers


# #### functions
# 
# A function in Python is defined using the keyword def, followed by a function name, a signature within parentheses (), and a colon :. The following code, with one additional level of indentation, is the function body.

# In[ ]:


def some_function(some_arg):
    print(f"Argument is: {some_arg}")


# In[ ]:


some_function(1)


# In a definition of a function, we can give default values to the arguments the function takes.

# In[ ]:


def some_function(some_arg=42): # default values
    print(f"Argument is: {some_arg}")


# In[ ]:


some_function()


# In[ ]:


some_function(some_arg=25)


# We can return multiple values from a function

# In[ ]:


def powers(x):
    """
    Return a few powers of x.
    """
    return x ** 2, x ** 3, x ** 4
  
powers(3)


# In[ ]:


x2, x3, x4 = powers(3)

print(x3)


# Here are some commonly used built-in functions in Python:

# In[ ]:


print(sum([1,2,3])) # sum
print(min([1,2,3])) # minimum
print(max([1,2,3])) # maximum
print(len([1,2,3])) # length


# #### classes
# 
# Classes are a key feature of object-oriented programming. A class is a structure for representing an object and the operations that can be performed on the object.
# 
# In Python a class can contain attributes (variables) and methods (functions).
# 
# A class is defined almost like a function, but using the class keyword, and the class definition usually contains a number of class method definitions (a function in a class).
# 
# Each class method should have an argument `self` as its first argument. This object is a self-reference.
# 
#     Some class method names have special meaning, for example:
#         __init__: The name of the method that is invoked when the object is first created.
#         __str__ : A method that is invoked when a simple string representation of the class is needed, as for example when printed.

# In[ ]:


class SomeClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_a(self):
        return self.a
    def get_b(self):
        return self.b


# In[ ]:


my_object = SomeClass(10,100)
my_object.get_b()


# #### function pass by reference

# In[ ]:


def some_function():
    return 42

def print_function_output(fn):
    print(fn())

print_function_output(some_function) # note that some_function has not executed here


# #### unpacking

# In[ ]:


# Using asterisk to pack the rest of the output
def foo():
    return 1,2,3,4,5,6,7

a, *_ = foo() # in case you are interested only in the first value returned
a


# ####modules
# 
# To use a module in a Python program it first has to be imported. A module can be imported using the import statement. For example, to import the module math, which contains many standard mathematical functions, we can do:

# In[ ]:


import math
x = math.cos(2 * math.pi)
print(x)


# Once a module is imported, we can list the symbols it provides using the `dir` function.

# In[ ]:


dir(math)


# And using the function `help` we can get a description of each function (not all functions will have docstrings, but the vast majority of functions are documented this way).

# In[ ]:


help(math.log)


# #### Nobody is perfect. A few Python quirks

# In[ ]:


def foo(a=[]):
    a.append(1)
    print(a)


# In[ ]:


foo()


# In[ ]:


foo()


# In[ ]:


foo()


# For more details and how to avoid it, see: [https://docs.python-guide.org/writing/gotchas/](https://docs.python-guide.org/writing/gotchas/)

# Here is another quirk:

# In[ ]:


a = 0
for i in range(10000000):
    a += 0.1
print(a)


# The problem is an approximation of 0.1. The true decimal value of the binary approximation stored by the machine is:
# ```python
# > 0.1
# 0.1000000000000000055511151231257827021181583404541015625
# ```
# The error in the approximation accumulates as you sum up many 0.1s. See here for more detail: https://docs.python.org/3.4/tutorial/floatingpoint.html

# And yet another quirk, that students have trouble with quite often in the assignments for this class:

# In[ ]:


a = [1,2]
b = a
b.append(3)
print(a)
print(b)


# The last case happens because the lists/arrays are passed by reference. You can avoid it using the following technique:

# In[ ]:


import copy
a = [1,2]
b = copy.copy(a)
b.append(3)
print(a)
print(b)


# ### Debugger
# 
# You can use debuggers within jupyter. There are two available by default: `%pdb` & `%debug`. We won't be covering those here. There are multiple tutorials available online that you can reference.
# * https://davidhamann.de/2017/04/22/debugging-jupyter-notebooks/
# * https://www.blog.pythonlibrary.org/2018/10/17/jupyter-notebook-debugging/
# 
# There are also visual third party debuggers that you can try: 
# * https://www.analyticsvidhya.com/blog/2018/07/pixie-debugger-python-debugging-tool-jupyter-notebooks-data-scientist-must-use/.

# <a name="numpy"/></a> <!-- <-this link used in table of contents -->
# ## NumPy
# 
# Numpy is one of the most important libraries you will be using for numerical computing in Python. Numpy provides support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
# 
# A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. The number of dimensions is the rank of the array; the shape of an array is a tuple of integers giving the size of the array along each dimension.

# In[ ]:


import numpy as np

a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"


# Numpy also provides many functions to create arrays:

# In[ ]:


import numpy as np

a = np.zeros((2,2))   # Create an array of all zeros
print(a)              # Prints "[[ 0.  0.]
                      #          [ 0.  0.]]"

b = np.ones((1,2))    # Create an array of all ones
print(b)              # Prints "[[ 1.  1.]]"

c = np.full((2,2), 7)  # Create a constant array
print(c)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"

d = np.eye(2)         # Create a 2x2 identity matrix
print(d)              # Prints "[[ 1.  0.]
                      #          [ 0.  1.]]"

e = np.random.random((2,2))  # Create an array filled with random values
print(e)                     # Might print "[[ 0.91940167  0.08143941]
                             #               [ 0.68744134  0.87236687]]"


# Numpy offers several ways to index into arrays. Similar to Python lists, numpy arrays can be sliced. Since arrays may be multidimensional, you must specify a slice for each dimension of the array.

# In[ ]:


import numpy as np

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]

# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
print(a[0, 1])   # Prints "2"
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])   # Prints "77"


# **Integer array indexing:** When you index into numpy arrays using slicing, the resulting array view will always be a subarray of the original array. In contrast, integer array indexing allows you to construct arbitrary arrays using the data from another array. Here is an example:

# In[ ]:


import numpy as np

a = np.array([[1,2], [3, 4], [5, 6]])

# An example of integer array indexing.
# The returned array will have shape (3,) and
print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"

# The above example of integer array indexing is equivalent to this:
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Prints "[1 4 5]"

# When using integer array indexing, you can reuse the same
# element from the source array:
print(a[[0, 0], [1, 1]])  # Prints "[2 2]"

# Equivalent to the previous integer array indexing example
print(np.array([a[0, 1], a[0, 1]]))  # Prints "[2 2]"


# One useful trick with integer array indexing is selecting or mutating one element from each row of a matrix:

# In[ ]:


import numpy as np

# Create a new array from which we will select elements
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])

print(a)  # prints "array([[ 1,  2,  3],
          #                [ 4,  5,  6],
          #                [ 7,  8,  9],
          #                [10, 11, 12]])"

# Create an array of indices
b = np.array([0, 2, 0, 1])

# Select one element from each row of a using the indices in b
print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"

# Mutate one element from each row of a using the indices in b
a[np.arange(4), b] += 10

print(a)  # prints "array([[11,  2,  3],
          #                [ 4,  5, 16],
          #                [17,  8,  9],
          #                [10, 21, 12]])


# **Boolean array indexing:** Boolean array indexing lets you pick out arbitrary elements of an array. Frequently this type of indexing is used to select the elements of an array that satisfy some condition. Here is an example:

# In[ ]:


import numpy as np

a = np.array([[1,2], [3, 4], [5, 6]])

bool_idx = (a > 2)   # Find the elements of a that are bigger than 2;
                     # this returns a numpy array of Booleans of the same
                     # shape as a, where each slot of bool_idx tells
                     # whether that element of a is > 2.

print(bool_idx)      # Prints "[[False False]
                     #          [ True  True]
                     #          [ True  True]]"

# We use boolean array indexing to construct a rank 1 array
# consisting of the elements of a corresponding to the True values
# of bool_idx
print(a[bool_idx])  # Prints "[3 4 5 6]"

# We can do all of the above in a single concise statement:
print(a[a > 2])     # Prints "[3 4 5 6]"


# Basic mathematical functions operate elementwise on arrays, and are available both as operator overloads and as functions in the numpy module:

# In[ ]:


import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))

# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))


# Note that for numpy.array objects, * is elementwise multiplication, not matrix multiplication. We instead use the dot function or the @ operator to compute inner products of vectors, to multiply a vector by a matrix, and to multiply matrices. dot is available both as a function in the numpy module and as an instance method of array objects:

# In[ ]:


import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))
print(v @ w)

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))
print(x @ v)

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))
print(x @ y)


# ---

# <a name="practice"/></a> <!-- <-this link used in table of contents -->
# ## Practice Questions

# In[2]:


# Question 1: Find the sum of all odd numbers between 1 and 99 (inclusive).
nums = []
i = 0
sum = 0
while i <= 99:
    nums.append(i)
    sum += i
    i+=1
print(sum)


# In[3]:


# Question 2: The population of a town starts at 100.
#   Each year, the population grows by 50% (rounded down to the nearest integer).
#   Calculate the number of years it takes for the population to exceed 2000.

population = 100
year = 0

while population <= 2000:
    population = population + (population/2)
    year += 1

print(year)


# In[3]:


# Question 3: Write a function that takes an input x (number of seconds)
# and returns 4 numbers, namely the number of days, hours, minutes, and seconds
# that is represented by the input.
# e.g. f(100) should return 1 minute 40 seconds
#       f(1000000) should return 11 days 13 hours 46 minutes 40 seconds

import math


def calTime(x):
    days = math.floor(x / 86400)
    x = x % 86400
    hours = math.floor(x/3600)
    x = x % 3600
    minutes = math.floor(x/60)
    x = x % 60
    print(days, "days", hours, "hours", minutes, "minutes", x, "seconds")
    
calTime(1000000)


# In[2]:


# Question 4: Write a function that takes in two lists of integers
#     and returns the integers that are in both lists
#     e.g. f([1,2,3], [2,3,5,6]) should return [2,3]
a = [1,2,3]
b = [2,3,5,6]

def findMatching(list1, list2):
    ans = []
    storage = set(num for num in list2)
    for val in list1:
        if val in storage:
            ans.append(val)
    return ans


# In[1]:


# Question 5: Create a NumPy array with 10 rows and 3 columns.
#   The first column should be all zeros
#   The second column should be all ones
#   The third column should be all fives
import numpy as np 

a=np.zeros((10,3))
a[:,:1] = 0
a[:,1:2] = 1
a[:,2:3] = 5

print(a)


# In[23]:


# Question 6: Using NumPy, count the number of positive numbers in each of the following lists:
import numpy as np

L1 = [5, -10, 4, 9, -3, -1, 3, 9, 4, 6]
L2 = [[-8, -8, 9], [-1, -3, 4], [ 1, -5, -9]]
L3 = [[[-4, 3], [-1, -1]], [[ 6, 1], [-4, -7]]]


a= np.array(L1)
bool_idx = (a>0)
print(np.count_nonzero(bool_idx))
a= np.array(L2)
bool_idx = (a>0)
print(np.count_nonzero(bool_idx))
a= np.array(L3)
bool_idx = (a>0)
print(np.count_nonzero(bool_idx))


# In[45]:


# Questions 7: The following NumPy array represents a table of weather data where
#   each row represents a city and each column represents the temperature at a particular day  
#   Calculate the mean and standard deviation in temperature for each city

import numpy as np
temperatures = np.array([ [61.7, 73.4, 74.4, 60.9, 63.2, 63.1, 73.3, 73.7, 79.4, 77.3],
                          [78.1, 67.7, 62. , 78.5, 62.9, 78.2, 75.8, 74.6, 76. , 66.1],
                          [76.8, 79.7, 63.6, 70.5, 74.3, 61.5, 76.3, 61.3, 66.7, 73. ],
                          [73.6, 77.7, 68.5, 65.4, 77.3, 62.4, 69.5, 71.2, 64.4, 76. ],
                          [78.8, 62.8, 63.8, 77.9, 68.7, 66.6, 69.3, 68.5, 61.9, 71.9]])


a = temperatures[0:10][0]
b = temperatures[0:20][1]
c = temperatures[0:30][2]
d = temperatures[0:40][3]
e = temperatures[0:50][4]

x=np.mean(a) 
y=np.std(a)
print('City 1\n Mean:',x,'\nStandard Deviation:', y)
x=np.mean(b) 
y=np.std(b)
print('City 2\n Mean:',x,'\nStandard Deviation:', y)
x=np.mean(c) 
y=np.std(c)
print('City 3\n Mean:',x,'\nStandard Deviation:', y)
x=np.mean(d) 
y=np.std(d)
print('City 4\n Mean:',x,'\nStandard Deviation:', y)
x=np.mean(e) 
y=np.std(e)
print('City 5\n Mean:',x,'\nStandard Deviation:', y)


# ---

# <a name="acknowledgements"/></a> <!-- <-this link used in table of contents -->
# # Acknowledgements
# 
# The examples and exercises given in this Jupyter notebook are compiled from the following sources:
# 
# 1. https://github.gatech.edu/omscs6601/assignment_0
# 2. https://cs231n.github.io/python-numpy-tutorial/
# 3. https://github.com/iitmcvg/Python-Exercises/blob/master/Exercise%201%20-%20Python.ipynb

# ---
# <!-- Hi there! -->
