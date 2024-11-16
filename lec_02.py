'''
 This is lecture number Two. Today we will learn about 
 1. Comments
 2. Variables
 3. Data types

1. Comments
           In python, comments are that piece of code which is ignored by the interpreter. It enhances the redability of code. 

 Comments are of two types 
 a. Single line comment
      when ever we want to comment out single line we use single line comment.
      it can be declared by using hash symbol --> #
 b. multi line comment 
      when ever we want to comment out multiple lines we use multi-line comment.
      it can be declared by triple single quote --> '''     '''

'''

# This is a single line comment 

''' 
    THIS 
    IS  
    MULTI 
    LINE 
    COMMENT
'''

'''
2. Variables
        Variables are the container that stores data values in the computer's memory. In other words we can say that variables are containers for storing data values

        In python a variable is created the moment you first assign a value to it. 
        Example: 
         num = 67

        A variable of name num is created which stores the value 67

Rules to create variable in python
    a. a variable name can contain alpha-numeric characters and underscores ( A-Z , 0-9 , _ ).
    b. variable name must start with a letter(a-z or A-Z) or the underscore ( _ ).
    c. variable name cannot start with a number.
    d. there should not be any space between variable name.
    e. variable name is case sensitive like num=5 and NUM= 5 are two different variables.
    f. Keywords cannot be used as variable names.
        ___________________________
        |  Correct  |  Incorrect  |
        |___________|_____________|
        |  _num     |   %num      |
        |   num     |   1num      |
        |   NUM     |   nu m      |
        |___________|_____________|
'''

'''
Data types : 
    Data types are the classification of data items. It represents the kind of value that tells what operation can be performed on a particular data.

    a.Integers --> it contains positve, negative , 0 without fractions and decimals

    b.Float    --> It is a real number with a floating point representation. it is specified by a decimal point.

    c.Strings --> A string is a collection of one or more characters put in a single,double or triple quote.

    d.Boolean  --> Boolean data type is either True or False

'''

# Program to declare variable and store some values of different data type. 

num_int = 23
num_float= 23.23
data_string = "Hello Prateek"
data_boolean = True


# Now printing the value of variables
print(" This is integer data type : ")
print(num_int)
print(" This is float data type : ")
print(num_float)
print(" This is string data type : ")
print(data_string)
print(" This is boolean data type : ")
print(data_boolean)
print("\n")


# Now printing the type of data 
print(type(num_int))
print(type(num_float))
print(type(data_string))
print(type(data_boolean))