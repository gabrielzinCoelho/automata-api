from fastapi import FastAPI
from controllers import dfa_router

app = FastAPI()
app.include_router(dfa_router)