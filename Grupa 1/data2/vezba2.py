import matplotlib.pyplot as plt

ljudi = ['Dovla','Aleksandra','Milan','Djole','Milos','Djape']

plt.title("Odnos plata i godina u Link Group")
plt.plot(ljudi,[35,28,38,35,25,33],"--D",color="red",label="Godine")
plt.plot(ljudi,[400,700,680,730,693,280],"--*",color="green",label="Plate")

plt.legend()
plt.xlabel("Zaposleni")
plt.ylabel("Plate i godine")

plt.show()