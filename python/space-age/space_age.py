class SpaceAge:
    def __init__(self, seconds):
        self.earth_year = 31557600  # Earth year in seconds
        self.age = seconds          # Person's age in seconds
    def aging(self, factor):        # Coverts age by a factor
        return round(self.age/(self.earth_year * factor),2)
                                    # Return age on other planets
    def on_earth(self):             return self.aging(1) 
    def on_mercury(self):           return self.aging(0.2408467)
    def on_venus(self):             return self.aging(0.61519726)
    def on_mars(self):              return self.aging(1.8808158)
    def on_jupiter(self):           return self.aging(11.862615)
    def on_saturn(self):            return self.aging(29.447498)
    def on_uranus(self):            return self.aging(84.016846)
    def on_neptune(self):           return self.aging(164.79132)