#Le code ci-dessous implemente 4 fonctions :
    #file_to_list : transforme un fichier en liste
    #fpres_mot : pour chaque mot qui se trouve dans les fichiers,
                 #calcule un facteur de pondération selon l’équation suivante :
                                                                                #fpres_mot = log ( total des documents / nombre de documents contenant le mot)
    #text_to_freq : pour chaque mot qui se trouve dans les fichier, calculer sa
                    #fréquence normalisée et retourner un dictionnaire contenant les mots et leurs
                    #fréquences normalisées selon l<éqution suivante:
                                                                        #freq_mot = nombre de fois le mot apparait dans le document / total des mots dans le même document
    #text_to_weight : Pour chaque mot du fichier (chacune des listes ci-dessus),
                      #calculer son poids comme suit :
                                                        #weight_mot = freq_mot * fpres_mot


#importer les librairies:
#Une expression régulière (ou RE) spécifie un ensemble de chaînes qui lui correspond; les fonctions de ce module vous permettent de vérifier si une chaîne particulière correspond à une expression régulière donnée (ou si une expression régulière donnée correspond à une chaîne particulière, ce qui revient à la même chose).
#math Ce module est toujours disponible. Il fournit l’accès aux fonctions mathématiques définies par le standard C.
import re
import math

#emplacement des fichiers .txt (fournis par le prof)
path1 = '/Users/Fosso Print/Documents/cours/INFO3005/devoir 3/python_1.txt'
path2 = '/Users/Fosso Print/Documents/cours/INFO3005/devoir 3/python_2.txt'
path3 = '/Users/Fosso Print/Documents/cours/INFO3005/devoir 3/python_3.txt'

#ouverture des fichiers .txt
file1 = open(path1,'r')
file2 = open(path2,'r')
file3 = open(path3,'r')

#recuperation du contenu des fichiers par lines sous forme de string .txt
myDic1 = file1.readline()
myDic2 = file2.readline()
myDic3 = file3.readline()

#declaration des fonction

#file_to_list: parametres : fichier
              #retourne: Liste des mots de la   sans ponctuations
def file_to_list(path):
    with open(path) as file: #ouvre le fichier
        liste = []
        for line in file:   #lit le fichier lignes après lignes
            for words in re.findall(r"\w+", line):
                liste.append(words)
    return liste

#Retirer tous les mots sans ponctuation dans les fichiers python_1, python_2, python_3
All_words1 = file_to_list(path1)
All_words2 = file_to_list(path2)
All_words3 = file_to_list(path3)


#fpres_mot: parametres : rien
           #retourne : dictionnaire(Liste) contenant les mots et leurs facteurs
           #de présence trié en ordre croissant
def fpres_mot():
    total_Word1 = []
    total_Word2 = []
    total_Word3 = []
    total = []
    totalDocuments = 3

    #mets les mots qui sont des crées plus haut dans des listes sans repétition de mots ceci
    #pour pouvoir compter nombre d'apparitions dans differents fichiers
    for word in All_words1:
        if word not in total_Word1:
            total_Word1.append(word)
    for word in All_words2:
        if word not in total_Word2:
            total_Word2.append(word)
    for word in All_words3:
        if word not in total_Word3:
            total_Word3.append(word)

    #concatener les listes qui contiennent tous les mots sans repetition. tous
    #les mots qui sont dans cette liste apparaissent une seule fois dans chaque fichiers
    total = total_Word1 + total_Word2 + total_Word3
    fpres = {}

    #prendre les mots qui sont dans la liste total et le mettre dans le tuple fpres
    #si le mot se trouve deja dans le tuple incrementer son nombre d'apparitions
    #sinon mettre le mot dans le tuple lui donner 1 comme nombre d'apparitions
    for words in total:
        if words in fpres:
            fpres[words] += 1 #incrementation
        else:
            fpres[words] = 1 #une seule apparition

    #pour tout les mot qui sont dans le tuple fpres changer le nombre d'apparition en
    #facteur de presence ceci avec la formule donné au debut du code
    for total_Appear in fpres:
        fpres[total_Appear] = math.log(fpres[total_Appear] / totalDocuments)

    #fusionner dans une même liste les mots qui on le même facteur de presence
    result = []
    finish = False
    while not finish:
        best_tuple = max(fpres.values()) #meilleur facteur de présence dans le tuple
        best_fpres = []
        for word in fpres:
            #si le meilleur facteur de presence correspond au facteur de prence du mot
            #mettre le mot dans la liste best_fpres
            if best_tuple == fpres[word]:
                best_fpres.append(word)
        #construire une liste ave les tuples present dans resultat +
        #le tuple(la liste de mots qui ont le meilleur facteur de prence et
        #le meilleur facteur de precence)
        result.append((best_fpres,best_tuple))

        for word_in_result in best_fpres:
            #si un mot se trouve dans la liste de mots qui ont le meilleur facteur de presence
            #est dans le tuples fpres le supprimer
            if word_in_result in fpres:
                del(fpres[word_in_result]) #supprions dans le tuple fpres
                if not fpres:
                    finish = True

    return tuple(result)

