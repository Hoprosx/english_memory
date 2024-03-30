from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base
from app.models.types import primary_key


class RussianWordOrm(Base):
    __tablename__ = "russian_words"

    id: Mapped[primary_key]
    word: Mapped[str]
    eng_word_id: Mapped[int] = mapped_column(ForeignKey("english_words.id"))

    english: Mapped["EnglishWordsOrm"] = relationship()
