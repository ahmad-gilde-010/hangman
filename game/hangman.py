import random

print("""
 _    _              _   _    __   _  __              _   _ 
| |  | |     /\     | \ | |  / __| |  \/  |     /\     | \ | |
| |_| |    /  \    |  \| | | |  _  | \  / |    /  \    |  \| |
|  _  |   / /\ \   | . ` | | | | | | |\/| |   / /\ \   | . ` |
| |  | |  / __ \  | |\  | | |_| | | |  | |  / ___ \  | |\  |
||  || //    \\ || \|  \__| ||  || //    \\ || \_|

""")

def kies_woord():
    with open('words.txt', 'r', encoding='utf-8') as bestand:
        woordenlijst = bestand.readlines()
    return random.choice(woordenlijst).strip()

def toon_woord(woord, geraden_letters):
    weergave = ''
    for letter in woord:
        if letter in geraden_letters:
            weergave += letter + ' '
        else:
            weergave += '_ '
    return weergave.strip()

def toon_hangman(pogingen):
    hangman_figures = [
        """
           -----
           |   |
               |
               |
               |
               |
        ============
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ============
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ============
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ============
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ============
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ============
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ============
        """
    ]
    return hangman_figures[pogingen]

def hangman():
    woord = kies_woord()
    geraden_letters = []
    resterende_kansen = 6
    hangman_pogingen = 0

    print("Welkom bij Hangman!")
    print("Probeer het woord te raden.")
    print("Je hebt 6 kansen om het woord te raden voordat je verliest.")


    while resterende_kansen > 0:
        print(toon_woord(woord, geraden_letters))

        gok = input("Raad een letter: ").lower()

        if len(gok) != 1 or not gok.isalpha():
            print("Voer een letter in.")
            continue

        if gok in geraden_letters:
            print("Je hebt deze letter al geraden.")
            continue

        geraden_letters.append(gok)

        if gok not in woord:
            resterende_kansen -= 1
            hangman_pogingen += 1
            print(f"Fout! De letter '{gok}' zit niet in het woord. Je hebt nog {resterende_kansen} kansen over.")
            print(toon_hangman(hangman_pogingen))
        else:
            print("Goed geraden!")

        if all(letter in geraden_letters for letter in woord):
            print(f"Proficiat! Je hebt het woord geraden: {woord}")
            break
            

    if resterende_kansen == 0:
        print(f"Helaas, je hebt geen kansen meer over. Het woord was: {woord}")

if __name__ == "__main__":
    hangman()
