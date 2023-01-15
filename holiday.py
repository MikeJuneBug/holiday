# Function that takes the number of hotel nights and returns total cost of stay.

# When the function is called eg hotel_cost(7), the number of nights, n, comes into the function as an argument.

def hotel_cost(nights):                                # Defines name of the function hotel_cost and argument 'nights'.

    hotel_cost_per_night = 100.00                      # Sets hotel cost to be £100.00 per night.  

    total_hotel_cost = nights * hotel_cost_per_night   # Calculates the total hotel cost (nights x cost per night).

    return total_hotel_cost                            # Returns the total hotel cost.



# Function that takes the city and returns the flight cost.

def plane_cost(city):                                      # Defines name of the function plane_cost and argument 'city'.

    if city == "Barcelona":                                # If statement to choose which price depending on the city
        flight_cost = 200.00
    elif city == "London":
        flight_cost = 100.00
    elif city == "Paris":
        flight_cost = 300.00
    elif city == "Moscow":
        flight_cost = 600.00
    elif city == "Budapest":
        flight_cost = 500.00
    elif city == "Prague":
        flight_cost = 400.00

    return flight_cost                                     # Returns the flight_cost.



# Function that takes the number of car rental days and returns the total cost of rental.

def car_rental_cost(days):                                 # Defines name of the function car_rental_cost and argument 'days'.

    car_rental_cost_per_day = 30.00                        # Sets car rental cost to be £30.00 per day.              
    
    total_car_cost = days * car_rental_cost_per_day        # Calculates the total car cost which is days x cost of rental per day.
    
    return total_car_cost                                  # Returns the total_car_cost.



# Function that takes the number of hotel nights, city and number of car rental days, calculates & returns the total holiday cost.

def holiday_cost(nights, city, days):             # Defines name of the function holiday_cost and the 3 argument 'nights', 'city', 'days'.

    holiday_cost_hotel = hotel_cost(nights)

    holiday_cost_car = car_rental_cost(days)

    holiday_cost_plane =plane_cost(city)    

    total_holiday_cost = holiday_cost_hotel + holiday_cost_car + holiday_cost_plane

    return total_holiday_cost



# Try with 7 nights, Barcelona, 3 days car rental

print('---------------------------------------')
print("Total Holiday Cost Calculator\n7 nights, Barcelona, 3 days of car rental")
print('---------------------------------------')

final_hotel_cost = hotel_cost(7)
print(f"\nHotel: £{final_hotel_cost}")

final_plane_cost = plane_cost("Barcelona")
print(f"\nFlight: £{final_plane_cost}")

final_car_cost = car_rental_cost(3)
print(f"\nCar: £{final_car_cost}")

final_cost = holiday_cost(7,"Barcelona",3)
print('--------------------------------------')
print(f"Final cost: £{final_cost}")
print('--------------------------------------')


# Try with 10 nights, Paris, 4 days car rental

print('---------------------------------------')
print("Total Holiday Cost Calculator\n10 nights, Paris, 4 days of car rental")
print('---------------------------------------')

final_hotel_cost = hotel_cost(10)
print(f"\nHotel: £{final_hotel_cost}")

final_plane_cost = plane_cost("Paris")
print(f"\nFlight: £{final_plane_cost}")

final_car_cost = car_rental_cost(4)
print(f"\nCar: £{final_car_cost}")

final_cost = holiday_cost(10,"Paris",4)
print('---------------------------------------')
print(f"Final cost: £{final_cost}")
print('---------------------------------------')


# Try with 2 nights, London, 1 day car rental

print('---------------------------------------')
print("Total Holiday Cost Calculator\n2 nights, London, 1 day car rental")
print('---------------------------------------')

final_hotel_cost = hotel_cost(2)
print(f"\nHotel: £{final_hotel_cost}")

final_plane_cost = plane_cost("London")
print(f"\nFlight: £{final_plane_cost}")

final_car_cost = car_rental_cost(1)
print(f"\nCar: £{final_car_cost}")

final_cost = holiday_cost(2,"London",1)
print('---------------------------------------')
print(f"Final cost: £{final_cost}")
print('---------------------------------------')
