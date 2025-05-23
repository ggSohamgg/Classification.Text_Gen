!pip install datasets

from datasets import load_dataset
from datasets import concatenate_datasets



math_text_dataset = load_dataset("text", data_files="extracted_maths.txt")
science_text_dataset = load_dataset("text", data_files="extracted_science.txt")
history_text_dataset = load_dataset("text", data_files="extracted_history.txt")

# Load existing Hugging Face datasets
science_studies = load_dataset("burgerbee/science_studies_textbook")
history_wiki = load_dataset("burgerbee/history_wiki")
auto_math = load_dataset("math-ai/AutoMathText", "code-jupyter-notebook-0.80-to-1.00")

# Combine datasets
combined_science = concatenate_datasets([science_studies["train"], science_text_dataset["train"]])
combined_history = concatenate_datasets([history_wiki["train"], history_text_dataset["train"]])
combined_math = concatenate_datasets([auto_math["train"], math_text_dataset["train"]])

# Save combined datasets to disk
combined_science.save_to_disk("combined_science_dataset")
combined_history.save_to_disk("combined_history_dataset")
combined_math.save_to_disk("combined_math_dataset")

# Print sample from combined datasets
print("Sample from combined science dataset:", combined_science)
print("Sample from combined history dataset:", combined_history)
print("Sample from combined math dataset:", combined_math)

# Keep only the 'text' column and rename it to 'train'
combined_science = combined_science.remove_columns([col for col in combined_science.column_names if col != 'text'])
combined_science = combined_science.rename_column('text', 'train')

combined_history = combined_history.remove_columns([col for col in combined_history.column_names if col != 'text'])
combined_history = combined_history.rename_column('text', 'train')

combined_math = combined_math.remove_columns([col for col in combined_math.column_names if col != 'text'])
combined_math = combined_math.rename_column('text', 'train')

# Print sample from combined datasets
print("Sample from combined science dataset:", combined_science)
print("Sample from combined history dataset:", combined_history)
print("Sample from combined math dataset:", combined_math)

# Simulate downsampling the science dataset from 13397 to 5000 samples
import random

# Set a random seed for reproducibility
random.seed(42)

# Randomly select 5000 indices from the science dataset
science_indices = random.sample(range(len(combined_science)), 5000)
combined_science_downsampled = combined_science.select(science_indices)

# Randomly select 5000 indices from the math dataset
math_indices = random.sample(range(len(combined_math)), 5000)
combined_math_downsampled = combined_math.select(math_indices)

# The history dataset can remain as is since it's already close to 5000 samples

print(f"Science: {len(combined_science_downsampled)} samples")
print(f"Math: {len(combined_math_downsampled)} samples")
print(f"History: {len(combined_history)} samples")

import pandas as pd

# Convert your datasets to pandas DataFrames
# If you have actual dataset objects, convert them first
science_df = pd.DataFrame(combined_science_downsampled)
math_df = pd.DataFrame(combined_math_downsampled)
history_df = pd.DataFrame(combined_history)

# Export to CSV
science_df.to_csv('science.csv', index=False)
math_df.to_csv('math.csv', index=False)
history_df.to_csv('history.csv', index=False)
