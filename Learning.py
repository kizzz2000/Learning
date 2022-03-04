# from datetime import datetime
#
# name = input('What is your name: ')
# age = int(input('How old are you? '))
# birthday = input("when is your birthday? (Month/Day) ")
# year = 1
# total = age + year
# currentYear = datetime.now().year
#
# print(f'Hello, {name}, i see you are {age} years old. You will be {total} on {birthday} {currentYear}')
#


# name = "Chris Stefanski"
#
# first_name = name[:6]
# last_name = name[6:]
# full_name = first_name + last_name
# weird_name = full_name[0:17:2]
# reversed_name = full_name[::-1]
#
# print(first_name)
# print(last_name)
# print(full_name)
# print(weird_name)
# print(reversed_name)

#slicing
# website = "http://google.com"
# website2 = "http://bing.com"
# slice = slice(7,-4)
#
#
# print(website[slice])
# print(website2[slice])

# age = int(input("how old are you? "))
# if age == 100:
#     print('Damn you old!')
# elif age >= 18:
#     print("You are an adult")
# elif age < 0:
#     print('You havnen"t been born yet.')
#
# else:
#     print("you are a child")

# temp = int(input("What is the temp outside? "))
#
# if not(temp >= 0 and temp <= 30):
#     print("the temp is bad today.")
#     print('stay inside')
# elif not(temp < 0 or temp > 30):
#     print("the temp is good today.")
#     print("go outside")
# else:
#     print("not a number")


# age = 15
# of_age = age >= 18
#
# age = input(int("what is your age? "))
# if of_age >= 18:
#     print("you are an adult")
# else:
#     print("you are a child")


# name = None
# while not name:
#     name = input("enter your name: ")
# print(f"Hello {name}")

# for i in range(10):
#     print(i+1)

# for i in range(50,100,5):
#     print(i+1)

# for i in "Chris Stefanski":
#     print(i)

# import time
#
# for seconds in range(10, 0,-1):
#     print(seconds)
#     time.sleep(0.5)
# print("happy new year")

# rows = int(input("how many rows? "))
# columns = int(input("how many columns? "))
# symbol = input("enter a symbol to use. ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# while True:
#     name = input("What is your name? ")
#     if name != "":
#         break

# phone_number = "555-555-5555"
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(0,21):
#     if i == 13:
#         pass
#     else:
#         print(i, end="")

# food = [
#     "pizza",
#     "hot dogs",
#     "your mom"
# ]
#
# food[0] = "your dad"
#
# food.append("ice cream")
# food.remove("your mom")
# food.pop()
# food.insert(1, "cake")
# food.sort()
# food.clear()
#
# for x in food:
#     print(x)

# drinks = ["coffie", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert =["cake", "ice cream"]
#
# food = drinks,dinner,dessert
#
# print(food[1][2])

# student = ("bro", 21, "male")
#
# print(student.count("Bro"))
# print(student.index("male"))
#
# for x in student:
#     print(x)
# if "bro" in student:
#     print("bro is here.")

# silverware = {"fork", "spoon", "knife"}
# dishes = {"bowl","plate","cup","knife"}
#
# dinner_table = silverware.union(dishes)
# print(silverware.intersection(dishes))
# # print(silverware.difference(dishes))
# # silverware.update(dishes)
# # silverware.add("plate")
# # silverware.remove("fork")
# # silverware.clear()
# # for x in dinner_table:
# #     print(x)

# capitals = {"USA":"Washington DC",
#             "India":"New Dehli",
#             "China":"Beijing",
#             "Russha":"Moscow"}
#
# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"LAS VEGAS"})
# capitals.pop("USA")
# capitals.clear()
# # print(capitals[""])
# # print(capitals.get("YOURMOM"))
# # print(capitals.keys())
# # print(capitals.values())
# # print(capitals.items())
#
# for key,value in capitals.items():
#     print(key,value)

# name = "chris Stefanski"
#
# # if(name[0].islower()):
# #     name = name.capitalize()
# first_name = name[:6].upper()
# last_name = name[6:].lower()
# full_name = first_name + last_name
#
# print(full_name)


