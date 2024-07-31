import time
import I2C_LCD_driver
import RPi.GPIO as GPIO
import sys
import Adafruit_DHT
from pad4pi import rpi_gpio
from gpiozero import Servo



temperatura = []
vlaznost = []



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

# Inicijalizacija LCD ekrana
lcd=I2C_LCD_driver.lcd()



# Funkcija za prikaz poruke na LCD ekranu
def prikazi_poruku(poruka,red=1):
    lcd.lcd_clear()
    lcd.lcd_display_string(poruka,red)

# Inicijalizacija promenljive za unos šifre
unesena_sifra = ""
ispravna_sifra = "333"

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


#REleJ
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,GPIO.LOW)



# Beskonačna petlja za nastavak programa
while True:
    
    
   
   
    
   
 
    
    prikazi_poruku("Unesite sifru1:")
    
    # Glavna petlja za unos šifre
    while len(unesena_sifra) != 3:  # Korisnik treba uneti tačno 3 broja
        key = keypad.getKey()
        if  key:
             unesena_sifra += str(key)
             prikazi_poruku("Unesite sif:" +"*" * len(unesena_sifra))
             time.sleep(0.2)

    if unesena_sifra == ispravna_sifra:
          prikazi_poruku("Sifra je tacna. ")
          unesena_sifra = ""

        # Display the available options to the user
          prikazi_poruku("Izaberite opciju:")
          time.sleep(1.0)  # Sleep for 1 second
            
          prikazi_poruku("A: Kvalitetno")
          lcd.lcd_display_string("B:Drvo za ogrev",2)
        
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
                        
                        prikazi_poruku("Kvalitetno (A)")
                        
                        n=4
                        for i in range(n):
                            humidity_prostora,temp_prostora= Adafruit_DHT.read_retry(11, 24)
                            time.sleep(1.4)
                        
                        humidity_str1 = f"Humidity: {humidity_prostora:.2f}%"
                        temperature_str1 = f"Temp: {temp_prostora:.2f}°C"
                        
                        lcd.lcd_display_string("Temp prostora", 2)
                        lcd.lcd_display_string("Vlaznost makete", 1)
                        time.sleep(1.5)
                
                        lcd.lcd_display_string(temperature_str1, 2)
                        lcd.lcd_display_string(humidity_str1, 1)
                        time.sleep(2)
                            
                        prikazi_poruku("Ubacite drvo")
                        time.sleep(13)
                        
                        
                        broj_ocitanja = 15

                        for i in range(broj_ocitanja):
                            humidity_pocetna, temperature_pocetna = Adafruit_DHT.read_retry(11, 24)
                            time.sleep(2.4)
                        
                        if(humidity_pocetna > 90):
                            zeljena_humidity = humidity_pocetna - 37
                        elif(humidity_pocetna > 85 and humidity_pocetna <=90):
                            zeljena_humidity = humidity_pocetna - 33
                        elif(humidity_pocetna > 80 and humidity_pocetna <=85):
                            zeljena_humidity = humidity_pocetna - 29
                        elif(humidity_pocetna > 75 and humidity_pocetna <=80):
                            zeljena_humidity = humidity_pocetna - 25
                        elif(humidity_pocetna <= 75 and humidity_pocetna > 70):
                            zeljena_humidity = humidity_pocetna - 20
                        elif(humidity_pocetna <= 70 and humidity_pocetna > 64):
                            zeljena_humidity = humidity_pocetna - 17
                        else:
                            zeljena_humidity = humidity_pocetna - 15
                            
                            
                             
                        
                        humidity_str2 = f"Humidity: {humidity_pocetna:.2f}%"
                        temperature_str2 = f"Temp: {temperature_pocetna:.2f}°C"
                        
                        lcd.lcd_display_string("Temp drveta", 2)
                        lcd.lcd_display_string("Vlaznost drveta", 1)
                        time.sleep(1.5)
                
                        lcd.lcd_display_string(temperature_str2, 2)
                        lcd.lcd_display_string(humidity_str2, 1)
                        
                        if(humidity_pocetna > humidity_prostora + 5):
                            duty=10
                            duty2=0
                            
                            while True:
                                
                                
                                humidity, temperature = Adafruit_DHT.read_retry(11, 24)
                                flag=True
                                stanjeGrijaca = 0
                                if temperature >= 31:
                                    GPIO.output(4,GPIO.LOW)
                                    stanjeGrijaca = 0
                                if (temperature < 31 ):
                                    GPIO.output(4,GPIO.HIGH)
                                    stanjeGrijaca = 1
                                    #fan_pwm.ChangeDutyCycle(20)
                                    #fan_pwm2.ChangeDutyCycle(15)
                       
                                time.sleep(0.2)
                                vlaznost.append(humidity)
                                temperatura.append(temperature)
                                
                                str_1 = f"H:{int(humidity)}% T:{int(temperature)}°C S:0 "
                                str_2 = f"V:{duty}% G:{stanjeGrijaca} V2:{duty2}%  "
                                lcd.lcd_clear()
                                lcd.lcd_display_string(str_2, 2)
                                lcd.lcd_display_string(str_1, 1)
                                    
                                    
                                if temperature <= 28 and temperature > 25 :
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
                                     
                                elif temperature <= 31 and temperature > 28  :
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
                               
                              
                                    
                               
                                
                                
                                if humidity <= zeljena_humidity and temp_prostora <26:
                                    if temperature >= 27:
                                        break
                                if humidity <= zeljena_humidity and temp_prostora >= 26:
                                    if temperature >= temp_prostora+1 :
                                        break
                            duty = 100
                            duty2 = 100
                            humidity, temperature = Adafruit_DHT.read_retry(11, 24)
                            time.sleep(1)
                            GPIO.output(4,GPIO.LOW)
                            stanjeGrijaca = 0
                            servo1.ChangeDutyCycle(6)
                            time.sleep(0.5)
                            servo1.ChangeDutyCycle(0)
                            time.sleep(0.3)
                            fan_pwm.ChangeDutyCycle(duty)
                            fan_pwm2.ChangeDutyCycle(duty2)
                            
                            str_1 = f"H:{int(humidity)}% T:{int(temperature)}°C S:1 "
                            str_2 = f"V:{duty}% G:{stanjeGrijaca} V2:{duty2}% "
                            lcd.lcd_clear() 
                            lcd.lcd_display_string(str_2, 2)
                            lcd.lcd_display_string(str_1, 1)
                            time.sleep(3)
                            lcd.lcd_clear()
                            lcd.lcd_display_string("Ispustanje ", 1)
                            lcd.lcd_display_string("Toplote", 2)
                            time.sleep(40)
                            humidity, temperature = Adafruit_DHT.read_retry(11, 24)
                            
                            lcd.lcd_clear()
                            duty = 0
                            duty2 = 0
                            fan_pwm.ChangeDutyCycle(duty)
                            fan_pwm2.ChangeDutyCycle(duty2)
                            
                            str_1 = f"H:{int(humidity)}% T:{int(temperature)}°C S:1 "
                            str_2 = f"V:{duty}% G:{stanjeGrijaca} V2:{duty2}% "
                
                            lcd.lcd_display_string(str_2, 2)
                            lcd.lcd_display_string(str_1, 1)
                            time.sleep(3)
                            
                            
                            with open ('podaci.txt' ,'w') as file:
                                for temp,hum in zip (temperatura,vlaznost):
                                    file.write(f"{temp},{hum}\n")
                        
                       
                        else:
                            prikazi_poruku("Drvo je suho",1)
                            time.sleep(2.8)
                            
                    elif choice == 'B':
                        prikazi_poruku("Drvo za ogrev (B)")
                        time.sleep(1.8)
           
      # Here you can add your code to continue the program.
    else:
        prikazi_poruku("Sifra je netacna.")
        unesena_sifra = ""
        time.sleep(0.6)  # Sleep for 0.6 seconds

    #servo1.stop()
    #GPIO_cleanup()
        
