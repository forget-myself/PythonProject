import random
import datetime
from xlwt import *

def GetDouble():
    curr = 0
    number = [0] * 5
    number2 = [0] * 2

    while curr < 5:
        a = random.randint(1, 35)
        hasCommon = 1
        for item in number:
            if (item == a):
                hasCommon = 0

        if (hasCommon != 0):
            number[curr] = a
            curr += 1
    number= sorted(number)
    curr = 0
    while curr < 2:
        a = random.randint(1, 12)
        hasCommon = 1
        for item in number2:
            if (item == a):
                hasCommon = 0

        if (hasCommon != 0):
            number2[curr] = a
            curr += 1
    number2= sorted(number2)
    return number+number2



def GetSingle() :
    curr = 0
    number = [0] * 6
    number2 = [0] * 1

    while curr < 6:
        a = random.randint(1, 32)
        hasCommon = 1
        for item in number:
            if (item == a):
                hasCommon = 0

        if (hasCommon != 0):
            number[curr] = a
            curr += 1
    sorted(number)
    curr = 0
    while curr < 1:
        a = random.randint(1, 16)
        hasCommon = 1
        for item in number2:
            if (item == a):
                hasCommon = 0

        if (hasCommon != 0):
            number2[curr] = a
            curr += 1
    sorted(number2)
    return  number+number2



def getweekday():
    weekday = datetime.datetime.now().weekday()
    if (weekday == 0 or weekday == 2 or weekday == 5):
        return 2
    if (weekday == 1 or weekday == 3 or weekday == 6):
        return  1
    if(weekday == 4):
        return 0

def GetDefault():
    weekday = getweekday()
    if (weekday == 2):
        GetDouble(5,2)
    if(weekday == 1):
        GetSingle(6,1)

def GetCurrInput(a,b):
    weekday = getweekday()
    if (weekday == 2):
        GetDouble(a,b)
    if(weekday == 1):
        GetSingle(a,b)

def loop_number_excel(weekday,count):
    index=0
    arr=[[] for i in range(7)]*count
    file = Workbook(encoding= 'utf-8')
    table = file.add_sheet('data')

    if(weekday==2):
        while index < count:
            abb = GetDouble()
            #print(abb)
            arr[index] = GetDouble()
            index += 1
        index = 0
        for item in arr:
            index2 = 0
            for item2 in item:
                table.write(index, index2, item2)
                index2 += 1
            index += 1
        file.save('data.xls')

    if (weekday == 1):
        while index < count:
            arr[index] = GetSingle()
            index += 1
        index=0
        for item in arr:
            index2 =0
            for item2  in item:
                table.write(index,index2,item2)
                index2+=1
            index+=1
        file.save('data.xls')


if __name__ == '__main__':
    #count = input('输入数量 ')
    starttime = datetime.datetime.now()
    count = 10000
    #weekday = getweekday()
    loop_number_excel(2, int(count))
    endtime = datetime.datetime.now()
    print((endtime - starttime).seconds)





