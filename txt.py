class txt:
    def __init__(self):
        pass

    def openFile(self, fileName, mode):
        self.f = open(fileName, mode)
    
    def lisToStr(self, lis):
        string = ''
        for i in lis:
            string = string + ' ' + str(i)
        return string
        
    def writeDBtoFile(self, db):
        lines = []
        for i in db:
            player = db[i]
            lines.append(i + '\n')
            print(self.lisToStr(player[0]))
            lines.append(self.lisToStr(player[0]) + ' \n')
            lines.append(self.lisToStr(player[1]) + ' \n')
        self.f.writelines(lines)
    
    def strToLis(self, string):
        list = []
        temp = ''
        for i in string:
            if i == ' ':
                list.append(temp)
                temp = ''
            else:
                temp = temp + i
        if len(list) != 0:
            list.pop(0)
        return list

    def readFile(self, file):
        file = self.openFile(file, 'r')
        result = {}
        ind = 1
        name = ''
        for i in self.f:
            print(ind)
            if ind == 1:
                result[i.rstrip()] = [[], []]
                name = i.rstrip()
                ind += 1
            elif ind == 2:
                result[name][0] = self.strToLis(i)
                ind += 1
            else:
                result[name][1] = self.strToLis(i)
                ind = 1
        return result