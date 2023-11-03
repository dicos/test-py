from src.models import SessionLocal

class PostRepository:
    def __init__(self):
        self.db = SessionLocal()

    pass