# wind-tunnel
###### Python script run on BeagleBone Black to handle IO stream

Files loading into desired directory via USB
```
mkdir /PythonScripts

rename src/script.py PythonScripts/script.py
```

Each file script is then set to run on boot with crontab

 ```
 sudo crontab -e
 
 @reboot sudo python path/PythonScripts/script.py
 ```
 
 ## Additional information:
 
 Accessories included: 
 
 - 150 CFM Computer Fan
 - Servo Motor
 - Arducam 16x2 I2C LCD
 - MPXV7002DP Transducer (Differential Pressure Sensor)
 - 300W Power Supply
 - Nichrome Wire (to heat oil causing smoke)
 - Various toggle/rocker switches
 - 3D Printed Inlet and Diffuser
 - Flow straightener
 
