# Initialize the punctfix fixer
fixer = PunctFixer(language="da")

# Correct file path to the input document
doc = Document("/Users/johanneskarasik/Desktop/commas/input_document.docx")  # Adjust path if needed

# Iterate over each paragraph in the document
for para in doc.paragraphs:
    # Apply punctuation correction to the paragraph text
    corrected_text = fixer.punctuate(para.text)
    # Replace the paragraph's text with the corrected text
    para.text = corrected_text

# Save the updated document to a new file
doc.save("/Users/johanneskarasik/Desktop/commas/output_document.docx")  # Adjust path as needed