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
weights = [random.uniform(0,1) * 2 - 1 for _ in range(1,5)] # creates random weights [-1, 1]
noise_scaling = 0.1

for x in range(2000): # Create noise and add to weights, if reward increases keep the changes, else increase noise scaler and try again
    new_weights = [weights[x] + ((random.uniform(0,1) * 2 - 1) * noise_scaling) for x in range(4)]
    reward = test_weights(env, new_weights)
    if reward > bestreward:
        bestreward = reward
        bestweights = new_weights
        weights = new_weights
        if reward == 200: # reward of 200 means it solved the game
            break
    else:
        noise_scaling += 0.0005 # if this is too big it devolves into pure random weight selection

print("The hill climb algo solved the environment in: " + str(x + 1) + " episodes.")
print("Weights: " + str(bestweights))



