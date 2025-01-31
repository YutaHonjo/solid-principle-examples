# pylint: disable=missing-docstring, useless-super-delegation
class UserService:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save_user(self):
        print(f"User {self.username} saved to database.")


class EmailService:
    def __init__(self, sender_name, sender_email):
        self.sender_name = sender_name
        self.sender_email = sender_email

    def send_email(self, recipient_email, message):
        print(f"Sending email from {self.sender_name} <{self.sender_email}> to {recipient_email}: {message}")

    def bulk_send_email(self, recipient_emails, message):
        for recipient_email in recipient_emails:
            self.send_email(recipient_email, message)

# TODO: add logging method
# MEMO: 分けていると、責務を管理しやすい
# class LoggerService:
#     def log(self, message):
#         print(f"Log: {message}")

user = UserService("john_doe", "john@example.com")
user.save_user()
email = EmailService(user.username, user.email)
email.send_email("test@gmail.com", "Hello!")
