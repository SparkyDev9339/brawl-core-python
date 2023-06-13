from DataStream.Writer import Writer


class ServerHelloMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20100
        self.player = player

    def encode(self):
        self.writeInt(24)
        for i in range(24):
            self.writeByte(i)