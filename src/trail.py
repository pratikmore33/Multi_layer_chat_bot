
class ChatBot:
    def __init__(self):
        self.rules = {
            "greeting": {
                "pattern": ["상품 문의", "가입방법", "정보 수정(변경) 및 가입확인서 발급",'사고 접수'],
                "response1": ['풍수해 6(상품)','풍수해 3(상품)'],
                'response2':['풍수해 6(상품)','풍수해 3(상품)'],
                'response3':['정보 수정','가입확인서 발급'],
                'response4':['사고 접수 방법']

            },
            "풍수해 6(상품)": {
                "response": ['가입대상','보상(담보)내용','기타']
            },
            '풍수해 3(상품)':{
                "response": ['가입대상','보상(담보)내용','기타']
            }
     
        }

    # def process_layer_1(self, user_input):
    #     for rule in self.rules["greeting"]["pattern"]:
    #         if rule in user_input.lower():
    #             return self.rules["greeting"]["response"]
    #     return "I'm sorry, I didn't understand. Could you please rephrase?"
    def frist_layer(self,user_input):
        list_of_pattern = self.rules['greeting']['pattern']
        if user_input in list_of_pattern:
            for i in list_of_pattern:
                if i == user_input:
                    number_of_index = list_of_pattern.index(i)
                    if number_of_index == 0:
                        result = '\n'.join(self.rules['greeting']['response1'])
                        return result
                    elif number_of_index == 1:
                        result = '\n'.join(self.rules['greeting']['response2'])
                        return result
                    elif number_of_index == 2:
                        result = '\n'.join(self.rules['greeting']['response3'])
                        return result
                    elif number_of_index == 3:
                        result = '\n'.join(self.rules['greeting']['response4'])
                        return result
                    else:
                        return 'choice is not selected from given choice'
    def second_layer(self,user_input):
        if user_input in self.rules.keys():
            if  user_input == '풍수해 6(상품)':
                result = '\n'.join(self.rules['풍수해 6(상품)']['response'])
                return result
            elif user_input == '풍수해 3(상품)':
                result = '\n'.join(self.rules['풍수해 3(상품)']['response'])
                return result
            else:
                return 'choice is noot given in response '
            

def run_trail(text):
    chat = ChatBot()
    if text in chat.rules['greeting']['pattern']:
        return chat.frist_layer(text)
    elif text in chat.rules.keys():
        return chat.second_layer(text)

print(run_trail('풍수해 6(상품)'))
    




