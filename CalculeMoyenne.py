i=1
while i<=5 :
    print("Quelles sont les notes de l'étudiant", i)
    
    # Saisir des notes
    Pyton=float(input("Saisir note python"))
    Algo=float(input("Saisir note Algo"))
    Php=float(input("Saisir note Php"))
    Javascript=float(input("Saisir note Javascript"))

    Moyenne=(Pyton+Algo+Php+Javascript)/4
    print("La moyenne de l'étudiant est:", Moyenne)

    # Afficher les mentions de chaque étudiant

    if Moyenne<10 : 
        print("Mention=Recalé")
    elif Moyenne>10 and Moyenne<=12 :
        print("Mention=passable")
    elif Moyenne>12 and Moyenne<=14 :
        print("Mention=Assez-Bien")
    elif Moyenne>14 and Moyenne<=16 :
        print("Mention=Bien")
    elif Moyenne>16:
        print("Mention=Bien")

    i=i+1
    



    

