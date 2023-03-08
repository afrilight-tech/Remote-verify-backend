from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from backend_api import settings

@csrf_exempt
def sendmail(request):
    if request.method == 'POST':
        name = request.POST['name'] or '--*--'
        phone = request.POST['phone'] or '--*--'
        email = request.POST['email'] or '--*--'
        message = request.POST['message'] or '--*--'
        country = request.POST['country'] or '--*--'
        job = request.POST['job'] or '--*--'
        company = request.POST['company'] or '--*--'
        reason = request.POST['reason'] or '--*--'
        service = request.POST['service'] or '--*--'
        # recipient_list = [request.POST.get('to_email')]
        if name and email and phone and message:
          admin_deliver = "Hello, Sales team \n" + ' ' +  '\n' + name + ' just reached out to us through our contact form, check the response below: \n' + ' ' + '\n' + 'Name: \n' + name + '\n' + ' ' + '\n' + 'Email: \n' + email + '\n' + ' ' + '\n' + 'Phone: \n' + phone +  '\n' + ' ' + '\n' + 'Job: \n' + job + '\n' + ' ' + '\n' + 'Country: \n' +  country + '\n' + ' ' + '\n' + 'Company: \n' + company + '\n' + ' ' + '\n' + 'Service: \n' + service + '\n' + ' ' + '\n' + 'Reason: \n' + reason + '\n' + ' ' + '\n' + 'Message: \n' + message
          admin_subject = "New Contact Form Entry From " + name
          user_deliver = "Hey there " + name + "," + '\n' + '\n' + "Thanks for reaching out to us - we're always excited to hear from people who love our products and services as much as we do!" + '\n' + '\n' + "We promise to get back to you within 24 hours (or less!) with more information on how we can help. In the meantime, feel free to keep sending us your burning questions - we're here to help you out however we can." + '\n' + '\n' + "Thanks for choosing AfriLight Technologies Ltd - we can't wait to show you what we have got in store." + '\n' + '\n' + "Best regards, \nGbenga Daniels." 
          user_subject = name + ", Your Details Have Been Submitted"
          site_title = "RemoteVerify"
          send_mail(
            admin_subject,
            admin_deliver,
            settings.DEFAULT_FROM_EMAIL,
            ['sales@remotverify.com'],
            fail_silently= False
        )

          send_mail(
            user_subject,
            user_deliver,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently= False
        )
        return JsonResponse({'message': 'Email sent successfully'})
    else:
      return JsonResponse({'Message': 'You need to make a post request'})    
