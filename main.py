from functions import *



def main():
    print(welcome())
    level = game_level()
    secret_number = generated_number(level)
    # print(f"DEBUG GENERATED NUMBER {secret_number}")
    count_asking = 0

    while True:
        user_guess = input(f"Prosim zadejte vas tip \n")
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
            print(f"Bulls: {comparsion['Bulls']}, Cows: {comparsion['Cows']}")





if __name__ == "__main__":
    main()