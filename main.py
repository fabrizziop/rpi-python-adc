import RPi.GPIO as GPIO
import time
import math

resistor = 1000
capacitor = 106 * (10**-6)
#~ capacitor = 470 * (10**-6)
rc_constant = resistor * capacitor
max_voltage = 12
GPIO.setwarnings(False)
pin_p_mosfet=31
pin_n_mosfet=29
pin_detect=33
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_p_mosfet, GPIO.OUT)
GPIO.setup(pin_n_mosfet, GPIO.OUT)
GPIO.setup(pin_detect, GPIO.IN, pull_up_down=GPIO.PUD_UP)
class single_measure(object):
	def __init__(self):
		self.init_time = time.time()
		self.end_time = False
	def store_time(self,_):
		#print("STORED:",time.time())
		self.end_time = time.time()
	def is_valid(self):
		if self.end_time == False:
			return False
		else:
			return True
	def return_time(self):
		return self.end_time - self.init_time
#~ GPIO.output(pin_p_mosfet, GPIO.HIGH)
#~ GPIO.output(pin_n_mosfet, GPIO.LOW)
#~ time.sleep(0.5)
#~ GPIO.output(pin_p_mosfet, GPIO.LOW)
#~ GPIO.output(pin_n_mosfet, GPIO.LOW)
#~ time.sleep(4)
def discharge_capacitor(p1, p2):
	GPIO.output(p1, GPIO.HIGH)
	GPIO.output(p2, GPIO.HIGH)
def charge_capacitor(p1, p2):
	GPIO.output(p1, GPIO.LOW)
	GPIO.output(p2, GPIO.LOW)
	
#measuring
while True:
	discharge_capacitor(pin_p_mosfet, pin_n_mosfet)
	time.sleep(0.5)
	nm1 = single_measure()
	GPIO.add_event_detect(pin_detect,GPIO.RISING, callback=nm1.store_time)
	charge_capacitor(pin_p_mosfet,pin_n_mosfet)
	time.sleep(1)
	if nm1.is_valid() == True:
		print("Voltage measured is:",max_voltage*(1-(math.e**(-1*nm1.return_time()/rc_constant))))
	else:
		if GPIO.input(pin_detect) == True:
			print("Voltage is under the detection threshold")
		else:
			print("Voltage is above the detection threshold")
	GPIO.remove_event_detect(pin_detect)
