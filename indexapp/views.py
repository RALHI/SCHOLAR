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

banner_content = [
  {
    "category" : "Our Courses",
    "heading" : "With Scholar Teachers, Everything Is Easier",
    "description" : "Scholar is free CSS template designed by TemplateMo for online educational related websites. This layout is based on the famous Bootstrap v5.3.0 framework.",
    "text" : "What's Scholar?"
  },  
  {
    "category" : "Best Result",
    "heading" : "Get the best result out of your effort",
    "description" : "You are allowed to use this template for any educational or commercial purpose. You are not allowed to re-distribute the template ZIP file on any other website.",
    "text" : "What's the best result?"
  },  
  {
    "category" : "Online Learning",
    "heading" : "Online Learning helps you save the time",
    "description" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod temporious incididunt ut labore et dolore magna aliqua suspendisse.",
    "text" : "What's Online Course?"
  },  
]

team = [
  {
    "image" : "member-01.jpg",
    "category" : "UX Teacher",
    "name" : "Sophia Rose",
    "facebook_url" : None,
    "twitter_url" : None,
    "linkdin_url" : None
  },
  {
    "image" : "member-02.jpg",
    "category" : "Graphic Teacher",
    "name" : "Cindy Walker",
    "facebook_url" : None,
    "twitter_url" : None,
    "linkdin_url" : None
  },
  {
    "image" : "member-03.jpg",
    "category" : "Full Stack Master",
    "name" : "David Hutson",
    "facebook_url" : None,
    "twitter_url" : None,
    "linkdin_url" : None
  },
  {
    "image" : "member-04.jpg",
    "category" : "Digital Animator",
    "name" : "Stella Blair",
    "facebook_url" : None,
    "twitter_url" : None,
    "linkdin_url" : None
  },
]


course_filter = {
  "*" : "Show All",
  "design" : "Webdesign",
  "development" : "Development",
  "wordpress" : "Wordpress"  
}

def index(request):
  data = {
    "nav_items" : nav_buttons,
    "banner" : banner_content,
    "service" : services,
    "team" : team,
    "coursefilter" : course_filter
  }
  return render(request, "indexapp/index.html", data)
