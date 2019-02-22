import xlrd

if __name__ == '__main__':
    first_prize = [0, 6275977]
    second_prize = [0, 75299]
    third_prize = [0, 3000]
    four_prize = [0, 200]
    five_prize = [0, 10]
    six_prize = [0, 5]
    write_numbers_front = [2, 12, 13, 23, 27,28]
    write_numbers_back = [12]
    front= set(write_numbers_front)
    back = set(write_numbers_back)
    readbook = xlrd.open_workbook(r'data.xls')
    sheet = readbook.sheet_by_index(0)  # 索引的方式，从0开始
    start_index = 0
    all_rows = sheet.nrows
    temp_arr = [0]*all_rows
    total =0
    while start_index < all_rows:
        arr_front = [0]*6
        arr_back = [0]*1
        front_index=0
        while front_index <6:
            arr_front[front_index]= int(sheet.cell(start_index,front_index).value)
            front_index+=1
        front_index=0
        while front_index <1:
            arr_back[front_index]= int(sheet.cell(start_index,front_index+6).value)
            front_index+=1
        start_index+=1
        #分别比较和号码相同的个数
        front_common = front.intersection(set(arr_front)).__len__()
        back_common = back.intersection(set(arr_back)).__len__()
       # print(front_common,back_common)
        if(front_common == 6 and back_common==1):
            print('no.1',start_index)
            first_prize[0]+=1
        elif(front_common==6 and back_common ==0):
            print('no.2', start_index)
            second_prize[0] +=1
        elif (front_common == 5 and back_common == 1):
            print('no.3',start_index)
            third_prize[0]+=1
        elif (front_common == 5 and back_common == 0):
            print('no.4',start_index)
            four_prize[0]+=1
        elif ((front_common == 4 and back_common == 1)):
            print('no.4',start_index)
            four_prize[0]+=1
        elif ((front_common == 4 and back_common == 0) or(front_common == 3 and back_common == 1)):
            five_prize[0]+=1
        elif ( (back_common == 1) ):
            #print('no.6',start_index)
            six_prize[0]+=1

    total = first_prize[0] * first_prize[1] + second_prize[0] * second_prize[1] + third_prize[0] * third_prize[1] \
        + four_prize[0] * four_prize[1]+five_prize[0]*five_prize[1]+six_prize[0]*six_prize[1]
    print('总计金额 :',total)
    print('1 有  .', first_prize[0])
    print('2 有  .', second_prize[0])
    print('3 有  .', third_prize[0])
    print('4 有  .', four_prize[0])
    print('5 有  .', five_prize[0])
    print('6 有  .', six_prize[0])




