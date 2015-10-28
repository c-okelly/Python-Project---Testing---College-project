__author__ = 'conor'

import itertools
import math
import random

def create_variation_4_list(airport1,airport2,airport3,airport4):

    possible = list(itertools.permutations([airport1,airport2,airport3,airport4], 4))
    possible = [list(i) for i in possible]
    airpots_order_4 = possible

    return airpots_order_4

def create_variation_5_list(home,airport1,airport2,airport3,airport4):


    # Using the above variables create a list of permutations
    order_repeat_home = list(itertools.permutations([airport1,airport2,airport3,airport4,home], 5))
    order_repeat_airport_1 = list(itertools.permutations([airport1,airport2,airport3,airport4,airport1], 5))
    order_repeat_airport_2 = list(itertools.permutations([airport1,airport2,airport3,airport4,airport2], 5))
    order_repeat_airport_3 = list(itertools.permutations([airport1,airport2,airport3,airport4,airport3], 5))
    order_repeat_airport_4 = list(itertools.permutations([airport1,airport2,airport3,airport4,airport4], 5))

    # Convert it from a list of tuples into a list of lists
    order_list_home_repeated = [list(i) for i in order_repeat_home]
    order_list_airport_1_repeated = [list(i) for i in order_repeat_airport_1]
    order_list_airport_2_repeated = [list(i) for i in order_repeat_airport_2]
    order_list_airport_3_repeated = [list(i) for i in order_repeat_airport_3]
    order_list_airport_4_repeated = [list(i) for i in order_repeat_airport_4]

    possible_order_4_with_repeats = order_list_home_repeated + order_list_airport_1_repeated + order_list_airport_2_repeated + order_list_airport_3_repeated + order_list_airport_4_repeated
    return possible_order_4_with_repeats

def add_home_start_finish(airport_list, home_airport):

    for item in airport_list:
        item.append(home_airport)
        item.reverse()
        item.append(home_airport)
        item.reverse()
        # print(item)

    return airport_list

def remove_2_in_row_lists(list_routes):

    # Remove a list where it has been repeated twice

    list_repeated = [] # list of repeated elements

    # print(list_routes)
    # print(len(list_routes))
    count = -1

    # For loop to test individual lists for duplicate
    for i in list_routes:
        # If duplicate is found index number is added to the list_repeated list
        current_list = i
        count +=1
        # print(current_list), print(count)
        if current_list[0] == current_list[1]:
            list_repeated.append(count)
        elif current_list[1] == current_list[2]:
            list_repeated.append(count)
        elif current_list[2] == current_list[3]:
            list_repeated.append(count)
        elif current_list[3] == current_list[4]:
            list_repeated.append(count)
        elif current_list[4] == current_list[5]:
            list_repeated.append(count)
        elif current_list[5] == current_list[6]:
            list_repeated.append(count)

    # list_repeated is reveresed so highest index number is first
    list_repeated.reverse()
    # print(list_repeated)

    # Remove indexed item start from highest index number

    # Remove items by index number from list
    for x in list_repeated:
        list_routes.pop(x)

    # print(list_routes)
    # print(len(list_routes))

    return list_routes

def create_list_of_possible_routes(home,airport_1,airport_2,airport_3,airport_4):

    # Generate possible routes for 4 airports and 4 airport with 1 repeated
    list_4 = create_variation_4_list(airport_1,airport_2,airport_3,airport_4)
    list_5 = create_variation_5_list(home,airport_1,airport_2,airport_3,airport_4)

    # Add home airport to start and finish of each route
    list_5 = add_home_start_finish(list_5, home)
    list_4 = add_home_start_finish(list_4, home)

    # Check for and remove duplicated if present

    list_5 = remove_2_in_row_lists(list_5)

    master_list = list_5 + list_4

    return master_list

def possible_leg_combinations(home,airport_1,airport_2,airport_3,airport_4):

    possible_legs = list(itertools.permutations([airport_1,airport_2,airport_3,airport_4,home], 2))
    possible_legs_list = [list(i) for i in possible_legs]

    # print(possible_legs)
    # print(len(possible_legs))

    return possible_legs


