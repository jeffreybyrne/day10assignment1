# Find the possible venues that are wheelchair accessible, in Toronto, and can fit at least 150 people. These results should be stored in a list.

venues = [
{ 'address': "123 Main Street", 'city': "Toronto", 'wheelchair_accessible': True, 'capacity': 100 },
{ 'address': "567 Centre Street", 'city': "Toronto", 'wheelchair_accessible': False, 'capacity': 400 },
{ 'address': "9B Ontario Street", 'city': "Montreal", 'wheelchair_accessible': True, 'capacity': 1000 },
{ 'address': "56 Road Avenue", 'city': "Ottawa", 'wheelchair_accessible': True, 'capacity': 650 },
{ 'address': "938 Avenue Way East", 'city': "Toronto", 'wheelchair_accessible': False, 'capacity': 90 },
{ 'address': "34 Main Street West", 'city': "London", 'wheelchair_accessible': False, 'capacity': 300 },
{ 'address': "44 Quebec Road", 'city': "Toronto", 'wheelchair_accessible': True, 'capacity': 200 },
{ 'address': "10 Spruce Avenue Ouest", 'city': "Montreal", 'wheelchair_accessible': False, 'capacity': 525 }

]
#Define a list that'll contain our results
end_list = []

#For each item in the original list
for num in range(0,len(venues)):
    curr_venue = venues[num] #Placeholder to make it easier to reference the current venue
    if curr_venue['city'] == 'Toronto' and curr_venue['wheelchair_accessible'] and curr_venue['capacity'] >=150:
        #If it's in Toronto, is wheelchair accessible, and has a capcity of at least 150, add it to our reult
        end_list.append(curr_venue)

#Finally, print the result
print(end_list)
