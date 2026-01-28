"""
Luke Riley

CSE 120 - Intro to Python

Final Project - CSE 110 Programming Companion
"""

#Import
from math import gcd

while True:
    #Print Intro and Menu
    print("\nWelcome to the CSE 110 - Mathematical Foundations for Computer Science Programming Companion\n")
    print("What would you like to do?\n")
    print("=== M E N U ===")
    print("1) Sieve of Eratosthenes")
    print("2) Number Systems Conversion")
    print("3) Matrices")
    print("4) Totient Function")
    print("5) Exit")

    #Menu user input
    choice = int(input("Enter your choice: "))

    #Sieve of Eratosthenes
    if choice == 1:
        def sieve_of_eratosthenes(num):
            primes = [True] * (num + 1)
            p = 2
            #Iterate up to number chosen by user
            while p * p <= num:
                if primes[p]:
                    for i in range(p * p, num + 1, p):
                        primes[i] = False
                p += 1

            prime_numbers = [p for p in range(2, num + 1) if primes[p]]
            return prime_numbers

        #Information/Description
        print("\nThe Sieve of Eratosthenes is a simple algorithm that finds the prime numbers up to a given integer\n")

        num = int(input("Enter a number: "))
        primes = sieve_of_eratosthenes(num)

        print("List of Prime Numbers Less Than or Equal to", num)
        print(sieve_of_eratosthenes(num))
        print(len(sieve_of_eratosthenes(num)))

    #Base Number Conversions
    if choice == 2:
        #Information/Description
        print("Most of the world uses base 10 (decimal) numbers for everyday calculations.\n"
              "However, computers use binary (base 2) numbers for processing data. Occasionally,\n"
              "humans and computers utilize base 16 (hexadecimal) to represent data such as cryptographic hashes.\n")

        dec = int(input("Enter a number in base 10: "))
        print("What do you want to convert", dec, "to?")
        print("1) Binary")
        print("2) Octal")
        print("3) Hexadecimal")
        print("")

        base_choice = int(input("Enter your choice: "))

        if base_choice == 1:
            #convert to binary
            print("The value of", dec, "is:")
            print(bin(dec), "in binary")

        if base_choice == 2:
            #convert to octal
            print("The value of", dec, "is:")
            print(oct(dec), "in octal")

        if base_choice == 3:
            #convert to hexadecimal
            print("The value of", dec, "is:")
            print(hex(dec), "in hexadecimal")

        if base_choice != 1 or base_choice != 2 or base_choice != 3:
            print("Invalid choice. Try again.")


    #Adding and Multiplying Matrices
    if choice == 3:
        print("\nWhat would you like to do: ")
        print("1) Add matrices")
        print("2) Multiply matrices")
        matrix_choice = int(input("Enter your choice: "))
        if matrix_choice == 1:
            #Adding matrices
            def add_matrices(matrix1, matrix2):
                if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
                    print("ERROR: Matrices must have the same dimensions for addition")

                rows = len(matrix1)
                cols = len(matrix1[0])
                result = [[0 for _ in range(cols)] for _ in range(rows)]

                for i in range(rows):
                    for j in range(cols):
                        result[i][j] = matrix1[i][j] + matrix2[i][j]
                return result

            #Matrix A
            print("Enter the values of the Matrix A: \n")
            A = [[int(input("R1C1: ")), int(input("R1C2: "))], [int(input("\nR2C1: ")), int(input("R2C2: "))]]

            #Matrix B
            print("\nEnter the values of the Matrix B: \n")
            B = [[int(input("R1C1: ")), int(input("R1C2: "))], [int(input("\nR2C1: ")), int(input("R2C2: "))]]

            #Matrix C
            C = add_matrices(A, B)

            print("\nMatrix Addition Result:")
            for row in C:
                print(row)

        if matrix_choice == 2:
            #Multiply Matrices
            def multiply_matrices(matrix1, matrix2):
                rows1 = len(matrix1)
                cols1 = len(matrix1[0])
                rows2 = len(matrix2)
                cols2 = len(matrix2[0])

                #Error Handling
                if cols1 != rows2:
                    print("ERROR: To multiply matrices the number of of rows in one and columns in the other have to be the same.")

                result = [[0 for _ in range(cols2)] for _ in range(rows1)]

                for i in range(rows1):
                    for j in range(cols2):
                        for k in range(cols1):
                            result[i][j] += matrix1[i][k] * matrix2[k][j]
                return result

            #User input - fill in matrix
            #Matrix A
            print("Enter the values of the Matrix A: \n")
            A = [[int(input("R1C1: ")), int(input("R1C2: ")), int(input("R1C3: "))], [int(input("\nR2C1: ")), int(input("R2C2: ")), int(input("R2C3"))]]

            #Matrix B
            print("\nEnter the values of the Matrix B: \n")
            B = [[int(input("R1C1: ")), int(input("R1C2: "))], [int(input("\nR2C1: ")), int(input("R2C2: "))], [int(input("\nR3C1: ")), int(input("R3C2: "))]]

            #Matrix C
            C = multiply_matrices(A, B)
            print("\nMatrix Multiplication Result:")
            for row in C:
                print(row)

    #Totient Function
    if choice == 4:
        def phi(n):
            amount = 0
            for k in range(1, n + 1):
                if gcd(n, k) == 1:
                    amount += 1
            return amount

        #Info/Description
        print("The totient function counts the number of positive integers up to a given integer 'n' that are relatively prime to 'n'.\n"
              "Two numbers are relatively prime if their greatest common divisor is 1\n")

        n = int(input("Enter a number to compute the totient function: "))
        print("\nThe totient function results are:")
        print(phi(n))

    if choice == 5:
        print("Good luck studying!")
        print("EXITING...")
        break






