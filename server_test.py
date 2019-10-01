#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:31:09 2019

@author: donghoon
"""

import os
from flask import Flask, request, jsonify
import json

app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome"


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=80)