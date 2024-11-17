from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, recipient, message):
        """Send a notification to the recipient."""
        pass
