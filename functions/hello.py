#!/usr/bin/python3

def hello(name):
    print(f"Hello {name}")

# hello("Ven")

def year_of_birth(name, age):
    year = 2024 - age
    print(f"Hello {name} you were born in {year}")

# year_of_birth("Lavender", 22)


def my_country(country="Uganda"):
    print(f"Hello Akirachix from {country}")



# def get_count(sentence):
#     lower = []
#     upper = []

#     for i in sentence:
#         if i.islower():
#             lower.append(i)
#         elif i.isupper():
#             upper.append(i)
#     return f'Upper = {len(upper)}, Lower = {len(lower)}'

# print(get_count("AkiraChix"))


def greet(*names):
    for name in names:
        print(f"Hello {name}")



def create_sentence(**words):
    print(words)
    sentence = ""
    for word in words.values():
        sentence+= word
        sentence+= " "
    return sentence

print(create_sentence(a="I", b="Love", c="Python", d="and", e="Javascript"))


def sum_and_greet(*args, **kwargs):
    total = 0
    for x in args:
        total += x

    f = kwargs["firstname"]
    l = kwargs["lastname"]

    greeting = f"Hello {f} {l} total of your numbers is {total}"
    return greeting

print(sum_and_greet(20, 40, 40, firstname="Ven", lastname="Akida"))
print(sum_and_greet(100, 300, 650, 8000, firstname="Nakato", lastname="Musana", contry="Kenya", email="musana@gmail.com" ))
print(sum_and_greet(100,firstname="Ben", lastname="Ten"))