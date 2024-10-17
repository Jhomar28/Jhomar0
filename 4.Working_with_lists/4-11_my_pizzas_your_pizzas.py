favorite_pizza = ['pepperoni', 'hawaiian', 'veggie']
friend_pizza = favorite_pizza[:]

favorite_pizza.append("meat lover's")
friend_pizza.append('pesto')

print("My favorite pizzas are:")
for pizza in favorite_pizza:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in favorite_pizza:
    print(f"- {pizza}")