lines = []

try:
    f = open('../day1Input.txt', 'r')
    lines = f.readlines()
except FileNotFoundError:
    print('File does not exist')
finally:
    f.close()
    print("File closed")


def number_in_letters(temp):
    my_long_array = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for num in my_long_array:
        if num in temp:
            return my_long_array.index(num)


def find_left(lines):
    left_num = 0
    __sum__ = 0
    for line in lines:
        temp = ''
        left = 0
        right = len(line) - 1
        while left <= len(line):
            if 48 <= ord(line[left]) <= 57:
                left_num = line[left]
                right_num = find_right(left, right, line)
                __sum__ += int(str(left_num) + str(right_num))
                break
            else:
                temp = temp + str(line[left])
                check_left = number_in_letters(temp)
                if not check_left:
                    left += 1
                else:
                    left_num = check_left
                    right_num = find_right(left, right, line)
                    __sum__ += int(str(left_num) + str(right_num))
                    break
    return __sum__


def find_right(left, right, line):
    temp = ''
    while right >= left:
        if 48 <= ord(line[right]) <= 57:
            return line[right]
        else:
            temp = str(line[right]) + temp
            check_right = number_in_letters(temp)
            if not check_right:
                right -= 1
            else:
                return check_right


print(find_left(lines))
