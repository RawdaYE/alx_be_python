CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

try:
    temprature = float(input("Enter the temperature to convert: "))
    unit = (input("Is this temperature in Celsius or Fahrenheit? (C/F): ")).upper().strip()

    if unit == "F":
        converted = convert_to_celsius(temprature)
        print(f"{temprature}°F is {converted}°C")
    elif unit == "C":
        converted = convert_to_fahrenheit(temprature)
        print(f"{temprature}°C is {converted}°F")
    else: 
        print("IInvalid unit. Please enter 'C' or 'F'.")
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")