games = []

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
        red_cubes = 0
        green_cubes = 0
        blue_cubes = 0
        temp_array = game.split(" ")
        for section in temp_array:
            temp_section = section.replace(',', '').replace(';', '').replace('\n', '')
            match temp_section:
                case 'red':
                    if int(last_section) >= red_cubes:
                        red_cubes = int(last_section)
                case 'green':
                    if int(last_section) >= green_cubes:
                        green_cubes = int(last_section)
                case 'blue':
                    if int(last_section) >= blue_cubes:
                        blue_cubes = int(last_section)
            last_section = temp_section
        total += red_cubes * green_cubes * blue_cubes
    return total


print(squid_games())




