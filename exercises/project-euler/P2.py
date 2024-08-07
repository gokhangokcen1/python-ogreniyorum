def fib():
    first = 1
    second = 1
    temp = 0
    total = 0
    while second < 4000000:      
        temp = second
        second = first + second
        first = temp 
        if second % 2 == 0:
            total += second
    print("total: {}".format(total))

        

fib()