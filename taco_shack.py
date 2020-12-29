import numpy as np


def Upgrades():
    return {
        'paint'      : (64000  , 10),
        'furniture'  : (117600 , 20),
        #'appliances' : (1153200, 20 * 3 * 10),
        'bathrooms'  : (156800 , 25),
        'billboard'  : (225000 , 35),
        #'tipjar'     : (648000 , 50 * 12),
        'flowers'    : (32400  , 5),
        'ornaments'  : (64800  , 10),
        'lights'     : (196000 , 30),
        #'mural'      : (540000 , 100),
        'statue'     : (4500000, 400),
        'apprentice' : (64000  , 10),
        'cook'       : (117600 , 20),
        'sous'       : (235200 , 40),
        'head'       : (392000 , 65),
        'executive'  : (980000 , 150),
        'advertiser' : (118300 , 20),
        'greeter'    : (156800 , 25),
        'newspaper'  : (59150  , 10),
        'radio'      : (127400 , 20),
        'email'      : (196000 , 30),
        'internet'   : (338000 , 50),
        'tv'         : (929500 , 160),
        'blimp'      : (2250000, 200),
        'register'   : (320000 , 50),
        'assistant'  : (640000 , 100),
        'driver'     : (1600000, 250),
        'kitchen'    : (2500000, 400),
        'engine'     : (9000000, 1000)
    }

def best(upgrades):
    return max(upgrades, key=lambda x: upgrades[x][1] / upgrades[x][0])


def Shop():
    shop = {
        'flipper' : (2000 , 500 , 8),
        'karaoke' : (10000, 2500, 6),
        'music'   : (16000, 6000, 4),
        'airplane': (65000, 3500, 24),
        'chef'    : (3000 , 1000, 4)
    }

    print(sum(shop[x][1] * shop[x][2] - shop[x][0] for x in shop))
    return ' '.join(reversed(sorted(shop, key=lambda x: shop[x][1] - shop[x][0] / shop[x][2])))


if __name__ == '__main__':
    ups = Upgrades()
    print(best(ups))
    print(Shop())