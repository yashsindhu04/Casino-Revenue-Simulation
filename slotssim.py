import random
import numpy as np
import matplotlib.pyplot as plt
def spin():
    global s
    s=np.array([random.randint(1,101),random.randint(1,101),random.randint(1,101)])
symbols=np.arange(56,77)
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
        return bet*3.5
    elif cs==2 and cj==1:
        return bet*51
    elif cs==1 and cj==2:
        return bet*251
    elif cj==3:
        return bet*1001
    elif cs==2:
        return bet*1.75
    elif cj==1:
        return bet*11
    elif cj==1 and cs==1:
        return bet*26
    elif cj==2:
        return bet*101
    else: 
        return 0

ndays=365
profits=np.array([])
for i in range(ndays):
    casinoprofit=0
    #max single bet can be of 100$ and min bet of 5$
    #bet is random
    bet=random.randrange(5,101,5)
    nspins=2400
    for n in range(nspins):
        winnings=0
        spin()
        winnings=odds(bet)
        casinoprofit+=(bet-(winnings*0.9))
    #print("Casino profit is",casinoprofit,"$")  
    profits=np.append(profits,casinoprofit)
print("Total profit over",ndays,"days is",np.sum(profits),"$")
print("Average daily profit is",np.average(profits),"$")
print("Maximum daily profit is",np.max(profits),"$")
print("Least daily profit is",np.min(profits),"$")
plt.bar(np.arange(1,ndays+1),profits,color='#DAA520')
plt.title("Daily profits in $")
