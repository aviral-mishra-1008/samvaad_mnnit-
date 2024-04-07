from django.shortcuts import render
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Submissions
from .models import Contact
import smtplib
from Vyas.models import Post
import random
import os
from django.contrib import  messages
from transformers import pipeline
import random
from datetime import datetime

# Create your views here.

def index(request):
    num = random.randint(21,26)
    arts = Post.objects.all()
    n = 6
    arts = arts[:n]
    for i in arts:
        i.article = i.article[0:255]+"..."
    params = {'key':num,'no_of_arts':n, 'range':range(1,n), 'arts': arts}
    return render(request, "indexNew.html",params)

def about(request):
    return render(request, "AboutNew.html")

def contact_us(request):
    if request.method=='POST':
        date= request.POST.get('date','')
        email= request.POST.get('email','')
        phone = request.POST.get('phone','')
        query = request.POST.get('query','')
        image = request.FILES.get('image',)
        print(image)
        date = datetime.strptime(date, '%Y-%m-%d').date()
        contact=Contact(date=date,email=email,phone=phone,query=query,image=image)
        contact.save()
        messages.success(request, 'Your message was sent successfully!')
        load_dotenv()
        password = os.getenv("ADMIN_PASS") #Always use double inverted commas
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.starttls
        server.login("glasnost.mnnit@gmail.com", password)
        subject = "[Contact Query Received!]"
        body = "A user has contacted us for the following reason: "+query+" and to reply to this customer the email id is: "+email+" and the provided contact number is: "+phone
        message = "Subject:{}\n\n{}".format(subject,body)
        server.sendmail("glasnost.mnnit@gmail.com","aviral.20225017@mnnit.ac.in",message)
        server.quit()
        return redirect('/')
   
    return render(request, "ContactNew.html")

def sub(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email_id = request.POST.get('email','')
        phone_no = request.POST.get('phone_no',)
        heading = request.POST.get('heading','')
        article = request.POST.get('article','')
        branch = request.POST.get('branch','')
        insta = request.POST.get('ig', '')
        reg_no = request.POST.get('reg',)
        year = request.POST.get('year',)
        estimated_time = request.POST.get('time',)
        image = request.FILES.get('image',)
        unique_id = random.randrange(1000000,99999999)
        load_dotenv()
        password = os.getenv("ADMIN_PASS") #Always use double inverted commas
        submission = Submissions(name=name, email_id=email_id, phone_no=phone_no, heading=heading, article=article, insta=insta, reg_no=reg_no, branch=branch, year=year,estimated_time=estimated_time, image=image, unique_id=unique_id )
        submission.save()
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.starttls
        server.login("glasnost.mnnit@gmail.com", password)
        subject1 = "[Article Submission Successful!]"
        body1 = "Hi " + name + "!" + "\n\n" + "You have successfully submitted the article, please hold on while we review your article and if your article is found to be relevant and within guidelines of the website then it'll get published on the website within 3-4 business days!"
        message1 = "Subject:{}\n\n{}".format(subject1,body1)
        server.sendmail("glasnost.mnnit@gmail.com",email_id,message1)
        subject2 = "[Article Submission Received!]"
        body2 = "A user by name of " + name + " has submitted an article with heading : " + heading + " . The article can be viewed on backend and now you must evaluate the same and if found worthy the article should be published on website." + "\n\n The U_Id for this article is : "+ str(unique_id)
        message2 = "Subject:{}\n\n{}".format(subject2,body2)
        email2 = "aviral.20225017@mnnit.ac.in"
        server.sendmail("glasnost.mnnit@gmail.com",email2,message2)
        server.quit()
        return render(request,"success.html")
    return render(request, "sub.html")


def success(request):
    return render(request, "success.html")




def backend(request):
    if request.method=="POST":
        u_id = request.POST.get('u_id','')
        params = {}
        l = []
        try:
            iD = Submissions.objects.get(unique_id=u_id)
            name = iD.name
            email = iD.email_id
            article = iD.article
            art = article[0:255]+"......."
            branch = iD.branch
            heading = iD.heading
            time = iD.estimated_time
            year = iD.year
            image = iD.image
            image = "\media\\"+str(image)
            try:
                sentiment_pipeline = pipeline("sentiment-analysis")
                result = sentiment_pipeline(article)
                predicted_sentiment = result[0]['label']
                score = round(result[0]['score'],5)
            except:
                predicted_sentiment = "Couldn't retrieve info!"
                score = '-'
                

            l.extend([name,email,article,branch,heading,time,year,u_id,image,predicted_sentiment,score])
            for i in range(11):
                t = str(i)
                query = "query"+t
                params[query]=l[i]
                
            return render(request, "article.html",params)
        except:
            return render(request, 'erono1.html')
    else:
        return HttpResponse('Unauthorised Access!')

def article(request):
    u_id = request.POST.get('U_id','')
    user = request.POST.get('Mnnitian','off')
    head = request.POST.get('Headline','off')
    art = request.POST.get('Article','off')
    img = request.POST.get('ImageVer','off')
    slug = "article/"+str(u_id)+"s"+"/"
    if user=='on' and head=='on' and art=='on' and img=='on':
        field = Submissions.objects.get(unique_id=u_id)
        name = field.name
        email = field.email_id
        article = field.article
        head = field.heading
        time = field.estimated_time
        branch = field.branch
        u_id = field.unique_id
        image = field.image
        print("Here is wht image prints: ",image)
        year = field.year
        push_data = Post(name=name, email_id = email, heading=head, estimated_time=time, article=article, image=image, branch=branch, year=year, unique_identifier=u_id,slug=slug)
        push_data.save()
        file = open("Templates\\"+str(u_id)+"s"+".html","w",encoding="utf-8") #USERS NEED TO COPY THE ABSOLUTE PATH OF TEMPLATE FOLDER AND PASTE HERE INCASE OF USE SINCE WE ARE FINDING IT A BIT HARD TO USE RELATIVE PATHS WITH OPEN FUNCTION
        l = ['{% extends "init.html" %}\n',"<br>\n",'{% block title%}\n',"Article - Samvaad\n",'{% endblock %}\n','{% block body%}\n',"<br>\n","<center>\n",'h1  class="text-4xl pb-4">\n',head,"\n",'</h1>\n',"<img src='\media\\"+str(image)+"' width='30%' class='imageD'>\n","</center>\n","<hr color='black'>\n",'<div class="px-10" >',"<br>\n",article,"\n","</div>\n",'<br> <br>\n',"{%endblock%}"]
        file.writelines(l)
        file.close()
        return render(request,'index.html')

    else:
        field = Submissions.objects.get(unique_id=u_id)
        field.delete()
        return render(request, 'index.html')  
    # return render(request, "article.html")

def search(request):
    query=request.POST.get('search_query','')
    if query=="":
        return render(request,"search_empty.html")
        
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(heading__icontains=query)
        allPostsAuthor= Post.objects.filter(name__icontains=query)
        allPostsContent =Post.objects.filter(article__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
        for post in allPosts:
            post.image = '/media/'+str(post.image)
    # if allPosts.count()==0:
    #      return HttpResponse("try some search")
       
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'search.html', params)

def login(request):
     if request.method=='POST':
        
        username=request.POST['Username']
        password=request.POST['psw']
        users=['shresth','ayushman','aviral']
        if username in users:
            username = username.upper()
            passw = os.getenv(username)
            if passw==password:
                return render (request,'backend.html')
            else :
                return render (request,'erono1.html')

        else:
            HttpResponse("user not found")
     return render(request, 'adminlogin.html')





