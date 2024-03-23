from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from functools import partial

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

# from kivymd.uix.screenmanager import ScreenManager

from layouts.box_layout_header import BoxLayoutHeader
from layouts.box_layout_search import BoxLayoutSearch
from layouts.data_table import *
from layouts.grid_layout_images import GridLayout
from layouts.map_view import MapView
from layouts.stack_layout_buttons import StackBtns
from kivy.uix.stacklayout import StackLayout
from layouts.widgets import BoxLayoutPub

from modules.multi_threading import MultiThreadingPub
from modules.get_data import GetData


class MainWindow(Screen):
    pass


class MapWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


# class AppBuilder(MDApp):
#     def build(self):
#         kv = Builder.load_file('kv_files/KivyPub_20240322.kv')
#         return kv
#
#
# if __name__ == "__main__":
#     AppBuilder().run()

# Builder.load_string('''
# <TestButton>:
#     text: "Submit"
#     on_press: root.click_button()
# ''')


# class TestButton(Button):
#
#     # def click_button(self):
#     #     print('button clicked')
#     #     print(self)
#
#     pass

class TestScreen(Screen):
    # list_of_filters = StringProperty("list_of_filters")
    # filters_list = []
    #
    # def on_state(self, tb, id):
    #     print('ON STATE - screen')
    #     print(tb)
    #     print(id)
    #     print(tb.state)
    #     if tb.state == 'normal':
    #         # widget.text = 'ON'
    #         self.filters_list.remove(id)
    #     else:
    #         # widget.text = 'OFF'
    #         self.filters_list.append(id)
    #     self.list_of_filters = str(self.filters_list)
    #     print(self.list_of_filters)
    #     TestDataTable.table_update(self.filters_list)
    #     # TestDataTable.target = self.list_of_filters
    #
    # def press(self, instance):
    #     print('SCREEN PRINT')
    #
    # def test_child(self):
    #     print('INSIDE data table TEST child METHOD')
    #     print(self)
    #
    #     # self.remove_widget()
    #     for child in self.children:
    #         print('child - rd1')
    #         print(child)

    pass

# class TestToggleButton(ToggleButton):
#     def on_toggle(self):
#         print('TOGGLE ON')
#         print(self)
#     pass

