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

#Made a function to determine if a venue is in a specified city
def in_city(venue,city):
    if venue['city'] == city:
        return True
    else:
        return False

#Made a function to determine whether a given venue is wheelchair accessible
def wheelchair_accessible(venue):
    return venue['wheelchair_accessible']

#Made a function to determine if a venue meets a capacity requirement
def meet_capacity(venue, num):
    if venue['capacity'] >= num:
        return True
    else:
        return False

#For each item in the original list
for num in range(0,len(venues)):
    curr_venue = venues[num] #Placeholder to make it easier to reference the current venue
    if in_city(curr_venue,'Toronto') and wheelchair_accessible(curr_venue) and meet_capacity(curr_venue,150):
        #If it's in Toronto, is wheelchair accessible, and has a capcity of at least 150, add it to our reult
        end_list.append(curr_venue)

#This was my original solution that didn't use any functions
#For each item in the original list
# for num in range(0,len(venues)):
#     curr_venue = venues[num] #Placeholder to make it easier to reference the current venue
#     if curr_venue['city'] == 'Toronto' and curr_venue['wheelchair_accessible'] and curr_venue['capacity'] >=150:
#         #If it's in Toronto, is wheelchair accessible, and has a capcity of at least 150, add it to our reult
#         end_list.append(curr_venue)

#Finally, print the result
print(end_list)
