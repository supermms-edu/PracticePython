#Exercise from: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

number = int(input("Enter a number \n"))

list = [x for x in range(1,number+1) if number%x ==0]
print(list)
