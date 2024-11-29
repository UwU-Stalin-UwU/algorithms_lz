import random as rand                    #создание листа из рандомных чисел
list_1=[]
for i in range (0, 100):
    x=rand.randint(0, 1000000)
    list_1.append(x)
list_2=list_1.copy()
kol1=0                                   #переменные для подсчета количества итераций
kol2=0


#сортировка пузырьком
#идем по каждому элементу листа и проверяем со следующим
#если он больше следующего, меняем местами
for i in range(len(list_1)-1):
    for j in range(len(list_1)-1-i):
        if list_1[j] > list_1[j+1]:
            list_1[j], list_1[j+1] = list_1[j+1], list_1[j]
            kol1+=1
        print(list_1)
output_data=open('output.txt', 'w')#для задания с поиском
for i in list_1 :
    output_data.write(str(i) + ' ')
output_data.close()

#сортировка выбором
# длина списка 
n=len(list_2)                                    
# главный цикл
for i in range(n):         
    print("До    :",list_2)   
    # ищем минимум на отрезке [i,n-1]
    mi=list_2[i] 
    ii=i
    for j in range(i,n): 
        if list_2[j]<mi:
            kol2 +=1
            # минимум
            mi=list_2[j]                     
            # меняем i-й с минимумом 
        list_2[i],list_2[j]=list_2[j],list_2[i]       
    print("После :",list_2)
    print()

#выводы
print("Отсортированные числа: ", list_2)
print("Количество сравнений при пузырьке: " + str(kol1))
print("Количество сравнений при выборе: " + str(kol2))