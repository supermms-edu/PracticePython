## Exercise from  https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

x = int(input("Enter a number\n"))
y = int(input("Enter a number again\n"))
 
 
if x%y == 0:
  print("{} is evenly divisible by {}".format(x,y))
else:
  print("Oops! {} is not evenly divisible by {}".format(x,y))
  

