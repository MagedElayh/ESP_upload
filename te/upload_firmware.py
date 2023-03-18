import os

# Change to the directory where your firmware project is located
os.chdir('/home/sky/Documents/PlatformIO/Projects/te')

# Build and upload the firmware to ESP32
os.system('platformio run --target upload')

