# 🚀 Portfolio Personal - Django

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0+-092E20?style=for-the-badge&logo=django&logoColor=white)
![Status](https://img.shields.io/badge/Status-Activo-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

**Portfolio web profesional y moderno para Data Scientists y Desarrolladores**

[Ver Demo](https://tu-demo-link.com) • [Características](#-características) • [Instalación](#-instalación-rápida) • [Personalización](#-personalización)

</div>

---

## 📋 Tabla de Contenidos

1. [📖 Descripción](#-descripción)
2. [✨ Características](#-características)
3. [🛠️ Tecnologías](#%EF%B8%8F-tecnologías)
4. [🚀 Instalación Rápida](#-instalación-rápida)
5. [📁 Estructura del Proyecto](#-estructura-del-proyecto)
6. [🎨 Personalización](#-personalización)
7. [🌐 Despliegue](#-despliegue)
8. [👤 Autor](#-autor)

---

## 📖 Descripción

Portfolio web personal desarrollado con **Django**, diseñado específicamente para profesionales de **Data Science** y **Desarrollo Python**. Presenta un diseño limpio, moderno y completamente responsive que destaca tus proyectos, habilidades y experiencia de manera profesional.

### ¿Por qué usar este portfolio?
* ✅ **Listo para usar:** Configuración mínima, máximo impacto.
* ✅ **Diseño profesional:** Inspirado en las mejores prácticas de UI/UX.
* ✅ **SEO optimizado:** Estructura semántica y meta tags.
* ✅ **100% Responsive:** Perfecto en móviles, tablets y desktop.
* ✅ **Fácil personalización:** Cambia colores, contenido y estructura fácilmente.
* ✅ **Código limpio:** Bien documentado y organizado.

---

## ✨ Características

### 🎨 Diseño y UI
* **Navegación fija:** Menú sticky con scroll suave.
* **Hero section atractivo:** Gradientes y animaciones CSS.
* **Cards interactivas:** Efectos hover y overlays modernos.
* **Modo Oscuro/Claro:** (Preparado para implementación).

### 📱 Responsive Design
* **Mobile First:** Optimizado para pantallas pequeñas.
* **Menú hamburguesa:** Navegación táctil amigable.
* **Grid adaptativo:** Layout flexible.

### 🛠️ Funcionalidades
* **Galería de Proyectos:** Hasta 6 proyectos destacados.
* **Estadísticas:** Visualización de experiencia y proyectos.
* **Formulario de Contacto:** Integración funcional.
* **Barras de Progreso:** Visualización animada de habilidades (Python, SQL, ML).

### ⚡ Rendimiento
* **Carga rápida:** CSS/JS minificado y optimizado.
* **Sin dependencias pesadas:** Vanilla JavaScript.
* **Lazy Load:** Carga diferida de imágenes.

---

## 🛠️ Tecnologías

| Categoría | Tecnologías |
|-----------|-------------|
| **Backend** | ![Django](https://img.shields.io/badge/Django-5.2.6-092E20) ![Python](https://img.shields.io/badge/Python-3.13-3776AB) |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white) ![JS](https://img.shields.io/badge/JavaScript-Vanilla-F7DF1E?logo=javascript&logoColor=black) |
| **Database** | ![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white) |
| **Tools** | ![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white) ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?logo=visual-studio-code&logoColor=white) |

---

## 🚀 Instalación Rápida

### Prerrequisitos
* Python 3.8+
* Git

### Pasos en 5 minutos

1. **Clona el repositorio**
   ```bash
   git clone [https://github.com/tu-usuario/portfolio-django.git](https://github.com/tu-usuario/portfolio-django.git)
   cd portfolio-django

2. **Crea y activa el entorno virtual**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    
3. **Instala dependencias**
   ```bash
   pip install django
    # O si tienes requirements.txt
    # pip install -r requirements.txt

4. Configura la Base de Datos
   ```bash
   python manage.py migrate

5. **Corre el servidor**
   ```bash
   python manage.py runserver

## 📁 Estructura del Proyecto
```Plaintext
portfolio-django/
│
├── 📁 portfolio_project/       # Configuración principal Django
│   ├── settings.py
│   └── urls.py
│
├── 📁 portfolio/               # App principal
│   ├── views.py               # 📊 Lógica y DATOS 
│   ├── models.py
│   └── urls.py
│
├── 📁 templates/
│   └── home.html              # 🏠 Único template HTML
│
├── 📁 static/
│   ├── 📁 css/styles.css      # 🎨 Estilos
│   ├── 📁 js/main.js          # ⚡ Scripts
│   └── 📁 images/             # 🖼️ Tus imágenes aquí
│
└── manage.py
```

## 🎨 Personalización

1. **Información Personal**
Edita portfolio/views.py:
```
info_personal = {
    'nombre': 'Tu Nombre',
    'titulo': 'Data Scientist',
    'github': '[https://github.com/tu-usuario](https://github.com/tu-usuario)',
    # ...
}
```

2. **Proyectos**
   En portfolio/views.py, modifica la lista proyectos:
```
   proyectos = [
    {
        'titulo': 'Análisis Sísmico',
        'descripcion': 'Análisis con Pandas y Matplotlib',
        'imagen': 'sismo.jpg', # Debe estar en static/images/
        'tags': ['Python', 'Pandas']
        },
    ]
```
## 🌐 Despliegue
Este proyecto está listo para desplegarse en plataformas gratuitas como PythonAnywhere, Railway o Render.

**Pasos previos a producción:**

1. En settings.py, cambia DEBUG = False.
2. Configura ALLOWED_HOSTS = ['tu-dominio.com'].
3. Genera los archivos estáticos:

```bash

python manage.py collectstatic
```

## 👤 Autor
Moises - Data Scientist

**💼 GitHub: @moisesdatasci**
**📧 Email: moises.ortega@usach.cl**

<div align="center"> <sub>Hecho con ❤️ y Django. Si te sirve este proyecto, ¡dale una estrella ⭐!</sub> </div>
