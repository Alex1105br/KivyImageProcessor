# KivyImageProcessor

# Processador de Imagem - Aplicativo Kivy

## Descrição
Este é um aplicativo desenvolvido em Python utilizando o framework Kivy e KivyMD. O objetivo é permitir a aplicação de filtros em imagens capturadas pela câmera ou selecionadas da galeria. O aplicativo possui uma interface intuitiva com navegação entre telas e funcionalidades para processamento de imagens.

## Funcionalidades
- Captura de imagens via câmera
- Seleção de imagens da galeria
- Aplicação de filtros diversos
- Salvamento de imagens processadas

## Estrutura do Projeto

### `janelaPrincipal.py`
- **Classe `BotaoMenu`**: Cria um botão que permite retornar à janela principal.
- **Classe `janelaPrincipal`**: Define a tela principal com os botões "Câmera" e "Galeria" para navegar entre as telas do aplicativo.
- **Classe `TelaCamera`**: Implementa a interface da tela da câmera, incluindo um botão de retorno e ajustes estéticos.
- **Classe `TelaGaleria`**: Similar à `TelaCamera`, mas voltada para a exibição de imagens da galeria.
- **Classe `ProcessadorImagem`**: Gerencia as telas do aplicativo usando `ScreenManager`.

### `botoesFiltro.py`
- **`__init__`**: Cria os botões de filtro e associa as ações de aplicação de filtros.
- **`aplica_filtro`**: Aplica o filtro selecionado e exibe o botão de salvar.
- **`normalize_image`**: Garante que os pixels da imagem estejam no intervalo de 0 a 255.
- **`save_photo`**: Define o diretório para salvar as imagens filtradas.

### `filtros.py`
- Define a implementação de cada filtro disponível no aplicativo.

### `camera.py`
- **Classe `CameraApp`**: Gerencia todas as funcionalidades da câmera.
- **`build`**: Cria os botões "Ativar Câmera" e "Capturar Foto".
- **`toggle_camera`**: Alterna entre ligar e desligar a câmera.
- **`update`**: Atualiza os quadros da exibição da câmera.
- **`capture_photo`**: Captura a foto e chama os botões de filtro.

### `galeria.py`
- **Classe `Galeria`**: Implementa as funcionalidades da galeria de imagens.
- **`__init__`**: Define a orientação e carrega imagens do diretório.
- **`carregar_imagens`**: Lista imagens compatíveis (`.png`, `.jpg`, `.jpeg`).
- **`criar_galeria`**: Exibe as imagens em colunas e permite seleção.
- **`exibir_imagem_destaque`**: Mostra uma imagem ampliada com opção de aplicar filtros.
- **`voltar_para_galeria`**: Retorna à tela de galeria ao pressionar o botão "Voltar".

## Instalação
1. Clone este repositório:
   ```bash
   git clone [https://github.com/seu-usuario/processador-imagem.git](https://github.com/Alex1105br/KivyImageProcessor.git)
   ```
2. Instale as dependências:
   ```bash
   pip install kivy kivymd numpy opencv-python
   ```
3. Execute o aplicativo:
   ```bash
   python janelaPrincipal.py
   ```

## Tecnologias Utilizadas
- **Python**
- **Kivy** e **KivyMD**
- **OpenCV** (para processamento de imagens)
- **Numpy**





