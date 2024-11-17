from notification_interface import NotificationService

class SMSService(NotificationService):
    def send_notification(self, recipient, message):
        print(f"Sending SMS to {recipient}: {message}")
