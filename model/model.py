import networkx as nx

from database.DAO import DAO
from model.retailer import Retailer


class Model:
    def __init__(self):
        self._allnations=None
        self._load_all_nations()
        self._allyears=None
        self._load_all_years()
        self._graph = nx.Graph()
        self._retailers=None
        self._archi=[]

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
        self._crea_archi(country, year, self._retailers)
        print(f"Ho appena creato un grafo!! {self._graph}")
        return self._graph

    #dovrei farlo con la lista delle vendite
    def _crea_archi(self, country, year, retailers):
        curr=DAO.get_items_sold_by_retailer(country, year)
        A=None
        B=None
        for element in curr:
            print(element.id)
            for i in retailers:
                if i.Retailer_code==element.ret1:
                    A=i
                if i.Retailer_code==element.ret2:
                    B=i
            if A is not None and B is not None:
                self._graph.add_edge(A, B)
