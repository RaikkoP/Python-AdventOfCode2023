games = []
red_cubes = 12
green_cubes = 13
blue_cubes = 14

try:
    f = open('day2Input.txt')
    games = f.readlines()
except FileNotFoundError:
    print('No file found')
finally:
    f.close()
    print('File closed')


def squid_games():
    total = 0
    for game in games:
        temp_array = game.split(" ")
        possible = False
        temp_id = temp_array[1].replace(':', '')
        for section in temp_array:
            temp_section = section.replace(',', '').replace(';', '').replace('\n', '')
            match temp_section:
                case 'red':
                    if red_cubes >= int(prev_section):
                        possible = True
                    else:
                        possible = False
                        break
                case 'green':
                    if green_cubes >= int(prev_section):
                        possible = True
                    else:
                        possible = False
                        break
                case 'blue':
                    if blue_cubes >= int(prev_section):
                        possible = True
                    else:
                        possible = False
                        break
            prev_section = section
        if possible:
            print(temp_id)
            total += int(temp_id)
    return total


print(squid_games())




