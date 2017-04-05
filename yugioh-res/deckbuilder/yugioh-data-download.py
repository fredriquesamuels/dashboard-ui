import sqlite3
import itertools
import urllib2
import urllib
import os
import sys
import json
from pprint import pprint
import re
import urlparse

import CardDataTransformer as cdt

def getMonsterJsonUrl(offset):
    url = "http://yugioh.wikia.com/wiki/Special:Ask?x=-5B-5BClass-201%3A%3AOfficial-5D-5D-20-5B-5BCard-20type%3A%3AMonster-20Card-5D-5D-20-5B-5BCard-20type%3A%3AMonster-20Card-5D-5D%2F-3FEnglish-20name%3D%2F-3FJapanese-20name%2F-3FCard-20image%2F-3FPrimary-20type%2F-3FSecondary-20type%2F-3FAttribute%3D-5B-5BAttribute-5D-5D%2F-3FType%3D-5B-5BType-5D-5D%2F-3FStars%3D-5B-5BLevel-5D-5D-2F-5B-5BRank-5D-5D%2F-3FATK%3D-5B-5BATK-5D-5D%2F-3FDEF%3D-5B-5BDEF-5D-5D%2F-3FPasscode%3D-5B-5BPasscode-5D-5D%2F-3FPendulum-20Scale%2F-3FPendulum-20Effect%3D-5B-5BPendulum-20Effect-5D-5D%2F-3FLore%3D-5B-5BLore-5D-5D%2F-3FRitual-20Monster-20required%2F-3FRitual-20Spell-20Card-20required%2F-3FMaterials%2F-3FFusion-20Material&mainlabel=-&limit=500&prettyprint=true&format=json&offset="
    return url + str(offset)

def getSynchroJsonUrl(offset):
    url = "http://yugioh.wikia.com/wiki/Special:Ask?x=-5B-5BClass-201%3A%3AOfficial-5D-5D-20-5B-5BCard-20type%3A%3AMonster-20Card-5D-5D-20-5B-5BCard-20type%3A%3ASynchro-20Monster-5D-5D%2F-3FEnglish-20name%3D%2F-3FJapanese-20name%2F-3FCard-20image%2F-3FPrimary-20type%2F-3FSecondary-20type%2F-3FAttribute%3D-5B-5BAttribute-5D-5D%2F-3FType%3D-5B-5BType-5D-5D%2F-3FStars%3D-5B-5BLevel-5D-5D-2F-5B-5BRank-5D-5D%2F-3FATK%3D-5B-5BATK-5D-5D%2F-3FDEF%3D-5B-5BDEF-5D-5D%2F-3FPasscode%3D-5B-5BPasscode-5D-5D%2F-3FPendulum-20Scale%2F-3FPendulum-20Effect%3D-5B-5BPendulum-20Effect-5D-5D%2F-3FLore%3D-5B-5BLore-5D-5D%2F-3FRitual-20Monster-20required%2F-3FRitual-20Spell-20Card-20required%2F-3FMaterials%2F-3FFusion-20Material&mainlabel=-&limit=500&prettyprint=true&format=json&offset="
    return url + str(offset)
def getXyzJsonUrl(offset):
    url = "http://yugioh.wikia.com/wiki/Special:Ask?x=-5B-5BClass-201%3A%3AOfficial-5D-5D-20-5B-5BCard-20type%3A%3AMonster-20Card-5D-5D-20-5B-5BCard-20type%3A%3AXyz-20Monster-5D-5D%2F-3FEnglish-20name%3D%2F-3FJapanese-20name%2F-3FCard-20image%2F-3FPrimary-20type%2F-3FSecondary-20type%2F-3FAttribute%3D-5B-5BAttribute-5D-5D%2F-3FType%3D-5B-5BType-5D-5D%2F-3FStars%3D-5B-5BLevel-5D-5D-2F-5B-5BRank-5D-5D%2F-3FATK%3D-5B-5BATK-5D-5D%2F-3FDEF%3D-5B-5BDEF-5D-5D%2F-3FPasscode%3D-5B-5BPasscode-5D-5D%2F-3FPendulum-20Scale%2F-3FPendulum-20Effect%3D-5B-5BPendulum-20Effect-5D-5D%2F-3FLore%3D-5B-5BLore-5D-5D%2F-3FRitual-20Monster-20required%2F-3FRitual-20Spell-20Card-20required%2F-3FMaterials%2F-3FFusion-20Material&mainlabel=-&limit=500&prettyprint=true&format=json&offset="
    return url + str(offset)
