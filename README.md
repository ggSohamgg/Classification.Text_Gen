# 📘 Science Text Analyzer

🔗 **Live Demo**: [Hugging Face Space](https://huggingface.co/spaces/nnsohamnn/Classification.Text_Gen)

The **Science Text Analyzer** is a dual-purpose deep learning application that:

- 🔍 **Classifies academic text** into **Science**, **Mathematics**, or **History**
- 🧠 **Generates educational content**, especially in **Physics**, **Chemistry**, and **Biology**

Built with **LSTM models** and trained on carefully curated academic datasets, this tool supports **educational research**, **curriculum support**, and **content creation**.

---

## 🚀 Features

### 🔹 Text Classification

- Classifies user input into one of:
  - **Science**
  - **Mathematics**
  - **History**
- Uses a custom **LSTM-based classifier** trained on domain-specific corpora
- Leverages **sequential context** and **linguistic structure** for high accuracy

### 🔹 Academic Text Generation

- Generates scientific-style paragraphs based on user prompts
- Focus areas: **Physics**, **Chemistry**, and **Biology**
- Configurable:
  - **Prompt**
  - **Temperature** (creativity)
  - **Max Length**

---

## 📚 Datasets

### 🔸 Used for Classification

The **classification model** was trained on:

- [`burgerbee/history_wiki`](https://huggingface.co/datasets/burgerbee/history_wiki) – Historical Wikipedia content  
- [`math-ai/AutoMathText`](https://huggingface.co/datasets/math-ai/AutoMathText) – Mathematical explanations  
- [`allenai/sciq`](https://huggingface.co/datasets/allenai/sciq) – Science questions and explanations  
- 📝 **CBSE academic text**, combined with the above and saved as: `classification_text.csv`

### 🔸 Used for Text Generation

The **text generator** was trained on:

- [`camel-ai/biology`](https://huggingface.co/datasets/camel-ai/biology) – Biology-focused academic dialogues and content  
- [`camel-ai/chemistry`](https://huggingface.co/datasets/camel-ai/chemistry) – Chemistry domain instruction-response pairs  
- [`camel-ai/math`](https://huggingface.co/datasets/camel-ai/chemistry) – Mathematics focused dataset

---

## 🧱 Tech Stack

- **Python**
- **Gradio** – UI with tabs for classification & generation
- **Tensorflow** – LSTM-based models
- **Hugging Face Datasets**
- **Pickle** – For tokenizer serialization
