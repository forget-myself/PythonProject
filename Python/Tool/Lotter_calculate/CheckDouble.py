import xlrd


def get_prize_level(numbers):
    print(1)


def check_double():
    print(1)


if __name__ == '__main__':
    first_prize = [0,10000000]
    second_prize =[0,334715]
    third_prize =[0,10000]
    four_prize=[0,3000]
    five_prize =[0,300]
    six_prize =[0,200]
    seven_prize =[0,100]
    eight_prize=[0,15]
    night_prize=[0,5]


    write_numbers_front = [4, 11, 19, 25, 32]
    write_numbers_back = [1, 2]

    front= set(write_numbers_front)
    back = set(write_numbers_back)

    readbook = xlrd.open_workbook(r'data.xls')
    sheet = readbook.sheet_by_index(0)  # 索引的方式，从0开始
    start_index = 0
    all_rows = sheet.nrows
    temp_arr = [0]*all_rows
    a=sheet.cell(0,1)
   # print(sheet.cell(0,1),type(a))
    while start_index < all_rows:
        arr_front = [0]*5
        arr_back = [0]*2
        front_index=0
        while front_index <5:
            arr_front[front_index]= int(sheet.cell(start_index,front_index).value)
            front_index+=1
        front_index=0
        while front_index <2:
            arr_back[front_index]= int(sheet.cell(start_index,front_index+5).value)
            front_index+=1
        start_index+=1
        #print(arr_front)
        #分别比较和号码相同的个数
        front_common = front.intersection(set(arr_front)).__len__()
        back_common = back.intersection(set(arr_back)).__len__()
       # print(front_common,back_common)
        if(front_common == 5 and back_common==2):
            print('no.1',start_index)
            first_prize[0]+=1
        elif(front_common==5 and back ==1):
            print('no.2', start_index)
            second_prize[0] +=1
        elif (front_common == 5 and back == 0):
            print('no.3',start_index)
            third_prize[0]+=1
        elif (front_common == 4 and back == 2):
            print('no.4',start_index)
            four_prize[0]+=1
        elif ((front_common == 4 and back == 1)):
            print('no.5',start_index)
            five_prize[0]+=1
        elif ((front_common == 3 and back == 2)):
            print('no.6', start_index)
            six_prize[0] += 1
        elif ((front_common == 4 and back == 0)):
            print('no.7',start_index)
            seven_prize[0]+=1
        elif ((front_common == 3 and back == 1) or(front_common == 2 and back == 2)):
            print('no.7',start_index)
            eight_prize[0]+=1
        elif ((front_common == 3 and back == 0) or ( front_common ==1 and back == 2) or
                (front_common ==2 and back == 1) or (back == 2) ):
            print('no.6',start_index)
            six_prize[0]+=1

        total = first_prize[0]*first_prize[1]+second_prize[0]*second_prize[1]+third_prize[0]*third_prize[1]
        +four_prize[0]*four_prize[1]+five_prize[0]*five_prize[1]+six_prize[0]*six_prize[1]
    print('总计金额 :',total)






