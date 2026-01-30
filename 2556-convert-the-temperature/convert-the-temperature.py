class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
       
        y = celsius + 273.15
        z = celsius * 1.80 + 32.00
        return [y, z]
    