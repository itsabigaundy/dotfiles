total_days = 298
total_hours = total_days * 24
work_rate = 3623 / total_hours
tip_rate = 4119 / total_hours


ShackUpgrades = {
    # 'paint'      : (306250  , 10),
    # 'furniture'  : (345600  , 20),
    # 'bathrooms'  : (720000  , 25),
    # 'billboard'  : (576000  , 35),
    # 'appliances' : (1153200 , 20 * work_rate),
    # 'tipjar'     : (648000  , 50 * tip_rate),

    # 'register'   : (2000000 , 50),
    # 'assistant'  : (810000  , 100),
    # 'driver'     : (2025000 , 250),
    # 'kitchen'    : (3600000 , 400),
    # 'engine'     : (9000000 , 1000),

    # 'flowers'    : (160000  , 5),
    # 'ornaments'  : (80000   , 10),
    # 'lights'     : (900000  , 30),
    # 'mural'      : (540000  , 100),
    # 'statue'     : (4500000 , 400),

    # 'apprentice' : (306250  , 10),
    # 'cook'       : (735000  , 20),
    # 'advertiser' : (809200  , 20),
    # 'greeter'    : (980000  , 25),
    # 'sous'       : (1470000 , 40),
    # 'head'       : (512000  , 65),
    # 'executive'  : (5780000 , 150),

    # 'newspaper'  : (404600  , 10),
    # 'radio'      : (585000  , 20),
    # 'email'      : (900000  , 30),
    # 'internet'   : (2048000 , 50),
    # 'tv'         : (1237500 , 160),
    # 'blimp'      : (2250000 , 200),
}

BeachUpgrades = {
    'paint'      : (272250   , 10),
    'furniture'  : (576600   , 20),
    'bathrooms'  : (720000   , 25),
    # 'billboard'  : (900000   , 35),
    # 'appliances' : (1153200  , 20 * work_rate),
    # 'tipjar'     : (648000   , 50 * tip_rate),

    'decals'     : (1445000  , 50),
    # 'wheels'     : (1912500  , 100),
    # 'mixers'     : (5625000  , 250),
    # 'server'     : (0000000  , 400),
    'freezer'    : (27000000 , 750),

    'shells'     : (136900   , 5),
    'umbrella'   : (272250   , 10),
    'leis'       : (864000   , 30),
    # 'tanks'      : (540000   , 125),
    # 'fountain'   : (13500000 , 500),

    'apprentice' : (272250   , 10),
    'cook'       : (576600   , 20),
    'advertiser' : (548800   , 20),
    'greeter'    : (720000   , 25),
    'sous'       : (1153200  , 40),
    'head'       : (1922000  , 65),
    'executive'  : (4205000  , 150),

    'newspaper'  : (274400   , 10),
    'radio'      : (546650   , 20),
    'email'      : (841000   , 30),
    'internet'   : (1352000  , 50),
    # 'tv'         : (2200000  , 160),
    # 'blimp'      : (4000000  , 200),
}

CityUpgrades = {
    'paint'      : (64000   , 10),
    'furniture'  : (135000  , 20),
    'bathrooms'  : (156800  , 25),
    'billboard'  : (225000  , 35),
    'appliances' : (97200   , 20 * work_rate),
    'tipjar'     : (180500  , 50 * tip_rate),

    # 'decals'     : (1445000  , 50),
    # 'wheels'     : (1912500  , 100),
    # 'mixers'     : (5625000  , 250),
    # 'server'     : (0000000  , 400),
    # 'freezer'    : (27000000 , 750),

    'banner'     : (33750   , 5),
    'sign'       : (60500   , 10),
    'glass'      : (202500  , 30),
    'artwork'    : (1600000 , 150),
    'chandelier' : (5000000 , 500),

    'apprentice' : (64000   , 10),
    'cook'       : (135000  , 20),
    'advertiser' : (137200  , 20),
    'greeter'    : (156800  , 25),
    'sous'       : (270000  , 40),
    'head'       : (392000  , 65),
    'executive'  : (980000  , 150),

    'newspaper'  : (68600   , 10),
    'radio'      : (127400  , 20),
    'email'      : (196000  , 30),
    'internet'   : (338000  , 50),
    # 'tv'         : (550000  , 160),
    'blimp'      : (2250000 , 200),
}

FranchiseUpgrades = {
    'drivethru' : (100000 , 1000),
    'customer'  : (22500  , .1 * tip_rate * 14000),
    'food'      : (22500  , .1 * work_rate * 14000),
    'overtime'  : (36000  , .1 * work_rate * 14000 * 2),
    'marketing' : (45000  , 300),
    'hq'        : (40000  , 500),
}


def best(upgrades):
    return max(upgrades, key=lambda x: upgrades[x][1] / upgrades[x][0])


if __name__ == '__main__':
    # print(best(ShackUpgrades))
    print('beach', best(BeachUpgrades))
    print('city', best(CityUpgrades))
    print('f', best(FranchiseUpgrades))