from fastapi import HTTPException, status

from .base_dao import BaseDao
from ..database.database import session
from ..models.russian_words import RussianWordOrm


class RussianWordsDao(BaseDao):
    model = RussianWordOrm

    @classmethod
    async def add_word(cls, word: str, eng_word_id: int):
        word = word.lower()
        async with session() as s:
            if await cls.get_all_word(word=word) == []:
                word = RussianWordOrm(word=word, eng_word_id=eng_word_id)
                s.add(word)
                await s.commit()
            else:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                    detail=f"слово {word} уже используется для перевода другого слова")
