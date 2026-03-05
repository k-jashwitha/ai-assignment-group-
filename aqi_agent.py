# Simple Reflex Agent for AQI

def main():
    try:
        file = open("sensor_data.txt", "r")
        data = file.read().split()
        file.close()

        pm25 = float(data[0])
        pm10 = float(data[1])
        no2 = float(data[2])
        so2 = float(data[3])
        co = float(data[4])

        print("Sensor Readings:")
        print("PM2.5:", pm25)
        print("PM10 :", pm10)
        print("NO2  :", no2)
        print("SO2  :", so2)
        print("CO   :", co)

        print("\nAQI Category:", end=" ")

        if pm25 <= 50:
            print("Good")
        elif pm25 <= 100:
            print("Moderate")
        elif pm25 <= 150:
            print("Unhealthy for Sensitive Groups")
        elif pm25 <= 200:
            print("Unhealthy")
        else:
            print("Very Unhealthy")

    except FileNotFoundError:
        print("sensor_data.txt file not found")


if __name__ == "__main__":
    main()