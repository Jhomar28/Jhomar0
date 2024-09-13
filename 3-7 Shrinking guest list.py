guests = ["Albert Einstein", "Marie cure", "Alan Turing", "Isaac Newton", "Ada lovelace", "Nikola tesala"]
print("unfortunately, the dinner table won't arrive in time. I can only Invite two pepole.")

while len(guests) >2:
    popped_guests = guests.pop()
    message = f"Dear {popped_guests}, \n\nI'm so sorry, but I won't be able to invite you to dinner. \n\nSincerely,\nJhomar Rosaliere"
    print(message)

del guests[:]
print(guests) #should print an empty list