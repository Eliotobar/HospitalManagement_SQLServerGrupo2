Configuración para SQL Server (Microsoft SQL Server Management Studio)

1) Instala el driver ODBC si no lo tienes (ODBC Driver 17 or 18 for SQL Server).
   https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server

2) Crea una base de datos en SQL Server llamada 'HospitalDB' o cambia el valor en settings.py

3) Ajusta usuario/contraseña si no usas 'sa'/'12345'.

4) Instala paquetes en tu entorno virtual:
   pip install -r requirements.txt

5) Ejecuta migraciones:
   python manage.py makemigrations
   python manage.py migrate

6) Crea superuser:
   python manage.py createsuperuser

7) Ejecuta servidor:
   python manage.py runserver

Si hay errores de conexión, revisa que el servicio SQL Server esté activo y que el puerto/driver sean correctos.
