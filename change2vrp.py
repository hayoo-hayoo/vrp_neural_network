def change2vrp(Route,nodeneedarray,cap):
    fRoute = []
    sum = 0
    for i in range(len(Route)):
        j = Route[i]
        sum += nodeneedarray[j].need
        if sum > cap:
            fRoute.append(0)
            fRoute.append(j)
            sum = 0
        else:
            fRoute.append(j)

    return fRoute

class nodeneed:
    def __init__(self,nood,need):
        self.node = nood
        self.need = need