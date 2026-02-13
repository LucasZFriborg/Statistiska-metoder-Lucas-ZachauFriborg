import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

score = 0
rounds = 0
max_rounds = 10
correct = ""

distributions = [
    "Geometric",
    "Binomial",
    "Negative Binomial",
    "Normal",
    "Standard Normal"
]

def new_round():
    global correct

    ax.clear()

    correct = random.choice(distributions)
    show_cdf = random.choice([True, False])

    if correct == "Geometric":
        p = random.uniform(0.2, 0.6)
        data = np.random.geometric(p, 1000)

    elif correct == "Binomial":
        n = random.randint(5, 20)
        p = random.uniform(0.2, 0.8)
        data = np.random.binomial(n, p, 1000)

    elif correct == "Negative Binomial":
        r = random.randint(3, 10)
        p = random.uniform(0.2, 0.7)
        data = np.random.negative_binomial(r, p, 1000)

    elif correct == "Normal":
        mu = random.uniform(-2, 2)
        sigma = random.uniform(0.5, 2)
        data = np.random.normal(mu, sigma, 1000)

    elif correct == "Standard Normal":
        data = np.random.normal(0, 1, 1000)

    if show_cdf:
        sorted_data = np.sort(data)
        y = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
        ax.plot(sorted_data, y)
        ax.set_title("Which distribution? (CDF)")
    else:
        ax.hist(data, bins=30)
        ax.set_title("Which distribution? (Histogram)")

    canvas.draw()


def check(answer):
    global score, rounds

    if rounds >= max_rounds:
        return

    rounds += 1

    if answer == correct:
        score += 1

    label.config(text=f"Score: {score}/{rounds}")

    if rounds == max_rounds:
        ax.clear()
        ax.text(
            0.5,
            0.5,
            f"Final score:\n{score}/{max_rounds}",
            ha="center",
            va="center",
            fontsize=16
        )
        canvas.draw()
    else:
        new_round()


root = tk.Tk()
root.title("Distribution Quiz")

fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

frame = tk.Frame(root)
frame.pack()

for name in distributions:
    tk.Button(
        frame,
        text=name,
        command=lambda n=name: check(n)
    ).pack(side=tk.LEFT)

label = tk.Label(root, text="Score: 0/0")
label.pack()

new_round()
root.mainloop()