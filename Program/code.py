#Author: Sheanli Fernando
#Date: 03/12/2024
#Student ID: 21200717

# Task A: Input Validation
import calendar
def validate_date_input():
#This function collects and validates a date input in DD MM YYYY format, ensuring the user provides valid data.
    
 """
 Prompts the user for a date in DD MM YYYY format, validates the input for:
 - Correct data type
 - Correct range for day, month, and year
 - Valid day for the specific month/year (handles leap years)
 """ 
 while True: # Main validation loop.
  try:     
         # Validation of the day input.
         while True: # Infinite loop to continuously prompt until valid day input is provided
             try:
                 day = int(input("Please enter the day of the survey in the format DD: "))
                 # Prompt user for input and attempt to convert it to an integer
                 if 1 <= day <= 31: # Check if the day is within the valid range (1–31)
                     break  # Exit from this loop once day is valid.
                 else:
                     print("Out of range - values must be in the range 1 and 31.")
                     # Notifying if input is out of valid range
             except ValueError:
                 print("Integer required.")
                 # Notifying if input is not an integer or an empty input(for an example; a string or special characters)

         # Validation of the month input.
         while True: # Infinite loop to continuously prompt until valid month input is provided 
             try:
                 month = int(input("Please enter the month of the survey in the format MM: "))
                 # Prompt user for input and attempt to convert it to an integer
                 if 1 <= month <= 12: # Check if the month is within the valid range (1–12) 
                     break  # Exit from this loop once month is valid.
                 else:
                     print("Out of range - values must be in the range 1 to 12.")
                     # Notifying if input is out of valid range 
             except ValueError:
                 print("Integer required.")
                 # Notifying if input is not an integer or an empty input(for an example; a string or special characters)
 
         # Validation of the year input.
         while True: # Infinite loop to continuously prompt until valid year input is provided 
             try:
                 year = int(input("Please enter the year of the survey in the format YYYY: "))
                 # Prompt user for input and attempt to convert it to an integer 
                 if 2000 <= year <= 2024: # Check if the year is within the valid range (2000–2024) 
                     break  # Exit from this loop once year is valid.
                 else:
                     print("Out of range - values must range from 2000 and 2024.")
                     # Notifying if input is out of valid range 
             except ValueError:
                 print("Integer required.")
                 # Notifying if input is not an integer or an empty input(for an example; a string or special characters)
            
         # Validation of the day with respect to the month and year.(Handling non-uniform month lengths, including leap year edge cases.)
         while True:
             # Get the number of days in the month for the specific year
             days_in_month = calendar.monthrange(year, month)[1]
             # Use `calendar.monthrange` to get the number of days in the month for the given year
             # Reference: https://docs.python.org/3/library/calendar.html#calendar.monthrange  
             if day <= days_in_month: # Check if the day is valid for the specific month and year    
                return day, month, year  # Valid date, return the result 
             else:
                 print(f"Invalid day for the given month/year. The month {month:02} in year {year} has {days_in_month:02} days.")
                 # Notifying that the day input exceeds the maximum allowed days in the month
                 print("Restarting input for day, month, and year...")
                 # Re-prompt the user for a valid day
                 break  # Break out to restart the entire process
  except Exception as e:
   print(f"Unexpected error: {e}")
  
"""
~Using multiple while True Loops in validate_date_input() function.
The function uses multiple while True loops to validate each input (day, month, year) separately. This ensures:
   -Granular Feedback: Errors in one part (e.g., day) are addressed without revalidating others (e.g., month or year).
   -Readability and Modularity: Each input validation is isolated, making the code easier to read and modify.
   -Efficiency: Previously validated inputs aren’t repeatedly checked, streamlining the process.

~Using Exception Handling in Each day, month, year validation loops.
Exception handling is used to manage invalid data types during input conversion (int()). This ensures:
   -Program Stability: Prevents crashes caused by non-numeric input (e.g., letters or special characters).
   -User-Friendly Feedback: Provides clear error messages (e.g., "Integer required.") instead of cryptic tracebacks.
   -Robustness: Handles unexpected input gracefully, ensuring the program remains functional and responsive.
"""

