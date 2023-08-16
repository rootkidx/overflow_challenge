
def asciiArt():                                   
    print('   )         (              )                 )')
    print('( /(         )\  (       ( /(     (   (    ( /(  ')
    print(' )\())  `  ) ((_)))\ (    )\())   ))\( )\   )(_))')
    print('((_)\   /(/(  _ /((_))\  ((_)\   /((_)(( ) ((_)')
    print(' / (_) ((_)_\| (_))(((_)  / (_) (_))((_)_) |_  )')
    print(" | |   | '_ \) | || (_-<  | |   / -_) _` |  / / ")
    print(' |_|   | .__/|_|\_,_/__/  |_|   \___\__, | /___|  ')
    print('       |_|                             |_| ')    
    print()


def check_overflow(a, b):
    sum = a+b
    if (abs(sum) > (2 ** 31 - 1)):
        return True
    return False

def main():
    asciiArt()
    while 1:
        try:
            a = int(input('Enter num1 >> '))
            b = int(input('Enter num2 >> '))

            if check_overflow(a,b):
                print()
                print("ZmxhZ3swdjNyZjEwd19lQTV5XzNhU3l9")
                print()
            else:
                print()
                print(a+b)
                print()
        except Exception:
            print()
            print('wrong input')
            print()

if __name__ == "__main__":
    main()
