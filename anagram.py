#checking if the two passed strings are anagrams


def anagram(s1,s2):
    
    flag = True 
    if len(s1) != len(s2):
      flag = False

    alist = list(s1)
    blist = list(s2)
    for i in alist:
      flag1 = False
      flag2 = False
      for j in blist:
        if i == j:
           flag2 = True

      flag1 = flag2

    if flag1 == True & flag == True:
      print("Yes, The strings are anagrams!")
    else:
      print('No ..recheck')


def main():
  anagram('earth','hear')

main()
