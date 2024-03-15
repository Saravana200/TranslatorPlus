import asyncio
from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
import uvicorn

from translator import entry

app = FastAPI()

templates = Jinja2Templates(directory="views")


#rendering website
@app.get("/")
async def test(request:Request):
    return templates.TemplateResponse("website.html",context={"request":request})


#translating and understanding sentiment and providing ways to reply back
@app.post("/translate")
def test(request:Request,textToTranslate:str=Form(...),translationDirection:str=Form(...)):
    
    resp=asyncio.run(entry(textToTranslate,translationDirection)) # running translation and llm task simultaneously
    
    return templates.TemplateResponse("website.html",context={"request":request,"translated_text":resp,"original_text":textToTranslate})

if(__name__) == '__main__':
        uvicorn.run(
        "server:app",
        host    = "127.0.0.1",
        port    = 8036, 
        reload  = True
    )