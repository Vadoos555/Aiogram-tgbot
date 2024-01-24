from app.database.model import async_session
from app.database.model import User
from sqlalchemy import select


async def set_user(user_id, username):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.user_id==user_id))
        if not user:
            session.add(User(user_id=user_id, username=username))
            await session.commit()
            