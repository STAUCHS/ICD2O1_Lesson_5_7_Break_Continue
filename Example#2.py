#-------------------------------------------------------------------------
# Name:		    Lesson 5.7 Break & Continue
# Purpose:		Basic While Loop with Continue
# Author:		  
# Created:		06/05/2024
#-------------------------------------------------------------------------

n = 5

while n > 0:
  if n == 2:
    continue
  print(n)
  n -= 1

print('Loop is finished.')