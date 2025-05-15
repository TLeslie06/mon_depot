
import numpy as np

connexions = np.array([20, 18, 25, 30, 22, 19, 17])
semaine_noms = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi","Dimanche"]

print("📊 Connexions détectées chaque jour :")
for i in range(len(connexions)):
    print(f"{semaine_noms[i]} : {connexions[i]} connexions")

print(f"\n🔢Nombre total de connexions de la semaine: {np.sum([connexions])}")
print(f"📊 Moyenne de connexions par jour: {round(np.mean([connexions]),2)}")

if np.mean([connexions]) >20 :
    print("\n⚠ Alerte: activité anormale.")
else:
    print("\n✅Semaine calme.")

print("\nJour avec plus de 20 connexions:")
for i in range(len(connexions)):
    if connexions[i] > 20:
        print(f"➡️ {semaine_noms[i]} : {connexions[i]} connexions")
