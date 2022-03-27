import random
from game import Agent
from game import Directions

class DumbAgent(Agent):
    "An agent that goes East until it can't"
    def getAction(self, state):
        "The agent always goes East"
        print("Location: ",state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        if Directions.EAST in state.getLegalPacmanActions():
            print("Going East.")
            return Directions.EAST
        else:
            print("Stopping.")
            return Directions.STOP

class RandomAgent(Agent):
    def getAction(self, state):
        print("Location: ", state.getPacmanPosition())
        print("Action available: ", state.getLegalPacmanActions())
        availableAction = state.getLegalPacmanActions()
        betterAction = availableAction[:-1]
        print("Better Action: ", betterAction)
        action = random.choice(betterAction)
        return action

class ReflexAgent(Agent):
    def getAction(self, state):
        print("Location: ", state.getPacmanPosition())
        print("Action available: ", state.getLegalPacmanActions())
        availableAction = state.getLegalPacmanActions()
        betterAction = availableAction[:-1]
        print("Better Action: ", betterAction)

        while(len(betterAction) != 0):
            currentNumFood = state.getNumFood()
            action = betterAction[0]
            nextState = state.generatePacmanSuccessor(action)
            nextNumFood = nextState.getNumFood()
            if currentNumFood != nextNumFood: return action
            else:
                betterAction = betterAction[1:]
        
        betterAction = availableAction[:-1]
        action = random.choice(betterAction)
        return action




        
