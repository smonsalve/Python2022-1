# taxi Fare
# 
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00,  plus $0.25 for every 140 meters traveled.
#  Write a function that takes the distance traveled (in kilometers)
#  as its only parameter and returns the total fare as its only result. Write a main program that demonstrates the function.

# Hint: Taxi fares change over time. Use constants to represent the base fare 
# and the variable portion of the fare so that the program can be updated easily when the rates increase.


BASE = 4.00   # Banderazo
FARE = 0.25   # for each 140 meters

def fare_meters_units(kms):
    return (kms*1000)/140
    #return (kms*1000)//140

def taxi_fare(kms):  # In kilometers
    return (BASE+(fare_meters_units(kms)*FARE))

if __name__ == "__main__":
    # print(fare_meters_units(0.140))
    # print(fare_meters_units(0.280))
    # print(fare_meters_units(1.40))
    # print(fare_meters_units(2.80))

    print(taxi_fare(0.140))
    print(taxi_fare(0.280))
    print(taxi_fare(1.40))
    print(taxi_fare(2.80))
    print(taxi_fare(0.290))