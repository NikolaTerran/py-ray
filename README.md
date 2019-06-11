# !IMPORTANT!
# need numpy installed '''pip install numpy'''
# py-ray, a raytracing capable graphics engine written in python
## Premise:
### I realize how horrible my c code is due to the need of frequent use of
### malloc, realloc, free. so I decided to port the c code to python and add
### raytracing capabilities to it. 
### I best I can do with the c code is ambient + diffused reflection, due to
### my lack of knowledge of how to manipulate the rgb value of the light, I
### was not able to accomplish specular reflection in the previouse iteration
### of morgen(the name of previous graphics engine)
## Phase I: porting
### due: probably over the weekend
### note: Because the new engine I envisioned has only raytracing
### capabilities, therefore I will not port most part of my previous engine,
### also the new engine will be programmed in object oriented manner, so it
### will be easier for me to handle the code.
## Phase II: linear perspective
### due: mid next week
### note: to simulate the effect that nearer objects will appear larger than
### those objects that are further away. This is an important first step for
### raytracing
## Phase III: Collision detection
### due: end of next week
### note: co
## Phase IV: Implementation of recursive ray algorithm
### due: ??
### note: when a ray detect a surface it will split into 3 instances of
### its class. Not really sure how to do that yet.
## Phase V: parallel processing
### due: together with Phase IV
### note: without parallel processing the raytracing program will 
### probably take weeks to finish execution. I'm counting on the
### xeon phi processor on homer to do it because I only have nvidia card.
