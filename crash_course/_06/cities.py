print("\n-----------")
print("6-11. Cities:") #Make a dictionary called cities . Use the names of three cities as keys in your dictionary . 
# Create a dictionary of information about each city and include the country that the city is in, its approximate 
# population, and one fact about that city . The keys for each city’s dictionary should be something like country, 
# population, and fact . Print the name of each city and all of the infor- mation you have stored about it
print("-----------\n")

cities = {
    'buenos aires' : {
        'country' : 'argentina',
        'population' : '2890000',
        'fact': 'Capital City and the most populated of its country'
    },
    'new york': {
        'country' : 'united states',
        'population' : '8623000',
        'fact': 'Its centre Manhattan is one of the main commercial centers'
    },
    'tokio': {
        'country' : 'japan',
        'population' : '9273000',
        'fact': 'Japan\'s capital is a mix of modern with traditional archiquecture'
    }
}

for name, info in cities.items():
    print("***City: %s" % name.title())
    for k,v in info.items():
        if k == 'fact':
            print("%s: %s" % (k.title(),v))
        else:
            print("%s: %s" % (k.title(),v.title()))
