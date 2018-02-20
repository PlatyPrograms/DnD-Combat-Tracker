from operator import attrgetter
import os

longestCreatureName = 8
longestStatusName = 6

class Creature(object):
    name = ''
    initiative = 0

    def __init__(self, newName, newInitiative):
        self.name = newName
        self.initiative = newInitiative
        global longestCreatureName
        if (len(newName) > longestCreatureName):
            longestCreatureName = len(newName)

    def __repr__(self):
        return self.name

class PC(Creature):

    def __init__(self, newName, newInitiative):
        super(PC, self).__init__(newName, newInitiative)

    def __repr__(self):
        return self.name

class NPC(Creature):
    name = ''
    maxHp = 0
    tempHp = 0
    curHp = 0
    ac = 0
    status = {}

    def __init__(self, newName, newHealth, newAc, newInitiative):
        super(NPC, self).__init__(newName, newInitiative)
        self.maxHp = newHealth
        self.curHp = newHealth
        self.ac = newAc
        self.initiative = newInitiative

    def __repr__(self):
        return self.name

    def addTempHp(self):
        numTempHp = input('  temp hp: ')
        self.tempHp += numTempHp

    def heal(self):
        numHeal = input('  heal: ')
        self.curHp += numHeal
        if(curHp > maxHp):
            self.curHp = maxHp
                
    def hit(self):
        numDmg = input('  damage: ')
        if (self.tempHp > numDmg):
            self.tempHp -= numDmg
        elif (self.tempHp < numDmg):
            numDmg -= self.tempHp
            self.tempHp = 0
            self.curHp -= numDmg
            if (self.curHp < 0):
                self.curHp = 0
            if (self.curHp <= 0):
                return True
        return False

    def addStatus(self):
        newStat = raw_input('  status name: ')
        duration = raw_input('  duration: ')
        if (duration != '-'):
            try:
                duration = int(duration)
            except:
                print('invalid duration')
                return
        self.status[newStat] = duration
        global longestStatusName
        if (len(newStat) > longestStatusName):
            longestStatusName = len(newStat)

    def removeStatus(self):
        toRemove = raw_input('  to remove: ')
        while (toRemove not in self.status):
            toRemove = raw_input('  invalid status, try again: ')
            if (toRemove == 'cancel'):
                return
        del self.status[toRemove]

def getInit(creature):
    return creature.initiative

def findCreature(creatures, name):
    for creature in creatures:
        if (creature.name == name):
            return creature
    return None



def getCreatures():
    creatures = []
    isPc = ''
    while (isPc != 'done'):
        isPc = raw_input('PC, NPC, or done? ')
        if (isPc == 'PC' or isPc == 'pc' or isPc == 'p'):
            playerName = raw_input('  PC name: ')
            while (findCreature(creatures, playerName)):
                playerName = raw_input('  Name taken. Try again: ')
            playerInitiative = input('  PC initiative: ')
            creatures.append(PC(playerName, playerInitiative))
        elif (isPc == 'NPC' or isPc == 'npc' or isPc == 'n'):
            name = raw_input('  NPC name: ')
            while (findCreature(creatures, name)):
                name = raw_input('  Name taken. Try again: ')
            health = input('  NPC HP: ')
            ac = input('  NPC AC: ')
            initiative = input('  NPC initiative: ')
            creatures.append(NPC(name, health, ac, initiative))
        elif (isPc != 'done'):
            print('Invalid input. Try again.')
    return creatures

def addCreatures(existingCreatures):
    newCreatures = getCreatures()
    existingCreatures.append(newCreatures)
    existingCreatures.sort(key=getInit, reverse = True)

def update(creatures, current):
    # UPDATE STATUSES
    curCreature = creatures[current]
    if isinstance(curCreature, NPC):
        toDelete = []
        for effect in curCreature.status:
            if curCreature.status[effect] != '-':
                curCreature.status[effect] -= 1
                if (curCreature.status[effect]) < 0:
                    toDelete.append(effect)
        for item in toDelete:
            del curCreature.status[item]
    #printTable(creatures, curCreature)
    
