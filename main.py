import RPi.GPIO as GPIO
import time, subprocess

buttonpin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

time_flag = False
button_flag = True

start_time = 0
target_time = 3

while True:
    if GPIO.input(buttonpin) == GPIO.HIGH:
        if time_flag == True:
            elapsed_time = time.time() - start_time
            if elapsed_time >= target_time:
                break
        if button_flag == True:
            button_flag = False
            time_flag = True
            start_time = time.time()
    else:
        button_flag = True
    time.sleep(0.2)
print("Shutting down...")
GPIO.cleanup()
subprocess.run(["sudo", "systemctl", "stop", "rpi-camera"])
subprocess.run(["shutdown", "-h", "now"])
