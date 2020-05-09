import pygame as g
import random
g.init()
gd=g.display
gt=g.time
m=255
t=9
w=gd.set_mode((m,m))
p=[150,m-t,(0,m,0)]
ce=(m,0,0)
en=[]
gt.set_timer(25,99)
r=1
q=0
while r:
	gt.Clock().tick(60)
	for e in g.event.get():
		if e.type==g.QUIT:r=0
		if e.type==25:en+=[[random.randint(0,m),0,ce]]
	ks=g.key.get_pressed()
	if ks[g.K_a]:p[0]-=3
	if ks[g.K_d]:p[0]+=3
	for e in list(en):
		e[1]+=7
		if e[1]>m-t:
			en.remove(e)
			q+=1
			if abs(e[0]-p[0])<t:r=0
	w.fill((0,0,0))
	for z in en+[p]:g.draw.rect(w,z[2],(z[0],z[1],t,t))
	gd.update()
g.quit()
print(q)
