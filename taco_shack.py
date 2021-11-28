total_days = 377
total_hours = total_days * 24
work_rate = (4482 + 2596 * 2) / total_hours
tip_rate = 5066 / total_hours


ShackUpgrades = {}

BeachUpgrades = {
    'decals'     : (2420000  , 50),
    # 'wheels'     : (1912500  , 100),
    # 'mixers'     : (5625000  , 250),
    # 'server'     : (0000000  , 400),
    'freezer'    : (36750000 , 750),

    # 'shells'     : (160000   , 5),
    # 'umbrella'   : (400000   , 10),
    'leis'       : (1441500  , 30),
    # 'tanks'      : (540000   , 125),
    # 'fountain'   : (13500000 , 500),

    # 'apprentice' : (400000   , 10),
    'cook'       : (960000   , 20),
    'advertiser' : (958300   , 20),
    'greeter'    : (1155200  , 25),
    'sous'       : (1825200  , 40),
    # 'head'       : (2450000  , 65),
    'executive'  : (6845000  , 150),

    'newspaper'  : (479150   , 10),
    # 'radio'      : (796250   , 20),
    # 'email'      : (1225000  , 30),
    'internet'   : (2312000  , 50),
    # 'tv'         : (2200000  , 160),
    # 'blimp'      : (4000000  , 200),
}

CityUpgrades = {
    'paint'      : (361000   , 10),
    'furniture'  : (735000   , 20),
    'bathrooms'  : (871200   , 25),
    'billboard'  : (1225000  , 35),
    'appliances' : (750000   , 20 * work_rate),
    # 'tipjar'     : (612500   , 50 * tip_rate),

    'buns'       : (1920000  , 50),
    'condiments' : (3610000  , 100),
    'beverages'  : (9800000  , 275),
    'coolers'    : (16000000 , 450),
    'grill'      : (36000000 , 800),

    'banner'     : (183750   , 5),
    'sign'       : (364500   , 10),
    'glass'      : (1102500  , 30),
    'artwork'    : (6400000  , 150),
    'chandelier' : (20000000 , 500),

    'apprentice' : (361000   , 10),
    'cook'       : (735000   , 20),
    'advertiser' : (716800   , 20),
    'greeter'    : (871200   , 25),
    'sous'       : (1387200  , 40),
    'head'       : (2312000  , 65),
    'executive'  : (5445000  , 150),

    'newspaper'  : (358400   , 10),
    'radio'      : (707850   , 20),
    'email'      : (1089000  , 30),
    'internet'   : (1800000  , 50),
    # 'tv'         : (4950000  , 160),
    # 'blimp'      : (6250000  , 200),
}

FranchiseUpgrades = {
    'drivethru' : (100000 , 1000),
    'customer'  : (62500  , .1 * tip_rate * 14000),
    'food'      : (90000  , .1 * work_rate * 14000),
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