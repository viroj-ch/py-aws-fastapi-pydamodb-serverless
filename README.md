
~~~
pip install fastapi
pip install uvicorn
pip install mangum

uvicorn app.main:app --reload

http://127.0.0.1:8000/search?query=x
~~~
or
~~~
pip install -r app/requirements.txt
serverless plugin install -n serverless-offline
serverless offline

http://localhost:3000/dev/search?query=x

http://localhost:3000/dev/docs
~~~
