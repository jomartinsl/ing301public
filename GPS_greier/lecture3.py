

class GPSPoint:
    def __init__(self, time: str, lat : float, long : float , height: float):
        self.time = time
        self.lat = lat
        self.long = long
        self.height = height

    today = "lørdag"
    def say_hi():
        print("Hi!")





point = GPSPoint(
    time="2017-08-13T08:57:57.000", 
    lat = 60.376988, 
    long = 5.227082, 
    height = 105.5)

point2 = {"time": "2017-08-13T08:57:57.000",
        "lat"       :  60.376988, 
        "long"      : 5.227082, 
        "height"    :  105.5
        }
print(point.__reduce__)
print("0x0000022BFC16EF10" in dir(point))
print(point2["lat"])
print(point.lat)
"""
# Some weird stuff going on: 
print(type(point))
print(dir(point))
print(point)
print("--------")
print("er lat i denne? ", "lat" in dir(point))
print("food" in dir(point))
print(point.height)
point.foord = "Snikkers"
print(point.foord)"""