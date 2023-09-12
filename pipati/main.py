import random

# proyecto para programar piedra papel o tijera.
print("Listo para desafiar a la computadora en el legendario juego piedra papel o tijera?")
a = "piedra"
b = "papel"
c = "tijera"
jugador = input("elije tu jugada! ")
j = 0
if (jugador == a):
  j = 1
elif (jugador == b):
  j = 2
elif (jugador == c):
  j = 3
else:
  print("selecciona una opcion correcta")
list = (1, 2, 3)
comp = random.choice(list)

if (comp == 1):
  compsel = "piedra"
elif (comp == 2):
  compsel = "papel"
elif (comp == 3):
  compsel = "tijera"
else:
  print("not possible")

if(j == comp):
  print("empataste ya que la computadora eligio "+ compsel)
elif((j-comp)==-1) or ((j-comp)==2) :
  print("perdiste ya que la computadora eligio "+ compsel)
else:
  print("ganaste ya que la computadora eligio "+ compsel)