# def hello(first_name, last_name, age):
#     print(f"hello, {first_name} {last_name} you are {age} damn you old")
#
# hello("Chris","Stefanski",36)

# def multiply(number1, number2):
#     return number1 * number2
#
# x = multiply(6,8)
# print(x)

# def hello(first,middle,last):
#     print(f"Hello {first} {middle} {last}")
#
# hello(last="Stefanski",middle="Stephen",first="Chris")

# num = input("enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)

# print(round(abs(float(input("enter a whole positive number: ")))))

# name = "Chris"
#
# def display_name():
#     name = "Stefanski"
#     print(name)
#
# display_name()
# print(name)

# def add(*args):
#     sum = 0
#     args = list(args)
#     args[0] = 0
#     for i in args:
#         sum += i
#     return sum
# print(add(1,2,3))

# def hello(**kwargs):
#     # print(f"hello, {kwargs['first']} {kwargs['last']}")
#     print("Hello,",end=" ")
#     for key,value in kwargs.items():
#         print(value,end=" ")
# hello(title="Mr",first="Chris",middle="Stephen",last="Stefanski")

# name = "chris"
# print(f"Hello my name is {name:20} I am awesome")
# print(f"Hello my name is {name:<20} I am awesome")
# print(f"Hello my name is {name:>20} I am awesome")
# print(f"Hello my name is {name:^20} I am awesome")

# number = 1000
#
# print(f"the number pi is {number:.2f}")
# print(f"the number is {number:,}")
# print(f"the number is {number:b}")
# print(f"the number is {number:o}")
# print(f"the number is {number:x}")
# print(f"the number is {number:e}")

# import random
#
# x = random.randint(1,6)
# y = random.random()
#
# my_list = ['Rock','paper','Scissors']
# z = random.choice(my_list)
#
# cards = [1,2,3,4,5,6,7,8,9,"j","q","k","A"]
# random.shuffle(cards)
#
# print(y)
# print(x)
# print(z)
# print(cards)
#
# try:
#     numerator = int(input("enter a number to divide: "))
#     denominator = int(input("enter a number to divide by: "))
#     result = numerator / denominator
#
# except ZeroDivisionError as e:
#     print(e)
#     print("You can't divide by zero idiot!")
# except ValueError as e:
#     print(e)
#     print("enter only numbers")
# except Exception as e:
#     print(e)
#     print("something went wrong")
# else:
#     print(result)
# finally:
#     print("This will always work")

# import os
#
# path = "C:\\Users\\d856185\\PycharmProjects\\Learning\\New folder"
#
# if os.path.exists(path):
#     print("that location exists")
#     if os.path.isfile(path):
#         print("that is a file")
#     elif os.path.isdir(path):
#         print("that is a folder")
# else:
#     print("that doesn't exists")

# try:
#     with open('C:\\Users\\d856185\\PycharmProjects\\Learning\\New folder\\text.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("that file was not found")

# text = "\n this is a new line"
#
# with open('C:\\Users\\d856185\\PycharmProjects\\Learning\\New folder\\text.txt','a') as file:
#     file.write(text)

# import shutil
#
# shutil.copyfile('C:\\Users\\d856185\\PycharmProjects\\Learning\\New folder\\text.txt','copy.txt')

# import os
#
# source = "C:\\Users\\d856185\\PycharmProjects\\Learning\\New folder"
# destination = "C:\\Users\\d856185\\OneDrive - Dart\\Desktop\\wallpaper\\New Folder"
#
# try:
#     if os.path.exists(destination):
#         print("there is already a file there.")
#     else:
#         os.replace(source,destination)
#         print(f"{source} was moved")
# except FileNotFoundError:
#     print(f"{source} file not found")

# import os
# import shutil
#
# path = 'C:\\Users\\d856185\\PycharmProjects\\Learning\\New folder'
#
# try:
#     # os.rmdir(path)
#     # os.remove(path)
#     shutil.rmtree(path)
# except FileNotFoundError:
#     print("that file was not found")
# except PermissionError:
#     print("you do not have permisson to delete that")
# except OSError:
#     print("You cannot delete that using that function.")
# else:
#     print(f"{path} was deleted.")

