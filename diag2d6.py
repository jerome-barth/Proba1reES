def distrib_tirage2d6(nb):
    effs = [0]*11      # initialisation
    for _ in range(nb):            # le compteur n'est pas utilisé dans la boucle, '_' permet de ne gagner en vitesse
        effs[randint(0,5)+randint(0,5)] += 1    # ici, l'opérateur += permet d'incrémenter la bonne case
    return effs

def changeD6(change):
    global nb_D6
    nb_D6 = change['new']
    bouton.description = "Tirer "+str(nb_D6)+" paire(s) D6"
txt_nb_D6 = widgets.IntText(value=nb_D6, description='Nb 2 D6 :', disabled=False)
txt_nb_D6.observe(changeD6, names='value')

def click(b):
    global resultats2d6
    resultats2d6 = [x + y for x, y in zip(resultats2d6, distrib_tirage2d6(nb_D6))]
    ax.clear()
    plt.bar(issues2d6, resultats2d6, .75, color="blue")
    fig.canvas.draw()
    txt_nb_tirages.value = str(sum(resultats2d6))
bouton = widgets.Button(description="Tirer "+str(nb_D6)+" paire(s) D6")
bouton.on_click(click)

txt_nb_tirages = widgets.IntText(value = sum(resultats2d6), description='Paires D6 :')

display(widgets.HBox([txt_nb_D6, bouton, txt_nb_tirages]))

