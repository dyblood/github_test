#4.3.1.10 Converting fuel consumption

# 1 American mile = 1609.344 metres;
# 1 American gallon = 3.785411784 litres.

def liters_100km_to_miles_gallon(liters):
    mpg = ((100/liters)*(3.785411784/1.609344)) #converting l/100km => mpg
    return mpg

def miles_gallon_to_liters_100km(miles):
     liters_km = (100*3.785411784)/(1.609344*miles)
     return liters_km


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
