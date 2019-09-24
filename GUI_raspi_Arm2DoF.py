from Tkinter import *
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

servo1 = GPIO.PWM(23, 100)
servo1.start(5)

servo2 = GPIO.PWM(24, 100)
servo2.start(5)

class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        Label(frame, text='Servo 1').grid(row=0, column=0)
        Label(frame, text='Servo 2').grid(row=1, column=0)
        scaleServo1 = Scale(frame, from_=0, to=180,
              orient=HORIZONTAL, command=self.updateServo1)
        scaleServo1.grid(row=0, column=1)
        scaleServo2 = Scale(frame, from_=0, to=180,
              orient=HORIZONTAL, command=self.updateServo2)
        scaleServo2.grid(row=1, column=1)

    def updateServo1(self, angle):
        duty = float(angle) / 10.0 + 2.5
        servo1.ChangeDutyCycle(duty)

    def updateServo2(self, angle):
        duty = float(angle) / 10.0 + 2.5
        servo2.ChangeDutyCycle(duty)

root = Tk()
root.wm_title('Robot Arm 2 DoF Control')
app = App(root)
root.geometry("200x100+0+0")
root.mainloop()
