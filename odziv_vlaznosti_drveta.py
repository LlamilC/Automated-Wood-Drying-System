import matplotlib.pyplot as plt
import datetime

# Podaci o temperaturi i vlažnosti drveta tokom vremena
start_time = datetime.datetime.now()

temperatura = [23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,24,24,24,24,24,24,24,25,25,25,25,25,25,26,26,26,26,26]  # Primer temperatura u °C
vlaznost =    [73,79,76,74,73,71,68,67,65,64,64,63,63,64,63,62,61,61,60,59,60,60,59,59,59,58,57,57,58,58,57,57,56,56,55,55,55,55,54,54,53]  # Primer vlažnosti u %
time_intervals = [start_time + datetime.timedelta(seconds=i*5) for i in range(len(temperatura))]

# Kreiranje grafikona
# Kreiranje prvog grafikona za temperaturu
plt.figure(figsize=(10, 5))
plt.plot(time_intervals, temperatura, label='Temperatura (°C)', marker='o')
plt.xlabel('Vreme (s)')
plt.ylabel('Temperatura (°C)')
plt.title('Grafički odziv sistema sušenja drveta - Temperatura')
plt.legend()
plt.grid(True)
plt.show()
plt.pause(1)

# Kreiranje drugog grafikona za vlažnost
plt.figure(figsize=(10, 5))
plt.plot(time_intervals, vlaznost, label='Vlažnost (%)', marker='o')
plt.xlabel('Vreme (s)')
plt.ylabel('Vlažnost (%)')
plt.title('Grafički odziv sistema sušenja drveta - Vlažnost')
plt.legend()
plt.grid(True)
plt.show()
