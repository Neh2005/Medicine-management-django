from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import MedicalProduct
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_list')
    else:
        form =ProductForm()
    return render(request, 'create.html', {'form': form})

def product_read(request):
    product_list=MedicalProduct.objects.all()
    return render(request,'retrieve.html',{'product_list':product_list})

def product_update(request, id):
    product = MedicalProduct.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('retrieveproduct')
    else:
        form =ProductForm(instance=product)           
    return render(request, 'update.html', {'form': form})

def product_delete(request,pk):
    product=MedicalProduct.objects.get(pk=pk)  
    if request.method == 'POST':
        product.delete()
        return redirect('retrieveproduct')
    
    return render(request,'delete.html',{'product':product})

def listing(request):
    product_list = MedicalProduct.objects.all()
    paginator = Paginator(product_list, 3)  # Set the number of items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj})


def generate_pdf(request,pk):
    # Get the product object
    product = get_object_or_404(MedicalProduct,pk=pk)

    # Render the HTML template with the product data
    template = get_template('product_pdf.html')
    html = template.render({'product': product})

    # Create a file-like buffer to receive PDF data.
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    pisa_status = pisa.CreatePDF(html, dest=buffer)

    # Return PDF document through a Django HTTP response.
    if pisa_status.err:
        return HttpResponse('PDF creation error!')
    else:
        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(product.name)
        return response
    
def send_product_email(request,pk):
   product=MedicalProduct.objects.get(pk=pk)
   subject = f"New Product: {product.name}"
   from_email = "user1@gmail.com"
   recipient_list = ["your_mailtrap_inbox@mailtrap.io"]
   html_message = render_to_string('product_email.html', {'product': product})
   plain_message = strip_tags(html_message)
   send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
   return HttpResponse('Email sent successfully')