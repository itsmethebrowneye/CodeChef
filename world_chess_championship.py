t = int(input())

while t > 0:
    x = int(input())
    games = list(input())
    carlson_points = 0
    chef_points = 0
    won_prize = 60
    lost_prize = 55
    for elem in games:
        total_prize = 0
        if elem == 'C':
            carlson_points += 2
        elif elem == 'N':
            chef_points += 2
        else:
            carlson_points += 1
            chef_points += 1

    if carlson_points > chef_points:
        total_prize = won_prize * x
    elif carlson_points < chef_points:
        total_prize = 40 * x
    else:
        total_prize = lost_prize * x

    print(total_prize)
    t -= 1