# End of section for list creation from airports

# Trip validator

def validate_trip(trip, airport_object_dictionary):
    # print("Trip has validated")

    # Variables to give information about validation process
    trip_processed = True
    error_messages = []

    name_trip = trip.trip_name
    home = airport_object_dictionary.assign_airport_object(trip.home.upper()) # Upper to convert lower case characters
    airport_1 = airport_object_dictionary.assign_airport_object(trip.airport_1.upper())
    airport_2 = airport_object_dictionary.assign_airport_object(trip.airport_2.upper())
    airport_3 = airport_object_dictionary.assign_airport_object(trip.airport_3.upper())
    airport_4 = airport_object_dictionary.assign_airport_object(trip.airport_4.upper())

    # Check if bad key has resulted in fail airport dict look up and set variables for error message.

    all_keys_found = True

    if home == None:
        bad_key = trip.home
        airport_position = "home"

        # Create error message
        error_message = ("The trip (%s) has an airport code (%s) in airport position (%s) "
                     "that could not be found" % (name_trip,bad_key, airport_position))

        #Create variables to track process
        error_messages.append(error_message)
        trip_processed = False
        all_keys_found = False

    if airport_1 == None:
        bad_key = trip.airport_1
        airport_position = "airport 1"

        # Create error message
        error_message = ("The trip (%s) has an airport code (%s) in airport position (%s) "
                     "that could not be found" % (name_trip,bad_key, airport_position))

        error_messages.append(error_message)
        trip_processed = False
        all_keys_found = False

    if airport_2 == None:
        bad_key = trip.airport_2
        airport_position = "airport 2"

        # Create error message
        error_message = ("The trip (%s) has an airport code (%s) in airport position (%s) "
                     "that could not be found" % (name_trip,bad_key, airport_position))

        error_messages.append(error_message)
        trip_processed = False
        all_keys_found = False

    if airport_3 == None:
        bad_key = trip.airport_3
        airport_position = "airport 3"

        # Create error message
        error_message = ("The trip (%s) has an airport code (%s) in airport position (%s) "
                     "that could not be found" % (name_trip,bad_key, airport_position))

        error_messages.append(error_message)
        trip_processed = False
        all_keys_found = False

    if airport_4 == None:
        bad_key = trip.airport_4
        airport_position = "airport 4"

        # Create error message
        error_message = ("The trip (%s) has an airport code (%s) in airport position (%s) "
                     "that could not be found" % (name_trip,bad_key, airport_position))

        error_messages.append(error_message)
        trip_processed = False
        all_keys_found = False



    # Check that each airport dict has all information required to complete process

    if all_keys_found == True: # Make sure all keys hae found a dict before we test each one

        if home.all_info_available == False:
            bad_key = trip.home
            airport_position = "home"

            # Output error message and make trip processed false
            error_message = ("The trip (%s) has an airport (%s) in position (%s) that does not have all the information "
                     "available for processing") % (name_trip,bad_key,airport_position)
            error_messages.append(error_message)
            trip_processed = False
            # print(error_message)

        if airport_1.all_info_available == False:
            bad_key = trip.airport_1
            airport_position = "airport 1"

            # Output error message and make trip processed false
            error_message = ("The trip (%s) has an airport (%s) in position (%s) that does not have all the information "
                     "available for processing") % (name_trip,bad_key,airport_position)
            error_messages.append(error_message)
            trip_processed = False
            # print(error_message)

        if airport_2.all_info_available == False:
            bad_key = trip.airport_2
            airport_position = "airport 2"

            # Output error message and make trip processed false
            error_message = ("The trip (%s) has an airport (%s) in position (%s) that does not have all the information "
                     "available for processing") % (name_trip,bad_key,airport_position)
            error_messages.append(error_message)
            trip_processed = False
            # print(error_message)

        if airport_3.all_info_available == False:
            bad_key = trip.airport_3
            airport_position = "airport 3"

            # Output error message and make trip processed false
            error_message = ("The trip (%s) has an airport (%s) in position (%s) that does not have all the information "
                     "available for processing") % (name_trip,bad_key,airport_position)
            error_messages.append(error_message)
            trip_processed = False
            # print(error_message)

        if airport_4.all_info_available == False:
            bad_key = trip.airport_4
            airport_position = "airport 4"

            # Output error message and make trip processed false
            error_message = ("The trip (%s) has an airport (%s) in position (%s) that does not have all the information "
                     "available for processing") % (name_trip,bad_key,airport_position)
            error_messages.append(error_message)
            trip_processed = False
            # print(error_message)


        # print(home, airport_1, airport_2, airport_3, airport_4)

    return trip_processed, error_messages

