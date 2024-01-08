import math

class GeoLocation:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        #print(self.latitude)
        self.longitude = longitude

    def inc_min(self,check,minutes):
        """
        Increment latitude and longitude based on a given number of minutes.

        Parameters:
        - minutes: Number of minutes to increment.

        Returns:
        - A new GeoLocation object with incremented latitude and longitude.
        """
        # Earth's radius in kilometers
        R = 6371

        # Convert latitude and longitude from degrees to radians
        if(check == "lat"):
            rad = math.radians(self.latitude)
        elif(check == "lng"):
            rad = math.radians(self.longitude)
        
        

        # Convert minutes to kilometers (1 minute of latitude is approximately 1 nautical mile)
        distance = (minutes / 60.0) * 1.852

        # Calculate new latitude
        new_rad = rad + (distance / R)

        # Calculate new longitude
        # For simplicity, we assume constant longitude movement (may not be accurate near the poles)
   

        # Convert new latitude and longitude back to degrees
        new_val = math.degrees(new_rad)
        

        # Create and return a new GeoLocation object with incremented values
        if(check == "lat"):
            #print("lat")
            self.updt_lat(round(new_val,4))
        elif(check == "lng"):
            #print("lng")
            self.updt_lng(round(new_val,4))
            
        
    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"
    
    def lat(self) -> float:
        return (float)(self.latitude)
    
    def lng(self) -> float:
        return (float)(self.longitude)
    
    def updt_lat(self,var):
        self.latitude = var
    
    def updt_lng(self,var):
        self.longitude = var