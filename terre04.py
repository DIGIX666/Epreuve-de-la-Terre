# Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair.
# Attention : gérez aussi les entiers négatifs.

import sys


def main(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


if len(sys.argv) == 2:
    if main(sys.argv[1]):
        if int(sys.argv[1]) % 2 == 0:
            print("Pair")
        else:
            print("Impair")
    else:
        print("Tu ne me la mettras pas à l’envers.")

else:
    print("Tu ne me la mettras pas à l’envers.")

if __name__ == "main":
    main()