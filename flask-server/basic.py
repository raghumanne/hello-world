from flask import request

def base():
    url = request.url
    surl = url.split("/")[-2:]
    if surl == 'basic':
        return 'hii'
