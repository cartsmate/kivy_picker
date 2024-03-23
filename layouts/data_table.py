from kivy.metrics import dp
from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.properties import StringProperty

from modules.multi_threading import MultiThreadingPub
from modules.get_data import GetData


class ClassBuiltTable(Screen):
    no_of_pubs = StringProperty("no_of_pubs")

    # def on_pre_enter(self, *args):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "MYdatatable"
        table_data = GetData().get_data()
        data_tables = MDDataTable(
            column_data=[
                ("No.", dp(10)),
                ("Pub Name", dp(45)),
                ("Rank", dp(15)),
                ("Station", dp(30))
            ],
            row_data=table_data,
            sorted_on='Rank',
            sorted_order='ASC',
            use_pagination=True,
            pagination_menu_pos='auto',
            background_color_header="808000",
            rows_num=10
        )
        self.add_widget(data_tables)

    def test_method(self):
        print('INSIDE data table TEST METHOD')
        print(self)

        # self.remove_widget()
        for child in self.children:
            print('child - rd1')
            print(child)

            self.remove_widget(child)

        for child in self.children:
            print('child - rd2')
            print(child)
        table_data2 = GetData().get_data()
        data_tables2 = MDDataTable(
            column_data=[
                ("No2.", dp(10)),
                ("Pub Name2", dp(45)),
                ("Rank2", dp(15)),
                ("Station2", dp(30))
            ],
            row_data=table_data2,
            sorted_on='Rank',
            sorted_order='ASC',
            use_pagination=True,
            pagination_menu_pos='auto',
            background_color_header="808000",
            rows_num=10
        )
        self.add_widget(data_tables2)
        # self.clear_widgets()
        # self.parent.remove_widget(self)

    # def update_table(self):
    #     # self.data_tables.dismiss()
    #     self.data_tables = [(f"{i + 1}", "0", "0", "0") for i in range(4)]
    #     self.data_tables.open()


class PubTable(MDDataTable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # screen = Screen()
        table = MDDataTable(
            column_data=[
                ("#", dp(10)),
                ("Pub Name", dp(40)),
                ("Ranking", dp(15)),
                ("Station", dp(30))
            ]
        )
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        self.add_widget(table)


# class DataTablePub(MDDataTable):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         screen = Screen()
#         table = MDDataTable(
#             column_data = [
#                 ("#", dp(10)),
#                 ("Pub Name", dp(40)),
#                 ("Ranking", dp(15)),
#             ]
#         )
#         screen.add_widget(table)
