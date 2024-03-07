import requests
import json
import random
import re

class Agent:
    def __init__(self, agent_id, api_key, temperature, knowledge=None):
        self.agent_id = agent_id
        self.api_key = api_key
        self.temperature = temperature
        self.knowledge = knowledge or {"guess": random.randint(1, 100), "reasoning": "Initial random guess."}
        self.messages = []

    def update_knowledge(self, new_knowledge):
        self.knowledge = new_knowledge

    def make_decision(self, prompt):
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={
                "model": "gpt-4",
                "messages": self.messages + [prompt],
                "temperature": self.temperature
            }
        )

        if response.status_code == 200:
            response_data = response.json()
            new_message_content = response_data['choices'][0]['message']['content']
            self.messages.append({"role": "assistant", "content": new_message_content})

            if "direct information" in new_message_content or "reliable source" in new_message_content:
                guess_match = re.search(r'\b\d+\b', new_message_content)
                if guess_match:
                    new_guess = int(guess_match.group())
                    self.knowledge['guess'] = new_guess
                    self.knowledge['reasoning'] = "I heard from a reliable source."
                    print(f"Agent {self.agent_id} updated knowledge to: {self.knowledge}")
            else:
                # Keep the existing guess and reasoning if the new information isn't considered more credible
                print(f"Agent {self.agent_id} keeps its guess and reasoning unchanged: {self.knowledge}.")
                
            return len(new_message_content.split())
        else:
            print(f"Error in make_decision: {response.text}")
            return 0

"""         if response.status_code == 200:
            response_data = response.json()
            new_message_content = response_data['choices'][0]['message']['content']
            self.messages.append({"role": "assistant", "content": new_message_content})

            # Check if the new information is considered direct or reliable 
            # Not sure if this is actually working!
            if "direct information" in new_message_content or "reliable source" in new_message_content:
                guess_match = re.search(r'\b\d+\b', new_message_content)
                if guess_match:
                    new_guess = int(guess_match.group())
                    self.knowledge['guess'] = new_guess
                    self.knowledge['reasoning'] = "I heard from a reliable source that this is the correct answer."
            else:
                # Keep the existing guess and reasoning if the new information isn't considered more credible
                self.knowledge['guess'] = self.knowledge['guess']
                self.knowledge['reasoning'] = self.knowledge['reasoning']
                print(f"Agent {self.agent_id} keeps its guess and reasoning unchanged.")
            
            print(f"Agent {self.agent_id} updated knowledge to: {self.knowledge}")
            return len(new_message_content.split())
        else:
            print(f"Error in make_decision: {response.text}")
            return 0 """
