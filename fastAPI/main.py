from typing import Union
from fastapi import FastAPI, Path
from easygoogletranslate import EasyGoogleTranslate

app = FastAPI()


@app.get("/translate/{english_text}")
def read_root(english_text: str = Path(..., description="The text to be translated")):
    translator = EasyGoogleTranslate()
    result = translator.translate(english_text, target_language='pt')
    return {
            "Português": result, 
            "English": english_text
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}