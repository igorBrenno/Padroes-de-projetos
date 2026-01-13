from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass

class NotificationEmail(Notification):
    def send(self, message: str) -> None:
        print(f"Enviando email com mensagem: {message}")

class NotificationSMS(Notification):
    def send(self, message: str) -> None:
        print(f"Enviando SMS com mensagem: {message}")

class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass

class EmailFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return NotificationEmail()
    
class SMSFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return NotificationSMS()
    
def client_code(factory: NotificationFactory, message: str) -> None:
    notification = factory.create_notification()
    notification.send(message)

if __name__ == "__main__":
    print("Enviando notificação por email:")
    email_factory = EmailFactory()
    client_code(email_factory, "Olá via Email!")

    print("\nEnviando notificação por SMS:")
    sms_factory = SMSFactory()
    client_code(sms_factory, "Olá via SMS!")