def getFusionJsonUrl(offset):
    url = "http://yugioh.wikia.com/wiki/Special:Ask?x=-5B-5BClass-201%3A%3AOfficial-5D-5D-20-5B-5BCard-20type%3A%3AMonster-20Card-5D-5D-20-5B-5BCard-20type%3A%3AFusion-20Monster-5D-5D%2F-3FEnglish-20name%3D%2F-3FJapanese-20name%2F-3FCard-20image%2F-3FPrimary-20type%2F-3FSecondary-20type%2F-3FAttribute%3D-5B-5BAttribute-5D-5D%2F-3FType%3D-5B-5BType-5D-5D%2F-3FStars%3D-5B-5BLevel-5D-5D-2F-5B-5BRank-5D-5D%2F-3FATK%3D-5B-5BATK-5D-5D%2F-3FDEF%3D-5B-5BDEF-5D-5D%2F-3FPasscode%3D-5B-5BPasscode-5D-5D%2F-3FPendulum-20Scale%2F-3FPendulum-20Effect%3D-5B-5BPendulum-20Effect-5D-5D%2F-3FLore%3D-5B-5BLore-5D-5D%2F-3FRitual-20Monster-20required%2F-3FRitual-20Spell-20Card-20required%2F-3FMaterials%2F-3FFusion-20Material&mainlabel=-&limit=500&prettyprint=true&format=json&offset="
    return url + str(offset)
def getRitualJsonUrl(offset):
    url = "http://yugioh.wikia.com/wiki/Special:Ask?x=-5B-5BClass-201%3A%3AOfficial-5D-5D-20-5B-5BCard-20type%3A%3AMonster-20Card-5D-5D-20-5B-5BCard-20type%3A%3ARitual-20Monster-5D-5D%2F-3FEnglish-20name%3D%2F-3FJapanese-20name%2F-3FCard-20image%2F-3FPrimary-20type%2F-3FSecondary-20type%2F-3FAttribute%3D-5B-5BAttribute-5D-5D%2F-3FType%3D-5B-5BType-5D-5D%2F-3FStars%3D-5B-5BLevel-5D-5D-2F-5B-5BRank-5D-5D%2F-3FATK%3D-5B-5BATK-5D-5D%2F-3FDEF%3D-5B-5BDEF-5D-5D%2F-3FPasscode%3D-5B-5BPasscode-5D-5D%2F-3FPendulum-20Scale%2F-3FPendulum-20Effect%3D-5B-5BPendulum-20Effect-5D-5D%2F-3FLore%3D-5B-5BLore-5D-5D%2F-3FRitual-20Monster-20required%2F-3FRitual-20Spell-20Card-20required%2F-3FMaterials%2F-3FFusion-20Material&mainlabel=-&limit=500&prettyprint=true&format=json&offset="
    return url + str(offset)
def getEffectJsonUrl(offset):
    url = "http://yugioh.wikia.com/wiki/Special:Ask?x=-5B-5BClass-201%3A%3AOfficial-5D-5D-20-5B-5BCard-20type%3A%3AMonster-20Card-5D-5D-20-5B-5BCard-20type%3A%3AEffect-20Monster-5D-5D%2F-3FEnglish-20name%3D%2F-3FJapanese-20name%2F-3FCard-20image%2F-3FPrimary-20type%2F-3FSecondary-20type%2F-3FAttribute%3D-5B-5BAttribute-5D-5D%2F-3FType%3D-5B-5BType-5D-5D%2F-3FStars%3D-5B-5BLevel-5D-5D-2F-5B-5BRank-5D-5D%2F-3FATK%3D-5B-5BATK-5D-5D%2F-3FDEF%3D-5B-5BDEF-5D-5D%2F-3FPasscode%3D-5B-5BPasscode-5D-5D%2F-3FPendulum-20Scale%2F-3FPendulum-20Effect%3D-5B-5BPendulum-20Effect-5D-5D%2F-3FLore%3D-5B-5BLore-5D-5D%2F-3FRitual-20Monster-20required%2F-3FRitual-20Spell-20Card-20required%2F-3FMaterials%2F-3FFusion-20Material&mainlabel=-&limit=500&prettyprint=true&format=json&offset="
    return url + str(offset)
