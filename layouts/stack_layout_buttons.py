from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty
from layouts.data_table import ClassBuiltTable
from kivy.lang import Builder

class StackLayoutQuick(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        image_list = ['brunch.jpeg', 'favourite.png', 'garden.png', 'quiz.png', 'roast.png', 'sport.png', 'music.png']
        for i in range(0, 7):
            b = Button(background_normal=f"images/icons/{image_list[i]}",
                       #background_color= (1, .3, .4, .85),
                       size_hint=(None, None),
                       size=(dp(50), dp(50)),
                       padding=(dp(50), dp(50), dp(50), dp(50)))
            self.add_widget(b)


class StackBtns(StackLayout):
    list_of_pubs = StringProperty("list_of_pubs")
    actual_list = []

    def on_press_update(self):
        print('update pressed - PRE')
        ClassBuiltTable().test_method()
        # Builder.load_file('kv_files/KivyPub_20240322.kv')
        print('update pressed - POST')

    def on_toggle_button(self, widget, id):
        print(f"{id} button clicked", widget.state)
        if widget.state == 'normal':
            # widget.text = 'ON'
            self.actual_list.remove(id)
        else:
            # widget.text = 'OFF'
            self.actual_list.append(id)
        self.list_of_pubs = str(self.actual_list)


# class StackLayoutPub(StackLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         for i in range(0, 100):
#             b = Button(text=str(i+1), size_hint=(None, None), size=(dp(100), dp(100)))
#             self.add_widget(b)
