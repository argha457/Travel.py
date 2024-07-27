import math
import requests
import urllib.parse

class Location:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"{self.name} ({self.latitude}, {self.longitude})"

class Route:
    def __init__(self, start_point, end_point, distance):
        self.start_point = start_point
        self.end_point = end_point
        self.distance = distance

    def __str__(self):
        return f"Route from {self.start_point.name} to {self.end_point.name} is {self.distance:.2f} km."

def calculate_distance(loc1, loc2):
    x_distance = loc2.latitude - loc1.latitude
    y_distance = loc2.longitude - loc1.longitude
    return math.sqrt(x_distance**2 + y_distance**2)

def get_weather(city_name, api_key):
    encoded_city_name = urllib.parse.quote(city_name)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={encoded_city_name}&appid={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        weather = data['weather'][0]['description']
        temp_kelvin = data['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        
        return f"Weather: {weather}, Temperature: {temp_celsius:.2f}°C"
    except requests.exceptions.RequestException as e:
        return f"Unable to fetch weather data: {e}"

def get_transport_options(city_name):
    transport_options = {
        "New York": "Subway, Bus, Taxi",
        "Los Angeles": "Metro, Bus, Taxi",
        "Chicago": "Train, Bus, Taxi",
        "San Francisco": "BART, Bus, Taxi",
        "London": "Tube, Bus, Taxi",
        "Paris": "Metro, Bus, Taxi"
    }
    return transport_options.get(city_name, "Bus, Taxi")

def get_hotels(city_name):
    hotels = {
        "New York": "Hotel A, Hotel B, Hotel C",
        "Los Angeles": "Hotel D, Hotel E, Hotel F",
        "Chicago": "Hotel G, Hotel H, Hotel I",
        "San Francisco": "Hotel J, Hotel K, Hotel L",
        "London": "Hotel X, Hotel Y, Hotel Z",
        "Paris": "Hotel P, Hotel Q, Hotel R"
    }
    return hotels.get(city_name, "Hotel M, Hotel N")

def get_shops(city_name):
    shops = {
        "New York": "Shop A, Shop B, Shop C",
        "Los Angeles": "Shop D, Shop E, Shop F",
        "Chicago": "Shop G, Shop H, Shop I",
        "San Francisco": "Shop J, Shop K, Shop L",
        "London": "Shop X, Shop Y, Shop Z",
        "Paris": "Shop P, Shop Q, Shop R"
    }
    return shops.get(city_name, "Shop M, Shop N")

def main():
    print("Starting main function")
    api_key = "your_openweathermap_api_key"
    locations = [
        Location("New York", 40.7128, -74.0060),
        Location("Los Angeles", 34.0522, -118.2437),
        Location("Chicago", 41.8781, -87.6298),
        Location("San Francisco", 37.7749, -122.4194),
        Location("London", 51.5074, -0.1278),
        Location("Paris", 48.8566, 2.3522)
    ]
    
    users = {}
    logged_in = False
    current_user = None
    
    while True:
        print("\nMain Menu:")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")  # Changed from getpass.getpass to input
            users[username] = password
            print("Sign up successful!")
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")  # Changed from getpass.getpass to input
            if users.get(username) == password:
                logged_in = True
                current_user = username
                print("Login successful!")
            else:
                print("Login failed. Incorrect username or password.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        
        if logged_in:
            while logged_in:
                print("\nSelect starting location and destination location:")
                for i, location in enumerate(locations, start=1):
                    print(f"{i}. {location.name}")
                start_choice = int(input("Enter starting location number: ")) - 1
                end_choice = int(input("Enter destination location number: ")) - 1
                
                start_location = locations[start_choice]
                end_location = locations[end_choice]
                
                distance = calculate_distance(start_location, end_location)
                route = Route(start_location, end_location, distance)
                print(route)
                
                print(f"Weather at {start_location.name}: {get_weather(start_location.name, api_key)}")
                print(f"Weather at {end_location.name}: {get_weather(end_location.name, api_key)}")
                
                print(f"Transport options at {start_location.name}: {get_transport_options(start_location.name)}")
                print(f"Transport options at {end_location.name}: {get_transport_options(end_location.name)}")
                
                print(f"Hotels at {start_location.name}: {get_hotels(start_location.name)}")
                print(f"Hotels at {end_location.name}: {get_hotels(end_location.name)}")
                
                print(f"Shops at {start_location.name}: {get_shops(start_location.name)}")
                print(f"Shops at {end_location.name}: {get_shops(end_location.name)}")
                
                print("\nWould you like to book a hotel or transport option?")
                print("1. Book hotel")
                print("2. Book transport option")
                print("3. Plan another trip")
                action_choice = input("Enter your choice: ")
                
                if action_choice == '1':
                    hotel_name = input("Enter hotel name to book: ")
                    nights = int(input("Enter number of nights: "))
                    total_cost = nights * 100.0  # Simulated cost
                    print(f"Hotel booked for {nights} nights. Total cost: ${total_cost:.2f}")
                elif action_choice == '2':
                    transport_option = input("Enter transport option to book: ")
                    tickets = int(input("Enter number of tickets: "))
                    total_cost = tickets * 50.0  # Simulated cost
                    print(f"Transport option booked for {tickets} tickets. Total cost: ${total_cost:.2f}")
                
                print("\n1. Plan another trip")
                print("2. Update password")
                print("3. Logout")
                trip_choice = input("Enter your choice: ")
                
                if trip_choice == '2':
                    current_password = input("Enter current password: ")  # Changed from getpass.getpass to input
                    if users.get(current_user) == current_password:
                        new_password = input("Enter new password: ")  # Changed from getpass.getpass to input
                        users[current_user] = new_password
                        print("Password updated successfully!")
                    else:
                        print("Password update failed. Incorrect current password.")
                elif trip_choice == '3':
                    print("Logging out...")
                    logged_in = False
                    current_user = None

if __name__ == "__main__":
    print("Executing main")
    main()
    print("Finished main")
