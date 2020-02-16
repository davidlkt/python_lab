print("\n-----------")
print("6-5. Rivers:") #Make a dictionary containing three major rivers and the country each river runs through . 
# One key-value pair might be 'nile': 'egypt' .
# • Use a loop to print a sentence about each river, such as The Nile runs through Egypt .
# • Use a loop to print the name of each river included in the dictionary .
# • Use a loop to print the name of each country included in the dictionary .
print("-----------\n")

rivers = {
    'nile': 'egypt',
    'colorado': 'united states',
    'amazonas': 'brazil'
}

for k,v in rivers.items():
    print("%s river runs through %s" % (k.title(),v.title()))

for k,v in rivers.items():
    print(k.title())

for k,v in rivers.items():
    print(v.title())