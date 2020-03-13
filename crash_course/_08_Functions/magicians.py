print("\n-----------")
print("8-9. Magicians:") #Make a list of magician’s names . Pass the list to a function called show_magicians(), which prints 
#the name of each magician in the list .
print("-----------\n")

magicians = ['melchor', 'gaspar', 'baltazar']

def show_magicians(list):
    for mage in list:
        print('. %s.' % mage.title())

show_magicians(magicians)

print("\n-----------")
print("8-10. Great Magicians:") #Start with a copy of your program from Exercise 8-9 . Write a function called make_great() that 
#modifies the list of magicians by add- ing the phrase the Great to each magician’s name . Call show_magicians() to see 
#that the list has actually been modified .
print("-----------\n")

def make_great(list):
    for n in range(0,int(len(list))):
        mage = list[n]
        list[n] = 'The Great ' + mage
great_magicians = magicians[:]
make_great(great_magicians)
show_magicians(magicians)

print("\n-----------")
print("8-11. Unchanged Magicians:") #Start with your work from Exercise 8-10 . Call the function make_great() with a copy of the list 
# of magicians’ names . Because the original list will be unchanged, return the new list and store it in a separate list . 
# Call show_magicians() with each list to show that you have one list of the origi- nal names and one list with the Great added 
# to each magician’s name .
print("-----------\n")

show_magicians(great_magicians)
