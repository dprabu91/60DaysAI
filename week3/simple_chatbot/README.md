# 📄 Simple PDF RAG Chatbot

A powerful and intuitive web-based chatbot that leverages Retrieval-Augmented Generation (RAG) to answer questions based on PDF documents. Built with Streamlit, LangChain, and OpenAI's GPT-4o-mini model.

## 🚀 Features

- **📤 Easy PDF Upload**: Simply upload any PDF file through an intuitive interface
- **🤖 AI-Powered Answers**: Uses OpenAI's GPT-4o-mini model for intelligent responses
- **🔍 Intelligent Retrieval**: Implements FAISS vector store for semantic document retrieval
- **📚 Source Transparency**: View the exact document chunks used to generate answers
- **⚡ Real-time Processing**: Get instant responses based on your PDF content
- **🛡️ Context-Aware**: Ensures answers are grounded in the uploaded document

## 📋 How It Works

1. **Document Loading**: Upload a PDF file
2. **Text Chunking**: Document is split into manageable chunks with overlapping context
3. **Embeddings**: Text is converted to semantic embeddings using Hugging Face models
4. **Vector Storage**: Embeddings are stored in FAISS for fast similarity search
5. **Retrieval**: When you ask a question, the system retrieves relevant chunks
6. **Generation**: GPT-4o-mini generates an answer using the retrieved context

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Fast web app framework
- **LLM Framework**: [LangChain](https://www.langchain.com/) - Modern chain orchestration
- **Large Language Model**: OpenAI's [GPT-4o-mini](https://openai.com)
- **Embeddings**: [Hugging Face](https://huggingface.co/) - sentence-transformers/all-MiniLM-L6-v2
- **Vector Database**: [FAISS](https://github.com/facebookresearch/faiss) - Similarity search
- **PDF Processing**: PyPDF2

## 📦 Installation

### Prerequisites
- Python 3.9+
- OpenAI API Key

### Steps

1. Clone or download the repository:
```bash
cd Simple_RAG_Chatbot_demo
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

5. Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📖 Usage

1. **Upload PDF**: Click the "Upload a PDF" button and select your PDF file
2. **Wait for Processing**: The app will process the PDF and create embeddings
3. **Ask Questions**: Type your question in the text input field
4. **Get Answers**: View the AI-generated answer and source chunks
5. **Explore Sources**: Expand the "Source Chunks" section to see which parts of the document were used

## 🔧 Configuration

### Adjustable Parameters

- **Chunk Size**: Modify `chunk_size=1000` in the text splitter
- **Chunk Overlap**: Modify `chunk_overlap=200` for context continuity
- **Number of Retrieved Chunks**: Change `search_kwargs={"k": 3}` to retrieve more/fewer chunks
- **Temperature**: Adjust LLM temperature (currently 0 for deterministic answers)
- **Embedding Model**: Change from `sentence-transformers/all-MiniLM-L6-v2` to another model

## 🎯 Use Cases

- **Research**: Extract insights from academic papers
- **Business Reports**: Analyze financial or strategic documents
- **Documentation**: Query technical documentation quickly
- **Legal Documents**: Review contracts and agreements
- **Knowledge Articles**: Search through company knowledge bases

## ⚠️ Limitations

- Works best with text-heavy PDFs (images/scans may not be processed)
- Requires valid OpenAI API key and internet connection
- Answer quality depends on document clarity and question relevance

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

## 📄 License

This project is open source and available under the MIT License.

## 💡 Future Enhancements

- Support for multiple document formats (DOCX, TXT, HTML)
- Multi-file document processing
- Conversation history and context memory
- Custom prompt templates
- Different LLM model options
- Cost estimation and tracking

## 📧 Support

If you encounter any issues or have questions, please open an issue in the repository.

---

**Built with ❤️ as part of the 60 Days AI Challenge**
