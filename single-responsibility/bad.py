# pylint: disable=missing-docstring, useless-super-delegation
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def send_email(self, recipient_email, message):
        print(
            f"Sending email from {self.email} to {recipient_email}: {message}"
        )

    def bulk_send_email(self, recipient_emails, message):
        for recipient_email in recipient_emails:
            self.send_email(recipient_email, message)

    def save_user(self):
        print(f"User {self.username} saved to database.")

    # TODO: add logging method
    # MEMO: 責務が多すぎて、管理が難しい
    # def log(self, message):
    #     print(f"Log: {message}")


user = User("john_doe", "john@example.com")
user.save_user()
user.send_email("test@gmail.com", "Hello!")
