total_days = 377
total_hours = total_days * 24
work_rate = (4482 + 2596 * 2) / total_hours
tip_rate = 5066 / total_hours


ShackUpgrades = {}

BeachUpgrades = {
    # 'decals'     : (3125000  , 50),
    # 'wheels'     : (1912500  , 100),
    # 'mixers'     : (5625000  , 250),
    # 'server'     : (0000000  , 400),
    'freezer'    : (48000000 , 750),
}

CityUpgrades = {
    'buns'       : (2707500  , 50),
    'condiments' : (5290000  , 100),
    'beverages'  : (14450000 , 275),
    'coolers'    : (25000000 , 450),
    'grill'      : (49000000 , 800),

    'banner'     : (264600   , 5),
    'sign'       : (544500   , 10),
    'glass'      : (1562500  , 30),
    # 'artwork'    : (6400000  , 150),
    'chandelier' : (45000000 , 500),

    # 'apprentice' : (506250   , 10),
    'cook'       : (1058400  , 20),
    'advertiser' : (1064700  , 20),
    'greeter'    : (1344800  , 25),
    'sous'       : (2116800  , 40),
    # 'head'       : (3200000  , 65),
    'executive'  : (8000000  , 150),

    'newspaper'  : (532350   , 10),
    'radio'      : (1040000  , 20),
    'email'      : (1600000  , 30),
    'internet'   : (2592000  , 50),
    # 'tv'         : (4950000  , 160),
    # 'blimp'      : (6250000  , 200),
}

FranchiseUpgrades = {
    'drivethru' : (100000 , 1000),
    'customer'  : (62500  , .1 * tip_rate * 14000),
    'food'      : (122500 , .1 * work_rate * 14000),
    'overtime'  : (196000 , .1 * work_rate * 14000 * 2),
    'marketing' : (45000  , 300),
    'hq'        : (40000  , 500),
}


def best(upgrades):
    ret = max(upgrades, key=lambda x: upgrades[x][1] / upgrades[x][0])
    return ret, upgrades[ret][0]


if __name__ == '__main__':
    # print(best(ShackUpgrades))
    print('beach', *best(BeachUpgrades))
    print('city', *best(CityUpgrades))
    print('f', *best(FranchiseUpgrades))