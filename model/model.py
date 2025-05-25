import networkx as nx

from database.DAO import DAO
from model.retailer import Retailer
from UI.controller import Controller


class Tupla_volumi:
    def __init__(self, C, N, V):
        self.retC = C
        self.retN = N
        self.retV = V

    def __eq__(self, other):
        return self.retV == other.retV

    def __lt__(self, other):
        return self.retV < other.retV

class Model:
    def __init__(self):
        self._allnations=None
        self._load_all_nations()
        self._allyears=None
        self._load_all_years()
        self._graph = nx.Graph()
        self._retailers=None
        self._archi=[]
        self._controller=Controller
        self.x = 0
        self.soluzioni=[]

    def _load_all_nations(self):
        self._allnations=DAO.get_all_nations()
        print(self._allnations)
    @property
    def listNations(self):
        return self._allnations
    @property
    def listYears(self):
        return self._allyears


    def _load_all_years(self):
        self._allyears=DAO.get_all_years()
        pass

    def _crea_grafo(self, country, year):
        self._retailers = DAO.get_retailers_fromcnt(country)
        for ret in self._retailers:
            print(f"{ret}\n")
        self._graph.add_nodes_from(self._retailers)
        print ("test")
        self._crea_archi( year, self._retailers)
        #self._controller.update_graph_text(self, f"Ho appena creato un grafo!! {self._graph}")
        print(f"Ho appena creato un grafo!! {self._graph}")
        '''
        qui la cosa si fa complicata, perché self.graph.edges indica un dizionario con tutti gli archi a cui é associato
        un peso che é un altro dizionario, quindi devo spacchettare tutto (tutti i edg in grafo sono gli edges tra due nodi di cui uno iniziale definito
        e poi devo accedere al parametro weight 
        '''
        '''for retA in self._retailers:
            for edg in self._graph.edges([retA],data=True):
                print (edg[2]['weight'])
        '''

        return self._graph


    def calcola_percorso(self,n_nodi):
        parziale = [[]]
        livello=0
        self.ricorsivo(livello,n_nodi,parziale)
        for sol in self.soluzioni:
            print(sol)

    def ricorsivo(self, livelloN, archiMax, parziale):
        temp=[]
        if livelloN<archiMax:
            livelloN+=1
            print(livelloN)
            retpool=self._retailers
            for p in parziale:
                print ('PARZIALEEE')
                print(p)
                for n in retpool:
                    if n not in p:
                        p.append(n)
                        retpool.pop(0)
                        parziale.append(p)
                        break


            print('HELOOOOO')
            self.ricorsivo(livelloN, archiMax,parziale)
        else:
            self.soluzioni=parziale




    def get_volumi(self):
        result=[]
        for ret in self._retailers:
            if self._calcola_volume(ret)>0:
                print(f'Il volume del retailer {ret.Retailer_name} é di {self._calcola_volume(ret)}')
                x=Tupla_volumi(ret.Retailer_code, ret.Retailer_name, self._calcola_volume(ret))
                result.append(x)
        result.sort(reverse=True)
        return result


    #dovrei farlo con la lista delle vendite
    def _crea_archi(self, year, retailers):
        peso=None
        for retA in retailers:
            for retB in retailers:
                if not retA==retB:
                    peso=DAO.items_n_two_vendors(retA.Retailer_code, retB.Retailer_code, year)
                if peso is not None and peso > 0 and self._graph.has_edge(retA,retB)==False:
                    self._graph.add_edge(retA, retB, weight=peso)

    def _calcola_volume(self,nodo_ini: Retailer):
        volume=0
        for edg in self._graph.edges([nodo_ini], data=True):
            volume+=edg[2]['weight']
        return volume

"""     curr=DAO.get_items_sold_by_retailer(country, year)
        A=None
        B=None
        for element in curr:
            for i in retailers:
                if i.Retailer_code==element.ret1:
                    A=i
                if i.Retailer_code==element.ret2:
                    B=i
            if A is not None and B is not None:
                self._graph.add_edge(A, B, weight=1)"""
