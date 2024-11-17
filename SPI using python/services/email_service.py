from notification_interface import NotificationService

class EmailService(NotificationService):
    def send_notification(self, recipient, message):
        print(f"Sending Email to {recipient}: {message}")
