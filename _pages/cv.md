---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

A summary of my academic record. More detail is on the [Publications](/publications/), [Talks](/talks/), [Teaching](/teaching/) and [Awards](/portfolio/) pages.

Education
======
* PhD in Engineering Mathematics, University of Bristol, 2025
* MSc in Mathematics, Universidad Técnica Federico Santa María, 2019
* BSc in Engineering Mathematics, Universidad Técnica Federico Santa María, 2019

Work experience
======
* 2026 -- Present: Postdoctoral Researcher
  * Technical University of Munich
  * Duties include: Planning my research timetable to complete the projects in my proposal and supervising PhD and MSc students.

* 2025 -- 2026: Teaching Associate
  * University of Bristol
  * Duties included: Delivering courses, marking, tutoring and supervising MSc students, and tracking information for courses that required it.

* 2021 -- 2024: Teaching Assistant
  * University of Bristol
  * Duties included: Providing support to students for different units and marking.

* 2018 -- 2020: Engineering Teacher
  * Universidad Técnica Federico Santa María and Universidad Adolfo Ibáñez
  * Duties included: Preparing exams and teaching different mathematical courses to ~40 students per class.

* 2014 -- 2017: Teaching Assistant
  * Universidad Técnica Federico Santa María
  * Duties included: Preparing material for each assistantship session and marking.

Awards
======
  <ul>{% for post in site.portfolio reversed %}
    <li>{{ post.date | date: "%Y" }}: <b>{{ post.title }}</b>. {{ post.excerpt | markdownify | remove: "<p>" | remove: "</p>" | strip_newlines }}</li>
  {% endfor %}</ul>

Skills
======
* Coding/Use of computational tools
  * Python
  * Mathematica
  * Matlab

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Service and leadership
======
* Refereed for different journals including Proceedings of the Royal Society A, Nonlinearity, and the Journal of Nonlinear Science
* Seminar organisation for the Engineering Mathematics Research Group at the University of Bristol
