a = int(input())   #500yen coin
b = int(input())   #100yen coin
c = int(input())   #50yen coin
x = int(input())   #Total amount
num_combination = 0
for n500 in range(0,a+1):
    for n100 in range(0,b+1):
        n50 = (x - n500*500 - n100*100)//50
        if n50<= c and n50>=0:
            #print (n500,n100,n50)

            num_combination += 1


print(num_combination)