
class Eval:
    def __init__(self):
        import copy as c
        self.c = c

    def focusGame(self, l1, l2, results, ft, fp):
        if l2 == {}:
            print(666)
            team = l1
        else:
            team = l2
            team[ft][fp] = l1[ft][fp]
        team.insert(0, team.pop(ft))
        team[0].insert(0, team[0].pop(fp))
        r = results
        r.insert(0, r.pop(ft))
        return team, r

    def evaluateGame(self, l1, l2, results, ft, fp):
        ply1, ply2, res = self.c.deepcopy(l1), self.c.deepcopy(l2), self.c.deepcopy(results)
        team, result = self.focusGame(ply1, ply2, res, ft, fp)
        result = [i / sum(result) for i in result]
        mPn, pR, tR, cR, pV = 0, 0, 0, 0, 0
        pDr = 0
        for i, t in enumerate(team):
            if len(t) > mPn:
                mPn = len(t)
            for ii, p in enumerate(t):
                rating = 10 ** (p[0] / 400)
                cR += rating
                if i == 0:
                    tR += rating
                    if ii == 0:
                        pR += rating
                        pDr = p[0]
                        pV = p[1]
        kFactor = (10 + 100 * abs(pV)) * mPn
        winProb = tR / cR
        contribution = pR / tR
        deviation = result[0] - winProb
        teamDelta = kFactor * deviation
        playerDelta = contribution * teamDelta
        newPr = pDr + playerDelta
        return newPr, deviation 