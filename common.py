PACKAGE_SIZE = 256

tag1 = b'<html>'
tag2 = b'</html>'

def encrypt(data):
    return b''.join([tag1 + data[index:index+1] + tag2 for index in range(len(data))])

def decrypt(data):
    return data.replace(tag1, b'').replace(tag2, b'')

def partial_send(conn, data):
    """
    The problem is when we send data, the package may be cut at the middle of an html tag "<html>" which corrupts the
    data as it's not computer after merging the data points.
    :param conn:
    :param data:
    :return:
    """
    num_packages = len(data) // 100 + 1 * (len(data) % 100 == 0)

    for num_pack in range(num_packages):
        conn.sendall(data[num_pack*PACKAGE_SIZE:(num_pack+1)*PACKAGE_SIZE])

