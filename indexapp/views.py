from django.shortcuts import render

nav_buttons = {
  "top" : "Home",
  "services" : "Services",
  "courses" : "Courses",
  "team" : "Team",
  "events" : "Events",
  "contact" : "Register Now",
}

services = [
  {
    "servicename" : "Online Degrees",
    "content" : "Whenever you need free templates in HTML CSS, you just remember TemplateMo website."
  },
  {
    "servicename" : "Short Courses",
    "content" : "You can browse free templates based on different tags such as digital marketing, etc."
  },
  {
    "servicename" : "Web Experts",
    "content" : "You can start learning HTML CSS by modifying free templates from our website too."
  },
]

def index(request):
  data = {
    "nav_items" : nav_buttons,
    "service" : services
  }

  
  return render(request, "indexapp/index.html", data)
