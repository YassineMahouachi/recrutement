#recrutement
Cet projet permet de :    
    - Charger les fenetres.
    - Verifier les champs saisis.
    - Sauvegarder les champs saisis dans un objet nommé Candiat puis le stocker dans le fichier temp.dat.
    - Trier le fichier temp.dat selon l'experience professionel ou l'age.
    - Generer les fichiers (bts.txt, bts.txt, ing.txt, tec.txt) a partir du ficher temp.dat qui
      est trié puis stocker chaque objet Candiat selon sa propieté Candiat.Diplome dans le fichier ou il merite
      sous la forme (Candiat.CIN ** Candiat.Nom&Prenom ** Candiat.Telephone).
      => les fichiers du resultat sont stockés dans le dossier "exported"
    NB: Ne supprimez pas le fichier temp.dat
        Pour installer pyqt5:
        - Ouvrez la console (CMD[Windows] / Terminal[Linux]) dans ce répertoire puis exécutez la commande:
          pip install -r requirements.txt
