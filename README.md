# Proyecto Django

Este proyecto fue desarrollado utilizando Django y Python en un entorno virtual. A continuación, se detallan los pasos necesarios para instalar y ejecutar el proyecto correctamente en tu máquina local.

---

## 🧱 Requisitos previos

- Python 3.x
- Git
- pip (instalado por defecto con Python)

---

## 📦 Instalación del entorno virtual

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/tu-repositorio.git
cd tu-repositorio
```

2. Crea el entorno virtual llamado `admin`:

```bash
python -m venv admin
```

3. Activa el entorno virtual:

- En **Windows**:

```bash
admin\Scripts\activate
```

- En **Linux/macOS**:

```bash
source admin/bin/activate
```

---

## 📜 Instalación de dependencias

Una vez activado el entorno virtual, instala las dependencias con:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Aplicar migraciones

Django necesita aplicar migraciones para crear las tablas en la base de datos. Ejecuta:

```bash
python manage.py migrate
```

---

## 👤 Crear superusuario

Para acceder al panel de administración de Django, es necesario crear un superusuario:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para ingresar un nombre de usuario, correo electrónico (opcional) y contraseña.

---

## 🚀 Ejecutar el servidor de desarrollo

Para iniciar el proyecto y probar que todo esté funcionando:

```bash
python manage.py runserver
```

Luego abre tu navegador y visita:

```
http://127.0.0.1:8000/
```

Para acceder al panel de administración:

```
http://127.0.0.1:8000/admin/
```

---

## 🧼 Notas adicionales

- El entorno virtual `admin` está ignorado en `.gitignore` y no se sube a GitHub.
- Todas las dependencias necesarias están incluidas en `requirements.txt`.
