import random
import string
from tkinter import *
def decryptage_de_la_phrase():
    global mot_de_passe
conversion_table_base_75_1 = { 
    0: 'W',1: '0',2: 'q',3: '3',4: '8',5: 'h',
    6: 'n',7: '1',8: 'j',9: 'H',10: '7',11: 'ç',
    12: 'x',13: 'P',14: 'C',15: 'F',16: 'w',17: 'û',
    18: 'i',19: 'J',20: 'î',21: 'O',22: 'ï',23: 'R',
    24: '2',25: 'X',26: 'ô',27: 'u',28: 'ü',29: 'v',
    30: 'V',31: 'N',32: 'e',33: 'd',34: 's',35: 'o',
    36: 'p',37: 'M',38: 'g',39: 'è',40: 'ë',41: 'G',
    42: 'f',43: 'ä',44: '%',45: 'b',46: '6',47: 'y',
    48: 'B',49: 'c',50: 't',51: 'E',52: 'a',53: '5',
    54: '@',55: '9',56: 'T',57: 'z',58: 'r',59: 'à',
    60: 'm',61: 'A',62: 'K',63: 'I',64: 'é',65: 'U',
    66: 'Z',67: '4',68: 'Y',69: 'Q',70: 'S',71: 'l',
    72: 'ù',73: 'ö',74: 'D', 75: 'µ', 76: 'k', 77: '#',
    78: '§', 79:'L'
    }
CRYPTEUR_base_75 = {
    0:'ü',1:'l',2:'7',3:'k',4:'z',5:'O',6:'ï',
    7:'R',8:'L',9:'A',10:'w',11:'W',12:'6',
    13:'I',14:'d',15:'s',16:'Y',17:'H',18:'0',
    19:'f',20:'j',21:'U',22:'r',23:'o',24:'p',
    25:'h',26:'u',27:'n',28:'a',29:'F',30:'i',
    31:'à',32:'ë',33:'T',34:'X',35:'x',36:'M',
    37:'ç',38:'E',39:'D',40:'B',41:'q',42:'é',
    43:'9',44:'3',45:'b',46:'2',47:'G',48:'N',
    49:'C',50:'ù',51:'S',52:'K',53:'c',54:'e',
    55:'4',56:'ä',57:'ô',58:'J',59:'è',60:'8',
    61:'m',62:'Z',63:'û',64:'y',65:'t',66:'5',
    67:'ö',68:'v',69:'g',70:'P',71:'Q',72:'1',
    73:'î',74:'V'
}
CRYPTEUR_base_75_inverse ={
    'ü': 0, 'l': 1, '7': 2, 'k': 3, 'z': 4,
    'O': 5, 'ï': 6, 'R': 7, 'L': 8, 'A': 9, 
    'w': 10, 'W': 11, '6': 12, 'I': 13, 
    'd': 14, 's': 15, 'Y': 16, 'H': 17, 
    '0': 18, 'f': 19, 'j': 20, 'U': 21, 
    'r': 22, 'o': 23, 'p': 24, 'h': 25, 
    'u': 26, 'n': 27, 'a': 28, 'F': 29, 
    'i': 30, 'à': 31, 'ë': 32, 'T': 33, 
    'X': 34, 'x': 35, 'M': 36, 'ç': 37, 
    'E': 38, 'D': 39, 'B': 40, 'q': 41, 
    'é': 42, '9': 43, '3': 44, 'b': 45, 
    '2': 46, 'G': 47, 'N': 48, 'C': 49, 
    'ù': 50, 'S': 51, 'K': 52, 'c': 53, 
    'e': 54, '4': 55, 'ä': 56, 'ô': 57, 
    'J': 58, 'è': 59, '8': 60, 'm': 61, 
    'Z': 62, 'û': 63, 'y': 64, 't': 65, 
    '5': 66, 'ö': 67, 'v': 68, 'g': 69, 
    'P': 70, 'Q': 71, '1': 72, 'î': 73, 'V': 74}
