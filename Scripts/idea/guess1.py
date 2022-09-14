usernumber = input('Pick a number from 1 to 25 ')
intusrnum = int(usernumber)
guessnumber = 26
minnum = 0
maxnum = 26
while intusrnum != guessnumber:
  guessnumber = int((maxnum + minnum) / 2)
  if guessnumber > intusrnum:
    maxnum = guessnumber
  if guessnumber < intusrnum:
    minnum = guessnumber
  print ("guessed " + str(int(guessnumber)))
print ('Your number is ' + str(guessnumber))