# -*- coding: utf-8 -*-
import json
from flask import jsonify, request

from succotash import app

@app.route("/", methods=['POST', 'GET'])
def main():
  print("=== Header ===")
  print(request.headers)

  print("=== Parameter ===")
  print(request.query_string)

  print("=== Body ===")
  print(json.dumps(request.json, indent=2, sort_keys=True))
  
  return jsonify(request.json)
