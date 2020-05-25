import random

class jeuxRoulette():
    nombre = int()
    couleur = str()
    tier = int()
    moitier = int()

dicoCouleur = {
    0:"vert",
    1:"rouge",
    2:"noir",
    3:"rouge",
    4:"noir",
    5:"rouge",
    6:"noir",
    7:"rouge",
    8:"noir",
    9:"rouge",
    10:"noir",
    11:"noir",
    12:"rouge",
    13:"noir",
    14:"rouge",
    15:"noir",
    16:"rouge",
    17:"noir",
    18:"rouge",
    19:"rouge",
    20:"noir",
    21:"rouge",
    22:"noir",
    23:"rouge",
    24:"noir",
    25:"rouge",
    26:"noir",
    27:"rouge",
    28:"noir",
    29:"noir",
    30:"rouge",
    31:"noir",
    32:"rouge",
    33:"noir",
    34:"rouge",
    35:"noir",
    36:"rouge",
    }

def LancerRoulette(roulette:jeuxRoulette):
    tier = 0
    roulette.moitier = 0
    nb = random.randint(0, 36) 
    if nb != 0 :
        if nb >= 1 and nb <= 18 : 
            roulette.moitier = 1
        else: roulette.moitier = 2
        if nb >= 1 and nb <= 12 :
            tier = 1
        elif nb >= 12 and nb <= 24 :
            tier = 2
        else:
            tier = 3
    else:
        pass
    roulette.nombre = nb
    roulette.couleur  = dicoCouleur[nb]
    roulette.tier = tier
    return(roulette)

def gameNumero():
    choix = 0
    dicoMise = dict()
    while choix != "100":
        print("souhaitez vous misez sur des nombres ? o/n")
        rep = input(":")
        if rep == "o" or rep == "O":
         print("Sur quels nombre voulez vous miser ?")
         nombreMiser = input(":")
         nombreMiser = int(nombreMiser)
         if nombreMiser >= 0 and nombreMiser <= 36:
            if nombreMiser in dicoMise:
                print("vous avez deja miser sur ce nombre !")
                continue
            montantMiser = input(
                "Combien souhaitez vous miser sur ce nombre ?")
            dicoMise.update({nombreMiser: int(montantMiser)})
            print(dicoMise)
            print(dicoMise[nombreMiser])
            choixSuite = input(
                "souhaitez vous miser sur un autre numero ? o/n :")
            if choixSuite == "O" or choixSuite == "o":
                continue
            else:
                return dicoMise
         else:
            print("Erreur")
        else:return dicoMise
 
def gameTier():
    
    dicoMise = dict()
    print("Vous souhaitez misez sur quels tier ? ")
    print("1) 1 - 12")
    print("2) 12 - 24")
    print("3) 24 - 36")
    print("4) Ne pas miser sur les tiers")
    choix = int(input(":"))
    if choix >= 1 and choix <= 3: 
        print("quel est le montant de votre mise ?")
        montant = int(input(":"))
        dicoMise.update({choix:montant})
        return dicoMise
    dicoMise.update({0:0})
    return dicoMise

def gameDemi():
    dicoMise = dict()
    print("Vous souhaitez misez sur quelles moitiee ? ")
    print("1) 1 - 18")
    print("2) 19 - 36")
    print("3) Ne pas miser sur les moitiees")
    choix = int(input(":"))
    if choix == 1 : 
        print("quel est le montant de votre mise ?")
        montant = int(input(":"))
        dicoMise.update({choix:montant})
        return dicoMise
    elif choix == 2 : 
        print("quel est le montant de votre mise ?")
        montant = int(input(":"))
        dicoMise.update({choix:montant})
        return dicoMise
    else : 
        dicoMise.update({0:0})
        return dicoMise

def gameCouleur():
    couleur = str()
    dicoMise = dict()
    print("Sur quelle couleur souhaitez vous miser ? rouge/noir ")
    print("1) Rouge")
    print("2) Noir")
    print("3) Vert")
    print("4) Pas de mise de couleur")
    couleurMiser = input(":")
    if couleurMiser == "1" : 
        couleur = "rouge"
    elif couleurMiser == "2" :
        couleur = "noir"
    elif couleurMiser == "2" :
        couleur = "vert"
    else: couleur = "4"
    if couleur != "4" :
        print(f"Combien souhaitez vous miser sur le {couleur}? ")
        montantMiser = input(":")
        dicoMise.update({couleur:int(montantMiser)})
        return dicoMise
    else: 
        dicoMise.update({0:0})
        return dicoMise

def totalMiser(dictionnaire:dict()):
    montantTotal = 0
    if len(dictionnaire) > 0 :
        for i in dictionnaire:
            montantTotal += dictionnaire[i]
        return montantTotal
    else: 
        return 0

def comparaisonDesGains(lancer:jeuxRoulette,nombreJouer:dict,couleur:dict,tier:dict,demi:dict):

    #On affiche les resultats :

    print(f"Le nombre gagnant est le : {lancer.nombre} {lancer.couleur} ")
    print(f"Le tiers gagnant est le : {lancer.tier}")
    print(f"la demi gagnante est le : {lancer.moitier}")
    print("")


    nombreGagnant = lancer.nombre
    gain = False
    GainNombre = 0
    gainTier = 0
    gainCouleur = 0
    gainDemi = 0

    indexGagant = int()

    # On va veriier les nombres
    for i in nombreJouer:
        if i == nombreGagnant:
            gain = True
            indexGagant = i
            break
    if gain : GainNombre = nombreJouer[indexGagant] * 36



    # On va verifier la couleur
    couleurGagnant = lancer.couleur
    if couleurGagnant in couleur :
        gainCouleur = couleur[couleurGagnant] * 2


    # on verifier le tier 
    gainTier = 0 
    tierGagnant = lancer.tier
    if tierGagnant in tier :
      gainTier = int(tier[tierGagnant]) * 2

        
    # on verifie quelle moitié
    moitierGagnante = lancer.moitier
    gainDemi = 0 
    if moitierGagnante in demi :
      gainDemi = int(demi[moitierGagnante]) * 2

    #on additionne le tout 

    gainTotal = gainCouleur + gainDemi + gainTier + GainNombre
    return gainTotal







