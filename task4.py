#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""

def isInteger(a):
  try:
    a = float(a)
    b = a/2
    b = round(b)
    c = b*2
    if c == a :
      return True
    else:
      return False
  except:
    return False


if __name__ == "__main__":
  assert isInteger( 9.5 ) == False
  assert isInteger( -2 ) == True    
  assert isInteger("hello") == False
  assert isInteger(0) == True