conversion_table_base_75_1_inverse={
    'W': 0, '0': 1, 'q': 2, '3': 3, '8': 4, 
    'h': 5, 'n': 6, '1': 7, 'j': 8, 'H': 9, 
    '7': 10, 'ç': 11, 'x': 12, 'P': 13, 'C': 14, 
    'F': 15, 'w': 16, 'û': 17, 'i': 18, 'J': 19,
    'î': 20, 'O': 21, 'ï': 22, 'R': 23, '2': 24, 
    'X': 25, 'ô': 26, 'u': 27, 'ü': 28, 'v': 29, 
    'V': 30, 'N': 31, 'e': 32, 'd': 33, 's': 34, 
    'o': 35, 'p': 36, 'M': 37, 'g': 38, 'è': 39, 
    'ë': 40, 'G': 41, 'f': 42, 'ä': 43, '%': 44, 
    'b': 45, '6': 46, 'y': 47, 'B': 48, 'c': 49, 
    't': 50, 'E': 51, 'a': 52, '5': 53, '@': 54, 
    '9': 55, 'T': 56, 'z': 57, 'r': 58, 'à': 59, 
    'm': 60, 'A': 61, 'K': 62, 'I': 63, 'é': 64, 
    'U': 65, 'Z': 66, '4': 67, 'Y': 68, 'Q': 69, 
    'S': 70, 'l': 71, 'ù': 72, 'ö': 73, 'D': 74, 
    'µ': 75, 'k': 76, '#': 77, '§': 78, 'L': 79}
def decryptage_de_la_clef(clef_de_decryptage):
    liste_phrase=[]
    liste_pour_la_clef_lettres = []
    liste_pour_la_clef_chiffres = []
    puissance = 256
    nombre_clef_decrypter=0
    for i in clef_de_decryptage:
        liste_pour_la_clef_lettres.append(i)
    for h in liste_pour_la_clef_lettres:
        liste_pour_la_clef_chiffres.append(conversion_table_base_75_1_inverse[h])
    for v in liste_pour_la_clef_chiffres:
        nombre_clef_decrypter=nombre_clef_decrypter + v*(80**puissance)
        puissance=puissance - 1
    a=str(nombre_clef_decrypter)
    for lettres in a:
            liste_phrase.append(lettres)
    resultat = []
    
    while len(liste_phrase) >= 4:
        quatre_termes = liste_phrase[:4]
        variable = ''.join(quatre_termes)
        resultat.append(variable)
        del liste_phrase[:4]
    decrypt_dictionnaire = {}
    accents = ["é","è","ç","ù","£","¤","µ","â","ê","û","î","ô","ë","ü","ï","ö","Â","Ê","Û","Î","Ô","§","Ä","Ë","Ü","Ï","Ö"," ","*"]
    keys = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + list(string.punctuation) + accents
    for i in range(len(resultat)):
        decrypt_dictionnaire[resultat[i]] = keys[i]
    return decrypt_dictionnaire

def decryptage_de_la_phrase(clef, mot_crypter):
    phrase_decrypter =[]
    lettre_a_decrypter = []
    de=0
    dictionnaire_de_base = decryptage_de_la_clef(clef)  # Unused variable

    while len(mot_crypter) >= 3:
        quatre_termes = mot_crypter[:3]
        variable = ''.join(quatre_termes)
        lettre_a_decrypter.append(variable)
        mot_crypter = mot_crypter[3:]

    lettre_phrase = []
    for i in lettre_a_decrypter:
        puissance = 2
        nombre_phrase_decrypter = 0
        liste_pour_la_phrase_chiffres = []
        for v in i:
            liste_pour_la_phrase_chiffres.append(CRYPTEUR_base_75_inverse[v])
        for h in liste_pour_la_phrase_chiffres:
            nombre_phrase_decrypter += h * (75 ** puissance)
            puissance -= 1
        lettre_phrase.append(str(nombre_phrase_decrypter))
    for u in lettre_phrase:
        phrase_decrypter.append(dictionnaire_de_base[u])
    mot_decrypter = phrase_decrypter[0]
    for element in phrase_decrypter[1:]:
        mot_decrypter += element
    return mot_decrypter

