#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# app.py
#######################

import os

from flask import Flask, request, jsonify

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.route("/countries",methods=['GET','POST'])

def get_countries():

    if request.method == 'POST':

        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201

    else:

        return jsonify(countries)
        #return countries

if __name__ == '__main__':

    homeDir = os.environ['HOME']
    userID = homeDir.split("/")[-1]

    if userID[2] == "6":
        port = "2" + userID[3:7]
    if userID[2] == "7":
        port = "3" + userID[3:7]

    print("Personal API Port: %s" %(port))

    app.run(port=int(port),host='0.0.0.0',use_reloader=False)
