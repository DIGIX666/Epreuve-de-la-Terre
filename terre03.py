# Afficher l'alphabet en lui indiquant la lettre de départ en argument


import sys

for i in range(ord(sys.argv[1]), 123):
    print(chr(i), end=" ")