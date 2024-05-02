import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
print("test")
def show_image():
    # Lista de nombres de archivos de las imágenes
    images = [f for f in os.listdir() if f.endswith('.jpg') or f.endswith('.png')]
    
    # Seleccionar una imagen al azar
    selected_image = random.choice(image)
    
    # Leer la imagen seleccionada
    img = mpimg.imread(selected_image)
    
    # Mostrar la imagen
    plt.imshow(img)
    plt.show()

if __name__ == "__main__":
    show_image()
