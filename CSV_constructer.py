__author__ = "Conor O'Kelly"

import csv

# Customm exceptions to be caught in main()

class CurrencyFileNotFound(Exception):
    pass
class ConversionFileNotFound(Exception):
    pass
class AirportFileNotFound(Exception):
    pass
class TripFileNotFound(Exception):
    pass
class FileNotCorrectlyFormatted(Exception):
    pass



# Each of the three classes will hold the input data in object form from respective files

class Currency:
    def __init__(self, country_name, country_currency, currency_code):
        self.country_name = country_name
        self.country_currency = country_currency
        self.currency_code = currency_code

    def __str__(self):
        return 'Country name is ("%s"), country currency is ("%s"), and currency code is ("%s")' % (self.country_name,
                                                                                                    self.country_currency,
                                                                                                    self.currency_code)

    def get_country_name(self):
        return self.country_name

    def get_currency_code(self):
        return self.currency_code


class Conversion_rates:
    def __init__(self, currency_name, currency_code, conversion_rate):
        self.country_name = currency_name
        self.currency_code = currency_code
        self.conversion_rate = conversion_rate

    def __str__(self):
        return 'Country name is ("%s"), currency code is ("%s") and conversion rate is ("%s")' % (
            self.country_name, self.currency_code, self.conversion_rate)


class AiportBasic:
    def __init__(self, airport_name, country_name, code3, latitude, longitude):
        self.airport_name = airport_name
        self.country_name = country_name
        self.code3 = code3
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return 'Airport name is ("%s"), country name is ("%s"), code3 is ("%s"), latitude is ("%s") and longitude is ("%s")' % (
            self.airport_name, self.country_name, self.code3, self.latitude, self.longitude)


class InputData:
    # Create all of the dictionaries that will hold the objects created from csv files

    __currency_dict = {}
    __conversion_dict = {}
    __airport_dict = {}

    # init will take in the file names and process each file.

    def __init__(self, currency_filename, conversion_rate_filename, airport_filename):
        self.currency_filename = currency_filename
        self.conversion_rate_filename = conversion_rate_filename
        self.airport_filename = airport_filename

        # Use object builder to construct the object dictionaries

        # try:
        try:  #Dealing with file not found erroes
            self.object_builder(currency_filename, "currency")
        except FileNotFoundError:
            # print("Currency for each country file not found. Please check that it has been entered correctly")
            raise CurrencyFileNotFound
        except IndexError:
            raise FileNotCorrectlyFormatted("Currency File")
        try:
            self.object_builder(conversion_rate_filename, "conversion rate")
        except FileNotFoundError:
            # print("Conversion rate file not found. Please check that it has been entered correctly")
            raise ConversionFileNotFound
        except IndexError:
            raise FileNotCorrectlyFormatted("Conversion rate File")

        try:
            self.object_builder(airport_filename, "airport")
        except FileNotFoundError:
            # print("Airport file not found. Please check that it has been entered correctly")
            raise AirportFileNotFound
        except IndexError:
            raise FileNotCorrectlyFormatted("Airport File")

        # except IndexError:
        #     print("The file does not appear to be indexed in the standard format as an index error has occurred.")


        # print("Input has successfully been converted into a dictionary")
        # print(len(self.__airport_dict), "1111")
        # print(len(self.__currency_dict), "222")
        # print(len(self.__conversion_dict), "3333")


    def object_builder(self, filename, type):
        #reader and builder for currency filename

        #reader take in input in utf-8 format and stores it accordingly.

        reader = csv.reader(open(filename, 'rU', encoding='utf-8'))
        for row in reader:
            current_row = row


            if type == "currency":
                # Items assiagned and formated from row
                country_name = current_row[0]
                # country_name = country_name.lower()
                currency_code = current_row[14]
                country_currency = current_row[17]

                # Object created
                currency = Currency(country_name, country_currency, currency_code)
                # print(currency)

                #objects are stored in dict with country name as key
                key = country_name
                self.__currency_dict[key] = currency

            elif type == "conversion rate":
                try:
                    # print("Length of conversion file", len(current_row))
                    # Items assiagned and formated from row
                    currency_name_conversion = current_row[0]
                    # currency_name_conversion = currency_name_conversion.lower()
                    currency_code_conversion = current_row[1]
                    conversion_to_euro = current_row[2]
                    # Convert string to float
                    conversion_to_euro = float(conversion_to_euro)

                    # Object created
                    conversion_rate = Conversion_rates(currency_name_conversion, currency_code_conversion,
                                                       conversion_to_euro)
                    #print(conversion_rate)

                    #objects are stored in dict with currency code as key
                    key = currency_code_conversion
                    self.__conversion_dict[key] = conversion_rate
                except ValueError:
                    print("An Value error occourred converting a string to a float")
                    pass


            elif type == "airport":
                try:
                    # print("Length of airport file", len(current_row))
                    # Items assiagned and formated from row
                    airport_name = current_row[1]
                    country_name_airport = current_row[3]
                    # country_name_airport = country_name_airport.lower()
                    code3 = current_row[4]
                    if len(code3) != 3:
                        raise UserWarning
                    latitude = current_row[6]
                    # Convert strings to floats
                    latitude = float(latitude)
                    longitude = current_row[7]
                    longitude = float(longitude)

                    # Object created
                    airport = AiportBasic(airport_name, country_name_airport, code3, latitude, longitude)
                    # print(airport)

                    #objects are stored in dict with airport code as key
                    key = code3
                    self.__airport_dict[key] = airport
                except ValueError:
                    print("An Value error occourred converting a string to a float for the airport (%s)" % (airport_name))
                    pass
                except UserWarning:
                    print("The 3 letter code for airport (%s) is not 3 letter long. This will most likely cause problems" % (airport_name))


            else:
                print("Internal naming error for typing")



    def find_object(self, term, dict_type):

        #This method will find the object in dict using keys

        # First element allows the picking of a dictionary
        if dict_type == "currency":
            dictionary = self.__currency_dict
        elif dict_type == "conversion":
            dictionary = self.__conversion_dict
        elif dict_type == "airport":
            dictionary = self.__airport_dict
        else:
            print("Internal naming error for dict type finder")

        # Finds the requested object and returns it.
        current_object = dictionary.get(term)
        print(current_object)
        return current_object

    def return_dict(self, dict_type):
        if dict_type == "currency":
            return self.__currency_dict
        elif dict_type == "conversion":
            return self.__conversion_dict
        elif dict_type == "airport":
            return self.__airport_dict
        else:
            print("Internal naming error for dict type finder")


