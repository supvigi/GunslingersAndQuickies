from settings.settings import characters, char_list
from cls.gunslinger import Gunslinger, calculate_outcome
from time import sleep
from random import randint


def main():
    # The program uses sleep(1) with console output functions in order to simulate more organic conversation
    # I really wanted to make a decorator for print that will make the sleep(1) for me
    # but IDE's complaints got too far up my head

    # Receiving quantity of players
    sleep(1)
    player_qty = 0
    while not (1 < player_qty < 6):
        player_qty = int(input("Howdy, y'all the ones that wanted to test their luck, they said. "
                               "Could ya tell me how much of y'all, then, I don't count well past one\n"))
        sleep(1)

    print("Gotcha, pardners, pick your characters then!")
    sleep(1)
    players = []  # List for holding all players' chars
    # This cycle goes through players, gives them the choice of characters and writes down their choices afterward
    for i in range(1, player_qty + 1):
        while True:
            print("Player {}, here are the available characters. "
                  "Pushing a number of a certain character will show their description".format(i))

            for j in range(len(char_list)):  # Cycle for outputting all characters in a list
                print('{}. {}'.format(j + 1, characters[j]["char"]["name"]))

            # Receiving the choice of the player and appending it to the list of players
            choice = int(input())
            sleep(1)
            if input(characters[choice - 1]["char"]["desc"] + "\nDo you want to pick this character? "
                                                              "Type Y if yes, "
                                                              "otherwise type anything else\n").upper() == "Y":
                players.append(Gunslinger(characters[choice - 1]))
                break

    sleep(1)
    print("The choice 'been made now, let's start!\n")
    sleep(1)
    print("It's time for y'all's fight! Pick your moves wisely.\n"
          "The turns happen simultaneously, which means you will bid your action against "
          "other player's action before the turn occurs.\n"
          "Please do not look at the screen when it is not your turn, "
          "otherwise you will be seeing what another player is planning")

    while True:  # This cycle repeats the FOR-cycle of players' moves
        logs = []

        if len(players) == 1:
            print("The survivor has been found! It's {}!".format(players[0].name))
            return 0

        for player in players:  # This cycle ensures every player gets their turn in line
            # Since every action takes time to do (exception is Move),
            # another while True is used to give the player a re-move in case they didn't have time for their choice
            while True:
                choice = None
                response = None
                sleep(1)
                args = (players.index(player) + 1, player.time, player.firearm["draw"],
                        player.firearm["fire"], player.firearm["reload"])
                print("\nPlayer {}, your turn! Pick one of the actions from the list below. You have {}s left\n"
                      "1. Draw {}s: Draw your weapon, not much you can do without doing this\n"
                      "2. Fire {}s: Fire your weapon, can only be done after drawing or bullets loaded\n"
                      "3. Reload {}s: Reload your weapon "
                      "in case you shot all your bullets and still haven't hit your other target\n"
                      "4. TBD | Move: Moving will take no time, "
                      "3 Move actions will allow you to find an enemy in cover and open fire.\n"
                      "Any turn with move action reduces your accuracy to hell\n"
                      "5. TBD | Find Cover: Hiding with a 75% chance will help you evade enemy fire, "
                      "to be used when not willing to risk "
                      "getting drawn first-move\n"
                      "6. End your turn, in case you have no more time left".format(*args))

                sleep(1)
                choice = int(input('So what are you going to do? Pick a number\n'))

                if choice == 1:
                    response, message = player.draw()
                    print(message)
                elif choice == 2:
                    while True:
                        while True:
                            sleep(1)

                            for j in range(len(players)):  # Cycle for outputting all characters in a list
                                print('{}. {}'.format(j + 1, players[j].char["name"]))

                            enemy_num = int(input("Alright, who are you shooting at? Specify the player's number\n"))
                            if input("Are you sure? Y if yes, anything else if no\n").upper() == "Y":
                                break

                        try:
                            response, message = player.fire(players[enemy_num - 1])

                            print(message)
                            if response == 200:
                                logs.append((player, player.time, players[enemy_num - 1]))

                            break
                        except IndexError:
                            print("Looks like the number you input is wrong. Try again")

                elif choice == 3:
                    response, message = player.reload()
                    print(message)
                elif choice == 4 or choice == 5:  # Movement and hiding are NotImplemented
                    raise NotImplementedError("This function/method is not yet implemented!")
                elif choice == 6:
                    sleep(1)
                    print("Ending your turn, I see")
                    sleep(3)
                    # Some stuff made to make one's moves unseen to next one
                    print("...\n" * 48)
                    if randint(0, 1):
                        print("PROTIP: play fairly, otherwise b-o-o-o-o-ring\n...\n")
                    else:
                        print("...\n" * 2)
                    break
                else:
                    sleep(1)
                    print("Did I give you another choice, pardner?")

        who_died = calculate_outcome(logs)

        for player in players:
            if player in who_died:
                players.remove(player)
            else:
                if player.time <= 0.5:
                    player.time += 1
                else:
                    player.time = 1.5


if __name__ == "__main__":
    main()
