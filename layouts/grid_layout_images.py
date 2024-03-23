from kivy.metrics import dp
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout


class ImageLayoutQuick(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        image_list = ['entertain.png', 'favourite.png', 'garden.png', 'quiz.png', 'roast.png', 'sport.png', 'music.png']
        for i in range(0, 7):
            # b = Image(text=str(i+1), size_hint=(None, None), size=(dp(40), dp(100)), source=f"images/icons/{image_list[i]}")
            b = Image(source=f"images/icons/{image_list[i]}", size_hint=(None, None), size=(dp(40), dp(100)), keep_ratio=True)
            self.add_widget(b)
