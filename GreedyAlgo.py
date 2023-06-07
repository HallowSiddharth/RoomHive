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
l=[[60,10,"ABC"],[100,20,"XYZ"],[120,30,"MNO"]]
def ArrFun(arr,l):
    for i in l:
        arr.append(Item(i[0],i[1],i[2]))
    return arr
arr=ArrFun(arr,l)
max_val = Knapsack(50, arr)
print(max_val)
