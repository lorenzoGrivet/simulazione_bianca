import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.soglia = 0
        self._grafo=nx.Graph()
        self.idMap={}
        self.maxLen=None
        self.solBest=None

    def creaGrafo(self,durata):
        self._grafo.clear()
        nodi=DAO.getAlbum(durata)
        self._grafo.add_nodes_from(nodi)
        for a in nodi:
            self.idMap[a.AlbumId]=a
        archi=DAO.getArchi(durata)
        for a in archi:
            self._grafo.add_edge(self.idMap[a[0]], self.idMap[a[1]])
        return nodi

    def analisi(self,nodo):
        comp= list(nx.node_connected_component(self._grafo, nodo))
        somma=0
        for a in comp:
            somma+=a.durata
        return len(comp),somma

    def getDetails(self):
        return len(self._grafo.nodes),len(self._grafo.edges)


    def cammino(self,soglia,start):
        self.solBest=[]
        self.maxLen=0
        self.soglia=soglia
        parziale=[start]
        self.ricorsione(parziale,start)
        # print(self.maxLen,self.solBest)
        # print(self.getDurata(self.solBest))
        return self.solBest, self.getDurata(self.solBest)


    def ricorsione(self,parziale,start):
        succ=list(self._grafo.neighbors(start))
        ammissibili = self.getAmmissibili(succ,parziale)

        if self.isTerminale(ammissibili):
            if len(parziale)>self.maxLen:
                self.solBest=copy.deepcopy(parziale)
                self.maxLen=len(parziale)
        else:
            for a in ammissibili:
                parziale.append(a)
                self.ricorsione(parziale,a)
                parziale.pop()


        pass

    def getAmmissibili(self,succ,parziale):
        amm=[]
        dTot=self.getDurata(parziale)

        for a in succ:
            if a not in parziale:
               if a.durata<(self.soglia-dTot):
                    amm.append(a)
        return amm

    def getDurata(self,parziale):
        somma=0
        for a in parziale:
            somma+=a.durata
        return somma

    def isTerminale(self, ammissibili):
        if len(ammissibili)==0:
            return True

        pass