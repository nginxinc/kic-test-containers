#!/usr/bin/env python3

import socket
import subprocess

import psutil


def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 1))  # connect() for UDP doesn't send packets
        local_ip_address = s.getsockname()[0]
        print("local ip:", local_ip_address)
        return local_ip_address
    except Exception:
        print("Unable to get Hostname and IP")


def stop(ps_object, including_parent=True):
    # subprocess.call(['kill', '-9', str(pid)])
    parent = psutil.Process(ps_object.pid)
    children = parent.children(recursive=True)
    for child in children:
        child.kill()
    gone, still_alive = psutil.wait_procs(children, timeout=5)
    if including_parent:
        parent.kill()
        parent.wait(5)


def start():
    # print "Webserver started. Log file: %s" % logfile
    # ip = get_ip()
    ip = "0.0.0.0"
    bind = ip + ":8080"
    p = subprocess.Popen(
        [
            "gunicorn",
            "--bind",
            bind,
            "-w",
            str(15),
            # this parameter for test stability
            # "--keep-alive", "2",
            "--error-logfile",
            "webserver-error.log",
            "flaskserver:app",
        ],
        shell=False,
    )
    return p


if __name__ == "__main__":
    p = start()
    # input("Press Enter to stop webserver")
    # stop(p)