def validate_continue_input():
#This function validates the user's input for whether they want to load another dataset, ensuring the response is either 'Y' or 'N'.

    """
    Prompts the user to decide whether to load another dataset:
    -Validates "Y" or "N" input
    """
    while True:
        continue_input = input("Do you want to select another data file for a different date? Y/N:").strip().upper()
        #The strip() method removes any leading, and trailing whitespaces.
        #Reference: https://www.w3schools.com/python/ref_string_strip.asp
        #The upper() method makes the input case-insensitive.If user enter a 'y',It will return as 'Y'.
        #Reference: https://www.w3schools.com/python/ref_string_upper.asp
        if continue_input == "Y" or continue_input == "N": # Check if the input is either "Y" or "N"    
            return continue_input
            # Return the valid input and exit loop
        else:
            print('Please enter "Y" or "N"')
            # Notifying that the input is invalid or an empty input

# Task B: Processed Outcomes
import csv

def process_csv_data(file_path):
# Defines the function 'process_csv_data()' that takes a single argument, file_path, which represents the path to traffic_data{selected_date}.csv files.

  try: # Starts a try block to handle exceptions that may arise during file processing (e.g., FileNotFoundError).
      outcomes = {}
      total_vehicles = 0
      total_trucks = 0
      total_bicycle = 0
      total_electric_vehicles = 0
      two_wheeled_vehicles = 0
      buses_north = 0
      no_turns = 0
      speeding_vehicles = 0
      vehicles_elm = 0
      vehicles_hanley = 0
      scooters_elm = 0
      hours_with_rain = 0
      peak_hour_vehicles = [0] * 24

      """
      ~Initializes variables to store outcomes and counts:
         -outcomes: A dictionary to hold the processed results.
         -total_vehicles, total_trucks, etc.: Counters for various vehicle types and conditions.
         -peak_hour_vehicles: A list of size 24 initialized to 0 to track the number of vehicles per hour.
      """

      with open(file_path, 'r') as file: # Opens the file at file_path in read mode ('r') and assigns it to file.
          reader = csv.DictReader(file)
          # Creates a CSV reader object (reader) that parses each row into a dictionary, where the column headers are keys.
          # Reference : https://docs.python.org/3/library/csv.html#csv.DictReader 

          for row in reader: # Loops through each row of the CSV file. Each row is represented as a dictionary
              total_vehicles += 1
              # Increments total_vehicles for every row, counting all vehicles
              
              # Using get() to avoid KeyError
              """
              With get(): The code is more robust and can handle missing or malformed CSV rows gracefully.
              Without get(): The program will raise KeyError whenever a key is missing, which can cause it to terminate unexpectedly.
              for an example: row.get('VehicleSpeed')  # Returns `None` if 'VehicleSpeed' is missing
                              row['VehicleSpeed']      # Raises KeyError if 'VehicleSpeed' is missing
              """
              # Count vehicle types
              if row.get('VehicleType') == 'Truck':
                  total_trucks += 1

              if row.get('VehicleType') == 'Bicycle':
                  total_bicycle += 1

              if row.get('elctricHybrid') == 'True':
                  total_electric_vehicles += 1

              if row.get('VehicleType') in ['Bicycle', 'Motorcycle', 'Scooter']:
                  two_wheeled_vehicles += 1
                  
              # Count buses leaving Elm Avenue/Rabbit Road heading North
              if row.get('JunctionName') == 'Elm Avenue/Rabbit Road' and row.get('travel_Direction_out') == 'N' and row.get('VehicleType') == 'Buss':
                  buses_north += 1
                  
              # Count vehicles Making No Turns
              # Counts vehicles where the travel direction in matches the travel direction out, indicating no turns.
              if row.get('travel_Direction_in') == row.get('travel_Direction_out'): 
                  no_turns += 1
                  
              #Count speeding vehicles
              """
              ~Compares vehicle speed (VehicleSpeed) with the speed limit (JunctionSpeedLimit):
                 -If vehicle speed is greater, increments speeding_vehicles.
                 -Handles invalid or missing speed values with a ValueError exception.
              """
              try:
                  if int(row.get('VehicleSpeed', 0)) > int(row.get('JunctionSpeedLimit', 0)):
                      speeding_vehicles += 1
              except (ValueError, TypeError):
                  continue  # Skip rows with invalid or missing speed/limit values
              """
              ~The default value 0 in row.get('VehicleSpeed', 0) and row.get('JunctionSpeedLimit', 0) ensures the program handles missing
               or invalid data in the CSV file safely. Without it:
                  -Missing Data: If VehicleSpeed or JunctionSpeedLimit is not in the row, the program would crash with a TypeError.
                  -Invalid Data: If the value is non-numeric, the program would crash with a ValueError.
              """
              
              # Counts vehicles passing through specific junctions
              if row.get('JunctionName') == 'Elm Avenue/Rabbit Road':
                  vehicles_elm += 1

              if row.get('JunctionName') == 'Hanley Highway/Westway':
                  vehicles_hanley += 1
                  
              # Counts scooters passing through Elm Avenue/Rabbit Road 
              if row.get('JunctionName') == 'Elm Avenue/Rabbit Road' and row.get('VehicleType') == 'Scooter':
                  scooters_elm += 1
                  
              # Count hours for the selected date 
              if row.get('Weather_Conditions') == 'Rain':
                  hours_with_rain += 1
                  
              # Count the number of vehicles passing through "Hanley Highway/Westway" junction during each hour of the day.
              try:
                  hour = int(row.get('timeOfDay', '').split(':')[0])
                  """
                  row.get('timeOfDay', ''): Retrieves the timeOfDay value from the row dictionary. If the key does not exist, it defaults to an empty string ('').
                  .split(':'): Splits the string into parts using the colon (:) as a delimiter. For example, '14:30' becomes ['14', '30'].
                  int(...[0]): Converts the first part (the hour) into an integer. For instance, '14' is converted to 14.
                  """
                  if row.get('JunctionName') == 'Hanley Highway/Westway': #  Only rows with this junction name are processed further.
                      peak_hour_vehicles[hour] += 1 # Increments the count of vehicles for the given hour in the peak_hour_vehicles dictionary.
              except (ValueError, IndexError):
                  continue
              # The try-except block ensures that the program doesn't crash due to such issues.

      # Populates the 'outcomes' dictionary with calculated results like totals, percentages, and averages.
      outcomes['total_vehicles'] = total_vehicles
      outcomes['total_trucks'] = total_trucks
      outcomes['total_bicycle'] = total_bicycle
      outcomes['total_electric_vehicles'] = total_electric_vehicles
      outcomes['two_wheeled_vehicles'] = two_wheeled_vehicles
      outcomes['buses_north'] = buses_north
      outcomes['no_turns'] = no_turns
      outcomes['trucks_percent'] = round((total_trucks / total_vehicles) * 100) if total_vehicles > 0 else 0 # Handling ZeroDivisionError
      outcomes['num_of_bikes_per_hour'] = round(total_bicycle / 24)
      outcomes['speeding_vehicles'] = speeding_vehicles
      outcomes['vehicles_elm'] = vehicles_elm
      outcomes['vehicles_hanley'] = vehicles_hanley
      outcomes['scooters_elm'] = scooters_elm
      outcomes['scooters_elm_percent'] = int((scooters_elm / vehicles_elm) * 100) if vehicles_elm > 0 else 0 # Handling ZeroDivisionError
      outcomes['hours_with_rain'] = hours_with_rain
      
      # Finds the hour with the maximum number of vehicles (peak_hour).
      peak_hour = 0
      max_vehicles = peak_hour_vehicles[0]
      for i in range(1, 24):
         if peak_hour_vehicles[i] > max_vehicles:
              peak_hour = i
              max_vehicles = peak_hour_vehicles[i]
      # Formats the peak times as a list of readable strings.        
      outcomes['peak_hour'] = peak_hour_vehicles[peak_hour]
      outcomes['peak_times'] = [f"Between {hour:02}:00 and {hour + 1:02}:00" for hour in range(24) if
                              peak_hour_vehicles[hour] == peak_hour_vehicles[peak_hour]]
      
      outcomes['file'] = file_path  # Add the selected file name to the outcomes

      return outcomes
  except FileNotFoundError:
      print(f"Error: The file '{file_path}' was not found.")
      return None
