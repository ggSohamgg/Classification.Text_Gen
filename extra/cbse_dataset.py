!pip install PyPDF2
!pip install pdfminer.six
!pip install pdf2image
!pip install pytesseract
!apt-get install -y tesseract-ocr

import os
import re
import PyPDF2
from pdfminer.high_level import extract_text as pdfminer_extract
import pytesseract
from pdf2image import convert_from_path
import numpy as np
from google.colab import files

# ===== CHANGE THIS TO YOUR PDF FILENAME =====
pdf_file_path = "history_merged - converted.pdf"  # <-- EDIT THIS LINE ONLY
# ============================================

def extract_with_pdfminer(pdf_path):
    """Extract text using PDFMiner (better for text-based PDFs)"""
    try:
        text = pdfminer_extract(pdf_path)
        return text
    except Exception as e:
        print(f"PDFMiner extraction failed: {e}")
        return ""

def extract_with_pypdf2(pdf_path):
    """Extract text using PyPDF2 (alternative method)"""
    try:
        text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n\n"
        return text
    except Exception as e:
        print(f"PyPDF2 extraction failed: {e}")
        return ""

def extract_with_ocr(pdf_path):
    """Extract text using OCR (for scanned PDFs or images)"""
    try:
        text = ""
        # Convert PDF to images
        images = convert_from_path(pdf_path)

        # Process each page
        for i, image in enumerate(images):
            # Save image temporarily
            image_path = f"temp_page_{i}.jpg"
            image.save(image_path, "JPEG")

            # Extract text with OCR
            page_text = pytesseract.image_to_string(image_path)
            text += page_text + "\n\n"

            # Remove temporary file
            os.remove(image_path)

        return text
    except Exception as e:
        print(f"OCR extraction failed: {e}")
        return ""

def clean_text(text):
    """Clean up the extracted text"""
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)

    # Fix common OCR errors for math symbols
    replacements = {
        '≈': '~',
        '÷': '/',
        '×': '*',
        '−': '-',
        '…': '...',
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Remove strange markers like 'v' at beginning/end of paragraphs
    text = re.sub(r'\bv+\s', '', text)
    text = re.sub(r'\s+v+\b', '', text)

    return text

# Main extraction process
print(f"Extracting text from {pdf_file_path}...")

# Try different extraction methods
pdfminer_text = extract_with_pdfminer(pdf_file_path)
pypdf2_text = extract_with_pypdf2(pdf_file_path)

# Determine which extraction method gave better results
# (Simple heuristic: longer text is usually better)
if len(pdfminer_text) > len(pypdf2_text) * 1.2:
    extracted_text = pdfminer_text
    print("Used PDFMiner for extraction (better results)")
elif len(pypdf2_text) > len(pdfminer_text) * 1.2:
    extracted_text = pypdf2_text
    print("Used PyPDF2 for extraction (better results)")
else:
    # If results are similar, combine them
    extracted_text = pdfminer_text if len(pdfminer_text) > len(pypdf2_text) else pypdf2_text
    print("Used best single extractor result")

# If text extraction failed or produced very little text, try OCR
if len(extracted_text.strip()) < 100:
    print("Text extraction produced little content. Trying OCR...")
    extracted_text = extract_with_ocr(pdf_file_path)

# Clean the text
cleaned_text = clean_text(extracted_text)

# Save the results
output_file = "extracted_history.txt"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(cleaned_text)

print(f"Text extraction complete! Saved to {output_file}")

# Display a sample of the extracted text
print("\nSample of extracted text:")
print(cleaned_text[:500] + "...\n")

# Download the extracted text file
files.download(output_file)

def clean_and_format_math_text(input_file, output_file):
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Clean the text with multiple regex patterns

    # Remove matrix notations with indices
    text = re.sub(r'Let\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*A\s*=\s*a\s*a\s*a\s*a\s*a\s*a\s*a\s*a\s*a', '', text)

    # Remove "Then" followed by matrix indices
    text = re.sub(r'Then\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*A\s*A\s*A\s*A\s*=\s*Transposeof\s*A\s*A\s*A\s*A\s*A\s*Aadj', '', text)

    # Remove matrix equations
    text = re.sub(r'\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*A\s*A\s*A\s*=\s*A\s*A\s*A\s*A\s*A\s*A', '', text)

    # Remove page numbers and headers like "88 MATHEMATICS"
    text = re.sub(r'\d+\s+MATHEMA\s*TICS', '', text)

    # Remove "Reprint 2025-26" footer
    text = re.sub(r'Reprint\s+2025-26', '', text)

    # Remove any remaining matrix indices (patterns of two digits together)
    text = re.sub(r'(?<!\d)\d{2}(?!\d)', '', text)

    # Remove any remaining matrix notation patterns
    text = re.sub(r'A\s*=\s*Transposeof\s*A', '', text)
    text = re.sub(r'adj\s*A', '', text)

    # Clean up excessive whitespace (but keep line breaks)
    text = re.sub(r' +', ' ', text)

    # Remove any Unicode box drawing or special characters
    text = re.sub(r'[\u2500-\u257f]+', '', text)
    text = re.sub(r'[\uf800-\uf8ff]+', '', text)

    # Now separate text into lines for classification

    # Split at periods followed by space or newline (end of sentences)
    sentences = re.split(r'\.(?=\s)', text)

    # Split at section headers (e.g., A.1.1 Introduction)
    lines = []
    for sentence in sentences:
        # Split at section headers
        section_parts = re.split(r'([A-Z]\.\d+\.\d+\s+[A-Za-z]+)', sentence)
        for part in section_parts:
            if part.strip():
                lines.append(part.strip())

    # Split at Example headers
    temp_lines = []
    for line in lines:
        example_parts = re.split(r'(Example\s+\d+)', line)
        for part in example_parts:
            if part.strip():
                temp_lines.append(part.strip())
    lines = temp_lines

    # Split at Solution headers
    temp_lines = []
    for line in lines:
        solution_parts = re.split(r'(Solution)', line)
        for part in solution_parts:
            if part.strip():
                temp_lines.append(part.strip())
    lines = temp_lines

    # Final cleanup of each line
    cleaned_lines = []
    for line in lines:
        # Remove leading/trailing whitespace
        line = line.strip()
        # Skip empty lines
        if line:
            cleaned_lines.append(line)

    # Write the cleaned and separated text to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for line in cleaned_lines:
            file.write(line + '\n')

    print(f"Text cleaned, separated into lines, and saved to {output_file}")
    return cleaned_lines

# Example usage
input_file = "extracted_science.txt"
output_file = "cleaned_formatted_science_text.txt"

cleaned_lines = clean_and_format_math_text(input_file, output_file)
print(f"Total lines after processing: {len(cleaned_lines)}")
print("Sample of first few lines:")
for line in cleaned_lines[:5]:
    print(line)
