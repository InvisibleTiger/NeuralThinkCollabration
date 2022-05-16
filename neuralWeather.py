from pyowm import OWM
from geopy import Nominatim
from datetime import datetime

class NeuralWeather():
    __location = "Allen, US"
    api_key = "7fa2ed4ff726fa39bca6c70db661020c"

    def __init__(self):
        self.ow = OWM(self.api_key)
        self.mgr = self.ow.weather_manager()
        locator = Nominatim(user_agent="blah")
        city = "Allen"
        country = "US"
        self.__location = str(city + ", " + country)
        loc = locator.geocode(self.__location)
        self.lat = loc.latitude
        self.long = loc.longitude

    def neuralUv_index(self, uvi:int):
        """ Returns a message depending on the UV Index provided """
        message = ""
        if uvi <= 2.0:
            message = "The Ultraviolet level is low, no protection is required."
        if uvi >= 3.0 and uvi <6.0:
            message = "The Ultraviolet level is medium, skin protection is required."
        if uvi >= 6.0 and uvi <8.0:
            message = "The Ultraviolet level is high, skin protection is required."
        if uvi >= 8.0 and uvi <11.0:
            message = "The Ultraviolet level is very high, extra skin protection is required."
        if uvi >= 11.0:
            message = "The Ultraviolet level is extremely high, caution is advised and extra skin protection is required."
        return message

    @property
    def weather(self):
        forecast = self.mgr.one_call(lat=self.lat, lon=self.long)
        return forecast

    @property
    def forecast(self):
        forecast = self.mgr.one_call(lat=self.lat, lon=self.long)
        detail_status = str(forecast.forecast_daily[0].detailed_status)
        pressure = str(forecast.forecast_daily[0].pressure.get("press"))
        humidity = str(forecast.forecast_daily[0].humidity)
        sunrise = str(datetime.utcfromtimestamp(forecast.forecast_daily[0].sunrise_time()).strftime("%H:%M:%S"))
        sunset = str(datetime.utcfromtimestamp(forecast.forecast_daily[0].sunset_time()).strftime("%H:%M:%S"))
        temperature = str(forecast.forecast_daily[0].temperature("celsius").get("day"))
        uviPre = int(forecast.forecast_daily[0].uvi)

        #print('detailed status: ', detail_status)
        #print("humidity ", humidity)
        #print("pressure ", pressure)
        #print("sunrise: ", sunrise)
        #print("Sunset ", sunset)
        #print("temperature", temperature)
        #print("UVI ", self.uv_index(uvi))
        
        if uviPre <= 2:
            mess = "The Ultraviolet level is low, no protection is required."
        elif uviPre >= 3 and uviPre <6:
            mess = "The Ultraviolet level is medium, skin protection is required."
        elif uviPre >= 6 and uviPre <8:
            mess = "The Ultraviolet level is high, skin protection is required."
        elif uviPre >= 8 and uviPre <11:
            mess = "The Ultraviolet level is very high, extra skin protection is required."
        elif uviPre >= 11:
            mess = "The Ultraviolet level is extremely high, caution is advised and extra skin protection is required."
        
        """
        message = "Here is the Weather: Today will be mostly " + detail_status \
                + ", humidity of " + humidity + " percent" \
                + " and a pressure of " + pressure + " millibars" \
                + " the temperature is " + temperature + "degrees" \
                + ". Sunrise was at " + sunrise \
                + " and sunset is at " + sunset \
        """
        message = str("Here is the Weather: Today will be mostly " + detail_status + ", humidity of " + humidity + " percent" + " and a pressure of " + pressure + " millibars" + " the temperature is " + temperature + "degrees" + ". Sunrise was at " + sunrise + " and sunset is at " + sunset + ". " + mess)
        
        #print(message)
        return message
"""
myweather = Weather()
print(myweather.forecast)
"""