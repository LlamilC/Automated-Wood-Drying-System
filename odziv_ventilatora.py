import matplotlib.pyplot as plt
import numpy as np

# Vlažnost drveta, temperatura i odgovarajući duty cycle za ventilator
vlažnost_drveta = [73, 79, 76, 74, 73, 71, 68, 67, 65, 64, 64, 63, 63, 64, 63, 62, 61, 61, 60, 59, 60, 60, 59, 59, 59, 58, 57, 57, 58, 58, 57, 57, 56, 56, 55, 55, 55, 55, 54, 54, 53, 52, 52, 51]
temperatura = [23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 27,27]
duty_cycle_ventilatora = np.zeros((len(vlažnost_drveta), len(temperatura)))  # Inicijalizacija matrice duty cycle-a za ventilator
duty = 10
for i, temperature in enumerate(temperatura):
    for j, v in enumerate(vlažnost_drveta):
        if v > 54:
            if temperature <= 28 and temperature > 25:
                if duty >= 100:
                    duty_cycle_ventilatora[j, i] = 100 
                else:
                    duty_cycle_ventilatora[j, i] = duty
                    duty = duty + 2
            elif temperature <= 31 and temperature > 28:
                if duty >= 100:
                    duty_cycle_ventilatora[j, i] = 100 
                else:
                    duty_cycle_ventilatora[j, i] = duty
                    duty = duty + 5
            else:
                duty_cycle_ventilatora[j, i] = duty
        else:
            duty_cycle_ventilatora[j, i] = 100


# Prikaz heatmap grafikona
plt.figure(figsize=(10, 6))
plt.imshow(duty_cycle_ventilatora, cmap='coolwarm', extent=[min(temperatura), max(temperatura), min(vlažnost_drveta), max(vlažnost_drveta)], aspect='auto')
plt.colorbar(label='Duty cycle ventilatora (%)')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Vlažnost drveta (%)')
plt.title('Zavisnost duty cycle-a ventilatora od temperature i vlažnosti drveta')
plt.grid(True)

# Dodavanje oznake za željenu vlažnost
zeljena_vlaznost = 54
plt.axhline(y=zeljena_vlaznost, color='r', linestyle='--', label='Željena vlažnost')

# Dodavanje oznake za minimalnu temperaturu za uključenje ventilatora
granicna_temp = 26
plt.axvline(x=granicna_temp, color='g', linestyle='--', label='Minimalna temperatura za uključenje ventilatora')

plt.legend()  # Dodavanje legende
plt.show()


                                  
 
