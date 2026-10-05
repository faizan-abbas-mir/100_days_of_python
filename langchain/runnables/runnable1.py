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

model=Naklillm()


"""prompt=template.format({'topic':'india','length':'short'})
print(prompt)


result=model.predict(prompt)
print(result)"""



class Naklillmchain:
    def __init__(self,prompt,llm):
        self.llm=llm
        self.prompt=prompt

    def run(self,input_dict):
       final_prompt= self.prompt.format(input_dict)
       print({'final prompt':final_prompt})
       result=self.llm.predict(final_prompt)


       return result['response']


chain=Naklillmchain(template,model)

print(chain.run({'length':'short','topic':'tajmahal'}))