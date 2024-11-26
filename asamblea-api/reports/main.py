app = FastAPI()

@app.get("/reports/results")
async def get_results():
    return get_vote_results()