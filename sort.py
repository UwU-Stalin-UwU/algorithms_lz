import random as rand
list_1=[]
for i in range (0, 100):
    x=rand.randint(0, 1000000)
    list_1.append(x)
#print(list_1)
list_2=list_1.copy()
kol1=0
kol2=0



for i in range(len(list_1)-1):
    for j in range(len(list_1)-1-i):
        if list_1[j] > list_1[j+1]:
            list_1[j], list_1[j+1] = list_1[j+1], list_1[j]
            kol1+=1
        print(list_1)
output_data=open('output.txt', 'w')
for i in list_1 :
    output_data.write(str(i) + ' ')
output_data.close()


razm=len(list_2)
for i in range(razm-1):
        m = i
        for j in range(i+1, razm):
            if list_2[j] < list_2[m]:
                m = j
                kol2+=1
        list_2[i], list_2[m] = list_2[m], list_2[i]
        print(list_2)
print(list_2)
print("Количество сравнений при пузырьке: " + str(kol1))
print("Количество сравнений при выборе: " + str(kol2))