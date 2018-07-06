%matplotlib nbagg

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0.0, 2.0, 100)

f = np.sin(np.pi*t)

fig = plt.figure()

ax = fig.add_subplot(111)

ax.plot(t, f, "orange", linewidth=2.0)

ax.set(xlim=[0.0, 2.0], ylim=[-1.0, 1.0],
       title=r"Senoide: $f(t)=sin(\pi*t)$",
       xlabel=r"$t$", ylabel=r"$f(t)$")

ax.grid(b=True, color='gray', linestyle='--', linewidth=0.5);