# Names
from argparse import Namespace


names = ["Harry","Ron","Hermione","Ginny"]

print(names)

val = input("Name :")

names.append(val)

names.sort()

print(names)