#include "update_q_table.h"
#include <hls_math.h>

float Q_table[NUM_STATES][NUM_ACTIONS];

float update_q_table(
    unsigned int state,
    unsigned int action,
    float reward,
    const float next_q_values[NUM_ACTIONS]
) {
    // Calculate the maximum Q-value
    float max_next_q = 0.0f;
    for (int i = 0; i < NUM_ACTIONS; i++) {
        if (next_q_values[i] > max_next_q) {
            max_next_q = next_q_values[i];
        }
    }

    // Update the Q-value
    float updated_q = Q_table[state][action] + ALPHA * (reward + GAMMA * max_next_q - Q_table[state][action]);
    Q_table[state][action] = updated_q;

    return updated_q; // Return the updated Q-value
}
