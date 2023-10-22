import random
import numpy as np
#ignore warnings created by comparing the datatype of num which can either be string or an array
import warnings
warnings.simplefilter(action='ignore',category=FutureWarning)
red=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black=[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
green=[0,37] #37->0
def bets(betType):
    global num
    global odds
    odds=1
    if betType==1:
        #num=int(input("Place your bet on a number: "))
        num=np.array([random.randint(0,37)])
        odds=36       
    elif betType==2:
        #num=int(input("Place your bet on 2 adjoining numbers: "))
        n1=random.randint(1,36)
        if n1%3==0:
            num=np.array([n1,n1-1])
        elif n1%3==1:
            num=np.array([n1,n1+1])
        else:
            n2=random.choice([n1-1,n1+1])
            num=np.array([n1,n2])
        odds=18 
    elif betType==3:
        #num=int(input("Place your bet on 3 numbers in a row: "))
        r=(random.randint(0,11))+1
        num=np.array([r,r+1,r+2])
        odds=12       
    elif betType==4:
        #num=int(input("Place your bet on 4 adjoinng numbers: "))
        n1=random.choice([random.randrange(1,36,3),random.randrange(3,37,3)])
        if n1%3==1:
            num=np.array([n1,n1+1,n1+3,n1+4])
        else:
            num=np.array([n1,n1-1,n1+2,n1+3])
        odds=9 
    elif betType==5:
        #num=int(input("Place your bet on 12 numbers: "))
        s=random.choice([1,13,25])
        num=np.arange(s,s+12)
        odds=3  
    elif betType==6:
        #num=int(input("Place your bet on 18 numbers in either half: "))
        h=random.choice([1,19])
        num=np.arange(h,h+18)
        odds=2
    elif betType==7:
        #num=input("Place your bet if its odd or even: ")
        num=random.choice(['odd','even'])
        odds=2
    elif betType==8:
        #num=input("Place your bet if its red or black: ")
        num=random.choice(['red','black'])
        odds=2
def spinresults(wheelnum,num,amt):
    if num == "odd":
        if wheelnum%2==1:
            return odds*amt
        else:
            return 0
    elif num == "even":
        if wheelnum%2==0:
            return odds*amt
        else:
            return 0
    elif num == "red":
        if wheelnum in red:
            return odds*amt
        else:
            return 0
    elif num == "black":
        if wheelnum in black:
            return odds*amt
        else:
            return 0
    elif wheelnum in num:
        return odds*amt
    else:
        return 0
#bal=int(input("Enter bank balance: "))
#bal=50000
#print("Balance is",bal)
#n=int(input("How many bets would u like to place: ))
profits=np.array([])
ndays=365
tbet=0
for i in range((ndays*100)):
    nplayers=random.randint(1,7)
    m=random.choices([1,2,3,4,5,6],weights=(4,5,6,3,1,1))
    n=random.randint(nplayers,(m[0]*nplayers))
    wheelnum=random.randint(0,38)
    dayprofit=0
    for i in range(n):
        #bettype=int(input("What type of bet would you like to place:\n1.Straight(35/1)- bet on one number\n2.Split(17/1)- bet on two numbers\n3.Street(11/1)- bet on a row\n4.Corner(8/1)- bet on 4 numbers\n5.Twelve(2/1)- bet on 1st,2nd or 3rd 12\n6.Eighteen(1/1)- bet on either of the 2 halves of the numbers\n7. Odd or Even(1/1)\n8.Color(1/1)- bet if its red or black))
        #amt=int(input("How much would you like to bet: ))
        casinoprofit=0
        betType=random.randint(1,8)
        maxbet=5000
        c=random.choices([5,10,25,random.randrange(50,maxbet,50)],weights=(1,2,2,15),k=1)
        amt=c[0]
        casinoprofit+=amt
        tbet+=amt
        bets(betType)
        winnings=spinresults(wheelnum,num,amt)
        casinoprofit-=winnings
        dayprofit+=casinoprofit
        #print("You won",winnings,"$ this round from a bet of",amt,"$")
    profits=np.append(profits,dayprofit)
print("Total profit over",ndays,"days is",np.sum(profits),"$")
print("Total amount betted is",tbet,"$")
print("House edge is",round((np.sum(profits)*100/tbet),2),"%")
print("Average daily profit is",np.average(profits)*100,"$")