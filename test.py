a = "America NUUUUUKEEEE Oooobaaaamaaaaa"

a = a.lower()
glas = 'aeiou'
main = 0
some = 0

if a[0] in glas:
    main += 1
    print('сработало первое условие')
for i in range(len(a)-1):
    if (a[i] != a[i+1]) and a[i+1] in glas:
        print(f'Второе условие {a[i]} and {a[i+1]}')
        main +=1

    elif (a[i] == a[i+1]) and a[i+1] in glas:
        some += 1



print(round(some/main, 2))









