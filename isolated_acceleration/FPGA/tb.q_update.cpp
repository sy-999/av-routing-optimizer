#include <iostream>
#include <cassert>
#include <chrono> //  Header file for measuring time
#include "update_q_table.h"

void test_update_q_table() {
    // Initialise the Q-table
    for (int i = 0; i < NUM_STATES; i++) {
        for (int j = 0; j < NUM_ACTIONS; j++) {
            Q_table[i][j] = 0.0f;
        }
    }

    // Test parameter
    unsigned int state = 2;
    unsigned int action = 1;
    float reward = 3.5f;
    float next_q_values[NUM_ACTIONS] = {1.2f, 2.3f, 0.7f, 1.8f};

    // Execute 100,000 iterations
    int iterations = 100000;
    float last_updated_q = 0.0f;




    auto start_time = std::chrono::high_resolution_clock::now();

    for (int i = 0; i < iterations; i++) {
        last_updated_q = update_q_table(state, action, reward, next_q_values);
    }


    auto end_time = std::chrono::high_resolution_clock::now();

        // Calculate the execution time (in seconds)
    auto elapsed_time = std::chrono::duration<double>(end_time - start_time).count();





    // Calculate the expected value
    float max_next_q = 2.3f;
    float expected_q = 10*(0.0f + ALPHA * (reward + GAMMA * max_next_q - 0.0f));



    // Print

    std::cout << "After " << iterations << " iterations:" << std::endl;
    std::cout << "Last Updated Q-value: " << last_updated_q << std::endl;
    std::cout << "Expected Q-value: " << expected_q << std::endl;

    // Print the Q-table
    std::cout << "Final Q-table:" << std::endl;
    for (int i = 0; i < NUM_STATES; i++) {
        for (int j = 0; j < NUM_ACTIONS; j++) {
            std::cout << Q_table[i][j] << " ";
        }
        std::cout << std::endl;
    }


    std::cout << "Total Execution Time: " << elapsed_time << " seconds" << std::endl;
    std::cout << "Average Time per Update: " << (elapsed_time / iterations) << " seconds" << std::endl;

=
}

int main() {
    test_update_q_table();
    return 0;
}
