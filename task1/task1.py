import sys


#load file in cmd args
if __name__ == '__main__':
    try:
        num = int(sys.argv[1])
        m = int(sys.argv[2])
    except:
        print("Opps. Open cmd: >python task1.py 5 4")
        exit()


main_list = []
slice = []
Flag = True
while Flag :
    for i in range(1, num+1):
        if len(slice) == m:
            main_list.append(slice)
            Flag = slice[-1] != 1
            #print(slice, (i))
            if Flag!=1:
                break
            slice_end = slice[-1]
            slice = []
            slice.append(slice_end)
        if len(slice) != m:
            slice.append(i)

[print(i[0], end = '') for i in main_list ]