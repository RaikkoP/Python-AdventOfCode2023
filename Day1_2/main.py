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
    my_dict = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'zero': 0,
    }
    for key in my_dict.keys():
        if key in temp:
            return int(my_dict.get(key))


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
