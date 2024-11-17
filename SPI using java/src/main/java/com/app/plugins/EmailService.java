package com.app.plugins;

import com.app.service.NotificationService;

public class EmailService implements NotificationService {
    @Override
    public void sendNotification(String message) {
        System.out.println("Sending Email: " + message);
    }
}
