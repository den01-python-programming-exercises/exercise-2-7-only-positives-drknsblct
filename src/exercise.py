
def main():
    #write your code below this line

    while True:
        num = int(input('Give a number:'))
        if num == 0:
            break
            
        # it's cleaner to use an if statement instead of an elif 
        # because if the above statement is true the loop breaks so both ifs won't be executed
        if num < 0:
            print('Unsuitable number')

        else:
            print(num**2)

if __name__ == '__main__':
    main()
