"""
This program describes the function *combine* that accepts two one-dimensional 
lists of integers as parameter and returns another one-dimensional list 
whose element at ith position is the sum of the ith elements returns another one-dimensional list whose element at ith posiBon is the sum of the ith 
elements of the two input lists.
If one of the lists is shorter than the others, then your function should 
consider the “missing” elements to be 0.

Author: Loc Le
    Date: February 2023
"""

def combine(list1, list2):
  len1 = len(list1)
  len2 = len(list2)

  if len1 > len2:
    for i in range(len2, len1):
      list2.append(0)
  else:
    for i in range(len1, len2):
      list1.append(0)

  res = []
  for i in range(len(list1)):
      res.append(list1[i] + list2[i])

  return res

# For testing the function
if __name__ == "__main__":
   print(combine([2, 8, 9], [-12, 3, 19]))
   print(combine([], [-12, 3, 19]))
   print(combine([3, 8, 9, 24], [-12, 3, 19]))
   print(combine([2, 8, 9], [-10, 13, 9, 57, -74, 0]))