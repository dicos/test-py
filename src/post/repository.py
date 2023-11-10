from sqlalchemy.exc import NoResultFound, IntegrityError
from sqlalchemy import desc
from sqlalchemy import func
from src.exceptions import NotFound, AlreadyExists

from src.models import SessionLocal
from src.post.models import Posts, PostLikes, PostComments
from src.user.models import User


class PostRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create_post(self, *, user: User, code: str) -> int:
        post = Posts(user_id=user.id, code=code)
        self.db.add(post)
        try:
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise AlreadyExists('Already exists')
        return post.id

    def add_like(self, *, user: User, code: str) -> int:
        try:
            post = self.db.query(Posts).filter(Posts.code==code).one()
        except NoResultFound:
            self.db.rollback()
            raise NotFound

        like = PostLikes(post_id=post.id, user_id=user.id)
        self.db.add(like)
        self.db.commit()
        return like.id

    def get_post_list(self, *, username: str):
        """
        Что-то типа вот такого:
        SELECT
  posts.code AS posts_code,
  count(post_likes.post_id) AS likes,
  (SELECT
      post_comments.text AS text
    FROM
      post_comments
    WHERE
      post_comments.parent_id IS NULL AND post_comments.post_id = posts.id
    ORDER BY
      post_comments.updated_at DESC
    LIMIT 1) AS anon_1_text,
  (SELECT
      post_comments.text AS text
   FROM
      post_comments
      WHERE
      post_comments.parent_id IS NULL AND post_comments.post_id = posts.id
      ORDER BY
      post_comments.updated_at DESC
      LIMIT
      1, 1
  ) AS anon_2_text
FROM
  posts
  LEFT OUTER JOIN post_likes ON post_likes.post_id = posts.id
  INNER JOIN users ON posts.user_id = users.id
WHERE
  users.login = 'dmitry'
GROUP BY
  post_likes.post_id
        """
        comment_1 = self.db.query(PostComments.post_id, PostComments.text, PostComments.updated_at) \
            .filter(PostComments.parent_id==None)\
            .order_by(desc(PostComments.updated_at)) \
            .limit(1)\
            .subquery()
        comment_2 = self.db.query(PostComments.post_id, PostComments.text)\
            .join(comment_1, comment_1.c.updated_at>PostComments.updated_at) \
            .filter(PostComments.parent_id==None, PostComments.post_id==comment_1.c.post_id)\
            .order_by(desc(PostComments.updated_at)) \
            .limit(1)\
            .subquery()
        return self.db.query(
            Posts.code,
            func.count(PostLikes.post_id),
            comment_1.c.text,
            comment_2.c.text) \
        .outerjoin(comment_1, comment_1.c.post_id==Posts.id)\
        .outerjoin(comment_2, comment_2.c.post_id==Posts.id)\
        .outerjoin(PostLikes, PostLikes.post_id==Posts.id)\
        .join(User, Posts.user_id==User.id)\
        .filter(User.login==username)\
        .group_by(Posts.id)\
        .all()

    def add_comment(self, *, user: User, code: str, text: str, parent_id: int | None) -> int:
        try:
            post = self.db.query(Posts).filter(Posts.code == code).one()
        except NoResultFound:
            raise NotFound
        comment = PostComments(post_id=post.id, user_id=user.id, text=text)
        if parent_id is not None:
            check_parent = self.db.query(PostComments)\
                .filter(PostComments.id==parent_id, PostComments.post_id==post.id)\
                .scalar()
            if not check_parent:
                raise NotFound
            comment.parent_id = parent_id

        self.db.add(comment)
        self.db.commit()
        return comment.id


post_repository = PostRepository()
