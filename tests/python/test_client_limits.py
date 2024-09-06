import signal

import utils

def test_user_limit():
    utils.pgcat_limited_start()

    # Open 2 connections for limited user
    limited_user_conns = [utils.connect_db_limited(user='limited') for _ in range(2)]

    # Validate 3rd connection fails
    conn, cur = utils.connect_db_limited(user='limited')
    cur.execute("SELECT 1;")
    utils.cleanup_conn(conn, cur)

    # Validate unlimted user is still able to conect
    conn, cur = utils.connect_db_limited(user='unlimited')
    cur.execute("SELECT 1;")
    utils.cleanup_conn(conn, cur)

    # close 1 connection for limited user
    conn, cur = limited_user_conns.pop(-1)
    utils.cleanup_conn(conn, cur)

    # validate limited user is able to connect lagain
    conn, cur = utils.connect_db_limited(user='limited')
    cur.execute("SELECT 1;")

    utils.pg_cat_send_signal(signal.SIGINT)


def test_server_limit():
    utils.pgcat_limited_start()

    # TODO Open 1 connection for limited user
    # TODO Open 3 connection for unlimited user

    # TODO Validate that new connection is rejected

    # TODO Close one connection for unlimited user
    # TODO Validate unlimited user is able to connect again

    utils.pg_cat_send_signal(signal.SIGINT)
