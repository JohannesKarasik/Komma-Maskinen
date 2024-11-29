from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from punctfix import PunctFixer
from docx import Document
from io import BytesIO
import enchant
import re
from . import views  # Ensure views are correctly imported


# Initialize the punctfix fixer and Danish dictionary
fixer = PunctFixer(language="da")
danish_dict = enchant.Dict("da_DK")

def index(request):
    if request.method == 'POST':
        if 'document' in request.FILES:
            uploaded_file = request.FILES['document']
            doc = Document(uploaded_file)

            for para in doc.paragraphs:
                para.text = fixer.punctuate(para.text)

            doc_io = BytesIO()
            doc.save(doc_io)
            doc_io.seek(0)

            return HttpResponse(doc_io, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                                headers={'Content-Disposition': 'attachment; filename="corrected_document.docx"'})

        text = request.POST.get('text', '')
        if text:
            corrected_text = fixer.punctuate(text)

            words = corrected_text.split()
            invalid_words = []
            start_index = 0

            for word in words:
                word_cleaned = word.strip(".,!?;:()[]\"'")  # Clean punctuation for spell checking

                # Skip words that start with a capital letter (e.g., Names or Places)
                if word_cleaned[0].isupper():
                    start_index += len(word) + 1  # Move to next word
                    continue

                # Skip words that are numbers or contain numbers
                if re.match(r'^[\d]+$', word_cleaned) or re.search(r'\d', word_cleaned):
                    start_index += len(word) + 1  # Move to next word
                    continue

                # Check word validity
                if not danish_dict.check(word_cleaned):
                    end_index = start_index + len(word)
                    invalid_words.append({'word': word, 'start': start_index, 'end': end_index})
                
                start_index += len(word) + 1  # Add 1 for the space

            return JsonResponse({
                'corrected_text': corrected_text,
                'invalid_words': invalid_words
            })

        return JsonResponse({'error': 'No text provided'}, status=400)

    return render(request, 'fixer/index.html')

# View for the first new page
def stavekontrol(request):
    return render(request, 'stavekontrol.html')

# View for the second new page
def page_two(request):
    return render(request, 'stavekontrol.html')  # Render the correct template
