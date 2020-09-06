# cartpole-v1
Three solutions to the [cartpole-v1](https://gym.openai.com/envs/CartPole-v1/) environment.   
  
## Synopsis
1. Random Weight Selection.  
     This method randomly generates a set of weights and tests them to see if they solve the environment. If yes, done. If no, repeat.

2. Hill Climbing Algorithm.  
     This method randomly generates weights, then adds 'noise' (random weights discounted by the noise_scaler) and checks for improvement in the total reward. If there is improvement repeat, if not increase the noise_scaler and try again.

3. Policy Gradient Solution.  
     Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...

## References
http://kvfrans.com/simple-algoritms-for-solving-cartpole/, kevin frans
