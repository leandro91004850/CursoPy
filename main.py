from typing import Union
from fastapi import FastAPI, Path
from easygoogletranslate import EasyGoogleTranslate
from fastAPI.english import English

app = FastAPI()

@app.get("/translate/{english_text}")
def read_root(english_text: str = Path(..., description="The text to be translated")):
    translator = EasyGoogleTranslate()
    result = translator.translate(english_text, target_language='pt')
    
    return {
            "Português": result, 
            "English": english_text
    }

@app.get("/generation/quiz")
def read_item():
    return English.english_learning()

@app.get("/generation/quiz/{item_id}/{traducao}")
async def update_item(item_id: str, traducao: str):
    return English.update_item(item_id, traducao)
