from functions import *


result = number_comparsion("8765", "3456")

assert result == {
    "Bulls": 0,
    "Cows": 2
}

assert number_comparsion("2345", "9876") == {
    "Bulls": 0,
    "Cows": 0
}

assert number_comparsion("2345", "2378") == {
    "Bulls": 2,
    "Cows": 0
}

assert number_comparsion("2345", "2346") == {
    "Bulls": 3,
    "Cows": 0
}

assert number_comparsion("2345", "2345") == {
    "Bulls": 4,
    "Cows": 0
}

# TEST WRONG INPUT
def test_wrong_input(user_input, secret_number):
    try:
        number_comparsion(user_input, secret_number)
        assert True is False

    except ValueError as error:
        print(error)

test_wrong_input("824", "8263")
test_wrong_input("8246", "263")
test_wrong_input(3456, "8263")
test_wrong_input("8246", 9543)
test_wrong_input(9234, 6498)
test_wrong_input(None, None)
test_wrong_input("", "")




