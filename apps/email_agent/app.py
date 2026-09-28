from fastapi import FastAPI

from .service import EmailService


app = FastAPI(
    title="Email Agent"
)


service = EmailService()


@app.get("/")
def root():

    return {
        "message": "Email Agent is running"
    }


@app.post("/send")
def send_email(
    recipient: str,
    subject: str,
    body: str
):

    return service.send_email(
        recipient,
        subject,
        body
    )