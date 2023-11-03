from src.models import SessionLocal

class StoryRepository:
    def __init__(self):
        self.db = SessionLocal()

    pass