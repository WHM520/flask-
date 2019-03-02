from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db, models

app = create_app("development")

manager = Manager(app)


# 将app与db关联起来
Migrate(app, db)

# 添加迁移命令到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    print(app.url_map)
    manager.run()
