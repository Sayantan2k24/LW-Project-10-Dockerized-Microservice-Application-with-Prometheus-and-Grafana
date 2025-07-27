from flask import Flask, jsonify, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time, random

app = Flask(__name__)

REQUEST_COUNT = Counter('requests_total', 'Total HTTP Requests', ['endpoint'])
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency', ['endpoint'])

@app.route("/")
def home():
    REQUEST_COUNT.labels("/").inc()
    start = time.time()
    time.sleep(0.1)  # simulate quick response
    REQUEST_LATENCY.labels("/").observe(time.time() - start)
    return jsonify({"msg": "Hello!"})

@app.route("/slow")
def slow():
    REQUEST_COUNT.labels("/slow").inc()
    start = time.time()
    delay = random.uniform(0.5, 2.0)
    time.sleep(delay)  # simulate slow task
    REQUEST_LATENCY.labels("/slow").observe(time.time() - start)
    return jsonify({"msg": f"Finished after {round(delay, 2)}s"})

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
