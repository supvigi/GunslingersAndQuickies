def where_bullets(unlucky_enemy):
    """empties the firearm of an unlucky enemy before start"""
    unlucky_enemy.ammo = 0
    return NotImplemented


def dexterity_and_luck(accuracy_usual) -> int:
    """Reduces enemy accuracy to 60% or keeps it as is if it"s less than 50"""
    if accuracy_usual < 60:
        return accuracy_usual
    # else
    return 60


characters = [
    {
        "char": {"name": "The Man With No Name",
                 "perk": lambda x: x,
                 "desc": "Developer Character with impressive stats, "
                         "however with a handful of luck you might still stand "
                         "after a fight with this legend of the West\n"
                         "Where'd all the bullets go?: In a fight of 3 and more,\n"
                         "one of your enemies realises that their firearm is completely unloaded, "
                         "right before start (and you know who)"},
        "firearm": {"model": "Colt 1851 Navy Cartridge Conversion TMWNN VERSION",
                    "reload_type": "OnePerLoad",
                    "draw": 0.2,
                    "fire": 0.3,
                    "reload": 0.5,
                    "magsize": 6,
                    "accuracy": 95}
    },
    {
        "char": {"name": "Dexter Lucky",
                 "perk": dexterity_and_luck,
                 "desc": "Feeling lucky, huh?\n"
                         "Recommended only against the developer character, The Man With No Name\n"
                         "Dexterity and bit of luck: Reduces enemy accuracy to 60% "
                         "or keeps it as is if it is less than 60"},
        "firearm": {"model": "1868 Double-Barreled Sawed-Off Shotgun",
                    "reload_type": "OnePerLoad",
                    "draw": 0.5,
                    "fire": 0.5,
                    "reload": 0.5,
                    "magsize": 2,
                    "accuracy": 40}
    }
]

char_list = ["The Man With No Name", "Dexter Lucky"]
QUICKDRAW_PERKS_LIST = tuple()
DODGY_PERKS_LIST = (characters[1]["char"]["perk"].__name__,)
