from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui 
from utils import functions
from sys import exit

"""
main.py: 
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
"""

__author__      = "Yassine Mahouachi"
__copyright__   = "Copyright Mars 2022, Lycee Jeune Filles Bizerte"

if __name__ == "__main__":
    #setting up windows ----
    app = QApplication([])
    win = loadUi("gui/main.ui")
    saving_win = loadUi("gui/generate.ui")
    error_win = loadUi("gui/errors.ui")
    existe_win = loadUi("gui/existe.ui")
    win.setWindowIcon(QtGui.QIcon("icons/recrutement.jpg"))
    saving_win.setWindowIcon(QtGui.QIcon("icons/alert.png"))
    error_win.setWindowIcon(QtGui.QIcon("icons/alert.png"))
    existe_win.setWindowIcon(QtGui.QIcon("icons/alert.png"))
    #functions ----
    win.close.clicked.connect(exit) #Button 'Fermer'
    win.reset.clicked.connect(lambda : functions.reset(win)) #Button 'Annuler'
    win.save.clicked.connect(saving_win.show) #Button 'Enregistrer
    saving_win.genereate.clicked.connect(lambda : functions.generateFiles(saving_win)) #Button 'Generer'
    saving_win.save.clicked.connect(lambda : functions.main_save(win, existe_win, error_win, saving_win)) #Button 'Sauvegarder'
    #showing the window ----
    win.show()
    app.exec_()