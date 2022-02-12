while True:
    opt = input('Enter 1,2 or 3:\n\n(1) Round\n(2) Truncate\n(3) Exit\n')

    if opt=='1':
        x = float(input('Please use the point(.) instead of the comma!\n\nNumber: '))
        r = int(input('Round to how many decimals: '))
        print(round(x,r))

    elif opt=='2':
        x = float(input('Please use the point(.) instead of the comma!\n\nNumber: '))
        p = int(input('Truncate to how many decimals: '))
        def trunchiere(x):
            return int(x*10**p)/10**p
        print(trunchiere(x))

    elif opt=='3':
        exit()
        



 
