#
#   Write a program that generates a random number.
#
#   Output:
#   The random number is: 4
#
from random import randint
RAND_RANGE = 986234

def main():
    rand_number = randint(0,RAND_RANGE)
    print(rand_number)

if __name__ == "__main__":
    main()