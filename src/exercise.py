def main():
    #write your code below this line
    while True:
        number = int(input("Give a number:"))

        if (number == 0):
            break

        if (number <= 0):
            print("Unsuitable number")
            continue

        print(number * number)

if __name__ == '__main__':
    main()
