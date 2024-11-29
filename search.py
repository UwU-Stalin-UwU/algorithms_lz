input_data = open('output.txt', 'r')     #ввод с предыдущего задания
list_1=[]
list_1=input_data.readline().split()
for i in range(0, len(list_1)):
    list_1[i]=int(list_1[i]) 
input_data.close()
print("Введите искомый элемент: ")    #ввод искомого элемента
n=input()
n=int(n)
pos=10101010     #для линейного поиска
kollin=0
kolbin=0


#бинарный поиск
#поиск числа в листе относительно центра промежутка
#если число больше/меньше центра, то нижняя/верхняя граница меняется на предыдущую середину+/-1
#и находится середина между новыми границами
#когда совпадет элемент листа с искомым, середина будет являться индексом в листе
low=0
high=len(list_1)-1
mid=len(list_1)//2
while list_1[mid] != n and low<=high :
    if n>list_1[mid]:
        low=mid+1
    else : 
        high=mid-1
    mid=(low+high)//2
    kolbin+=1
if low>high :  print("Элемента нет")
else : print("Позиция элемента при бинарном поиске: "+str(mid+1))
print("Количество опреаций при бинарном поиске: "+str(kolbin))


#линейный поиск
#просто перебираем, пока не найдем
for i in range (len(list_1)):
    kollin+=1
    if n == list_1[i] : 
        pos=i
        break
if pos==10101010 : print("Элемента нет")
else : print("Позиция элемента при линейном поиске: "+str(pos+1))
print('Количество операций при линейном поиске: '+str(kollin))