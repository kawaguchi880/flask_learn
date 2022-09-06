# flask_learn

以下のコマンドでenvの仮想環境を作る
```
>activate env
```
サーバーを起動する
```
(env) >flask run
```

http://127.0.0.1:5000/にアクセス．

FlaskアプリがSQLAlchemyを使えるようにするための初期化
```
flask db init
```

modelsからmigrationを作成する
```
flask db migrate
```

migrationを実行しDBを作成する
```
flask db upgrade
```
