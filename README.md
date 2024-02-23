# HiQA
Hierarchical Contextual Augmentation RAG for Massive Documents QA.

HiQA offers a suite of tools designed for document processing, which includes segmenting documents into sections, enhancing them with metadata, and embedding them for detailed analysis. 
This is followed by employing a multi-route retrieval system to search for relevant knowledge in response to a specific question. 
The identified knowledge, alongside the question, is then fed into a large language model (LLM) to generate an answer. 
While processing documents might incur some costs, this one-time process substantially enhances the quality of the outcomes.  

# How to use
1. Python version == 3.9
2. pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
3. Set your own OpenAI key
4. Start demo: PYTHONUNBUFFERED=1 nohup streamlit run app_streamlit.py --server.port 8080 --server.address 0.0.0.0 > logs/run.log 2>&1 &
