total_days = 377
total_hours = total_days * 24
work_rate = (4482 + 2596 * 2) / total_hours
tip_rate = 5066 / total_hours


ShackUpgrades = {}

BeachUpgrades = {
    'paint'      : (380250   , 10),
    # 'furniture'  : (735000   , 20),
    'bathrooms'  : (980000   , 25),
    # 'billboard'  : (900000   , 35),
    # 'appliances' : (1153200  , 20 * work_rate),
    # 'tipjar'     : (648000   , 50 * tip_rate),

    'decals'     : (2000000  , 50),
    # 'wheels'     : (1912500  , 100),
    # 'mixers'     : (5625000  , 250),
    # 'server'     : (0000000  , 400),
    'freezer'    : (36750000 , 750),

    # 'shells'     : (160000   , 5),
    'umbrella'   : (380250   , 10),
    'leis'       : (1176000  , 30),
    # 'tanks'      : (540000   , 125),
    # 'fountain'   : (13500000 , 500),

    'apprentice' : (380250   , 10),
    'cook'       : (777600   , 20),
    'advertiser' : (762300   , 20),
    'greeter'    : (924800   , 25),
    'sous'       : (1555200  , 40),
    'head'       : (2450000  , 65),
    'executive'  : (5780000  , 150),

    'newspaper'  : (381150   , 10),
    'radio'      : (751400   , 20),
    'email'      : (1156000  , 30),
    'internet'   : (1922000  , 50),
    # 'tv'         : (2200000  , 160),
    # 'blimp'      : (4000000  , 200),
}

CityUpgrades = {
    'paint'      : (240250   , 10),
    'furniture'  : (504600   , 20),
    'bathrooms'  : (627200   , 25),
    'billboard'  : (841000   , 35),
    'appliances' : (529200   , 20 * work_rate),
    # 'tipjar'     : (612500   , 50 * tip_rate),

    'buns'       : (1267500  , 50),
    'condiments' : (2560000  , 100),
    'beverages'  : (7200000  , 275),
    'coolers'    : (12250000 , 450),
    'grill'      : (25000000 , 800),

    'banner'     : (126150   , 5),
    'sign'       : (242000   , 10),
    'glass'      : (722500   , 30),
    'artwork'    : (3600000  , 150),
    'chandelier' : (20000000 , 500),

    'apprentice' : (240250   , 10),
    'cook'       : (504600   , 20),
    'advertiser' : (510300   , 20),
    'greeter'    : (627200   , 25),
    'sous'       : (1009200  , 40),
    'head'       : (1568000  , 65),
    'executive'  : (3645000  , 150),

    'newspaper'  : (255150   , 10),
    'radio'      : (509600   , 20),
    'email'      : (729000   , 30),
    'internet'   : (1250000  , 50),
    'tv'         : (4009500  , 160),
    'blimp'      : (6250000  , 200),
}

FranchiseUpgrades = {
    'drivethru' : (100000 , 1000),
    'customer'  : (62500  , .1 * tip_rate * 14000),
    'food'      : (62500  , .1 * work_rate * 14000),
    'overtime'  : (144000 , .1 * work_rate * 14000 * 2),
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