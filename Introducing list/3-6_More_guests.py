guests = ["Albert Einstein", "Marie cure", "Alan Turing"]

# add there more guests
guests.insert(0, "Isaac Newton")
guests.insert(2, "Ada Lovelace")


print("great news! I found a bigger table, so I can invite more people.")

for guest in guests: message = f"Dear {guests}, \n\nI would be honored if you would join me for dinner on [5/20/2024]. \n\nSincerely,\nJhomar Rosaliere"
print(message)
