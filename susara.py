import time
import I2C_LCD_driver
import RPi.GPIO as GPIO
import sys
import Adafruit_DHT
from pad4pi import rpi_gpio
from gpiozero import Servo



temperature = []
humidity = []



KEYPAD = [
    [1, 2, 3, 'A'],
    [4, 5, 6, 'B'],
    [7, 8, 9, 'C'],
    ['*', 0, '#', 'D']
]

factory = rpi_gpio.KeypadFactory()

# these GPIO pins are connected to the keypad
# change these according to your connections!
L1 = 25
L2 = 22
L3 = 27
L4 = 5

C1 = 6
C2 = 13
C3 = 19
C4 = 26

# Initialize the GPIO pins

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

# Make sure to configure the input pins to use the internal pull-down resistors

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

ROW_PINS = [L1, L2, L3, L4]
COL_PINS = [C1, C2, C3, C4]

keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

GPIO.setmode(GPIO.BCM)


def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        print(characters[0])
    if(GPIO.input(C2) == 1):
        print(characters[1])
    if(GPIO.input(C3) == 1):
        print(characters[2])
    if(GPIO.input(C4) == 1):
        print(characters[3])
    GPIO.output(line, GPIO.LOW)

# Initialize LCD screen
lcd=I2C_LCD_driver.lcd()



# Function to display message on LCD screen
def display_message(message,row=1):
    lcd.lcd_clear()
    lcd.lcd_display_string(message,row)

# Initialize variable for password input
entered_password = ""
correct_password = "333"

#servo=AngularServo(18,min_pulse_width=0.0006,max_pulse_width=0.0023)
servo_pin=18
GPIO.setup(servo_pin,GPIO.OUT)
servo1= GPIO.PWM(servo_pin,50)
servo1.start(0)




fan_pin=27

GPIO.setup(fan_pin,GPIO.OUT)
#GPIO.output(fan_pin, GPIO.HIGH)
fan_pwm=GPIO.PWM(fan_pin,25000)
fan_pwm.start(0)

fan_pin2=21

GPIO.setup(fan_pin2,GPIO.OUT)
#GPIO.output(fan_pin, GPIO.HIGH)
fan_pwm2=GPIO.PWM(fan_pin2,25000)
fan_pwm2.start(0)


#RELAY
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,GPIO.LOW)



