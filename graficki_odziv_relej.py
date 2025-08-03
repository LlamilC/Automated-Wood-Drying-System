import matplotlib.pyplot as plt

# Wood humidity and corresponding relay state
wood_humidity = range(0, 101, 5)  # Humidity from 0 to 100%, step 5
relay_state = []
desired_humidity = 45  # Assumption: Desired wood humidity

for h in wood_humidity:
    if h <= desired_humidity:
        relay_state.append(0)  
    else:
        relay_state.append(1) 

# Plot relay state dependency on wood humidity
plt.figure(figsize=(10, 6))
plt.plot(wood_humidity, relay_state, marker='o', linestyle='-', color='blue', label='Relay state')
plt.axvline(x=desired_humidity, color='r', linestyle='--', label='Desired humidity')
plt.xlabel('Wood humidity (%)')
plt.ylabel('Relay state')
plt.title('Relay state dependency on wood humidity')
plt.legend()
plt.grid(True)
plt.show()


