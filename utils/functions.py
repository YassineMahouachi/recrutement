from pickle import load, dump
from .candiat import Candiat
import time

errors = {
    "cin" : "Verifiez Cin!",
    "np" : "Verifez Nom&Prenom!",
    "age" : "Verifez Age!",
    "tel" : "Verifez Telephone!",
    "xp" : "Verifez Experience Professionel!"
}

def estNum(ch:str) -> bool:
    i = 0
    valid = len(ch) > 0
    while True and valid:
        if not(ch[i] >= "0" and ch[i] <= "9"):
            valid = False
        else:
            i += 1
        if not(valid) or i >= len(ch)-1:
            break
    return valid

def estAlpha(ch:str) -> bool:
    i = 0
    valid = len(ch) > 0
    while True and valid:
        if not(ch[i].upper() >= "A" and ch[i].upper() <= "Z" or ch[i] == " "):
            valid = False
        else:
            i += 1
        if not(valid) or i >= len(ch)-1:
            break
    return valid

def verifCinTel(ch:str) -> bool:
    return estNum(ch) and len(ch) == 8

def verifNp(ch:str) -> bool:
    ch = ch.split(" ")
    v = True
    i = -1
    while True:
        i += 1
        if not(estAlpha(ch[i])):
            v = False
        if i == len(ch)-1 or v == False:
            break
    return v and len(ch) >= 2

def verifAns(ch:str) -> bool:
    return estNum(ch) and ((len(ch) > 0 and len(ch) <= 2) or int(ch) > 0)

def Tri(tab:list, n:int):
    while True:
        is_swaped = False
        for i in range(n-1):
            if int(tab[i].xp) < int(tab[i+1].xp) or (int(tab[i].xp) == int(tab[i+1].xp) and int(tab[i].age) < int(tab[i+1].age)):
                temp = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = temp
                is_swaped = True
        if is_swaped == False:
            break
    
def writing(F, tab):
    for i in range(len(tab)):
        c = tab[i]
        ch = c.cin + " ** " + c.np + " ** " + c.tel + "\n"
        F.write(ch)

def saveToFile(window, second_win):
    F = open("temp.dat", "ab")
    cin = window.cin.text()
    np = window.np.text()
    age = window.age.text()
    tel = window.tel.text()
    xp = window.tel.text()
    sexe = ""
    diplome = ""
    sgroup = window.sexe.children()
    #print(sgroup)
    dgroup = window.diplome.children()
    #print(dgroup)
    for b in sgroup:
        if b.isChecked():
            sexe = b.objectName()
    for b in dgroup:
        if b.isChecked():
            diplome = b.objectName()
    #print(diplome)
    C = Candiat(cin, np, age, tel, xp, sexe, diplome)
    print(C.__repr__(), "is saved")
    dump(C, F)
    #print("saved")
    F.close()
    second_win.hide()

def generateFiles(second_win):
    F = open("temp.dat", "rb")
    bts = []
    btp = []
    tec = []
    ing = []
    endFile = False
    while not(endFile):
        try:
            C = load(F)
            if C.diplome == "bts":
                bts.append(C)
            elif C.diplome == "btp":
                btp.append(C)
            elif C.diplome == "tec":
                tec.append(C)
            else:
                ing.append(C)
        except:
            endFile = True
    F.close()
    #sorting lists
    Tri(bts, len(bts))
    Tri(btp, len(btp))
    Tri(tec, len(tec))
    Tri(ing, len(ing))
    #exporting data
    F1 = open("exported/btp.txt", "w")
    F2 = open("exported/bts.txt", "w")
    F3 = open("exported/tec.txt", "w")
    F4 = open("exported/ing.txt", "w")
    writing(F1, btp)
    writing(F2, bts)
    writing(F3, tec)
    writing(F4, ing)
    F1.close()
    F2.close()
    F3.close()
    F4.close()
    #delete file's content for the next new data
    F = open("temp.dat", "wb")
    F.close()
    second_win.hide()
    
def reset(window):
    window.cin.clear()
    window.np.clear()
    window.age.clear()
    window.tel.clear()
    window.xp.clear()
    window.sexe.children()[0].setChecked(True)
    window.diplome.children()[0].setChecked(True)

def existe(cin):
    F = open("temp.dat", "rb")
    v = False
    endFile = False
    while not(endFile):
        try:
            C = load(F)
            if cin == C.cin:
                v = True
        except:
            endFile = True
    F.close()
    return v

def main_save(main, existe_win, errors_win, save_win):
    cin = main.cin.text()
    np = main.np.text()
    age = main.age.text()
    tel = main.tel.text()
    xp = main.tel.text()
    total = [verifCinTel(cin), verifNp(np), verifAns(age), verifCinTel(tel), verifAns(xp)]
    #print(total)
    s = 0
    for i in range(len(total)):
        if total[i] == False:
            s += 1
    if s >= 1:
        errors_win.show()
        for i in range(len(total)):
            if total[i] == False:
                match i:
                    case 0:
                        errors_win.cinv.setText(errors["cin"])
                    case 1:
                        errors_win.npv.setText(errors["np"])
                    case 2:
                        errors_win.agev.setText(errors["age"])
                    case 3:
                        errors_win.telv.setText(errors["tel"])
                    case 4:
                        errors_win.xpv.setText(errors["xp"])
        save_win.hide()
        errors_win.ok.clicked.connect(errors_win.hide)
    else:
        test = existe(cin)
        if test:
            existe_win.show()
            existe_win.ok.clicked.connect(existe_win.hide)
            save_win.hide()
        else:
            saveToFile(main, save_win)