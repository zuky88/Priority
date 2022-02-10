import server
import datetime

class Processor():
    def __init__(self) -> None:
        pass
    def set2queue(self, name, num, data):
        msg = []
        msg.append(num)
        msg.append(data)
        server.msg_send(msg)
        now = datetime.datetime.now()
        print('[{0}]send:{1}, {2}'.format(name, msg, now))
