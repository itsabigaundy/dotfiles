total_days = 298
total_hours = total_days * 24
work_rate = 3623 / total_hours
tip_rate = 4119 / total_hours


ShackUpgrades = {}

BeachUpgrades = {
    'paint'      : (361000   , 10),
    'furniture'  : (693600   , 20),
    'bathrooms'  : (871200   , 25),
    # 'billboard'  : (900000   , 35),
    # 'appliances' : (1153200  , 20 * work_rate),
    # 'tipjar'     : (648000   , 50 * tip_rate),

    'decals'     : (1805000  , 50),
    # 'wheels'     : (1912500  , 100),
    # 'mixers'     : (5625000  , 250),
    # 'server'     : (0000000  , 400),
    'freezer'    : (27000000 , 750),

    # 'shells'     : (160000   , 5),
    'umbrella'   : (342250   , 10),
    'leis'       : (1093500  , 30),
    # 'tanks'      : (540000   , 125),
    # 'fountain'   : (13500000 , 500),

    'apprentice' : (342250   , 10),
    'cook'       : (693600   , 20),
    'advertiser' : (716800   , 20),
    'greeter'    : (871200   , 25),
    'sous'       : (1387200  , 40),
    'head'       : (2312000  , 65),
    'executive'  : (5120000  , 150),

    'newspaper'  : (358400   , 10),
    'radio'      : (707850   , 20),
    'email'      : (1024000  , 30),
    'internet'   : (1800000  , 50),
    # 'tv'         : (2200000  , 160),
    # 'blimp'      : (4000000  , 200),
}

CityUpgrades = {
    'paint'      : (210250   , 10),
    'furniture'  : (405600   , 20),
    'bathrooms'  : (540800   , 25),
    'billboard'  : (729000   , 35),
    'appliances' : (235200   , 20 * work_rate),
    'tipjar'     : (612500   , 50 * tip_rate),

    'buns'       : (607500   , 50),
    'condiments' : (1000000  , 100),
    'beverages'  : (3200000  , 275),
    'coolers'    : (6250000  , 450),
    'grill'      : (9000000  , 800),

    'banner'     : (101400   , 5),
    'sign'       : (220500   , 10),
    'glass'      : (640000   , 30),
    'artwork'    : (3600000  , 150),
    'chandelier' : (20000000 , 500),

    'apprentice' : (210250   , 10),
    'cook'       : (405600   , 20),
    'advertiser' : (437500   , 20),
    'greeter'    : (540800   , 25),
    'sous'       : (811200   , 40),
    'head'       : (1352000  , 65),
    'executive'  : (3125000  , 150),

    'newspaper'  : (218750   , 10),
    'radio'      : (406250   , 20),
    'email'      : (625000   , 30),
    'internet'   : (1058000  , 50),
    # 'tv'         : (2200000  , 160),
    # 'blimp'      : (4000000  , 200),
}

FranchiseUpgrades = {
    'drivethru' : (100000 , 1000),
    'customer'  : (40000  , .1 * tip_rate * 14000),
    'food'      : (40000  , .1 * work_rate * 14000),
    'overtime'  : (100000 , .1 * work_rate * 14000 * 2),
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