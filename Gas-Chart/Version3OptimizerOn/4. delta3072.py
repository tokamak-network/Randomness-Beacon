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
  [ 0, 7378207, 'λ3072', 'T2^22' ],
  [ 0, 7706138, 'λ3072', 'T2^23' ],
  [ 0, 8098164, 'λ3072', 'T2^24' ],
  [ 1, 7026264, 'λ3072', 'T2^22' ],
  [ 1, 7351039, 'λ3072', 'T2^23' ],
  [ 1, 7742890, 'λ3072', 'T2^24' ],
  [ 2, 6675939, 'λ3072', 'T2^22' ],
  [ 2, 7005893, 'λ3072', 'T2^23' ],
  [ 2, 7389605, 'λ3072', 'T2^24' ],
  [ 3, 6331297, 'λ3072', 'T2^22' ],
  [ 3, 6662708, 'λ3072', 'T2^23' ],
  [ 3, 7040387, 'λ3072', 'T2^24' ],
  [ 4, 5991349, 'λ3072', 'T2^22' ],
  [ 4, 6319148, 'λ3072', 'T2^23' ],
  [ 4, 6700914, 'λ3072', 'T2^24' ],
  [ 5, 5659029, 'λ3072', 'T2^22' ],
  [ 5, 5983952, 'λ3072', 'T2^23' ],
  [ 5, 6363188, 'λ3072', 'T2^24' ],
  [ 6, 5339147, 'λ3072', 'T2^22' ],
  [ 6, 5667383, 'λ3072', 'T2^23' ],
  [ 6, 6043488, 'λ3072', 'T2^24' ],
  [ 7, 5047288, 'λ3072', 'T2^22' ],
  [ 7, 5373012, 'λ3072', 'T2^23' ],
  [ 7, 5746031, 'λ3072', 'T2^24' ],
  [ 8, 4809775, 'λ3072', 'T2^22' ],
  [ 8, 5131435, 'λ3072', 'T2^23' ],
  [ 8, 5501757, 'λ3072', 'T2^24' ],
  [ 9, 4708272, 'λ3072', 'T2^22' ],
  [ 9, 5036234, 'λ3072', 'T2^23' ],
  [ 9, 5400236, 'λ3072', 'T2^24' ],
  [ 10, 4768639, 'λ3072', 'T2^22' ],
  [ 10, 5094782, 'λ3072', 'T2^23' ],
  [ 10, 5458807, 'λ3072', 'T2^24' ],
  [ 11, 5237267, 'λ3072', 'T2^22' ],
  [ 11, 5562540, 'λ3072', 'T2^23' ],
  [ 11, 5928166, 'λ3072', 'T2^24' ],
  [ 12, 6584395, 'λ3072', 'T2^22' ],
  [ 12, 6903174, 'λ3072', 'T2^23' ],
  [ 12, 7264840, 'λ3072', 'T2^24' ],
  [ 13, 9654278, 'λ3072', 'T2^22' ],
  [ 13, 9971154, 'λ3072', 'T2^23' ],
  [ 13, 10331621, 'λ3072', 'T2^24' ],
  [ 14, 16665189, 'λ3072', 'T2^22' ],
  [ 14, 16981575, 'λ3072', 'T2^23' ],
  [ 14, 17332122, 'λ3072', 'T2^24' ]
]

#colors = ['#ff0000', '#008800', '#0000ff']
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
plt.text(9.9, 18280000, 'Minimum', ha='right', fontsize=15)
# plt.annotate('Minimum', xy=(10.00000001, 4200000), xytext=(0, 50), 
#              textcoords='offset points', ha='right', va='bottom',
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.legend(title=r'$\tau$', fontsize=18, title_fontsize=18)
plt.xlabel('Number of Skipped Proof',labelpad= 10.9,fontsize=21 ) #y=-0.1
plt.ylabel('Gas Used ($10^6$)', labelpad= 7, fontsize=21)
plt.gca().yaxis.get_offset_text().set_visible(False)
def custom_formatter(x, _):
    return '{:.0f}'.format(x * 1e-6)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(custom_formatter))
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
# Adjust the bottom margin
#plt.subplots_adjust(top=0.55)
plt.subplots_adjust(bottom=0.1)
plt.grid(True, linestyle="--")
# fig_size = plt.gcf().get_size_inches() # Get current size
# fig_size[1] += 0.1
# plt.gcf().set_size_inches(fig_size) # Set new size
plt.tight_layout()
plt.savefig('4. delta3072.png', dpi=500)
plt.show()