import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.selectedAlbum = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDD(self,nodi):
        nodiDD=list(map(lambda x: ft.dropdown.Option(key=x.Title,data=x,on_click=self.getSelectedAlbum),nodi))
        self._view.ddAlbum.options=nodiDD
        self._view.update_page()
        pass


    def handleCreaGrafo(self,e):
        self._view.txtResult.clean()

        try:
            intDurata=int(self._view.txtDurata.value)
        except ValueError:
            self._view.create_alert("Valore non numerico")
            return

        nodi = self._model.creaGrafo(intDurata)
        self._view.txtResult.controls.append(ft.Text(f"Grafo creato"))
        n,a=self._model.getDetails()
        self._view.txtResult.controls.append(ft.Text(f"Nodi: {n}. Archi: {a}"))
        self.fillDD(nodi)
        self._view.update_page()

        pass

    def handleAnalisi(self,e):
        l,s=self._model.analisi(self.selectedAlbum)
        self._view.txtResult.controls.append(ft.Text(f"Componente connessa di {self.selectedAlbum}"))
        self._view.txtResult.controls.append(ft.Text(f"Dimensione: {l}"))
        self._view.txtResult.controls.append(ft.Text(f"Somma durate: {s}"))
        self._view.update_page()
        pass

    def handleSet(self,e):

        try:
            intSoglia=int(self._view.txtSoglia.value)
        except ValueError:
            self._view.create_alert("Valore non numerico")
            return

        set,d=self._model.cammino(intSoglia, self.selectedAlbum)

        self._view.txtResult.controls.append(ft.Text(f""))
        self._view.txtResult.controls.append(ft.Text(f"Set di lunghezza max di {self.selectedAlbum}: "))
        self._view.txtResult.controls.append(ft.Text(f"Lunghezza max {len(set)}"))
        self._view.txtResult.controls.append(ft.Text(f"Durata: {d}"))

        for a in set:
            self._view.txtResult.controls.append(ft.Text(f"{a}"))
        self._view.update_page()
        pass


    def getSelectedAlbum(self,e):
        if e.control.data is None:
            pass
        else:
            self.selectedAlbum=e.control.data
