package com.app;

import com.app.loader.PluginLoader;
import com.app.service.NotificationService;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<NotificationService> plugins = PluginLoader.loadPlugins();

        for (NotificationService plugin : plugins) {
            plugin.sendNotification("Hello from the plugin!");
        }
    }
}
