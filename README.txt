Simple Reflex Agent for Air Quality Index (AQI)

Description:-
This project implements a Simple Reflex Agent that determines the Air Quality Index (AQI) of a region based on environmental sensor data.
The agent reads pollution parameters from a file and uses condition–action rules to determine the AQI category.

Concept:-
A Simple Reflex Agent selects actions based only on the current percept.

Rule format:
IF condition -> THEN action
In this project:-
*Sensors -> Read environmental data from a file
*Agent Program -> Applies AQI rules
*Actuator -> Displays AQI category

Environmental Parameters:-
The following pollutants are used:
*PM2.5
*PM10
*NO2
*SO2
*CO
These values are stored in a file named "sensor_data.txt".
Example:
85 120 40 25 1

AQI Rules:-
The agent uses PM2.5 levels to determine AQI:

| PM2.5 Range | AQI Category                   |
| ----------- | ------------------------------ |
| 0 - 50      | Good                           |
| 51 - 100    | Moderate                       |
| 101 - 150   | Unhealthy for Sensitive Groups |
| 151 - 200   | Unhealthy                      |
| > 200       | Very Unhealthy                 |

How It Works:-
1.Sensor data is stored in a file.
2.The program reads pollutant values.
3.The agent applies condition-action rules.
4.The AQI category is displayed.

How to Run:-
Compile the program:

gcc aqi_agent.c -o aqi

Run the program:

./aqi

Sample Output:-
 Sensor Readings:
 PM2.5: 85.00
 PM10 : 120.00
 NO2  : 40.00
 SO2  : 25.00
 CO   : 1.00

AQI Category: Moderate

Applications:-
*Environmental monitoring systems
*Smart city pollution monitoring
*Air quality alert systems
