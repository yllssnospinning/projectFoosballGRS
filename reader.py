class reader:
    def __init__(self):
        pass
    
    def seperateBySpaces(self, strIn):
        result = []
        temp = ''
        for i in strIn:
            if i == ' ':
                if not result == '\\n':
                    # print(temp)
                    result.append(temp)
                temp = ''
            else:
                temp = temp + i
        # if len(temp) != 0 and not temp == '\\n':
            # result.append(temp)
        return result
    
    def readGame(self, strIn):
        lisIn = self.seperateBySpaces(strIn)
        print(lisIn)
        teams = []
        results = []
        temp = []
        for i in lisIn:
            if not i == '/':
                temp.append(i)
            else:
                results.append(temp.pop(len(temp) - 1))
                teams.append(temp)
                temp = []
        return results, teams
    
    def readLegacyGame(self, strIn):
        lisIn = self.seperateBySpaces(strIn)
        stage = 1
        temp = []
        teams = []
        result = 0
        for i in lisIn:
            if i == '/':
                if len(temp) != 0:
                    teams.append(temp)
                    temp = []
                stage += 1
            else:
                if stage <= 2:
                    temp.append(i)
                else:
                    result = i
                    break
        return [teams, [int(result), 1 - int(result)]]