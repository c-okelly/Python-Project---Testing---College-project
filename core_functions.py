__author__ = "Conor O'Kelly"

from CSV_constructer import CheapestTrip
from airport_list_functions import *


# The two main core functions - first calculates cost of multiple trips and returns a dict - Second calculates cost of single trip

def calculate_cheapest_route_from_dict(trip_requests_dict,airport_object_dictionary):

    cheapest_trips_list = []
    # Run cheapest trip method on each trip
    for i in trip_requests_dict:
        current_trip = trip_requests_dict.get(i)
        cheapest_trip = calculate_cheapest_route_single(current_trip, airport_object_dictionary)
        cheapest_trips_list.append(cheapest_trip)
        # print(cheapest_trip)
    # print(cheapest_trips_list)
    return cheapest_trips_list


def calculate_cheapest_route_single(trip, airport_object_dictionary):

    name_trip = trip.trip_name

    validator = validate_trip(trip, airport_object_dictionary)

    trip_processed = validator[0]
    error_messages = validator[1]

    # See if trip has passed validation if not return cheapest object blank with error messages

    if trip_processed == False:
        trip_finshed = CheapestTrip(name_trip, "No home", "No home code", "No route", "No cost", trip_processed, error_messages)
        # print("Trip has not been processed")
        # print(error_messages)
        return trip_finshed

    elif trip_processed == True:

        # print("Trip has been processed and validated")
        #Process of calculating cheapest route

        home = airport_object_dictionary.assign_airport_object(trip.home.upper()) # Upper to convert lower case characters
        airport_1 = airport_object_dictionary.assign_airport_object(trip.airport_1.upper())
        airport_2 = airport_object_dictionary.assign_airport_object(trip.airport_2.upper())
        airport_3 = airport_object_dictionary.assign_airport_object(trip.airport_3.upper())
        airport_4 = airport_object_dictionary.assign_airport_object(trip.airport_4.upper())

        # Find the cheapest trip
        cheapest_trip = find_cheapest_route(home, airport_1, airport_2, airport_3, airport_4)
        # print(cheapest_trip)

        # Created CheapestTrip object to be output

        airport_route = cheapest_trip[0]
        # print(airport_route)
        trip_price = cheapest_trip[1]

        best_trip = CheapestTrip(name_trip, home.airport_name, home.airport_code, airport_route, trip_price, True, "No error occurred")
        # print(best_trip)

        return best_trip # Should return the finished trip
    else:
        print("Error has occurred in core_functions")


def calculate_trip_with_random_airport_as_repeated():
    return True