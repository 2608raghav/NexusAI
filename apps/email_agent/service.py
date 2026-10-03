import json
import httpx

from shared.core.base_agent import BaseAgent


class EmailService(BaseAgent):

    def __init__(self):

        super().__init__(
            name="Email Agent",
            version="1.0"
        )

        self.ollama_url = "http://127.0.0.1:11434/api/chat"
        self.model = "qwen3:8b"

    def compose_email(
        self,
        recipient: str,
        request: str
    ):

        print("Email Agent received request")

        print("Recipient:", recipient)
        print("Request:", request)

        prompt = f"""
You are a professional email writing assistant.

Write a clear, polite and professional email based on the user's request.

Recipient:
{recipient}

User request:
{request}

Return ONLY valid JSON in this exact format:

{{
    "subject": "email subject",
    "body": "complete email body"
}}

Do not add markdown.
Do not add explanations.
"""

        try:

            response = httpx.post(
                self.ollama_url,
                json={
                    "model": self.model,
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "stream": False
                },
                timeout=120.0
            )

            response.raise_for_status()

            data = response.json()


            email_data = json.loads(content)

            content = data["message"]["content"]

            print("Generated email:")
            print(content)

            return {
                "status": "success",
                "recipient": recipient,
                "subject": email_data["subject"],
                "body": email_data["body"],
                
            }

        except httpx.TimeoutException:

            return {
                "status": "error",
                "message": "Email generation timed out"
            }

        except httpx.RequestError:

            return {
                "status": "error",
                "message": "Could not connect to Ollama"
            }