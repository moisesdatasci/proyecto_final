🚀 Portfolio Personal - Django<div align="center"></div>Portfolio web profesional y moderno para Data Scientists y Desarrolladores.Un proyecto personal desarrollado con Django y Vanilla JavaScript, diseñado para destacar tus habilidades, proyectos y experiencia de forma profesional y con un enfoque en el rendimiento.Ver Demo • Características • Instalación • Personalización📋 Tabla de Contenidos📖 Descripción✨ Características🖼️ Preview🛠️ Tecnologías🚀 Instalación Rápida📁 Estructura del Proyecto🎨 Personalización🌐 Despliegue🤝 Contribución📝 Licencia👤 Autor📖 DescripciónEste es un portfolio web personal desarrollado con Django, diseñado específicamente para profesionales de Data Science y Desarrollo Python. Presenta un diseño limpio, moderno y completamente responsive que destaca tus proyectos, habilidades y experiencia de manera profesional.¿Por qué usar este portfolio?✅ Listo para usar: Configuración mínima, máximo impacto.✅ Diseño profesional: Inspirado en las mejores prácticas de UI/UX.✅ SEO optimizado: Estructura semántica y meta tags.✅ 100% Responsive: Perfecto en móviles, tablets y desktop.✅ Fácil personalización: Cambia colores, contenido y estructura fácilmente.✅ Código limpio: Bien documentado y organizado.✨ Características🎨 Diseño y UINavegación fija: Menú sticky con scroll suave entre secciones.Hero section atractivo: Primera impresión impactante con gradientes y animaciones.Cards interactivas: Efectos hover y overlays modernos.Paleta de colores profesional: Gradientes púrpura/azul personalizables.Tipografía moderna: San Francisco (system fonts).Animaciones suaves: Transiciones CSS y JavaScript.📱 Responsive DesignMobile First: Optimizado para dispositivos móviles.Menú hamburguesa: Navegación touch-friendly en móviles.Grid adaptativo: Layout que se ajusta automáticamente.Imágenes responsive: Carga y visualización optimizada.🛠️ FuncionalidadesSección Home: Presentación personal con call-to-action.Galería de Proyectos: Muestra hasta 6 proyectos con detalles.Sobre Mí: Biografía, estadísticas y habilidades técnicas.Formulario de Contacto: Integración lista para email.Enlaces sociales: GitHub, LinkedIn, Email.Barras de progreso animadas: Visualización de habilidades.⚡ RendimientoCarga rápida: CSS y JS optimizados.Sin dependencias pesadas: Solo Vanilla JavaScript.Caché optimizado: Configuración de archivos estáticos.Imágenes lazy load: Placeholder automático.🖼️ PreviewSecciónContenido Destacado🏠 Home / HeroPresentación impactante, botones de acción, enlaces sociales.📁 ProyectosGrid responsive, cards con hover, tags de tecnologías.👤 Sobre MíDescripción personal, estadísticas, barras de habilidades.📧 ContactoFormulario funcional, información de contacto con iconos.🛠️ TecnologíasEste proyecto está construido con las siguientes tecnologías clave:CategoríaTecnologíaDescripciónBackendDjango 5.2.6Framework web Python para la lógica y la estructura.LenguajePython 3.13Lenguaje de programación principal.FrontendHTML5/CSS3Estructura semántica y estilos modernos (Grid, Flexbox).InteractividadJavaScript (Vanilla)Para animaciones y manejo del menú sin dependencias pesadas.Base de DatosSQLiteBase de datos por defecto (incluida).🚀 Instalación RápidaSigue estos pasos para tener tu portfolio corriendo localmente en menos de 5 minutos.PrerrequisitosAsegúrate de tener instalado:Python 3.8 o superiorpip (incluido con Python)GitInstalación en 5 minutosClona el repositorio:Bashgit clone https://github.com/tu-usuario/portfolio-django.git
cd portfolio-django
Crea un entorno virtual:Bash# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
Instala Django y dependencias:Bashpip install django
# O, si usas requirements.txt:
# pip install -r requirements.txt 
Aplica las migraciones:Bashpython manage.py migrate
Ejecuta el servidor:Bashpython manage.py runserver
¡Listo! Abre tu navegador y visita: http://127.0.0.1:8000/📁 Estructura del Proyectoportfolio-django/
│
├── 📁 portfolio_project/       # Configuración principal de Django
│   ├── settings.py            # ⚙️ Configuraciones del proyecto
│   └── urls.py                # 🔗 URLs principales
│
├── 📁 portfolio/               # Aplicación principal del portfolio
│   ├── models.py              # Esquema de la DB (si aplica)
│   ├── views.py               # 📊 Lógica de vistas y datos (donde personalizarás)
│   └── urls.py                # 🔗 URLs de la app
│
├── 📁 templates/               # Plantillas HTML
│   └── home.html              # 🏠 Página principal (única)
│
├── 📁 static/                  # Archivos estáticos (CSS, JS, Imágenes)
│   ├── 📁 css/
│   │   └── styles.css         # 🎨 Todos los estilos
│   ├── 📁 js/
│   │   └── main.js            # ⚡ JavaScript interactivo
│   └── 📁 images/              # 🖼️ Imágenes de proyectos
│
├── 📄 manage.py                # Utilidad Django
├── 📄 requirements.txt         # Dependencias Python
└── 📄 README.md                # Este archivo
🎨 PersonalizaciónToda la información clave se maneja a través del archivo portfolio/views.py y los estilos en static/css/styles.css.1. Cambiar tu Información PersonalEdita el diccionario info_personal en portfolio/views.py:Pythoninfo_personal = {
    'nombre': 'Tu Nombre',
    'titulo': 'Tu Título Profesional',
    'descripcion': 'Tu descripción',
    'email': 'tu@email.com',
    'github': 'https://github.com/tu-usuario',
    'linkedin': 'https://linkedin.com/in/tu-perfil',
    'ubicacion': 'Tu Ciudad, País'
}
2. Agregar/Modificar ProyectosEdita la lista proyectos en portfolio/views.py:Pythonproyectos = [
    {
        'id': 1,
        'titulo': 'Nombre del Proyecto',
        'descripcion': 'Descripción breve y atractiva',
        'github_url': 'https://github.com/usuario/repo',
        'imagen': 'nombre-imagen.jpg', # Debe estar en static/images/
        'tecnologias': ['Python', 'Django', 'PostgreSQL']
    },
    # Agrega más proyectos aquí...
]
3. Personalizar ColoresEdita las variables CSS en static/css/styles.css:CSS:root {
    --primary-color: #667eea;     /* Tu color principal (ej. Morado) */
    --secondary-color: #764ba2;   /* Tu color secundario (ej. Azul oscuro) */
    --dark-color: #2c3e50;        /* Color oscuro para texto y fondo */
    --light-color: #f8f9fa;       /* Color claro para fondo y texto inverso */
}
4. Modificar HabilidadesEdita la lista habilidades en portfolio/views.py:Pythonhabilidades = [
    {'nombre': 'Python', 'nivel': 90},  # Nivel de 0 a 100
    {'nombre': 'JavaScript', 'nivel': 75},
    # Agrega tus habilidades...
]
🌐 DesplieguePreparación para ProducciónActualiza settings.py:PythonDEBUG = False
ALLOWED_HOSTS = ['tu-dominio.com', 'www.tu-dominio.com']
SECRET_KEY = os.environ.get('SECRET_KEY')  # ¡Usa una variable de entorno!
STATIC_ROOT = BASE_DIR / 'staticfiles'
Crea requirements.txt:Bashpip freeze > requirements.txt
Recolecta archivos estáticos:Bashpython manage.py collectstatic
Opciones de Hosting GratuitoOpciónVentajasRecursos🔷 PythonAnywhereGratis para proyectos pequeños, soporte Django nativo.Tutorial de despliegue🔷 RailwayDeploy con GitHub, SSL gratis, bases de datos.Guía Railway + Django🔷 RenderDeploy automático desde Git, SSL incluido, plan gratuito.Deploy Django en Render🤝 Contribución¡Las contribuciones son bienvenidas! Si quieres mejorar este proyecto, sigue los siguientes pasos:Fork el proyecto.Crea una rama para tu feature: git checkout -b feature/NuevaCaracteristicaCommit tus cambios: git commit -m 'Agrega nueva característica'Push a la rama: git push origin feature/NuevaCaracteristicaAbre un Pull Request.Ideas para Contribuir🌙 Modo oscuro (dark mode).🌐 Internacionalización (i18n).📊 Blog integrado.✉️ Integración con EmailJS o servicios de correo.📝 LicenciaEste proyecto está bajo la Licencia MIT.MIT License

Copyright (c) 2024 [Tu Nombre]

Se concede permiso, libre de cargos, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados (el "Software")...
Ver el archivo LICENSE para más detalles.👤 AutorMoises - Data Scientist🌐 Portfolio: tu-portfolio.com💼 GitHub: @moisesdatasci📧 Email: tu-email@ejemplo.com💬 LinkedIn: Tu Perfil<div align="center">💡 Tips y TrucosOptimización de Imágenes: Usa TinyPNG y formato WebP. Tamaño recomendado: 800x600px, < 200KB.SEO: Asegúrate de incluir <meta name="description"> y <meta name="keywords"> en home.html.📞 Soporte¿Problemas o preguntas?🐛 Bug reports: Abrir Issue💬 Preguntas: Discussions📧 Email: tu-email@ejemplo.com⭐ Si te gustó este proyecto, ¡dale una estrella!Hecho con ❤️ y Django<a href="#portfolio-personal---django">⬆ Volver arriba</a></div>
