# Tools-Python-
Small Programs with Specific Uses

Python Function name: RemoveOutliers
  Example Usage:
    offset = 10
    noMoreOutliers=[]
    noMoreOutliers = RemoveOutliers(inputs,offset)  
  Inputs: 
    Array of non-negative numbers unsorted, 
    Offset in percent (5, or 10 or 1) of values on ends to ignore.  
      For example an input of 10 for the offset will remove the values in the inputs that are less than the p10 and greater than 
      the p90 values.
  Assumes distribution is normal. Linear scale for numbers
