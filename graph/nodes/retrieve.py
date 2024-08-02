from typing import Any, Dict 

from graph.state import GraphState
from ingestion import retriever 

def retrieve(state: GraphState) -> Dict[str, Any]: 
    print("---Retrieve---") 
    question=state["question"]
    
    documents=retriever.invoke(question) 
    
    return {"documents": documents, "question": question} # Updates the state/GraphState object