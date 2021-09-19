def main():
    #write your code below this line
    while True:
        number = int(input("Input a number"))

        if (number == 0):
            break

        if (number <= 0):
            print("Invalid number! Try again.")
            continue

        print(number * number)

if __name__ == '__main__':
    main()
