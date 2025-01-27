import logging
import socket

from flask import Flask, Response, jsonify
from prometheus_client import Gauge, generate_latest, CollectorRegistry
import psutil
import os

# Create a Flask app
app = Flask(__name__)

# Create a registry for custom metrics
registry = CollectorRegistry()

# Define Prometheus metrics
cpu_used_gauge = Gauge('cpu_used', 'CPU usage in percentage', registry=registry)
ram_used_gauge = Gauge('ram_used', 'RAM usage percentage', registry=registry)
ram_available_gauge = Gauge('ram_available', 'RAM available percentage', registry=registry)

@app.route('/ip')
def ip():
    response_json = {"ip": socket.gethostbyname(socket.gethostname()), "name": socket.gethostname()}
    return jsonify(response_json)

@app.route('/metrics')
def metrics():
    # Collect system stats
    cmd = """
    grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }'
    """
    cpu_used = round(float(os.popen(cmd).readline()), 1)
    ram_used = psutil.virtual_memory().percent
    ram_available = round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, 1)

    # Update Prometheus metrics
    cpu_used_gauge.set(cpu_used)
    ram_used_gauge.set(ram_used)
    ram_available_gauge.set(ram_available)
    # Generate and return the metrics in Prometheus format
    return Response(generate_latest(registry), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
