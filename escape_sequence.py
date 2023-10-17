""" Escape characters or sequences are illegal characters for python and never get printed as part of the output.
When backslash is used in python. It allows the programs to escape the next characters.
\' ->  Single quotation
\" -> Double quotation
\\ ->  Backslash
\n -> newline
\t -> tab
\b-> backspace"""

print("Hello World")
print("This is Python classes.")

print("Hello World\nThis is Python classes.")
print("My name is Vaibhav\nMy age is 25\nMy gender is Male")

print("This is\t\t\tPython classes")
#output:- This is		Python classes

print("This is \"python classes\"")
#output:- This is "python classes"

print("Hello\\This is python classes")

print("Hello\b This is python classes")


#Assigment Questions
""" Q1:Write a program that prints a path like this:
C:\John\Desktop\File.txt
using the appropriate escape sequences.

Q2.
Write a Python program that prints a message with a double-quote character inside it.
For example: He said, "Hello!".

Q3.
Create a program that prints a message containing both single and double quotes, like this:
She said, 'It's cold'.
"""

# print("C:\\Users\\John\\Desktop\\file.txt")
# print("He said,\"Hello\"")
# print("She said,\'It's cold\'")