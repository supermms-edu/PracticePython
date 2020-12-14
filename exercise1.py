##Exercise from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

import datetime

nome = input("Hello, what's your name?\n")
idade = int(input("And what is your age?\n"))

x = datetime.datetime.now()
ano = x.year
ano100 = (100-idade)+ano

print("{}, you'll be 100 years old in {}".format(nome,ano100))
