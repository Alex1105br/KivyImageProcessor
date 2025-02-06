from kivy.uix.button import Button
from functools import partial
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
import cv2
from kivymd.uix.button import MDRaisedButton
from Filtros import filtros
#from Filtros import borda
import numpy as np
import os






class BotoesFiltros(FloatLayout):
    def __init__(self, image_widget, frame, **kwargs):
        super().__init__(**kwargs)
        self.image_widget = image_widget  # Armazenar a referência do widget de imagem
        self.frame = frame  # Armazenar o quadro capturado como um atributo da classe
        

        # Adicionar os botões de filtro
        self.btn_negativo = MDRaisedButton(text="Filtro Negativo", on_release=partial(self.aplicar_filtro, filtros.filtro_negativo))
        self.btn_negativo.disabled = False
        self.btn_negativo.size_hint = (None, None)
        self.btn_negativo.size = (100, 50)
        self.btn_negativo.pos_hint = {'center_x': 0.1, 'center_y': 0.7}
        self.btn_negativo.md_bg_color = (1, 0.5, 0, 1)
        self.add_widget(self.btn_negativo)

        self.btn_preto_branco = MDRaisedButton(text="Filtro Preto e Branco", on_release=partial(self.aplicar_filtro, filtros.filtro_preto_branco))
        self.btn_preto_branco.disabled = False
        self.btn_preto_branco.size_hint = (None, None)
        self.btn_preto_branco.size = (100, 50)
        self.btn_preto_branco.pos_hint = {'center_x': 0.3, 'center_y': 0.7}
        self.btn_preto_branco.md_bg_color = (1, 0.5, 0, 1)
        self.add_widget(self.btn_preto_branco)

        self.btn_aumenta_brilho = MDRaisedButton(text="Aumentar Brilho", on_release=partial(self.aplicar_filtro, filtros.aumenta_brilho))
        self.btn_aumenta_brilho.disabled = False
        self.btn_aumenta_brilho.size_hint = (None, None)
        self.btn_aumenta_brilho.size = (100, 50)
        self.btn_aumenta_brilho.pos_hint = {'center_x': 0.5, 'center_y': 0.7}
        self.btn_aumenta_brilho.md_bg_color = (1, 0.5, 0, 1)
        self.add_widget(self.btn_aumenta_brilho)

        self.btn_borda = MDRaisedButton(text="Filtro borda", on_release=partial(self.aplicar_filtro, filtros.filtro_roberts))
        self.btn_borda.disabled = False
        self.btn_borda.size_hint = (None, None)
        self.btn_borda.size = (100, 50)
        self.btn_borda.pos_hint = {'center_x': 0.7, 'center_y': 0.7}
        self.btn_borda.md_bg_color = (1, 0.5, 0, 1)
        self.add_widget(self.btn_borda)

        self.btn_borda = MDRaisedButton(text="Escala Logarítmica", on_release=partial(self.aplicar_filtro, filtros.escala_logaritmica))
        self.btn_borda.disabled = False
        self.btn_borda.size_hint = (None, None)
        self.btn_borda.size = (100, 50)
        self.btn_borda.pos_hint = {'center_x': 0.9, 'center_y': 0.7}
        self.btn_borda.md_bg_color = (1, 0.5, 0, 1)
        self.add_widget(self.btn_borda)

    def aplicar_filtro(self, filtro, instance):
        # Aplicar o filtro à imagem capturada
        frame_filtrado = filtro(self.frame)

        # Normalize the filtered image
        frame_filtrado = self.normalize_image(frame_filtrado)

        # Inverter verticalmente a imagem filtrada
        frame_filtrado = cv2.flip(frame_filtrado, 0)

        # Criar uma textura com a imagem filtrada
        buf = frame_filtrado.tostring()
        texture = Texture.create(size=(frame_filtrado.shape[1], frame_filtrado.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')

        # Atualizar a imagem no widget de imagem
        self.image_widget.texture = texture

        # Remover botão "Salvar" se existir
        if hasattr(self, 'btn_save'):
            self.remove_widget(self.btn_save)

        # Adicionar botões "Voltar" e "Salvar" usando FloatLayout
        layout_buttons = FloatLayout(size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.1})

        

        # Botão "Salvar"
        self.btn_save = MDRaisedButton(text="Salvar", on_release=self.save_photo)
        self.btn_save.disabled = True
        self.btn_save.size_hint = (None, None)
        self.btn_save.size = (100, 50)
        self.btn_save.pos_hint = {'center_x': 0.1, 'center_y': 0.7}
        self.btn_save.md_bg_color = (0, 1, 0, 1)
        layout_buttons.add_widget(self.btn_save)

        self.add_widget(layout_buttons)

        # Habilitar o botão "Salvar"
        self.btn_save.disabled = False

        # Salvar a foto no diretório atual
        self.filtered_image = frame_filtrado

        print(f"Foto capturada, aplicado filtro {filtro.__name__}")

    def normalize_image(self, image):
        # Find maximum pixel value
        max_pixel_value = np.max(image)

        # Normalize pixel values
        normalized_image = (image / max_pixel_value) * 255

        # Convert data type to ensure compatibility with display function
        normalized_image = normalized_image.astype(np.uint8)

        return normalized_image

    

    def save_photo(self, instance):
        # Check if the image_widget source is set
        if self.image_widget.source is None:
            print("Error: Image source is not set.")
            return
        
        # Flip the filtered image
        flipped_image = cv2.flip(self.filtered_image, 0)

        # Define the directory where you want to save the images
        save_directory = "../OFICIAL_app_camera/imagens"

        # Create the directory if it does not exist
        os.makedirs(save_directory, exist_ok=True)

        # Get the original image name from the current image_widget source
        original_image_name = os.path.basename(self.image_widget.source)

        # Split the file name and extension
        original_image_base, original_image_ext = os.path.splitext(original_image_name)

        # Get the name of the filter applied from the button text
        filtro_name = self.btn_save.text.lower().replace(" ", "_")

        # Create the filename based on the original image name and filter name
        filename = f"{original_image_base}_{filtro_name}{original_image_ext}"

        # Construct the full file path to save the image
        file_path = os.path.join(save_directory, filename)

        # Save the flipped image to the specified directory
        cv2.imwrite(file_path, flipped_image)

        print(f"Photo saved as {file_path}")



