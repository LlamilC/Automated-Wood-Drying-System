import matplotlib.pyplot as plt
import datetime

# Temperature and wood humidity data over time
start_time = datetime.datetime.now()

temperature = [23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,24,24,24,24,24,24,24,25,25,25,25,25,25,26,26,26,26,26]  # Example temperatures in °C
humidity =    [73,79,76,74,73,71,68,67,65,64,64,63,63,64,63,62,61,61,60,59,60,60,59,59,59,58,57,57,58,58,57,57,56,56,55,55,55,55,54,54,53]  # Example humidity in %
time_intervals = [start_time + datetime.timedelta(seconds=i*5) for i in range(len(temperature))]

# Create charts
# Create first chart for temperature
plt.figure(figsize=(10, 5))
plt.plot(time_intervals, temperature, label='Temperature (°C)', marker='o')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.title('Wood drying system graphic response - Temperature')
plt.legend()
plt.grid(True)
plt.show()
plt.pause(1)

# Create second chart for humidity
plt.figure(figsize=(10, 5))
plt.plot(time_intervals, humidity, label='Humidity (%)', marker='o')
plt.xlabel('Time (s)')
plt.ylabel('Humidity (%)')
plt.title('Wood drying system graphic response - Humidity')
plt.legend()
plt.grid(True)
plt.show()
