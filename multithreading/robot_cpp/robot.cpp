
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

enum STATE {
    STATE_LEFT,
    STATE_RIGHT
};

std::mutex mutex;
std::condition_variable cv;
STATE state = STATE_LEFT;

void run_both(STATE expected_state, STATE next_state, const std::string &message) {
    while (true) {
        std::unique_lock<std::mutex> lock(mutex);
        cv.wait(lock, [=]{ return state == expected_state; });
        std::cout << message << std::endl;
        state = next_state;
        cv.notify_all();
    }
}

// void run_right() {
//     while (true) {
//         std::unique_lock<std::mutex> lock(mutex);
//         cv.wait(lock, []{ return state == STATE_RIGHT; });
//         std::cout << "right" << std::endl;
//         state = STATE_LEFT;
//         cv.notify_all();
//     }
// }

int main(int argc, const char * argv[]) {

    std::cout << "hello" << std::endl;

    std::thread producer{run_both, STATE_LEFT, STATE_RIGHT, "left"};
    std::thread consumer{run_both, STATE_RIGHT, STATE_LEFT, "right"};

    producer.join();
    consumer.join();

    std::cout << "done" << std::endl;

    return 0;
}

