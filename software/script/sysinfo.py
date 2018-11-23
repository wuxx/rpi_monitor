#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime
import psutil
import socket
import fcntl
import struct

from demo_opts import get_device
from luma.core.render import canvas

def bytes2human(n):
    """
    >>> bytes2human(10000)
    '9K'
    >>> bytes2human(100001221)
    '95M'
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = int(float(n) / prefix[s])
            return '%s%s' % (value, s)
    return "%sB" % n

def disk_usage(dir):
    usage = psutil.disk_usage(dir)
    return "SD: avail %s/%s %.0f%%" \
           % (bytes2human(usage.free), bytes2human(usage.total), usage.percent)

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = "null"
    try:
        ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
        )[20:24])
    except:
        #print "error"
        pass
    finally:
        return ip

def sysinfo(device, draw):
    #print device.bounding_box

    now = datetime.datetime.now()
    #today_date = now.strftime("%d %b %y")
    today_date = now.strftime("%Y-%m-%d")
    today_time = now.strftime("%H:%M:%S")
    today = "%s %s" %(today_date, today_time)

    disk_info = disk_usage('/');
    ip = "IP: [%s]" %(get_ip_address('wlan0'));

    #draw.rectangle(device.bounding_box, outline="white")
    draw.rectangle((0, 0, 127, 63), outline="white")

    draw.text((3, 3), today, fill="yellow")
    #draw.text((10, 40), today_time, fill="yellow")
    draw.line((0, 17, 127, 17), fill="yellow")

    draw.text((3, 18), disk_info, fill="yellow")

    draw.line((0, 33, 127, 33), fill="yellow")

    draw.text((3, 35), ip, fill="yellow")

    draw.line((0, 50, 127, 50), fill="yellow")

    draw.text((3, 52), "status: running", fill="yellow")

def main():
    device = get_device()
    while True:
        with canvas(device) as draw:
            sysinfo(device, draw)
        time.sleep(5)
        #print "draw"


    time.sleep(60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
