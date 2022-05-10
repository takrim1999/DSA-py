def call(n):
    if n<1:
        print("0th")
    else:
        print(f"{n}th")
        call(n-1)
        

call(6)