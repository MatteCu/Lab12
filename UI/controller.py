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

    def fillDD(self):
        self._listCountry = self._model.listNations
        self._listYear=self._model.listYears

        for a in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(a))

        for c in self._listCountry:
            self._view.ddcountry.options.append(ft.dropdown.Option(c))

        self._view.update_page()
        pass


    def handle_graph(self, e):
        pass



    def handle_volume(self, e):
        pass


    def handle_path(self, e):
        pass
