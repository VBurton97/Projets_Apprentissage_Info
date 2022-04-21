class Erreur_saisie:


    def bad_income(self, income, text = ""):
        test = True
        while test == True:
            if income != text:
                print(f"Veuillez rentrer une donnée valide")

            else:
                test = False




