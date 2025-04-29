import os

if __name__ == "__main__":
    port = os.getenv("PORT", "5005")
    os.system(f"rasa run --enable-api --cors '*' --port {port}")
