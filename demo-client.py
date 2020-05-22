import random
from paho.mqtt.client import *


class ClusterClient(Client):
    """A subclass of paho.mqtt.Client that supports connecting to a cluster of
       mqtt brokers. connect() and connect_async() additionally accept a list
       of hostnames or host/port tuples:

           connect("host1")

           connect(["host1", "host2", "host3"]) # use default port 1883

           connect(["host1", ("host2", 8883), ("host3", 8883)])

       Hosts to connect to are chosen randomly. If a host disappears the client
       automatically connects to another host from the list.
    """

    def __init__(self, client_id="", clean_session=True, userdata=None,
            protocol=MQTTv311, transport="tcp"):
        super().__init__(client_id, clean_session, userdata, protocol, transport)
        self._hosts = []

    def connect_async(self, host, port=1883, keepalive=60, bind_address=""):
        if isinstance(host, (list, tuple)):
            self._hosts = [(t, 1883) if isinstance(t, str) else t for t in host]
        else:
            self._hosts = [(host, port)]

        for host, port in self._hosts:
            if host is None or len(host) == 0:
                raise ValueError('Invalid host.')
            if port <= 0:
                raise ValueError('Invalid port number.')

        host, port = random.choice(self._hosts)

        super().connect_async(host, port, keepalive, bind_address)

    def reconnect(self):
        hosts = self._hosts[:]
        random.shuffle(hosts)
        while True:
            self._host, self._port = hosts.pop(0)
            try:
                return super().reconnect()
            except socket.error:
                if not hosts:
                    raise 