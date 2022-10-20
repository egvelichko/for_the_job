import math
import numpy as np

a = np.array([[0,	0,	22500,	14015,	8200,	12200,	0,	0,	0,	8200,	0,	0,	22500,	0,	22215,	0,	0,	0,	0,	8200,	0,	0,	22500,	0,	20400,	14015,	0,	12100,	61750,	8200],
[0,	0,	0,	16250,	8200,	14200,	0,	0,	0,	33765,	0,	25100,	0,	0,	24450,	0,	0,	0,	0,	33765,	0,	0,	0,	0,	22400,	16250,	0,	25100,	31850,	39020],
[0,	0,	16500,	0,	10100,	8600,	0,	0,	0,	22300,	0,	13150,	16500,	0,	10100,	0,	0,	0,	0,	22300,	0,	0,	16500,	0,	18700,	0,	0,	13150,	57650,	22300],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	9980,	0],
[0,	0,	2226,	0,	0,	0,	0,	0,	0,	0,      0,	0,	2226,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2226,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	8200,	12200,	0,	0,	0,	32500,	0,	0,	0,	0,	8200,	0,	0,	0,	0,	32500,	0,	0,	0,	0,	20400,	0,	0,	0,	34160,	32500],
[0,	0,	4600,	5400,	8200,	0,	0,	0,	0,	8200,	0,	6500,	4600,	0,	13600,	0,	0,	0,	0,	8200,	0,	0,	4600,	0,	8200,	5400,	0,	6500,	0,	0],
[0,	0,	12450,	3800,	8200,	0,	0,	0,	0,	34500,	0,	0,	12450,	0,	12000,	0,	0,	0,	0,	34500,	0,	0,	12450,	0,	8200,	3800,	0,	0,	55100,	8200],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	4100,	0,	0,	0,	0,	0,	0,	0,	0,	0,	4100,	0,	0,	0,	0,	0,	0,	0,	0,	9900,	32500],
[0,	0,	0,	0,	3200,	0,	0,	0,	0,	3200,	0,	0,	0,	0,	3200,	0,	0,	0,	0,	3200,	0,	0,	0,	0,	3200,	0,	0,	0,	15600,	3200]])

arrayNeeds = a.transpose()

# print(arrayNeeds)

x, power, newPertia = 0, 0, 0

listX = []  # оптимальная партия
C1 = 3000  # стоимость наладки
C2 = 0.450  # затраты на хранени за тонну в мес
listQ = [256995, 290350, 247850, 9980, 6678, 180660, 92200, 231950, 22200, 34800]  # потребность в месяц
listOst = [25670, 33830, 16400, 3550, 3600, 24550, 7800, 22780, 3600, 5260]  # остаток на начало месяца
listOst1 = listOst.copy()
listOst2 = listOst.copy()
listPower = [1100, 1160, 1100, 1000, 1050, 1000, 1150, 1150, 1160, 1150]  # производительность
listOptTime = []
listOptPartia = []

for i in range(len(listQ)):
    x = ((2 * listQ[i] * C1) / C2) ** (1 / 2)
    x = round(x)
    listX.append(x)

for i in range(len(listX)):
    power = listX[i] / listPower[i]
    listOptTime.append(power)

for i in range(len(listX)):
    newPartia = math.ceil(listOptTime[i]) * listPower[i]
    listOptPartia.append(newPartia)
    listOptTime[i] = math.ceil(listOptTime[i])

#listOstProverka = []
ostatok = 0
# listProuzvodstvo = []
# listTime = []
# timeSdelat = 0
# nadoSdelat = 0

listOchered = []
newList = []

for i in range(30):  # stroka
    for j in range(0, 10):  # stolbec\
        ostatok = listOst[j] - a[j][i]
        listOst[j] = ostatok
        if ostatok < 0:
            newList.append(j)

for i in newList:  # выстраиваем очередб
    if i not in listOchered:
        listOchered.append(i)

hour1 = 1
hour2 = 1
line1 = []
line2 = []
listProverit1 = []
listProverit2 = []

print("Лист очереди ----", listOchered)

for i in listOchered:
   #print(listOchered.index(i), "and", len(listOchered))
    if listOst1[i] < listQ[i]:

        if (len(listOchered) - 10) == 0:
            listOst1[i] += listOptPartia[i]
            hour1 += listOptTime[i]
            hour1 += 1  # переналадка
            line1.append(hour1)
            listProverit1.append(i)
            listOchered.append(i)

        else:
            if (hour1 - hour2) >= 0:
                listOst1[i] += listOptPartia[i]
                hour2 += listOptTime[i]
                hour2 += 1  # переналадка
                line2.append(hour2)
                listProverit2.append(i)
                listOchered.append(i)
            else:
                listOst1[i] += listOptPartia[i]
                hour1 += listOptTime[i]
                hour1 += 1  # переналадка
                line1.append(hour1)
                listProverit1.append(i)
                listOchered.append(i)

    else:
        continue

listZatrat = []
listOst3 = []
zatrat = 0
count = 0
count2 = 0
sum1 = 0
print(line1)

for hour in range(1, 720):

    if count < len(line1) and count2 < len(line2):

        listOst2[listProverit1[count]] += listPower[listProverit1[count]]
        listOst2[listProverit2[count2]] += listPower[listProverit2[count2]]
        print(hour, 'час ---- на складе', listOst2[listProverit1[count]], "кг товара", listProverit1[count])
        print("Остаток на складе по всей продукции --->", listOst2)

        if hour == line1[count] and hour != line1[len(line1) - 1]  :
            count += 1
            #print('Индекс товара на линии 1 ==== ', count)

        if hour == line2[count2] - 1:
            count2 += 1
            #print('Индекс товара на линии 2 ==== ', count2)

        if hour != 0 and hour % 24 == 0:
            day = hour//24
            print("день -----> ",day)
            for i in range(day, day + 1):
                for j in range(0, 10):
                    if listOst2[j] >= a[j][i]:
                        listOst3.append(listOst2[j] - a[j][i])
                    else:
                        for x in range(0, 10):
                            sum1 += a[x][i]
                        listOst3.clear()
                        break
                if len(listOst3) != 0:
                    listOst2 = listOst3.copy()
                    listOst3.clear()

                zatrat = zatrat + sum1 * 20 * 0.05
                zatrat = zatrat + (sum(listOst2) / 1000) * 15

        print(zatrat)

    else:
        break

zatrat = zatrat + (len(line1) - 1) * 3000 + len(line2) * 3000

print("Оптимальная партия ---> ", listX)
print("Оптимальное время ---> ", listOptTime)
print("Оптимальная партия за округленное в большую сторону время ---> ", listOptPartia)
#print("Остатки по товарам --- когда изготовили", i, "----", listOst1)
#ПЕРЕНАЛАДКА
print("Очередь изготовления продукции на 1 линии --", listProverit1)
print("Часы производства с учетом переналадки", line1)
print("Очередь изготовления продукции на 2 линии --", listProverit2)
print("Часы производства с учетом переналадки", line2)
print("Остатки по товарам в соответствии с оптимальным производством ---", listOst1)

print("Общие затраты =", zatrat)



