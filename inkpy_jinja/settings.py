import os


def bool_from_env(var, default: bool=False) -> bool:
    """Helper for converting env string into boolean.

    Returns bool True for string values: '1' or 'true', False otherwise.
    """
    def str_to_bool(s: str) -> bool:
        return s.lower() in ('1', 'true')

    os_var = os.environ.get(var)
    if os_var is None:
        # as user expect
        return default
    else:
        return str_to_bool(os_var)


REDIS_MASTER_IP = None
REDIS_MASTER_PORT = None

REDIS_SENTINEL_ENABLED = bool_from_env('REDIS_SENTINEL_ENABLED', False)
if REDIS_SENTINEL_ENABLED:
    from redis.sentinel import Sentinel

    # REDIS_SENTINEL_HOSTS env variable format: host_1:port;host_2:port
    REDIS_SENTINEL_HOSTS = os.environ['REDIS_SENTINEL_HOSTS'].split(';')
    REDIS_CLUSTER_NAME = os.environ['REDIS_CLUSTER_NAME']

    sentinel = Sentinel(
        [tuple(s_host.split(':')) for s_host in REDIS_SENTINEL_HOSTS],
        socket_timeout=float(
            os.environ.get('REDIS_SENTINEL_SOCKET_TIMEOUT', 0.2)
        )
    )
    REDIS_MASTER_IP, REDIS_MASTER_PORT = sentinel.discover_master(
        REDIS_CLUSTER_NAME
    )

REDIS_HOST = REDIS_MASTER_IP or os.environ.get('REDIS_HOST', '127.0.0.1')
REDIS_PORT = REDIS_MASTER_PORT or int(os.environ.get('REDIS_PORT', 6379))
REDIS_DB = int(os.environ.get('REDIS_DB', 0))
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', None)
REDIS_SSL = bool_from_env('REDIS_SSL', False)
