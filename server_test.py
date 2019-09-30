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
    print("Welcome to my page")
    return


if __name__=="__main__":
    app.run(port=5000)