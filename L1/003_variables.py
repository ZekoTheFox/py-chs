# [Lesson Header Information]
# Level: Beginner, Newcomer
# Name: "Hello World!"
# Language: Python 3.9.6
# Author: ZekoTheFox, https://github.com/ZekoTheFox
# Requirements: Python Shell
# [Lesson Content Information]
#     In this lesson file, you will learn to create and store values in objects
# known as variables.
# Variables are the way of storing values into a another place, saving it for
# later.
# An analogy for this method of storing values in variables is similar to making
# a book of knowledge. The benefit of this is that we can store all our words
# into one place, and keep it for later use.
# Variables can be inserted into whatever area a constant (1, 2, 3, etc.) can.
# [Lesson Info End]

# Variables can be named whatever you want.
# Capitalization *does* matter, and you'll see that later.
my_variable = 5
# = 5

# You can also assign variables to another variable.
variable_inception = my_variable
# = my_variable (5)

# Reference to the variable for accessing.
# You just simply type the name of the variable *exactly*, otherwise it'll fail.
# Accessing the variable in a function is also possible, as demonstrated here.
# Note how this produces the output [5], as the variable is set to 5 implicitly.
# This is because we set the variable to the first variable, my_variable.
print(variable_inception)
# = "5"

# You can also store letters in a sequence known as a String.
string_variable = "This is my sequence letters."

# String variables can be used just like regular number variables.
print(string_variable)

#print(does_not_exist)
# = NameError: name 'does_not_exist' is not defined

# There are more variable types, however they are not needed as of the moment.