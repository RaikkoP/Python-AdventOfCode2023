lines = []

try:
    f = open('../day1Input.txt', 'r')
    lines = f.readlines()
except FileNotFoundError:
    print('File does not exist')
finally:
    f.close()
    print("File closed")


def find_left(lines):
    left_num = 0
    __sum__ = 0
    for line in lines:
        left = 0
        right = len(line)-1
        while left <= len(line):
            if 48 <= ord(line[left]) <= 57:
                left_num = line[left]
                right_num = find_right(left, right, line)
                __sum__ += int(str(left_num) + str(right_num))
                break
            else:
                left += 1
    return __sum__


def find_right(left, right, line):
    while right >= left:
        if 48 <= ord(line[right]) <= 57:
            return line[right]
        else:
            right -= 1


print(find_left(lines))