# Handles missing file errors by printing an error message and returning None.


def display_outcomes(outcomes):
    if outcomes is None:
        print("Error: No valid data to display. The CSV file was not processed successfully.")
        return  # Exit the function early if outcomes are invalid

    outcome_data = ("***************************\n"
            f"data file selected is {outcomes['file']}\n"
            "***************************\n"
            f"The total number of vehicles recorded for this date is {outcomes['total_vehicles']}\n"
            f"The total number of trucks recorded for this date is {outcomes['total_trucks']}\n"
            f"The total number of electric vehicles for this date is {outcomes['total_electric_vehicles']}\n"
            f"The total number of two-wheeled vehicles for this date is {outcomes['two_wheeled_vehicles']}\n"
            f"The total number of Buses leaving Elm Avenue/Rabbit Road heading North is {outcomes['buses_north']}\n"
            f"The total number of Vehicles through both junctions not turning left or right is {outcomes['no_turns']}\n"
            f"The percentage of total vehicles recorded that are trucks for this date is {outcomes['trucks_percent']}%\n"
            f"The average number of Bikes per hour for this date is {outcomes['num_of_bikes_per_hour']}\n\n"
            f"The total number of Vehicles recorded as over the speed limit for this date is {outcomes['speeding_vehicles']}\n"
            f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {outcomes['vehicles_elm']}\n"
            f"The total number of vehicles recorded through Hanley Highway/Westway junction is {outcomes['vehicles_hanley']}\n"
            f"{outcomes['scooters_elm_percent']}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.\n\n"
            f"The highest number of vehicles in an hour on Hanley Highway/Westway is {outcomes['peak_hour']}\n"
            f"The most vehicles through Hanley Highway/Westway were recorded {', '.join(outcomes['peak_times'])}\n" 
            f"The number of hours of rain for this date is {outcomes['hours_with_rain']}\n\n")
    print(outcome_data)
    # .join(): If there are mutiple peak_hours. It will Combines all elements in the list into a single string,
    #                                            with ', ' (a comma followed by a space) used as the separator.


