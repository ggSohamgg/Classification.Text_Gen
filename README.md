# 📘 Science Text Analyzer

The **Science Text Analyzer** is a dual-purpose deep learning application that:

-  **Classifies academic text** into **Science**, **Mathematics**, or **History**
-  **Generates Scientific content**, especially in **Physics**, **Chemistry**, and **Biology**

Built with **LSTM models** and trained on carefully curated academic datasets, this tool supports **educational research**, **curriculum support**, and **content creation**.

---
## 🚀 How to Use

Simply visit the [Hugging Face Space](https://huggingface.co/spaces/nnsohamnn/Classification.Text_Gen) to use the application directly in your browser. No installation required!

### For Text Classification:
1. Navigate to the "Classify Text" tab
2. Enter or paste your academic text in the input box
3. Click "Classify" to see the predicted subject and confidence score

### For Text Generation:
1. Navigate to the "Generate Text" tab
2. Enter a scientific prompt in the input box
3. Adjust the length (maximum 60 words) and temperature sliders as desired
4. Click "Generate" to create scientific text based on your prompt
- **Note**: Longer generations may take more time to process

---

## Features

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
- Uses a **custom hybrid LSTM-GRU language model** trained on curated educational corpora, with **mixed-precision FP16** training.
- Configurable:
  - **Prompt**
  - **Temperature** (creativity)
  - **Max Length**
- For detailed analysis, [Download Technical_Documentation.pdf](extra/Technical_Documentation.pdf)

---

##  Datasets

### 🔸 Used for Classification

The **classification model** was trained on:

- [`burgerbee/history_wiki`](https://huggingface.co/datasets/burgerbee/history_wiki) – Historical Wikipedia content  
- [`math-ai/AutoMathText`](https://huggingface.co/datasets/math-ai/AutoMathText) – Mathematical explanations  
- [`allenai/sciq`](https://huggingface.co/datasets/allenai/sciq) – Science questions and explanations  
-  **CBSE academic text**, combined with the above and saved as: `classification_text.csv`

### 🔸 Used for Text Generation

The **text generator** was trained on:

- [`camel-ai/biology`](https://huggingface.co/datasets/camel-ai/biology) – Biology-focused academic dialogues and content  
- [`camel-ai/chemistry`](https://huggingface.co/datasets/camel-ai/chemistry) – Chemistry domain instruction-response pairs  
- [`camel-ai/physics`](https://huggingface.co/datasets/camel-ai/physics) – Physics focused dataset

---

## 📊 Training Graphs

### Classification Model (LSTM)

![Classification Training Graph](plot/classification_training_graph.png)

### Generation Model (LSTM-GRU)

![Generation Training Graph](plot/generation_training_graph.png)

---
## 📈 Evaluation Metrics

### 🔹 Classification Results

| Class     | Precision | Recall | F1-Score | Support |
| :-------- | :-------- | :----- | :------- | :------ |
| Science   | 0.84      | 0.90   | 0.87     | 989     |
| Math      | 0.94      | 0.93   | 0.94     | 1013    |
| History   | 0.92      | 0.86   | 0.89     | 1009    |
|           |           |        |          |         |
| **Accuracy** |        |        | **0.90** | **3011**|
| Macro Avg | 0.90      | 0.90   | 0.90     | 3011    |
| Weighted Avg| 0.90      | 0.90   | 0.90     | 3011    |

**Overall Test Accuracy: 90.00%**

---

### 🔹 Text Generation Results

| Metric                | Value     |
|-----------------------|-----------|
| Training Accuracy     | 41.43%    |
| Training Loss         | 3.0162    |
| Training Perplexity   | 20.41     |
| Validation Accuracy   | 33.84%    |
| Validation Loss       | 4.4889    |
| Validation Perplexity | 89.02     |
| Learning Rate         | 5e-4      |

---



## Tech Stack

- **Python**
- **Gradio** – UI with tabs for classification & generation
- **Tensorflow** – LSTM-based models
- **Hugging Face Datasets**
- **Pickle** – For tokenizer serialization
