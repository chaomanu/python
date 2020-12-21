import random
randomnumber = random.randint(0,2)
#1 rock #2 paper #3 scissor


choices = ["rock", "paper", "scissor"]
print("Possible inputs: ")
print(*choices, sep = ", ")

hand = input("Please choose: ").lower()

print("\n")

if hand in choices:
      print("You chose " + hand)
else:
      print("You chose... well...: " + hand)


randochoices = ["rock", "paper", "scissor"]
randohando = randochoices[randomnumber]
print("randobot chose " + randohando)

if hand == randohando:
   print("It's a draw! (lame)")

elif hand == "rock" and randohando == "scissor" or hand == "scissor" and randohando == "paper" or hand == "paper" and randohando == "rock":
   print("Yes! Suck it, randobot!")

elif hand == "scissor" and randohando == "rock" or hand == "paper" and randohando == "scissor" or hand == "rock" and randohando == "paper":
   print("Oh no, you got owned by robobot!")

else:
   print("who knows what happened there...?")
   print("let's just say you lost")