def getNormalJsonUrl(offset):
    url = "http://yugioh.wikia.com/wiki/Special:Ask?x=-5B-5BClass-201%3A%3AOfficial-5D-5D-20-5B-5BCard-20type%3A%3AMonster-20Card-5D-5D-20-5B-5BCard-20type%3A%3ANormal-20Monster-5D-5D%2F-3FEnglish-20name%3D%2F-3FJapanese-20name%2F-3FCard-20image%2F-3FPrimary-20type%2F-3FSecondary-20type%2F-3FAttribute%3D-5B-5BAttribute-5D-5D%2F-3FType%3D-5B-5BType-5D-5D%2F-3FStars%3D-5B-5BLevel-5D-5D-2F-5B-5BRank-5D-5D%2F-3FATK%3D-5B-5BATK-5D-5D%2F-3FDEF%3D-5B-5BDEF-5D-5D%2F-3FPasscode%3D-5B-5BPasscode-5D-5D%2F-3FPendulum-20Scale%2F-3FPendulum-20Effect%3D-5B-5BPendulum-20Effect-5D-5D%2F-3FLore%3D-5B-5BLore-5D-5D%2F-3FRitual-20Monster-20required%2F-3FRitual-20Spell-20Card-20required%2F-3FMaterials%2F-3FFusion-20Material&mainlabel=-&limit=500&prettyprint=true&format=json&offset="
    return url + str(offset)
def getPendulumJsonUrl(offset):
    url = "http://yugioh.wikia.com/wiki/Special:Ask?x=-5B-5BClass-201%3A%3AOfficial-5D-5D-20-5B-5BCard-20type%3A%3AMonster-20Card-5D-5D-20-5B-5BCard-20type%3A%3APendulum-20Monster-5D-5D%2F-3FEnglish-20name%3D%2F-3FJapanese-20name%2F-3FCard-20image%2F-3FPrimary-20type%2F-3FSecondary-20type%2F-3FAttribute%3D-5B-5BAttribute-5D-5D%2F-3FType%3D-5B-5BType-5D-5D%2F-3FStars%3D-5B-5BLevel-5D-5D-2F-5B-5BRank-5D-5D%2F-3FATK%3D-5B-5BATK-5D-5D%2F-3FDEF%3D-5B-5BDEF-5D-5D%2F-3FPasscode%3D-5B-5BPasscode-5D-5D%2F-3FPendulum-20Scale%2F-3FPendulum-20Effect%3D-5B-5BPendulum-20Effect-5D-5D%2F-3FLore%3D-5B-5BLore-5D-5D%2F-3FRitual-20Monster-20required%2F-3FRitual-20Spell-20Card-20required%2F-3FMaterials%2F-3FFusion-20Material&mainlabel=-&limit=500&prettyprint=true&format=json&offset="
    return url + str(offset)
def getTunerJsonUrl(offset):
    url = "http://yugioh.wikia.com/wiki/Special:Ask?x=-5B-5BClass-201%3A%3AOfficial-5D-5D-20-5B-5BCard-20type%3A%3AMonster-20Card-5D-5D-20-5B-5BMonster-20type%3A%3ATuner-20monster-5D-5D%2F-3FEnglish-20name%3D%2F-3FJapanese-20name%2F-3FCard-20image%2F-3FPrimary-20type%2F-3FSecondary-20type%2F-3FAttribute%3D-5B-5BAttribute-5D-5D%2F-3FType%3D-5B-5BType-5D-5D%2F-3FStars%3D-5B-5BLevel-5D-5D-2F-5B-5BRank-5D-5D%2F-3FATK%3D-5B-5BATK-5D-5D%2F-3FDEF%3D-5B-5BDEF-5D-5D%2F-3FPasscode%3D-5B-5BPasscode-5D-5D%2F-3FPendulum-20Scale%2F-3FPendulum-20Effect%3D-5B-5BPendulum-20Effect-5D-5D%2F-3FLore%3D-5B-5BLore-5D-5D%2F-3FRitual-20Monster-20required%2F-3FRitual-20Spell-20Card-20required%2F-3FMaterials%2F-3FFusion-20Material&mainlabel=-&limit=500&prettyprint=true&format=json&offset="
    return url + str(offset)
