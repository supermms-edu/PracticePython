#Exercise from: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

wrd=input("Please enter a word...\n")

wrd=str(wrd)

rvs=wrd[::-1]
print(rvs.lower())

if wrd.lower() == rvs.lower():
  print("This word is a palindrome!")
else: 
  print("This word is not a palindrome!")
