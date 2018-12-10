import sys
sys.path.extend(['/root/rce'])

from common import bottle
from manager import Manager

manager = Manager()


@bottle.route('/', method='POST')
def execute():
    commands = bottle.request.body.readlines()
    manager.execute_commands(commands)


@bottle.route('/clean')
def clean():
    manager.clear_executors()


bottle.run(host='0.0.0.0', port=50201)