def getGeminiJsonUrl(offset):
    url = "http://yugioh.wikia.com/wiki/Special:Ask?x=-5B-5BClass-201%3A%3AOfficial-5D-5D-20-5B-5BCard-20type%3A%3AMonster-20Card-5D-5D-20-5B-5BMonster-20type%3A%3AGemini-20monster-5D-5D%2F-3FEnglish-20name%3D%2F-3FJapanese-20name%2F-3FCard-20image%2F-3FPrimary-20type%2F-3FSecondary-20type%2F-3FAttribute%3D-5B-5BAttribute-5D-5D%2F-3FType%3D-5B-5BType-5D-5D%2F-3FStars%3D-5B-5BLevel-5D-5D-2F-5B-5BRank-5D-5D%2F-3FATK%3D-5B-5BATK-5D-5D%2F-3FDEF%3D-5B-5BDEF-5D-5D%2F-3FPasscode%3D-5B-5BPasscode-5D-5D%2F-3FPendulum-20Scale%2F-3FPendulum-20Effect%3D-5B-5BPendulum-20Effect-5D-5D%2F-3FLore%3D-5B-5BLore-5D-5D%2F-3FRitual-20Monster-20required%2F-3FRitual-20Spell-20Card-20required%2F-3FMaterials%2F-3FFusion-20Material&mainlabel=-&limit=500&prettyprint=true&format=json&offset="
    return url + str(offset)
def getSpiritJsonUrl(offset):
    url = "http://yugioh.wikia.com/wiki/Special:Ask?x=-5B-5BClass-201%3A%3AOfficial-5D-5D-20-5B-5BCard-20type%3A%3AMonster-20Card-5D-5D-20-5B-5BMonster-20type%3A%3ASpirit-20monster-5D-5D%2F-3FEnglish-20name%3D%2F-3FJapanese-20name%2F-3FCard-20image%2F-3FPrimary-20type%2F-3FSecondary-20type%2F-3FAttribute%3D-5B-5BAttribute-5D-5D%2F-3FType%3D-5B-5BType-5D-5D%2F-3FStars%3D-5B-5BLevel-5D-5D-2F-5B-5BRank-5D-5D%2F-3FATK%3D-5B-5BATK-5D-5D%2F-3FDEF%3D-5B-5BDEF-5D-5D%2F-3FPasscode%3D-5B-5BPasscode-5D-5D%2F-3FPendulum-20Scale%2F-3FPendulum-20Effect%3D-5B-5BPendulum-20Effect-5D-5D%2F-3FLore%3D-5B-5BLore-5D-5D%2F-3FRitual-20Monster-20required%2F-3FRitual-20Spell-20Card-20required%2F-3FMaterials%2F-3FFusion-20Material&mainlabel=-&limit=500&prettyprint=true&format=json&offset="
    return url + str(offset)

def getTrapJsonUrl(offset):
    url = "http://yugioh.wikia.com/wiki/Special:Ask/-5B-5BClass-201::Official-5D-5D-20-5B-5BConcept:Non-2Dmonster-20cards-5D-5D-20-5B-5BCard-20type::Trap-20Card-5D-5D/-3FEnglish-20name/-3FJapanese-20name/-3FCard-20image/-3FProperty/-3FLore/mainlabel%3D-2D/offset%3D"+str(offset)+"/limit%3D500/prettyprint%3Dtrue/format%3Djson"
    return url

def getSpellJsonUrl(offset):
    url = "http://yugioh.wikia.com/wiki/Special:Ask/-5B-5BClass-201::Official-5D-5D-20-5B-5BConcept:Non-2Dmonster-20cards-5D-5D-20-5B-5BCard-20type::Spell-20Card-5D-5D/-3FEnglish-20name/-3FJapanese-20name/-3FCard-20image/-3FProperty/-3FLore/mainlabel%3D-2D/offset%3D"+str(offset)+"/limit%3D500/prettyprint%3Dtrue/format%3Djson"
    return url

