from settings.settings import QUICKDRAW_PERKS_LIST, DODGY_PERKS_LIST
from random import randint
from enum import IntEnum


class Response(IntEnum):
    """At all times the methods of the main class Gunslinger return a tuple, with the first element being Response
    This is meant to simplify reading of the code
    New response codes may appear as project gains size"""
    CONTINUE = 100  # Continue the order of turns
    OK = 200  # Somebody has been shot
    BAD_REQUEST = 400  # Re-run turn, something wrong occurred


class Gunslinger:
    def __init__(self, character : dict):
        self._char = character["char"]
        self._firearm = character["firearm"]
        self._is_drawn = False
        self.ammo = character["firearm"]["magsize"]
        self._cover = False

        # editable by the main code values
        self.time = 1.0

        # properties
        self._name = character["char"]["name"]


    @property
    def name(self):
        return self._name

    @property
    def char(self):
        return self._char

    @property
    def firearm(self):
        return self._firearm

    def draw(self) -> tuple:
        """Draw your weapon to be able in future fire with it.
        Highly depends on the firearm, since, for instance, a rifle takes quite a bit to unsheathe"""
        if self._is_drawn:
            return Response.BAD_REQUEST, "The weapon is already drawn"
        # else
        subtract_time = self.firearm["draw"]
        if self._char["perk"].__name__ in QUICKDRAW_PERKS_LIST:
            subtract_time = self._char["perk"](subtract_time)

        if self.time - subtract_time < 0:  # If you have no time, you can't do something
            return Response.BAD_REQUEST, ("Ain't no time for that, you gotta be quicker on hand than this! "
                                          "You still have {}s left").format(self.time)

        self._is_drawn = True
        self.time -= self.firearm["draw"]
        return Response.CONTINUE, ("You draw your weapon pointing at your sworn enemy! "
                                   "You have {}s left").format(self.time)


    def fire(self, enemy) -> tuple: # enemy : Gunslinger
        """Shoot another gunslinger, dropping them dead
        with a chance determined by the accuracy of the firearm"""

        if self == enemy:
            return Response.BAD_REQUEST, ("Trying to escape life, huh? "
                                          "We don't allow such things here, cmon, get to shooting others")

        if not self._is_drawn:
            return Response.BAD_REQUEST, ("You are trying some movements with your hand, "
                                          "as if trying to shoot your gun, only to realise it's still holstered?")
        elif self.firearm["magsize"] == 0:
            return Response.BAD_REQUEST, "You gotta load your gun for that, I think"
        elif self.time - self.firearm["fire"] < 0:  # If you have no time, you can't do something
            return Response.BAD_REQUEST, ("Ain't no time for that, you gotta be quicker on hand than this! "
                                          "You still have {}s left").format(self.time)
        # else

        self.time -= self.firearm["fire"]
        self.ammo -= 1
        result = randint(1, 100)
        if enemy.char["perk"] in DODGY_PERKS_LIST:
            if enemy.char["perk"](self.firearm["accuracy"]) - result >= 0:
                return Response.OK, ("The bullet will be shot directly at " + enemy.char["name"] +
                                     ", only thing that might stop you is some other 'slinger being faster. "
                                     "You still have {}s left".format(self.time))
        else:
            if self.firearm["accuracy"] - result >= 0:
                return Response.OK, ("The bullet will be shot directly at " + enemy.char["name"] +
                                     ", only thing that might stop you is some other 'slinger being faster. "
                                     "You still have {}s left".format(self.time))

        return Response.CONTINUE, ("Not quite! " + enemy.char["name"] +
                                   " will be still standing with your bullet cutting air beside them. "
                                   "You still have {}s left".format(self.time))


    def reload(self) -> tuple:
        """Reload your weapon, quantity of new cartridges loaded
        as well as the speed are determined by the firearm parameters"""
        # When moving/hiding behind cover will be added,
        # a system of decreasing reload speed during movement will be implemented

        if self.time - self.firearm["reload"] < 0:  # If you have no time, you can't do something
            return Response.BAD_REQUEST, ("Ain't no time for that, you gotta be quicker on hand than this! "
                                          "You still have {}s left").format(self.time)
        # else

        if self.firearm["reload_type"] == "OnePerLoad":
            if self._is_drawn and self.ammo < self.firearm["magsize"]:
                self.ammo += 1
                self.time -= self.firearm["reload"]
                return Response.CONTINUE, ("You are pushing pushing a cartridge your gun with shaky hands... "
                                           "You still have {}s left "
                                           "and your weapon is up {} cartridges now".format(self.time, self.ammo))
            # else
            return Response.BAD_REQUEST, ("Not sure what happened there, "
                                          "you tried pushing a cartridge either into air or into another bullet")

        elif self.firearm["reload_type"] == "magazine":
            if self._is_drawn and self.ammo < self.firearm["magsize"]:
                self.ammo = self.firearm["magsize"]
                self.time -= self.firearm["reload"]
                return Response.CONTINUE, ("You are pushing pushing the magazine into your gun with shaky hands... "
                                           "You still have {}s left "
                                           "and your weapon holds {} rounds now".format(self.time, self.ammo))
            # else
            return Response.BAD_REQUEST, ("Not sure what happened there, "
                                          "you tried pushing a mag either into air or into another mag")

        # else
        return Response.BAD_REQUEST, "Nonexistent weapon type, consider fixing your code ape!"


    def find_cover(self) -> tuple:
        raise NotImplementedError


    def move(self, towards_who) -> tuple:  # towards_who : Gunslinger
        raise NotImplementedError


def calculate_outcome(logs : list) -> tuple:  # returns a tuple of the dead
    """Accepts on input a list of tuples with each tuple inside being a log for a gunshot
    Example structure of the tuple inside main tuple:
    (Gunslinger object of the shooter, shooter's leftover time, Gunslinger object of the player who got hit)"""
    unread_logs = list(logs)  # the function will delete logs from unread_logs as they are processed
    who_died = []

    while len(unread_logs) > 0:
        fastest = 0
        for i in range(1, len(unread_logs)):
            if unread_logs[i][1] > unread_logs[fastest][1]:
                fastest = i

        who_died.append(unread_logs[fastest][2])
        print(unread_logs[fastest][2].name, "has been shot!")
        death = unread_logs.pop(fastest)

        for i in range(len(unread_logs)):
            if unread_logs[i][0] == death[2]:
                unread_logs.pop(i)

    return tuple(who_died)
