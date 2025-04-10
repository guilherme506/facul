def funçao(a,b,c,d):
    count = 0
    for num in range(a,b):
        if count == c:
            print(d)
            count = 0
        else:
            print(num)
            count += 1
funçao(1, 10, 2 , 'Dois')