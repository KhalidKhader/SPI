from plugin_loader import load_plugins
import services

if __name__ == "__main__":
    plugins = load_plugins(services)
    for plugin in plugins:
        plugin.send_notification("user@example.com", "This is a test message")
