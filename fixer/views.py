from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from punctfix import PunctFixer
from docx import Document
from io import BytesIO

# Initialize the punctfix fixer
fixer = PunctFixer(language="da")

def index(request):
    if request.method == 'POST':
        if 'document' in request.FILES:
            # Handle file upload and process the document
            uploaded_file = request.FILES['document']
            doc = Document(uploaded_file)
            
            # Correct punctuation in the document
            for para in doc.paragraphs:
                para.text = fixer.punctuate(para.text)

            # Save corrected document to BytesIO
            doc_io = BytesIO()
            doc.save(doc_io)
            doc_io.seek(0)

            # Return corrected document as a downloadable response
            return HttpResponse(doc_io, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                                 headers={'Content-Disposition': 'attachment; filename="corrected_document.docx"'})

        # If the request contains text input, correct the punctuation
        text = request.POST.get('text', '')
        if text:
            corrected_text = fixer.punctuate(text)
            # Return the corrected text as a JSON response for JS to handle
            return JsonResponse({'corrected_text': corrected_text})
        
        return JsonResponse({'error': 'No text provided'}, status=400)

    # Default page render for GET requests
    return render(request, 'fixer/index.html')