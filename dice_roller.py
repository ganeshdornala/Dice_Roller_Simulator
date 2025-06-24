import random
import time
import sys
def rolling_animation():
    animation=["Rolling.","Rolling..","Rolling..."]
    for frame in animation:
        print(frame,end="\r")
        time.sleep(0.5)
def main():
    print("Welcome to the Dice Roller Simulator!")
    input("Press Enter to roll the dice...")
    rolling_animation()
    result=random.randint(1,6)
    print(f"You rolled a: {result}")
if __name__=="__main__":
    main()