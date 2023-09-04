from getpass import getpass
from langchain.llms import Clarifai
from langchain import PromptTemplate, LLMChain


class ClarifiLLM:
    def __init__(
            self, 
            clarifai_pat: str = "890cdb0cb5aa4795ba51af9670120a1e", 
            user_id="meta", 
            app_id="Llama-2", 
            model_id="llama2-70b-chat"
        ):
        self.CLARIFAI_PAT = clarifai_pat
        self.USER_ID = user_id
        self.APP_ID = app_id
        self.MODEL_ID = model_id
        self.clarifai_llm = Clarifai(
            pat=self.CLARIFAI_PAT, 
            user_id=self.USER_ID, 
            app_id=self.APP_ID, 
            model_id=self.MODEL_ID
        )
        self.template = """Question: {question}\n\nAnswer: Let's think step by step."""
        self.prompt = PromptTemplate(template=self.template, input_variables=["question"])
        self.llm_chain = LLMChain(prompt=self.prompt, llm=self.clarifai_llm)
    
    def generate(self, question):
        return self.llm_chain.run(question)
    
    def __call__(self, question):
        return self.generate(question)
