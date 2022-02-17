import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', nargs='?')
    return parser
if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

    if namespace.name:
        my_file = open(f"{namespace.name}")
        nums = [int(i) for i in my_file]
    else:
        print("Opps no file. Open cmd: task4.py input4.txt")

mean = round(sum(nums)/len(nums))
def equal_list(lis):
    for i in range(1,len(lis)):
        if lis[0] != lis[i]:
            return True
    else:
        return False

count = 0
while equal_list(nums):
    for index in range(len(nums)):
        if mean > nums[index]:
            nums[index] = nums[index] + 1
            count += 1
        elif mean < nums[index]:
            nums[index] = nums[index] - 1
            count += 1
print(f'Минимальное количество ходов: {count}')
