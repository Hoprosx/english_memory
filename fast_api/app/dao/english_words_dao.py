from sqlalchemy import select
from sqlalchemy.orm import joinedload

from .base_dao import BaseDao
from .russian_words_dao import RussianWordsDao
from ..database.database import session
from ..models.english_words import EnglishWordsOrm


class EnglishWordsDao(BaseDao):
    model = EnglishWordsOrm

    @classmethod
    async def add_word_with_translate(cls, eng_word, rus_word):
        async with session() as s:
            eng_word = eng_word.lower()
            rus_word = rus_word.lower()

            word = await cls.get_all_word(word=eng_word)

            if word == []:
                word = EnglishWordsOrm(word=eng_word)
                s.add(word)
                await s.commit()
                await s.refresh(word)
            else:
                word = word[0]

            await RussianWordsDao.add_word(word=rus_word, eng_word_id=word.id)

        return await cls.get_words_with_translate(id=word.id)

    @classmethod
    async def get_words_with_translate(cls, **filter_by):
        async with session() as s:
            query = select(cls.model).options(joinedload(cls.model.russian)).filter_by(**filter_by)
            result = await s.execute(query)
            return result.unique().scalars().all()
