#! /usr/bin/python

print 'Content-type: text/html'
print ''

import cgi
import random
form = cgi.FieldStorage();

reds = 0
whites = 0
message = "I have made a random 4 digit number.Guess it in minimum moves!"
if "answer" in form:
  answer = form.getvalue("answer")
  print answer
else:
  answer = ""
  for i in range(4):
    answer += str(random.randint(0,9))
    
  
if "guess" in form:
  guess = form.getvalue("guess")
  
  for key,digit in enumerate(guess):
    if digit == answer[key]:
      reds+=1
    else:
      if digit in answer:
        whites+=1
else:
  guess=""
  
if "GuessNo" in form:
  GuessNo = int(form.getvalue("GuessNo")) + 1
else:
  GuessNo = 0
  
if GuessNo==0:
  message = "I have made a random 4 digit number.Guess it in minimum moves!"
elif reds ==4:
  message = "You guessed it correct in "+str(GuessNo)+" guesses."+"<a href=''>Play Again!</a>"
else:
  message = "You have "+str(reds)+" reds and "+str(whites)+" whites"
  
  
print "<h1> MasterMind : The Game </h1>"
print "<p><b>Instructions</b></p>"
print "<ul><li>Reds symbolizes the number of digits you have in correct places</li><li>Whites symbolizes the remaining number of digits apart from are present in a number.</li></ul>"
print "<p>"+message+"</p>"
print "<form method='post'>"
print "<input type='text' value='"+guess+"' placeholder='Guess here' name='guess'>"
print "<input type='hidden' name='answer' value='"+answer+"'>"
print "<input type='submit' value='Guess!'>"
print "<input type='hidden' name='GuessNo' value='"+str(GuessNo)+"'>"
print "</form>"