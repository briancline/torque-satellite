OBDII Codes and Torque Real-time HTTP Keys
==========================================

The following **work-in-progress** tables list known OBDII codes and their
equivalent keys when sent to an HTTP endpoint via the query string.


Basic Torque Data
-----------------

| Description                                        |  OBDII  |   HTTP   |
|----------------------------------------------------|--------:|---------:|
| Timestamp                                          |         |     time |
| Device ID                                          |         |       id |
| Session ID                                         |         |  session |


Vehicle Instrumentation
-----------------------

| Description                                        |  OBDII  |   HTTP   |
|----------------------------------------------------|--------:|---------:|
| Absolute Throttle Position B                       |      47 |      k47 |
| Accelerator PedalPosition D                        |      49 |      k49 |
| Accelerator PedalPosition E                        |      4a |      k4a |
| Accelerator PedalPosition F                        |      4b |      k4b |
| Air Fuel Ratio(Commanded)                          |         |  kff124d |
| Air Fuel Ratio(Measured)                           |         |  kff1249 |
| Air Status                                         |      12 |      k12 |
| Ambient air temp                                   |      46 |      k46 |
| Average trip speed(whilst moving only)             |         |  kff1263 |
| Average trip speed(whilst stopped or moving)       |         |  kff1272 |
| Barometer (on Android device)                      |         |  kff1270 |
| Barometric pressure (from vehicle)                 |      33 |      k33 |
| Catalyst Temperature (Bank 1 Sensor 1)             |      3c |      k3c |
| Catalyst Temperature (Bank 1 Sensor 2)             |      3e |      k3e |
| Catalyst Temperature (Bank 2 Sensor 1)             |      3d |      k3d |
| Catalyst Temperature (Bank 2 Sensor 2)             |      3f |      k3f |
| CO₂ in g/km (Average)                              |         |  kff1258 |
| CO₂ in g/km (Instantaneous)                        |         |  kff1257 |
| Commanded Equivalence Ratio(lambda)                |      44 |      k44 |
| Cost per mile/km (Instant)                         |         |  kff126d |
| Cost per mile/km (Trip)                            |         |  kff126e |
| Distance to empty (Estimated)                      |         |  kff126a |
| Distance travelled since codes cleared             |      31 |      k31 |
| Distance travelled with MIL/CEL lit                |      21 |      k21 |
| EGR Commanded                                      |      2c |      k2c |
| EGR Error                                          |      2d |      k2d |
| Engine Coolant Temperature                         |      05 |      k05 |
| Engine kW (At the wheels)                          |         |  kff1273 |
| Engine Load                                        |      04 |      k04 |
| Engine Load(Absolute)                              |      43 |      k43 |
| Engine Oil Temperature                             |      5c |      k5c |
| Engine RPM                                         |      0c |      k0c |
| Ethanol Fuel %                                     |      52 |      k52 |
| Evap System Vapour Pressure                        |      32 |      k32 |
| Exhaust Gas Temperature 1                          |      78 |      k78 |
| Exhaust Gas Temperature 2                          |      79 |      k79 |
| Fuel cost (trip)                                   |         |  kff125c |
| Fuel flow rate/hour                                |         |  kff125d |
| Fuel flow rate/minute                              |         |  kff125a |
| Fuel Level (From Engine ECU)                       |      2f |      k2f |
| Fuel pressure                                      |      0a |      k0a |
| Fuel Rail Pressure                                 |      23 |      k23 |
| Fuel Rail Pressure (relative to manifold vacuum)   |      22 |      k22 |
| Fuel Remaining (Calculated from vehicle profile)   |         |  kff126b |
| Fuel Status                                        |      03 |      k03 |
| Fuel Trim Bank 1 Long Term                         |      07 |      k07 |
| Fuel trim bank 1 sensor 1                          |      14 |      k14 |
| Fuel trim bank 1 sensor 2                          |      15 |      k15 |
| Fuel trim bank 1 sensor 3                          |      16 |      k16 |
| Fuel trim bank 1 sensor 4                          |      17 |      k17 |
| Fuel Trim Bank 1 Short Term                        |      06 |      k06 |
| Fuel Trim Bank 2 Long Term                         |      09 |      k09 |
| Fuel trim bank 2 sensor 1                          |      18 |      k18 |
| Fuel trim bank 2 sensor 2                          |      19 |      k19 |
| Fuel trim bank 2 sensor 3                          |      1a |      k1a |
| Fuel trim bank 2 sensor 4                          |      1b |      k1b |
| Fuel Trim Bank 2 Short Term                        |      08 |      k08 |
| Fuel used (trip)                                   |         |  kff1271 |
| Horsepower (At the wheels)                         |         |  kff1226 |
| Intake Manifold Pressure                           |      0b |      k0b |
| Kilometers Per Litre(Instant)                      |         |  kff1203 |
| Kilometers Per Litre(Long Term Average)            |         |  kff5202 |
| Litres Per 100 Kilometer(Instant)                  |         |  kff1207 |
| Litres Per 100 Kilometer(Long Term Average)        |         |  kff5203 |
| Mass Air Flow Rate                                 |      10 |      k10 |
| Miles Per Gallon(Instant)                          |         |  kff1201 |
| Miles Per Gallon(Long Term Average)                |         |  kff5201 |
| O2 Sensor1 Equivalence Ratio                       |      24 |      k24 |
| O2 Sensor1 Equivalence Ratio(alternate)            |      34 |      k34 |
| O2 Sensor1 wide-range Voltage                      |         |  kff1240 |
| O2 Sensor2 Equivalence Ratio                       |      25 |      k25 |
| O2 Sensor2 wide-range Voltage                      |         |  kff1241 |
| O2 Sensor3 Equivalence Ratio                       |      26 |      k26 |
| O2 Sensor3 wide-range Voltage                      |         |  kff1242 |
| O2 Sensor4 Equivalence Ratio                       |      27 |      k27 |
| O2 Sensor4 wide-range Voltage                      |         |  kff1243 |
| O2 Sensor5 Equivalence Ratio                       |      28 |      k28 |
| O2 Sensor5 wide-range Voltage                      |         |  kff1244 |
| O2 Sensor6 Equivalence Ratio                       |      29 |      k29 |
| O2 Sensor6 wide-range Voltage                      |         |  kff1245 |
| O2 Sensor7 Equivalence Ratio                       |      2a |      k2a |
| O2 Sensor7 wide-range Voltage                      |         |  kff1246 |
| O2 Sensor8 Equivalence Ratio                       |      2b |      k2b |
| O2 Sensor8 wide-range Voltage                      |         |  kff1247 |
| O2 Volts Bank 1 sensor 1                           |         |  kff1214 |
| O2 Volts Bank 1 sensor 2                           |         |  kff1215 |
| O2 Volts Bank 1 sensor 3                           |         |  kff1216 |
| O2 Volts Bank 1 sensor 4                           |         |  kff1217 |
| O2 Volts Bank 2 sensor 1                           |         |  kff1218 |
| O2 Volts Bank 2 sensor 2                           |         |  kff1219 |
| O2 Volts Bank 2 sensor 3                           |         |  kff121a |
| O2 Volts Bank 2 sensor 4                           |         |  kff121b |
| Relative Accelerator Pedal Position                |      5a |      k5a |
| Relative Throttle Position                         |      45 |      k45 |
| Run time since engine start                        |      1f |      k1f |
| Speed (GPS)                                        |         |  kff1001 |
| Speed (OBD)                                        |      0d |      k0d |
| Intake Air Temperature                             |      0f |      k0f |
| Throttle Position(Manifold)                        |      11 |      k11 |
| Timing Advance                                     |      0e |      k0e |
| Torque                                             |         |  kff1225 |
| Transmission Temperature(Method 1)                 |  fe1805 |  kfe1805 |
| Transmission Temperature(Method 2)                 |      b4 |      kb4 |
| Trip average KPL                                   |         |  kff1206 |
| Trip average Litres/100 KM                         |         |  kff1208 |
| Trip average MPG                                   |         |  kff1205 |
| Trip Distance                                      |         |  kff1204 |
| Trip distance (stored in vehicle profile)          |         |  kff120c |
| Trip Time(Since journey start)                     |         |  kff1266 |
| Trip Time(whilst moving)                           |         |  kff1268 |
| Trip time(whilst stationary)                       |         |  kff1267 |
| Turbo Boost & Vacuum Gauge                         |         |  kff1202 |
| Voltage (Control Module)                           |      42 |      k42 |
| Voltage (OBD Adapter)                              |         |  kff1238 |
| Volumetric Efficiency (Calculated)                 |         |  kff1269 |