# NOt using this since max results on wikia is 5000 and yugioh has more than that :|
def getCardsJsonUrl(offset):
    url = "http://yugioh.wikia.com/wiki/Special:Ask/-5B-5BClass-201::Official-5D-5D/-3FEnglish-20name/-3FJapanese-20name/-3FCard-20image/-3FPrimary-20type/-3FSecondary-20type/-3FAttribute/-3FType/-3FStars/-3FATK/-3FDEF/-3FPasscode/-3FPendulum-20Scale/-3FPendulum-20Effect/-3FLore/-3FRitual-20Monster-20required/-3FRitual-20Spell-20Card-20required/-3FMaterials/-3FFusion-20Material/-3FProperty/mainlabel%3D-2D/offset%3D"+str(offset)+"/limit%3D500/prettyprint%3Dtrue/format%3Djson"
    return url

def saveDataToFile(url, filename):
    if os.path.exists(filename):
        return
    print 'downloading.... ', url
    response = urllib2.urlopen(url)
    data = response.read()      # a `bytes` object
    # text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
    print 'saving... ', filename
    fh = open(filename, 'w')
    fh.write(data)
    fh.close()

def saveMonsterFile(offset):
    response = urllib2.urlopen(getMonsterJsonUrl(offset))
    data = response.read()      # a `bytes` object
    # text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
    fh = open('monster-list-'+str(offset)+'.json', 'w')
    fh.write(data)
    fh.close()

def saveSpellFile(offset):
    response = urllib2.urlopen(getSpellJsonUrl(offset))
    data = response.read()      # a `bytes` object
    # text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
    fh = open('spell-list-'+str(offset)+'.json', 'w')
    fh.write(data)
    fh.close()

def saveTrapFile(offset):
    response = urllib2.urlopen(getTrapJsonUrl(offset))
    data = response.read()      # a `bytes` object
    # text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
    fh = open('trap-list-'+str(offset)+'.json', 'w')
    fh.write(data)
    fh.close()

def saveCardsFile(offset):
    response = urllib2.urlopen(getCardsJsonUtl(offset))
    data = response.read()      # a `bytes` object
    # text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
    fh = open('card-list-'+str(offset)+'.json', 'w')
    fh.write(data)
    fh.close()

def saveFile(urlCallback,offset,prefix):
    jsonFile = './cardlists/'+prefix+'-list-'+str(offset)+'.json'
    url = urlCallback(offset)
    saveDataToFile(url, jsonFile)
    return jsonFile

    # response = urllib2.urlopen(urlCallback(offset))
    # data = response.read()      # a `bytes` object
    # # text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
    # fh = open(jsonFile, 'w')
    # fh.write(data)
    # fh.close()
    # return jsonFile

CARD_NAME = ""
CARD_STARS = '[[Level]]/[[Rank]]'
CARD_ATK = '[[ATK]]'
CARD_DEF = '[[DEF]]'
CARD_TYPE = '[[Type]]'
CARD_PEN_EFF = '[[Pendulum Effect]]'
CARD_JAP_NAME = 'Japanese name'
CARD_PASSCODE = '[[Passcode]]'
CARD_PRI_TYPE = 'Primary type'
CARD_SEC_TYPE = 'Secondary type'
CARD_ATTR = '[[Attribute]]'
CARD_LORE = '[[Lore]]'
CARD_PEN_SCALE = 'Pendulum Scale'
CARD_IMAGE = 'Card image'
CARD_RIT_SP_REQ = 'Ritual Spell Card required'
CARD_MAT_REQ = 'Materials'
CARD_RIT_MON_REQ = 'Ritual Monster required'
CARD_FUS_MAT_REQ = 'Fusion Material'
CARD_PROPERTY = 'Property'

class JsonDataToCardDataTransformer:
    def transform(i):pass

