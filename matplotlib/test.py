import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()
fig.text(0.5, 0.5, matplotlib.__path__, ha='center')
fig.show() 
#fig.canvas.start_event_loop(10)
