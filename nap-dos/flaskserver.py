#!/usr/bin/env python
import time
from multiprocessing import Process

from flask import Flask, Response, jsonify, make_response, redirect, request

app = Flask(__name__)
global_log = []


@app.route("/good_path.html")
def good():
    if request.args.get("response_delay_seconds", ""):
        time.sleep(float(request.args.get("response_delay_seconds", "")))

    if request.args.get("response_status_code", ""):
        response_status_code = request.args.get("response_status_code", "")
    else:
        response_status_code = "200"

    if request.args.get("response_add_header", ""):
        response_add_header = request.args.get("response_add_header", "")
    else:
        response_add_header = "I am GOOD"

    response = make_response("Good path!", response_status_code)
    response.headers.extend({"X-Actor-Class": response_add_header})
    return response


@app.route("/bad_path.html")
def bad():
    if request.args.get("response_delay_seconds", ""):
        time.sleep(float(request.args.get("response_delay_seconds", "")))
    else:
        time.sleep(1)

    if request.args.get("response_status_code", ""):
        response_status_code = request.args.get("response_status_code", "")
        response = make_response("Bad path!", response_status_code)
    else:
        # response_status_code = '500'
        print("response code is not set, using default")
        response = make_response("Bad path!")

    if request.args.get("response_add_header", ""):
        response_add_header = request.args.get("response_add_header", "")
    else:
        response_add_header = "I am BAD"

    # response = make_response('Bad path!', response_status_code)
    response.headers.extend({"X-Actor-Class": response_add_header})
    return response


@app.route("/")
def index():
    logrequest(request)
    return "<!DOCTYPE html><html><head><title>Title of the document</title></head><body>Fast index!</body></html>"


def logrequest(req):
    myrequest = {}
    myrequest["time"] = int(time.time())
    myrequest["type"] = "request"
    # // myrequest.id = req.requestId;
    myrequest["url"] = str(req.url)
    myrequest["method"] = str(req.__dict__["environ"]["REQUEST_METHOD"])
    myrequest["httpVersion"] = str(req.__dict__["environ"]["SERVER_PROTOCOL"])
    myrequest["params"] = dict(req.args)
    myrequest["headers"] = dict(req.headers)
    myrequest["payload"] = req.get_json()
    print('myrequest["params"]: %s' % (myrequest["params"]))
    print('myrequest["hearders"]: %s' % (myrequest["headers"]))
    print('myrequest["payload"]: %s' % (myrequest["payload"]))
    global_log.append(myrequest)
