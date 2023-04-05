class Noeud:
  def __init__(self,cle,valeur, gauche=None, droit=None):
    self.valeur = valeur
    self.cle=cle
    self.gauche= gauche
    self.droit= droit
# Niveau 0
arbre = Noeud('root',['racine']) 

# Niveau 1

arbre.gauche = Noeud('house',['maison'])
arbre.droit = Noeud("help",['aide',])

# niveau 2
arbre.droit.droit = Noeud("like",['aime'])
arbre.gauche.droit = Noeud("please",['stp','svp'])
arbre.droit.gauche = Noeud("us",['nous'])
arbre.droit.droit = Noeud("me",['moi'])

def rechercher(abr,k):
    mot=[]
    if abr ==None:
        pass
    elif abr.cle ==k:
        print(abr.valeur[0])
    elif abr.cle!=k:
        x=rechercher(abr.droit,k)
        y=rechercher(abr.gauche,k)
    
def traduction(x):
    x= x.split(' ')
    for i in range(len(x)):
        rechercher(arbre,x[i])
        
traduction('please help me')