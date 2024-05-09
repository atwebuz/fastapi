```
pip install sqlalchemy pymysql uvicorn
```

### Docker
```
docker run --name mysqldb -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABSE=test mysql
 ```

```
python -m uvicorn index:app --reload  

python -m uvicorn path.to.index:app --reload

```