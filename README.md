# HiQA
**Paper**: [HiQA: A Hierarchical Contextual Augmentation RAG for Massive Documents QA](https://arxiv.org/abs/2402.01767), arXiv:2402.01767.

HiQA provides a comprehensive toolkit for document processing, enabling the segmentation of documents into sections, enrichment with metadata, and embedding for in-depth analysis. It leverages a multi-route retrieval system to identify relevant knowledge in response to specific queries. This knowledge, along with the query, is then processed by a large language model (LLM) to generate answers. Although document processing incurs some initial costs, this investment significantly improves the quality of the results.

## Usage
Ensure your environment meets the following prerequisites:
- Python version 3.9
- Install dependencies from `requirements.txt` using the following command: 
  \```
  pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
  \```
- Set your OpenAI API key in the environment variables.
- To start the demo, execute:
  \```
  PYTHONUNBUFFERED=1 nohup streamlit run app_streamlit.py --server.port 8080 --server.address 0.0.0.0 > logs/run.log 2>&1 &
  \```
  Note: Before running the above command, manually create a `logs` directory.

## Creating Your Own Dataset
To build a dataset, follow these steps:
1. Utilize the tools in the `build_tool` directory.
2. Begin with a PDF file that is text-extractable.
3. **Step 1**: Convert the PDF to a well-formatted markdown file using `pdf2md`, leveraging the `gpt-4-turbo-preview (0125)` model.
4. **Step 2**: Convert the markdown file into a CSV file with `md2csv`, organizing content into sections with hierarchical metadata, and labeling tables.
5. **Step 3**: Use `section2embedding` to append embedding vectors to sections.
6. **Step 4**: Place all processed CSV files into a dataset directory. Load this dataset in `knowledge_client.py` for querying in the `app_streamlit.py` demo.
   Note: File names and titles are processed through Named Entity Detection models to generate critical keywords, which are stored in `utils.filter.critic_keywords`.

## Extracting and Searching Images from a PDF
For image processing:
1. In `image_service`, execute load, build, and commit operations to create an `/indexes` directory for Whoosh.
2. Use VLM (such as [Ollama -> Llama:34b](https://github.com/ollama/ollama/) ) to generate descriptions for each extracted image.
3. Image searches can be conducted using `app_streamlit.search_images_from_response`.
