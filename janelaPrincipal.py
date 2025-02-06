from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from Telas import camera
from Telas import galeria
from kivymd.uix.button import MDIconButton
from kivy.uix.image import AsyncImage
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton




class BotaoMenu(MDIconButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.icon = "arrow-left"
        self.size_hint = (None, None)
        self.size = (150, 50)
        self.pos_hint = {'x': 0, 'top': 1}
        self.bind(on_press=self.abrir_menu_principal)

    def abrir_menu_principal(self, instance):
        # Get the ScreenManager instance from the root widget
        screen_manager = self.get_screen_manager()

        # Switch to the main menu screen
        screen_manager.current = 'tela_principal'

    def get_screen_manager(self):
        # Search for the ScreenManager instance by traversing up through the parent widgets
        parent_widget = self.parent
        while parent_widget:
            if isinstance(parent_widget, ScreenManager):
                return parent_widget
            parent_widget = parent_widget.parent

        # Return None if no ScreenManager instance is found
        return None


class janelaPrincipal(Screen):
    def __init__(self, **kwargs):
        super(janelaPrincipal, self).__init__(**kwargs)

        # Create MDTopAppBar with orange background
        toolbar = MDTopAppBar(
            #title="Main Menu",
            md_bg_color=(0, 1, 0, 1),  # Orange color (RGBA)
        )
        

        layout = BoxLayout(orientation='vertical', spacing=20)
        
        # Add the toolbar to the layout
        layout.add_widget(toolbar)

         # Add the image with the full or relative path
        image_path = "..\OFICIAL_app_camera\icones\img2.png"  # Ícone da Câmera, imagem que ficá no centro da Tela
        image = AsyncImage(source=image_path, size_hint=(0.3, 0.3), size=(100, 100),
                           pos_hint={'center_x': 0.5, 'center_y': 0.5})  # posição

        layout.add_widget(image)
        
        self.add_widget(layout)


        btn_camera = MDRaisedButton(text="Câmera", size_hint=(None, None), size=(150, 50),
                                     pos_hint={'center_x': .5, 'center_y': 0.5}, on_press=self.abrir_camera,
                                     md_bg_color=(0, 1, 0, 1))  # Green color (RGBA)
        
        btn_galeria = MDRaisedButton(text="Galeria", size_hint=(None, None), size=(150, 50),
                                      pos_hint={'center_x': .5, 'center_y': 0.5}, on_press=self.abrir_galeria,
                                      md_bg_color=(0, 1, 0, 1))  # Green color (RGBA)

        layout.add_widget(btn_camera)
        layout.add_widget(btn_galeria)



    def abrir_camera(self, *args):
        # Define a tela atual como a tela da câmera
        self.manager.current = 'tela_camera'

    def abrir_galeria(self, *args):
        # Define a tela atual como a tela da galeria
        self.manager.current = 'tela_galeria'



from kivy.uix.label import Label
from kivy.graphics import Color, Line

class TelaCamera(Screen):
    def __init__(self, **kwargs):
        super(TelaCamera, self).__init__(**kwargs)
        
        # Create MDTopAppBar with orange background and no elevation
        toolbar = MDTopAppBar(
            #md_bg_color=(1, 0.5, 0, 1),  # Orange color (RGBA)
            md_bg_color=(0, 1, 0, 1),  # Cor verde (RGBA)
            elevation=0,  # No shadow
            pos_hint={'top': 1}  # Position the toolbar at the top of the screen
        )
        
        # Add left arrow button to the toolbar
        left_button = MDIconButton(
            icon="arrow-left",
            theme_text_color="Custom",  # Set text color manually
            text_color=[1, 1, 1, 1],  # Set text color to white
            on_press=self.abrir_menu_principal
        )
        toolbar.add_widget(left_button)
        
        
        layout = BoxLayout(orientation='vertical', spacing=10)  # Ensure vertical orientation and appropriate spacing

        titulo_layout = BoxLayout(orientation = 'horizontal')

        nome_Tela = Label(
            text= 'Câmera', 
            font_size = 24, 
            color = (1,1,1,1),
            pos_hint={'center_x':0.5, 'center_y':3.0}
            )
        
        titulo_layout.add_widget(nome_Tela)

        toolbar.add_widget(titulo_layout)

        # Add the toolbar to the layout
        layout.add_widget(toolbar)

        # Add the CameraApp widget
        layout.add_widget(camera.CameraApp().build())

        # Add the layout to the screen
        self.add_widget(layout)

    def abrir_menu_principal(self, instance):
        # Navigate to the main menu screen
        self.manager.current = 'tela_principal'




class TelaGaleria(Screen):
    def __init__(self, **kwargs):
        super(TelaGaleria, self).__init__(**kwargs)
        
        # Create MDTopAppBar with orange background and no elevation
        toolbar = MDTopAppBar(
            md_bg_color=(0, 1, 0, 1),  # Orange color (RGBA)
            elevation=0,  # No shadow
            pos_hint={'top': 1}  # Position the toolbar at the top of the screen
        )
        
        # Add left arrow button to the toolbar
        left_button = MDIconButton(
            icon="arrow-left",
            theme_text_color="Custom",  # Set text color manually
            text_color=[1, 1, 1, 1],  # Set text color to white
            on_press=self.abrir_menu_principal
        )
        toolbar.add_widget(left_button)

        titulo_layout = BoxLayout(orientation = 'horizontal')

        nomeTela = Label(
            text='Galeria', 
            font_size=24, 
            color=(1, 1, 1, 1), 
            pos_hint = {'x':0.5, 'y':3.0}
            )


        titulo_layout.add_widget(nomeTela)

        toolbar.add_widget(titulo_layout)

        
        layout = BoxLayout(orientation='vertical', spacing=10)  # Ensure vertical orientation and appropriate spacing

        # Add the toolbar to the layout
        layout.add_widget(toolbar)

        # Specify the directory path for Galeria
        directory_path = "../OFICIAL_app_camera/imagens"  # Update with the desired directory path

        # Add the Galeria widget with specified directory path
        layout.add_widget(galeria.Galeria(directory_path=directory_path))

        # Add the layout to the screen
        self.add_widget(layout)

    def abrir_menu_principal(self, instance):
        # Navigate to the main menu screen
        self.manager.current = 'tela_principal'


class ProcessadorImagem(MDApp):
    def build(self):
        self.screen_manager = ScreenManager()

        # Add screens to the screen manager
        janela_principal = janelaPrincipal(name='tela_principal')
        self.screen_manager.add_widget(janela_principal)
        self.screen_manager.add_widget(TelaCamera(name='tela_camera'))
        self.screen_manager.add_widget(TelaGaleria(name='tela_galeria'))

        return self.screen_manager


ProcessadorImagem().run()

