def hanoi(n , avali , akhary , komaki):
    if n > 0:
        hanoi(n-1 , avali , komaki , akhary)
        print(f"{n} ----> {akhary}")
        hanoi(n-1 , komaki , akhary , avali)



hanoi(64 , 1 , 3 , 2)