from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.properties import ObjectProperty, NumericProperty
from kivy.core.image import Image as CoreImage
from kivy.core.image import ImageData
from kivy.lang import Builder
from kivy.uix.scatterlayout import ScatterLayout, Scatter


# Declare both screens
class TitleScreen(Screen):
    def __init__(self, **kwargs):
        super(TitleScreen, self).__init__(**kwargs)


class LoadingMainScreen(Screen):
    def __init__(self, **kwargs):
        super(LoadingMainScreen, self).__init__(**kwargs)


class ScatterBack(Scatter):
    def __init__(self, **kwargs):
        super(ScatterBack, self).__init__(**kwargs)


class MyImage(Image):
    def __init__(self, **kwargs):
        super(MyImage, self).__init__(**kwargs)
        print("Init MyImage size:", self.size)

        # self.bind(height=self.update_image)
        self.bind(source=self.update_source)
        self.bind(pos=self.update_pos)

    def update_pos(self, *args):
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        print(self.get_root_window())

    def update_image(self, *args):
        self.height = Window.size[1]
        print("Update_Image size:", self.size)

    def update_source(self, *args):
        self.source = self.source
        im = CoreImage(self.source)
        print("Update_Source 1 Image size:", im.size)
        ratio = Window.size[1]/im.size[1]
        self.size = (ratio*im.size[0], ratio*im.size[1])
        print("Update_Source 2 Image size:", im.size)


class FireEmblem_copyApp(App):
    def build(self):
        Builder.load_file("fireemblem_copy.kv")

        Window.size = (288, 513)
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(TitleScreen(name='title'))
        sm.add_widget(LoadingMainScreen(name='loading_main'))

        return sm


if __name__ == '__main__':
    FireEmblem_copyApp().run()



