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
data = [
  [ '0', '3477259', 'λ2048', 'T2^21' ],
  [ '0', '3826182', 'λ2048', 'T2^23' ],
  [ '0', '4180322', 'λ2048', 'T2^25' ],
  [ '1', '3302900', 'λ2048', 'T2^21' ],
  [ '1', '3649559', 'λ2048', 'T2^23' ],
  [ '1', '4002690', 'λ2048', 'T2^25' ],
  [ '2', '3129633', 'λ2048', 'T2^21' ],
  [ '2', '3475634', 'λ2048', 'T2^23' ],
  [ '2', '3826551', 'λ2048', 'T2^25' ],
  [ '3', '2960686', 'λ2048', 'T2^21' ],
  [ '3', '3303148', 'λ2048', 'T2^23' ],
  [ '3', '3651469', 'λ2048', 'T2^25' ],
  [ '4', '2792283', 'λ2048', 'T2^21' ],
  [ '4', '3134860', 'λ2048', 'T2^23' ],
  [ '4', '3482112', 'λ2048', 'T2^25' ],
  [ '5', '2626659', 'λ2048', 'T2^21' ],
  [ '5', '2971324', 'λ2048', 'T2^23' ],
  [ '5', '3313537', 'λ2048', 'T2^25' ],
  [ '6', '2468299', 'λ2048', 'T2^21' ],
  [ '6', '2811170', 'λ2048', 'T2^23' ],
  [ '6', '3151914', 'λ2048', 'T2^25' ],
  [ '7', '2324793', 'λ2048', 'T2^21' ],
  [ '7', '2664384', 'λ2048', 'T2^23' ],
  [ '7', '3002151', 'λ2048', 'T2^25' ],
  [ '8', '2203286', 'λ2048', 'T2^21' ],
  [ '8', '2540952', 'λ2048', 'T2^23' ],
  [ '8', '2876089', 'λ2048', 'T2^25' ],
  [ '9', '2133372', 'λ2048', 'T2^21' ],
  [ '9', '2470594', 'λ2048', 'T2^23' ],
  [ '9', '2799805', 'λ2048', 'T2^25' ],
  [ '10', '2147290', 'λ2048', 'T2^21' ],
  [ '10', '2481625', 'λ2048', 'T2^23' ],
  [ '10', '2809564', 'λ2048', 'T2^25' ],
  [ '11', '2348458', 'λ2048', 'T2^21' ],
  [ '11', '2678874', 'λ2048', 'T2^23' ],
  [ '11', '3011533', 'λ2048', 'T2^25' ],
  [ '12', '2952367', 'λ2048', 'T2^21' ],
  [ '12', '3281754', 'λ2048', 'T2^23' ],
  [ '12', '3607656', 'λ2048', 'T2^25' ],
  [ '13', '4460145', 'λ2048', 'T2^21' ],
  [ '13', '4790519', 'λ2048', 'T2^23' ],
  [ '13', '5125162', 'λ2048', 'T2^25' ],
  [ '14', '8111726', 'λ2048', 'T2^21' ],
  [ '14', '8434021', 'λ2048', 'T2^23' ],
  [ '14', '8759346', 'λ2048', 'T2^25' ]
]
ts = ["21", "23",  "25"]
colors = ["tab:red", "tab:green", "tab:blue"]
 # circle, triangle, square
markers = ['o', '^', 's']
x = [[],[],[]]
y = [[],[],[]]
for i in range(len(data)):
    x[i%3].append(int(data[i][0]))
    y[i%3].append(int(data[i][1]))
for i in range(3):
    plt.plot(x[i], y[i], color=colors[i], label="$"+ts[i]+"$", marker=markers[i])
plt.axvline(x=9.00000001, color='black')
plt.text(10, 9180000, 'Minimum', ha='right', fontsize=13)
# plt.annotate('Minimum', xy=(10.00000001, 4200000), xytext=(0, 50), 
#              textcoords='offset points', ha='right', va='bottom',
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.legend(title=r'$\tau$', fontsize=13, title_fontsize=13)
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