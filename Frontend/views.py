from django.shortcuts import render,redirect,get_object_or_404
from Backend.models import songdb,Eventdb,Genredb
from Frontend.models import registerdb,contactdb,checkoutdb
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm,LoginForm
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle,Spacer,Image
from django.utils.safestring import mark_safe
# import os
# from google.cloud import dialogflow_v2beta1 as dialogflow
# from google.api_core.exceptions import InvalidArgument

import razorpay


# Create your views here.

def home(req):
    genre=Genredb.objects.all()
    hiphop=songdb.objects.filter(Genre="Hip hop")
    metal=songdb.objects.filter(Genre="Metal band")
    return render(req,"Home.html",{'genre':genre,'hiphop':hiphop,'metal':metal})

def albums(req,alphabet):
    genre=Genredb.objects.all()

    if alphabet=="all":
        album=songdb.objects.all()
    else:

        album=songdb.objects.filter(Song_name__istartswith=alphabet)
    return render(req,"Albums.html",{'album':album,'genre':genre})

def contact(req):
    genre=Genredb.objects.all()

    return render(req,"Contact.html",{'genre':genre})

def events(req):
    event=Eventdb.objects.all()
    genre=Genredb.objects.all()

    return render(req,"Events.html",{'event':event,'genre':genre})

def news(req):
    genre=Genredb.objects.all()
    return render(req,"News.html",{'genre':genre})

def singlegenre(req,genrename):
    data=Genredb.objects.all()
    genre=songdb.objects.filter(Genre=genrename)
    gen=genrename
    return render(req,"SingleGenre.html",{"genre":genre,"gen":gen,'data':data})

# def login(req):
#     return render(req,"Login.html")


def register(request):
    genre=Genredb.objects.all()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page or another appropriate page after successful registration
    else:
        form = RegisterForm()
    return render(request, "Register.html", {"form": form,'genre':genre})

class LoginView(View):
    def get(self, request, *args, **kwargs):
        genre=Genredb.objects.all()
        form = LoginForm()
        return render(request, 'Login.html', {"form": form,'genre':genre})

    def post(self, request, *args, **kwargs):
        genre=Genredb.objects.all()
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            usr = authenticate(request, username=uname, password=pwd)
            if usr:
                login(request,user=usr)
                messages.success(request, 'login successfully')
                return redirect('home')
        messages.error(request, 'invalid credential')
        return render(request, 'login.html', {"form": form,'genre':genre})
    

@login_required(login_url='login')
def log_out_view(request, *args, **kwargs):
    logout(request)
    messages.success(request, 'logout successfully')
    return redirect('home')

# def save_register(req):
#     if req.method=="POST":
#         fna=req.POST.get("fname")
#         lna=req.POST.get("lname")
#         una=req.POST.get("uname")
#         em=req.POST.get("email")
#         pass1=req.POST.get("pass1")
#         pass2=req.POST.get("pass2")
#         ob=registerdb(First_name=fna,Last_name=lna,Username=una,Email=em,Password=pass1,Password2=pass2)
#         if registerdb.objects.filter(Username=una).exists():
#             messages.warning(req, "User already Exists!")
#             return redirect(register)
#         elif registerdb.objects.filter(Email=em).exists():
#             messages.warning(req, "This Email already Exists!")
#             return redirect(register)
#         else:
#             ob.save()
#             messages.success(req, "Registered Successfully !")

#         return redirect(login)

# def loginbycheck(req):
#     if req.method=="POST":
#         pas=req.POST.get("pass")
#         em=req.POST.get("email")
#         una=req.POST.get("name")
#         if registerdb.objects.filter(Password=pas,Email=em,Username=una).exists():
#             req.session['username']=una
#             req.session['password']=pas
#             req.session['email']=em
#             messages.success(req,"Login Success")
#             return redirect(home)
#         else:
#             messages.warning(req,"Check Password and try again!!")

#             return redirect(login)
#     else:
#         messages.error(req, "User not found!")

#         return redirect(login)

