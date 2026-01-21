import os
from pathlib import Path
if 'RENDER' in os.environ:
    # Configuración para producción en Render
    DEBUG = False
    ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']
    
    # Archivos static en producción
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    
    # Usar SQLite incluso en Render (más simple para free tier)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    # Configuración para desarrollo local
    DEBUG = True
    ALLOWED_HOSTS = []