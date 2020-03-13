print("\n-----------")
print("5-5. Alien Colors #3:")  #Turn your if-else chain from Exercise 5-4 into an if-elif- else chain .
# • If the alien is green, print a message that the player earned 5 points .
# • If the alien is yellow, print a message that the player earned 10 points .
# • If the alien is red, print a message that the player earned 15 points .
# • Write three versions of this program, making sure each message is printed for the appropriate color alien .
print("-----------\n")

alien_color = input("Enter the color of the alien (green/yellow/red): ").lower()

if alien_color == "green":
    print("A %s alien gives 5 points!" % alien_color)
elif alien_color == "yellow":
    print("A %s alien gives 10 points!" % alien_color)
elif alien_color == "red":
    print("A %s alien gives 15 points!" % alien_color)
else:
    print("You didn't choose a correct option.")