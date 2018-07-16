from pythonds.basic.stack import Stack

def baseConverter(decNum, base):
  digits = "0123456789ABCDEF"

  remstack = Stack()

  while decNum > 0:
     rem = decNum % base
     remstack.push(rem)
     decNum = decNum // base

  newString = ""
  while not remstack.isEmpty():
     newString  = newString + digits[remstack.pop()]

  return newString


print(baseConverter(25,16))
print(baseConverter(25,2))

