import random
from words import word_list

def prendi_parola():
    word = random.choice(word_list)
    return word.upper()

def gioca(word):
    word_completamento = "_" * len(word)
    trovata = False
    trovate_lettere = []
    trovate_parole = []
    tentativi = 6
    print("Iniziamo!")
    print(mostra_pipotto(tentativi))
    print(word_completamento)
    print("\n")
    while not trovata and tentativi > 0:
        indovina = input("Inserisci la lettera o parola:  ").upper()
        if len(indovina) == 1 and indovina.isalpha():
            if indovina in trovate_lettere:
                print("Hai già indovinato sta lettera", indovina)
            elif indovina not in word:
                print(indovina, "sei nabbo, non è nella parola")
                tentativi -= 1
                trovate_lettere.append(indovina)
            else:
                print("Hai indovinato", indovina, "è nella parola")
                trovate_lettere.append(indovina)
                parole_nella_lista = list(word_completamento)
                indici = [i for i, lettera in enumerate(word) if lettera == indovina] 
                for indice in indici:
                    parole_nella_lista[indice] = indovina
                word_completamento="".join(parole_nella_lista)
                if "_" not in word_completamento:
                    trovata = True
        elif len(indovina) == len(word) and indovina.isalpha():
            if indovina in trovate_parole:
                print("Già indovinatà")
            elif indovina != word:
                print(indovina, "Non è la parola")
                tentativi -= 1
                trovate_parole.append(indovina)
            else:
                trovata = True
                word_completamento = word_list
        else:
            print("Non è valido")
        print(mostra_pipotto(tentativi))
        print(word_completamento)
        print("\n")
    if trovata:
        print("GG, indovinata!")
    else:
        print("Suca nabbo, riprova")

def mostra_pipotto(tentativi):
    step = [
            # PARTE FINALE
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # INIZIO
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return step[tentativi]

def inizio():
    word = prendi_parola()
    gioca(word)
    while input("Gioca contro (S/N)").upper() == "S":
        word = prendi_parola()
        gioca(word)

if __name__ == "__main__":
    inizio()
