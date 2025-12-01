import os
from pathlib import Path

# Obtener el directorio base
BASE_DIR = Path(__file__).resolve().parent

# Crear carpetas
folders = [
    'templates',
    'static/css',
    'static/images',
    'static/js',
]

for folder in folders:
    folder_path = BASE_DIR / folder
    folder_path.mkdir(parents=True, exist_ok=True)
    print(f"✓ Carpeta creada: {folder}")

# Contenido del template HTML
html_content = """{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Portfolio - Proyectos GitHub</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <header>
        <div class="container">
            <h1>Mis Proyectos de Data Science</h1>
            <p class="subtitle">Explora mi trabajo en GitHub</p>
        </div>
    </header>

    <main class="container">
        <div class="proyectos-grid">
            {% for proyecto in proyectos %}
            <div class="proyecto-card">
                <div class="proyecto-imagen">
                    <img src="{% static 'images/' %}{{ proyecto.imagen }}" 
                         alt="{{ proyecto.titulo }}"
                         onerror="this.src='{% static 'images/placeholder.jpg' %}'">
                </div>
                <div class="proyecto-contenido">
                    <h2>{{ proyecto.titulo }}</h2>
                    <p>{{ proyecto.descripcion }}</p>
                    <a href="{{ proyecto.github_url }}" 
                       target="_blank" 
                       class="btn-github">
                        <svg height="20" width="20" viewBox="0 0 16 16" fill="currentColor">
                            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
                        </svg>
                        Ver en GitHub
                    </a>
                </div>
            </div>
            {% endfor %}
        </div>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2024 Moises Data Science. Todos los derechos reservados.</p>
        </div>
    </footer>
</body>
</html>
"""

# Crear archivo home.html
html_file = BASE_DIR / 'templates' / 'home.html'
html_file.write_text(html_content, encoding='utf-8')
print(f"✓ Archivo creado: templates/home.html")

# Contenido del CSS
css_content = """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f5f5f5;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 60px 0;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

header h1 {
    font-size: 2.5rem;
    margin-bottom: 10px;
}

.subtitle {
    font-size: 1.2rem;
    opacity: 0.9;
}

main {
    padding: 60px 0;
}

.proyectos-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 30px;
    margin-top: 20px;
}

.proyecto-card {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.proyecto-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 15px rgba(0,0,0,0.2);
}

.proyecto-imagen {
    width: 100%;
    height: 200px;
    overflow: hidden;
    background-color: #e0e0e0;
}

.proyecto-imagen img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.proyecto-contenido {
    padding: 25px;
}

.proyecto-contenido h2 {
    font-size: 1.5rem;
    color: #2c3e50;
    margin-bottom: 10px;
}

.proyecto-contenido p {
    color: #666;
    margin-bottom: 20px;
    line-height: 1.6;
}

.btn-github {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 20px;
    background-color: #24292e;
    color: white;
    text-decoration: none;
    border-radius: 6px;
    font-weight: 500;
    transition: background-color 0.3s ease;
}

.btn-github:hover {
    background-color: #1a1e22;
}

.btn-github svg {
    flex-shrink: 0;
}

footer {
    background-color: #2c3e50;
    color: white;
    text-align: center;
    padding: 30px 0;
    margin-top: 60px;
}

@media (max-width: 768px) {
    header h1 {
        font-size: 2rem;
    }
    
    .proyectos-grid {
        grid-template-columns: 1fr;
    }
}
"""

# Crear archivo styles.css
css_file = BASE_DIR / 'static' / 'css' / 'styles.css'
css_file.write_text(css_content, encoding='utf-8')
print(f"✓ Archivo creado: static/css/styles.css")

# Contenido del JavaScript
js_content = """// Funcionalidad JavaScript
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    if (hamburger) {
        hamburger.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            const spans = hamburger.querySelectorAll('span');
            spans[0].style.transform = navMenu.classList.contains('active') ? 'rotate(45deg) translate(5px, 5px)' : 'none';
            spans[1].style.opacity = navMenu.classList.contains('active') ? '0' : '1';
            spans[2].style.transform = navMenu.classList.contains('active') ? 'rotate(-45deg) translate(7px, -6px)' : 'none';
        });
    }

    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                const spans = hamburger.querySelectorAll('span');
                spans.forEach(span => span.style.transform = 'none');
                hamburger.querySelectorAll('span')[1].style.opacity = '1';
            }
        });
    });

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scrollTo({ top: target.offsetTop - 70, behavior: 'smooth' });
            }
        });
    });

    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const nombre = document.getElementById('nombre').value;
            alert(`¡Gracias ${nombre}! Tu mensaje ha sido recibido.`);
            contactForm.reset();
        });
    }
});
"""

js_file = BASE_DIR / 'static' / 'js' / 'main.js'
js_file.write_text(js_content, encoding='utf-8')
print(f"✓ Archivo creado: static/js/main.js")

print("\n¡Estructura creada exitosamente!")
print("\nAhora ejecuta:")
print("python manage.py runserver")