import time

def run_python_bench():
    N = 100_000_000  # 1e8
    runs = 5
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
