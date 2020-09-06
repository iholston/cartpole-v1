# cartpole-v1
Three solutions to the [cartpole-v1](https://gym.openai.com/envs/CartPole-v1/) environment.   
  
## Synopsis
1. Brute force, randomized weight selection 
     This method randomly generates a set of weights and tests them to see if they solve the environment. If yes, done. If no, repeat.

2. Simple hill climbing solution that gradually improves randomly selected weights  
     This method randomly generates weights then adds 'noise' (random weights discounted by the noise_scaler) and checks for improvement in total reward. If there is improvement repeat, if not increase the noise_scaler and try again.

3. A policy gradient solution
The brute force method randomly creates weights until the environment is solved. The hill climbing solution starts with random weights and sublty introduces noise to improve the weight sets rather than randomly selecting weights. It is important to note that if the noise is introduced aggressively the algorithm is essentially the same as random selection. And lastly the policy gradient method...

## References
http://kvfrans.com/simple-algoritms-for-solving-cartpole/, kevin frans
