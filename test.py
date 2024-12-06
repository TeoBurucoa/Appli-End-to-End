import argparse

def check_even_odd(number):
    if number % 2 == 0:
        return "Le nombre est pair."
    else:
        return "Le nombre est impair."

def main():
    # Création du parseur d'arguments
    parser = argparse.ArgumentParser(description='Vérifie si un nombre est pair ou impair.')
    parser.add_argument('number', type=int, help='Le nombre à vérifier')
    
    # Parse les arguments
    args = parser.parse_args()
    
    # Utilise l'argument fourni
    result = check_even_odd(args.number)
    print(result)

if __name__ == "__main__":
    main()