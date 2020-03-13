print("\n-----------")
print("8-7. Album:") #Write a function called make_album() that builds a dictionary describing a music album . 
# The function should take in an artist name and an album title, and it should return a dictionary containing 
# these two pieces of information . Use the function to make three dictionaries representing different albums . 
# Print each return value to show that the dictionaries are storing the album information correctly .
# Add an optional parameter to make_album() that allows you to store the number of tracks on an album . 
# If the calling line includes a value for the num- ber of tracks, add that value to the album’s dictionary . 
# Make at least one new function call that includes the number of tracks on an album .
print("-----------\n")

def make_album(artist,title,tracks=''):
    if tracks:
        album = {'artist_name': artist, 'album_title': title, 'tracks_amount': tracks}
    else:
        album = {'artist_name': artist, 'album_title': title}
    
    return album

print(make_album("Soda Stereo","Canción Animal"))
print(make_album("Nirvana","Nevermind",12))
print(make_album("Primus","Sailing the Seas of Cheese"))

print("\n-----------")
print("8-8. User Albums:") #Start with your program from Exercise 8-7 . Write a while loop that allows users to enter an 
# album’s artist and title . Once you have that information, call make_album() with the user’s input and print the 
# dictionary that’s created . Be sure to include a quit value in the while loop .
print("-----------\n")

flag = True

while flag:
    artist = input("Enter name of artist: \n")
    title = input("Enter name of album: \n")
    
    print(make_album(artist,title))

    response = input("Another? q for quit")

    if response == 'q':
        flag = False
        
