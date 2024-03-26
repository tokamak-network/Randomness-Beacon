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
[ 3746113, 'λ2048', 'T2^20' ],
[ 3937877, 'λ2048', 'T2^21' ],
[ 4127804, 'λ2048', 'T2^22' ],
[ 4334579, 'λ2048', 'T2^23' ],
[ 4520732, 'λ2048', 'T2^24' ],
[ 4735860, 'λ2048', 'T2^25' ]
]
AppliedEverything = [
[ 8, 2041688, 'λ2048', 'T2^20' ],
[ 8, 2205528, 'λ2048', 'T2^21' ],
[ 8, 2369185, 'λ2048', 'T2^22' ],
[ 8, 2543717, 'λ2048', 'T2^23' ],
[ 8, 2698784, 'λ2048', 'T2^24' ],
[ 8, 2879220, 'λ2048', 'T2^25' ],
[ 9, 1964917, 'λ2048', 'T2^20' ],
[ 9, 2127046, 'λ2048', 'T2^21' ],
[ 9, 2290828, 'λ2048', 'T2^22' ],
[ 9, 2463480, 'λ2048', 'T2^23' ],
[ 9, 2618446, 'λ2048', 'T2^24' ],
[ 9, 2797229, 'λ2048', 'T2^25' ],
[ 10, 1987078, 'λ2048', 'T2^20' ],
[ 10, 2148986, 'λ2048', 'T2^21' ],
[ 10, 2311847, 'λ2048', 'T2^22' ],
[ 10, 2483847, 'λ2048', 'T2^23' ],
[ 10, 2637298, 'λ2048', 'T2^24' ],
[ 10, 2812165, 'λ2048', 'T2^25' ],
]

# 4 colors for 4 lines
colors = ["tab:red", "tab:green", "tab:blue", "tab:orange"]
# 4 markers for 4 lines
markers = ['o', 'P', 's', 'D']  # circle, triangle, square, diamond
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
custom_lines = [Line2D([0], [0], color='tab:red', linestyle='--', marker='o', lw=1),
                Line2D([0], [0], color='black', linestyle='-', lw=1),
                Line2D([0], [0], color='tab:green', marker='P', lw=1.5),
                Line2D([0], [0], color='tab:blue', marker='s', lw=1.5),
                Line2D([0], [0], color='tab:orange', marker='^', lw=1.5)]
plt.legend(custom_lines, ['Baseline Model', "Optimized",'δ = 8', 'δ = 9', 'δ = 10'], prop={'size': 12},bbox_to_anchor=(0.39, 0.4))
plt.xlabel(r'Exponentiation ($\tau$)', labelpad= 15, fontsize = 14)
plt.ylabel('Gas Used ($10^5$)', labelpad= 15, fontsize = 14)
plt.gca().yaxis.get_offset_text().set_visible(False)
def custom_formatter(x, pos):
    return '{:.0f}'.format(x * 1e-5)
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))
plt.yticks(fontsize=13)
plt.xticks(fontsize=13)
plt.grid(True, linestyle="--")
plt.tight_layout()
plt.savefig('7. AllAndNoneApplied.png', dpi=500)  # Adjust the dpi as needed
plt.show()
