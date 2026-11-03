from fastapi import  FastAPI


#创建 FastApi 实例

app=FastAPI()

#定义API接口--->该函数的返回值表示API接口的返回数据,接口访问路径为/，请求方式为GET

@app.get("/")
def read_root():
    return {"Hello": "World"}



#定义API接口--->该函数的返回值表示API接口的返回数据,接口访问路径为/users，请求方式为GET

@app.get("/users")
def get_users():
    return [
        {"id": 1,"name": "张三"},
        {"id": 2,"name": "李四"},
        {"id": 3,"name": "王五"},
    ]



#启动服务--->uvicorn:Python中的轻量级Web服务器，用于运行FastAPI应用
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)













