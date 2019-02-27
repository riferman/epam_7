#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Create a class “Car” that counts how many cars it has produced.
#
# Let all the cars have 5 wheels (4 driving and 1 spare) and black color by default.
#
# Red cars should have only 4 wheels (no spare wheels for red cars! J).
#
# All cars must have a method called “diag”, that prints out the color of the car and its wheels count.
#
# Mind the ‘__init__’ method.


__author__ = "Sergey_Matusevich"


class Car(object):
    quantity = 0

    def __init__(self, spare, color):
        Car.quantity += 1  # machine count
        self.spare = spare
        self.color = color
        self.wheels = 4

    @staticmethod
    def print_quantity():
        print(Car.quantity)

    def diag(self):
        print(self.color)
        print(self.wheels + self.spare)


black = Car(1, "black")
black.diag()
Car.print_quantity()

red = Car(0, "red")
red.diag()
Car.print_quantity()
