currents_user = ["Cintia", "Sebastian", "Adrian", "Juan", "Matias"]
new_user = ["Cintia", "Francisco", "Leonel", "Camila", "Luciana"]

"""
currents_user += new_user
print(currents_user)"""

for new_user in new_user:
    if new_user not in currents_user:
        print("Add "+new_user+" , Welcome")
        currents_user.append(new_user)
    else:
        print(""+new_user+" will need to enter a new username")
print("New currents user list :", currents_user)