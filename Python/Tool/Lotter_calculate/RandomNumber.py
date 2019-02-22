import random
import datetime

def GetDouble(front,back):
    curr = 0
    number = [0] * front
    number2 = [0] * back

    while curr < front:
        a = random.randint(1, 35)
        hasCommon = 1
        for item in number:
            if (item == a):
                hasCommon = 0

        if (hasCommon != 0):
            number[curr] = a
            curr += 1

    curr = 0
    while curr < back:
        a = random.randint(1, 12)
        hasCommon = 1
        for item in number2:
            if (item == a):
                hasCommon = 0

        if (hasCommon != 0):
            number2[curr] = a
            curr += 1

    strstr = ""
    for item in number:
        strstr += (str(item) + "  ")
    print(strstr)

    strstr = ""
    for item in number2:
        strstr += (str(item) + "  ")
    print(strstr)


def GetSingle(front,back) :
    curr = 0
    number = [0] * front
    number2 = [0] * back

    while curr < front:
        a = random.randint(1, 32)
        hasCommon = 1
        for item in number:
            if (item == a):
                hasCommon = 0

        if (hasCommon != 0):
            number[curr] = a
            curr += 1

    curr = 0
    while curr < back:
        a = random.randint(1, 16)
        hasCommon = 1
        for item in number2:
            if (item == a):
                hasCommon = 0

        if (hasCommon != 0):
            number2[curr] = a
            curr += 1

    strstr = ""
    for item in number:
        strstr += (str(item) + "  ")
    print(strstr)

    strstr = ""
    for item in number2:
        strstr += (str(item) + "  ")
    print(strstr)


def getweekday():
    weekday = datetime.datetime.now().weekday()
    print(weekday)
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

if __name__ == '__main__':
    front = input('输入号码 ')
    print(front,type(front))
    if(front == '0'):
        GetDefault()
    else:
        back = input('输入后区 ')
        print(back)
        GetCurrInput(int(front),int(back) )




