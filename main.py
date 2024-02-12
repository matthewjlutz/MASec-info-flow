from agent import Agent
from debate_manager import DebateManager
import matplotlib.pyplot as plt
import numpy as np
import json

API_KEY = "XXXXXX"

NUM_AGENTS = 16
CORRECT_ANSWER = "42"

def initialize_agents(num_agents=NUM_AGENTS, api_key=API_KEY):
    return [Agent(agent_id=i+1, api_key=api_key) for i in range(num_agents)]

def run_simulation(num_agents=NUM_AGENTS, correct_answer=CORRECT_ANSWER, api_key=API_KEY):
    agents = initialize_agents(num_agents, api_key)
    debate_manager = DebateManager(agents, correct_answer, api_key)
    _, correct_counts_over_time = debate_manager.start_debate_rounds()
    return correct_counts_over_time

def run_multiple_simulations(num_simulations, num_agents=NUM_AGENTS, correct_answer=CORRECT_ANSWER, api_key=API_KEY):
    all_results = []
    for _ in range(num_simulations):
        result = run_simulation(num_agents, correct_answer, api_key)
        all_results.append(result)
    return all_results

def plot_simulation_results(all_results):
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
    plt.grid(False)
    plt.show()

def main():
    num_simulations = 6
    all_results = run_multiple_simulations(num_simulations)
    plot_simulation_results(all_results)

if __name__ == "__main__":
    main()
