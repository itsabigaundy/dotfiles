total_days = 531
total_hours = total_days * 24
num_work = 5255
num_tips = 5875
num_ot = 3279
work_rate = (num_work + num_ot * 2) / total_hours
tip_rate = num_tips / total_hours


ShackUpgrades = {}

BeachUpgrades = {
    # 'decals'     : (3125000  , 50),
    # 'wheels'     : (1912500  , 100),
    # 'mixers'     : (5625000  , 250),
    # 'server'     : (0000000  , 400),
    'freezer'    : (60750000 , 750),
}

CityUpgrades = {
    'buns'       : (3000000  , 50),
    'condiments' : (5760000  , 100),
    'beverages'  : (16200000 , 275),
    'coolers'    : (30250000 , 450),
    'grill'      : (49000000 , 800),

    'banner'     : (290400   , 5),
    'sign'       : (578000   , 10),
    'glass'      : (1690000  , 30),
    # 'artwork'    : (6400000  , 150),
    'chandelier' : (45000000 , 500),

    # 'apprentice' : (506250   , 10),
    'cook'       : (1161600  , 20),
    'advertiser' : (1176700  , 20),
    'greeter'    : (1411200  , 25),
    'sous'       : (2323200  , 40),
    # 'head'       : (3200000  , 65),
    'executive'  : (8405000  , 150),

    'newspaper'  : (588350   , 10),
    # 'radio'      : (1040000  , 20),
    # 'email'      : (1600000  , 30),
    'internet'   : (2888000  , 50),
    # 'tv'         : (4950000  , 160),
    # 'blimp'      : (6250000  , 200),
}

FranchiseUpgrades = {
    'drivethru' : (100000 , 1000),
    'customer'  : (62500  , .1 * tip_rate * 14000),
    'food'      : (122500 , .1 * work_rate * 14000),
    'overtime'  : (256000 , .1 * work_rate * 14000 * 2),
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