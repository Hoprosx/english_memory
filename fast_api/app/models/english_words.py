from sqlalchemy.orm import Mapped, relationship

from app.database.database import Base
from app.models.types import primary_key


class EnglishWordsOrm(Base):
    __tablename__ = 'english_words'

    id: Mapped[primary_key]
    word: Mapped[str]

    russian: Mapped[list["RussianWordOrm"]] = relationship()
