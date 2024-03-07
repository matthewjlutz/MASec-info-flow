from agent import Agent
from debate_manager import DebateManager
import matplotlib.pyplot as plt
import numpy as np
import json
import os
from dotenv import load_dotenv


# Load API key as environment variable from .env file
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# Adjustable parameters
NUM_AGENTS = 16
CORRECT_ANSWER = "42"
NUM_ROUNDS = 4
NUM_SIMULATIONS = 4
TEMPERATURE = 0.2  # Adjust this to control the randomness of responses

def initialize_agents(num_agents=NUM_AGENTS, api_key=API_KEY, temperature=TEMPERATURE):
    # Initialize and return a list of Agent objects
    return [Agent(agent_id=i+1, api_key=api_key, temperature=temperature) for i in range(num_agents)]

def run_simulation(num_agents=NUM_AGENTS, correct_answer=CORRECT_ANSWER, num_rounds=NUM_ROUNDS, api_key=API_KEY, temperature=TEMPERATURE):
    # Initialize agents and the debate manager, then start the debate rounds
    agents = initialize_agents(num_agents, api_key, temperature)
    debate_manager = DebateManager(agents, correct_answer, num_rounds)
    correct_counts_over_time = debate_manager.start_debate_rounds()
    return correct_counts_over_time

def run_multiple_simulations(num_simulations=NUM_SIMULATIONS, num_agents=NUM_AGENTS, correct_answer=CORRECT_ANSWER, num_rounds=NUM_ROUNDS, api_key=API_KEY, temperature=TEMPERATURE):
    # Run multiple simulations and collect the results
    all_results = []
    for _ in range(num_simulations):
        result = run_simulation(num_agents, correct_answer, num_rounds, api_key, temperature)
        all_results.append(result)
    return all_results

def plot_simulation_results(all_results):
    # Plot the results of multiple simulations
    rounds = np.arange(len(all_results[0]) + 1)
    adjusted_results = [np.insert(result, 0, 1) for result in all_results]
    
    for result in adjusted_results:
        plt.plot(rounds, np.array(result) / NUM_AGENTS, marker='o', linestyle='-', color='lightcoral', alpha=0.5)
    
    mean_results = np.mean(adjusted_results, axis=0) / NUM_AGENTS
    plt.plot(rounds, mean_results, marker='o', linestyle='-', color='orangered', label='Mean Proportion')
    
    plt.title('Proportion of Agents with Correct Answer Over Rounds')
    plt.xlabel('Round')
    plt.ylabel('Proportion with Correct Answer')
    plt.ylim(0, 1.1)
    plt.xticks(rounds)
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    all_results = run_multiple_simulations()
    plot_simulation_results(all_results)

if __name__ == "__main__":
    main()