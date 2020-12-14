##https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

examplelist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

##Exercise
for i in examplelist:
  if i<5:
    print(i)


#Extras 1 and 2
newlist = [x for x in examplelist if x<5]
print(newlist)

#Extra 3
cutline = int(input("Enter the cutline\n"))
newlist2 = [x for x in examplelist if x<cutline]
print(newlist2)
