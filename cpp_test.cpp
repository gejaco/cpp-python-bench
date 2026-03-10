#include <iostream>
#include <chrono>
#include <vector>
#include <algorithm>

double run_once(long long N) {
    volatile double x = 0.0;
    auto start = std::chrono::high_resolution_clock::now();

    for (long long i = 0; i < N; ++i) {
        x += 0.0000001;
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;

    if (x == -1.0) std::cerr << ""; // keep compiler from removing x
    return elapsed.count();
}

int main() {
    const long long N = 1000000; // 1e6
    const int runs = 1;
    std::vector<double> times;
    times.reserve(runs);

    for (int i = 0; i < runs; ++i) {
        times.push_back(run_once(N));
    }

    double sum = 0.0;
    for (double t : times) sum += t;
    double avg = sum / runs;

    // Print a tiny JSON object to stdout
    std::cout << "{";
    std::cout << "\"language\":\"cpp\",";
    std::cout << "\"iterations\":" << N << ",";
    std::cout << "\"runs\":" << runs << ",";
    std::cout << "\"avg_time\":" << avg;
    std::cout << "}" << std::endl;

    return 0;
}

