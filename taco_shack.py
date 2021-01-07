import numpy as np


def Upgrades():
    return {
        'paint'      : (90250  , 10),
        'furniture'  : (153600 , 20),
        #'appliances' : (1153200, 20 * 3 * 10),
        'bathrooms'  : (204800 , 25),
        'billboard'  : (289000 , 35),
        #'tipjar'     : (648000 , 50 * 12),
        'flowers'    : (40000  , 5),
        'ornaments'  : (80000  , 10),
        'lights'     : (256000 , 30),
        #'mural'      : (540000 , 100),
        'statue'     : (4500000, 400),
        'apprentice' : (81000  , 10),
        'cook'       : (153600 , 20),
        'sous'       : (307200 , 40),
        'head'       : (512000 , 65),
        'executive'  : (1280000, 150),
        'advertiser' : (157500 , 20),
        'greeter'    : (204800 , 25),
        'newspaper'  : (78750  , 10),
        'radio'      : (166400 , 20),
        'email'      : (225000 , 30),
        'internet'   : (392000 , 50),
        'tv'         : (1237500, 160),
        'blimp'      : (2250000, 200),
        'register'   : (405000 , 50),
        'assistant'  : (810000 , 100),
        'driver'     : (2025000, 250),
        # 'kitchen'    : (3600000, 400),
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