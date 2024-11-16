from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Definir la ruta del directorio en Windows
ruta_directorio = r"D:\Dev\miro\cof-tanner\ttbanca-web-2-backend\EFE_TE_PE"

# Definir las credenciales para el usuario FTP
authorizer = DummyAuthorizer()
authorizer.add_user("user", "password", ruta_directorio, perm="elradfmw")  # permisos completos

# Configurar el manejador FTP
handler = FTPHandler
handler.authorizer = authorizer

# Definir la dirección IP y el puerto del servidor FTP
server = FTPServer(("127.0.0.1", 21), handler)

# Iniciar el servidor FTP
server.serve_forever()
