def chose():
    sum1=0
    list = [40, 50, 60, 75]
    list1 = ["S", "M", "L", "XL"]
    tyap = input("Enter size  of pizza: ")
    for tr in list1:
        sum1 += list[list1.index(tyap)]
        break
    return sum1
# chose()