Device Instrumentation
----------------------

| Description                                        |  OBDII  |   HTTP   |
|----------------------------------------------------|--------:|---------:|
| Acceleration Sensor(Total)                         |         |  kff1223 |
| Acceleration Sensor(X axis)                        |         |  kff1220 |
| Acceleration Sensor(Y axis)                        |         |  kff1221 |
| Acceleration Sensor(Z axis)                        |         |  kff1222 |
| GPS Accuracy                                       |         |  kff1239 |
| GPS Altitude                                       |         |  kff1010 |
| GPS Bearing                                        |         |  kff123b |
| GPS Latitude                                       |         |  kff1006 |
| GPS Longitude                                      |         |  kff1005 |
| GPS Satellites                                     |         |  kff123a |
| GPS vs OBD Speed difference                        |         |  kff1237 |
| Tilt(x)                                            |         |  kff124a |
| Tilt(y)                                            |         |  kff124b |
| Tilt(z)                                            |         |  kff124c |


Saved Measurements
------------------

| Description                                        |  OBDII  |   HTTP   |
|----------------------------------------------------|--------:|---------:|
| 0-100kph Time                                      |         |  kff122e |
| 0-200kph Time                                      |         |  kff124f |
| 0-30mph Time                                       |         |  kff1277 |
| 0-60mph Time                                       |         |  kff122d |
| 1/4 mile time                                      |         |  kff122f |
| 1/8 mile time                                      |         |  kff1230 |
| 100-0kph Time                                      |         |  kff1264 |
| 40-60mph Time                                      |         |  kff1260 |
| 60-0mph Time                                       |         |  kff1265 |
| 60-120mph Time                                     |         |  kff125e |
| 60-130mph Time                                     |         |  kff1276 |
| 60-80mph Time                                      |         |  kff125f |
| 80-100mph Time                                     |         |  kff1261 |
| 80-120kph Time                                     |         |  kff1275 |


Credits
-------
* [Optima Forums][1]
* [Torque Pro][2]


[1]: http://www.optimaforums.com/forum/6-optima-engine-technical-discussion/7337-torque-app-others-discussion-what-you-got-5-print.html
[2]: https://play.google.com/store/apps/details?id=org.prowl.torque