class Airport:

    all_info_available = False

    # Mian airport class that will be used to build the finail airport object
    def __init__(self, airport_code, airport_name, country_name, country_currency, currency_code, conversion_rate,
                 airport_latitude, airport_longitude, all_info_available):
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.country_name = country_name
        self.country_currency = country_currency
        self.currency_code = currency_code
        self.conversion_rate = conversion_rate
        self.airport_latitude = airport_latitude
        self.airport_longitude = airport_longitude
        self.all_info_available = all_info_available

    def __str__(self):
        return """Airport code is ("%s"), airport name is ("%s"), country name is ("%s"),
        country currency is ("%s"), currency code is ("%s"),
        conversion rate is ("%s"),
        latitude is ("%s"), longitude is ("%s")
        and was all information found and input into object = ("%s") \n""" % (self.airport_code, self.airport_name,
                                                            self.country_name,self.country_currency,
                                                            self.currency_code,self.conversion_rate,
                                                            self.airport_latitude, self.airport_longitude,
                                                            self.all_info_available)


class AirportDict:
    __airport_dit = {}

    # Creates an object with all three files stored in it to be used to build the final dictionary
    def __init__(self, currency_filename, conversion_rate_filename, airport_filename):
        objects = InputData(currency_filename, conversion_rate_filename, airport_filename)

        #Assign dict to variables
        currency_dict = objects.return_dict("currency")
        conversion_dict = objects.return_dict("conversion")
        airport_dict = objects.return_dict("airport")

        self.assemble_final_dict(currency_dict, conversion_dict, airport_dict)

    def assemble_final_dict(self, currency_dict, conversion_dict, airport_dict ):
        #Assign each dict object for each csv file
        self.currency_dict = currency_dict
        self.conversion_dict = conversion_dict
        self.airport_dict = airport_dict

        # Create a final airport object for each item in the airport dictionary

        for i in airport_dict:
            current_airport_object = airport_dict.get(i)
            # print(current_airport_object)

            # Assign each variable for airport object

            #Avalibe from current object

            airport_code = current_airport_object.code3
            airport_name = current_airport_object.airport_name
            airport_country = current_airport_object.country_name
            airport_latitude = current_airport_object.latitude
            airport_longitude = current_airport_object.longitude
            all_info_available = False

            # Select the correct currency dictionary by using the current ariports name as key
            current_currency_object = currency_dict.get(current_airport_object.country_name, "No currency found")

            try:
                currency_code = current_currency_object.currency_code
                country_currency = current_currency_object.country_currency
                # print(currency_code,"and", country_currency)
            except:
                currency_code = "No currency code found for this country"
                country_currency = "No currency found for this country"
                # print(currency_code,"and", country_currency)



            #Check if dict is found and assign correct values if it is
            try:
                # Using currency code call correct conversion dict
                current_conversion_object = conversion_dict.get(current_currency_object.currency_code)
                conversion_rate = current_conversion_object.conversion_rate
                all_info_available = True
                # print(conversion_rate, "\n")
            except:
                conversion_rate = "No conversion rate was found"
                all_info_available = False # Test that all information was collected for airport object
                # print(conversion_rate, "\n")

            # Create airport object
            airport_main = Airport(airport_code, airport_name, airport_country ,country_currency,currency_code,conversion_rate, airport_latitude, airport_longitude, all_info_available)
            # print(airport_main, "\n")

            key = airport_code

            # Put in dictionary
            self.__airport_dit[key] = airport_main

        # print(len(self.__airport_dit))

    def assign_airport_object(self, airport_key_code):

        airport_object = self.__airport_dit.get(airport_key_code)
        return airport_object




            # Testing elements

