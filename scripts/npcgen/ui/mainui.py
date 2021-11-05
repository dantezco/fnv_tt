from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.clock import Clock

MOCK_DATA = ["Deathclaw 1", "Blind Deathclaw", "Ranger Paul Veerhoven", "Ranger Logan", "Ranger Clyde Parker"]


class MainLayout(Screen):
    npc_list = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.npc_list.data = [{'text': str(x)} for x in MOCK_DATA]



class MainuiApp(App):
    def build(self):
        return MainLayout()


if __name__ == "__main__":
    MainuiApp().run()
