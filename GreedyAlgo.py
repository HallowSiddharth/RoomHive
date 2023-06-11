import pandas as pd
df=pd.read_csv("C:\\Users\\vicky\\OneDrive\\Desktop\\Project_4th_sem\\RoomHive\\hotels_list.csv")
try:
  if df.isna().sum().sum() != 0:
    df = df.dropna()
except:
  print("Something went wrong when checking for null values")

df['Occupancy'] = df['Occupancy'].astype(int)

f = 'yes'
ac = 'yes'
o = 2
s1 = 1000
s2 = 4000
condition = (df['Food'] == f) & (df['AC'] == ac) & (df['Occupancy'] >=o) & (df['Price'] <= s2) & (df['Price']>=s1)
result = df[condition]
not_result = df[~condition]
condition1=(not_result['Price'] <= s2) & (not_result['Price'] >= s1)
result1=not_result[condition1]
not_result1=not_result[~condition1]
List1=[]
List2=[]
List3=[]
for i in range(0,len(result)):
    s=result['Name'].values[i]+result['Address'].values[i]
    wei=1
    profit=result['Price'].values[i]
    if result['Price'].values[i]>s1 and result['Price'].values[i]<s2:
        wei+=1
    if result['AC'].values[i]==ac:
        wei+=1
    if result['Food'].values[i]==f:
        wei+=1
    if result['Occupancy'].values[i]==o:
        wei+=1
    if result['AC'].values[i]=="yes":
        profit+=1
    if result['Food'].values[i]=="yes":
        profit+=1
    if result['Occupancy'].values[i]=="yes":
        profit+=1
    lis=[wei,profit,s]
    List1.append(lis)
for i in range(0,len(result1)):
    s=result1['Name'].values[i]+result1['Address'].values[i]
    wei=1
    profit=result1['Price'].values[i]
    if result1['Price'].values[i]>s1 and result1['Price'].values[i]<s2:
        wei+=1
    if result1['AC'].values[i]==ac:
        wei+=1
    if result1['Food'].values[i]==f:
        wei+=1
    if result1['Occupancy'].values[i]==o:
        wei+=1
    if result1['AC'].values[i]=="yes":
        profit+=1
    if result1['Food'].values[i]=="yes":
        profit+=1
    if result1['Occupancy'].values[i]=="yes":
        profit+=1
    lis=[wei,profit,s]
    List2.append(lis)
for i in range(0,len(not_result1)):
    s=not_result1['Name'].values[i]+not_result1['Address'].values[i]
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