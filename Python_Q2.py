# Complete the Temperature class in temperature.py that converts between Celsius and Fahrenheit.
# Then use this class in driver.py to test temperature conversions.
# Follow the TODO comments in both files for step-by-step instructions.
#
# Print each conversion as [celsius]°C is [fahrenheit]°F, with the Celsius value
# exactly as it was given and the Fahrenheit value as Python computes it.
# Do not round or format the numbers.


class Temperature:
    def __init__(self, celsius):
        # Store the temperature, but use the setter for validation
        self.celsius = celsius

    # TODO: Create a property decorator for celsius that returns self._celsius
    @property
    def celsius(self):
        return self._celsius

    # TODO: Create a celsius.setter that validates the temperature is above absolute zero (-273.15°C)
    # TODO: If value < -273.15, raise ValueError with message "Temperature cannot be below absolute zero (-273.15°C)"
    # TODO: Otherwise, set self._celsius to the value
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
            # print("Temperature cannot be below absolute zero (-273.15°C)")
        else:
            self._celsius = value

    # TODO: Create a property decorator for fahrenheit that converts Celsius to Fahrenheit
    # TODO: Use the formula: F = C × 9/5 + 32
    @property
    def fahrenheit(self):
        fahrenheit = self.celsius * 9/5 + 32
        return fahrenheit

    # TODO: Create a fahrenheit.setter that converts Fahrenheit to Celsius
    # TODO: Use the formula: C = (F - 32) × 5/9
    # TODO: Set self.celsius to this converted value (this will use your celsius setter for validation)
    @fahrenheit.setter
    def fahrenheit(self, value):
        celsius = (value - 32) * 5/9
        self.celsius = celsius


# TODO: Import the Temperature class from the temperature module
# from temperature import Temperature

# Test the class:
# TODO: Create a temperature instance at 25°C
temp = Temperature(25)  # Replace with actual Temperature instance

# TODO: Print both Celsius and Fahrenheit values
# TODO: Use the format: "25.0°C is 77.0°F"
print(f"{temp.celsius}°C is {temp.fahrenheit}°F")

# TODO: Set the temperature to 98.6°F
temp.fahrenheit = 98.6
# Temperature.fahrenheit(98.6)

# TODO: Print both values again to confirm the conversion works
# TODO: Use the same format as before
print(f"{temp.celsius}°C is {temp.fahrenheit}°F")
