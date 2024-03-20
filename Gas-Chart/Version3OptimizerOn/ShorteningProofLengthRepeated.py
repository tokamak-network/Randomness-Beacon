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
from matplotlib.ticker import FuncFormatter
ts = ["2^{22}", "2^{23}", "2^{24}"]
data = [
[ 0, 4265513, 'λ2048', 'T2^22' ],
[ 0, 4481288, 'λ2048', 'T2^23' ],
[ 0, 4673584, 'λ2048', 'T2^24' ],
[ 1, 4061364, 'λ2048', 'T2^22' ],
[ 1, 4276555, 'λ2048', 'T2^23' ],
[ 1, 4467075, 'λ2048', 'T2^24' ],
[ 2, 3861555, 'λ2048', 'T2^22' ],
[ 2, 4073640, 'λ2048', 'T2^23' ],
[ 2, 4263579, 'λ2048', 'T2^24' ],
[ 3, 3670365, 'λ2048', 'T2^22' ],
[ 3, 3877755, 'λ2048', 'T2^23' ],
[ 3, 4065630, 'λ2048', 'T2^24' ],
[ 4, 3485044, 'λ2048', 'T2^22' ],
[ 4, 3689913, 'λ2048', 'T2^23' ],
[ 4, 3877505, 'λ2048', 'T2^24' ],
[ 5, 3315775, 'λ2048', 'T2^22' ],
[ 5, 3519740, 'λ2048', 'T2^23' ],
[ 5, 3707570, 'λ2048', 'T2^24' ],
[ 6, 3178382, 'λ2048', 'T2^22' ],
[ 6, 3383340, 'λ2048', 'T2^23' ],
[ 6, 3570520, 'λ2048', 'T2^24' ],
[ 7, 3107386, 'λ2048', 'T2^22' ],
[ 7, 3311154, 'λ2048', 'T2^23' ],
[ 7, 3500368, 'λ2048', 'T2^24' ],
[ 8, 3166877, 'λ2048', 'T2^22' ],
[ 8, 3373064, 'λ2048', 'T2^23' ],
[ 8, 3564869, 'λ2048', 'T2^24' ],
[ 9, 3508772, 'λ2048', 'T2^22' ],
[ 9, 3721172, 'λ2048', 'T2^23' ],
[ 9, 3918982, 'λ2048', 'T2^24' ],
[ 10, 4503325, 'λ2048', 'T2^22' ],
[ 10, 4729648, 'λ2048', 'T2^23' ],
[ 10, 4941635, 'λ2048', 'T2^24' ],
[ 11, 7176504, 'λ2048', 'T2^22' ],
[ 11, 7431737, 'λ2048', 'T2^23' ],
[ 11, 7671864, 'λ2048', 'T2^24' ],
[ 12, 14733094, 'λ2048', 'T2^22' ],
[ 12, 15050832, 'λ2048', 'T2^23' ],
[ 12, 15348354, 'λ2048', 'T2^24' ]
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
plt.axvline(x=7.00000001, color='black')
plt.text(7.8, 16100000, 'Minimum', ha='right', fontsize=11)
# plt.annotate('Minimum', xy=(10.00000001, 4200000), xytext=(0, 50), 
#              textcoords='offset points', ha='right', va='bottom',
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.legend(title="T", fontsize=13, title_fontsize=13)
plt.xlabel('Number of Skipped Proof', labelpad= 15, fontsize=13, y=-0.1)
plt.ylabel('Gas Used ($10^6$)', labelpad= 15, fontsize=13)
plt.gca().yaxis.get_offset_text().set_visible(False)
def custom_formatter(x, pos):
    return '{:.0f}'.format(x * 1e-6)
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Adjust the bottom margin
plt.subplots_adjust(left=0.17)
plt.subplots_adjust(bottom=0.2)
plt.grid(True, linestyle="--")
plt.savefig('delta repeated.png', dpi=500)
plt.show()