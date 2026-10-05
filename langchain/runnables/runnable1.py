import random

class Naklillm:
    def __init__(self):
        print('llm created')

    def predict(self,prompt):

        response_list=['delhi is the capital',
                       'ipl is a cricket league',
                       'AI stands for srtificial intelegence ']
        return {"response": random.choice(response_list)}







class NaklipromptTemplate:
    def __init__(self,template,input_variable):
        self.template=template
        self.input_variable=input_variable

    def format(self,input_dict):
        return self.template.format(**input_dict)



template=NaklipromptTemplate(
    template="write a {length} poem about {topic}",
    input_variable=['topic','length']

)


prompt=template.format({'topic':'india','length':'short'})

model=Naklillm()
print(prompt)
resut=model.predict(prompt)
print(resut)
