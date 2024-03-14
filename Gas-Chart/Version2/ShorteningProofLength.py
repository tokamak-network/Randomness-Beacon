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
  [ 0, 4343887, 'λ2048', 'T2^22' ],
  [ 0, 4560589, 'λ2048', 'T2^23' ],
  [ 0, 4754491, 'λ2048', 'T2^24' ],
  [ 1, 4135075, 'λ2048', 'T2^22' ],
  [ 1, 4351111, 'λ2048', 'T2^23' ],
  [ 1, 4543238, 'λ2048', 'T2^24' ],
  [ 2, 3928589, 'λ2048', 'T2^22' ],
  [ 2, 4141295, 'λ2048', 'T2^23' ],
  [ 2, 4332767, 'λ2048', 'T2^24' ],
  [ 3, 3727140, 'λ2048', 'T2^22' ],
  [ 3, 3935249, 'λ2048', 'T2^23' ],
  [ 3, 4124810, 'λ2048', 'T2^24' ],
  [ 4, 3524977, 'λ2048', 'T2^22' ],
  [ 4, 3730745, 'λ2048', 'T2^23' ],
  [ 4, 3919868, 'λ2048', 'T2^24' ],
  [ 5, 3326169, 'λ2048', 'T2^22' ],
  [ 5, 3530794, 'λ2048', 'T2^23' ],
  [ 5, 3719769, 'λ2048', 'T2^24' ],
  [ 6, 3133572, 'λ2048', 'T2^22' ],
  [ 6, 3337801, 'λ2048', 'T2^23' ],
  [ 6, 3526214, 'λ2048', 'T2^24' ],
  [ 7, 2955284, 'λ2048', 'T2^22' ],
  [ 7, 3155982, 'λ2048', 'T2^23' ],
  [ 7, 3345753, 'λ2048', 'T2^24' ],
  [ 8, 2799628, 'λ2048', 'T2^22' ],
  [ 8, 2998537, 'λ2048', 'T2^23' ],
  [ 8, 3188072, 'λ2048', 'T2^24' ],
  [ 9, 2689635, 'λ2048', 'T2^22' ],
  [ 9, 2886284, 'λ2048', 'T2^23' ],
  [ 9, 3075517, 'λ2048', 'T2^24' ],
  [ 10, 2675782, 'λ2048', 'T2^22' ],
  [ 10, 2871035, 'λ2048', 'T2^23' ],
  [ 10, 3060337, 'λ2048', 'T2^24' ],
  [ 11, 2848777, 'λ2048', 'T2^22' ],
  [ 11, 3042207, 'λ2048', 'T2^23' ],
  [ 11, 3231467, 'λ2048', 'T2^24' ],
  [ 12, 3417484, 'λ2048', 'T2^22' ],
  [ 12, 3609489, 'λ2048', 'T2^23' ],
  [ 12, 3801471, 'λ2048', 'T2^24' ],
  [ 13, 4903829, 'λ2048', 'T2^22' ],
  [ 13, 5096756, 'λ2048', 'T2^23' ],
  [ 13, 5250235, 'λ2048', 'T2^24' ],
  [ 14, 8515295, 'λ2048', 'T2^22' ],
  [ 14, 8703025, 'λ2048', 'T2^23' ],
  [ 14, 8891806, 'λ2048', 'T2^24' ]
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
plt.axvline(x=10.00000001, linestyle='dotted', color='black')
plt.text(10.9, 9290000, 'Minimum', ha='right', fontsize=11)
# plt.annotate('Minimum', xy=(10.00000001, 4200000), xytext=(0, 50), 
#              textcoords='offset points', ha='right', va='bottom',
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.legend(title="T", fontsize=13, title_fontsize=13)
plt.xlabel('Delta', labelpad= 15, fontsize=13)
plt.ylabel('Gas Used ($10^6$)', labelpad= 15, fontsize=13)
plt.gca().yaxis.get_offset_text().set_visible(False)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Adjust the bottom margin
plt.subplots_adjust(left=0.15)
plt.subplots_adjust(bottom=0.2)
plt.show()