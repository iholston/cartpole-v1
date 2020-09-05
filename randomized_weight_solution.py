import gym, random

# multiply weights by observation to determine a move 0 or 1
def get_action(weights, observation):
    action = weights[0]*observation[0] + weights[1]*observation[1] + weights[2]*observation[2] + weights[3]*observation[3]
    return 0 if action < 0 else 1

# Find how long weights keep pole up
def test_weights(env, weights):
    observation = env.reset()
    totalreward = 0
    for _ in range(200):
        action = get_action(weights, observation)
        observation, reward, done, _ = env.step(action)
        totalreward += reward
        if done:
            break
    return totalreward

# Main
gym.logger.set_level(40) # Might need this to remove logger warning https://stackoverflow.com/questions/60149105/userwarning-warn-box-bound-precision-lowered-by-casting-to-float32
env = gym.make('CartPole-v1')
bestweights = None
bestreward = 0

for x in range(1000): # Test 1000 randomized weights and keep track of the best one
    weights = [random.uniform(0,1) * 2 - 1 for _ in range(1,5)] # creates random weights [-1, 1]
    reward = test_weights(env, weights)
    if reward > bestreward:
        bestreward = reward
        bestweights = weights
        if reward == 200: # reward of 200 means it solved the game
            break


print("Random Search solved the environment in: " + str(x + 1) + " episodes.")
print("Weights: " + str(bestweights))



