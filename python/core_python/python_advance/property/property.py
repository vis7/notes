'''
This program illusrate and provide notes for use of property
reference - https://www.programiz.com/python-programming/property
'''

class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature
    
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
    # getter
    def get_temperature(self):
        print('getting value of temperature ...')
        return self._temperature
    
    # setter
    def set_temperature(self, temperature):
        if temperature < -273.15:
            raise ValueError("Temperature below absolute zero (-273.15) is not possible")
        print('setting property ...')
        self._temperature = temperature
    
    temperature = property(get_temperature, set_temperature)

human = Celsius(38)

# testing the code
# getting value
human.temperature

print(human.to_fahrenheit())

# setting temperature below absolute zero
human.temperature = -274

print('this statement should not print ...')
