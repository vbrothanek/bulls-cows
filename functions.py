import random

DUAL_DIVIDER = 60 * "="
SIMPLE_DIVIDER = 60 * "-"


def welcome():
    print(DUAL_DIVIDER, "Vitejte ve hre Bulls & Cows", DUAL_DIVIDER, sep="\n")
    print("""Pravidla hry:
             Cilem hry je uhadnout nahodne vygenerovane 4 mistne, 5 mistne nebo 6 mistne cislo.

             Pri kazdem zadani cisla je za potrbi zadat cele cislo. (1234)
             Program na vase zadani dopovida Bulls x & Cows y, kdy misto x a y nahrazuje pocet uhodnutych cisel a
             cisel na spravnych pozicich. 
             
             Bulls - Uhodnuta cisla ktere jsou zaroven na spravne pozici.
             Cows - Uhodnute cislo ktere je na nespravne pozici.
    """)
    print(SIMPLE_DIVIDER)

    return ""



def user_guess_input(user_guess):
    user_input_str = str(user_guess)

    if len(user_input_str) > len(generated_number()) or len(user_input_str) < len(generated_number()):
        print("Prilis mnoho nebo malo cisel..")
        exit()

    else:
        return user_input_str


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
    number_of_numbers = int(input("Zadejte s kolika cisly chcete hrat: 4,5,6: \n"))

    if number_of_numbers < 4 or number_of_numbers > 6:
        print("Spatne zadane zadane udaje! :-( ")
        exit()
    else:
        return number_of_numbers



def generated_number(level):
    random_number = random.sample(range(1, 10), k=level)

    random_list = []
    for item in random_number:
        random_number_str = str(item)
        random_list.append(random_number_str)


    return "".join(random_list)




if __name__ == "__main__":
    a = game_level()
    print(a)