# Task C: Save Result to Text File

def save_results_to_file(outcomes, file_name="results.txt"):
 """
 This function takes two parameters:
 outcomes: A dictionary containing all the computed results.
 file_name: The name of the text file where the results will be saved.
 """
 try:    
    # Constructing the data string
    data=( "***************************\n"
        f"data file selected is {outcomes['file']}\n"
        "***************************\n"
        f"The total number of vehicles recorded for this date is {outcomes['total_vehicles']}\n"
        f"The total number of trucks recorded for this date is {outcomes['total_trucks']}\n"
        f"The total number of electric vehicles for this date is {outcomes['total_electric_vehicles']}\n"
        f"The total number of two-wheeled vehicles for this date is {outcomes['two_wheeled_vehicles']}\n"
        f"The total number of Buses leaving Elm Avenue/Rabbit Road heading North is {outcomes['buses_north']}\n"
        f"The total number of Vehicles through both junctions not turning left or right is {outcomes['no_turns']}\n"
        f"The percentage of total vehicles recorded that are trucks for this date is {outcomes['trucks_percent']}%\n"
        f"The average number of Bikes per hour for this date is {outcomes['num_of_bikes_per_hour']}\n\n"   
        f"The total number of Vehicles recorded as over the speed limit for this date is {outcomes['speeding_vehicles']}\n"
        f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {outcomes['vehicles_elm']}\n"
        f"The total number of vehicles recorded through Hanley Highway/Westway junction is {outcomes['vehicles_hanley']}\n"
        f"{outcomes['scooters_elm_percent']}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.\n\n"  
        f"The highest number of vehicles in an hour on Hanley Highway/Westway is {outcomes['peak_hour']}\n"
        f"The most vehicles through Hanley Highway/Westway were recorded {', '.join(outcomes['peak_times'])}\n"
        f"The number of hours of rain for this date is {outcomes['hours_with_rain']}\n\n")

    with open(file_name, 'a') as file:
    # Opens the file specified by file_name (default: "results.txt").
    # Mode: 'a' (append mode): Ensures that the new results are added to the end of the file without overwriting existing data.   
        file.write(data) # The constructed data string is written to the file
    print(f"Data successfully saved to {file_name}")
    
 except Exception as e:
        print(f"Error saving results to {file_name}: {e}")     
        
 """
 ~ Using "with" statement
    -The with statement ensures that the file is properly closed after writing, even if an error occurs during the process.
    -No need to manually call file.close().
 """

