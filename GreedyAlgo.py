import pandas as pd
dataset=pd.read_csv("C:\\Users\\vijay\\OneDrive - SSN Trust\\Desktop\\Project 4\\RoomHive\\GreedyAlgo.py")
List=[]
s1=4000
s2=5000
ac="yes"
f="yes"
o=3
for i in range(0,len(dataset)):
    s=dataset['Name'].values[i]+dataset['Address'].values[i]
    wei=1
    profit=not_result1['Price'].values[i]
    if not_result1['Price'].values[i]>s1 and not_result1['Price'].values[i]<s2:
        wei+=1
    if not_result1['AC'].values[i]==ac:
        wei+=1
    if not_result1['Food'].values[i]==f:
        wei+=1
    if not_result1['Occupancy'].values[i]==o:
        wei+=1
    if not_result1['AC'].values[i]=="yes":
        profit+=1
    if not_result1['Food'].values[i]=="yes":
        profit+=1
    if not_result1['Occupancy'].values[i]=="yes":
        profit+=1
    lis=[wei,profit,s]
    List3.append(lis)

class Item:
    def __init__(self, profit, weight, details):
        self.profit = profit
        self.weight = weight
        self.details = details

def Knapsack(W, arr):

    arr.sort(key=lambda x: (x.profit/x.weight), reverse=True)   

    list_of_hotels=[]

    for item in arr:

        if item.weight <= W:
            W -= item.weight
            list_of_hotels.append(item.details)

    return list_of_hotels
cap=(s1+s2)/2
if ac=="yes":
    cap+=1
if f=="yes":
    cap+=1
cap=cap+o
cap1=5*cap
def ArrFun(arr,l):
    for i in l:
        arr.append(Item(i[0],i[1],i[2]))
    return arr
arr1=ArrFun([],List1)
arr2=ArrFun([],List2)
arr3=ArrFun([],List3)
Suitable_result1 = Knapsack(cap1, arr1)
if len(Suitable_result1)>5:
    while True:
        if len(Suitable_result1)==5:
            break
        else:
            Suitable_result1.pop(-1)
print(Suitable_result1)
if len(Suitable_result1)!=5:
    cap2=(5-len(Suitable_result1))*cap
    Suitable_result2 = Knapsack(cap2, arr2)
    if len(Suitable_result1)+len(Suitable_result2)<5:
        print(Suitable_result2)
        cap3=(5-len(Suitable_result1)+len(Suitable_result2))*cap
        Suitable_result3 = Knapsack(cap3, arr3)
        while True:
            if len(Suitable_result1)+len(Suitable_result2)+len(Suitable_result3)==5:
                break
            else:
                Suitable_result3.pop(-1)
        print(Suitable_result3)
    elif len(Suitable_result1)+len(Suitable_result2)>5:
        while True:
            if len(Suitable_result1)+len(Suitable_result2)==5:
                break
            else:
                Suitable_result2.pop(-1)
        print(Suitable_result2)