while True:
    opt = input('(1) Round\n(2) Truncate\n(3) Exit\n')

    if opt=='1':
        x = float(input('Number: '))
        r = int(input('Round to how many decimals '))
        print(round(x,r))

    elif opt=='2':
        x = float(input('Number: '))
        p = int(input('Truncate to how many decimals: '))
        def trunchiere(x):
            return int(x*10**p)/10**p
        print(trunchiere(x))

    elif opt=='3':
        exit()
        



 
