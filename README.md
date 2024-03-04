# Mapping information spread in LLM groups
## Overview
We present a simple framework for analyzing the diffusion of information through a group of LLM agents.  

This project simulates a multi-agent debate where agents interact in pairs over multiple rounds to share and update their guesses based on the information received from others. One agent starts with the correct answer, and through a series of pairwise interactions, the correct answer should be disseminated throughout the group. The simulation explores how quickly a group can converge to a unanimous decision, given the dynamics of information exchange and the agents' decision-making processes powered by OpenAI's GPT API.

## Structure
The project consists of three Python scripts:
* `debate_manager.py` defines the `DebateManager` class, which manages the simulation of a group debate where agents iteratively exchange information, via pairwise interactions.
* `agent.py`
* `main.py` 

## Requirements
### Dependencies
This project requires Python 3.9+ and packages `dotenv`, `matplotlib`, `numpy`, and `requests`, which can be installed using pip:

```
pip install python-dotenv matplotlib numpy requests
```

### API Keys
This project requires OpenAI API access to use the GPT models (and can be modified for other LLMs). Using these APIs requires the corresponding API keys, which should be provided as environment variables stored in a '.env' file in the project directory or your home directory. This file, ignored by git for security, is a text file with key=value pairs, e.g.:

```
OPENAI_API_KEY="sk-..."
OPENAI_API_ORG="org-..."
ANTHROPIC_API_KEY="sk-ant-..."
...
```

These variables are imported from the `.env` file using the `dotenv` package:

```
import dotenv
dotenv.load_dotenv()
```

## Usage
To run, execute the main.py script:

```
python main.py
```

