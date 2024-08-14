# tau, averageGasUsed
#   20 230679
#   21 233440
#   22 230228
#   23 232067
#   24 231939
#   25 230898
#   Bits:  3072
#   tau, averageGasUsed
#   20 459546
#   21 458456
#   22 457266
#   23 457641
#   24 459446
#   25 460088

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import math
import numpy

x = ['2048', '3072']
value2048 = math.floor(numpy.mean([230679, 233440, 230228, 232067, 231939, 230898]))
value3072 = math.floor(numpy.mean([459546, 458456, 457266, 457641, 459446, 460088]))
y = [value2048, value3072]

fig, ax = plt.subplots()
bar_width = 0.2 # Adjust the bar width
bars = ax.bar(x, y, width=bar_width)

#Center the bars
ax.set_xticks(x)
ax.set_xticklabels(x)
ax.margins(x=0.7)


plt.xlabel('bit size', fontsize=16)
plt.ylabel('Gas Used ($10^5$)', labelpad= 7, fontsize=15.5)
plt.gca().yaxis.get_offset_text().set_visible(False)
def custom_formatter(x, pos):
    return '{:.0f}'.format(x * 1e-5)
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.grid(True, linestyle="--")
plt.tight_layout()


plt.savefig('wesolowskigas.png', dpi=500)
plt.show()