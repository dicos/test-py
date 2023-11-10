from datetime import datetime, timedelta

from src.models import SessionLocal

from src.exceptions import NotFound
from src.story.models import Stories, StoryViews
from src.user.models import User

class StoryRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create_story(self, *, user: User, text: str) -> int:
        story = Stories(user_id=user.id, text=text)
        self.db.add(story)
        self.db.commit()
        return story.id

    def view_story(self, *, user: User, story_id: int) -> int:
        if not self.db.query(Stories).filter(Stories.id==story_id).scalar():
            self.db.rollback()
            raise NotFound
        view = StoryViews(story_id=story_id, user_id=user.id)
        self.db.add(view)
        self.db.commit()
        return view.id

    def delete_old_stories(self):
        yesterday = datetime.now() - timedelta(days=1)
        self.db.query(Stories).filter(Stories.created_at<yesterday).delete()
        self.db.commit()


story_repository = StoryRepository()
