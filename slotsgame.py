import random
import numpy as np
#3 symbols - 2/1
#2 symbols and $ sign - 50/1
#1 symbol and 2 $ signs - 500/1
#jackpot - 10000/1
def spin():
    global s
    s=np.array([random.randint(1,101),random.randint(1,101),random.randint(1,101)])
symbols=np.arange(66,77)
jackpot=np.arange(99,101)
def odds(bet):
    cs=0
    cj=0
    for i in s:
        if i in symbols:
            cs+=1
        elif i in jackpot:
            cj+=1
    if cs==3:
        return bet*3
    elif cs==2 and cj==1:
        return bet*51
    elif cs==1 and cj==2:
        return bet*501
    elif cj==3:
        return bet*10001
    else: 
        return 0

casinoprofit=0
credit=100000
#max single bet can be of 100$ and min bet of 5$
#bet is random
bet=random.randrange(5,101,5)
nspins=2400
for n in range(nspins):
    if credit<bet:
        print("You are out of credits")
        break
    else:
        winnings=0
        credit-=bet
        spin()
        winnings=odds(bet)
        if winnings>0:
            print("You won",winnings,"$ in round",n+1)
        credit+=(winnings*0.9)
        casinoprofit+=(bet-(winnings*0.9))
print("Your current balance is",credit,"$")
print("Casino profit is",casinoprofit,"$")