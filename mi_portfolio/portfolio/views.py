from django.shortcuts import render

def home(request):
    # Información personal para la sección Home/Inicio
    info_personal = {
        'nombre': 'Moises',
        'titulo': 'Data Scientist & Python Developer',
        'descripcion': 'Transformo datos en insights accionables. Especializado en análisis estadístico, machine learning y desarrollo de soluciones basadas en datos.',
        'email': 'moises.ortega@usach.cl',
        'github': 'https://github.com/moisesdatasci',
        'linkedin': 'https://linkedin.com/in/tu-perfil',
        'ubicacion': 'Chile'
    }
    
    # Información para la sección Sobre Mí
    sobre_mi = {
        'titulo': 'Sobre Mí',
        'descripcion_1': 'Soy un profesional apasionado por transformar datos en insights accionables. Con experiencia en análisis estadístico, machine learning y desarrollo de software, me especializo en crear soluciones basadas en datos que resuelven problemas reales.',
        'descripcion_2': 'Mi enfoque combina rigor analítico con creatividad técnica, siempre buscando las mejores prácticas y herramientas para cada proyecto. Me encanta aprender nuevas tecnologías y compartir conocimiento con la comunidad.',
        'experiencia': '3+ años',
        'proyectos_completados': '15+',
        'tecnologias': '10+'
    }
    
    # Habilidades técnicas para Sobre Mí
    habilidades = [
        {'nombre': 'Python', 'nivel': 90},
        {'nombre': 'Data Analysis', 'nivel': 85},
        {'nombre': 'Machine Learning', 'nivel': 80},
        {'nombre': 'SQL', 'nivel': 75},
        {'nombre': 'Django', 'nivel': 70},
        {'nombre': 'Statistics', 'nivel': 85}
    ]
    
    # Lista de proyectos para la sección Proyectos
    proyectos = [
        {
            'id': 1,
            'titulo': 'Análisis Riesgo Sísmico 2015',
            'descripcion': 'Análisis estadístico y visualización de datos de riesgo sísmico utilizando Python y técnicas de ciencia de datos para identificar patrones y zonas de alto riesgo.',
            'github_url': 'https://github.com/moisesdatasci/Analisis_Riesgo_Sismico_2015',
            'imagen': 'proyecto1.jpg',
            'tecnologias': ['Python', 'Pandas', 'Matplotlib', 'Seaborn']
        },
        {
            'id': 2,
            'titulo': 'SpaceX Data Science Project',
            'descripcion': 'Proyecto de análisis predictivo sobre lanzamientos de SpaceX utilizando machine learning y análisis de datos para predecir el éxito de las misiones.',
            'github_url': 'https://github.com/moisesdatasci/SpaceX-Data-Science-Project',
            'imagen': 'proyecto2.jpg',
            'tecnologias': ['Python', 'Scikit-learn', 'SQL', 'API']
        },
        {
            'id': 3,
            'titulo': 'Tarjetas Anki Python',
            'descripcion': 'Generador automático de tarjetas de estudio Anki con Python para optimizar el aprendizaje mediante repetición espaciada.',
            'github_url': 'https://github.com/moisesdatasci/Tarjetas_Anki_Python',
            'imagen': 'proyecto3.jpg',
            'tecnologias': ['Python', 'Automation', 'NLP']
        },
        {
            'id': 4,
            'titulo': 'IPC Chile',
            'descripcion': 'Análisis del Índice de Precios al Consumidor de Chile con visualizaciones interactivas y predicciones de tendencias económicas.',
            'github_url': 'https://github.com/moisesdatasci/IPC_Chile',
            'imagen': 'proyecto4.jpg',
            'tecnologias': ['Python', 'Plotly', 'Time Series', 'Economics']
        },
        {
            'id': 5,
            'titulo': 'Bayes Code',
            'descripcion': 'Implementación de métodos bayesianos y estadística inferencial aplicada a problemas reales de clasificación y predicción.',
            'github_url': 'https://github.com/moisesdatasci/bayes_code',
            'imagen': 'proyecto5.jpg',
            'tecnologias': ['Python', 'Statistics', 'Bayesian', 'PyMC3']
        },
        {
            'id': 6,
            'titulo': 'Fauna Chilena',
            'descripcion': 'Proyecto educativo sobre la biodiversidad de Chile con análisis de datos, clasificación de especies y visualizaciones interactivas.',
            'github_url': 'https://github.com/moisesdatasci/fauna-chilena',
            'imagen': 'proyecto6.jpg',
            'tecnologias': ['Python', 'Data Viz', 'Education', 'Biology']
        }
    ]
    
    # Información de contacto
    contacto_info = {
        'email': 'moises.ortega@usach.cl',
        'github': 'https://github.com/moisesdatasci',
        'linkedin': 'https://linkedin.com/in/tu-perfil',
        'mensaje': '¿Tienes un proyecto en mente? ¡Hablemos! Estoy disponible para colaboraciones y nuevos desafíos.'
    }
    
    context = {
        'info_personal': info_personal,
        'sobre_mi': sobre_mi,
        'habilidades': habilidades,
        'proyectos': proyectos,
        'contacto_info': contacto_info
    }
    
    return render(request, 'home.html', context)