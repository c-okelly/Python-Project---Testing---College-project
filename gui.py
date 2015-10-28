__author__ = "Conor O'Kelly"

from Main import run_in_single_input_from_file_output_to_file_mode, run_in_multiple_input_from_file_output_to_file_mode, run_in_single_input_return_output_mode
from CSV_constructer import Trip
from tkinter import *
import tkinter as tk

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

    # Mode 2

    run_in_multiple_input_from_file_output_to_file_mode(country_currency_file_name, currency_rate_file_name, airports_filename, trips_input_filename_multiple)

class TripProgram(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(500, weight=1)
        container.grid_columnconfigure(500, weight=1)

        self.frames = {}

        for F in (StartPage, BatchInput, SingleInput):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew", padx=150, pady=50)

        self.show_frame(StartPage)

    def show_frame(self, page):

        frame = self.frames[page]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page")
        label.grid(columnspan=3, pady=100,padx=100)


        # Buttons at the bottom
        button = tk.Button(self, text="Batch Input", command=lambda: controller.show_frame(BatchInput))
        button.grid(row=2,column=0, padx=10, pady=10)

        button2 = tk.Button(self, text="Single Input", command=lambda: controller.show_frame(SingleInput))
        button2.grid(row=2,column=1, padx=10, pady=10)

        button3 = tk.Button(self, text="Quit", command=quit)
        button3.grid(row=2,column=2, padx=10, pady=10)


class BatchInput(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Batch Input")
        label.grid(columnspan=3, pady=10,padx=100)

        # Process information

        def process_files(**args):

            #Get values
            value_1 = currencyFile.get() #str(currency_file.get())
            value_2 = conversionRate.get()
            value_3 = airportFile.get()
            value_4 = tripRequestsFile.get()


            # print(value_1,value_2,value_3,value_4)

            # If function fails it will return and error. If it passes returns nothing
            sys_error = run_in_multiple_input_from_file_output_to_file_mode(value_1,value_2,value_3,value_4)
            if sys_error != None:
                # print(sys_error)
                error.set(sys_error)
            else:
                sys_error = "Success"
                error.set(sys_error)

        # File Inputs
        currencyFile = StringVar()
        conversionRate = StringVar()
        airportFile = StringVar()
        tripRequestsFile = StringVar()
        error = StringVar()


        # Currency file input

        currency_label = Label(self, text="Currency filename:").grid(row=1,column=0, sticky=(W))

        currency_file = Entry(self, width=12, textvariable=currencyFile).grid(row=1,column=1,columnspan=2, sticky=(W, E))

        # Conversion rate file input

        conversion_label = Label(self, text="Conversion rates filename:").grid(row=2,column=0, sticky=(W))

        conversion_file = Entry(self, width=12, textvariable=conversionRate).grid(row=2,column=1,columnspan=2, sticky=(W, E))

        # Airport file input

        currency_label = Label(self, text="Airport data filename:").grid(row=3,column=0, sticky=(W))

        currency_file = Entry(self, width=12, textvariable=airportFile).grid(row=3,column=1,columnspan=2, sticky=(W, E))

        # Trip Requests file input

        currency_label = Label(self, text="Trip request filename:").grid(row=4,column=0, sticky=(W))

        currency_file = Entry(self, width=12, textvariable=tripRequestsFile).grid(row=4,column=1,columnspan=2, sticky=(W, E))

        # Button to call function and return result and text box to display output

        monitor = Label(self, textvariable=error).grid(row=5, columnspan=2, sticky=(W, E))

        process_button = Button(self, text="Process Input", command=process_files).grid(row=5,column=2, padx=10, pady=10)

        # Buttons at the bottom
        button = tk.Button(self, text="Batch Input", command=lambda: controller.show_frame(BatchInput))
        button.grid(row=6,column=0, padx=10, pady=10)

        button2 = tk.Button(self, text="Single Input", command=lambda: controller.show_frame(SingleInput))
        button2.grid(row=6,column=1, padx=10, pady=10)

        button3 = tk.Button(self, text="Quit", command=quit)
        button3.grid(row=6,column=2, padx=10, pady=10)

    # result= run_in_multiple_input_from_file_output_to_file_mode(1,2,3,4)

class SingleInput(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Single Input Page")
        label.grid(columnspan=3, pady=10,padx=100)

        # Process information

        def process_files(**args):

            #Get values
            currencyfile = currencyFile.get() #str(currency_file.get())
            conversionfile = conversionRate.get()
            airportfile = airportFile.get()

            value_1 = homeCode.get()
            value_2 = airport1Code.get()
            value_3 = airport2Code.get()
            value_4 = airport3Code.get()
            value_5 = airport4Code.get()

            # print(currencyfile,conversionfile,airportfile,value_1,value_2,value_3,value_4,value_5)

            trip = Trip("GUI input trip",value_1,value_2,value_3,value_4,value_5)

            airportObject = run_in_single_input_return_output_mode(currencyfile, conversionfile, airportfile, trip)

            # print(type(airportObject))

            if type(airportObject) == str:
                error = airportObject
                cheapestRoute.set(error)
            else:
                if airportObject.trip_processed == True:
                    route = airportObject.route
                    cost = airportObject.cost_of_trip
                    # print(cost)
                    cost = float(cost)
                    cheapestRoute.set("The cheapest route is %s at a cost of %s Euro"  % (route, cost))
                elif airportObject.trip_processed == False:
                    error = airportObject.error_message
                    cheapestRoute.set(error)

# countrycurrency.csv currencyrates.csv airport.csv DUB LHR DXB JFK CDG


        # File Inputs
        currencyFile = StringVar()
        conversionRate = StringVar()
        airportFile = StringVar()

        homeCode = StringVar()
        airport1Code = StringVar()
        airport2Code = StringVar()
        airport3Code = StringVar()
        airport4Code = StringVar()

        cheapestRoute = StringVar()

        # Currency file input

        currency_label = Label(self, text="Currency filename:").grid(row=1,column=0,columnspan=2, sticky=(W))

        currency_file = Entry(self, width=12, textvariable=currencyFile).grid(row=1,column=2,columnspan=2, sticky=(W, E))

        # Conversion rate file input

        conversion_label = Label(self, text="Conversion rates filename:").grid(row=2,column=0,columnspan=2, sticky=(W))

        conversion_file = Entry(self, width=12, textvariable=conversionRate).grid(row=2,column=2,columnspan=2, sticky=(W, E))

        # Airport file input

        currency_label = Label(self, text="Airport data filename:").grid(row=3,column=0,columnspan=2, sticky=(W))

        currency_file = Entry(self, width=12, textvariable=airportFile).grid(row=3,column=2,columnspan=2, sticky=(W, E))

        # Airport Labels

        home_label = Label(self, text="Home airport").grid(row=4,column=0, sticky=(W,E), pady=20)
        airport_1_label = Label(self, text="Airport 1").grid(row=4,column=1, sticky=(W,E), pady=20)
        airport_2_label = Label(self, text="Airport 2").grid(row=4,column=2, sticky=(W,E), pady=20)
        airport_3_label = Label(self, text="Airport 3").grid(row=4,column=3, sticky=(W,E), pady=20)
        airport_4_label = Label(self, text="Airport 4").grid(row=4,column=4, sticky=(W,E), pady=20)

        # Airport file inputs

        home_code = Entry(self, width=9, textvariable=homeCode).grid(row=5,column=0, sticky=(W, E))
        airport_1_code = Entry(self, width=9, textvariable=airport1Code).grid(row=5,column=1, sticky=(W, E))
        airport_2_code = Entry(self, width=9, textvariable=airport2Code).grid(row=5,column=2, sticky=(W, E))
        airport_3_code = Entry(self, width=9, textvariable=airport3Code).grid(row=5,column=3, sticky=(W, E))
        airport_4_code = Entry(self, width=9, textvariable=airport4Code).grid(row=5,column=4, sticky=(W, E))

        # Output and monitor buttons

        output = Label(self, textvariable=cheapestRoute).grid(row=6, columnspan=4, sticky=(W, E))

        process_button = Button(self, text="Find cheapest route", command=process_files).grid(row=6,column=4, padx=10, pady=10)

        # Buttons at the bottom
        button = tk.Button(self, text="Batch Input", command=lambda: controller.show_frame(BatchInput)).grid(row=7,column=1, padx=10, pady=10)

        button2 = tk.Button(self, text="Single Input", command=lambda: controller.show_frame(SingleInput)).grid(row=7,column=2, padx=10, pady=10)

        button3 = tk.Button(self, text="Quit", command=quit).grid(row=7,column=3, padx=10, pady=10)

def launch_gui():
    trips_window = TripProgram()
    trips_window.mainloop()

