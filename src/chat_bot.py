class ChatBot:
    def __init__(self):
        self.rules = {
            "greeting": {
                "pattern": ["hi", "hello", "hey"],
                "response": "Hello! How can I assist you today?"
            },
            "sport": {
                "response": "Great! What sport would you like to choose? (cricket, football, baseball)"
            },
            "package": {
                "cricket": {
                    "response": "What package would you like for cricket? (package1, package2)"
                },
                "football": {
                    "response": "What package would you like for football? (package1, package2)"
                },
                "baseball": {
                    "response": "What package would you like for baseball? (package1, package2)"
                }
            },
            "price": {
                "cricket": {
                    "package1": "price for package1 for cricket is $100",
                     "package2":"price for package2 for cricket is $200"
                },
                "football": {
                    "package1": "price for package1 for footbal is $300",
                     "package2":"price for package2 for football is $400"
                }
            },
            "farewell": {
                "pattern": ["bye", "goodbye"],
                "response": "Thank you! Have a great day!"
            }
        }

    def process_layer_1(self, user_input):
        for rule in self.rules["greeting"]["pattern"]:
            if rule in user_input.lower():
                return self.rules["greeting"]["response"]
        return "I'm sorry, I didn't understand. Could you please rephrase?"

    def process_layer_2(self, user_input):
        return self.rules["sport"]["response"]

    def process_layer_3(self, user_input):
        for sport in self.rules["package"]:
            if sport in user_input.lower():
                return self.rules["package"][sport]["response"]
        return "I'm sorry, I didn't catch that. Please select a sport from the available options."

    def process_layer_4(self, user_input):
        for sport in self.rules["package"]:
            if sport in user_input.lower():
                selected_sport = sport
                for package in self.rules["package"][selected_sport]:
                    if package in user_input.lower():
                        return f"The cost of {package} for {selected_sport} is $XX."
                return "I'm sorry, I didn't understand. Could you please repeat the package you mentioned?"
        return "I'm sorry, I didn't catch that. How can I assist you further?"

# Usage
chat_bot = ChatBot()

# user_input = input("User: ")
# print(chat_bot.process_layer_1(user_input))

# user_input = input("User: ")
# print(chat_bot.process_layer_2(user_input))

# user_input = input("User: ")
# print(chat_bot.process_layer_3(user_input))

# user_input = input("User: ")
# print(chat_bot.process_layer_4(user_input))

print(type(chat_bot.rules.keys()))

for i in chat_bot.rules.keys():
    print(i)