def clef(dictionnaire):
    dictionnaire_de_nombre = dictionnaire
    liste_des_valeur= list(dictionnaire_de_nombre.values())
    a=str(liste_des_valeur[0])
    for i in range(1, len(liste_des_valeur)):
        a=a+str(liste_des_valeur[i])
    nombre_entier=int(a)
    return clef_de_decryptage(nombre_entier)
    
def dictionnaire():
    accents=["é","è","ç","ù","£","¤","µ","â","ê","û","î","ô","ë","ü","ï","ö","Â","Ê","Û","Î","Ô","§","Ä","Ë","Ü","Ï","Ö"," "]
    keys = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + list(string.punctuation) + accents
    key_dictionnaire = {}
    decrypt_dictionnaire = {}
    for key in keys:
        while True:
            num = random.randint(5625, 9999)
            if num not in key_dictionnaire.values():
                key_dictionnaire[key] = num
                decrypt_dictionnaire[num] = key
                break
    return key_dictionnaire

def phrase(liste_phrase, dictionnaire):
    lettre_crypter = []
    liste_base_75 = []
    dictionnaire_de_nombre_2 = dictionnaire
    for Base_cryptage in liste_phrase:
        lettre_crypter.append(dictionnaire_de_nombre_2.get(Base_cryptage))
    for base75 in lettre_crypter:
        liste_base_75.append(decimalToBase75(base75))
    mot_crypter=liste_base_75[0]
    for lettres_coller in range(1,len(liste_base_75)):
        mot_crypter=mot_crypter+liste_base_75[lettres_coller]
    return mot_crypter
    
def clef_de_decryptage(decimal):
    Base75_1 = ''
    while(decimal > 0):
        remainder = decimal % 80
        Base75_1 = conversion_table_base_75_1[remainder] + Base75_1
        decimal = decimal // 80
    return Base75_1

def decimalToBase75(decimal):
    Base75_1 = ''
    while(decimal > 0):
        remainder = decimal % 75
        Base75_1 = CRYPTEUR_base_75[remainder] + Base75_1
        decimal = decimal // 75
    return Base75_1

def fenetre_crypteur():
    Fenêtre_crypteur = Tk()
    Fenêtre_crypteur.title("Crypteur")
    frame_crypteur_1=Frame(Fenêtre_crypteur, bg='#cfcfcf')
    frame_crypteur_2=Frame(Fenêtre_crypteur, bg='#cfcfcf')

    Fenêtre_crypteur.geometry("1080x210")
    Fenêtre_crypteur.minsize(1080, 210)
    Fenêtre_crypteur.config(background="#cfcfcf")
    label_title = Label(Fenêtre_crypteur, text="Cryptez votre message", font=('aptos', 20), bg='#cfcfcf')
    label_title.pack()

    entre_votre_phrase = Label(frame_crypteur_1, text="Entez votre phrase: ", font=('aptos', 8), bg='#cfcfcf')
    entre_votre_phrase.grid(row=0,column=0)
    Entré_texte =Entry ( frame_crypteur_1 , width = 150 )
    Entré_texte.grid(row=0, column=1)
    frame_crypteur_1.pack(expand='True')
    
    def ecrir_crypte():
        liste_phrase = []
        Phrase=Entré_texte.get()
        for lettres in Phrase:
            liste_phrase.append(lettres)
        dictionnaire_pour_traduction=dictionnaire()
        clef_ecrite.delete(0, END)
        clef_ecrite.insert(0, clef(dictionnaire_pour_traduction))
        phrase_crypter_ecrite.delete(0, END)
        phrase_crypter_ecrite.insert(0, phrase(liste_phrase, dictionnaire_pour_traduction))
        
         

    texte_clef= Label(frame_crypteur_2, text="Votre clef de cryptage", font=('aptos', 8), bg='#cfcfcf')
    texte_clef.grid(row=0,column=0)
    clef_ecrite =Entry ( frame_crypteur_2 , width = 150 )
    clef_ecrite.grid(row=0, column=1)
    texte_phrase_crypter= Label(frame_crypteur_2, text="Votre phrase crypté", font=('aptos', 8), bg='#cfcfcf')
    texte_phrase_crypter.grid(row=1,column=0)
    phrase_crypter_ecrite =Entry ( frame_crypteur_2 ,width=150)
    phrase_crypter_ecrite.grid(row=1, column=1)
    bouton_cryptage= Button(frame_crypteur_2, text="crypter", command=ecrir_crypte)
    bouton_cryptage.grid(row=2, column=0)
    frame_crypteur_2.pack(expand='True')
    Fenêtre_crypteur.mainloop()

