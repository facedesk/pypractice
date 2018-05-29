import pylab
from random import shuffle

def bubblesort_anim(a):
 x = range(len(a))
 imgidx = 0
 # bubble sort algorithm
 swapped = True
 while swapped: # until there's no swapping
  swapped = False
  for i in range(len(a)-1):
   if a[i] > a[i+1]:
    a[i+1], a[i] = a[i], a[i+1] # swap
    swapped = True
  pylab.plot(x,a,'k.',markersize=6)
  pylab.savefig("bubblesort/img" + '%04d' % imgidx + ".png")
  pylab.clf() # figure clear
  imgidx = imgidx + 1

# running the algorithm
a = range(300)
shuffle(a)
bubblesort_anim(a)
