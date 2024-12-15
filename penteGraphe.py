import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Constantes physiques
g = 9.806  #Gravité
ro = 1.292  #Masse volumique air

#Paramètres de la voiture
Masse = 1540  #Masse
Largeur = 1.79  #Largeur
Hauteur = 1.36  #Hauteur
Cx = 0.34  #Coef de traînée
mu = 0.1  #Coef de frottement
AccMoyenne = 5.8  #Accélération moyenne
A = Largeur * Hauteur  #Surface frontale

#Paramètres du circuit
anglePente = np.radians(3.7)  #Angle de la pente (radians)

#Valeurs initiales
V0 = 0  #Vitesse initiale
X0 = 0  #Position initiale
y0 = [V0, X0]  #Conditions initiales [vitesse, position]

#Équations différentielles couplées
def SetDiffEq(y, t, g, ro, Masse, A, Cx, mu, AccMoyenne, anglePente):
    v = y[0]  #Vitesse
    x = y[1]  #Position
    dv_dt = ( g * np.sin(anglePente) + AccMoyenne  - mu * g * np.cos(anglePente) - (0.5 * Cx * ro * A * v**2) / Masse) #L'acceleration (dérivée de la vitesse)
    dx_dt = v  #La vitesse (dérivée de la position)
    return [dv_dt, dx_dt]

#Temps (en secondes)
t = np.linspace(0, 5,)  #Simulation sur 5 secondes

#Résolution des équations différentielles
solution = odeint(SetDiffEq,y0,t,args=(g, ro, Masse, A, Cx, mu, AccMoyenne, anglePente))

#Extraction des résultats
v = solution[:, 0]  #Vitesse (m/s)
x = solution[:, 1]  #Position (m)

#Graphique
plt.figure(figsize=(12, 6))

#Vitesse
plt.plot(t, v, label='Vitesse (m/s)', color='blue')

#Position
plt.plot(t, x, label='Position (m)', color='red')

plt.xlabel('Temps (s)')
plt.ylabel('Valeurs')
plt.title('Évolution de la vitesse et de la position d\'une voiture descendant une pente')
plt.legend()
plt.grid()
plt.show()

