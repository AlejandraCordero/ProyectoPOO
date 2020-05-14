import cv2
from Main import Main_object
from Main import Pokemon

def img_to_gray_scale():
    #Recibe un objeto imagen y devuleve la imagen en blanco y negro
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('imagen_gris', gray_img)
    print("El proyecto corrio exitosamente--> gris")
    cv2.waitKey(5000)
    cv2.destroyAllWindows()


def img_color():
    #Recibe un objeto imagen y devuleve a colores
    cv2.imshow('imagen_color', img)
    print("El proyecto corrio exitosamente-->color")
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

def img_jump():
    img = Main_object.read_image("salta.jpg")
    cv2.imshow('imagen_salta', img)
    print("El proyecto corrio exitosamente-->salta")
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

def img_fight():
    img = Main_object.read_image("pelear.jpg")
    cv2.imshow('imagen_pelea', img)
    print("El proyecto corrio exitosamente-->pelea")
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

def img_sleep(num):
    if Pokemon._sleep()=='num':
        img = Main_object.read_image("dormir.jpg")
        cv2.imshow('imagen_dormir', img)
        print("El proyecto corrio exitosamente-->dormir")
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
    else:
        img = Main_object.read_image("despierto.jpg")
        cv2.imshow('imagen_despierto', img)
        print("El proyecto corrio exitosamente-->despierto")
        cv2.waitKey(5000)
        cv2.destroyAllWindows()


#Obtenemos la imagen
print("------------------------------------------------")
print("María Alejandra Mamani Cordero")
print("------------------------------------------------")
img = Main_object.read_image("img1.png")
imagen_color=img_color()  #Se muestra la imagen en colores
imagen_gris=img_to_gray_scale() # Se muestra la imagen en gris
#Main_object.save_img(img=Imagen_color, name_img="imagen_dark") #Método para copiar
imagen_salta=img_jump() #Método saltar
imagen_pelea=img_fight() #Método saltar
imagen_dormir=img_sleep('1') #Método dormir




