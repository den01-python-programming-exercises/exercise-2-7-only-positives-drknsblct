def main():
    #write your code below this line
    while True:
        num = int(input('Give a number:'))
        if num == 0:
            break
            
        elif num < 0:
            print('Unsuitable number')

        else:
            print(num**2)

if __name__ == '__main__':
    main()
