class grs:
    def __init__(self, smoothingLimit):
        from eval import Eval
        from reader import reader
        self.r = reader()
        self.e = Eval()
        self.l1, self.l2 = {}, {}
        self.maPeriod = smoothingLimit
    
    def setPlayer(self, playerName, new):
        if playerName in self.l1:
            player = self.l1[playerName]
            player[0] = new[0]
            player[1].append(new[1])
            while len(player[1]) > self.maPeriod:
                player[1].pop(0)
        else:
            self.l1[playerName] = [new[0], [0 for i in range(0, self.maPeriod - 1)]]
            self.l1[playerName][1].append(new[1])
    
    def getPlayer(self, playerName, db):
        if playerName in db:
            player = db[playerName]
            return [player[0], sum(player[1]) / len(player[1])]
        else:
            return [1500, 0]
    
    def getTeam(self, team, layer):
        ply = self.l1 if layer == 1 else self.l2
        tLis = []
        temp = []
        for t in team:
            for p in t:
                temp.append(self.getPlayer(p, ply))
            tLis.append(temp)
            temp = []
        return tLis
    
    def getFoci(self, team):
        foci = []
        name = []
        for ft, t in enumerate(team):
            for fp, p in enumerate(t):
                foci.append([ft, fp])
                name.append(p)
        return foci, name
    
    def computeGame(self, game):
        players = game[0]
        results = game[1]
        tl1, tl2 = self.getTeam(players, 1), self.getTeam(players, 2)
        foci = self.getFoci(players)
        newP = []
        for i in foci[0]:
            newP.append(self.e.evaluateGame(tl1, tl2, results, i[0], i[1]))
        for i, ii in enumerate(newP):
            self.setPlayer(foci[1][i], ii)
        
    def loadGames(self, fileName):
        f = open(fileName)
        self.db = []
        for i in f:
            self.db.append(self.r.readLegacyGame(i))
    
    def compute(self, no, depth):
        prevDB = self.db
        for i in range(0, depth):
            # print(str(i + 1), 'out of', str(depth))
            for ii, iii in enumerate(self.db):
                self.computeGame(iii)
                if ii >= no:
                    break
            self.l2 = self.l1
            self.l1 = {}
            if not prevDB == self.db:
                1 / 0
            prevDB = self.db
        players = {}
        for i in self.l2:
            players[i] = self.getPlayer(i, self.l2)
        return players
        

