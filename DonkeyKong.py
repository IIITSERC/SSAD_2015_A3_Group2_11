#!/usr/bin/python
# -*- coding: utf-8 -*-
#Created by Divanshu jain on 19 Aug, 2015

from random import choice
from random import randint
import os
import sys
import time
import copy

mapChars = ['═','║','╚','╝','╔','╗','╩','╦','╠','╣']

sampleMap = u"""
╔════════════════════╦══════════════╦══════════════════════════════════════════╗
║                    ║          Q   ║                                          ║
║                    ╚═════╗H╔══════╝                                          ║
║                          ║H║                                                 ║
║                          ║H║                                                 ║
║                           H                                                  ║
╠═════════════════════════════════════════╗H╔═══                               ║
║                                         ║H║                                  ║
║                                         ║H║                                  ║
║                                          H                                   ║
║                              ═══╗H╔═══════════╗H╔════════════════════════════╣
║                                 ║H║           ║H║                            ║
║                                 ║H║                                          ║
║                                  H             H                             ║
╠═════════════════════════════════════════════════════╗H╔════                  ║
║                                                     ║H║                      ║
║                                                     ║H║                      ║
║                                                      H                       ║
║                     ════╗H╔══════════════════════════════════════════════════╣
║                         ║H║                                                  ║
║                         ║H║                                                  ║
║                          H                                                   ║
╠══════════════════════════════════════╗H╔═══════════                          ║
║                                      ║H║                                     ║
║                                      ║H║                                     ║
║                                       H                                      ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

colors = {
"blue": lambda x: "\x1b[01;34m" + x + "\x1b[00m",
"yellow": lambda x: "\x1b[01;33m" + x + "\x1b[00m",
"green": lambda x: "\x1b[01;32m" + x + "\x1b[00m",
"red": lambda x: "\x1b[01;31m" + x + "\x1b[00m",
}


class Game(object):
        "The class for whole game, including all other classes."

        def __init__(self):
                self.score = 0
                self.lives = 3
                self.status = 'ready'
                self.previnp = 'right'

        def setMap(self, mapString):
                self.map = self.Map(self, mapString)
                self.map.init()

        def collectCoin(self):
                self.score += 5

        def getScore(self):
                return self.score

        def getLives(self):
                return self.lives

        def encounterball(self):
                self.lives -= 1
                if self.lives == 0:
                        self.status = 'dead'
                self.score -= 25
                if self.score < 0:
                        self.score = 0

        def _clearScreen(self):
                os.system('cls' if os.name == 'nt' else 'clear')

        def doAction(self):
                if self.status is 'running':
			self.map.display()
			print "Score: "+str(self.getScore())
                        print "Lives: "+str(self.getLives())

			try:
				inp = raw_input(':')
			except KeyboardInterrupt:
				self.stop('exit')
				return False

			self._clearScreen()

                        self.Donkey
                        if inp is 'w':
                                self.map.player.move('up')
                                self.previnp = self.previnp
                        elif inp is 's':
                                self.map.player.move('down')
                                self.previnp = self.previnp
                        elif inp is 'a':
                                self.map.player.move('left')
                                self.previnp = 'left'
                        elif inp is 'd':
                                self.map.player.move('right')
                                self.previnp = 'right'
                        elif inp is ' ':
                                # print 'yay'
                                self.map.player.move('jump')
                                self.previnp = self.previnp
                        elif inp is 'q':
                                self.stop('exit')
                                return False
                        else:
                                return True

                if self.status is 'dead' or self.status is 'win':
			self.map.display()
			print "Score: "+str(self.getScore())
                        print "Lives: "+str(self.getLives())
			self.stop(self.status)
			return False

                return True

        def start(self):
                self.status = 'running'
                self._clearScreen()
                while self.doAction():
                        pass

        def stop(self, type):
                if type == 'dead':
                        self._clearScreen()
			print colors['red']("""
  _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______
 /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \
