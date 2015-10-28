__author__ = "Conor O'Kelly"

from CSV_constructer import AirportDict, TripRequestsDict, CheapestTrip, Trip, CurrencyFileNotFound, ConversionFileNotFound,AirportFileNotFound, TripFileNotFound, FileNotCorrectlyFormatted
from core_functions import *
import csv
import datetime

# Load GUI that will take number of inputs



# Take in input of files for information and file for trip requests
# Last two parameters are bollans True or False that will dictate the output and type of input.

def core_function(country_currency_filename, currency_rate_filename, airport_information_filename, trip_requests, is_trip_item_single_true, file_output_mode_true ):

    # Create main airport object dictionary
    airport_object_dictionary = take_information_data_input(country_currency_filename, currency_rate_filename, airport_information_filename)

    # Check if input is single or multipule
    if is_trip_item_single_true == True:

        # Calculate_cheapest_route_single() - calculate using a singe request

        trip = trip_requests # Assign trip object

        cheapest_trip = calculate_cheapest_route_single(trip, airport_object_dictionary)


    elif is_trip_item_single_true == False: # Means there a multiple trip items to be processed

        # Create trips dictionary from file input
        trip_requests_dict = take_trips_request_inputs(trip_requests)
        # print(trip_requests_dict)

        # Multiple routes calculation using a dictionary of requests
        cheapest_trip_list = calculate_cheapest_route_from_dict(trip_requests_dict, airport_object_dictionary)



    # Output information section

    if file_output_mode_true == True:

        if is_trip_item_single_true == True:

            #Output infromation from an dict_object holidng cheapest trip dicts
            output_csv_file(cheapest_trip, True)

        elif is_trip_item_single_true == False:

            output_csv_file(cheapest_trip_list, False)

    elif file_output_mode_true == False:
        # Output from a single trip requests

        return cheapest_trip

def create_trip(trip_name, home, airport_1, airport_2, airport_3, airport_4):

    #Create trip object
    trip = Trip(trip_name, home, airport_1, airport_2, airport_3, airport_4)
    return trip


# Functions to process take input and assign objects containing relevant dict objects

def take_information_data_input(country_currency_file, currency_rates_file, airport_info_file):
    # Take inputs from three information files and from employee trip requests
    airport_object_dictionary = AirportDict(country_currency_file, currency_rates_file, airport_info_file)
    return airport_object_dictionary

def take_trips_request_inputs(trips_input_files):
    trips = TripRequestsDict(trips_input_files)
    trips_dict = trips.return_dict()
    return trips_dict

# Output to file mode


def time_string():
    current_time = datetime.datetime.now()

    hour = str(current_time.hour)
    minute = (current_time.minute)
    seconds = (current_time.second)

    if minute <10:
        minute = ("0"+str(minute))
    elif minute >= 10:
        minute = str(minute)

    if seconds <10:
        seconds = ("0"+str(seconds))
    elif seconds >= 10:
        seconds = str(seconds)

    time_string = (hour+":"+ minute+":"+seconds)
    return time_string

def output_csv_file(list_or_trip, single_trip_object_true): # Will write output to file

    # Open file. If files does not exist create it

    # Create string of time
    time = time_string()

    # Differenciate between mode 1 and 2 - multiple lines of file input vs one
    mode = "1"
    if single_trip_object_true == False:
        mode = "2"

    file_name = ("Trip plans for employees created at (%s) in (mode %s)" % (time,mode))
    f = open(file_name, 'w')
    writer = csv.writer(f)

    # Check if single trip object or dictionary or trip object

    if single_trip_object_true == True:

        trip = list_or_trip
        if trip.trip_processed == True: # Check if the current item has been correctly proccesed

            # Create line to be output and write it to file
            # Row is a list that contains one item - to prevent CSV writer outputting each item separately

            row = [("The cheapest trip for (%s) will cost (%.2f euro), and is as follows (%s)") % (trip.trip_name, trip.cost_of_trip,trip.route)]
            # print(row)
            writer.writerow(row)

        elif trip.trip_processed == False:

            # Check the numbers of errors
            if len(trip.error_message) == 1:
                number_of_errors = "1 error"
            elif len(trip.error_message) > 1:
                no_error = str(len(trip.error_message))
                number_of_errors = (no_error + " errors")

            # Create line to be output and write it to file
            # Row is a list that contains one item - to prevent CSV writer outputting each item separately

            row = [("The trip for (%s), could not be processed due to %s occurring as follows (%s) " % (trip.trip_name, number_of_errors, trip.error_message))]
            # print(row)
            writer.writerow(row)


    elif single_trip_object_true == False: # Output multiple objects
        # Call object from dictionary
        for i in list_or_trip:
            current_dict_item = i
            # print(current_dict_item)

            if current_dict_item.trip_processed == True: # Check if the current item has been correctly proccesed

                # Create line to be output and write it to file
                # Row is a list that contains one item - to prevent CSV writer outputting each item separately

                row = [("The cheapest trip for (%s) will cost (%.2f euro), and is as follows (%s)") % (current_dict_item.trip_name, current_dict_item.cost_of_trip,current_dict_item.route)]
                # print(row)
                writer.writerow(row)

            elif current_dict_item.trip_processed == False:

                # Check the numbers of errors
                if len(current_dict_item.error_message) == 1:
                    number_of_errors = "1 error"
                elif len(current_dict_item.error_message) > 1:
                    no_error = str(len(current_dict_item.error_message))
                    number_of_errors = (no_error + " errors")

                # Create line to be output and write it to file
                # Row is a list that contains one item - to prevent CSV writer outputting each item separately

                row = [("The trip for (%s), could not be processed due to %s occurring as follows (%s) " % (current_dict_item.trip_name, number_of_errors, current_dict_item.error_message))]
                # print(row)
                writer.writerow(row)

