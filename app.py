import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def mostrar_imagen_aleatoria():
    # Lista de nombres de archivos de las imágenes
    imagenes = [f for f in os.listdir() if f.endswith('.jpg') or f.endswith('.png')]
    
    # Seleccionar una imagen al azar
    imagen_seleccionada = random.choice(imagenes)
    
    # Leer la imagen seleccionada
    img = mpimg.imread(imagen_seleccionada)
    
    # Mostrar la imagen
    plt.imshow(img)
    plt.show()

if __name__ == "__main__":
    mostrar_imagen_aleatoria()
