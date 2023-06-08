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
    profit=dataset['Price'].values[i]
    if dataset['Price'].values[i]>s1 and dataset['Price'].values[i]<s2:
        wei+=1
    if dataset['AC'].values[i]==ac:
        wei+=1
    if dataset['Food'].values[i]==f:
        wei+=1
    if dataset['Occupancy'].values[i]==o:
        wei+=1
    if dataset['AC'].values[i]=="yes":
        profit+=1
    if dataset['Food'].values[i]=="yes":
        profit+=1
    if dataset['Occupancy'].values[i]=="yes":
        profit+=1
    lis=[wei,profit,s]
    List.append(lis)
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
arr=[]
cap=(s1+s2)/2
if ac=="yes":
    cap+=1
if f=="yes":
    cap+=1
cap=cap+o
cap=3*cap
def ArrFun(arr,l):
    for i in l:
        arr.append(Item(i[0],i[1],i[2]))
    return arr
arr=ArrFun(arr,List)
max_val = Knapsack(cap, arr)
print(max_val)
