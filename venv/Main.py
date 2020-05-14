import cv2

class Main_object:

    @staticmethod
    def read_image(path_img):
        """Leer una imagen desde el disco y devolver in objeto imagen"""
        if isinstance(path_img, str):
            try:
                img = cv2.imread(path_img)
            except:
                print("Ërror de path")
            return img
        else:
            print("formato no valido")
            return None

    @staticmethod
    def save_img(img, name_img):
        # write image on disk
        # escribir validador de string, regex, validar que un string termine en jpg
        name_img = name_img + ".jpg"
        cv2.imwrite(name_img, img)

class Pokemon:

    def __init__(self, name, age, type):
        self._name = name
        self._age = age
        self._type=type

    def _sleep():
        a=int(input("Esta durmiendo el Pikachu?"))
        if a==1:
          return 1
        else:
            return 0


