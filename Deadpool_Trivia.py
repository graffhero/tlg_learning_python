#!/usr/bin/env python3
#Convert the 0 into a number so we can add scores
score = 0
score = int(score)

#Ask user for their name
name = input("What is your name?")
name = name.title()
print("""{}? Well that\'s a silly name. Welcome to Deadpool Trivia! 
I have 5 questions for you.
Pick a number to choose your answer.
Let\'s test your knowledge on the Merc with a Mouth and Good Luck""".format(name))

#Question1
print("""What is Deadpool\'s real name?
1. Logan 
2. Ryan Reynolds 
3. James Howlett 
4. Wade Wilson""")

answer1 = "4"
response1 = input("Your answer is:")

if (response1 != answer1):
    print("NOPE! Not the right answer, dummy!")
else:
    print("Nice job!..I guess." + response1 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question2
print("""What is Deadpool\'s super power?
1. Teleportation 
2. Healing Factor
3. Super Strength 
4. Calisthenics""")

answer2 = "2"
response2 = input("Your answer is:")

if (response2 != answer2):
    print("WRONG, WRONG, WRONG!")
else:
    print("Sweet Justice! You\'re not completely stupid! " + response2 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question3
print("""What is Deadpool\'s favorite Mexican food?
1. Chimichangas 
2. Tacos 
3. Gorditas 
4. Enchiladas""")

answer3 = "1"
response3 = input("Your answer is:")

if (response3 != answer3):
    print("Sorry, moron! Blind Al know\'s me better than you!")
else:
    print("CHIMI-F@%$\'n-CHANGAS!!! " + response3 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question4
print("""Who has Deadpool NOT slept with?
1. Death
2. The Wasp
3. Rogue
4. Vanessa 'Copycat' Carlysle""")

answer4 = "3"
response4 = input("Your answer is:")

if (response4 != answer4):
    print("WRONG! We did the nasty!")
else:
    print("I\'ve locked lips with this soul sucker but we never shacked up! " + response4 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question5
print("""Who is Deadpool\'s favorite super hero?
1. Cable
2. Captain America
3. Wolverine
4. Domino""")

answer5 = "2"
response5 = input("Your answer is:")

if (response5 != answer5):
    print("Wrong Again! But surely I\'m THEIR favorite superhero!")
else:
    print("I may be Canadian, but Capsicle was my idol growing up and probably one of the only people that actually likes me!! " + response5 + " is correct!")
    score = score + 1

print("Your total score is " + str(score) + " out of 5")
print("Thanks for 'playing' with me, {}. (If you know what I mean.) Adios, pal!".format(name))