# Infinite loop to continue the program
while True:
    
    
   
   
    
   
 
    
    display_message("Enter password:")
    
    # Main loop for password input
    while len(entered_password) != 3:  # User needs to enter exactly 3 numbers
        key = keypad.getKey()
        if  key:
             entered_password += str(key)
             display_message("Enter pass:" +"*" * len(entered_password))
             time.sleep(0.2)

    if entered_password == correct_password:
          display_message("Password correct.")
          entered_password = ""

        # Display the available options to the user
          display_message("Choose option:")
          time.sleep(1.0)  # Sleep for 1 second
            
          display_message("A: High quality")
          lcd.lcd_display_string("B:Firewood",2)
        
          time.sleep(1.0)  # Sleep for 1 second
          choice = None
    # Wait for user input (A or B)
          while choice not in ('A', 'B'):
                key = keypad.getKey()
                if key and key in ('A', 'B'):
                    choice = key
                    if choice == 'A':
                        
                        #servo1.ChangeDutyCycle(9)
                        servo1.ChangeDutyCycle(12)
                        time.sleep(0.5)
                        servo1.ChangeDutyCycle(0)
                        time.sleep(0.3)
                        
                        display_message("High quality (A)")
                        
                        n=4
                        for i in range(n):
                            room_humidity,room_temp= Adafruit_DHT.read_retry(11, 24)
                            time.sleep(1.4)
                        
                        humidity_str1 = f"Humidity: {room_humidity:.2f}%"
                        temperature_str1 = f"Temp: {room_temp:.2f}°C"
                        
                        lcd.lcd_display_string("Room temp", 2)
                        lcd.lcd_display_string("Model humidity", 1)
                        time.sleep(1.5)
                
                        lcd.lcd_display_string(temperature_str1, 2)
                        lcd.lcd_display_string(humidity_str1, 1)
                        time.sleep(2)
                            
                        display_message("Insert wood")
                        time.sleep(13)
                        
                        
                        number_of_readings = 15

                        for i in range(number_of_readings):
                            initial_humidity, initial_temperature = Adafruit_DHT.read_retry(11, 24)
                            time.sleep(2.4)
                        
                        if(initial_humidity > 90):
                            desired_humidity = initial_humidity - 37
                        elif(initial_humidity > 85 and initial_humidity <=90):
                            desired_humidity = initial_humidity - 33
                        elif(initial_humidity > 80 and initial_humidity <=85):
                            desired_humidity = initial_humidity - 29
                        elif(initial_humidity > 75 and initial_humidity <=80):
                            desired_humidity = initial_humidity - 25
                        elif(initial_humidity <= 75 and initial_humidity > 70):
                            desired_humidity = initial_humidity - 20
                        elif(initial_humidity <= 70 and initial_humidity > 64):
                            desired_humidity = initial_humidity - 17
                        else:
                            desired_humidity = initial_humidity - 15
                            
                            
                             
                        
                        humidity_str2 = f"Humidity: {initial_humidity:.2f}%"
                        temperature_str2 = f"Temp: {initial_temperature:.2f}°C"
                        
                        lcd.lcd_display_string("Wood temp", 2)
                        lcd.lcd_display_string("Wood humidity", 1)
                        time.sleep(1.5)
                
                        lcd.lcd_display_string(temperature_str2, 2)
                        lcd.lcd_display_string(humidity_str2, 1)
                        
                        if(initial_humidity > room_humidity + 5):
                            duty=10
                            duty2=0
                            
                            while True:
                                
                                
                                current_humidity, current_temperature = Adafruit_DHT.read_retry(11, 24)
                                flag=True
                                heater_state = 0
                                if current_temperature >= 31:
                                    GPIO.output(4,GPIO.LOW)
                                    heater_state = 0
                                if (current_temperature < 31 ):
                                    GPIO.output(4,GPIO.HIGH)
                                    heater_state = 1
                                    #fan_pwm.ChangeDutyCycle(20)
                                    #fan_pwm2.ChangeDutyCycle(15)
                       
                                time.sleep(0.2)
                                humidity.append(current_humidity)
                                temperature.append(current_temperature)
                                
                                str_1 = f"H:{int(current_humidity)}% T:{int(current_temperature)}°C S:0 "
                                str_2 = f"F:{duty}% H:{heater_state} F2:{duty2}%  "
                                lcd.lcd_clear()
                                lcd.lcd_display_string(str_2, 2)
                                lcd.lcd_display_string(str_1, 1)
                                    
                                    
                                if current_temperature <= 28 and current_temperature > 25 :
                                    if(duty >= 100 or duty2 >= 100 ):
                                        fan_pwm.ChangeDutyCycle(100)
                                        fan_pwm2.ChangeDutyCycle(100)
                                        time.sleep(5)
                                        
                                    else :
                                        print(duty)
                                        fan_pwm.ChangeDutyCycle(duty)
                                        fan_pwm2.ChangeDutyCycle(duty2)
                                        time.sleep(5)
                                        duty = duty + 2
                                        duty2=duty2 + 2
                                        print(duty)
                                     
                                elif current_temperature <= 31 and current_temperature > 28  :
                                    if(duty >= 100 or duty2 >=100):
                                        fan_pwm.ChangeDutyCycle(100)
                                        fan_pwm2.ChangeDutyCycle(100)
                                        time.sleep(5)
                                        
                                    else :
                                        print(duty)
                                        fan_pwm.ChangeDutyCycle(duty)
                                        fan_pwm2.ChangeDutyCycle(duty)
                                        time.sleep(5)
                                        duty = duty + 5
                                        duty2=duty2 + 5
                                        print(duty)
                        
                                else:
                                   fan_pwm.ChangeDutyCycle(duty)
                                   #fan_pwm2.ChangeDutyCycle(10)
                                   #GPIO.output(4,GPIO.HIGH)
                                   #flag=True
                               
                              
                                    
                               
                                
                                
                                if current_humidity <= desired_humidity and room_temp <26:
                                    if current_temperature >= 27:
                                        break
                                if current_humidity <= desired_humidity and room_temp >= 26:
                                    if current_temperature >= room_temp+1 :
                                        break
                            duty = 100
                            duty2 = 100
                            final_humidity, final_temperature = Adafruit_DHT.read_retry(11, 24)
                            time.sleep(1)
                            GPIO.output(4,GPIO.LOW)
                            heater_state = 0
                            servo1.ChangeDutyCycle(6)
                            time.sleep(0.5)
                            servo1.ChangeDutyCycle(0)
                            time.sleep(0.3)
                            fan_pwm.ChangeDutyCycle(duty)
                            fan_pwm2.ChangeDutyCycle(duty2)
                            
                            str_1 = f"H:{int(final_humidity)}% T:{int(final_temperature)}°C S:1 "
                            str_2 = f"F:{duty}% H:{heater_state} F2:{duty2}% "
                            lcd.lcd_clear() 
                            lcd.lcd_display_string(str_2, 2)
                            lcd.lcd_display_string(str_1, 1)
                            time.sleep(3)
                            lcd.lcd_clear()
                            lcd.lcd_display_string("Heat release", 1)
                            lcd.lcd_display_string("", 2)
                            time.sleep(40)
                            end_humidity, end_temperature = Adafruit_DHT.read_retry(11, 24)
                            
                            lcd.lcd_clear()
                            duty = 0
                            duty2 = 0
                            fan_pwm.ChangeDutyCycle(duty)
                            fan_pwm2.ChangeDutyCycle(duty2)
                            
                            str_1 = f"H:{int(end_humidity)}% T:{int(end_temperature)}°C S:1 "
                            str_2 = f"F:{duty}% H:{heater_state} F2:{duty2}% "
                
                            lcd.lcd_display_string(str_2, 2)
                            lcd.lcd_display_string(str_1, 1)
                            time.sleep(3)
                            
                            
                            with open ('data.txt' ,'w') as file:
                                for temp,hum in zip (temperature,humidity):
                                    file.write(f"{temp},{hum}\n")
                        
                       
                        else:
                            display_message("Wood is dry",1)
                            time.sleep(2.8)
                            
                    elif choice == 'B':
                        display_message("Firewood (B)")
                        time.sleep(1.8)
           
      # Here you can add your code to continue the program.
    else:
        display_message("Password incorrect.")
        entered_password = ""
        time.sleep(0.6)  # Sleep for 0.6 seconds

    #servo1.stop()
    #GPIO_cleanup()
        
