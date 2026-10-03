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


@app.post("/compose")
def compose_email(
    recipient: str,
    request: str
):

    return service.compose_email(
        recipient,
        request
    )