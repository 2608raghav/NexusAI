from shared.core.base_agent import BaseAgent


class EmailService(BaseAgent):

    def __init__(self):

        super().__init__(
            name="Email Agent",
            version="1.0"
        )

    def send_email(
        self,
        recipient: str,
        subject: str,
        body: str
    ):

        print("Email Agent received request")

        print("Recipient:", recipient)
        print("Subject:", subject)
        print("Body:", body)

        return {
            "status": "success",
            "message": "Email request received",
            "recipient": recipient,
            "subject": subject,
            "body": body
        }