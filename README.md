# 一个简单的demo，演示celery在爬虫开发中的应用

### 使用说明

* 运行 scripts/generate_orm_code.py 生成models/live.py 中的 ORM 代码
* 运行 bin/run_mysql.sh bin/run_redis.sh bin/run_celery.sh 分别启动mysql、redis以及celery
* 运行 bin/generate_mysql_table.sql 创建数据库以及数据表
* python3 app.py 启动知乎 live 爬虫

### TODO

- [x] 使用脚本生成ORM表模块
- [x] 使用脚本生成建表sql
- [x] 引入celery，使用任务队列做数据处理并入库
