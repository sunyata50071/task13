# This program calculates a user's holiday cost for a mystery holiday company.
# The company arranges a 4-5 star hotel and flights for the user. 

print("\nWelcome to the StoryMaker cost calculator.")
print("\nWhich city takes your fancy? This year we have these destinations:")
print("\n1: Osaka, 2: Cairo, 3: Phuket, 4: Peru, 5: Abu Dhabi, 6: Rome")

city_flight = int(input("\nJust enter the number for your desired city:"))
num_nights = int(input("\nHow many nights will you be staying at the hotel?"))

def plane_cost(city_flight):
    """Calculates the flight cost."""
    if city_flight == 1:
        return 820
    elif city_flight == 2:
        return 1100
    elif city_flight == 3:
        return 980
    elif city_flight == 4:
        return 612
    else:
        return 490
    
def hotel_cost(num_nights):
    """Calculates the hotel accommodation fees."""
    return 320 * num_nights

def holiday_cost(city_flight, num_nights):
    """Adds flight, hotel and car rental costs to calculate total holiday.""" 
    return plane_cost(city_flight)+ hotel_cost(num_nights)

total_cost = holiday_cost(city_flight, num_nights)
hotel = hotel_cost(num_nights)
flights = plane_cost(city_flight)

print(f"\nYour next adventure awaits! The total price will be £{total_cost}.")
print(f"\nYour flights are £{flights} and the hotel fees are £{hotel}")

print("\nThanks for booking with StoryMaker.") 
print("Have an awesome time and bring back some awe-inspiring stories!")
