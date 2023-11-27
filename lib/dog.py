#!/usr/bin/env python3

class Dog:
    # Class body goes here
    def bark(self):
        print('Woof!')
        # bark becomes a method for all instances of Dogs

    def sit(self):
        print('The dog is sitting.')

    #Instance method definition
fido = Dog()
snoop = Dog()

fido.bark()
snoop.bark()