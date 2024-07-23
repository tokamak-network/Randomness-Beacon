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
  [ '0', '6701878', 'λ3072', 'T2^22' ],
  [ '0', '6996898', 'λ3072', 'T2^23' ],
  [ '0', '7354495', 'λ3072', 'T2^24' ],
  [ '1', '6383071', 'λ3072', 'T2^22' ],
  [ '1', '6675222', 'λ3072', 'T2^23' ],
  [ '1', '7032908', 'λ3072', 'T2^24' ],
  [ '2', '6065631', 'λ3072', 'T2^22' ],
  [ '2', '6363254', 'λ3072', 'T2^23' ],
  [ '2', '6713091', 'λ3072', 'T2^24' ],
  [ '3', '5753613', 'λ3072', 'T2^22' ],
  [ '3', '6052915', 'λ3072', 'T2^23' ],
  [ '3', '6397061', 'λ3072', 'T2^24' ],
  [ '4', '5446081', 'λ3072', 'T2^22' ],
  [ '4', '5741953', 'λ3072', 'T2^23' ],
  [ '4', '6090540', 'λ3072', 'T2^24' ],
  [ '5', '5145851', 'λ3072', 'T2^22' ],
  [ '5', '5439096', 'λ3072', 'T2^23' ],
  [ '5', '5785397', 'λ3072', 'T2^24' ],
  [ '6', '4857883', 'λ3072', 'T2^22' ],
  [ '6', '5154619', 'λ3072', 'T2^23' ],
  [ '6', '5498098', 'λ3072', 'T2^24' ],
  [ '7', '4597578', 'λ3072', 'T2^22' ],
  [ '7', '4892043', 'λ3072', 'T2^23' ],
  [ '7', '5232785', 'λ3072', 'T2^24' ],
  [ '8', '4425788', 'λ3072', 'T2^22' ],
  [ '8', '4718680', 'λ3072', 'T2^23' ],
  [ '8', '5059652', 'λ3072', 'T2^24' ],
  [ '9', '4318050', 'λ3072', 'T2^22' ],
  [ '9', '4614955', 'λ3072', 'T2^23' ],
  [ '9', '4947040', 'λ3072', 'T2^24' ],
  [ '10', '4409533', 'λ3072', 'T2^22' ],
  [ '10', '4704821', 'λ3072', 'T2^23' ],
  [ '10', '5037178', 'λ3072', 'T2^24' ],
  [ '11', '4908917', 'λ3072', 'T2^22' ],
  [ '11', '5203672', 'λ3072', 'T2^23' ],
  [ '11', '5537941', 'λ3072', 'T2^24' ],
  [ '12', '6290043', 'λ3072', 'T2^22' ],
  [ '12', '6578898', 'λ3072', 'T2^23' ],
  [ '12', '6909863', 'λ3072', 'T2^24' ],
  [ '13', '9390036', 'λ3072', 'T2^22' ],
  [ '13', '9677264', 'λ3072', 'T2^23' ],
  [ '13', '10007353', 'λ3072', 'T2^24' ],
  [ '14', '16432336', 'λ3072', 'T2^22' ],
  [ '14', '16719577', 'λ3072', 'T2^23' ],
  [ '14', '17040333', 'λ3072', 'T2^24' ],
]
ts = ["22", "23",  "24"]
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
plt.axvline(x=9.00285,  color='black')
plt.text(10, 17950000, 'Minimum', ha='right', fontsize=13)
# plt.annotate('Minimum', xy=(10.00000001, 4200000), xytext=(0, 50), 
#              textcoords='offset points', ha='right', va='bottom',
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.legend(title=r'$\tau$', fontsize=13, title_fontsize=13)
plt.xlabel('Number of Skipped Proof', labelpad= 10.9,fontsize=15 ) #y=-0.1
plt.ylabel('Gas Used ($10^6$)', labelpad= 7, fontsize=15)
plt.gca().yaxis.get_offset_text().set_visible(False)
def custom_formatter(x, _):
    return '{:.0f}'.format(x * 1e-6)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(custom_formatter))
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

plt.subplots_adjust(bottom=0.1)
plt.grid(True, linestyle="--")
plt.tight_layout()
plt.savefig('8. Delta Chart when Proof Length And Element Pruning Applied3072.png', dpi=500)
plt.show()