# cartpole-v1
Three solutions to the [cartpole-v1](https://gym.openai.com/envs/CartPole-v1/) environment. 1) brute force, randomized weight selection, 2) simple hill climbing solution that gradually improves randomly selected weights, and 3) a policy gradient solution.

## References
http://kvfrans.com/simple-algoritms-for-solving-cartpole/, kevin frans

## Synopsis
The brute force method randomly creates weights until the environment is solved. The hill climbing solution starts with random weights and sublty introduces "noise" to the weights to improve them rather than randomly selecting weights. It is important to note that if the noise is added too aggressively the algorithm essentially is the same as random selection. And lastly the policy gradient method...
