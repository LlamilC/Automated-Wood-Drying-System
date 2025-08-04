import matplotlib.pyplot as plt
import numpy as np

# Wood humidity, temperature and corresponding duty cycle for fan
wood_humidity = [73, 79, 76, 74, 73, 71, 68, 67, 65, 64, 64, 63, 63, 64, 63, 62, 61, 61, 60, 59, 60, 60, 59, 59, 59, 58, 57, 57, 58, 58, 57, 57, 56, 56, 55, 55, 55, 55, 54, 54, 53, 52, 52, 51]
temperature = [23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 27,27]
fan_duty_cycle = np.zeros((len(wood_humidity), len(temperature)))  # Initialize fan duty cycle matrix
duty = 10
for i, temp in enumerate(temperature):
    for j, h in enumerate(wood_humidity):
        if h > 54:
            if temp <= 28 and temp > 25:
                if duty >= 100:
                    fan_duty_cycle[j, i] = 100 
                else:
                    fan_duty_cycle[j, i] = duty
                    duty = duty + 2
            elif temp <= 31 and temp > 28:
                if duty >= 100:
                    fan_duty_cycle[j, i] = 100 
                else:
                    fan_duty_cycle[j, i] = duty
                    duty = duty + 5
            else:
                fan_duty_cycle[j, i] = duty
        else:
            fan_duty_cycle[j, i] = 100


# Display heatmap chart
plt.figure(figsize=(10, 6))
plt.imshow(fan_duty_cycle, cmap='coolwarm', extent=[min(temperature), max(temperature), min(wood_humidity), max(wood_humidity)], aspect='auto')
plt.colorbar(label='Fan duty cycle (%)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Wood humidity (%)')
plt.title('Fan duty cycle dependency on temperature and wood humidity')
plt.grid(True)

# Add desired humidity label
desired_humidity = 54
plt.axhline(y=desired_humidity, color='r', linestyle='--', label='Desired humidity')

# Add minimum temperature label for fan activation
threshold_temp = 26
plt.axvline(x=threshold_temp, color='g', linestyle='--', label='Minimum temperature for fan activation')

plt.legend()  # Add legend
plt.show()


                                  
 