# def user_logout(request):
#     del request.session['username']
#     del request.session['password']

#     messages.success(request, "Successfully Logout")

#     return redirect(home)

def save_message(req):
    if req.method=="POST":
        na=req.POST.get("name")
        em=req.POST.get("email")
        sub=req.POST.get("sub")
        mes=req.POST.get("message")
        ob=contactdb(Name=na,Email=em,Subject=sub,Message=mes)
        ob.save()
        messages.success(req,"Thank you for Your Message 🙏")
        return redirect(contact)

def music_player(req,mid):
    music=songdb.objects.get(id=mid)
    return render(req,"music_player.html",{"music":music})

# def browse_by_alphabet(request, alphabet):
#     items = songdb.objects.filter(Song_name__istartswith=alphabet)
#     items_list = list(items.values('Song_name'))  # Adjust fields as needed
#     return JsonResponse(items_list, safe=False)

# @login_required(login_url='login')
def eventdetails(req,eid):
    user = req.user
    if user.is_authenticated:
        data=Eventdb.objects.get(id=eid)
        return render(req,"EventDetail.html",{"data":data})
    messages.info(req,"Login to see event details!!")
    return redirect('login')

def payment(req):
    customer=checkoutdb.objects.order_by("-id").first()
    pay=customer.TotalPrice
    amount=int(pay*100)
    pay_str=str(amount)
    for i in pay_str:
        print(i)
    if req.method=="POST":
        order_currency="INR"
        client=razorpay.Client(auth=('rzp_test_UMVTetC6neXnFs','BDFnuQBfZAqcmYI1FpL1OC50'))
        payment=client.order.create({'amount':amount,'currency':order_currency,'payment_capture':'1'})
    html = "<a href='#'><button>Click to Download Ticket</button></a>"
    messages.success(req, mark_safe(f"Your Ticket is Booked! {html}"))
    return render(req,"Payment.html",{"customer":customer,"pay_str":pay_str})

def save_check(req):
    if req.method=="POST":
        ena=req.POST.get("ename")
        na=req.POST.get("name")
        em=req.POST.get("email")
        mob=req.POST.get("mobile")
        qty=req.POST.get("qty")
        tot=req.POST.get("total")
        ob=checkoutdb(Eventname=ena,Username=na,Email=em,Mobile=mob,Quantity=qty,TotalPrice=tot)
        ob.save()
        
        client_email = em
        ticket_details = ena

        # Send booking confirmation email
        send_booking_confirmation_email(client_email, ticket_details)
        html = "<a href='#'><button>Click to Download Ticket</button></a>"
        messages.success(req, mark_safe(f"Your Ticket is Booked! {html}"))
        return redirect(payment)

def send_booking_confirmation_email(client_email, ticket_details):
    subject = 'Ticket Booking Confirmation'
    message = f'Thank you for choosing Sound Tribe. You are about to book :\n\n{ticket_details}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [client_email]

    try:
        send_mail(subject, message, email_from, recipient_list)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    except Exception as e:
        # Log the error or handle it as necessary
        return HttpResponse(f'Error sending email: {e}')
    

#for chatbot    

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/MIDHUN PHILIP\Desktop\Luminar Projects\Django\SoundTribe\SoundTribe\credential\m.json"

# def detect_intent_texts(project_id, session_id, texts, language_code):
#     """Returns the result of detect intent with texts as inputs."""
#     session_client = dialogflow.SessionsClient()

#     session = session_client.session_path(project_id, session_id)
#     print("Session path: {}\n".format(session))

#     for text in texts:
#         text_input = dialogflow.types.TextInput(text=text, language_code=language_code)

#         query_input = dialogflow.types.QueryInput(text=text_input)

#         try:
#             response = session_client.detect_intent(
#                 session=session, query_input=query_input
#             )
#         except InvalidArgument:
#             raise

#         return response.query_result.fulfillment_text