#text_to_freq: parametre: Liste
              #retourne :  retourner un dictionnaire(tuple) contenant les mots et leurs
              #facteurs de présence.
              #ici les duplicats sont gardés vue que c'est pas spécifié dans l'exercice
def text_to_freq(All_words):
    tuple_Word_Frequency = {}
    for word in All_words:
        #si le mot se trouve plus d'une fois dans le fichier, incrémenter la frequence
        #la fréquence d'apparition du mot dans le fichier
        #sinon attribuer la valeur 1 à la frequence d'apparition
        if word in tuple_Word_Frequency:
            tuple_Word_Frequency[word] += 1 #incremente le facteur d'apparition
        else:
            tuple_Word_Frequency[word] = 1

    #pour tous les éléments dans le tuple, calculer la fréquence normalisée et remplacer
    #la frequence d'apparition par la frequence normalisé
    for totalappear in tuple_Word_Frequency:
        tuple_Word_Frequency[totalappear] = tuple_Word_Frequency[totalappear]/len(All_words)

    return tuple_Word_Frequency

#text_to_weight: parametre : Liste
                #retourne : Retourner un dictionnaire contenant les mots et leurs poids
def text_to_weight(A_List):
    fpres = 0
    freq = 0
    tuple_Words_fpres = fpres_mot()
    tuple_Words_freq = text_to_freq(A_List)
    weight_word = {}

    #cherche les correspondances entre les mots qui sont dans la liste passsé en parametre
    #et les mots qui sont dans les tuples tuple_Words_fpres et tuple_Words_freq
    for word in A_List:
        for find_fpres in tuple_Words_fpres:
            for word_list in find_fpres[0]: #prend uniquement la partie contenant les mots
                #s'il y a une correspondance entre les mots, prendre la partie
                #facteurs de presence et sortir
                if word == word_list:
                    fpres = find_fpres[1]   #partie facteur de presence
                    break #sortie
        #s'il y a une correspondance entre les mots, prendre la partie
        #fréquences normalisées et sortir
        for find_freq in tuple_Words_freq:
            if word == find_freq:
                freq = tuple_Words_freq[word] #fréquences normalisées
                break
        weight = freq * fpres
        weight_word[word] = weight

    #fusionner les tuple avec le meme poid et arranger les poids dans l'ordre croissant
    #Le code est deja commenté plus haut c'est le meme processus
    result = []
    finish = False
    while not finish:
        best_weight = max(weight_word.values())
        best_tuple = []
        for word in weight_word:
            if weight_word[word] == best_weight:
                best_tuple.append(word)

        result.append((best_tuple,best_weight))
        for word_in_result in best_tuple:
            if word_in_result in weight_word:
                del(weight_word[word_in_result])
                if not weight_word:
                    finish = True
    return tuple(result)
file1.close()
file2.close()
file3.close()
