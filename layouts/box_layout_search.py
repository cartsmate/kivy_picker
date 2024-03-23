from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutSearch(BoxLayout):
    assigned_text = StringProperty("Search - placeholder")
    slider_value = StringProperty("value")
    text_input = StringProperty("name")

    def on_search_click(self):
        print("search button clicked")
        self.assigned_text = "Search Results"

    def on_value_slide(self, slider):
        print("slider value", slider.value)
        self.slider_value = str(int(slider.value))

    def on_text_validate(self, text_input):
        self.text_input = text_input.text
