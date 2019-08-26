from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from main import app
from models import db, User

manager = Manager(app)      # 初始化管理器
migrate = Migrate(app, db)  # 初始化 migrate

manager.add_command('server', Server())
manager.add_command('db', MigrateCommand)   # 添加db命令，并与MigrateCommand 绑定


@manager.shell
def make_shell_context():
    """
    Create a python CLI

    :return: Default import object
    :type: `Dict`
    """
    return dict(
        app = app,
        db = db,
        User = User
    )

if __name__ == '__main__':
    manager.run()