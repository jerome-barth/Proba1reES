ax = fig.add_subplot(111)
ax.set_xlabel('Issues')
ax.set_ylabel('Fréquences en %')
plt.axis([0.5, 6.5, 0, 20])
plt.bar(issues, frequences, .75, color="red")
rectangles = ax.patches
for rect, pourcent in zip(rectangles, frequences):
    hauteur = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2, hauteur, round(pourcent, 1) , ha='center', va='bottom')
fig.canvas.draw()
