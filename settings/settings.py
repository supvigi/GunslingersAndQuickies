QUICKDRAW_PERKS_LIST = ('tmwnn_perk',)
DODGY_PERKS_LIST = ('dexter_perk',)


def quickdraw(draw_time_usual) -> int:
    """Reduces drawing time by 0.2 seconds"""
    return draw_time_usual - 0.2


def dexterity_and_luck(accuracy_usual) -> int:
    """Reduces enemy accuracy to 60% or keeps it as is if it's less than 50"""
    if accuracy_usual < 60:
        return accuracy_usual
    # else
    return 60


characters = [
    {
        'char': {'name': 'The Man With No Name',
                 'perk': quickdraw,
                 'desc': 'Developer Character with impressive stats, '
                         'however with a handful of luck you might still stand '
                         'after a fight with this legend of the West\n'
                         'Quickdraw: Reduces drawing time by 0.2 seconds'},
        'firearm': {'model': 'Colt 1851 Navy Cartridge Conversion',
                    'reload_type': 'OnePerLoad',
                    'draw': 0.4,
                    'shoot': 0.3,
                    'reload': 0.5,
                    'ammo': 6,
                    'accuracy': 95}
    },
    {
        'char': {'name': 'Dexter Lucky',
                 'perk': dexterity_and_luck,
                 'desc': 'Feeling lucky, huh? '
                         'Recommended only against the developer character, The Man With No Name\n'
                         'Dexterity and bit of luck: Reduces enemy accuracy to 60% '
                         'or keeps it as is if it is less than 60'},
        'firearm': {'model': '1868 Double-Barreled Sawed-Off',
                    'reload_type': 'OnePerLoad',
                    'draw': 0.5,
                    'shoot': 0.6,
                    'reload': 0.5,
                    'ammo': 2,
                    'accuracy': 40}
    }
]

char_list = ['The Man With No Name', 'Dexter Lucky']
