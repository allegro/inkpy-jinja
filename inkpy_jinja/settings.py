import os

REDIS_HOST = os.environ.get('REDIS_PORT_6379_TCP_ADDR', '127.0.0.1')
REDIS_PORT = int(os.environ.get('REDIS_PORT_6379_TCP_PORT', 6379))
REDIS_DB = int(os.environ.get('REDIS_PORT_6379_DB', 0))
