# Mapping information spread in LLM groups
## Overview
We present a simple framework for analyzing the diffusion of information through a group of LLM agents.  

This project simulates a multi-agent debate where agents interact in pairs over multiple rounds to share and update their guesses based on the information received from others. One agent starts with the correct answer, and through a series of pairwise interactions, the correct answer should be disseminated throughout the group. The simulation explores how quickly a group can converge to a unanimous decision, given the dynamics of information exchange and the agents' decision-making processes powered by OpenAI's GPT API.

## Features
Pairwise Interactions: Agents are paired randomly without replacement in each round to discuss and potentially update their guesses.
Adaptive Reasoning: Agents use the information received from their pair to reconsider their current guess. They may change their guess if they find the new information more credible, especially if it claims to be from a reliable source.
Convergence Tracking: The system tracks and plots the number of agents with the correct answer after each round, analyzing how group consensus evolves.
API Integration: Utilizes OpenAI's GPT API to simulate agent reasoning, making the interactions dynamic and unpredictable.

## Requirements
### Dependencies
This project requires Python 3.9+ and packages `dotenv`, `matplotlib`, `numpy`, and `requests`, which can be installed using pip:

```
pip install python-dotenv matplotlib numpy requests
```

### API Keys
This project makes API calls to OpenAI's GPT models, and can be modified to use other models. Use of these APIs requires the corresponding API keys, which you can provide as environment variables, stored in a '.env' file located in the project directory or your home directory. (This file is ignored by git by default). The file is a simple text file with key=value pairs, e.g.:

```
OPENAI_API_KEY=sk-...
OPENAI_API_ORG=org-...
ANTHROPIC_API_KEY=sk-ant-...
...
```

These variables can be imported from the `.env` file using the `dotenv` package as follows:

```
import dotenv
dotenv.load_dotenv()
```

## Usage
To run, execute the main.py script:

```
python main.py
```

