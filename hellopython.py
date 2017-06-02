import random
import sys
import os

print('hello world')

name = 'Schuman'
print(name)

name = 15

#5 major data types: numbers, strings, lists, tuples, dictionaries
#7 opeartors: + - * / % ** // 

#exponential
print('5 ** 2 = ', 5 ** 2)

#divide and discard remainder
print('5 // 2 = ', 5 // 2)

#lets look at a list
grocery_list = ['Juice', 'Tomatoes', 34, 'Apples']

print('first item', grocery_list[0])

grocery_list[0] = 'Green Juice'

#select subsets of a list
print(grocery_list[1: 3]) #print from 1 to 3, not including 3

other_events = ['Wash car', 'Pick up kids', 'Cash check']

#2 lists inside a new list
to_do_list = [other_events, grocery_list]

print(to_do_list)

#print 2nd item from 2nd list
print((to_do_list[1][1]))

#appending
grocery_list.append('Onions')
print(to_do_list)

#insert in a particular index and misc list operations
grocery_list.insert(1, 'Pickle')

grocery_list.remove('Pickle')

grocery_list.sort()

grocery_list.reverse()

#delete an item
del grocery_list[4]
print(to_do_list)

#combining lists
to_do_list2 = other_events + grocery_list

#get length, max and min
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

#Tuples - not changeable after created
#tuple convert to list
pi_tuple = (3,1,4,1,5,9)

new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

len(tuple)
min(tuple)
max(tuple)

#Dictionaries or maps, values and unique key
#you cannot join dictionaries

super_villains = {'Fiddler': 'Issac Bowin', 'Captain Cold': 'Leonard Snart', 'Weather Wizard': 'Mark Mardon'}

#select by key
print(super_villains['Captain Cold'])

#removing an entry
del super_villains['Fiddler']

#replace value
super_villains['Captain Cold'] = 'Hello world'

print(len(super_villains))

#getting key and value
print(super_villains.get('Weather Wizard'))

#getting just the keys
print(super_villains.keys())

#getting just the values
print(super_villains.values())

#conditionals are if, else, elif, == != > >= <=

age = 21

if age > 16 :
    print('you are old enough to drive')
else :
    print('you are not old enough to drive')

if age >= 21 :
    print('yo')
elif age >= 16 :
    print('sdfs')
else :
    print('whatever')


if ((age >= 1) and (age <= 18)) :
    print('you get a birthday')
elif ((age == 21) or (age >= 65)) :
    print('You get a little birthday')
elif not (age == 30) :
    print('You do not get a birthday')
else :
    print('you get a birthday')

#Loops

#loop 10 times, 0 to 9
for x in range(0, 10) :
    print(x, '', end='')

# for loop
for y in grocery_list:
    print(y)

for x in [2,3,6,8,10]:
    print(x)

num_list = [[1, 2, 3], [10, 20, 30]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

#while loops - when you don't know how many times to loop
random_num = random.randrange(0, 100)

while (random_num != 15): 
    print(random_num)
    random_num = random.randrange(0, 100)

i = 0

while(i <= 20):
    if(i % 2 == 0):
        print(i)
    elif(i == 9):
        break
    else: 
        i += 1
        continue
    
    i += 1

#functions
def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum

print(addNumber(1, 3))

#get user's input
print('What is your name?')

name = sys.stdin.readline()

print('Hello', name)

#Lets look at strings
long_string = "I'll catch you if you fall"

#print first 4
print(long_string[0: 4])

#print last 5
print(long_string[-5:])

#print everything up to last 5
print(long_string[:-5])

#concatenate or join
print(long_string[:4] + " be there")

print(long_string.find('you'))
print(long_string.isalpha())
print(long_string.replace('you', 'me'))
print(long_string.strip())

quote_list = long_string.split(' ')
print(quote_list)

#File IO

#create and write a file
test_file = open('test.txt', 'wb')

print(test_file.mode)
print(test_file.name)

test_file.write(bytes('Write me to file', 'UTF-8'))

test_file.close()

#read from a file
test_file = open('test.txt', 'r+')

test_file = test_file.read()

os.remove('test.txt')

#Objects in Python
class Animal:
    #__ is private
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    #all setters and getters

    def get_type(self):
        print('Animal')

    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}" .format(self.__name, self.__height, self.__weight, self.__sound)

cat = Animal('Whiskers', 33, 10, 'meow')

print(cat.toString())

#Inheritance, class Dog inherits from Animal
class Dog(Animal):
    __owner = ''

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)



    