def download_json_data():
    files=[]
    files += [ saveFile(getSynchroJsonUrl, 0, 'synchro') ]
    files += [ saveFile(getXyzJsonUrl, 0, 'xyz') ]
    files += [ saveFile(getNormalJsonUrl, 0, 'normal') ]
    files += [ saveFile(getNormalJsonUrl, 1, 'normal') ]
    files += [ saveFile(getFusionJsonUrl, 0, 'fusion') ]
    files += [ saveFile(getRitualJsonUrl, 0, 'ritual') ]
    files += [ saveFile(getEffectJsonUrl, 0, 'effect') ]
    files += [ saveFile(getEffectJsonUrl, 500, 'effect') ]
    files += [ saveFile(getEffectJsonUrl, 1000, 'effect') ]
    files += [ saveFile(getEffectJsonUrl, 1500, 'effect') ]
    files += [ saveFile(getEffectJsonUrl, 2000, 'effect') ]
    files += [ saveFile(getEffectJsonUrl, 2500, 'effect') ]
    files += [ saveFile(getEffectJsonUrl, 3000, 'effect') ]
    files += [ saveFile(getPendulumJsonUrl, 0, 'pendulum') ]
    files += [ saveFile(getGeminiJsonUrl, 0, 'gemini') ]
    files += [ saveFile(getTunerJsonUrl, 0, 'tuner') ]
    files += [ saveFile(getSpiritJsonUrl, 0, 'spirit') ]
    files += [ saveFile(getTrapJsonUrl, 0, 'trap') ]
    files += [ saveFile(getTrapJsonUrl, 500, 'trap') ]
    files += [ saveFile(getTrapJsonUrl, 1000, 'trap') ]
    files += [ saveFile(getSpellJsonUrl, 0, 'spell') ]
    files += [ saveFile(getSpellJsonUrl, 500, 'spell') ]
    files += [ saveFile(getSpellJsonUrl, 1000, 'spell') ]
    files += [ saveFile(getSpellJsonUrl, 1500, 'spell') ]
    return files


class BaseTransformer:
    def __init__(self, key):
        self.key = key
    def get(self, f):
        if(self.key in f):
            r = f[self.key]
            if(len(r)==1):
                return r[0]
            elif(len(r)>1):
                print '========'
                print self.key, r
                print '========'
                raise r
        return None

class FullTextTransformer:
    def __init__(self, key):
        self.key = key
    def get(self, f):
        if(self.key in f):
            r = f[self.key]
            if(len(r)==1):
                return r[0]['fulltext']
            elif(len(r)>1):
                print '========'
                print self.key, r
                print '========'
                raise r
        return None


CARD_NAME = "English name"
CARD_STARS = '[[Level]]/[[Rank]]'
CARD_ATK = '[[ATK]]'
CARD_DEF = '[[DEF]]'
CARD_TYPE = '[[Type]]'
CARD_PEN_EFF = '[[Pendulum Effect]]'
CARD_JAP_NAME = 'Japanese name'
CARD_PASSCODE = '[[Passcode]]'
CARD_PRI_TYPE = 'Primary type'
CARD_SEC_TYPE = 'Secondary type'
CARD_ATTR = '[[Attribute]]'
CARD_LORE = '[[Lore]]'
CARD_PEN_SCALE = 'Pendulum Scale'
CARD_IMAGE = 'Card image'
CARD_RIT_SP_REQ = 'Ritual Spell Card required'
CARD_MAT_REQ = 'Materials'
CARD_RIT_MON_REQ = 'Ritual Monster required'
CARD_FUS_MAT_REQ = 'Fusion Material'
CARD_PROPERTY = 'Property'

class Card:
    def __init__(self, json=None):
        self.name = None
        self.type = None
        self.japName = None
        self.attack = None
        self.defense = None
        self.stars = None
        self.pendulumEffect = None
        self.pendulumScale = None
        self.passcode = None
        self.primaryType = None
        self.secondaryType = None
        self.attribute = None
        self.image = None
        self.lore = None
        self.ritualSpellRequired = None
        self.ritualMonstersRequired = None
        self.fusionMaterialsRequired = None
        self.materialsRequired = None
        if(json):
            self.fromJson(json)
    def toJson(self):
        return {
            'name':self.name,
            'type':self.type,
            'japName':self.japName,
            'attack':self.attack,
            'defense':self.defense,
            'stars':self.stars,
            'pendulumEffect':self.pendulumEffect,
            'pendulumScale':self.pendulumScale,
            'passcode':self.passcode,
            'primaryType':self.primaryType,
            'secondaryType':self.secondaryType,
            'attribute':self.attribute,
            'image':self.image,
            'lore':self.lore,
            'ritualSpellRequired':self.ritualSpellRequired,
            'ritualMonstersRequired':self.ritualMonstersRequired,
            'fusionMaterialsRequired':self.fusionMaterialsRequired,
            'materialsRequired':self.materialsRequired,
        }
    def fromJson(self, json):
        for k in json:
            self.__dict__[k] = json[k]
    def __str__(self):
        return str(self.toJson())
    def __repr__(self):
        return str(self.toJson())