class TestDataTable(MDDataTable):
    target = ObjectProperty()

    list_of_pubs = StringProperty("list_of_pubs")
    actual_list = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        row_datas = GetData().get_data_all()
        # self.column_data = [
        #                   ("No.", dp(15)),
        #                   ("Pub Name", dp(65)),
        #                   ("Ranking", dp(25)),
        #                   ("Station", dp(50)),
        #               ],
        self.row_data = row_datas

    # def press(self, instance):
    #     print('TABLE PRINT')
    #     self.row_data = GetData().get_data_entertain()
    #
    # def press2(self, instance):
    #     print('TABLE PRINT2')
    #     self.row_data = GetData().get_data_favourite()

    # def on_toggle_filter(self, widget, id):
    #     print('INSIDER toggle filter')
    #     print(f"{id} button clicked", widget)
    #     # if widget.state == 'normal':
    #     #     # widget.text = 'ON'
    #     #     self.actual_list.remove(id)
    #     # else:
    #     #     # widget.text = 'OFF'
    #     #     self.actual_list.append(id)
    #     # self.list_of_pubs = str(self.actual_list)
    #
    # def table_update(self, list_):
    #     print(list_)

    # def on_toggle_entertain(self, instance, id):
    #     print('TABLE TOGGLE entertain')
    #     print('instance', instance)
    #     if instance in self.actual_list:
    #         self.actual_list.remove(instance)
    #     else:
    #         self.actual_list.append(instance)
    #     self.list_of_pubs = str(self.actual_list)
    #     print('actual_list', str(self.actual_list))
    #     print('list_of_pubs', str(self.list_of_pubs))
    #     # self.row_data = GetData().get_data_entertain()
    #     self.row_data = GetData().get_data_filter(self.actual_list)
    #
    # def on_toggle_favourite(self, instance, id):
    #     print('TABLE TOGGLE favourite')
    #     print('instance', instance)
    #     if instance in self.actual_list:
    #         self.actual_list.remove(instance)
    #     else:
    #         self.actual_list.append(instance)
    #     self.list_of_pubs = str(self.actual_list)
    #     print('actual_list', str(self.actual_list))
    #     print('list_of_pubs', str(self.list_of_pubs))
    #     # self.row_data = GetData().get_data_favourite()
    #     self.row_data = GetData().get_data_filter(self.actual_list)
    #
    # def on_toggle_garden(self, instance, id):
    #     print('TABLE TOGGLE garden')
    #     print('instance', instance)
    #     if instance in self.actual_list:
    #         self.actual_list.remove(instance)
    #     else:
    #         self.actual_list.append(instance)
    #     self.list_of_pubs = str(self.actual_list)
    #     print('actual_list', str(self.actual_list))
    #     print('list_of_pubs', str(self.list_of_pubs))
    #     # self.row_data = GetData().get_data_garden()
    #     self.row_data = GetData().get_data_filter(self.actual_list)
    #
    # def on_toggle_music(self, instance, id):
    #     print('TABLE TOGGLE music')
    #     print('instance', instance)
    #     if instance in self.actual_list:
    #         self.actual_list.remove(instance)
    #     else:
    #         self.actual_list.append(instance)
    #     self.list_of_pubs = str(self.actual_list)
    #     print('actual_list', str(self.actual_list))
    #     print('list_of_pubs', str(self.list_of_pubs))
    #     # self.row_data = GetData().get_data_music()
    #     self.row_data = GetData().get_data_filter(self.actual_list)
    #
    # def on_toggle_quiz(self, instance, id):
    #     print('TABLE TOGGLE quiz')
    #     print('instance', instance)
    #     if instance in self.actual_list:
    #         self.actual_list.remove(instance)
    #     else:
    #         self.actual_list.append(instance)
    #     self.list_of_pubs = str(self.actual_list)
    #     print('actual_list', str(self.actual_list))
    #     print('list_of_pubs', str(self.list_of_pubs))
    #     # self.row_data = GetData().get_data_quiz()
    #     self.row_data = GetData().get_data_filter(self.actual_list)
    #
    # def on_toggle_roast(self, instance, id):
    #     print('TABLE TOGGLE roast')
    #     print('instance', instance)
    #     if instance in self.actual_list:
    #         self.actual_list.remove(instance)
    #     else:
    #         self.actual_list.append(instance)
    #     self.list_of_pubs = str(self.actual_list)
    #     print('actual_list', str(self.actual_list))
    #     print('list_of_pubs', str(self.list_of_pubs))
    #     # self.row_data = GetData().get_data_roast()
    #     self.row_data = GetData().get_data_filter(self.actual_list)
    #
    # def on_toggle_sport(self, instance, id):
    #     print('TABLE TOGGLE sport')
    #     print('instance', instance)
    #     if instance in self.actual_list:
    #         self.actual_list.remove(instance)
    #     else:
    #         self.actual_list.append(instance)
    #     self.list_of_pubs = str(self.actual_list)
    #     print('actual_list', str(self.actual_list))
    #     print('list_of_pubs', str(self.list_of_pubs))
    #     # self.row_data = GetData().get_data_sport(actual_list)
    #     self.row_data = GetData().get_data_filter(self.actual_list)

    def on_toggle_xxx(self, instance, id):
        print('TABLE TOGGLE xxx')
        print('instance', instance)
        if instance in self.actual_list:
            self.actual_list.remove(instance)
        else:
            self.actual_list.append(instance)
        self.list_of_pubs = str(self.actual_list)
        # print('actual_list', str(self.actual_list))
        # print('list_of_pubs', str(self.list_of_pubs))
        # self.row_data = GetData().get_data_sport(actual_list)
        self.row_data = GetData().get_data_filter(self.actual_list)

    # def stack_btn(self, instance):
    #     print('STACK BTN')
    #
    # def on_state(self, tb):
    #     print('ON STATE - tables')
    #     print(tb)
    #     print(tb.id)
    #     print(tb.on_state)

    pass

# class EntertainToggleButton(ToggleButton):
#
#     def on_state_entertain(self, instance, id):
#         print(f'{id}on state ETB')
#         # print(instance)
#         if instance.state == 'normal':
#             # widget.text = 'ON'
#             print('norm')
#             # self.filters_list.remove(id)
#         else:
#             print('down')
#             # widget.text = 'OFF'
#             # self.filters_list.append(id)
#     pass

class BoxerLayout0(BoxLayout):
    pass
class BoxerLayout1(BoxLayout):
    pass
