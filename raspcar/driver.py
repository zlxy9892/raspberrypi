#!/usr/bin/python
#coding: utf8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

port1 = 11
port2 = 12
port3 = 13
port4 = 15

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(port1, GPIO.OUT)
	GPIO.setup(port2, GPIO.OUT)
	GPIO.setup(port3, GPIO.OUT)
	GPIO.setup(port4, GPIO.OUT)

def left_forward(sleeptime=1.0):
	init()
	GPIO.output(port1, False)
	GPIO.output(port2, False)
	GPIO.output(port3, GPIO.LOW)
	GPIO.output(port4, GPIO.HIGH)
	time.sleep(sleeptime)
	GPIO.cleanup()

def right_forward(sleeptime=1.0):
	init()
	GPIO.output(port1, GPIO.LOW)
	GPIO.output(port2, GPIO.HIGH)
	GPIO.output(port3, False)
	GPIO.output(port4, False)
	time.sleep(sleeptime)
	GPIO.cleanup()

def left_backward(sleeptime=1.0):
	init()
	GPIO.output(port1, False)
	GPIO.output(port2, False)
	GPIO.output(port3, GPIO.HIGH)
	GPIO.output(port4, GPIO.LOW)
	time.sleep(sleeptime)
	GPIO.cleanup()

def right_backward(sleeptime=1.0):
	init()
	GPIO.output(port1, GPIO.HIGH)
	GPIO.output(port2, GPIO.LOW)
	GPIO.output(port3, False)
	GPIO.output(port4, False)
	time.sleep(sleeptime)
	GPIO.cleanup()

def forward(sleeptime=1.0, duration=0.3):
	itertime = int(float(sleeptime) / duration / 2 + 0.5)
	for i in range(itertime):
		left_forward(duration)
		right_forward(duration)

def backward(sleeptime=1.0, duration=0.3):
	itertime = int(float(sleeptime) / duration / 2 + 0.5)
	for i in range(itertime):
		left_backward(duration)
		right_backward(duration)

def w(sleeptime):
	init()	
	GPIO.output(port1, GPIO.LOW)
	GPIO.output(port2, GPIO.HIGH)
	GPIO.output(port3, GPIO.LOW)
	GPIO.output(port4, GPIO.HIGH)
	time.sleep(sleeptime)
	GPIO.cleanup()

####################### main #######################

#w(2)
#forward(2)
#backward(2)
#left_forward(0.5)
#right_forward(0.5)
#left_backward(1)
#right_backward(1)

if __name__ == '__main__':
	while True:
		str_input = raw_input("input your direction: ")
		#print str_input
		if str_input == 'w':
			forward(1)
		elif str_input == 's':
			backward(1)
		elif str_input == 'wa':
			left_forward(0.5)
		elif str_input == 'wd':
			right_forward(0.5)
		elif str_input == 'sa':
			left_backward(0.5)
		elif str_input == 'sd':
			right_backward(0.5)
		elif str_input == 'ww':
			forward(3)
		elif str_input == 'ss':
			backward(3)	
		elif str_input == 'www':
			forward(6)
		elif str_input == 'sss':
			backward(6)
		elif str_input == 'end':
			break
		else:
			continue

