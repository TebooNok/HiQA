# HiQA
Hierarchical Contextual Augmentation RAG for Massive Documents QA

# How to use
1. Python version == 3.9
2. pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
3. Start demo: PYTHONUNBUFFERED=1 nohup streamlit run app_streamlit.py --server.port 8080 --server.address 0.0.0.0 > logs/run.log 2>&1 &