#Le code ci-dessous:
                    #Inclus le module qui doit contenir les fonctions file_to_list, fpres_mot,
                    #text_to_freq, text_to_weight
                    #Lit les documents et fait les calculs;
                    #Pour chaque document, affiche les N mots avec les plus haut poids
                    #(affiche N plus haut paires de mots : poids). N est être paramétrable
                    #et on peut le changer dans le code du test.

#Dans le module textfreq importer toute les fonctions
from textfreq import *

#lire les documents et faire les calculs
tuple_Word_Weight1 = text_to_weight(All_words1)
tuple_Word_Weight2 = text_to_weight(All_words2)
tuple_Word_Weight3 = text_to_weight(All_words3)

#N_best: parametre: entier (qui est les N premiers)
def N_best (N):
    print ('les ' + repr(N) + ' premiers poids du document 1 sont:')

    #si N > nombre d'éléments alors trop d'éléments demandé
    #si non afficher les N premiers éléments de la liste
    if N > len(tuple_Word_Weight1):
        print('out of stack')
    else:
        for i in range(N):
            print('{0} : {1}'.format(tuple_Word_Weight1[i][0], tuple_Word_Weight1[i][1]))
    print('\n') #saut à la ligne
    print ('les ' + repr(N) + ' premiers poids du document 2 sont:')
    if N > len(tuple_Word_Weight2):
        print('out of stack')
    else:
        for i in range(N):
            print('{0} : {1}'.format(tuple_Word_Weight2[i][0], tuple_Word_Weight1[i][1]))
    print('\n')
    print ('les ' + repr(N) + ' premiers poids du document 3 sont:')
    if N > len(tuple_Word_Weight3):
        print('out of stack')
    else:
        for i in range(N):
            print('{0} : {1}'.format(tuple_Word_Weight3[i][0], tuple_Word_Weight1[i][1]))


#Requête
N_best(1)
