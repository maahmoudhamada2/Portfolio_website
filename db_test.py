#!/usr/bin/python3

from models import storage
from models.projects import Project
from models.blogs import Blog

bl = Blog()
bl.blog_title = "What is frontend"
bl.author = "Mahmoud"
bl.intro = "Intro to frontend is...."
bl.article = "Front end is lorem....."
bl.conclusion = "The conclusion is....."

bl.save()

p1 = Project()
p1.title = "Simple shell"
p1.description = "Description 1"
p1.technologies_used = "HTML"

p1.save()
