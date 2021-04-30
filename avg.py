def avg(list):
    total = 0
    if(list):
        for num in list:
            try:
                num = int(num)
            except:
                print("list values must be numbers")
                return False
            total += num
        return total/len(list)
    print("empty list")
    return 0