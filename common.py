PACKAGE_SIZE = 256

tag1 = b'<html>'
tag2 = b'</html>'
tag3 = b'a'

data_received = 0

def encrypt(data):
    return b''.join([b'a' + data[index:index+1] for index in range(len(data))])

def decrypt(data):
    global data_received

    output_data = b''
    for index in range(len(data)):
        data_received = data_received + 1

        # skip tag 3 => b'a'
        if data_received % 2 == 0:
            output_data = output_data + data[index:index+1]

    return output_data

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

