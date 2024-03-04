# Mapping information flow in LLM groups
## Overview
We present a simple framework for analyzing the diffusion of information through a group of LLM agents. 

This project simulates a multi-agent debate where agents interact in pairs over multiple rounds to share and update their guesses based on the information received from others. One agent starts with the correct answer, and through a series of pairwise interactions, the correct answer should be disseminated throughout the group. The simulation explores how quickly a group can converge to a unanimous decision, given the dynamics of information exchange and the agents' decision-making processes powered by OpenAI's GPT API.

## Features
Pairwise Interactions: Agents are paired randomly without replacement in each round to discuss and potentially update their guesses.
Adaptive Reasoning: Agents use the information received from their pair to reconsider their current guess. They may change their guess if they find the new information more credible, especially if it claims to be from a reliable source.
Convergence Tracking: The system tracks and plots the number of agents with the correct answer after each round, analyzing how group consensus evolves.
API Integration: Utilizes OpenAI's GPT API to simulate agent reasoning, making the interactions dynamic and unpredictable.

## Requirements
API Key: You'll need an API key from OpenAI. Set it in the code where indicated.
Dependencies: This project requires Python 3.x and the following packages: requests, matplotlib, numpy, and re. Install them using pip.

## Usage
To run the simulation, execute the main.py script:
'''
python main.py
'''

