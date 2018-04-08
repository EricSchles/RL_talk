import gym

def try_env(game):
    env = gym.make(game)
    env.reset()
    for _ in range(1000):
        env.render()
        env.step(env.action_space.sample())

games = ["CartPole-v0",
         "MountainCar-v0",
         "MsPacman-v0",
         "Hopper-v2"]

for game in games:
    try_env(game)
