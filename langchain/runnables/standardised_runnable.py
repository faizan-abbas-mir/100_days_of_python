import random
from abc import ABC,abstractmethod

class Runnable(ABC):
    @abstractmethod
    def invoke(input_data):
        pass



class Naklillm(Runnable):
    def __init__(self):
        print('llm created')

    def predict(self,prompt):

        response_list=['delhi is the capital',
                       'ipl is a cricket league',
                       'AI stands for srtificial intelegence ']
        return {"response": random.choice(response_list)}

    def invoke(self,prompt):
        response_list=['delhi is the capital',
                               'ipl is a cricket league',
                               'AI stands for srtificial intelegence ']
        return {"response": random.choice(response_list)}

class NaklipromptTemplate(Runnable):
    def __init__(self,template,input_variable):
        self.template=template
        self.input_variable=input_variable

    def format(self,input_dict):
        return self.template.format(**input_dict)

    def invoke(self,input_dict):
         return self.template.format(**input_dict)
    

class Runableconnector(Runnable):
    def __init__(self,runnable_list):
        self.runnable_list=runnable_list

    def invoke(self,input_data):
        for each in self.runnable_list:
            input_data=each.invoke(input_data)
        return input_data


class Stroutputparser(Runnable):
    def __init__(self):
        pass
    def invoke(self,input_data):
        return input_data['response'].upper()


llm=Naklillm()
template=NaklipromptTemplate(
   template="write a {length} poem about {topic}",
    input_variable=['topic']
)
parser=Stroutputparser()
chain=Runableconnector([template,llm,parser])

result=chain.invoke( {'topic':'tajmahal','length':'long'} )

print(result)


new_template1=NaklipromptTemplate(
    template='write a joke abot the topic{topic}',
    input_variable=['topic']
)

new_template2=NaklipromptTemplate(
    template='explain the joke \n {response}',
    input_variable=['response']
)
joke_chain=Runableconnector([new_template1,llm,new_template2,llm,parser])

result=joke_chain.invoke({'topic':'monkey'})
print(result)