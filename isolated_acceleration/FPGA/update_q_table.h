#ifndef UPDATE_Q_TABLE_H
#define UPDATE_Q_TABLE_H

#define NUM_STATES 5
#define NUM_ACTIONS 4
#define ALPHA 0.1f
#define GAMMA 0.9f

extern float Q_table[NUM_STATES][NUM_ACTIONS];

float update_q_table(
    unsigned int state,
    unsigned int action,
    float reward,
    const float next_q_values[NUM_ACTIONS]
);

#endif
