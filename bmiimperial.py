# -*- coding: utf-8 -*-
"""biometric

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1677a8FNuUbuzGFG59sv_DD2H1XY6zeoY
"""

#requests user enter weight
print("Please enter weight in pounds:")
weight = int(input()) * 0.453592 

#requests user enter height
print("Please enter height in inches:")
height = float(input()) * 0.0254 

#calculates BMI
BMI = weight / (height*height)

#prints BMI
print("BMI is:", BMI)