#Running modes - First is batch mode - second take single file input and return trips

def run_in_single_input_from_file_output_to_file_mode(country_currency_filename, currency_rate_filename, airport_information_filename, trip_requests_file):

    try:
        trips_request_dict = take_trips_request_inputs(trip_requests_file)
    except TripFileNotFound:
        error_message = "The trips request file was not found"
        print(error_message)
        return error_message

    try:
        for i in trips_request_dict:
            trip_request_item = trips_request_dict.get(i)

        core_function(country_currency_filename, currency_rate_filename, airport_information_filename, trip_request_item,True,True)

    # except UnboundLocalError:
    #     pass
    except CurrencyFileNotFound:
        error_message = "The Currency file was not found"
        print(error_message)
        return error_message
    except ConversionFileNotFound:
        error_message = "The Conversion rate file was not found"
        print(error_message)
        return error_message
    except AirportFileNotFound:
        error_message = "The Airport file was not found"
        print(error_message)
        return error_message

def run_in_multiple_input_from_file_output_to_file_mode(country_currency_filename, currency_rate_filename, airport_information_filename, trip_requests_file):

    # Run with input from file - batch mode

    try:
        core_function(country_currency_filename, currency_rate_filename, airport_information_filename, trip_requests_file,False,True)

    except CurrencyFileNotFound:
        error_message = "The Currency file was not found"
        print(error_message)
        return error_message
    except ConversionFileNotFound:
        error_message = "The Conversion rate file was not found"
        print(error_message)
        return error_message
    except AirportFileNotFound:
        error_message = "The Airport file was not found"
        print(error_message)
        return error_message
    except TripFileNotFound:
        error_message = "The trips request file was not found"
        print(error_message)
        return error_message
    except FileNotCorrectlyFormatted as e:
        details = e
        error_message = "The file (%s) was not correctly formatted" % (details)
        print(error_message)
        return error_message


def run_in_single_input_return_output_mode(country_currency_filename, currency_rate_filename, airport_information_filename, trip_object):

    # Run with input from single trip

    try:
        cheap = core_function(country_currency_filename, currency_rate_filename, airport_information_filename,trip_object,True,False)
        return cheap
    except CurrencyFileNotFound:
        error_message = "The Currency file was not found"
        print(error_message)
        return error_message
    except ConversionFileNotFound:
        error_message = "The Conversion rate file was not found"
        print(error_message)
        return error_message
    except AirportFileNotFound:
        error_message = "The Airport file was not found"
        print(error_message)
        return error_message
    except FileNotCorrectlyFormatted as e:
        details = e
        error_message = "The file (%s) was not correctly formatted" % (details)
        print(error_message)
        return error_message

    # print(cheap)



# # Testing
#
# # Mode 1
#
# run_in_single_input_from_file_output_to_file_mode("countrycurrency.csv", "currencyrates.csv", "airport.csv","tripsInput.csv")
#
# # Mode 2
#
# run_in_multiple_input_from_file_output_to_file_mode("countrycurrency.csv", "currencyrates.csv", "airport.csv","tripsInput.csv")
#
# # Mode 3
#
# trip = Trip("Single_tester Trip","DUB","JFK","AAL","SYD","CDG") # Assign trip object to variable
#
# x = run_in_single_input_return_output_mode("countrycurrency.csv", "currencyrates.csv", "airport.csv", trip)


# # print(x)
