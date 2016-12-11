from flask_script import Manager, Server

from flask_mongo_engine_sample.app import create_app

manager = Manager(create_app)
manager.add_option('-c', '--config', default='Development', required=False,
                   choices=('Production', 'Development', 'Testing'), dest='config')
manager.add_command('runserver', Server(threaded=True))

if __name__ == '__main__':
    manager.run()