# if you have contracted to do this assignment please do not remove this line

# Task D: Histogram Display
import tkinter as tk
from tkinter import Canvas


class HistogramApp:
    def __init__(self, traffic_data, date):
        # traffic_data: A dictionary holding hourly vehicle counts for two junctions.
        """
        Initializes the histogram application with the traffic data and selected date.
        """
        self.traffic_data = traffic_data
        self.date = date
        self.root = tk.Tk()
        self.root.title(f"Traffic Histogram for {date}")
        self.canvas = None
        # Initializes key attributes (traffic_data, date, root, and canvas) for the histogram display.


    def setup_window(self):
        """
        Sets up the tkinter window and canvas for the histogram.
        """
        self.canvas = Canvas(self.root, width=1200, height=600, bg="#FEF5E7")
        # Canvas: The area where the histogram will be drawn.
        # Dimensions: 1200x600 pixels.
        # Background: A light beige color (#FEF5E7).
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_text(350, 50,text=f"Histogram of Vehicles Frequency per Hour ({self.date})",font=("Arial", 18, "bold"),fill="#626567")

    def draw_histogram(self): 
        """
        Draws the histogram with axes, labels, and bars.
        """

        colors = {"Elm Avenue/Rabbit Road": "#58D68D", "Hanley Highway/Westway": "#FA8072"}
        # Defines colors for the bars of each junction:
          # -Green (#58D68D) for Elm Avenue/Rabbit Road.
          # -Red (#FA8072) for Hanley Highway/Westway.

        # Finds the maximum hourly vehicle count across all junctions. This helps scale the histogram bars proportionally.
        max_vehicle_count = max(max(vehicle_counts) for vehicle_counts in self.traffic_data.values())

        max_height = 300

        bar_width = 18 # bar_width: Width of each bar.
        group_width = len(colors) * (bar_width + 5) # group_width: Total width of a group of bars (one bar for each junction per hour).
        x = 50
        y = 500

        # Draw axes
        self.canvas.create_line(x , y , x + 24 * group_width, y , width=1, fill="#626567")

        # X-axis label
        self.canvas.create_text(x + 24 * group_width // 2, y + 40,
                                text="Hours 00:00 to 24:00",
                                font=("Arial", 12),
                                fill="#626567")

        # Draw bars
        for hour in range(24):
            x_start = x + hour * group_width
            for i, (junction_name, color) in enumerate(colors.items()):
            # Reference: https://chatgpt.com/share/6769db56-4b88-8011-8f64-c7bf01220af1    
                vehicle_count = self.traffic_data[junction_name][hour]
                height = (float(vehicle_count) / float(max_vehicle_count)) * max_height
                bar_x1 = x_start + i * (bar_width + 0)
                bar_x2 = bar_x1 + bar_width
                bar_y1 = y - height
                self.canvas.create_rectangle(bar_x1, y , bar_x2, bar_y1,
                                             fill=color,
                                             stipple="gray75",
                                             outline=color,
                                             width=2)
                
                # Label on top of each bar
                self.canvas.create_text((bar_x1 + bar_x2) // 2, bar_y1 - 10,
                                        text=str(vehicle_count),
                                        font=("Arial", 10),
                                        fill="#626567")

        # Add hour labels
        for hour in range(24):
            self.canvas.create_text(
                x + hour * group_width + group_width // 2,
                y + 20,
                text=f"{hour:02}",
                font=("Arial", 10),
                 fill="#626567")
        # add a label
        self.canvas.create_text(600,30, text='Histogram traffic data viewer',font=("Arial",10),fill="#626567")

    def add_legend(self):
        """
        Adds a legend to the histogram.
        """
        x_legend = 55
        y_legend = 70
        legend_items = [("Elm Avenue/Rabbit Road", "#58D68D"), ("Hanley Highway/Westway", "#FA8072")]
        for i, (label, color) in enumerate(legend_items):
        # Reference: https://chatgpt.com/share/6769db56-4b88-8011-8f64-c7bf01220af1    
            self.canvas.create_rectangle(x_legend, y_legend + i * 30, x_legend + 20, y_legend + 20 + i * 30,
                                         fill=color,
                                         stipple="gray75",
                                         outline=color,
                                         width=2)
            # Add legend labels
            self.canvas.create_text(x_legend + 30, y_legend + 10 + i * 30,
                                    text=label, anchor="w",
                                    font=("Arial", 12),
                                    fill="#626567")

    def run(self):
        """
        Runs the tkinter main loop to display the histogram.
        """
        self.setup_window()
        self.draw_histogram()
        self.add_legend()
        self.root.mainloop()


