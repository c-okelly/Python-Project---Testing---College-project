__author__ = "Conor O'Kelly"

from Main import run_in_single_input_from_file_output_to_file_mode, run_in_multiple_input_from_file_output_to_file_mode, run_in_single_input_return_output_mode
from CSV_constructer import Trip

# Testing of different mode

def different_mode():

    # Mode 1 - Take single line from an input file and output it as a file and output cheapest route to file

    run_in_single_input_from_file_output_to_file_mode("countrycurrency.csv", "currencyrates.csv", "airport.csv","tripsInput.csv")

    # Mode 2 - Take multiple lines of input from file and output cheapest route to file

    run_in_multiple_input_from_file_output_to_file_mode("countrycurrency.csv", "currencyrates.csv", "airport.csv","tripsInput.csv")

    # Mode 3 - Take single input of trip object and filenames and return cheapest routes

    trip = Trip("Single_tester Trip","DUB","JFK","AAL","SYD","CDG") # Assign trip object to variable

    cheap_trip = run_in_single_input_return_output_mode("countrycurrency.csv", "currencyrates.csv", "airport.csv", trip)

    print(cheap_trip)

# 2 incorrect file name

def incorrect_file_name():
    trip = Trip("Single_tester Trip","DUB","JFK","AAL","SYD","CDG") # Assign trip object to variable

    # Error will also reteun from the function as a string to be displayed elsewhere

    # Currency filename incorrect
    run_in_single_input_return_output_mode("x.csv", "currencyrates.csv", "airport.csv", trip)

    # Conversion rates filename incorrect
    run_in_single_input_return_output_mode("countrycurrency.csv", "x.csv", "airport.csv", trip)

    # Aiport information filename incorrect
    run_in_single_input_return_output_mode("countrycurrency.csv", "currencyrates.csv", "x.csv", trip)

    # Trips filename incorrect
    run_in_multiple_input_from_file_output_to_file_mode("countrycurrency.csv", "currencyrates.csv", "airport.csv", "x.csv")

incorrect_file_name()

# 3 Incorrectly formatted file

    # Handled within the program and an error message is generated as a return instead of a cheapest trip object

# 4 Airport code from employee request not found

    # # Handled within the program and an error message is generated as a return instead of a cheapest trip object

# 5 Airport code from employee request does not have sufficient information to process

    # Handled within the program and an error message is generated as a return instead of a cheapest trip object

# 6 Country has no information on currency and conversion rate can not be found

    # Handled within the program and an error message is generated as a return instead of a cheapest trip object


# 8 CSV value for 3 letter key is not 3 letters

    # Handled within the program and an error message is generated as a return instead of a cheapest trip object

#
#
#
#
#
#
#
#
#
#
#
#