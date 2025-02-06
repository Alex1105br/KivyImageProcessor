import cv2
import numpy as np


def retorna_mediana(matrix, x, y):
    matrix = np.clip(matrix, 0, 255)  # Limita os valores no intervalo [0, 255]

    # Converte a matriz em um vetor unidimensional com precisão de ponto flutuante
    flattened_matrix = matrix.flatten().astype(np.float64)

    # Ordena os pixels
    flattened_matrix.sort()

    # Calcula a mediana dos valores ordenados
    mediana = flattened_matrix[len(flattened_matrix) // 2]

    return mediana

def filtro_mediana(imgOriginal):
    # Copia a imagem original para evitar alterações na imagem original
    img = imgOriginal.copy()
    altura, largura, bandas = img.shape

    for i in range(altura):
        for j in range(largura):
            for k in range(bandas):
                pixelCentral = img[i, j, k]

                vizinhos = []

                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if 0 <= i + x < altura and 0 <= j + y < largura:
                            vizinhos.append(img[i + x, j + y, k])

                # Calcula a mediana dos valores dos vizinhos
                mediana = retorna_mediana(np.array(vizinhos), pixelCentral, k)

                img[i, j, k] = mediana

    return img



def k_valores_proximo(matrix, x, k):
    # Verifique se os valores da matriz estão dentro dos limites
    matrix = np.clip(matrix, 0, 255)  # Limita os valores no intervalo [0, 255]

    # Converte a matriz em um vetor unidimensional com precisão de ponto flutuante
    flattened_matrix = matrix.flatten().astype(np.float64)
    
    # Calcula as diferenças entre x e todos os elementos do vetor, considerando apenas valores positivos
    differences = [(abs(x - elem), elem) if elem >= 0 else (x, elem) for elem in flattened_matrix]

    # Ordena as diferenças em ordem crescente
    differences.sort()

    # Seleciona os primeiros k elementos da lista ordenada
    k_closest = [elem for _, elem in differences[:k]]

    # Soma os k valores mais próximos
    sum_closest = sum(k_closest)

    return sum_closest

#Filtro da média com os k vizinhos mais próximos

def filtroVizinhosProximos(imgOriginal):
    # Copia a imagem original para evitar alterações na imagem original
    img = imgOriginal.copy()
    altura, largura, bandas = img.shape

    for i in range(altura):
        for j in range(largura):
            for k in range(bandas):
                pixelCentral = img[i, j, k]

                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if 0 <= i + x < altura and 0 <= j + y < largura:
                            soma_k_proximos = k_valores_proximo(img[i + x, j + y, k], pixelCentral, 6)
                            soma_k_proximos = pixelCentral + soma_k_proximos
                
                media_k = soma_k_proximos / 7
                img[i, j, k] = media_k
    return img


def retorna_moda(lista_pixels_vizinhos):
    # Calcula a moda usando a função max, set e o atributo count
    moda = max(set(lista_pixels_vizinhos), key=lista_pixels_vizinhos.count)

    return moda

def filtro_moda(imgOriginal):
    # Copia a imagem original para evitar alterações na imagem original
    img = imgOriginal.copy()
    altura, largura, bandas = img.shape

    for i in range(altura):
        for j in range(largura):
            for k in range(bandas):
                pixelCentral = img[i, j, k]

                vizinhos = []

                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if 0 <= i + x < altura and 0 <= j + y < largura:
                            vizinhos.append(img[i + x, j + y, k])

                # Calcula a moda dos valores dos vizinhos
                moda = retorna_moda(vizinhos)

                img[i, j, k] = moda

    return img


def filtroMedio(imgOriginal):
    # Copia a imagem original para evitar alterações na imagem original
    img = imgOriginal.copy()
    altura, largura, bandas = img.shape

    for i in range(altura):
        for j in range(largura):
            for k in range(bandas):
                pixelCentral = img[i, j, k]

                # Calcula a média dos pixels vizinhos
                soma = 0
                count = 0

                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if 0 <= i + x < altura and 0 <= j + y < largura:
                            soma += img[i + x, j + y, k]
                            count += 1

                media = soma / count
                img[i, j, k] = media

    return img

def filtro_negativo(img_original):
    # Copia a imagem original para evitar alterações na imagem original
    img = img_original.copy()

    # Obtém as dimensões da imagem
    altura, largura, _ = img.shape

    cor_negativa = 255
    for y in range(altura):
        for x in range(largura):
            # Acessa o pixel na posição (x, y)
            pixel = img[y, x]

            pixel = cor_negativa - pixel

            # Limita o valor do pixel entre 0 e 255
            pixel = np.clip(pixel, 0, 255)

            # Atualiza o pixel na imagem
            img[y, x] = pixel

    return img



def aumenta_brilho(img_original):
    # Copia a imagem original para evitar alterações na imagem original
    img = img_original.copy()

    valor = 100
    # Percorrer a imagem como uma matriz
    for i in range(img.shape[0]): # Linhas
        for j in range(img.shape[1]): # Colunas
            for k in range(img.shape[2]): # Canais
            # Somar o valor ao pixel, limitando ao máximo de 255
                img[i,j,k] = min(img[i,j,k] + valor, 255)
    
    return img

def filtro_preto_branco(img_original):
    # Copia a imagem original para evitar alterações na imagem original
    img = img_original.copy()

    # Obtém as dimensões da imagem
    altura, largura, _ = img.shape

    for y in range(altura):
        for x in range(largura):
            # Acessa o pixel na posição (x, y)
            pixel = img[y, x]

            # Calcula a média dos valores dos canais de cor
            media = np.mean(pixel)

            # Atribui a média a todos os canais de cor
            pixel = [media, media, media]

            # Atualiza o pixel na imagem
            img[y, x] = pixel

    return img




import cv2
import numpy as np

def filtro_roberts(imagem):
    if len(imagem.shape) == 2:
        altura, largura = imagem.shape
        canais = 1
    else:
        altura, largura, canais = imagem.shape

    imagemFiltrada = np.zeros_like(imagem, dtype=np.float32)
    
    Gx = np.array([[1, 0], [0, -1]])
    Gy = np.array([[0, 1], [-1, 0]])

    for canal in range(canais):
        for i in range(altura - 1):
            for j in range(largura - 1):
                if canais == 1:
                    regiao = imagem[i:i + 2, j:j + 2]
                else:
                    regiao = imagem[i:i + 2, j:j + 2, canal]

                gx = np.sum(Gx * regiao)
                gy = np.sum(Gy * regiao)

                gradiente = np.sqrt(gx**2 + gy**2)

                if canais == 1:
                    imagemFiltrada[i, j] = gradiente
                else:
                    imagemFiltrada[i, j, canal] = gradiente

    imagemFiltrada = (imagemFiltrada / imagemFiltrada.max()) * 255
    return imagemFiltrada


def escala_logaritmica(image):
    c = 50
    # Copia a imagem original para evitar alterações na imagem original
    img_contrast = image.copy()

    # Aplicar a transformação logarítmica para cada pixel da imagem
    for i in range(image.shape[0]): # Linhas
        for j in range(image.shape[1]): # Colunas
            for k in range(image.shape[2]): # Canais
                img_contrast[i, j, k] = int(np.clip(c * np.log(1 + image[i, j, k]), 0, 255))

    return img_contrast
