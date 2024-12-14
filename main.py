from grs import grs
grs = grs(50)
grs.loadGames('C:\\Users\\PC\\Desktop\\Trading Sim\\GRS\\scores.txt')
import matplotlib.pyplot as plt

players = {}
for i in range(0, len(grs.db)):
    print(i)
    db = grs.compute(i, 3)
    for ii in db:
        if ii in players:
            p = players[ii]
            p[0].append(i)
            p[1].append(db[ii][0])
            p[2].append(db[ii][1])
        else:
            players[ii] = [[i], [db[ii][0]], [db[ii][1]]]

fig, ax = plt.subplots()
player = players['YCL']
ax2 = ax.twinx()
ax.plot(player[0], player[1])
ax2.plot(player[0], player[2], color = 'black')
fig.dpi = 1500
plt.show()