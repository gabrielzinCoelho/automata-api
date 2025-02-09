from fastapi import FastAPI
from controllers import dfa_router, npda_router, dtm_router

app = FastAPI()
app.include_router(dfa_router)
app.include_router(npda_router)
app.include_router(dtm_router)