import flet as ft
from model import model

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []
        self._current_year= None
        self._current_country=None

    def current_year_set(self,e):
        if e is None: self._current_year=None
        else: self._current_year=e.control.data
    def current_country_set(self,e):
        if e is None: self._current_country=None
        else: self._current_country=e.control.data

    def fillDD(self):
        self._listCountry = self._model.listNations
        self._listYear=self._model.listYears

        for a in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(text=a, data=a, on_click=self.current_year_set))

        for c in self._listCountry:
            self._view.ddcountry.options.append(ft.dropdown.Option(text=c, data=c, on_click=self.current_country_set))

        self._view.update_page()

    def handle_graph(self, e):
        self._model._crea_grafo(self._current_country, self._current_year)

    def handle_volume(self, e):
        pass


    def handle_path(self, e):
        pass
