from functions import *
import re


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

        while secret_number_loop != len(user_guess) or user_guess.isalpha():
            user_guess = input(f"Prosim zadejte vas tip \n")
            # print(len(user_guess), ",", secret_number_loop)

            found_wrong_letter = re.search("[a-zA-Z!@#$%^&*()_+}{|';/.,]", user_guess)
            if found_wrong_letter != None:
                print("Vase zadani obsahuje pismena, zadejte Vas tip znova..", print(found_wrong_letter))
                # continue
            else:
                if len(user_guess) < secret_number_loop:
                    print("Zadali jste prilis malo znaku.. Zadejte Vas tip znova", SIMPLE_DIVIDER, sep="\n")
                elif len(user_guess) > secret_number_loop:
                    print("Zadali jste prilis mnoho znaku.. Zadejte Vas tip znova", SIMPLE_DIVIDER, sep="\n")



        count_asking += 1
        comparsion = number_comparsion(user_guess, secret_number)

        if comparsion == {
            "Bulls": level,
            "Cows": 0
        }:
            print(DUAL_DIVIDER)
            print(f"Dobra hra! Zvladnul jsi to na {count_asking} pokus :-)")
            print(DUAL_DIVIDER)
            break
        else:
            print(SIMPLE_DIVIDER)
            print(f"Bulls: {comparsion['Bulls']} & Cows: {comparsion['Cows']}")
            print(SIMPLE_DIVIDER)

if __name__ == "__main__":
    main()
