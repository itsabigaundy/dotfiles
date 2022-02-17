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
    'paint'      : (484000   , 10),
    # 'furniture'  : (960000   , 20),
    'bathrooms'  : (1216800  , 25),
    # 'billboard'  : (1600000  , 35),
    'appliances' : (1080000  , 20 * work_rate),
    # 'tipjar'     : (612500   , 50 * tip_rate),

    'buns'       : (2430000  , 50),
    'condiments' : (4840000  , 100),
    'beverages'  : (14450000 , 275),
    'coolers'    : (25000000 , 450),
    'grill'      : (49000000 , 800),

    'banner'     : (252150   , 5),
    'sign'       : (512000   , 10),
    'glass'      : (1562500  , 30),
    # 'artwork'    : (6400000  , 150),
    'chandelier' : (45000000 , 500),

    'apprentice' : (484000   , 10),
    'cook'       : (1008600  , 20),
    'advertiser' : (1010800  , 20),
    'greeter'    : (1216800  , 25),
    'sous'       : (2017200  , 40),
    'head'       : (3200000  , 65),
    'executive'  : (7220000  , 150),

    'newspaper'  : (505400   , 10),
    'radio'      : (988650   , 20),
    'email'      : (1444000  , 30),
    'internet'   : (2450000  , 50),
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