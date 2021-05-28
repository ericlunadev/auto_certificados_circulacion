# auto_certificados_circulacion

¿Estás cansado de completar todos los días el formulario para sacar los permisos de circulación?
Yo también.

**auto_certificados_circulacion** es un script de Selenium que podes correr para que autocomplete el formulario y sólo tengas que llenar los campos que pueden llegar a cambiar.

## ⚙️ Setup
- Instalar dependencias
```pip install requirements.text```

- Descargar chromedriver

- Actualizar ```DRIVER_PATH``` con la ubicación donde descargaron chromedriver.
- Actualizar ```LOGIN_URL``` de acuerdo a la provincia/ciudad del permiso.
- Actualizar las constantes de main.py con tus datos.
- Correr main.py ```python main.py```
