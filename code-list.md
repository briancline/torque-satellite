OBDII Codes and Torque Real-time HTTP Keys
==========================================

The following **work-in-progress** tables list known OBDII codes and their
equivalent keys when POSTed to an HTTP endpoint.


Basic Torque Data
-----------------

| Description                             |    OBDII  |  Torque |
|-----------------------------------------|----------:|--------:|
| Timestamp                               |           |    time |
| Device ID                               |           |      id |
| Session ID                              |           | session |


Vehicle Instrumentation
-----------------------

| Description                             |    OBDII  |  Torque |
|-----------------------------------------|----------:|--------:|
| Absolute Throttle Position B            |       47  |     k47 |
| Accelerator Pedal Position D            |       49  |     k49 |
| Accelerator Pedal Position E            |       4a  |     k4a |
| Air Fuel Ratio, Commanded               |           | kff124d |
| Air Fuel Ratio, Measured                |           | kff1249 |
| Ambient Air Temp                        |       46  |     k46 |
| Average trip speed, moving only         |           | kff1263 |
| Average trip speed, all                 |           | kff1272 |
| Barometric Pressure, from vehicle       |       33  |     k33 |
| Catalyst Temp, Bank 1 Sensor 1          |       3c  |     k3c |
| Catalyst Temp, Bank 1 Sensor 2          |       3e  |     k3e |
| Commanded Equivalence Ratio             |       44  |     k44 |
| Engine Coolant Temp                     |       05  |     k05 |
| Engine Load                             |       04  |     k04 |
| Engine Load, Absolute                   |       43  |     k43 |
| Engine RPM                              |       0c  |     k0c |
| Evap System Vapour Pressure             |       32  |     k32 |
| Fuel Level, per ECU                     |       2f  |     k2f |
| Fuel Trim Bank 1, Long Term             |       07  |     k07 |
| Fuel Trim Bank 1, Short Term            |       06  |     k06 |
| GPS vs OBD Speed Difference             |           | kff1237 |
| Horsepower, at wheels calc              |           | kff1226 |
| Intake Air Temp                         |       0f  |     k0f |
| Intake Manifold Pressure                |       0b  |     k0b |
| O2 Sensor 1 Equivalence Ratio, alt.     |       34  |     k34 |
| O2 Volts Bank 1 Sensor 2                |           | kff1215 |
| Relative Throttle Position              |       45  |     k45 |
| Speed, GPS                              |           | kff1001 |
| Speed, OBD                              |       0d  |     k0d |
| Throttle Position, Manifold             |       11  |     k11 |
| Timing Advance                          |       0e  |     k0e |
| Torque                                  |           | kff1225 |
| Turbo Boost & Vacuum Gauge              |           | kff1202 |
| Voltage, Control Module                 |       42  |     k42 |
| Voltage, OBD Adapter                    |           | kff1238 |


Other Instrumentation
---------------------

| Description                             |    OBDII  |  Torque |
|-----------------------------------------|----------:|--------:|
| Acceleration Sensor, Total              |           | kff1223 |
| Acceleration Sensor, X                  |           | kff1220 |
| Acceleration Sensor, Y                  |           | kff1221 |
| Acceleration Sensor, Z                  |           | kff1222 |


Saved Measurements
------------------

| Description                             |    OBDII  |  Torque |
|-----------------------------------------|----------:|--------:|
| 0-60 MPH Time                           |           | kff122d |
| 1/4 Mile Time                           |           | kff122f |
| 1/8 Mile Time                           |           | kff1230 |
| 40-60 MPH Time                          |           | kff1260 |
| 60-0 MPH Time                           |           | kff1265 |
| 60-120 MPH Time                         |           | kff125e |
| 60-80 MPH Time                          |           | kff125f |
| 80-100 MPH Time                         |           | kff1261 |


Credits
-------
* [Optima Forums][1]


[1]: http://www.optimaforums.com/forum/6-optima-engine-technical-discussion/7337-torque-app-others-discussion-what-you-got-5-print.html
