import matplotlib.pyplot as plt

# Vlažnost drveta i odgovarajuće stanje releja
vlažnost_drveta = range(0, 101, 5)  # Vlažnost od 0 do 100%, korak 5
stanje_releja = []
zeljena_vlaznost = 45  # Pretpostavka: Željena vlažnost drveta

for v in vlažnost_drveta:
    if v <= zeljena_vlaznost:
        stanje_releja.append(0)  
    else:
        stanje_releja.append(1) 

# Plotovanje zavisnosti stanja releja od vlažnosti drveta
plt.figure(figsize=(10, 6))
plt.plot(vlažnost_drveta, stanje_releja, marker='o', linestyle='-', color='blue', label='Stanje releja')
plt.axvline(x=zeljena_vlaznost, color='r', linestyle='--', label='Željena vlažnost')
plt.xlabel('Vlažnost drveta (%)')
plt.ylabel('Stanje releja')
plt.title('Zavisnost stanja releja od vlažnosti drveta')
plt.legend()
plt.grid(True)
plt.show()


