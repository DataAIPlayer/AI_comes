#code: utf-8

from flask import Flask,request
import requests
import json
import random
import openai
import os

app = Flask(__name__)

@app.route('/message',methods = ['POST'])
def mess():  # put application's code here
    message = request.json.get('msg')
    openai.api_key = "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" #修改这里为自己申请的api_key
    messages = [
        {"role": "system", "content": "你是一个智能助理"},
    ]
    messages.append({"role": "user", "content": message})
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": message}]
    )
    #messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})
    res = {
            "resmsg":completion,
            "code":200
            }
    return res