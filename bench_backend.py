from flask import Flask, jsonify, send_from_directory  # Added send_from_directory
import json
import subprocess
import time

app = Flask(__name__, static_folder=".", static_url_path="")  # Serve files from current dir

def run_python_bench():
    N = 1_000_000
    runs = 1
    times = []
    for _ in range(runs):
        x = 0.0
        start = time.perf_counter()
        for _ in range(N):
            x += 0.0000001
        end = time.perf_counter()
        if x == -1.0:
            print("impossible")
        times.append(end - start)
    avg_time = sum(times) / runs
    return {
        "language": "python",
        "iterations": N,
        "runs": runs,
        "avg_time": avg_time,
    }

def run_cpp_bench():
    result = subprocess.run(["./cpp_test"], capture_output=True, text=True, check=True)
    return json.loads(result.stdout.strip())

@app.route("/")
def index():  # ← NEW: serves index.html
    return send_from_directory(".", "index.html")

@app.route("/api/bench", methods=["GET"])
def bench():
    cpp_result = run_cpp_bench()
    py_result = run_python_bench()
    return jsonify({"cpp": cpp_result, "python": py_result})

if __name__ == "__main__":
    app.run(debug=True)