# def chat(request):
#     if request.method == "POST":
#         user_message = request.POST.get('message')
#         project_id = "soundtribeproject"  # Replace with your Dialogflow project ID
#         session_id = "123456789"  # You can use a unique session ID per user
#         response_text = detect_intent_texts(project_id, session_id, [user_message], "en")
#         return JsonResponse({"response": response_text})

#     return render(request, "chat.html")

# file_path = "C:/Users/MIDHUN PHILIP\Desktop\Luminar Projects\Django\SoundTribe\SoundTribe\credential\m.json"
# print(os.path.exists(file_path))

def bookhistory(req):
    user=req.user
    if user.is_authenticated:
        genre=Genredb.objects.all()
        una=req.user.first_name
        history=checkoutdb.objects.filter(Username=una)
        return render(req,"history.html",{'genre':genre,'history':history})
    messages.info(req,"login to see Booking details!")
    return redirect('login')

def delete_history(req,hid):
    data=checkoutdb.objects.filter(id=hid)
    data.delete()
    messages.success(req, "Removed")
    return redirect(bookhistory)


def booking_pdf(request, booking_id):
    booking = get_object_or_404(checkoutdb, pk=booking_id)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="booking_{booking_id}.pdf"'

    pdf = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'TicketTitle',
        fontSize=28,
        leading=34,
        alignment=1,  # Center alignment
        textColor=colors.darkblue,
        spaceAfter=20,
    )

    body_style = ParagraphStyle(
        'TicketBody',
        fontSize=14,
        leading=18,
        spaceAfter=12,
        textColor=colors.black,
    )

    header_style = ParagraphStyle(
        'HeaderStyle',
        fontSize=12,
        leading=14,
        textColor=colors.white,
        backColor=colors.darkblue,
        spaceAfter=6,
        leftIndent=10,
    )

    # Ticket border style
    border_table_style = TableStyle([
        ('GRID', (0, 0), (-1, -1), 2, colors.darkblue),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ])

    content = []

    # Add ticket title
    title = Paragraph("Concert Ticket", title_style)
    content.append(title)

    # Optional: Add a logo at the top
    logo_path = r'C:\Users\MIDHUN PHILIP\Desktop\Luminar Projects\Django\SoundTribe\Frontend\static\assets\img\bg-img\a7.jpg'  # Update with your logo's path
    logo = Image(logo_path, 1.5 * inch, 1.5 * inch)
    content.append(logo)
    
    # Booking information table
    booking_info = [
        [Paragraph("<b>User Name:</b>", header_style), Paragraph(str(booking.Username), body_style)],
        [Paragraph("<b>Event Name:</b>", header_style), Paragraph(booking.Eventname, body_style)],
        [Paragraph("<b>Customer Email:</b>", header_style), Paragraph(booking.Email, body_style)],
        [Paragraph("<b>Customer Mobile:</b>", header_style), Paragraph(str(booking.Mobile), body_style)],
        [Paragraph("<b>Quantity:</b>", header_style), Paragraph(str(booking.Quantity), body_style)],
        [Paragraph("<b>Total Price:</b>", header_style), Paragraph(f"${booking.TotalPrice}", body_style)],
    ]

    # Wrap the booking information in a bordered table
    booking_table = Table(booking_info, colWidths=[2.5 * inch, 3.5 * inch])
    booking_table.setStyle(border_table_style)
    
    content.append(booking_table)

    # Decorative line or box to give the ticket a nice border
    content.append(Spacer(1, 0.5 * inch))
    line = Table(
        [[Paragraph(" ", body_style)]],
        colWidths=[5.5 * inch]
    )
    line.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, -1), 2, colors.darkblue),
    ]))
    content.append(line)

    # Add some space before adding a final decorative element
    content.append(Spacer(1, 0.5 * inch))

    # Optional: Add a barcode or QR code at the bottom for authenticity
    # from reportlab.graphics.barcode import qr
    # barcode = qr.QrCodeWidget(f"Booking ID: {booking_id}")
    # barcode_bar = barcode.makeImage()
    # content.append(Image(barcode_bar, width=1.5*inch, height=1.5*inch))

    # Build the PDF
    pdf.build(content)

    return response