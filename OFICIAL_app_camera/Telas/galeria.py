from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from Botoes import botoesFiltro
import cv2
import os
from kivymd.app import MDApp  # Importar MDApp de KivyMD
from kivy.app import App


from kivy.uix.image import AsyncImage
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.button import MDIconButton
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton



class Galeria(BoxLayout):
    def __init__(self, directory_path=None, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.diretorio_atual = directory_path or os.getcwd()  # Use specified directory or current working directory
        self.carregar_imagens()

    def carregar_imagens(self):
        arquivos = os.listdir(self.diretorio_atual)
        self.imagens = [arquivo for arquivo in arquivos if arquivo.endswith(('.png', '.jpg', '.jpeg'))]
        self.criar_galeria()

    def criar_galeria(self):
        # Create GridLayout for displaying images
        grid_layout = GridLayout(cols=3, padding=10, spacing=20, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        for imagem in self.imagens:
            img = Image(
                source=os.path.join(self.diretorio_atual, imagem),
                size_hint=(None, None),
                size=(300, 300),
                keep_ratio=True,
                allow_stretch=True
            )
            img.bind(on_touch_down=self.exibir_imagem_destaque)
            grid_layout.add_widget(img)


        # Create ScrollView to contain the GridLayout
        scroll_view = ScrollView()
        scroll_view.add_widget(grid_layout)

        self.add_widget(scroll_view)

    def exibir_imagem_destaque(self, instance, touch):
        if instance.collide_point(*touch.pos):
            # Clear existing widgets
            self.clear_widgets()

            # Display clicked image prominently
            img_destaque = Image(
                source=instance.source,
                size_hint=(None, None),
                size=(500, 500),
                pos_hint={'center_x': 0.5, 'center_y': 0.5}
            )

            # Create filter buttons
            botoes_filtro = botoesFiltro.BotoesFiltros(image_widget=img_destaque, frame=cv2.imread(instance.source))

            # Create layout for "Voltar" button
            layout_voltar = FloatLayout(size_hint=(1, None), size=(Window.width, 50))

            # Create "Voltar" button
            btn_voltar = MDRaisedButton(
                text="Voltar para galeria",
                size_hint=(None, None),
                size=(100, 50),
                pos_hint={'center_x': 0.6, 'center_y': 1.4},
                md_bg_color=(1, 0, 0, 1)
            )
            btn_voltar.bind(on_release=self.voltar_para_galeria)

            # Add "Voltar" button to layout
            layout_voltar.add_widget(btn_voltar)

            # Add widgets to main layout
            self.add_widget(img_destaque)
            self.add_widget(botoes_filtro)
            self.add_widget(layout_voltar)

    def voltar_para_galeria(self, instance):
        # Reload gallery
        self.clear_widgets()
        self.carregar_imagens()

class MyApp(MDApp):
    def build(self):
        return Galeria(directory_path="../OFICIAL_app_camera/Telas")  # Specify directory path here

if __name__ == '__main__':
    MyApp().run()
