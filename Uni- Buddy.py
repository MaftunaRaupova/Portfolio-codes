"""The code is for chatbot to help university freashmen smooth transition. 
It wil ask several questions from user to make it more personal. 
Also it will suggest the user to join some of the clubs."""

intro = "Hi my name is Chatty. Welcome to our Uni!"
print(intro)

user_name = input("What is your name? ")
print(f"Welcome {user_name}. It's nice to meet you, I hope you have fantastic time in here!")

# below code will ask the user's age and respond depending on the age. 

user_age = int(input(f"How old are you {user_name}? "))

if user_age >=50:
    print(f"{user_name}, don't worry, late bloomers bloom brightest!")
elif user_age >= 18: 
    print(f"{user_name}, perfect timing!")
else:
    print(f"{user_name}, you must be genius, awesome!")

# the code will give the choice of clubs for the user and give info. 

club_options = "We have several club types if you are interested in. Art, Debate, Cooking and Book Clubs. "
print(club_options)

user_club_choice = input("Please choose the club: ")

while True:
    if user_club_choice.lower() == "art":
        print(f"Creative choice {user_name}! Art club is on Tuesdays between 18:00-19:00 in The Design campus. ")
        break
    elif user_club_choice.lower() == "debate":
        print(f"Interesting choice {user_name}! Debate club is on Wednesdays between 18:00-19:00 in the main Library. ")
        break
    elif user_club_choice.lower() == "cooking":
        print(f"Excellent choice {user_name}! Cooking club is on Fridays between 18:00-19:00 in the dormitory kitchen. It gives the students opportunity to socialsie and enjoy the declicious meal. ")
        break
    elif user_club_choice.lower() == "book":
        print(f"{user_name}, you are a bookworm! Book club is on Thursdays between 18:00-19:00 in the dormitory's main sitting room. ")
        break
    else:
        print(f"Well {user_name}, are you triying to arrange a new club? Please choose the one availbale.")

print("If you are unfamiliar with the campus locations, you can always check our University map at the bottom of this page. ")

#code will continue to intercat with the user providing further information depending on user's choice.
 
user_input = input("Well I hope I haven't bored you yet! Would you like to hear more? ")
if user_input.lower() == "yes":
    print("We also have Academic Calendar, Faculty and Staff Contacts, Career Services, Mental Health Support and Technology and IT Services.")
    user_input= input("Please enter the information you would like to know: ")
    
    while True:
        if user_input.lower() == "academic calendar":
            print("Please download Academic_Calendar.pdf on the following link.")
            break
        elif user_input.lower() == "faculty and staff ontacts":
            print("You can see the contact details on our Contacts page below. ")
            break
        elif user_input.lower() == "career services":
            print("Our Career Services support team are great. Please contact them via email, career@uni.com")
            break
        elif user_input.lower() == "mental health support":
            print("As well as education, your mental wellbeing is also importat and our university arranged whole team to support students. Please contact wellbeing@uni.com ")
            break
        elif user_input.lower()== "technology and it services":
            print("Well, sometimes you might have some technical issues. Our IT Team is always there to support you no matter how big or small your issue is. Contact via  ")
            break
        else:
            print("Please choose the availbale service.")
            
    print(f"{user_name}, it was pleasure to speak to you. If you have any question please do not hesitate to chat to me. In case if you are detoxing from screen, you can find the info inside the Student Manual.")  

else:
    print(f"{user_name}, it was pleasure to speak to you. If you have any question please do not hesitate to chat to me. In case if you are detoxing from screen, you can find the info inside the Student Manual.")