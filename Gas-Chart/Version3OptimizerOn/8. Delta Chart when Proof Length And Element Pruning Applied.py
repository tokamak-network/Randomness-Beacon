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
  [ '0', '3637127', 'λ2048', 'T2^22' ],
  [ '0', '3819762', 'λ2048', 'T2^23' ],
  [ '0', '3982966', 'λ2048', 'T2^24' ],
  [ '1', '3462352', 'λ2048', 'T2^22' ],
  [ '1', '3643264', 'λ2048', 'T2^23' ],
  [ '1', '3806699', 'λ2048', 'T2^24' ],
  [ '2', '3289911', 'λ2048', 'T2^22' ],
  [ '2', '3469502', 'λ2048', 'T2^23' ],
  [ '2', '3632004', 'λ2048', 'T2^24' ],
  [ '3', '3120055', 'λ2048', 'T2^22' ],
  [ '3', '3297153', 'λ2048', 'T2^23' ],
  [ '3', '3459606', 'λ2048', 'T2^24' ],
  [ '4', '2951184', 'λ2048', 'T2^22' ],
  [ '4', '3129028', 'λ2048', 'T2^23' ],
  [ '4', '3289495', 'λ2048', 'T2^24' ],
  [ '5', '2786572', 'λ2048', 'T2^22' ],
  [ '5', '2965630', 'λ2048', 'T2^23' ],
  [ '5', '3122786', 'λ2048', 'T2^24' ],
  [ '6', '2629421', 'λ2048', 'T2^22' ],
  [ '6', '2805638', 'λ2048', 'T2^23' ],
  [ '6', '2961725', 'λ2048', 'T2^24' ],
  [ '7', '2482828', 'λ2048', 'T2^22' ],
  [ '7', '2658831', 'λ2048', 'T2^23' ],
  [ '7', '2815915', 'λ2048', 'T2^24' ],
  [ '8', '2361460', 'λ2048', 'T2^22' ],
  [ '8', '2535443', 'λ2048', 'T2^23' ],
  [ '8', '2690239', 'λ2048', 'T2^24' ],
  [ '9', '2291549', 'λ2048', 'T2^22' ],
  [ '9', '2464333', 'λ2048', 'T2^23' ],
  [ '9', '2614515', 'λ2048', 'T2^24' ],
  [ '10', '2300850', 'λ2048', 'T2^22' ],
  [ '10', '2472310', 'λ2048', 'T2^23' ],
  [ '10', '2625474', 'λ2048', 'T2^24' ],
  [ '11', '2487936', 'λ2048', 'T2^22' ],
  [ '11', '2656878', 'λ2048', 'T2^23' ],
  [ '11', '2816624', 'λ2048', 'T2^24' ],
  [ '12', '3041044', 'λ2048', 'T2^22' ],
  [ '12', '3206428', 'λ2048', 'T2^23' ],
  [ '12', '3368935', 'λ2048', 'T2^24' ],
  [ '13', '4322558', 'λ2048', 'T2^22' ],
  [ '13', '4487592', 'λ2048', 'T2^23' ],
  [ '13', '4651958', 'λ2048', 'T2^24' ],
  [ '14', '6986702', 'λ2048', 'T2^22' ],
  [ '14', '7148107', 'λ2048', 'T2^23' ],
  [ '14', '7310591', 'λ2048', 'T2^24' ]
]
colors = ["tab:red", "tab:green", "tab:blue"]
markers = ['o', '^', 's']  # circle, triangle, square
x = [[],[],[]]
y = [[],[],[]]
for i in range(len(data)):
    x[i%3].append(int(data[i][0]))
    y[i%3].append(int(data[i][1]))
for i in range(3):
    plt.plot(x[i], y[i], color=colors[i], label="$"+ts[i]+"$", marker=markers[i])
plt.axvline(x=9.00000001, color='black')
plt.text(9.9, 7680000, 'Minimum', ha='right', fontsize=13)
# plt.annotate('Minimum', xy=(10.00000001, 4200000), xytext=(0, 50), 
#              textcoords='offset points', ha='right', va='bottom',
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.legend(title=r'$T$', fontsize=13, title_fontsize=13)
plt.xlabel('Number of Skipped Proof', labelpad= 10.9,fontsize=15 ) 
plt.ylabel('Gas Used ($10^6$)', labelpad= 18, fontsize=15)
plt.gca().yaxis.get_offset_text().set_visible(False)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
# Adjust the bottom margin
#plt.subplots_adjust(top=0.55)
plt.subplots_adjust(bottom=0.1)
plt.grid(True, linestyle="--")
plt.tight_layout()
plt.savefig('8. Delta Chart when Proof Length And Element Pruning Applied.png', dpi=500)
plt.show()