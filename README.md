# Starting project
`pip install venv`

`python3 -m venv .venv`

`.venv\Script\activate`

`$env:FLASK_ENV = "development"`

`flask run` or `python3 -m flask run`

# Database (SQL Alchemy)
create a `database.sqlite` file under the app directory

app/database.sqlite

```python
>> from app import db
>> db.create_all()
```
