import time
from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(response.headers)
    return response


@app.get("/")
async def main():
    return {"message": "Hello World"}


if __name__ == '__main__':
    import uvicorn #web框架 类似go的gin
    uvicorn.run(app, host="127.0.0.1", port=8000)

    '''
    谷歌浏览器输入: http://127.0.0.1:8000 
     显示:
     {"message":"Hello World"}
    
    
INFO:     Started server process [32321] 启动服务器进程[32321]
INFO:     Waiting for application startup.等待应用程序启动。
INFO:     Application startup complete.应用程序启动完成
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
             Uvicorn运行在http://127.0.0.1:8000(按CTRL+C退出)
    '''