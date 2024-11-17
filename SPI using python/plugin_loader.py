import importlib
import pkgutil
from notification_interface import NotificationService  

def load_plugins(package):
    """Dynamically load all modules in a package."""
    plugins = []
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f"{package.__name__}.{module_name}")
        for attr in dir(module):
            cls = getattr(module, attr)
            if isinstance(cls, type) and issubclass(cls, NotificationService) and cls is not NotificationService:
                plugins.append(cls())
    return plugins
