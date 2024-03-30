from fastapi import FastAPI, Body
from .dao.english_words_dao import EnglishWordsDao
from .schemas.word import Translate, Word

app = FastAPI()


@app.get('/words')
async def get_all_words() -> list[Word]:
    return await EnglishWordsDao.get_all_word()


@app.get('/words/translated')
async def get_all_translated_words() -> list[Translate]:
    return await EnglishWordsDao.get_words_with_translate()


@app.post('/words')
async def add_word(eng_word: str, russian_word: str):
    return await EnglishWordsDao.add_word_with_translate(eng_word, russian_word)
