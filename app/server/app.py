from fastapi import FastAPI, Request, status, Response

app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root(request: Request, response: Response):
    params = request.query_params
    if params['status'] == "500":
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "Something went wrong:( Please check you service ASAP."}
    else:
        return {"message": "Your service is up and running. No worries!"}
