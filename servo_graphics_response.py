import matplotlib.pyplot as plt
import numpy as np

# Wood humidity, temperature and corresponding servo motor angles
wood_humidity = [73,79,76,74,73,71,68,67,65,64,64,63,63,64,63,62,61,61,60,59,60,60,59,59,59,58,57,57,58,58,57,57,56,56,55,55,55,55,54,54,53,52,52,51]
temperature = [23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,24,24,24,24,24,24,24,25,25,25,25,25,25,26,26,26,26,26,26,27,27]

desired_humidity = 54
threshold_temp=26
servo_motor_angles = np.zeros((len(wood_humidity), len(temperature)))  # Initialize servo motor angle matrix

for i, temp in enumerate(temperature):
    for j, h in enumerate(wood_humidity):
        if temp >= 26 and h <= desired_humidity:
            servo_motor_angles[j, i] = 90  # Angle when temperature is greater than 27 and wood humidity is greater than desired humidity
        if temp < 26:
            servo_motor_angles[j, i] = 0  # Angle when temperature is less than or equal to 27 and wood humidity is less than or equal to desired humidity

# Display heatmap chart
plt.figure(figsize=(10, 6))
plt.imshow(servo_motor_angles, cmap='coolwarm', extent=[min(temperature), max(temperature), min(wood_humidity), max(wood_humidity)], aspect='auto')
plt.colorbar(label='Servo motor angle (degrees)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Wood humidity (%)')
plt.title('Servo motor angle dependency on temperature and wood humidity')
plt.grid(True)

# Add desired humidity label
plt.axhline(y=desired_humidity, color='r', linestyle='--', label='Desired humidity')

# Add temperature label
plt.axvline(x=26, color='g', linestyle='--', label='Minimum temperature for opening model')

plt.legend()  # Add legend
plt.show()


