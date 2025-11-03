import random

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the math book look sad? Because it had too many problems.",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "What do you call fake spaghetti? An impasta.",
    "I told my computer I needed a break — and it froze."
]

def tell_joke():
    print(random.choice(jokes))
