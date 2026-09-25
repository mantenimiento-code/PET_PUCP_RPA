from cryptography.fernet import Fernet
import json

# La llave generada en el paso anterior
LLAVE_MAESTRA = b"mqNccQKc61i3hctDPSVY-gH9k7xIJc-IXf2s_g-YdFM=" 
fernet = Fernet(LLAVE_MAESTRA)

# Los datos que deseas proteger
datos_credenciales = {
    "usuario": "W0026327",
    "password": "mntoPUCP2026***"
}

# Convertir a texto e inundar en bytes
json_bytes = json.dumps(datos_credenciales).encode('utf-8')

# Encriptar
datos_encriptados = fernet.encrypt(json_bytes)

# Guardar en un archivo local para subirlo a GitHub
with open("credenciales_ocultas.enc", "wb") as archivo:
    archivo.write(datos_encriptados)

print("Archivo 'credenciales_ocultas.enc' generado con éxito. Ya puedes subirlo a GitHub.")