# Calculating ditance and cost section

def calculate_distance(lat_1, long_1, lat_2, long_2):

    radius_of_earth = 6373 # Value from qustion in fourm                 # Wikipediea Value - Also value used in assignment handout

    # Convert lat / longitude to spherical coordinates in radians.
    degrees_radians = math.pi/180.0

    # phi = 90 - latitude
    phi_1 = (90.0 - lat_1)*degrees_radians
    phi_2 = (90.0 - lat_2)*degrees_radians

    # theta = longitude
    theta_1 = long_1*degrees_radians
    theta_2 = long_2*degrees_radians

    # Calculate distane using coCompute spherical distance from spherical coordinates.

    cos = (math.sin(phi_1)*math.sin(phi_2)*math.cos(theta_1 - theta_2) + math.cos(phi_1)*math.cos(phi_2))
    flight_arc = math.acos( cos )
    flight_arc = flight_arc * radius_of_earth

    # Remember to multiply arc by the radius of the earth
    # in your favorite set of units to get length.
    # print(flight_arc)
    return flight_arc

def calculate_distance_with_airport_objects(airport_object_1, airport_object_2):

    # Assign varibles from
    lat_1 = airport_object_1.airport_latitude
    long_1 = airport_object_1.airport_longitude
    lat_2 = airport_object_2.airport_latitude
    long_2 = airport_object_2.airport_longitude

    distance = calculate_distance(lat_1, long_1, lat_2, long_2)

    return distance

def calculate_cost(airport_object_1, airport_object_2):

    # Calculate distance
    distance = calculate_distance_with_airport_objects(airport_object_1, airport_object_2)

    # Cost is distance multiplied by conversion rate at originating airport

    # print(distance)
    cost = distance * airport_object_1.conversion_rate
    # print(cost)

    return cost

# Create dictionary of cost from possible legs

def possible_routes_cost_dict(possible_legs):
    # Take in possible legs and return a dict where key is in format "DXB.JFK : cost"
    # This can then be used to build costs for any route. Much more efficient then doing the calculation for each route

    """ By using the method I will only have to run the calculate cost function 20 times instead of 2,280 times"""

    cost_dict = {}

    count = 0
    for i in possible_legs:
        current_item = i
        count += 1
        first_airport = current_item[0]
        second_airport = current_item[1]
        cost_leg = calculate_cost(first_airport, second_airport)
        # print( "The cost of leg (%s), to (%s), is (%f)" % (first_airport.airport_code, second_airport.airport_code, cost_leg))
        key = first_airport.airport_code + "." + second_airport.airport_code
        # print(key)
        cost_dict[key] = cost_leg
    # print(cost_dict)

    return cost_dict

# Created dictionary with route at index 0 and cost at index 1. Key is in form of "Route No xx"

