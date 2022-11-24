import random

tri1 = random.randint(1, 9)
tri2 = random.randint(1, 9)
def diigame():
    game = input("Do you want to play a diegame? y/n ")
    if game == 'y':
        product = tri2 * tri1
        print(product)
    else:
        print("Thanks")
    return 1