def fenetre_décrypteur():
    Fenêtre_décrypteur = Tk()
    Fenêtre_décrypteur.title("Décrypteur")
    frame_décrypteur_1=Frame(Fenêtre_décrypteur, bg='#cfcfcf')
    frame_décrypteur_2=Frame(Fenêtre_décrypteur, bg='#cfcfcf')

    Fenêtre_décrypteur.geometry("1080x210")
    Fenêtre_décrypteur.minsize(1080, 210)
    Fenêtre_décrypteur.config(background="#cfcfcf")
    label_title = Label(Fenêtre_décrypteur, text="Décryptez votre message", font=('aptos', 20), bg='#cfcfcf')
    label_title.pack()

    entre_votre_phrase = Label(frame_décrypteur_1, text="Entez votre phrase: ", font=('aptos', 8), bg='#cfcfcf')
    entre_votre_phrase.grid(row=0,column=0)
    Entré_phrase =Entry ( frame_décrypteur_1 , width = 150 )
    Entré_phrase.grid(row=0, column=1)
    entre_votre_clef = Label(frame_décrypteur_1, text="Entez votre clef: ", font=('aptos', 8), bg='#cfcfcf')
    entre_votre_clef.grid(row=1,column=0)
    Entré_clef =Entry ( frame_décrypteur_1 , width = 150 )
    Entré_clef.grid(row=1, column=1)
    frame_décrypteur_1.pack(expand='True')
    
    def ecrir_phrase():
        liste_phrase = []
        Phrase_à_decrypter=Entré_phrase.get()
        clef_à_decrypter=Entré_clef.get()
        for lettres in Phrase_à_decrypter:
            liste_phrase.append(lettres)
        phrase_décrypter_ecrite.delete(0, END)
        phrase_décrypter_ecrite.insert(0, decryptage_de_la_phrase(clef_à_decrypter,liste_phrase))
        
         

    
    texte_phrase_décrypter= Label(frame_décrypteur_2, text="Votre phrase décrypté", font=('aptos', 8), bg='#cfcfcf')
    texte_phrase_décrypter.grid(row=1,column=0)
    phrase_décrypter_ecrite =Entry ( frame_décrypteur_2 ,width=150)
    phrase_décrypter_ecrite.grid(row=1, column=1)
    bouton_cryptage= Button(frame_décrypteur_2, text="décrypter", command=ecrir_phrase)
    bouton_cryptage.grid(row=2, column=0)
    frame_décrypteur_2.pack(expand='True')
    Fenêtre_décrypteur.mainloop()

def Fenetre_base():
    Fenêtre = Tk()
    Fenêtre.title("Accueil")
    frame=Frame(Fenêtre, bg='#cfcfcf')

    Fenêtre.geometry("480x360")
    Fenêtre.minsize(480, 360)
    Fenêtre.config(background="#cfcfcf")
    label_title = Label(Fenêtre, text="Bienvenue dans votre crypteur\n ou decrypteur, que voulez-vous faire", font=('aptos', 20), bg='#cfcfcf')
    label_title.pack()
    crypteur_button= Button(frame, text='Crypteur', command=fenetre_crypteur)
    crypteur_button.grid(row=0, column=0)

    décrypteur_button= Button(frame, text='Décrypteur', command=fenetre_décrypteur)
    décrypteur_button.grid(row=0, column=1)

    boite= Frame(Fenêtre, bg='#cfcfcf')
    frame.pack(expand='True')

    Fenêtre.mainloop()
Fenetre_base()