class StackerLayout(StackLayout):
    pass
class GriderLayout(GridLayout):
    pass
class TestImage(Image):
    pass
class FilterBox(BoxLayout):
    pass

class Example(MDApp):


    # def press(self, instance):
    #     print("PRESSED")
    #     print(self.__dict__)
    #     print(self.root)
    #     for child in self.root.children:
    #         print(child)

    def build(self):

        Builder.load_file('kv_files/Kivy_CustomToggle.kv')
        screen = TestScreen()
        layout = FilterBox(orientation='vertical')
        screen.add_widget(layout)

        data_tables = TestDataTable(column_data=[
            ("No.", dp(15)),
            ("Pub Name", dp(65)),
            ("Ranking", dp(25)),
            ("Station", dp(50))])

        bigbox = BoxLayout(orientation='horizontal', padding=20, spacing=20)

        quick_list = ['entertain', 'favourite', 'garden', 'music', 'quiz', 'roast', 'sport']

        for quick in quick_list:
            box10 = BoxLayout(orientation="vertical")
            image10 = TestImage(source=f'images/icons/{quick}.png')
            btn10 = ToggleButton(text=f'{quick}')
            btn10.bind(on_press=partial(data_tables.on_toggle_xxx, quick))
            box10.add_widget(image10)
            box10.add_widget(btn10)
            bigbox.add_widget(box10)

        # box0 = BoxLayout(orientation="vertical")
        # image0 = TestImage(source='images/icons/entertain.png')
        # btn0 = ToggleButton(text='entertain')
        # btn0.bind(on_press=partial(data_tables.on_toggle_xxx, 'entertain'))
        # box0.add_widget(image0)
        # box0.add_widget(btn0)
        # bigbox.add_widget(box0)
        #
        # box1 = BoxLayout(orientation="vertical")
        # image1 = TestImage(source='images/icons/favourite.png')
        # btn1 = ToggleButton(text='favourite')
        # btn1.bind(on_press=partial(data_tables.on_toggle_xxx, 'favourite'))
        # box1.add_widget(image1)
        # box1.add_widget(btn1)
        # bigbox.add_widget(box1)
        #
        # box2 = BoxLayout(orientation="vertical")
        # image2 = TestImage(source='images/icons/garden.png')
        # btn2 = ToggleButton(text='garden')
        # btn2.bind(on_press=partial(data_tables.on_toggle_xxx, 'garden'))
        # box2.add_widget(image2)
        # box2.add_widget(btn2)
        # bigbox.add_widget(box2)
        #
        # box3 = BoxLayout(orientation="vertical")
        # image3 = TestImage(source='images/icons/music.png')
        # btn3 = ToggleButton(text='music')
        # btn3.bind(on_press=partial(data_tables.on_toggle_xxx, 'music'))
        # box3.add_widget(image3)
        # box3.add_widget(btn3)
        # bigbox.add_widget(box3)
        #
        # box4 = BoxLayout(orientation="vertical")
        # image4 = TestImage(source='images/icons/quiz.png')
        # btn4 = ToggleButton(text='quiz')
        # btn4.bind(on_press=partial(data_tables.on_toggle_xxx, 'quiz'))
        # box4.add_widget(image4)
        # box4.add_widget(btn4)
        # bigbox.add_widget(box4)
        #
        # box5 = BoxLayout(orientation="vertical")
        # image5 = TestImage(source='images/icons/roast.png')
        # btn5 = ToggleButton(text='roast')
        # btn5.bind(on_press=partial(data_tables.on_toggle_xxx, 'roast'))
        # box5.add_widget(image5)
        # box5.add_widget(btn5)
        # bigbox.add_widget(box5)
        #
        # box6 = BoxLayout(orientation="vertical")
        # image6 = TestImage(source='images/icons/sport.png')
        # btn6 = ToggleButton(text='sport')
        # btn6.bind(on_press=partial(data_tables.on_toggle_xxx, 'sport'))
        # box6.add_widget(image6)
        # box6.add_widget(btn6)
        # bigbox.add_widget(box6)

        layout.add_widget(bigbox)

        # total_count = len(data_tables.row_data)
        # heading = Label(text=str(total_count), color=(1, 0, 0, 1))
        # layout.add_widget(heading)

        layout.add_widget(data_tables)

        return screen

    # def on_start(self):
    #     self.data_tables


Example().run()
