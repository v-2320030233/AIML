import random

def coin_toss():
    result = random.choice(['Heads', 'Tails']) 
    print(f"The coin toss result is: {result}")
    return result

print("Tossing the coin...")
coin_toss()