#-------------------------------------------------------------------------
# Name:		    Lesson 5.7 Break & Continue
# Purpose:		Bike Frame Size Example - Use loop and break/continue
# Author:		  
# Created:		06/05/2024
#-------------------------------------------------------------------------

size = int(input("Enter the frame size (cm): "))

if size > 60:
  print("The bike is too big!!")
elif size < 55:
  print("The bike is too small!")
else:
  print("The bike is the correct size.")