def cost_each_routes(dict_of_cost_of_legs, list_of_possible_routes):

    dict_of_routes_with_costs = {}
    count = 0

    # Loop though list of possible routes. Using dict of leg cost sum the total cost of routes
    for i in list_of_possible_routes:
        current_item = i
        # print(current_item)

        # Sort between 5 leg and 6 leg routes
        # Generate price based on sum of legs cost
        if len(current_item) == 6:
            # print(current_item)
            count += 1

            first_leg = current_item[0] + "." + current_item[1]
            second_leg = current_item[1] + "." + current_item[2]
            third_leg = current_item[2] + "." + current_item[3]
            fourth_leg = current_item[3] + "." + current_item[4]
            fifth_leg = current_item[4] + "." + current_item[5]

            first_leg_cost = dict_of_cost_of_legs.get(first_leg)
            second_leg_cost = dict_of_cost_of_legs.get(second_leg)
            third_leg_cost = dict_of_cost_of_legs.get(third_leg)
            fourth_leg_cost = dict_of_cost_of_legs.get(fourth_leg)
            fifth_leg_cost = dict_of_cost_of_legs.get(fifth_leg)

            price = first_leg_cost + second_leg_cost + third_leg_cost + fourth_leg_cost + fifth_leg_cost
            # print(price)

        elif len(current_item) == 7:
            count += 1

            first_leg = current_item[0] + "." + current_item[1]
            second_leg = current_item[1] + "." + current_item[2]
            third_leg = current_item[2] + "." + current_item[3]
            fourth_leg = current_item[3] + "." + current_item[4]
            fifth_leg = current_item[4] + "." + current_item[5]
            sixth_leg = current_item[5] + "." + current_item[6]

            first_leg_cost = dict_of_cost_of_legs.get(first_leg)
            second_leg_cost = dict_of_cost_of_legs.get(second_leg)
            third_leg_cost = dict_of_cost_of_legs.get(third_leg)
            fourth_leg_cost = dict_of_cost_of_legs.get(fourth_leg)
            fifth_leg_cost = dict_of_cost_of_legs.get(fifth_leg)
            sixth_leg_cost = dict_of_cost_of_legs.get(sixth_leg)

            price = first_leg_cost + second_leg_cost + third_leg_cost + fourth_leg_cost + fifth_leg_cost + sixth_leg_cost

        #Store route and prices in dict with Route No as key
        key = ("Route No " + str(count))
        # print(key)
        dict_of_routes_with_costs[key] = [current_item, price]

    # print("Routes costs have been calculated\n")
    return dict_of_routes_with_costs




    return True

# Loop through each item in the rotes cost dict and return the cheapest one. Dict item - index 0 is route - index 1 is cost

def find_cheapest_in_dict(all_routes_cost_dict):

    # Set current best to random price in dictionary and double that price

    """ While I could have set it to a arbitrarily high value this method of setting eliminates the possibility
    of a semantic error arising due to the value that was set becoming smaller then the cost of any
    route in the dict. Such an event might occur if we used a currency like Loais Kip as our base currency
    Where 1 euro is = 50,000 Kip """

    random_route = random.choice(list(all_routes_cost_dict.keys()))
    random_dict_item = all_routes_cost_dict.get(random_route)
    current_best = random_dict_item[1]
    current_best = current_best + current_best
    # print(current_best)

    for i in all_routes_cost_dict:
        current_item = all_routes_cost_dict.get(i)
        price = current_item[1]
        # print(price)
        if price < current_best:
            current_best = price
            best_route = current_item


    # print(best_route)

    return best_route

# Find the cost of each possible route and return the cheapest one

def find_cheapest_route(home, airport_1, airport_2, airport_3, airport_4):

    # List of all possible legs needed to create any of the possible routes - stored in airport object form
    possible_legs = possible_leg_combinations(home, airport_1,airport_2,airport_3,airport_4)

    # Create list of possible routes. Only storing code3 elements for each - To be used later as key retrival
    possible_routes = create_list_of_possible_routes(home.airport_code, airport_1.airport_code, airport_2.airport_code, airport_3.airport_code, airport_4.airport_code)

    # Will create a dict containing the cost of the 20 different legs possible
    dict_of_legs_cost = possible_routes_cost_dict(possible_legs)

    # Calculate the total cost of each route
    all_routes_cost_dict = cost_each_routes(dict_of_legs_cost, possible_routes)

    # Find the cheapest route and return it
    cheapest_trip = find_cheapest_in_dict(all_routes_cost_dict)


    return cheapest_trip