#import paho.mqtt.publish as publish

#publish.single("paho/test/single", "payload=test_msg", hostname="192.168.122.131")

import paho.mqtt.publish as publish
import time
i=1
while i < 1000:
    publish.single("Test/test", payload='test', hostname="192.168.122.131", auth = {'username':"quan", 'password':"123"})
    i += 1
    time.sleep(1)
