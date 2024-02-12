import random

class DebateManager:
    def __init__(self, agents, correct_answer, api_key):
        self.agents = agents
        self.correct_answer = int(correct_answer)  # Ensure correct_answer is an integer
        self.api_key = api_key
        self.total_rounds = 8
        self.correct_counts_over_time = []

    def start_debate_rounds(self):
        total_tokens = 0
        print(f"Starting simulation with {len(self.agents)} agents.")

        # Assign correct answer to one agent
        correct_agent = random.choice(self.agents)
        correct_agent.update_knowledge({"guess": self.correct_answer, "reasoning": "I have direct information about the correct answer."})

        for round_num in range(self.total_rounds):
            print(f"Round {round_num + 1} begins.")
            tokens, correct_count = self.conduct_round()
            total_tokens += tokens
            self.correct_counts_over_time.append(correct_count)  # Add the count for this round to the list
            print(f"Round {round_num + 1} ends. Correct answers: {correct_count}/{len(self.agents)}.")
            print("-" * 50)

        return total_tokens, self.correct_counts_over_time

    def conduct_round(self):
        tokens_used = 0
        correct_count = 0
        
        # Shuffle agents for random pairing
        shuffled_agents = random.sample(self.agents, len(self.agents))
        
        # Iterate through agents in pairs
        for i in range(0, len(shuffled_agents), 2):
            if i + 1 < len(shuffled_agents):
                agent1 = shuffled_agents[i]
                agent2 = shuffled_agents[i + 1]
                print(f"\nAgent {agent1.agent_id} is interacting with Agent {agent2.agent_id}")
                
                # Exchange information and make decisions based on the new information
                tokens_used += self.exchange_information(agent1, agent2)
            else:
                # Handle the case where there's an odd number of agents
                # Example: the last agent might not interact or could perform a self-review
                print(f"Agent {shuffled_agents[i].agent_id} has no partner this round.")

        # Count how many agents have the correct answer now
        for agent in self.agents:
            guess = agent.knowledge.get('guess')
            
            if guess is not None and int(guess) == int(self.correct_answer):
                correct_count += 1

        return tokens_used, correct_count
    
    def exchange_information(self, agent1, agent2):
        tokens_used = 0
        # Exchange information logic with prompts:
        prompt_agent1 = {
            "role": "system",
            "content": f"Agent {agent1.agent_id}, you've received information that the number might be {agent2.knowledge['guess']} because '{agent2.knowledge['reasoning']}'. Update your current answer if you receive direct or reliable information about the correct answer. What's your decision?"
        }
        prompt_agent2 = {
            "role": "system",
            "content": f"Agent {agent2.agent_id}, you've received information that the number might be {agent1.knowledge['guess']} because '{agent1.knowledge['reasoning']}'. Update your current answer if you receive direct or reliable information about the correct answer. What's your decision?"
        }

        # Make decisions based on the prompts
        tokens_used += agent1.make_decision(prompt_agent1)
        tokens_used += agent2.make_decision(prompt_agent2)

        return tokens_used


