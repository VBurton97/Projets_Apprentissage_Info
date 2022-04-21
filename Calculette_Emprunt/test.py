a = (12*20)
Taux_Mensuel = 0.00195
x = (pow((1+Taux_Mensuel),-a)-1)
y = (150000*Taux_Mensuel*pow((1+Taux_Mensuel),a))
tot = y/x


print(y)
print(a)
print(x)
print(tot)
print(u"\U0001D366")
