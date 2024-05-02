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
  [ 0, 6706388, 'λ3072', 'T2^22' ],
  [ 0, 7001533, 'λ3072', 'T2^23' ],
  [ 0, 7359538, 'λ3072', 'T2^24' ],
  [ 1, 6387325, 'λ3072', 'T2^22' ],
  [ 1, 6679585, 'λ3072', 'T2^23' ],
  [ 1, 7037679, 'λ3072', 'T2^24' ],
  [ 2, 6069625, 'λ3072', 'T2^22' ],
  [ 2, 6367373, 'λ3072', 'T2^23' ],
  [ 2, 6717618, 'λ3072', 'T2^24' ],
  [ 3, 5757347, 'λ3072', 'T2^22' ],
  [ 3, 6056790, 'λ3072', 'T2^23' ],
  [ 3, 6401328, 'λ3072', 'T2^24' ],
  [ 4, 5449571, 'λ3072', 'T2^22' ],
  [ 4, 5745584, 'λ3072', 'T2^23' ],
  [ 4, 6094548, 'λ3072', 'T2^24' ],
  [ 5, 5149081, 'λ3072', 'T2^22' ],
  [ 5, 5442482, 'λ3072', 'T2^23' ],
  [ 5, 5789145, 'λ3072', 'T2^24' ],
  [ 6, 4860853, 'λ3072', 'T2^22' ],
  [ 6, 5157761, 'λ3072', 'T2^23' ],
  [ 6, 5501594, 'λ3072', 'T2^24' ],
  [ 7, 4600296, 'λ3072', 'T2^22' ],
  [ 7, 4894949, 'λ3072', 'T2^23' ],
  [ 7, 5236022, 'λ3072', 'T2^24' ],
  [ 8, 4393892, 'λ3072', 'T2^22' ],
  [ 8, 4684707, 'λ3072', 'T2^23' ],
  [ 8, 5023362, 'λ3072', 'T2^24' ],
  [ 9, 4320200, 'λ3072', 'T2^22' ],
  [ 9, 4617307, 'λ3072', 'T2^23' ],
  [ 9, 4949718, 'λ3072', 'T2^24' ],
  [ 10, 4411375, 'λ3072', 'T2^22' ],
  [ 10, 4706867, 'λ3072', 'T2^23' ],
  [ 10, 5039546, 'λ3072', 'T2^24' ],
  [ 11, 4910420, 'λ3072', 'T2^22' ],
  [ 11, 5205377, 'λ3072', 'T2^23' ],
  [ 11, 5539958, 'λ3072', 'T2^24' ],
  [ 12, 6291215, 'λ3072', 'T2^22' ],
  [ 12, 6580266, 'λ3072', 'T2^23' ],
  [ 12, 6911518, 'λ3072', 'T2^24' ],
  [ 13, 9391115, 'λ3072', 'T2^22' ],
  [ 13, 9678539, 'λ3072', 'T2^23' ],
  [ 13, 10008904, 'λ3072', 'T2^24' ],
  [ 14, 16433433, 'λ3072', 'T2^22' ],
  [ 14, 16720860, 'λ3072', 'T2^23' ],
  [ 14, 17041885, 'λ3072', 'T2^24' ]
]
colors = ["tab:red", "tab:green", "tab:blue"]
markers = ['o', '^', 's']  # circle, triangle, square
x = [[],[],[]]
y = [[],[],[]]
for i in range(len(data)):
    x[i%3].append(data[i][0])
    y[i%3].append(data[i][1])
for i in range(3):
    plt.plot(x[i], y[i], color=colors[i], label="$"+ts[i]+"$", marker=markers[i])
plt.axvline(x=9.00285,  color='black')
plt.text(9.9, 18000000, 'Minimum', ha='right', fontsize=13)
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