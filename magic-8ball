import random

# Initialize variables
name = "Emma"
question = "Did I do well on my project?"
random_number = random.randint(1, 9)

# Formatted user question
def userQuestion(name, question):
  return name + " asks: " + question

# Formatted Magic 8-Ball's answer
def answer():
  return "Magic 8-Ball's answer: "

if name != "": # Ensure name field isn't empty
  if question != "": # Ensure question field isn't empty
    print(str(userQuestion(name, question))) # Print user's question
    match random_number:
      case 1:
        print(str(answer()) + "Yes - definitely")
      case 2:
        print(str(answer()) + "It is decidedly so")
      case 3:
        print(str(answer()) + "Without a doubt")
      case 4:
        print(str(answer()) + "Reply hazy, try again")
      case 5:
        print(str(answer()) + "Ask again later")
      case 6:
        print(str(answer()) + "Better not tell you now")
      case 7:
        print(str(answer()) + "My sources say no")
      case 8:
        print(str(answer()) + "Outlook not so good")
      case 9:
        print(str(answer()) + "Very doubtful")
  else:
    print("Please ask the Magic 8-Ball a question.") # Prints when question field is empty
else:
  print("Please enter your name.") # Prints when name field is empty
