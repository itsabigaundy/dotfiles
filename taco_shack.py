ShackUpgrades = {
    'paint'      : (289000  , 10),
    # 'furniture'  : (345600  , 20),
    # 'bathrooms'  : (720000  , 25),
    # 'billboard'  : (576000  , 35),
    # 'appliances' : (1153200 , 20 * 3 * 10),
    # 'tipjar'     : (648000  , 50 * 12),

    'register'   : (1445000 , 50),
    # 'assistant'  : (810000  , 100),
    # 'driver'     : (2025000 , 250),
    # 'kitchen'    : (3600000 , 400),
    # 'engine'     : (9000000 , 1000),

    'flowers'    : (144400  , 5),
    # 'ornaments'  : (80000   , 10),
    'lights'     : (900000  , 30),
    # 'mural'      : (540000  , 100),
    # 'statue'     : (4500000 , 400),

    'apprentice' : (289000  , 10),
    'cook'       : (576600  , 20),
    'advertiser' : (588700  , 20),
    'greeter'    : (720000  , 25),
    'sous'       : (1153200 , 40),
    # 'head'       : (512000  , 65),
    'executive'  : (4500000 , 150),

    'newspaper'  : (294350  , 10),
    'radio'      : (585000  , 20),
    'email'      : (900000  , 30),
    'internet'   : (1458000 , 50),
    # 'tv'         : (1237500 , 160),
    # 'blimp'      : (2250000 , 200),
}

BeachUpgrades = {
    'paint'      : (169000   , 10),
    'furniture'  : (345600   , 20),
    'bathrooms'  : (423200   , 25),
    'billboard'  : (576000   , 35),
    # 'appliances' : (1153200  , 20 * 3 * 10),
    # 'tipjar'     : (648000   , 50 * 12),

    'decals'     : (845000   , 50),
    'wheels'     : (1666000  , 100),
    'mixers'     : (4225000  , 250),
    # 'server'     : (0000000  , 400),
    'freezer'    : (12000000 , 750),

    'shells'     : (84100    , 5),
    'umbrella'   : (169000   , 10),
    'leis'       : (486000   , 30),
    # 'tanks'      : (540000   , 125),
    'fountain'   : (13500000 , 500),

    'apprentice' : (169000   , 10),
    'cook'       : (345600   , 20),
    'advertiser' : (338800   , 20),
    'greeter'    : (423200   , 25),
    'sous'       : (691200   , 40),
    'head'       : (1058000  , 65),
    'executive'  : (2420000  , 150),

    'newspaper'  : (169400   , 10),
    'radio'      : (343850   , 20),
    'email'      : (484000   , 30),
    'internet'   : (800000   , 50),
    'tv'         : (1408000  , 160),
    'blimp'      : (4000000  , 200),
}


def best(upgrades):
    return max(upgrades, key=lambda x: upgrades[x][1] / upgrades[x][0])


if __name__ == '__main__':
    print(best(ShackUpgrades))
    print(best(BeachUpgrades))