input_data = open('output.txt', 'r')
list_1=[]
list_1=input_data.readline().split()
for i in range(0, len(list_1)):
    list_1[i]=int(list_1[i]) 
input_data.close()
print("Введите искомый элемент: ")
n=input()
n=int(n)
pos=0



low=0
high=len(list_1)-1
mid=len(list_1)//2
while list_1[mid] != n and low<=high :
    if n>list_1[mid]:
        low=mid+1
    else : 
        high=mid-1
    mid=(low+high)//2
if low>high :  print("Элемента нет")
else : print("Позиция элемента при бинарном поиске: "+str(mid))



for i in range (len(list_1)):
    if n == list_1[i] : 
        pos=i
if pos==0 : print("Элемента нет")
else : print("Позиция элемента при линейном поиске: "+str(pos))