# toCows
Para el Back

Generar entorno virtual del back
Ir al directorio back/integrador app
Generar entorno:
Comando Linux: python3 -m venv venv
Comando Windows: py -m venv venv

Activar entorno:
Comando Linux: source venv/bin/activate
Comando Windows: .\venv\Scripts\activate

Instalar requerimientos: pip install -r requirements.txt
Correr el servidor:
Comando Linux: python3 manage.py runserver
Comando Windows: py manage.py runserver

->cuando hay cambios en los modelos
python manage.py makemigrations
python manage.py migrate
