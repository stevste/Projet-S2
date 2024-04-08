import random as rand
import matplotlib.pyplot as plt

data = []

for i in range (5):
    data.append(dict([("2024-4-8", rand.randint(-5, 35)), ("2024-4-9", rand.randint(-5, 35)), ("2024-4-10", rand.randint(-5, 35)), ("2024-4-11", rand.randint(-5, 35)), ("2024-4-12", rand.randint(-5, 35)), ("2024-4-13", rand.randint(-5, 35))]))

date = data[0].keys()

for i in data:
    plt.plot(date, i.values(), label=str())

plt.xlabel("Date")
plt.ylabel("Températures")

plt.show()