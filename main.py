
# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes


def question():
    question = input("I am going to tell you a joke! Do you want to hear a joke about robbers, tanks, or pencils? ")
    while question != "finished":
        if question == "robbers":
            input("Knock Knock ")
            input("Calder")
            print("Calder police - I've been robbed!")
            question = input("What would you like to hear a joke about now? If your done, say finished.")
        elif question == "tanks":
            input("Knock Knock ")
            input("Tank ")
            print("You are welcome! ")
            question = input("What would you like to hear a joke about now? If your done, say finished.")
        elif question == "pencils":
            input("Knock Knock ")
            input("Broken pencil ")
            print("Nevermind, it's pointless! ")
            question = input("What would you like to hear a joke about now? If your done, say finished.")
        if question == "finished":
            return "Thank you so much"
 
    

list_score=[70,90,80,100]

def score(list_score):
    total=0
    joke=input("Would you like to give feedback?")
    if joke =="yes":
        rate=int(input("Please rate our game 1-10!:"))
        final_score= int(rate * 10)
        list_score.append(final_score)
        # print(list_score)
    else:
         return "Thats fine. Thank you!"
    for num in list_score:
            total+=num
            count=len(list_score)
            average=total/count
    return f"Our satisfaction average is now {average}! Thank you so much for your feedback!" 



print(question())
print(score(list_score))
    