# from messages import hello, bye
#
# hello()
# bye()

# help("modules")

# import random
#
# while True:
#     choices = ["rock","paper","scissors"]
#     player = None
#     computer = random.choice(choices)
#     while player not in choices:
#         player = input("rock, paper, or scissors? ").lower()
#
#     if player == computer:
#         print(f"Computer: {computer}")
#         print("It was a tie.")
#     elif player == "rock":
#         if computer == "paper":
#             print(f"Computer: {computer}")
#             print("you lose.")
#         if computer == "scissors":
#             print(f"Computer: {computer}")
#             print("you win.")
#
#     elif player == "sissors":
#         if computer == "rock":
#             print(f"Computer: {computer}")
#             print("you lose.")
#         if computer == "paper":
#             print(f"Computer: {computer}")
#             print("you win.")
#
#     elif player == "paper":
#         if computer == "scissors":
#             print(f"Computer: {computer}")
#             print("you lose.")
#         if computer == "rock":
#             print(f"Computer: {computer}")
#             print("you win.")
#     play_again = input("Would you like to play again (y/n) ").lower()
#     if play_again != "y":
#         break
# print("Bye")

#=========================
# def new_game():
#
#     guesses = []
#     correct_guesses = 0
#     question_num = 1
#
#     for key in questions:
#         print("")
#         print(key)
#         for i in options[question_num-1]:
#             print(i)
#         guess = input("Enter (A, B, C, or D): ")
#         guess = guess.upper()
#         guesses.append(guess)
#
#         correct_guesses += check_answer(questions.get(key), guess)
#         question_num += 1
#     display_score(correct_guesses, guesses)
# #=========================
# def check_answer(answer, guess):
#     if answer == guess:
#         print("Correct")
#         return 1
#     else:
#         print("wrong")
#         return 0
# #=========================
# def display_score(correct_guesses, guesses):
#     print("-------------")
#     print("Results")
#     print("-------------")
#     print("Answers: ", end=" ")
#     for i in questions:
#         print(questions.get(i), end=" ")
#     print()
#
#     print("Guesses: ", end=" ")
#     for i in guesses:
#         print(i, end=" ")
#     print()
#
#     score = int((correct_guesses/len(questions))*100)
#     print(f"\nyour score is: {score}%")
# #=========================
# def play_again():
#     response = input("Do you want to play again? (y/n) ")
#     response = response.upper()
#     if response == 'Y':
#         return True
#     else:
#         return False
#
# questions = {
#     "\nWho created Python ": "A",
#     "\nWhat year was Python created? ": "B",
#     "\nPython is tributed to which comedy group? ": "C",
#     "\nIs the Earth round? ": "A"
# }
#
# options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
#           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
#           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
#           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]
#
# new_game()
#
# while play_again():
#     new_game()
#
# print("Thanks for playing.")

# from car import Car
#
# car_1 = Car("Dodge", "Neon", "2021", "Red")
# car_2 = Car("Ford", "Mustang", 2022, "Blue")
#
# car_1.drive()
# car_2.stop()

# from car import Car
#
# car_1 = Car("Dodge", "Neon", "2021", "Red")
# car_2 = Car("Ford", "Mustang", 2022, "Blue")
#
# Car.wheels = 2
#
# print(car_1.wheels)
# print(car_2.wheels)

# class Animal: #PARENT CLASS
#
#     alive = True
#
#     def eat(self):
#         print("This animal is eating")
#
#     def sleep(self):
#         print("This animal is sleeping")
#
# class Rabbit(Animal): # CHILD CLASS
#     def run(self):
#         print("This rabbit is running")
#
# class Fish(Animal): # CHILD CLASS
#     def swim(self):
#         print("this fish is swimming")
#
# class Hawk(Animal): # CHILD CLASS
#     def fly(self):
#         print("this hawk is flying")
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
#
# # print(rabbit.alive)
# # fish.eat()
# # hawk.sleep()
#
# rabbit.run()
# fish.swim()
# hawk.fly()

