from diygam import diigame
from choose import chose
def main():
    # list=[40,50,60,75]
    # list1=["S","M","L","XL"]

    sum=0
    # total = 0
    age=int(input("Enter age: "))
    destnation = input("enter your destnatuion: ")
    residentPriceinBsh = 20
    residentPriceObSh = 60
    while age>=18:

        sum1=chose()
        product = diigame()
        total = 0
        extraslice = input("do you want to extra slices y/n")
        if extraslice == "y":
            amountExtra = int(input("how many extra do yo want to add? "))
            total += sum+amountExtra*2
        else:
            total += sum

        if destnation == "beersheba":
            total +=sum1 +sum+ residentPriceinBsh
            print(total)
            print(total * (1 - (product/100)))
        else:
            total +=sum1+sum + residentPriceObSh
            print(total*(1-(product/100)))
        customer = input("do you want to contnue? y/n ")
        if customer == 'n':
            exit()
    print(" Soory you canot order!!")
# main()


