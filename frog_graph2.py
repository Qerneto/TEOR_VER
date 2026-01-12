from matplotlib.patches import Circle, Wedge, FancyBboxPatch, Ellipse
import matplotlib.pyplot as plt
import random

repeat_time = 100
left_eye_count = 0
total_blink = 0


prob_history = []

fig, my_plot = plt.subplots(figsize=(10, 10))

# Тело лягушки
body_frog = FancyBboxPatch((-0.5, 0), 1.2, 1.2,
                           boxstyle="round,pad=0.02,rounding_size=0.3",
                           edgecolor='black', facecolor='lightgreen', linewidth=2)
my_plot.add_patch(body_frog)

belly_frog = FancyBboxPatch((-0.2, 0.1), 0.6, 0.6,
                            boxstyle="round,pad=0.02,rounding_size=0.3",
                            edgecolor='black', facecolor='lightyellow', linewidth=2)
my_plot.add_patch(belly_frog)

leg1 = FancyBboxPatch((-0.52, -0.2), 0.35, 0.35,
                      boxstyle="round,pad=0.0001,rounding_size=0.15",
                      edgecolor='black', facecolor='lightgreen', linewidth=2)
leg1_1 = Ellipse((-0.5, 0.25), width=0.8, height=0.4, angle=120,
                 facecolor='lightgreen', edgecolor='black', linewidth=2)
my_plot.add_patch(leg1_1)
my_plot.add_patch(leg1)

leg2 = FancyBboxPatch((0.33, -0.2), 0.35, 0.35,
                      boxstyle="round,pad=0.0001,rounding_size=0.15",
                      edgecolor='black', facecolor='lightgreen', linewidth=2)
leg2_1 = Ellipse((0.7, 0.25), width=0.8, height=0.4, angle=60,
                 facecolor='lightgreen', edgecolor='black', linewidth=2)
my_plot.add_patch(leg2_1)
my_plot.add_patch(leg2)

# рот
my_plot.plot([0.2, 0.4], [0.8, 0.8], color='black', linewidth=2)

# левый глаз
eye1 = Circle((-0.4, 1.1), 0.25, fill=True, facecolor="white", edgecolor='black', linewidth=2)
my_plot.add_patch(eye1)
half1 = Wedge((-0.4, 1.1), 0.25, theta1=30, theta2=210,
              facecolor='lightgreen', edgecolor='black', linewidth=1.5)
my_plot.add_patch(half1)
core_eye1 = Circle((-0.25, 1.1), 0.05, fill=True, color="black")
my_plot.add_patch(core_eye1)

# правый глаз
eye2 = Circle((0.6, 1.1), 0.25, fill=True, facecolor="white", edgecolor='black', linewidth=2)
my_plot.add_patch(eye2)
half2 = Wedge((0.6, 1.1), 0.25, theta1=-30, theta2=150,
              facecolor='lightgreen', edgecolor='black', linewidth=1.5)
my_plot.add_patch(half2)
core_eye2 = Circle((0.45, 1.1), 0.05, fill=True, color="black")
my_plot.add_patch(core_eye2)

my_plot.set_xlim(-2, 2)
my_plot.set_ylim(-2, 2)
my_plot.axis("off")

txt = my_plot.text(0, -0.5, "", ha="center", va="center", fontsize=12)

plt.ion()
plt.show()

for i in range(repeat_time):
    total_blink += 1
    blink_eye = random.choice([0, 1])
    if blink_eye == 0:
        left_eye_count += 1
        eye1.set_facecolor("lightgreen")
        half1.set_visible(False)
        core_eye1.set_visible(False)
        fig.canvas.draw()
        fig.canvas.flush_events()
        half1.set_visible(True)
        core_eye1.set_visible(True)
        eye1.set_facecolor("white")
    else:
        eye2.set_facecolor("lightgreen")
        half2.set_visible(False)
        core_eye2.set_visible(False)
        fig.canvas.draw()
        fig.canvas.flush_events()
        half2.set_visible(True)
        core_eye2.set_visible(True)
        eye2.set_facecolor("white")

    prob = left_eye_count / total_blink
    prob_history.append(prob)
    txt.set_text(f"total blinks = {total_blink}\nleft eye prob = {prob:.2f}")

    # обновить холст
    fig.canvas.draw()
    fig.canvas.flush_events()

plt.ioff()

#Построение статистики
plt.figure(figsize=(8, 5))
plt.plot(range(1, repeat_time + 1), prob_history, label="Опытная вероятность")
plt.axhline(0.5, color="red", linestyle="--", label="Теоретическая вероятность 0.5")
plt.xlabel("Количество морганий")
plt.ylabel("Вероятность закрытия левого глаза")
plt.title("Сравнение теоретической и опытной вероятности")
plt.legend()
plt.grid(True)
plt.show()
