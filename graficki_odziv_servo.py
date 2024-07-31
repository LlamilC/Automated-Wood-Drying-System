import matplotlib.pyplot as plt
import numpy as np

# Vlažnost drveta, temperatura i odgovarajući uglovi servo motora
vlažnost_drveta = [73,79,76,74,73,71,68,67,65,64,64,63,63,64,63,62,61,61,60,59,60,60,59,59,59,58,57,57,58,58,57,57,56,56,55,55,55,55,54,54,53,52,52,51]
temperatura = [23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,24,24,24,24,24,24,24,25,25,25,25,25,25,26,26,26,26,26,26,27,27]

zeljena_vlaznost = 54
granicna_temp=26
uglovi_servo_motora = np.zeros((len(vlažnost_drveta), len(temperatura)))  # Inicijalizacija matrice uglova servo motora

for i, temp in enumerate(temperatura):
    for j, v in enumerate(vlažnost_drveta):
        if temp >= 26 and v <= zeljena_vlaznost:
            uglovi_servo_motora[j, i] = 90  # Ugao kada je temperatura veća od 27 i vlažnost drveta veća od željene vlažnosti
        if temp < 26:
            uglovi_servo_motora[j, i] = 0  # Ugao kada je temperatura manja ili jednaka 27 i vlažnost drveta manja ili jednaka željenoj vlažnosti

# Prikaz heatmap grafikona
plt.figure(figsize=(10, 6))
plt.imshow(uglovi_servo_motora, cmap='coolwarm', extent=[min(temperatura), max(temperatura), min(vlažnost_drveta), max(vlažnost_drveta)], aspect='auto')
plt.colorbar(label='Ugao servo motora (stepeni)')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Vlažnost drveta (%)')
plt.title('Zavisnost ugla servo motora od temperature i vlažnosti drveta')
plt.grid(True)

# Dodavanje oznake za željenu vlažnost
plt.axhline(y=zeljena_vlaznost, color='r', linestyle='--', label='Željena vlažnost')

# Dodavanje oznake za temperaturu
plt.axvline(x=26, color='g', linestyle='--', label='Minimalna temperatura za otvaranje makete')

plt.legend()  # Dodavanje legende
plt.show()


