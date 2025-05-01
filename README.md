# GunslingersAndQuickies
Console quickdraw wild west game meant to show my knowledge of Object-Oriented-Programming and Python overall

Current missing functions described in README:
  1. Local PvE
  2. Online PvP

First, the player picks whether they would like to PvP or PvE.
After the game has set up the fight, the player picks a character from the given list
Then, the program proceeds to start the gunfight

The gunfight works as follows:
The gunfight takes simultaneous turns, each turn is 1 in-game second, which can be used by the fighters for taking different actions
Simultaneous turns - the fighters pick their actions in a line if local, but the aftermath is detected

The fighters have several actions to do during their turn:

1. Draw (takes the the time specified as drawing speed of the firearm + any character perks)
  Your character draws their weapon. A weapon cannot be shot before being drawn (unless you want to shoot your own toe off)

2. Fire (takes the time specified as shooting speed of the firearm + any character perks)
  Fire your weapon

3. Reload (takes the time specified as reloading speed of the firearm)
  Reload your weapon in case you have already shot all your bullets into thin air

### The following actions are to be added later on

4. Take aim (takes the time specified as aiming speed of the firearm)
  Aim your weapon well, increasing the accuracy

5. Find cover (takes 1 full second of the turn):
  The fighter seeks cover around them, with a 75% chance manages to hide themselves from enemy fire, making themselves safe from gunfire
    This function is implied to be used by players when in disadvantage on the drawing speed

6. Move (takes no time)
  Takes no time to do, since the character can do whatever while moving. 3 successful Move actions will make the character able to see a character that is hiding behind cover
    All actions taken during a turn that is also a Move turn take twice as much time or have twice as lower success chance
