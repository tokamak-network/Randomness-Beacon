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
ts = ["2^{22}", "2^{23}", "2^{24}"]
data = [
  [ 0, 3789036, 'λ2048', 'T2^22' ],
  [ 0, 3981689, 'λ2048', 'T2^23' ],
  [ 0, 4149269, 'λ2048', 'T2^24' ],
  [ 1, 3606592, 'λ2048', 'T2^22' ],
  [ 1, 3798848, 'λ2048', 'T2^23' ],
  [ 1, 3964769, 'λ2048', 'T2^24' ],
  [ 2, 3426672, 'λ2048', 'T2^22' ],
  [ 2, 3615924, 'λ2048', 'T2^23' ],
  [ 2, 3781407, 'λ2048', 'T2^24' ],
  [ 3, 3251902, 'λ2048', 'T2^22' ],
  [ 3, 3436434, 'λ2048', 'T2^23' ],
  [ 3, 3599969, 'λ2048', 'T2^24' ],
  [ 4, 3076279, 'λ2048', 'T2^22' ],
  [ 4, 3258161, 'λ2048', 'T2^23' ],
  [ 4, 3421451, 'λ2048', 'T2^24' ],
  [ 5, 2903568, 'λ2048', 'T2^22' ],
  [ 5, 3084264, 'λ2048', 'T2^23' ],
  [ 5, 3247489, 'λ2048', 'T2^24' ],
  [ 6, 2736858, 'λ2048', 'T2^22' ],
  [ 6, 2917637, 'λ2048', 'T2^23' ],
  [ 6, 3079587, 'λ2048', 'T2^24' ],
  [ 7, 2584431, 'λ2048', 'T2^22' ],
  [ 7, 2762164, 'λ2048', 'T2^23' ],
  [ 7, 2924635, 'λ2048', 'T2^24' ],
  [ 8, 2454169, 'λ2048', 'T2^22' ],
  [ 8, 2630345, 'λ2048', 'T2^23' ],
  [ 8, 2792191, 'λ2048', 'T2^24' ],
  [ 9, 2369604, 'λ2048', 'T2^22' ],
  [ 9, 2544054, 'λ2048', 'T2^23' ],
  [ 9, 2705219, 'λ2048', 'T2^24' ],
  [ 10, 2385327, 'λ2048', 'T2^22' ],
  [ 10, 2558241, 'λ2048', 'T2^23' ],
  [ 10, 2715319, 'λ2048', 'T2^24' ],
  [ 11, 2578323, 'λ2048', 'T2^22' ],
  [ 11, 2748520, 'λ2048', 'T2^23' ],
  [ 11, 2911090, 'λ2048', 'T2^24' ],
  [ 12, 3177501, 'λ2048', 'T2^22' ],
  [ 12, 3347233, 'λ2048', 'T2^23' ],
  [ 12, 3505161, 'λ2048', 'T2^24' ],
  [ 13, 4680501, 'λ2048', 'T2^22' ],
  [ 13, 4850492, 'λ2048', 'T2^23' ],
  [ 13, 5017780, 'λ2048', 'T2^24' ],
  [ 14, 8320839, 'λ2048', 'T2^22' ],
  [ 14, 8485888, 'λ2048', 'T2^23' ],
  [ 14, 8649593, 'λ2048', 'T2^24' ]
]
colors = ['#ff0000', '#008800', '#0000ff']
markers = ['o', '^', 's']  # circle, triangle, square
x = [[],[],[]]
y = [[],[],[]]
for i in range(len(data)):
    x[i%3].append(data[i][0])
    y[i%3].append(data[i][1])
for i in range(3):
    plt.plot(x[i], y[i], color=colors[i], label="$"+ts[i]+"$", marker=markers[i])
plt.axvline(x=9.00000001, color='black')
plt.text(9.9, 9090000, 'Minimum', ha='right', fontsize=11)
# plt.annotate('Minimum', xy=(10.00000001, 4200000), xytext=(0, 50), 
#              textcoords='offset points', ha='right', va='bottom',
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.legend(title="T", fontsize=13, title_fontsize=13)
plt.xlabel('Number of Skipped Proof', labelpad= 15, fontsize=13, y=-0.1)
plt.ylabel('Gas Used ($10^6$)', labelpad= 15, fontsize=13)
plt.gca().yaxis.get_offset_text().set_visible(False)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Adjust the bottom margin
plt.subplots_adjust(left=0.17)
plt.subplots_adjust(bottom=0.2)
plt.grid(True, linestyle="--")
plt.savefig('8. Delta Chart when Proof Length And Element Pruning Applied.png', dpi=500)
plt.show()