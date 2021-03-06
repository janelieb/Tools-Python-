# -*- coding: utf-8 -*-
#Automatically generated by Colaboratory.

#given a list of numbers return the numbers without outliers. Consider case: list has repeats generally grouped on one side

#my approach is count the amount of integers given, take the top percentile and bottom percentile after sorting as thresholds

#future work:
    #this could be more manipulatable for different scales, log-scale or exponentials
    #This could be tested to work with negative numbers

import math


def RemoveOutliers(inputs, offset):
  #Step 1, sort the input
  sortedInputs=[]
  sortedInputs = inputs.copy()
  sortedInputs.sort()
  count = len(inputs)
  #Step 2 get the min and max thresholds - assume 10% offsets
  offset = offset
  min_index = 0
  max_index = count
  min_value = sortedInputs[0]
  max_value = sortedInputs[count-1]
  lower_index = (offset/100.0)*count
  upper_index = ((100.0-offset)/100.0)*count
  lower_threshold= (sortedInputs[math.floor(lower_index)])
  upper_threshold= (sortedInputs[math.ceil(upper_index)-1])
  #Step 3 create new array and return
  output = []
  for x in sortedInputs:
    if lower_threshold <=x and x<= upper_threshold:
      output.append(x)
  return output





inputsToTest = [1,0,2,1,2,1,3,4,8,21,99,33,2,1,1]
offsetToTest = 5.0
test = RemoveOutliers(inputsToTest, offsetToTest)
for x in test:
  print(x)

