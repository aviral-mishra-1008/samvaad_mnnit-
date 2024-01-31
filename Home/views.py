from django.shortcuts import render
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import HttpResponse
from .models import Submissions
from .models import Contact
import smtplib
from Vyas.models import Post
import random
import os
from django.contrib import  messages
from transformers import pipeline

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact_us(request):
    if request.method=='POST':
        name= request.POST['name']
        email= request.POST['email']
        phone = request.POST['phone']
        query = request.POST['query']
        
        contact=Contact(name=name,email=email,phone=phone,query=query)
        contact.save()
   
    return render(request, "Contact.html")

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
            sentiment_pipeline = pipeline("sentiment-analysis")
            result = sentiment_pipeline(article)
            predicted_sentiment = result[0]['label']
            score = round(result[0]['score'],5)
                

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
        l = ['{% extends "init.html" %}\n',"<br>\n",'{% block title%}\n',"Article - Samvaad\n",'{% endblock %}\n','{% block body%}\n',"<style>\n","body{\n","background: url('https://images2.alphacoders.com/600/600022.png')\n}",".bg-dark{\n","background: rgb(0,0,0);\n","background: linear-gradient(186deg, rgba(0,0,0,1) 0%, rgba(55,9,17,1) 99%);\n","}\n","div{\n","padding-right: 10%;\n","padding-left:10%;\n}","</style>\n","<div>\n", "<font color='white'>\n","<br>\n","<center>\n","<h2>\n",head,"\n",'</h2>\n',"<img src='\media\\"+str(image)+"' width='100' class='imageD'>\n","</center>\n","<hr color='black'>\n","<br>\n",article,"\n","</div>\n","{%endblock%}"]
        file.writelines(l)
        file.close()
        return render(request,'index.html')

    else:
        field = Submissions.objects.get(unique_identifier=u_id)
        field.delete()
        return render(request, 'index.html')  
    # return render(request, "article.html")

def search(request):
    query=request.GET['query']
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





