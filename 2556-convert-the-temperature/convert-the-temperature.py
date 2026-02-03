class Solution:
    def convertTemperature(self, celsius: float) -> list:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.8 + 32
        return [kelvin, fahrenheit]