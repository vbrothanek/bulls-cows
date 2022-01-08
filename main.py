from functions import *


def main():
    print(welcome())
    level = game_level()
    print(SIMPLE_DIVIDER)
    secret_number = generated_number(level)
    # print(f"DEBUG GENERATED NUMBER {secret_number}")
    count_asking = 0

    secret_number_loop = len(secret_number)

    while True:

        user_guess = ""

        while not user_guess.isnumeric() or secret_number_loop != len(user_guess):
            user_guess = input(f"Prosím zadejte Váš tip. \n")

            if secret_number_loop == len(user_guess) and user_guess.isnumeric():
                break
            elif user_guess.isalpha():
                print("Vaše zadání obsahuje písmena, zadejte Váš tip znovu.", SIMPLE_DIVIDER, sep="\n")
            elif secret_number_loop != len(user_guess):
                if len(user_guess) < secret_number_loop:
                    print("Zadali jste příliš málo znaků. Zadejte Váš tip znovu.", SIMPLE_DIVIDER, sep="\n")
                elif len(user_guess) > secret_number_loop:
                    print("Zadali jste příliš mnoho znaků. Zadejte Váš tip znovu.", SIMPLE_DIVIDER, sep="\n")
            else:
                print("Chyba v zadání. Zadejte Váš tip znovu.", SIMPLE_DIVIDER, sep="\n")


        count_asking += 1
        comparsion = number_comparsion(user_guess, secret_number)

        if comparsion == {
            "Bulls": level,
            "Cows": 0
        }:
            print(DUAL_DIVIDER)
            print(f"Výborná práce! Zvládli jste to na {count_asking} platných pokusů :-)")
            print(DUAL_DIVIDER)
            # new_game()
            break
        else:
            print(SIMPLE_DIVIDER)
            print(f"Bulls: {comparsion['Bulls']} & Cows: {comparsion['Cows']}")
            print(SIMPLE_DIVIDER)



if __name__ == "__main__":
    main()
