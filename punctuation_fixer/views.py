from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from punctfix import PunctFixer
from docx import Document
from io import BytesIO

# Initialize the punctfix fixer
fixer = PunctFixer(language="da")

def index(request):
    # This view can be kept for fallback rendering (POST with form submission)
    if request.method == 'POST':
        text = request.POST.get('text', '')
        
        # Apply punctuation fixing
        corrected_text = fixer.punctuate(text)
        
        # Return the form with the corrected text (this can still work for traditional form submission)
        return render(request, 'fixer/index.html', {
            'text': text,
            'corrected_text': corrected_text,
        })

    # Default rendering for the page
    return render(request, 'fixer/index.html')


def process_text(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        
        # Apply punctuation fixing
        corrected_text = fixer.punctuate(text)
        
        return JsonResponse({'corrected_text': corrected_text})

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def download_corrected(request):
    text = request.POST.get('text', '')

    # Create a DOCX document with the corrected text
    doc = Document()
    doc.add_paragraph(text)
    
    # Save to a BytesIO object and return as a download
    doc_io = BytesIO()
    doc.save(doc_io)
    doc_io.seek(0)

    return HttpResponse(doc_io, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document', 
                        headers={'Content-Disposition': 'attachment; filename="corrected_document.docx"'})