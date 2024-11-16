from ftplib import FTP
import os

def download_files_from_ftp(host, user, passwd, remote_directory, local_directory):
    # Conexión al servidor FTP
    ftp = FTP(host)
    ftp.login(user, passwd)

    # Cambio al directorio especificado
    ftp.cwd(remote_directory)

    # Creación del directorio local si no existe
    if not os.path.exists(local_directory):
        os.makedirs(local_directory)

    # Listado de archivos en el directorio remoto
    files = ftp.nlst()

    for file in files:
        # Omitir entradas de directorio
        if file in ['.', '..']:
            continue

        # Nombre de archivo local
        local_file = os.path.join(local_directory, file)
        
        # Intento de descarga del archivo
        try:
            print(f"Intentando descargar {file}...")
            with open(local_file, 'wb') as f:
                ftp.retrbinary("RETR " + file, f.write)
            print(f"{file} descargado con éxito.")
            # Eliminar archivo del directorio remoto
            ftp.delete(file)
            print(f"{file} eliminado del directorio remoto.")
        except Exception as e:
            print(f"Error al descargar {file}. Razón: {e}")

    ftp.quit()
    print("Proceso completado.")

# Configuración
# Configuración desde variables de entorno
HOST = os.environ.get('ATWCL_FTP_HOST')
USER = os.environ.get('ATWCL_FTP_USER')
PASSWD = os.environ.get('ATWCL_FTP_PASSWD')

REMOTE_DIRECTORY = '/respaldos/atwclbd'
LOCAL_DIRECTORY = 'D:/Dev/bkp/sql/fi.atw.cl/'

download_files_from_ftp(HOST, USER, PASSWD, REMOTE_DIRECTORY, LOCAL_DIRECTORY)


# Configuración
# Configuración desde variables de entorno
HOST2 = os.environ.get('LYM_FTP_HOST')
USER2 = os.environ.get('LYM_FTP_USER')
PASSWD2 = os.environ.get('LYM_FTP_PASSWD')

REMOTE_DIRECTORY2 = '/respaldosh/bdsql'
LOCAL_DIRECTORY2 = 'D:/Dev/bkp/sql/latasymoldes_rvweb/'


download_files_from_ftp(HOST2, USER2, PASSWD2, REMOTE_DIRECTORY2, LOCAL_DIRECTORY2)