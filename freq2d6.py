ax2d6 = fig.add_subplot(111)
ax2d6.set_xlabel('Issues')
ax2d6.set_ylabel('Fréquences en %')
plt.axis([1.5, 12.5, 0, 20])
plt.bar(issues2d6, frequences2d6, .75, color="red")
rectangles = ax2d6.patches
for rect, pourcent in zip(rectangles, frequences2d6):
    hauteur = rect.get_height()
    ax2d6.text(rect.get_x() + rect.get_width()/2, hauteur, round(pourcent, 1) , ha='center', va='bottom')
fig.canvas.draw()
fig.canvas.draw()