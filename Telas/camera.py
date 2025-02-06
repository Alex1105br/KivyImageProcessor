from kivymd.uix.button import MDRaisedButton
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
import cv2
from kivy.graphics.texture import Texture
from Botoes import botoesFiltro
from kivy.uix.screenmanager import ScreenManager



class CameraApp(MDApp):
    def build(self):
        
        self.layout = BoxLayout(orientation='vertical')

        # Widget de imagem para exibir a captura da câmera
        self.image_widget = Image()
        self.layout.add_widget(self.image_widget)

        # Botão para ativar/desativar a câmera
        self.btn_camera = MDRaisedButton(text="Ativar Câmera", on_release=self.toggle_camera)
        self.btn_camera.size_hint = (None, None)
        self.btn_camera.size = (100, 50)
        self.btn_camera.pos_hint = {'center_x': 0.5, 'center_y': 0.1}
        self.btn_camera.md_bg_color = (0, 1, 0, 1)  # green (RGBA)
        self.layout.add_widget(self.btn_camera)

        # Espaçador vazio para criar um espaço entre os botões
        self.layout.add_widget(Widget(size_hint_y=None, height=5))

        # Botão para capturar uma foto
        self.btn_capture = MDRaisedButton(text="Capturar Foto", on_release=self.capture_photo)
        self.btn_capture.disabled = True
        self.btn_capture.size_hint = (None, None)
        self.btn_capture.size = (100, 50)
        self.btn_capture.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.btn_capture.md_bg_color = (0, 1, 0, 1)  # green
        self.layout.add_widget(self.btn_capture)


        return self.layout

    def toggle_camera(self, instance):
        if not hasattr(self, 'capture') or not self.capture.isOpened():
            # Se a câmera não estiver ativa, ativá-la
            self.capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 1 para a webcam, e 0 para webcam do notebook
            Clock.schedule_interval(self.update, 1.0 / 30.0)  # Atualizar a imagem a cada 1/30 segundos
            self.btn_camera.text = "Desativar Câmera"
            self.btn_camera.md_bg_color = (1, 0, 0, 1)  # Red color (RGBA)
            self.btn_capture.disabled = False  # Ativar o botão de captura
        else:
            # Se a câmera estiver ativa, desativá-la
            self.capture.release()
            self.btn_camera.text = "Ativar Câmera"
            self.btn_capture.disabled = True  # Desativar o botão de captura
            self.image_widget.texture = None  # Limpar a imagem exibida
            self.btn_camera.md_bg_color = (0, 1, 0, 1)  # Reset to green color


    def update(self, dt):
        # Capturar um quadro da câmera
        ret, frame = self.capture.read()

        if frame is not None:
            # Inverter horizontalmente a imagem
            buf1 = cv2.flip(frame, -1)

            buf = buf1.tostring()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')

            # Atualizar a imagem no widget de imagem
            self.image_widget.texture = texture

    def capture_photo(self, instance):
        # Capturar um quadro da câmera
        ret, self.frame = self.capture.read()

        # Desativar a câmera
        self.toggle_camera(None)

        # Definir o caminho da imagem capturada
        image_path = "../OFICIAL_app_camera/imagens/fotoCamera.jpg"
        # Inverter a imagem horizontalmente antes de salvar
        flipped_frame = cv2.flip(self.frame, 1)
        cv2.imwrite(image_path, flipped_frame)  # Salvar a imagem capturada

        # Atualizar o widget de imagem com a imagem capturada
        self.image_widget.source = image_path
        self.image_widget.reload()  # Recarregar o widget para exibir a nova imagem
        

        # Remover os botões "Ativar Câmera" e "Capturar Foto"
        self.layout.remove_widget(self.btn_camera)
        self.layout.remove_widget(self.btn_capture)

        # Adicionar os botões de filtro usando a classe BotõesFiltros e passando a referência do widget de imagem e o quadro capturado
        botoes_filtros = botoesFiltro.BotoesFiltros(image_widget=self.image_widget, frame=flipped_frame)
        
        self.layout.add_widget(botoes_filtros)
        


if __name__ == "__main__":
    CameraApp().run()