|  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |
|  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /
|  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.
 \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|
""")
		elif type == 'exit':
			print colors['yellow']("""
  _______   ______     ______    _______     .______   ____    ____  _______  __
 /  _____| /  __  \   /  __  \  |       \    |   _  \  \   \  /   / |   ____||  |
|  |  __  |  |  |  | |  |  |  | |  .--.  |   |  |_)  |  \   \/   /  |  |__   |  |
|  | |_ | |  |  |  | |  |  |  | |  |  |  |   |   _  <    \_    _/   |   __|  |  |
|  |__| | |  `--'  | |  `--'  | |  '--'  |   |  |_)  |     |  |     |  |____ |__|
 \______|  \______/   \______/  |_______/    |______/      |__|     |_______|(__)
""")
		elif type == 'win':
			self._clearScreen()
			print colors['green']("""
____    ____  ______    __    __     ____    __    ____  __  .__   __.  __
\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  | |  |
 \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  | |  |
  \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  | |  |
    |  |    |  `--'  | |  `--'  |       \    /\    /    |  | |  |\   | |__|
    |__|     \______/   \______/         \__/  \__/     |__| |__| \__| (__)
""")

	"Definations of classes required"
        #class point do later
        class Point(object):
                "Class for points in map"

                def __init__(self, row, col, char):
                        """
			int row - Row
			int col - Column
			char char - defines char is there at the point
			"""
                        self.col = col
                        self.row = row
                        self.type = 'notAvailable'
                        self.set(char)
                        if self.type in ['free', 'player', 'coin', 'princess']:
                                self.permChar = u" "
                        elif self.type is 'stairs':
                                self.permChar = u"H"
                        # else:
                        #         self.permChar = u" "


                def __str__(self):
			if self.isCoin():
				return colors['yellow'](self.char.encode('utf-8'))
			elif self.isPlayer():
				return colors['blue'](self.char.encode('utf-8'))
			return self.char.encode('utf-8')

		def __repr__(self):
			return self.__str__()

                def set(self, char):
                        if char == u"C":
                                char == u"$"
                        self.char = char
                        if self.char.encode('utf-8') in mapChars:
                                self.type = 'wall'
                        elif self.char == u" ":
                                self.type = 'free'
                        elif self.char == u"P":
				self.type = 'player'
			elif self.char == u"$" or self.char == u"C":
				self.type = 'coin'
                        elif self.char == u"H":
                                self.type = 'stairs'
                        elif self.char == u"Q":
                                self.type = 'princess'

                def reset(self):
                        self.set(self.permChar)

                def isFree(self):
			return True if self.type is 'free' else False

                def isWall(self):
			return True if self.type is 'wall' else False

                def isPlayer(self):
			return True if self.type is 'player' else False

		def isCoin(self):
			return True if self.type is 'coin' else False

                def isStairs(self):
                        return True if self.type is 'stairs' else False

		def getChar(self):
			return self.char

        class Map(object):
                "Class for the game map"

                def __init__(self, game, mapString):
                        self.game = game
                        self.coins = 0
                        self.matrix = self._analyzeMap(mapString)
                        self.height = len(self.matrix)
                        self.width = len(self.matrix[0])

                def _analyzeMap(self, mapString):
                        mapMatrix = filter(None, mapString.split("\n"))
			for lineI in xrange(0, len(mapMatrix)):
				mapMatrix[lineI] = filter(None, list(mapMatrix[lineI]))
				if lineI is 0:
					lineLen = len(mapMatrix[0])
				elif lineLen != len(mapMatrix[lineI]):
					raise ValueError('The map inserted is not valid')
				for charI in xrange(0, len(mapMatrix[lineI])):
					mapMatrix[lineI][charI] = self.game.Point(lineI, charI, mapMatrix[lineI][charI])

			return mapMatrix

                def init(self):
			self.freePoints = list()
			for lineI in self.matrix:
				for charI in lineI:
					if charI.isFree():
                                                if charI.col != 1 and charI.row !=25:
                                                        self.freePoints.append(charI)
			self._setPlayer()
			self._setCoins(20)
                        self._setDonkey()
			del self.freePoints

		def _setPlayer(self):

			self.player = self.game.Player(self.game, 1, 25)

                def _setDonkey(self):

                        pos = randint(0, 45)
                        self.donkey = self.game.Donkey(self.game, pos, 5)


		def _setCoins(self, number):
			frees = self.freePoints[:]
			for i in xrange(0, number):
				index = randint(0, len(frees))
				frees[index].set(u"C")
				self.coins += 1
				del frees[index]

                def display(self):
                        for line in self.matrix:
                                print ''.join([str(s) for s in line])

                def getPoint(self, col, row):
                        "Get information about a point"

                        return self.matrix[row][col]

                def getSurroundings(self, col, row, direction = 'all'):
                        "Get information about surrounding points"

                        ans = {};

                        if direction is 'up' or direction is 'all':
                                ans['up'] = self.getPoint(col, row-1)
			if direction is 'down' or direction is 'all':
				ans['down'] = self.getPoint(col, 0 if row == self.height-1 else row+1)
			if direction is 'left' or direction is 'all':
				ans['left'] = self.getPoint(col-1 if col > 0 else self.width-1, row)
			if direction is 'right' or direction is 'all':
				ans['right'] = self.getPoint(0 if col == self.width-1 else col+1, row)

			return ans

        class Person(object):
                "Class for persons like donkeykong, player"

                def __init__(self, game, personType, col, row):
                        self.game = game
                        self.col = col
                        self.row = row
                        self.personType = personType

        class Player(Person):
                "Class for Player inherited from Person"

                def __init__(self, game, col, row):
                        Game.Person.__init__(self, game, u"P", col, row)
                        self.game.map.getPoint(col, row).set(u"P")

                def move(self, direction):
                        if direction is 'jump':
                                target = self.game.map.getPoint(self.col, self.row-1)
                        else:
                                target = self.game.map.getSurroundings(self.col, self.row, direction)[direction]


                        if (direction in ['up']):
                                if self.game.map.getPoint(self.col, self.row).permChar == u'H':
        				target.set(self.personType)
                                        self.game.map.getPoint(self.col, self.row).reset()
                                        self.col = target.col
                                        self.row = target.row


                        elif (direction in ['down']):
                                if self.game.map.getPoint(self.col, self.row+1).permChar == u'H':
                                        target.set(self.personType)
                                        self.game.map.getPoint(self.col, self.row).reset()
                                        self.col = target.col
                                        self.row = target.row


                        elif direction in ['jump']:
                                if (target.isFree() or target.isCoin()):
                                        target = self.game.map.getSurroundings(self.col, self.row, 'up')['up']
                                        if target.isCoin():
                                                self.game.collectCoin()
                                        target.set(self.personType)
                                        self.game.map.getPoint(self.col, self.row).reset()
                                        self.col = target.col
                                        self.row = target.row
                                target = self.game.map.getPoint(self.col+1, self.row)
                                if (target.isFree() or target.isCoin()):
                                        target = self.game.map.getSurroundings(self.col, self.row, self.game.previnp)[self.game.previnp]
                                        if target.isCoin():
                                                self.game.collectCoin()
                                        target.set(self.personType)
                                        self.game.map.getPoint(self.col, self.row).reset()
                                        self.game.map.display()
                                        time.sleep(0.2)
                                        self.game._clearScreen()
                                        self.col = target.col
                                        self.row = target.row
                                target = self.game.map.getPoint(self.col, self.row-1)
                                if (target.isFree() or target.isCoin()):
                                        target = self.game.map.getSurroundings(self.col, self.row, 'up')['up']
                                        if target.isCoin():
                                                self.game.collectCoin()
                                        target.set(self.personType)
                                        self.game.map.getPoint(self.col, self.row).reset()
                                        self.col = target.col
                                        self.row = target.row
                                target = self.game.map.getPoint(self.col+1, self.row)
                                if (target.isFree() or target.isCoin()):
                                        target = self.game.map.getSurroundings(self.col, self.row, self.game.previnp)[self.game.previnp]
                                        if target.isCoin():
                                                self.game.collectCoin()
                                        target.set(self.personType)
                                        self.game.map.getPoint(self.col, self.row).reset()
                                        self.game.map.display()
                                        time.sleep(0.2)
                                        self.game._clearScreen()
                                        self.col = target.col
                                        self.row = target.row
                                target = self.game.map.getPoint(self.col, self.row+1)
                                if (target.isFree() or target.isCoin()):
                                        target = self.game.map.getSurroundings(self.col, self.row, 'down')['down']
                                        if target.isCoin():
                                                self.game.collectCoin()
                                        target.set(self.personType)
                                        self.game.map.getPoint(self.col, self.row).reset()
                                        self.col = target.col
                                        self.row = target.row
                                target = self.game.map.getPoint(self.col+1, self.row)
                                if (target.isFree() or target.isCoin()):
                                        target = self.game.map.getSurroundings(self.col, self.row, self.game.previnp)[self.game.previnp]
                                        if target.isCoin():
                                                self.game.collectCoin()
                                        target.set(self.personType)
                                        self.game.map.getPoint(self.col, self.row).reset()
                                        self.game.map.display()
                                        time.sleep(0.2)
                                        self.game._clearScreen()
                                        self.col = target.col
                                        self.row = target.row
                                target = self.game.map.getPoint(self.col, self.row+1)
                                if (target.isFree() or target.isCoin()):
                                        target = self.game.map.getSurroundings(self.col, self.row, 'down')['down']
                                        if target.isCoin():
                                                self.game.collectCoin()
                                        target.set(self.personType)
                                        self.game.map.getPoint(self.col, self.row).reset()
                                        self.col = target.col
                                        self.row = target.row
                                target = self.game.map.getPoint(self.col+1, self.row)
                                if (target.isFree() or target.isCoin()):
                                        target = self.game.map.getSurroundings(self.col, self.row, self.game.previnp)[self.game.previnp]
                                        if target.isCoin():
                                                self.game.collectCoin()
                                        target.set(self.personType)
                                        self.game.map.getPoint(self.col, self.row).reset()
                                        self.game.map.display()
                                        time.sleep(0.2)
                                        self.game._clearScreen()
                                        self.col = target.col
                                        self.row = target.row


                        elif (direction in ['left', 'right'] and not target.isWall()):
                                if target.isCoin():
                                        self.game.collectCoin()
                                target.set(self.personType)
                                self.game.map.getPoint(self.col, self.row).reset()
                                self.col = target.col
                                self.row = target.row

                        else:
                                return False

                        r = self.row+1
                        c = self.col

                        while not self.game.map.getPoint(c, r).isWall() and not self.game.map.getPoint(c, r).isStairs():
                                m = self.game.map.getSurroundings(self.col, self.row, 'down')['down']
                                if m.isCoin():
                                        self.game.collectCoin()
                                m.set(self.personType)
                                self.game.map.getPoint(self.col, self.row).reset()
                                self.game.map.display()
                                time.sleep(0.1)
                                self.game._clearScreen()
                                self.col = m.col
                                self.row = m.row
                                r = self.row+1
                                c = self.col

                        if (self.game.map.getPoint(self.col+1, self.row) is self.game.map.getPoint(32, 1)):
                                self.game.status = 'win'

        class Donkey(Person):
                "Class that defines the Donkey"

                def __init__(self, game, col, row):
                        Game.Person.__init__(self, game, u"D", col, row)
                        self.game.map.getPoint(col, row).set(u"D")







if __name__ == '__main__':
        a = Game()
        a.setMap(sampleMap)
        a.start()
