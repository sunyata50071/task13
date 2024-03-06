# This program calculates a user's holiday cost for a mystery holiday company.
# The company arranges a 4-5 star hotel, car and flights for the user. 

print("\nWelcome to the StoryMaker cost calculator.")
print("\nWhich city takes your fancy? This year we have these destinations:")
print("\n1: Hangzhou, 2: Toulouse, 3: Tokyo, 4: Abu Dhabi, 5: Jordan")

city_flight = int(input("\nJust enter the number for your desired city:"))
num_nights = int(input("\nHow many nights will you be staying at the hotel?"))
rental_days = int(input("\nNeed a car? Enter the number of days or 0 if not:"))

def plane_cost(city_flight):
    """Calculates the flight cost."""
    if city_flight == 1:
        return 1270
    elif city_flight == 2:
        return 699
    elif city_flight == 3:
        return 900
    elif city_flight == 4:
        return 470 
    elif city_flight == 5:
        return 1300
    else:
        return 300
    
def hotel_cost(num_nights):
    """Calculates the hotel accommodation fees."""
    return 320 * num_nights

def car_rental(rental_days):
    """Calculates the total cost for car hire."""
    if rental_days < 5:
        return 180 * rental_days
    else:
        return 120 * rental_days
    
def holiday_cost(city_flight, num_nights, rental_days):
    """Adds flight, hotel and car rental costs to calculate total holiday.""" 
    return plane_cost(city_flight)+ hotel_cost(num_nights)+ car_rental(rental_days)

total_cost = holiday_cost(city_flight, num_nights, rental_days)
hotel = hotel_cost(num_nights)
flights = plane_cost(city_flight)
car = car_rental(rental_days)

print(f"\nYour next adventure awaits! The total price will be £{total_cost}.")

if car == 0:  # Don't include the car price if the user doesn't need one.
    print(f"\nThis includes flights at £{flights} and £{hotel} for accommodation.")
else:
    print(f"\nFlights are £{flights}, hotel fees £{hotel} and the car £{car}.")

print("\nThanks for booking with StoryMaker.") 
print("Have an awesome time and bring back some awe-inspiring stories!")
