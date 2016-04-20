import forecastio

def main():
    api_key = "ad46d12c4858033423cca44ab934c330"
    lat = -13.1955
    lng = 49.0505
    time = "current"

    forecast = forecastio.load_forecast(api_key, lat, lng, time=currently)

    print "===========Currently Data========="
    print forecast.currently()
