from cryptography.fernet import Fernet
import base64

#desencriptar imagenes en base64
def desencript_img(nom_archivo):
    img_data = open(nom_archivo,"rb").read()
    with open(nom_archivo + "Decode.png","wb") as fh:
        fh.write(base64.decodebytes(img_data))
        
#generar por primera vez una clave
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key","wb") as archivo_clave:
        archivo_clave.write(clave)

#usar la llave
def cargar_clave():
    return open("clave.key","rb").read()

#encriptar archivo
def encript(nom_archivo,clave):
    f = Fernet(clave)
    with open(nom_archivo, "rb") as file:
        archivo_info = file.read()
    encrypted_data = f.encrypt(archivo_info)
    with open(nom_archivo,"wb") as file:
        file.write(encrypted_data)

#desencriptar archivos
def desencript(nom_archivo,clave):
    f = Fernet(clave)
    with open(nom_archivo,"rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(nom_archivo,"wb") as file:
        file.write(decrypted_data)

count =+ 1
str(count)
while True:
    opc = input("""Que deseas hacer?
1.- Encriptar un archivo
2.- Desencriptar un archivo
3.- Desencriptar una imagen
4.- Salir
""")
    clave = cargar_clave()
    if opc == "1":
        nom_archivo = input("Nombre del archivo: ")
        encript(nom_archivo,clave)
    if opc == "2":
        nom_archivo = input("Nombre del archivo: ")
        desencript(nom_archivo,clave)
    if opc == "3":
        nom_archivo = input("Nombre del archivo: ")
        desencript_img(nom_archivo)
    if opc == "4":
        print("Hasta pronto")
        break
    if opc != "1" and opc != "2" and opc != "3" and opc != "4":
        print("opción no valida, intenta con otra")
        continue



