# Ask the user to enter a temperature in celcius
celcius = float(input("Enter temperature in Celcius: ")) 
# Covert to Fahrenheit
fahrenheit = (celcius * 9/5) + 32
# Convert to Kelvin 
Kelvin = celcius + 273.15
# Display the results  
print("Fahrenheit: ")
print(fahrenheit)
print("Kelvin:")
print(Kelvin)