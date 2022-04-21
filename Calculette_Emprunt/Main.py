#Calculate the rentability of an real estate investment


#Prix d'achat
def Prix_achat():
    Prix_achat = input("Renseigner le prix d'achat FA inclut: ")
    while not Prix_achat.isdigit(): #Verifie que l'entré soit bien juste un nombre
        print("Veuillez rentrer uniquement un nombre")
        Prix_achat = input("Renseigner le prix d'achat FA inclut: ")
    return float(Prix_achat)
    

#Apport
def Apport():
    M_Apport = input("Quel est le montant de votre apport? ")
    while not M_Apport.isdigit(): #Verifie que l'entré soit bien juste un nombre
        print("Veuillez rentrer uniquement un nombre")
        M_Apport = input("Quel est le montant de votre apport? ")
    return float(M_Apport)
    
     
#Taux d'emprunt
def Taux_emprunt():
    print("Si vous ne savez pas quel taux d'intérêt rentrer, référez vous rapidement au site Meilleurs taux: https://www.meilleurtaux.com/credit-immobilier/simulation-de-pret-immobilier/calcul-des-mensualites.html")
    taux = input("Taux d'intérêt: ")
    x = True
    while x == True:
        try:
            taux = float(taux)/100
            x = False
        except:
            print("Seul un nombre avec ou sans virgule est attendu. Symboliser la virgule par un point. Pas de symbole %.")
            taux = input("Taux d'intérêt: ")

    return taux

#Taux d'assurance
def Taux_assurance():
    print("Si vous ne savez pas quel taux d'intérêt rentrer, référez vous rapidement au site Meilleurs taux: https://www.meilleurtaux.com/credit-immobilier/simulation-de-pret-immobilier/calcul-des-mensualites.html")
    taux_A = input("Taux d'assurance: ")
    x = True
    while x == True:
        try:
            taux_A = float(taux_A)/100
            x = False
        except:
            print("Seul un nombre avec ou sans virgule est attendu. Pas de symboles.")
            taux_A = input("Taux d'assurance : ")
    return taux_A


#Durée de l'emprunt en années:
def temps():
    temps = input("Quel est la durée de votre emprunt en années? ")   
    while not temps.isdigit():
        print("Seulement un nombre est attendu.")
        temps = input("Quel est la durée de votre emprunt en années? ")  
    return float(temps)

#Calcul mensualité du credit
def mensualite():
    mensualite = ((A-a)*(T/12))/(1-pow(1+(T/12),(-12*Duree)))
    return mensualite


#Calcul Coût assurance
def M_assurance():
    M_assurance = (A*t)/12
    return M_assurance

#Résumé du credit
def recapitulatif():
    print("*"*54)
    print(f"*****Montant total emprunté : {int(total)}€"+"*"*17)
    print("*"*54)
    print(f"*****Coût du crédit {int(total - A)}€ dont {int(m*Duree*12)}€ d'assurance"+"*"*5)
    print("*"*54)
    print(f"*****Votre Mensusalité est de : {int(M+m)}€"+"*"*19)
    print("*"*54)


#Calcul rentabilité


#Récupération des données nécessaire et exéctution
if __name__ == "__main__":
    
    A = Prix_achat()
    a = input("Avez vous un Apport? (oui/non) ")
    while True:
        if a == "oui":
            a = Apport()
            break
        elif a == "non":
            a = 0
            break
        else:
            print("Veuillez répondre par 'oui' ou 'non'")
            a = input("Avez vous un Apport? (oui/non) ")
    T = Taux_emprunt()
    t = Taux_assurance()
    Duree = temps()
    M = mensualite()
    m = M_assurance()
    total = (M+m)*Duree*12
    recapitulatif()




   







