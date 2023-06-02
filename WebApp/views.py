from django.shortcuts import render
from django.http import HttpResponse
from .models import GetUserFile, tickets_notifications
from .forms import TicketUpload
# Create your views here.

def home(response):
    return render(response, "WebApp/home.html")

def aboutUs(response):
    return render(response, "WebApp/aboutUs.html")

def forgotPassword(response):
    return render(response, "WebApp/forgotPassword.html")

def home2(response):
    return render(response, "WebApp/home2.html")

def home3(response):
    return render(response, "WebApp/home3.html")

def notifications(response):
    messages = tickets_notifications.objects.all()
    context = {'messages': messages}
    return render(response, "WebApp/notifications.html", context)

def notifications2(response):
    return render(response, "WebApp/notifications2.html")

def database(response):
    myFile = GetUserFile.objects.all()

    folderDisplay = "Main"
    #The files are grouped into folders. This is the folder what should be displayed

    #This is when the user clicks on the file/folders
    if response.method == "POST":
        for item in myFile:
            if response.POST.get("save_"+str(item.id)):
                fileName = response.POST.get("myInfo_"+str(item.id))
                #When a button is pressed I get the name of the file/folder
                folderDisplay = fileName
                # Than it'll open the file/folder the user wants on the screen
                print(folderDisplay)

    #When the user searches for the file/folder
    if response.method == "POST":
        if response.POST.get("fileSearchBar"):
            searched = response.POST.get("fileSearchBar")
            #searchedFile = GetImage.objects.filter(File_Name__contains=searched)
            folderDisplay = searched
            print(searched)

    context = {'myFile': myFile,'folderDisplay': folderDisplay}
    return render(response, "WebApp/database.html", context)

def tickets(response):
    return render(response, "WebApp/tickets.html")

def tickets2(response):
    uploadTicket = TicketUpload(response.POST)
    print(response.POST)
    '''if response.method == "POST":
        form = tickets_notifications(response.POST or None)
        if form.is_valid():
            form.save()
            return render(response, "WebApp/tickets2.html", context)'''

    context = {'uploadTicket': uploadTicket}
    return render(response, "WebApp/tickets2.html", context)

def tickets3(response):
    return render(response, "WebApp/tickets3.html")