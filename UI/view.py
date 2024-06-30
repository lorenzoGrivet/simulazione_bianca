import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._btnGrafo = None
        self.txtDurata = None
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None



    def load_interface(self):

        self._title = ft.Text("Simulazione esame", color="blue", size=24)
        self._page.add(self._title)

        #row1
        self.txtDurata=ft.TextField(label="Durata")
        self._btnGrafo=ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handleCreaGrafo)
        row1=ft.Row([ft.Container(self.txtDurata,width=500), ft.Container(self._btnGrafo, width=300)], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1)

        #row2
        self.ddAlbum=ft.Dropdown(label="Album")
        self.btnAnalisi=ft.ElevatedButton(text="Analisi Componente",on_click=self._controller.handleAnalisi)
        row2 = ft.Row([ft.Container(self.ddAlbum, width=500), ft.Container(self.btnAnalisi, width=300)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)


        #row3
        self.txtSoglia = ft.TextField(label="Soglia")
        self.btnSet = ft.ElevatedButton(text="Set di album", on_click=self._controller.handleSet)
        row3 = ft.Row([ft.Container(self.txtSoglia, width=500), ft.Container(self.btnSet, width=300)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row3)

        #row4
        self.txtResult = ft.ListView(auto_scroll=True,expand=True)
        self._page.add(self.txtResult)

        self.update_page()



        pass

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
