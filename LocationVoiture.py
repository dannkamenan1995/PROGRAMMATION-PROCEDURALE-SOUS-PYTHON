TarifEssance=15000
TarifDiesel=16000
KmEssance=500
KmDiesel=600
i=1 
r=1
NombreJour=1
NombreVOITURE=1
NombreKm=1
i=int(input("Quelle voiture voulez vous louer :"))
while i!=1 and i!=2 :
    i=int(input("Quelle voiture voulez vous louer :"))
    

if i==1 :
    NombreVOITURE=int(input("Combien de voiture voulez vous louer :"))
    NombreJour=int(input("Combien de jours de location :"))
    NombreKm=int(input("Combien de Km parcouru :"))
    PrixFinal1=(NombreJour*(TarifEssance*NombreVOITURE))+(NombreKm*(NombreVOITURE*KmEssance))
    print("Le tarif total est :",PrixFinal1,"FCFA")
        

elif i==2 :
    NombreVOITURE=int(input("Combien de voiture voulez vous louer :"))
    NombreJour=int(input("Combien de jours de location :"))
    NombreKm=int(input("Combien de Km parcouru :"))
    PrixFinal2= (NombreJour*(TarifDiesel*NombreVOITURE))+(NombreKm*(NombreVOITURE*KmDiesel))
    print("Le tarif total est :",PrixFinal2,"FCFA")
        