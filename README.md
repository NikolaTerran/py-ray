# !IMPORTANT!
# need numpy installed '''pip install numpy'''
# py-ray, a raytracing graphics engine written in python
## Development summary #1:
### Phase I (completed)
### Phase II (completed)
### Phase III (completed)
### Phase IV (moved after phase V)
### Phase V:
#### After this phase the engine should be able to distribute processing power 
#### for compute intensive raytracing algorithm. In the beginning, I intended to work
#### on this after I have completed phase four. However, the debugging process is much more
#### rigorous than I have assumed initially. I have to spend around 5 minites to trace an image
#### with rays set up to bounce only once. So I put this phase prior to the Phase IV.
#### ----
#### This phase has not yet completed due to how complicated python multiprocessing library is,
#### I'm still having troble to write the color value returned by multiple processes to the canvas.
#### I have tried to store the return value in multiprocess.Array and multiprocess.Queue, somehow
#### the value is not written into the file and I'm confused.
#### ----
#### Potential optimization solution, and why I decided not to implement them to speed up the engine:
#### 1. Space Partitioning, organize the objects in tree like structure to reduce the number of
####    ray-intersection tests. I did not implement this because currently the scene contains less than
####    20 triangle meshes, so this method is unlikely to improve the overall speed of the engine, and will
####    take me a whole lot of time to code and debug.
#### 2. Writing the tracer code as c extension of python, since c is way faster than python. Doing this 
####    will complete destroy the premise of building a raytracing engine in python because c is not 
####    object-oriented and it will be a nightmare to pass pointers around.
### Phase IV:
#### Currently, the best this engine can do is to collide the primary ray with a polygon and cast another shadow ray.
#
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
