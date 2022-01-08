# from main import *
import random

DUAL_DIVIDER = 70 * "="
SIMPLE_DIVIDER = 70 * "-"


def welcome():
    print(DUAL_DIVIDER, "Vítejte ve hře Bulls & Cows!", DUAL_DIVIDER, sep="\n")
    print("""Pravidla hry:
    Cílem hry je odhalit náhodně vygenerované čtyřmístné, 
    pětimístné nebo šestimístné číslo.

    Při každém pokusu je nutné zadat číslo, které se skládá z počtu
    číslic dle vybrané úrovně.
    Program na Vaše zadání vyhodnotí Bulls (x) & Cows (y), 
    kdy x a y nahrazuje počet uhodnutých číslic a
    číslic na správné pozici. 
     
    Bulls - Počet uhodnutých číslic, které jsou na správném místě.
    Cows - Počet uhodnutých číslic, které jsou zvoleny dobře,
           ale na nesprávné pozici.
    """)
    print(SIMPLE_DIVIDER)

    return ""


def number_comparsion(user_input_str, secret_number):
    if not isinstance(user_input_str, str) or not isinstance(secret_number, str):
        raise ValueError("Wrong input")

    bulls_count = 0
    cows_count = 0


    for i in range(len(user_input_str)):
       user_number = user_input_str[i]
       gen_number = secret_number[i]

       if user_number == gen_number:
            bulls_count += 1


       elif user_number in secret_number and user_number != gen_number:
            cows_count += 1


    return {
       "Bulls": bulls_count,
       "Cows": cows_count
    }


def game_level():
    number_of_numbers = 0
    levels = [4, 5, 6]

    while number_of_numbers not in levels:
        number_of_numbers = int(input("Zadejte úroveň hry: 4,5,6: \n"))

        if number_of_numbers < 4 or number_of_numbers > 6:
            print("Špatně zadané údaje! Prosím, znovu zvolte úroveň hry.")
        else:
            return number_of_numbers



def generated_number(level):
    random_number = random.sample(range(1, 10), k=level)

    random_list = []
    for item in random_number:
        random_number_str = str(item)
        random_list.append(random_number_str)


    return "".join(random_list)

# def new_game():
#     answers = ["Y", "N"]
#     new_game_answer = ""
#     while new_game_answer not in answers:
#         new_game_answer = input('Pro novou hru zadejte "Y", pro ukonceni hry zadjete "N".').upper()
#
#         if new_game_answer == "Y":
#             main()
#         elif new_game_answer == "N":
#             print("Dekujeme za hru :-)")
#             exit()




if __name__ == "__main__":
    a = game_level()
    print(a)