class Trip:
    # Class to build object that will hold information about individual trips requests

    def __init__(self, trip_name, home, airport_1, airport_2, airport_3, airport_4):
        self.trip_name = trip_name
        self.home = home
        self.airport_1 = airport_1
        self.airport_2 = airport_2
        self.airport_3 = airport_3
        self.airport_4 = airport_4

    def __str__(self):
        return '''Persons name is ("%s"), home airport is ("%s"), airport 1 is ("%s"),
        airport 2 is ("%s"), airport 3 is ("%s") and airport 4 is ("%s") \n ''' % (self.trip_name,
                                                                    self.home,self.airport_1, self.airport_2,
                                                                    self.airport_3, self.airport_4)

class TripRequestsDict:
    # Class to hold dict for trip requests and to build it

    __trip_dict_requests = {}

    def __init__(self, trip_requests_file_name):
        self.trip_requests_file_name = trip_requests_file_name

        try:
            self.build_dict(trip_requests_file_name)
            # print("Trips have been accepted")
        except FileNotFoundError:
            # print("The trips file was not found \n")
            raise TripFileNotFound
        # except IndexError:
            # print("Index error has occurred \n")


    def build_dict(self,trip_requests_file_name):
        #reader and builder for trip requests dict

        #reader take in input in utf-8 format and stores it accordingly.
        reader = csv.reader(open(self.trip_requests_file_name, 'rU', encoding='utf-8'))
        for row in reader:
            current_row = row
            name = current_row[0]
            home = current_row[1]
            airport_1 = current_row[2]
            airport_2 = current_row[3]
            airport_3 = current_row[4]
            airport_4 = current_row[5]

            # Construct a trip object using file input
            current_trip = Trip(name, home, airport_1, airport_2, airport_3, airport_4)
            # print(current_trip)

            # Append trip object to dictionary
            key = name
            self.__trip_dict_requests[key] = current_trip
        # print(self.__trip_dict_requests)

    def assign_trip(self,key):
        trip_individual = self.__trip_dict_requests.get(key)
        # print(trip_individual)
        return trip_individual

    def return_dict(self):
        return self.__trip_dict_requests

class CheapestTrip:
    def __init__(self, trip_name, home_name, home_code, route, cost_of_trip, trip_processed, error_message):
        self.trip_name = trip_name
        self.home_name = home_name
        self.home_code = home_code
        self.route = route
        #Format trip cost into formatted float
        self.cost_of_trip = cost_of_trip
        self.trip_processed = trip_processed
        self.error_message = error_message

    def __str__(self):
        return ''''Persons name is (%s), home airport name is "%s), home airport code is (%s), the cheapest route is (%s),
        the trip cost (%s Euro), the trip is valid ("%s") and Error messege = ("%s") \n ''' % (self.trip_name,
                                                                    self.home_name, self.home_code,self.route,self.cost_of_trip,self.trip_processed,self.error_message)



# class DictOfCheapestTrips:
#
#     __cheapest_trip_dict = {}
#
#     def __init__(self, cheapest_trips_dict):
#         self.cheapest_trips_dict = cheapest_trips_dict
#         print("Object has been created")
#
#     def add_trip(self, object):
#         #Assign key based on name of individual
#         key = object.person_name
#         print(key)
#         self.__cheapest_trip_dict[key] = CheapestTrip
#
#     def output_csv_file(self):
#         writer = csv.writer(open("Emmploye_trip_plans",'wU', encoding='utf-8', ))
#         for i in self.__cheapest_trip_dict:
#             object = self.__cheapest_trip_dict.get(i)
#
#             writer.write(object)
#
#     def hello(self):
#         print("hello")


#Tesing elements
#
# request = TripRequestsDict("tripsInput.csv")
#
# cheapestTrip = request.return_dict()
# # print(cheapestTrip)
#
# output_csv_file(cheapestTrip)
#
#


