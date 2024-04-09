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