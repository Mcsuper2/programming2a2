# Quiz.py
score = 0
print("Welcome to the quiz!")
name = input("What's your name?")
print(f"Hello {name}! What is 109 + 1299?")
response1 = input()
if response1 == "1408":
    print(f"{name}, you are correct!")
    score += 1
else:
    print(f"{name}, sorry, you are incorrect")
response2 = input("Question 2. Where is the Oort cloud? A: In the brain  B: At the North Pole  C: At the edge of the solar system  D: In cyberspace")
if response2 == "C" or response2 == "c":
    print(f"{name}, you are correct!")
    score += 1
else:
    print(f"{name}, sorry, you are incorrect")
response3 = input("Question 3. What is an act of sternutation? A: Sneezing  B: Coughing  C: Kindness  D: Walking")
if response3 == "A" or response3 == "a":
    print(f"{name}, you are correct!")
    score += 1
else:
    print(f"{name}, sorry, you are incorrect")
response4 = input("Question 4. What is the most spoken language in the world?")
if response4 == "English" or response4 == "english":
    print(f"{name}, you are correct!")
    score += 1
else:
    print(f"{name}, sorry, you are incorrect")
response5 = input("Last question. What is the meaning of life, the universe, and everything?")
if response5 == "42" or "forty-two" or "forty two":
    print(f"{name}, you are correct!")
    score += 1
else:
    print(f"{name}, sorry, you are incorrect")
print(score/5)
per = score/5 * 100
print(f"You got {per}%!")
