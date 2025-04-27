from settings.settings import QUICKDRAW_PERKS_LIST, DODGY_PERKS_LIST
from random import randint


# return True, ... - successful turn
# return False, ... - rerun turn, something wrong happened
# return None, ... - a death has occured, leading to the victory of another side
class Gunslinger:
    def __init__(self, character : dict):
        self.char = character['char']
        self.firearm = character['firearm']
        self.is_drawn = False
        self.time = 1.0
        self.magsize = character['firearm']['ammo']

    def draw(self):
        """Draw your weapon to be able in future fire with it.
        Highly depends on the firearm, since a rifle takes quite a bit to unsheathe"""
        if self.is_drawn:
            return False, 'The weapon is already drawn'
        # else

        if self.char['perk'].__name__ in QUICKDRAW_PERKS_LIST:
            self.time -= self.char['perk'](self.firearm['draw'])
        else:
            self.time -= self.firearm['draw']
        self.is_drawn = True
        return True, 'You draw your revolver pointing at your sworn enemy!'


    def fire(self, enemy): # enemy : Gunslinger
        """Shoot another gunslinger, dropping them dead
        with a chance determined by the accuracy of the firearm"""

        if not self.is_drawn:
            return False, ("You are making some movements with your hand, "
                           "as if trying to shoot your gun, only to realise it's still holstered!")
        elif self.firearm['ammo'] == 0:
            return False, 'You gotta load your gun for that!'
        # else

        self.time -= self.firearm['shoot']
        self.firearm['ammo'] -= 1

        if enemy.char['perk'] in DODGY_PERKS_LIST:
            result = randint(1, 100)
            if enemy.char['perk'](self.firearm['accuracy']) - result >= 0:
                return None, ('The bullet has hit ' + enemy.char['name'] +
                              ' leaving them wishing they never started a fight with you')
        else:
            result = randint(1, 100)
            if self.firearm['accuracy'] - result >= 0:
                return None, ('The bullet has hit ' + enemy.char['name'] +
                              ' leaving them wishing they never started a fight with you')

        return (True, 'Not quite! ' + enemy.char['name'] +
                ' is still standing as your bullet cuts air beside them')

    def reload(self):
        """Reload your weapon, quantity of new cartridges loaded
        as well as the speed are determined by the firearm parameters"""
        # When moving/hiding behind cover will be added,
        # a system of increasing reload speed during movement will be implemented

        if self.firearm['reload_type'] == 'OnePerLoad':
            ammo_loaded = 1
            if self.is_drawn and self.firearm['ammo'] < self.magsize:
                self.firearm['ammo'] += 1
                return True, 'You are pushing pushing a cartridge your gun with shaky hands...'
            # else
            return False, ('Not sure what happened there, '
                           'you tried pushing a cartridge either into air or into another bullet')

        elif self.firearm['reload_type'] == 'Magazine':
            if self.is_drawn and self.firearm['ammo'] < self.magsize:
                self.firearm['ammo'] = self.magsize
                return True, 'You are pushing pushing the magazine into your gun with shaky hands...'
            # else
            return False, ('Not sure what happened there, '
                           'you tried pushing a mag either into air or into another mag')

        # else
        return False, 'Inexistent weapon type'
