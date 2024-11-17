package com.app.loader;

import com.app.service.NotificationService;
import java.util.ArrayList;
import java.util.List;
import java.util.ServiceLoader;

public class PluginLoader {
    public static List<NotificationService> loadPlugins() {
        List<NotificationService> plugins = new ArrayList<>();
        ServiceLoader<NotificationService> serviceLoader = ServiceLoader.load(NotificationService.class);

        for (NotificationService plugin : serviceLoader) {
            plugins.add(plugin);
        }

        return plugins;
    }
}
