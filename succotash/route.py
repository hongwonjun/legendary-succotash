# -*- coding: utf-8 -*-
from flask import jsonify, request

from succotash import app

@app.route("/", methods=['POST', 'GET'])
def main():
  print("=== Header ===")
  print(request.headers)

  print("=== Parameter ===")
  print(request.query_string)

  print("=== Body ===")
  print(request.json)

  return jsonify(request.json)
