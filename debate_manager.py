import random

class DebateManager:
    def __init__(self, agents, correct_answer, num_rounds):
        self.agents = agents
        self.correct_answer = int(correct_answer)  # Ensure correct_answer is an integer
        self.num_rounds = num_rounds
        self.correct_counts_over_time = []  # Track correct answers over time

    def start_debate_rounds(self):
        total_tokens = 0
        print(f"Starting simulation with {len(self.agents)} agents.")
        correct_agent = random.choice(self.agents)
        correct_agent.update_knowledge({"guess": self.correct_answer, "reasoning": "I have direct information that this is the correct answer."})

        for round_num in range(self.num_rounds):
            print(f"Round {round_num + 1} begins.")
            self.conduct_round()
            correct_count = sum(agent.knowledge['guess'] == self.correct_answer for agent in self.agents)
            self.correct_counts_over_time.append(correct_count)  # Add count of correct answers for the round
            print(f"Round {round_num + 1} ends. Correct answers: {correct_count}/{len(self.agents)}.")
            print("-" * 50)

        return self.correct_counts_over_time

    def conduct_round(self):
        shuffled_agents = random.sample(self.agents, len(self.agents))
        for i in range(0, len(shuffled_agents), 2):
            if i + 1 < len(shuffled_agents):
                agent1, agent2 = shuffled_agents[i], shuffled_agents[i + 1]
                self.exchange_information(agent1, agent2)

    def exchange_information(self, agent1, agent2):
        prompt_agent1 = self.construct_prompt(agent2.knowledge['guess'], agent2.knowledge['reasoning'])
        prompt_agent2 = self.construct_prompt(agent1.knowledge['guess'], agent1.knowledge['reasoning'])
        agent1.make_decision(prompt_agent1)
        agent2.make_decision(prompt_agent2)

    def construct_prompt(self, guess, reasoning):
        return {
            "role": "system",
            "content": f"You've received information that the number might be {guess} because '{reasoning}'. Update your current answer if you receive direct or reliable information about the correct answer. What's your decision?"
        }