# fonction qui enregistre les changements du nb de dés à lancer
def changeD6(change):
    global nb_D6    # nécessaire pour pouvoir modifier la variable globalement
    nb_D6 = change['new']
    bouton.description = "Tirer "+str(nb_D6)+" D6"
    
# fonction qui s'exécute lorsque le bouton est cliqué
def click(b):
    global effectifs
    repartition = distrib_tirage(nb_D6)
    for i in range(6):
        effectifs[i] = effectifs[i] + repartition[i]
    ### partie pour tracer le diagramme
    plt.bar(issues, effectifs, 0.75, color="blue")
    ax.set_xlabel('Issues')
    ax.set_ylabel('Effectifs')
    fig.canvas.draw()
    txt_nb_tirages.value = sum(effectifs)  # on met à jour le nombre de tirages

### Création de l'interface
# boîte nb de dés
txt_nb_D6 = widgets.IntText(value=nb_D6, description='Nb de D6 :', disabled=False)
txt_nb_D6.observe(changeD6, names='value')

# bouton pour les lancers
bouton = widgets.Button(description="Tirer "+str(nb_D6)+" D6")
bouton.on_click(click)

# affichage du nb de lancers total
txt_nb_tirages = widgets.IntText(value = sum(effectifs), description='D6 tirés :')

# mise en forme
display(widgets.HBox([txt_nb_D6, bouton, txt_nb_tirages]))
