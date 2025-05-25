from .start import start_handler
from .admin import admin_handler
from .settings import settings_handler
from .search import inline_search_handler

def register_handlers(app):
    start_handler(app)
    admin_handler(app)
    settings_handler(app)
    inline_search_handler(app)
