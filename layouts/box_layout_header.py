from kivy.uix.boxlayout import BoxLayout


class BoxLayoutHeader(BoxLayout):

    def on_switch_active(self, switch):
        print('switch', str(switch.active))

    def on_toggle_button_state(self, widget):
        print("toggle button clicked", widget.state)
        if widget.state == 'normal':
            widget.text = 'ON'
        else: #'down'
            widget.text = 'OFF'

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="C")
    #     self.add_widget(b1)
    #     self.add_widget(b3)
    #     self.add_widget(b2)