class FusionMaterialTransformer:
    def get(self, f):
        if(CARD_FUS_MAT_REQ in f):
            r = f[CARD_FUS_MAT_REQ]
            return map(lambda x:x['fulltext'], r)
        return None

class PrimaryTypeTransformer:
    def get(self, f):
        if(CARD_PRI_TYPE in f):
            r = f[CARD_PRI_TYPE]
            return map(lambda x:x['fulltext'].upper(), r)
        return None

class SecondaryTypeTransformer:
    def get(self, f):
        if(CARD_SEC_TYPE in f):
            r = f[CARD_SEC_TYPE]
            return map(lambda x:x['fulltext'].upper(), r)
        return None

class NameTransformer:
    def get(self, f):
        v = self.__get(f)
        if(v):
            'returning ', v
            return v
        print f
        raise 'No Name Found '
    def __get(self, f):
        if(CARD_NAME in f):
            return f[CARD_NAME][0]
        elif("" in f):
            return f[""][0]
        print 'Error. Returning Noen'

class TypeTransformer:
    def get(self, f):
        if(CARD_TYPE in f):
            r = f[CARD_TYPE]
            if len(r)==0:
                return None
            return map(lambda x:x['fulltext'].upper(), r)[0]
        return None

class PasscodeTransformer:
    def get(self, f):
        if(CARD_PASSCODE in f):
            if(len(f[CARD_PASSCODE])>0):
                r = f[CARD_PASSCODE][0]
                return r
        return None

class PropertyTransformer:
    def __init__(self, key):
        self.key = key
    def get(self, f):
        if(self.key in f):
            r = f[self.key]
            if(len(r)==1):
                return r[0].upper()
            elif(len(r)>1):
                print '========'
                print self.key, r
                print '========'
                raise r
        return None


def pv(po, v, debugNone=False):
    if(v):
        print v
    elif(not v and debugNone):
        print "No Value Found"
        print po
        print ""

def parseFile(f):
    cards = []
    with open(f) as data_file:
        data = json.load(data_file)
        rows = data['rows']
        results = data['results']
        for k in results:
            cardJson = results[k]
            printouts = cardJson['printouts']
            # print printouts
            c = Card()
            c.name = NameTransformer().get(printouts)
            c.attack = BaseTransformer(CARD_ATK).get(printouts)
            c.defense = BaseTransformer(CARD_DEF).get(printouts)
            c.stars = BaseTransformer(CARD_STARS).get(printouts)
            c.type =  TypeTransformer().get(printouts)
            c.primaryType = PrimaryTypeTransformer().get(printouts)
            c.pendulumEffect = BaseTransformer(CARD_PEN_EFF).get(printouts)
            c.japName = BaseTransformer(CARD_JAP_NAME).get(printouts)
            c.passcode = PasscodeTransformer().get(printouts)
            c.secondaryType = SecondaryTypeTransformer().get(printouts)
            c.attribute = FullTextTransformer(CARD_ATTR).get(printouts)
            c.lore =  BaseTransformer(CARD_LORE).get(printouts)
            c.pendulumScale = BaseTransformer(CARD_PEN_SCALE).get(printouts)
            c.image = BaseTransformer(CARD_IMAGE).get(printouts)
            c.ritualSpellRequired = FullTextTransformer(CARD_RIT_SP_REQ).get(printouts)
            c.materialsRequired = BaseTransformer(CARD_MAT_REQ).get(printouts)
            c.fusionMaterialsRequired = FusionMaterialTransformer().get(printouts)
            c.ritualMonstersRequired = BaseTransformer(CARD_RIT_MON_REQ).get(printouts)
            c.property = PropertyTransformer(CARD_PROPERTY).get(printouts)
            # print c.passcode
            # break
            cards.append(c)
    return cards



def writeMasterFile():
    if os.path.exists('master-card-list.json'):
        return
    cards = []
    jsonDataFiles = download_json_data()
    for f in jsonDataFiles:
        cards+=parseFile(f)


    jsonData = json.dumps({'cards':map(lambda c:c.toJson(),cards)})
    fh = open('master-card-list.json', 'w')
    fh.write(jsonData)
    fh.close()


def urlEncodeNonAscii(b):
    return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), b)

def iriToUri(iri):
    parts= urlparse.urlparse(iri)
    return urlparse.urlunparse(
        part.encode('idna') if parti==1 else urlEncodeNonAscii(part.encode('utf-8'))
        for parti, part in enumerate(parts)
    )

