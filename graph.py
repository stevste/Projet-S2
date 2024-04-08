import random as rand
import matplotlib.pyplot as plt

def createGraph(data):
    fig = plt.figure(figsize=(6, 4), dpi=100)
    axes = fig.add_subplot()
    axes.set_title('Évolution des températures')
    axes.set_xlabel("Date")
    axes.set_ylabel("Températures")

    index = 0
    for i in data:
        axes.plot(i.keys(), i.values(), '.-', label='zone '+str(index))
        index += 1

    axes.legend()

    return fig

data = []

for i in range (5):
    data.append(dict([("2024-4-8", rand.randint(-5, 35)), ("2024-4-9", rand.randint(-5, 35)), ("2024-4-10", rand.randint(-5, 35)), ("2024-4-11", rand.randint(-5, 35)), ("2024-4-12", rand.randint(-5, 35)), ("2024-4-13", rand.randint(-5, 35))]))

fig = createGraph(data)
fig.show()