# class Organism:
#
#     alive = True
#
# class Animal(Organism):
#
#     def eat(self):
#         print("This animal is eating")
#
# class Dog(Animal):
#
#     def bark(self):
#         print("this dog is barking.")
#
# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()


# class Prey:
#
#     def flee(self):
#         print("this animal flees")
#
# class Predator:
#
#     def hunt(self):
#         print("this animal is hunting")
#
# class Rabbit(Prey):
#     pass
#
# class Hawk(Predator):
#     pass
#
# class Fish(Prey, Predator):
#     pass
#
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
#
# rabbit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()

# class Animal:
#
#     def eat(self):
#         print("this animla is eating")
#
# class Rabbit(Animal):
#
#     def eat(self):
#         print("The rabbit is eatting carrots")
#
# rabbit = Rabbit()
# rabbit.eat()


# class Car:
#
#     def turn_on(self):
#         print("you start the car")
#         return self
#
#     def drive(self):
#         print("you drive the car")
#         return self
#
#     def brake(self):
#         print("you hit the breaks")
#         return self
#
#     def turn_off(self):
#         print("you turn off the car")
#         return self
# car = Car()
#
# car.turn_on()\
#     .drive()\
#     .brake()\
#     .turn_off()

# class Rectangle:
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
# class Square(Rectangle):
#
#     def __init__(self, length, width):
#         super().__init__(length, width)
#
#     def area(self):
#         return self.length*self.width
#
# class Cube(Rectangle):
#
#     def __init__(self, length, width, height):
#         super().__init__(length, width)
#         self.height = height
#
#     def volume(self):
#         return self.length*self.width*self.height
#
# square = Square(3, 3)
# cube = Cube(3, 3, 3)
#
# print(square.area())
# print(cube.volume())


# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#
#     @abstractmethod
#     def go(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
#
# class Car(Vehicle):
#
#     def go(self):
#         print("you drive the car")
#
#     def stop(self):
#         print("this car is stopped")
#
# class Motorcycle(Vehicle):
#
#     def go(self):
#         print("you ride the motercycle")
#
#     def stop(self):
#         print("this motorcycle is stopped")
#
# # vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()
#
# # vehicle.go()
# car.go()
# motorcycle.go()
#
# car.stop()
# motorcycle.stop()

# class Car:
#
#     color = None
#
# class Motorcycle:
#
#     color = None
#
# def change_color(car, color):
#
#     car.color = color
#
# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
#
# bike_1 = Motorcycle()
#
# change_color(car_1,"red")
# change_color(car_2,"blue")
# change_color(car_3,"yellow")
#
# change_color(bike_1, "black")
#
# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
#
# print(bike_1.color)


# class Duck:
#
#     def walk(self):
#         print("this duck is walking")
#
#     def talk(self):
#         print("this duck is quacking")
#
# class Chicken:
#
#     def walk(self):
#         print("this chicken is walking")
#
#     def talk(self):
#         print("This chicken is clucking")
#
# class Person:
#
#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("you caught the bird")
#
# duck = Duck()
# chicken = Chicken()
# person = Person()
#
# person.catch(chicken)

# happy = True
# print(happy)
#
# print(happy := True)
#
# foods = list()
# while True:
#     food = input("what food do you like? ")
#     if food == "quit":
#         break
#     foods.append(food)
#
# foods = list()
# while food := input("what food do you like? ") != "quit":
#     foods.append(food)

# def hello():
#     print("hello")
#
# # hello = hello
# # hello()
# # hi()
#
# say = print
# say("I am a awesome person :)")

# def loud(text):
#     return text.upper()
#
# def quite(text):
#     return text.lower()
#
# def hello(func):
#     text = func("hElLo")
#     print(text)
#
# hello(loud)

# def divisor(x):
#     def dividend(y):
#         return y / x
#     return dividend
#
# divide = divisor(2)
# print(divide(10))

# def double(x):
#     return x * 2
#
# print(double(5))

# double = lambda x:x * 2
# multiply = lambda x, y: x * y
# add = lambda  x, y, z: x + y + z
# full_name = lambda first_name, last_name: first_name+" "+last_name
# age_check = lambda age:True if age >= 18 else False
#
# print(age_check(17))




















