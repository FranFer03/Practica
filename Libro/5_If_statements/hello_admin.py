#user_lest = ["ricard", "admin", "carlos", "daniel"]
user_lest = []
if user_lest:
    for user in user_lest:
        if user == "admin":
            print("Hello admin, would you ike to see a status report?")
        else:
            print("Hello "+user+" ,thank you for log")
else:
    print("List empty")