def printTable(creatures, curCreatureNum):
    # lengths
    curCreature = creatures[curCreatureNum]
    lenCreatureLine = max(10, longestCreatureName + 2)
    lenStatusLine = max(8, longestStatusName + 2)
    creatureHead = ' Creature ' + (' ' * (lenCreatureLine - 10))
    statusHead = ' Status ' + (' ' * (lenStatusLine - 8))
    lenHead = 23 + lenCreatureLine + lenStatusLine
    # lines
    mainLine = '=' * lenHead + '\n'
    bigCreatureLine = '=' * lenCreatureLine
    littleCreatureLine = '-' * lenCreatureLine
    bigStatusLine = '=' * lenStatusLine
    littleStatusLine = '-' * lenStatusLine
    bigSeparator = bigCreatureLine + '|====|=====|' + bigStatusLine + '|==========\n'
    littleSeparator = littleCreatureLine + '|---|----|' + littleStatusLine + '|----------\n'
    # table creation
    table = mainLine + ' CURRENT: ' + curCreature.name + '\n' + mainLine + creatureHead \
            + '| AC | HP  |' + statusHead + '| Duration\n' + bigSeparator
    for creature in creatures:
        table += ' ' + creature.name + ' ' + (' ' * (longestCreatureName - len(creature.name)))\
                 + '| '
        if isinstance(creature, PC):
            table += '-  | -   | -      ' + (' ' * (lenStatusLine - 8)) +  '| -\n'
        else:
            acBuf = ' '
            if (creature.ac / 10 == 0):
                acBuf += ' '
            table += str(creature.ac) + acBuf + '| '
            hpBuf = ''
            if (creature.curHp / 100 == 0):
                hpBuf += ' '
                if (creature.curHp / 10 == 0):
                    hpBuf += ' '
            table += str(creature.curHp) + hpBuf + ' |'
            if (creature.status == {}):
                table += ' -' + (' ' * (lenStatusLine - 2)) +  '| -\n'
            else:
                isFirst = True
                for effect in creature.status:
                    if isFirst:
                        isFirst = False
                        table += ' ' + effect + (' ' * (lenStatusLine - len(effect) - 1)) + \
                                 '| '
                    else:
                        table += (' ' * lenCreatureLine) + '|    |     | ' \
                                 + effect + (' ' * (lenStatusLine - len(effect) - 1)) + '| '
                    if (creature.status[effect]) == '-':
                        table += u'\u221e' + '\n'
                    else:
                        table += str(creature.status[effect]) + '\n'
    table += mainLine[:-1]
    os.system('clear')
    print(table)

def getTarget(creatures):
    targetString = raw_input('  target: ')
    targetCreature = findCreature(creatures, targetString)
    while (targetCreature == None):
        targetString = raw_input('  invalid target, try again: ')
        targetCreature = findCreature(creatures, targetString)
    return targetCreature
    
def runCombat(creatures):
    print('starting combat')
    action = ''
    curCreature = 0
    printTable(creatures, curCreature)
    toKill = []
    while (action != 'end' and action != 'done'):
        action = raw_input('action: ')
        if (action == 'next turn' or action == 'next' or action == 'n'):
            for dead in toKill:
                creatures.remove(dead)
            toKill = []
            if (len(creatures) <= 0):
                print("they're all dead!")
                break
            curCreature += 1
            if (curCreature >= len(creatures)):
                curCreature = 0
            update(creatures, curCreature)

        elif (action == 'hit' or action == 'damage'):
            targetCreature = getTarget(creatures)
            while (isinstance(targetCreature, PC)):
                print('  cannot target a PC')
                targetCreature = getTarget(creatures)
            isDead = targetCreature.hit()
            if isDead:
                toKill.append(targetCreature)

        elif (action == 'kill' or action == 'remove'):
            targetCreature = getTarget(creatures)
            toKill.append(targetCreature)
            
        elif (action == 'add status' or action == 'stat'):
            targetCreature = getTarget(creatures)
            targetCreature.addStatus()
            
        elif (action == 'remove stat' or action == 'unstat'):
            targetCreature.removeStatus()
        printTable(creatures, curCreature)

def main():
    creatures = getCreatures()
    creatures.sort(key=getInit, reverse=True)
    print(creatures)
    runCombat(creatures)

main()
