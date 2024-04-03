#Exersise 1-1
#1
"Hello World!"
'Hello World!'
#hello world!
SyntaxError: invalid syntax
"Hello World!
SyntaxError: unterminated string literal (detected at line 1)

#2
("hello world!")
'hello world!'
("hello world)
 
SyntaxError: unterminated string literal (detected at line 1)
("Hello world!"

#3
>>> type(2)
 
SyntaxError: '(' was never closed
(2)
 
2
(2)+(2)
 
4
(-2)-2
 
-4
(2++2)
 
4
4
(02)
 
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
02+4
 
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
2+2
 4

5
(3)(4)
 
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    (3)(4)
TypeError: 'int' object is not callable
