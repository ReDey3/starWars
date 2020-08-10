from math import sqrt

def do_turn(pw):
    if len(pw.my_fleets()) >= 1:
        return

    if len(pw.my_planets()) == 0:
        return
    for i in pw.my_planets():
        dest = 0
        if len(pw.neutral_planets()) >= 1:
            dest = get_closet_natrual(pw, i)
        else:
            if len(pw.enemy_planets()) >= 1:
                dest = pw.enemy_planets()[0]

        if dest.num_ships() + 1 < i.num_ships():
            num_ships = dest.num_ships() + 1
            pw.debug('Num Ships: ' + str(num_ships))

            pw.issue_order(i, dest, num_ships)



def get_closet_natrual(pw, planet):
    plantets = pw.neutral_planets()
    minPlant = plantets[0]
    min = sqrt( (minPlant.x() - planet.x())**2 + (minPlant.y() - planet.y())**2 )
    for i in plantets:
        pX = i.x()
        pY = i.y()
        mX = planet.x()
        mY = planet.y()
        if min > sqrt((i.x() - planet.x())**2 + (i.y() - planet.y())**2):
            min = sqrt((i.x() - planet.x())**2 + (i.y() - planet.y())**2)
            minPlant = i
    return minPlant
