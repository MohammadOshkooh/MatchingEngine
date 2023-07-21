import requests

# while True:
#     api_url = "http://127.0.0.1:8000/api/test/"
#     response = requests.get(api_url)
#     print(response.text)


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    print('f')
    return {"message": "Hello World"}