# Task E: Code Loops to Handle Multiple CSV File.
class MultiCSVProcessor:
    def __init__(self):
        """
        Initializes the processor for handling multiple CSV files.
        """
        self.traffic_data = None

    def load_csv_file(self, selected_date):

        """
        Loads a CSV file based on the selected date and processes its data into a traffic dictionary.
        """
        # Construct the file path dynamically
        file_path = f"traffic_data{selected_date}.csv"

        try:
            # Initialize traffic data
            traffic_data = {"Elm Avenue/Rabbit Road": [0] * 24, "Hanley Highway/Westway": [0] * 24}
            with open(file_path, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    time_of_day = row.get('timeOfDay')
                    if time_of_day and ':' in time_of_day:
                        try:
                            hour = int(time_of_day.split(':')[0])
                            junction_name = row.get('JunctionName')
                            if junction_name in traffic_data:
                                traffic_data[junction_name][hour] += 1
                        except ValueError:
                            continue
            self.traffic_data = traffic_data
            print(f"Successfully loaded data from {file_path}")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found. Please check the date and try again.")
        except Exception as e:
            print(f"Error loading file: {e}")

    def clear_previous_data(self):
        # clears dats from the previous run to process a new dataset.
        self.traffic_data = None  # Reset the traffic_data to None to clear it
        print("Previous data has been cleared.")

    def handle_user_interaction(self):
        """
        Handles user input for processing multiple files.
        Allows the user to load and process multiple CSV files based on the selected dates.
        """
        while True:
            # Step 1: Validate Date Input
            print("Please enter the date of the survey.")
            day, month, year = validate_date_input()

            # Step 2: Construct the file path using the validated date
            selected_date = f"{day:02}{month:02}{year}"
            file_path = f"traffic_data{selected_date}.csv"
            self.load_csv_file(selected_date)

            # Step 3: Process CSV Data
            outcomes = process_csv_data(file_path)

            if outcomes:
                # Step 4: Display Outcomes
                display_outcomes(outcomes)
                save_results_to_file(outcomes)

                # Step 5: Display Histogram
                histogram_app = HistogramApp(self.traffic_data, f"{day:02}/{month:02}/{year}")
                histogram_app.run()
                break


    def process_files(self):
        """
        Main loop for handling multiple CSV files until the user decides to quit.
        """
        while True:
            # Start the interaction with the user for processing files
            self.handle_user_interaction()

            # After processing one file, ask if the user wants to process another file
            continue_input = validate_continue_input()
            if continue_input == "N":
                print("End of run")
                break
            else:
                # If the user chooses "Y", clear previous data before loading new dataset.
                self.clear_previous_data()

# Main Program Execution
if __name__ == "__main__":
    program = MultiCSVProcessor()
    program.process_files()



