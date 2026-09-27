from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

template=PromptTemplate(
    template="generate 3 interesting facts about {topic}",
    input_variables=['topic']
)
llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="conversational",
    max_new_tokens=512,
    provider="novita"
    
)
model1=ChatHuggingFace(llm=llm)
model2=ChatHuggingFace(llm=llm)

prompt1=PromptTemplate(
    template="generate notes for a quiz on \n {text}",
    input_variables={'text'}
)

prompt2=PromptTemplate(
    template="generate a quiz on the \n {text}",
    input_variables={'text'}
)

prompt3=PromptTemplate(
    template="merge the provided notes and quiz into a single document \n notes-> {notes} and quiz->{quiz}",
    input_variables=['notes','quiz']
)

parser= StrOutputParser()

parelell_chain=RunnableParallel(
{
    "notes": prompt1 | model1 | parser,
    "quiz":  prompt2 | model2 |parser,
}

)
merge_chain= prompt3 | model1 | parser

final_chain= parelell_chain | merge_chain

text="""Coronavirus disease 2019 (COVID-19) is a contagious disease caused by the coronavirus SARS-CoV-2. Starting in January 2020, the disease spread worldwide, resulting in the COVID-19 pandemic. In March 2020, the World Health Organization declared COVID-19 a global health emergency; they declared the end of the emergency in May 2023.[7]

The symptoms of COVID‑19 can vary but often include fever,[8] fatigue, cough, shortness of breath, loss of smell, and loss of taste.[9][10][11] Symptoms may begin one to fourteen days after exposure to the virus. At least a third of people who are infected do not develop noticeable symptoms.[12][13] Of those who develop symptoms noticeable enough to be classified as patients, most (81%) develop mild to moderate symptoms (up to mild pneumonia), while 14% develop severe symptoms (dyspnea, hypoxia, or more than 50% lung involvement on imaging), and 5% develop critical symptoms (respiratory failure, shock, or multiorgan dysfunction).[14] Older people have a higher risk of developing severe symptoms and dying. Some people experience persistent symptoms (long COVID), for months or years after infection, including fatigue, cognitive issues and shortness of breath. Damage to organs has been observed in a subset.[15]

COVID‑19 transmission occurs when infectious particles are breathed in or come into contact with the eyes, nose, or mouth. The risk is highest when people are close together, but small airborne particles containing the virus can remain suspended in the air and travel over longer distances, particularly indoors. Transmission can also occur when people touch their eyes, nose, or mouth after touching surfaces or objects that have been contaminated by the virus. People remain contagious for up to 20 days and can spread the virus even if they do not develop symptoms.[16]

There are two common tests to detect a COVID infection. Antigen tests (also called rapid lateral flow tests) can be used at home. A positive test indicates an active infection. However, negative test results are not always accurate, especially when there are no symptoms.[17] Health care providers can perform a more accurate PCR test, which is typically analysed in a laboratory.[18][17]

Several COVID-19 vaccines have been approved and distributed in various countries, many of which have initiated mass vaccination campaigns. Other preventive measures include physical or social distancing, quarantining, ventilation of indoor spaces, use of face masks or coverings in public, covering coughs and sneezes, hand washing, and keeping unwashed hands away from the face. Initial treatment consists of drugs that have been developed to inhibit the virus for those at high risk and symptomatic treatment, managing the disease through supportive care.

The first known case was identified in Wuhan, China, in December 2019.[19] Most scientists believe that the SARS-CoV-2 virus entered into human populations through natural zoonosis, similar to the SARS-CoV-1 and MERS-CoV outbreaks, and consistent with other pandemics in human history.[20][21] Social and environmental factors including climate change, natural ecosystem destruction and wildlife trade increased the likelihood of such zoonotic spillover.[22][23][24][25]

"""

result=final_chain.invoke({"text":text})
print(result)
final_chain.get_graph().print_ascii()