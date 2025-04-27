from settings.settings import characters, char_list
from cls.gunslinger import Gunslinger
from time import sleep


def main():
    sleep(1)
    player_qty = int(input("Howdy, y'all the ones that wanted to test their luck, they said. "
                           "Could ya tell me how much of y'all, then, I don't count well past one\n"))
    sleep(1)
    print('Gotcha, pardners, pick your characters then!')
    sleep(1)

    players = []
    for i in range(1, player_qty + 1):
        # This cycle goes through players, gives them the choice of characters
        # and writes down their choices afterward
        print('Player {}, here are the available characters'.format(i))

        for j in range(len(char_list)):
            print('{}. {}'.format(j + 1, char_list[j]))

        choice = int(input())
        players.append(Gunslinger(characters[choice - 1]))

    print("The choice 'been made now, let's start!")

    response = (True, 'Start')
    while True:
        print("""It's time for y'all's fight! Pick your moves wisely.
        \nThe turns happen simultaneously, which means you will bid your action against other player's action before the turn occures""")
        while response is not None:
            print("""Player 1, your turn! Pick one of the actions from the list below
            1. Draw: Draw your weapon, not much you can do without doing this
            2. Fire: Fire your weapon, can only be done after drawing or bullets loaded
            3. Reload: Reload your weapon in case you shot all your bullets and still haven't hit your other target
            4. Move: Moving will take no time, but will reduce your accuracy, as well as enemy's accuracy (unless they are holding a rifle)""")
            choice = int(input('So what are you going to do?\n'))




if __name__ == '__main__':
    main()
