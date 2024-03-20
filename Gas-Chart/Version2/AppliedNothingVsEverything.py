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
AppliedNothing = NTXYVInProof = [
  [ 3921992, 'λ2048', 'T2^20' ],
  [ 4128691, 'λ2048', 'T2^21' ],
  [ 4338719, 'λ2048', 'T2^22' ],
  [ 4555330, 'λ2048', 'T2^23' ],
  [ 4749156, 'λ2048', 'T2^24' ],
  [ 4980923, 'λ2048', 'T2^25' ],
]
AppliedEverything = [
  [ 8, 2121825, 'λ2048', 'T2^20' ],
  [ 8, 2294894, 'λ2048', 'T2^21' ],
  [ 8, 2470614, 'λ2048', 'T2^22' ],
  [ 8, 2645229, 'λ2048', 'T2^23' ],
  [ 8, 2809183, 'λ2048', 'T2^24' ],
  [ 8, 2997233, 'λ2048', 'T2^25' ],
  [ 9, 2037925, 'λ2048', 'T2^20' ],
  [ 9, 2210566, 'λ2048', 'T2^21' ],
  [ 9, 2385186, 'λ2048', 'T2^22' ],
  [ 9, 2557626, 'λ2048', 'T2^23' ],
  [ 9, 2721487, 'λ2048', 'T2^24' ],
  [ 9, 2908376, 'λ2048', 'T2^25' ],
  [ 10, 2053635, 'λ2048', 'T2^20' ],
  [ 10, 2226654, 'λ2048', 'T2^21' ],
  [ 10, 2399814, 'λ2048', 'T2^22' ],
  [ 10, 2566266, 'λ2048', 'T2^23' ],
  [ 10, 2730371, 'λ2048', 'T2^24' ],
  [ 10, 2916069, 'λ2048', 'T2^25' ],
]

# 4 colors for 4 lines
colors = ['#ff0000', '#008800', '#0000ff', 'orange']
# 4 markers for 4 lines
markers = ['o', '^', 's', 'D']  # circle, triangle, square, diamond
ts = ["$2^{20}$", "$2^{21}$", "$2^{22}$", "$2^{23}$", "$2^{24}$", "$2^{25}$"]
x = [[],[],[],[]]
y = [[],[],[],[]]

for i in range(len(AppliedNothing)):
  x[0].append(ts[i])
  y[0].append(AppliedNothing[i][0])
for i in range(0, len(AppliedEverything), 6):
  for j in range(6):
    x[i//6+1].append(ts[j])
    y[i//6+1].append(AppliedEverything[i+j][1])

plt.plot(x[0], y[0], color=colors[0], marker=markers[0], linestyle="--")
plt.plot(x[1], y[1], color=colors[1], marker=markers[1], label="δ = 8")
plt.plot(x[3], y[3], color=colors[3], marker=markers[3], label="δ = 10")
plt.plot(x[2], y[2], color=colors[2], marker=markers[2], label="δ = 9")
custom_lines = [Line2D([0], [0], color='red', linestyle='--', marker='o', lw=1),
                Line2D([0], [0], color='black', linestyle='-', lw=1),
                Line2D([0], [0], color='green', marker='D', lw=1.5),
                Line2D([0], [0], color='blue', marker='s', lw=1.5),
                Line2D([0], [0], color='orange', marker='^', lw=1.5)]
plt.legend(custom_lines, ['Nothing Applied', "All Applied",'δ = 8', 'δ = 9', 'δ = 10'], prop={'size': 11.5},bbox_to_anchor=(0.43, 0.4))
plt.xlabel('T', labelpad= 15, fontsize = 13)
plt.ylabel('Gas Used ($10^5$)', labelpad= 15, fontsize = 13)
plt.gca().yaxis.get_offset_text().set_visible(False)
def custom_formatter(x, pos):
    return '{:.0f}'.format(x * 1e-5)
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
plt.subplots_adjust(left=0.17, bottom=0.2) #, right=0.65)  # Adjust the right space as needed)
plt.grid(True, linestyle="--")
plt.savefig('7. AllAndNoneApplied.png', dpi=500)  # Adjust the dpi as needed
plt.show()
