# Copyright 2024 justin
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter
NTXYVInProof = [
  [ 1948075, 'λ1024', 'T2^20' ],
  [ 2055287, 'λ1024', 'T2^21' ],
  [ 2159308, 'λ1024', 'T2^22' ],
  [ 2266357, 'λ1024', 'T2^23' ],
  [ 2363314, 'λ1024', 'T2^24' ],
  [ 2480958, 'λ1024', 'T2^25' ],
  [ 3921992, 'λ2048', 'T2^20' ],
  [ 4128691, 'λ2048', 'T2^21' ],
  [ 4338719, 'λ2048', 'T2^22' ],
  [ 4555330, 'λ2048', 'T2^23' ],
  [ 4749156, 'λ2048', 'T2^24' ],
  [ 4980923, 'λ2048', 'T2^25' ],
  [ 6882805, 'λ3072', 'T2^20' ],
  [ 7235788, 'λ3072', 'T2^21' ],
  [ 7603641, 'λ3072', 'T2^22' ],
  [ 7964096, 'λ3072', 'T2^23' ],
  [ 8334172, 'λ3072', 'T2^24' ],
  [ 8729305, 'λ3072', 'T2^25' ]
]
SkippingTXY= [
  [ 1733213, 'λ1024', 'T2^20' ],
  [ 1829177, 'λ1024', 'T2^21' ],
  [ 1921829, 'λ1024', 'T2^22' ],
  [ 2017168, 'λ1024', 'T2^23' ],
  [ 2102773, 'λ1024', 'T2^24' ],
  [ 2208887, 'λ1024', 'T2^25' ],
  [ 3581413, 'λ2048', 'T2^20' ],
  [ 3769836, 'λ2048', 'T2^21' ],
  [ 3961610, 'λ2048', 'T2^22' ],
  [ 4159560, 'λ2048', 'T2^23' ],
  [ 4335290, 'λ2048', 'T2^24' ],
  [ 4548137, 'λ2048', 'T2^25' ],
  [ 6411812, 'λ3072', 'T2^20' ],
  [ 6739194, 'λ3072', 'T2^21' ],
  [ 7081530, 'λ3072', 'T2^22' ],
  [ 7415860, 'λ3072', 'T2^23' ],
  [ 7760099, 'λ3072', 'T2^24' ],
  [ 8128899, 'λ3072', 'T2^25' ]
]

BitSize = [1024, 2048, 3072]
colors = ['#ff0000', '#008800', '#0000ff']
markers = ['o', '^', 's']  # circle, triangle, square
ts = ["$2^{20}$", "$2^{21}$", "$2^{22}$", "$2^{23}$", "$2^{24}$", "$2^{25}$"]
lineStyles = ['-', '--']

x = [[],[],[]]
y = [[],[],[]]

for i in range(0,len(NTXYVInProof),6):
    for j in range(0,6):
        x[i//6].append(ts[j])
        y[i//6].append(NTXYVInProof[i+j][0] - SkippingTXY[i+j][0])

for i in range(0,3):
    plt.plot(x[i], y[i], color=colors[i], marker=markers[i], label=str(BitSize[i])+" λ")

plt.xlabel('T', labelpad= 15, fontsize = 13)
plt.ylabel('Gas Used Difference ($10^4$)', labelpad= 15, fontsize = 13)

custom_lines = [Line2D([0], [0], color='red', marker='o', lw=1.5),
                Line2D([0], [0], color='green', marker='^', lw=1.5),
                Line2D([0], [0], color='blue', marker='s', lw=1.5),
                Line2D([0], [0], color='black', linestyle='--', lw=1)]

plt.legend(custom_lines, ['λ = 1024', 'λ = 2048', 'λ = 3072'], prop={'size': 11.5})
#plt.legend(bbox_to_anchor=(1.05, 0), loc='lower left', borderaxespad=0., fontsize = 13)

# custom_lines = [Line2D([0], [0], color=colors[i], lw=2) for i in range(3)] + [Line2D([0], [0], color='black', linestyle=lineStyles[i], lw=2) for i in range(2)]
# plt.legend(custom_lines, [str(BitSize[i]) + ' Bits' for i in range(3)] + ['One N', 'N in Proof'])

plt.gca().yaxis.get_offset_text().set_visible(False)
def custom_formatter(x, pos):
    return '{:.0f}'.format(x * 1e-4)
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
plt.subplots_adjust(left=0.17, bottom=0.2) #, right=0.65)  # Adjust the right space as needed)
plt.grid(True, linestyle="--")
plt.savefig('6. T diff.png', dpi=500)
plt.show()
