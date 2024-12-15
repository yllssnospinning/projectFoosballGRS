from grs import grs
from txt import txt
grs = grs(25)
grs.loadGames('C:\\Users\\PC\\Desktop\\Trading Sim\\GRS\\scores.txt')
fileHandler = txt()
import matplotlib.pyplot as plt

players = {}
iHist = []
db = {}
for i in range(0, len(grs.db)):
    print(i)
    db = grs.compute(i, 30)
    inflation = 0
    for ii in db:
        ratings = [db[k][0] for k in db]
        inflation = (sum(ratings) / len(ratings)) - 1500
        if ii in players:
            p = players[ii]
            p[0].append(i)
            p[1].append(db[ii][0])
            p[2].append(db[ii][1])
        else:
            players[ii] = [[i], [db[ii][0]], [db[ii][1]]]
    iHist.append(inflation)

fileHandler.openFile('C:\\Users\\PC\\Desktop\\Trading Sim\\GRS\\test.txt', 'w')
fileHandler.writeDBtoFile(players)