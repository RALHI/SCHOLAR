from django.shortcuts import render

nav_buttons = {
  "top" : "Home",
  "services" : "Services",
  "courses" : "Courses",
  "team" : "Team",
  "events" : "Events",
  "contact" : "Register Now",
}

def index(request):
  data = {
    "nav_items" : nav_buttons
  }
  return render(request, "indexapp/index.html", data)
