__author__ = "Conor O'Kelly"

from Main import run_in_single_input_from_file_output_to_file_mode, run_in_multiple_input_from_file_output_to_file_mode, run_in_single_input_return_output_mode
from gui import launch_gui

def batch_mode():

    # Change to load different files

    # Data files
    country_currency_file_name = "countrycurrency.csv"
    currency_rate_file_name = "currencyrates.csv"
    airports_filename = "airport.csv"

    #Trips
    trips_input_filename_single = "tripsInputSingle.csv"
    trips_input_filename_multiple = "tripsInput.csv"

    #Mode 1
    run_in_single_input_from_file_output_to_file_mode(country_currency_file_name, currency_rate_file_name, airports_filename, trips_input_filename_single)
    # print("1")

    # Mode 2

    run_in_multiple_input_from_file_output_to_file_mode(country_currency_file_name, currency_rate_file_name, airports_filename, trips_input_filename_multiple)
    # print("2")

def gui_mode():
    launch_gui()
    return True

x = 1

# batch_mode()

gui_mode()