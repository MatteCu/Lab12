from database.DAO import DAO

class Model:
    def __init__(self):
        self._allnations=None
        self._load_all_nations()
        self._allyears=None
        self._load_all_years()
        pass
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
