total_days = 377
total_hours = total_days * 24
work_rate = (4482 + 2596 * 2) / total_hours
tip_rate = 5066 / total_hours


ShackUpgrades = {}

BeachUpgrades = {
    'decals'     : (2205000  , 50),
    # 'wheels'     : (1912500  , 100),
    # 'mixers'     : (5625000  , 250),
    # 'server'     : (0000000  , 400),
    'freezer'    : (36750000 , 750),

    # 'shells'     : (160000   , 5),
    # 'umbrella'   : (400000   , 10),
    'leis'       : (1350000  , 30),
    # 'tanks'      : (540000   , 125),
    # 'fountain'   : (13500000 , 500),

    # 'apprentice' : (400000   , 10),
    'cook'       : (866400   , 20),
    'advertiser' : (907200   , 20),
    'greeter'    : (1095200  , 25),
    'sous'       : (1732800  , 40),
    # 'head'       : (2450000  , 65),
    'executive'  : (6480000  , 150),

    'newspaper'  : (453600   , 10),
    # 'radio'      : (796250   , 20),
    # 'email'      : (1225000  , 30),
    'internet'   : (2178000  , 50),
    # 'tv'         : (2200000  , 160),
    # 'blimp'      : (4000000  , 200),
}

CityUpgrades = {
    'paint'      : (324000   , 10),
    'furniture'  : (653400   , 20),
    'bathrooms'  : (819200   , 25),
    'billboard'  : (1156000  , 35),
    'appliances' : (691200   , 20 * work_rate),
    # 'tipjar'     : (612500   , 50 * tip_rate),

    'buns'       : (1687500  , 50),
    'condiments' : (3240000  , 100),
    'beverages'  : (9800000  , 275),
    'coolers'    : (16000000 , 450),
    'grill'      : (36000000 , 800),

    'banner'     : (163350   , 5),
    'sign'       : (338000   , 10),
    'glass'      : (1000000  , 30),
    'artwork'    : (4900000  , 150),
    'chandelier' : (20000000 , 500),

    'apprentice' : (324000   , 10),
    'cook'       : (653400   , 20),
    'advertiser' : (630000   , 20),
    'greeter'    : (819200   , 25),
    'sous'       : (1306800  , 40),
    'head'       : (2048000  , 65),
    'executive'  : (4805000  , 150),

    'newspaper'  : (315000   , 10),
    'radio'      : (665600   , 20),
    'email'      : (961000   , 30),
    'internet'   : (1568000  , 50),
    # 'tv'         : (4950000  , 160),
    'blimp'      : (6250000  , 200),
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