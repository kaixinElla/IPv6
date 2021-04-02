# coding:utf-8
import RPi.GPIO as GPIO  
from datetime import datetime
import pymysql
from multiprocessing import Process
import time
'''
set model
'''
GPIO.setmode(GPIO.BOARD)

'''
============================================================================================
monitor Sensor Data channel
use GPIO.0-----> Port 11 as the infrared sensor1 data channel   In side
use GPIO.1-----> Port 12 as the infrared sensor2 data channel   Out side

Data stream state:
    1 --------------> Work Normally 
    0 --------------> Something Shelter from the sensor

So the common state is 3.3V high vol
keep the port volume stable and strict the electric stream 
Use PUD_UP to pull up resistence on the port

--------------------------------------------------------|
Note!                                                   |
Use Port 6 on Raspberry to link the shared  Ground      |
--------------------------------------------------------|        

=============================================================================================
'''


'''
--------------------------------------------
Use GPIO.16------> Port 13 as the led      |
--------------------------------------------
Note 
Use the Port 6 on Raspberry to linke the shared Ground
'''
GPIO.setup(16, GPIO.OUT)
'''
---------------------------------------
Use Port 7 as the tempurate sensor    |
It has been set out of this code file |
In the file /boot/config.txt          |
---------------------------------------
'''
'''
start connect to mysql
'''
conn = pymysql.connect(
            host = 'localhost',
            user = 'pi',
            password = 'raspberry',
            db = 'zhang',
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor
        )
cursor = conn.cursor()

light_state1 = False
GPIO.output(16, 0)

GPIO.setup(15, GPIO.OUT)
GPIO.output(15, 0)
pwm_fan = GPIO.PWM(15, 300)
pwm_fan.start(0)
fan_state = False


def read_temprature():
    try:
        temp_file = open("/sys/bus/w1/devices/28-051760a8a9ff/w1_slave")
        read_lines = temp_file.read()
        temp_file.close()
        data = read_lines.split("\n")[1]
        temp_data = data.split(" ")[9]
        temp = float(temp_data[2:]) / 1000
        return temp
    except (BaseException), ex:
        print('Read t'
              'emp exception',ex)
    finally:
        temp_file.close()


def fan_process(pwm_fan, light_state1):
    try:    
        while True:
            time.sleep(2)
            tpr = read_temprature()
            print(tpr)
            if tpr < 18.0:
                pwm_fan.ChangeDutyCycle(0)
                fan_state = False
            else:
                pwm_fan.ChangeDutyCycle(100)
                fan_state = True 
            insert_sql = """INSERT INTO 
                        tem(temp, state) 
                        values('%f', '%d')""" % (tpr, light_state1)
            cursor.execute(insert_sql)
            conn.commit()
    except (BaseException),ex:
        print(ex)
        print('Interrupt here, clean GPIO..')
        print('close sql service cursor and connection...')
        GPIO.cleanup()
        cursor.close()
        conn.close()
#fan = Process(target = fan_process)
'the state of the light1'



try:
    time.sleep(2)
    p_num = 1
    print('There are ' + str(p_num) + ' students')

    if p_num > 0:
        if light_state1 == False:
            light_state1 = True
            GPIO.output(16, 1)
            print('open the fan_process')
            fan_process(pwm_fan, light_state1)
    else:
        if light_state1 == True:
            light_state1 = False
            GPIO.output(16, 0)




except (BaseException),ex:
    print(ex)
    print('Interrupt here, clean GPIO..')
    GPIO.cleanup()

    
    



