# pylint: disable=E0401
import cv2

img = cv2.imread(r'C:\\Users\\52616\\OneDrive\\Documentos\\tobeyatspiderman.jpg')

if img is not None:
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("alto, ancho, canales = " + str(img2.shape))

    cv2.imshow('Fondo de pantalla', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No se pudo cargar la imagen 'tobeyatspiderman.jpg'")