def getImageUrl(c, lowres):
    if not c.image:
        return None
    imageHtmlUrl = "http://yugioh.wikia.com/wiki/File:" + c.image
    imageHtmlUrl = iriToUri(imageHtmlUrl)

    print 'parsing... ', imageHtmlUrl
    resource = urllib.urlopen(imageHtmlUrl)
    html = resource.read()

    fa = re.findall("<a.*?href\=.*?download\=\"", html)
    if len(fa)==0:
        return None

    imageUrl = fa[0].split('href=\"')[1].split('"')[0].split("?")[0]
    if lowres:
        imageUrl+="/scale-to-width-down/162"
    imageUrl += '?cb=20170113151913'
    return imageUrl

def saveImageUrls(cards, lowres=True):
    urlList = None
    with open('card-image-url-list.json') as data_file:
        urlList = json.load(data_file)

    lastSave=0
    i=0
    for c in cards:
        i+=1
        if c.image in urlList['imageUrls']:
            continue
        print i, len(cards)
        url = getImageUrl(c, lowres)
        if url:
            urlList['imageUrls'][c.image] = url
        if i-lastSave>10:
            print 'save point ...'
            jsonData = json.dumps(urlList)
            fh = open('card-image-url-list.json', 'w')
            fh.write(jsonData)
            fh.close()
            lastSave=i

    jsonData = json.dumps(urlList)
    fh = open('card-image-url-list.json', 'w')
    fh.write(jsonData)
    fh.close()

def downloadImages(cards, lowres=False):
    i=0
    for c in cards:
        i+=1
        if c.image:
            imagePath = './card_images/'+c.image
            if(lowres):
                imagePath = './card_images_lr/'+c.image

            if os.path.exists(imagePath):
                continue

            imageUrl = getImageUrl(c, lowres)
            if not imageUrl:
                continue

            print i,'/',len(cards)
            print 'downloading... ', imageUrl
            resource = urllib.urlopen(imageUrl)
            imageData = resource.read()

            print 'writing... ', imagePath
            output = open(imagePath,"wb")
            output.write(imageData)
            output.close()

            # imageData.


def readMasterFile():
    data = None
    with open('master-card-list.json') as data_file:
        data = json.load(data_file)
    return map(lambda x:Card(x), data['cards'])


if __name__ == '__main__':
    writeMasterFile()
    cards = readMasterFile()
    # print len(cards)

    c=[]
    # c = filter(lambda x:'Karakuri' in x.name, cards)
    # c = filter(lambda x:'Speedroid' in x.name, cards)
    # c = filter(lambda x:'Mermail' in x.name, cards)
    # c = filter(lambda x:'Phantom' in x.name, cards)
    # c = filter(lambda x:'Symphonic' in x.name, cards)
    # c += filter(lambda x:x.primaryType and 'PENDULUM MONSTER' in x.primaryType, cards)
    # c += filter(lambda x:x.primaryType and 'NORMAL MONSTER' in x.primaryType, cards)
    # c += filter(lambda x:x.primaryType and 'RITUAL MONSTER' in x.primaryType, cards)
    # c += filter(lambda x:x.primaryType and 'FUSION MONSTER' in x.primaryType, cards)
    # c += filter(lambda x:x.primaryType and 'NORMAL MONSTER' in x.primaryType, cards)
    # c += filter(lambda x:x.primaryType and 'XYZ MONSTER' in x.primaryType, cards)
    # c += filter(lambda x:x.primaryType and 'EFFECT MONSTER' in x.primaryType, cards)
    # c += filter(lambda x:x.primaryType and 'SYNCHRO MONSTER' in x.primaryType, cards)
    # c += filter(lambda x:'Geargia' in x.name, cards)
    # c += filter(lambda x:'Gadget' in x.name, cards)
    # c += filter(lambda x:'Cyber Dragon' in x.name, cards)
    # c += filter(lambda x:'Ancient Gear' in x.name, cards)
    # c += filter(lambda x:'Genex' in x.name, cards)
    # c += filter(lambda x:'Atlantean' in x.name, cards)
    # c += filter(lambda x:'Yosenju' in x.name, cards)
    # c += filter(lambda x:'Superheavy' in x.name, cards)
    c += cards
    print len(c)
    # downloadImages(c, True)
    saveImageUrls(c, True)
