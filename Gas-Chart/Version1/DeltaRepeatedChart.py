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
  [ 0, 4190332, 'λ2048', 'T2^22' ],
  [ 0, 4399852, 'λ2048', 'T2^23' ],
  [ 0, 4585284, 'λ2048', 'T2^24' ],
  [ 1, 3990731, 'λ2048', 'T2^22' ],
  [ 1, 4199765, 'λ2048', 'T2^23' ],
  [ 1, 4383267, 'λ2048', 'T2^24' ],
  [ 2, 3794976, 'λ2048', 'T2^22' ],
  [ 2, 4000817, 'λ2048', 'T2^23' ],
  [ 2, 4183921, 'λ2048', 'T2^24' ],
  [ 3, 3607262, 'λ2048', 'T2^22' ],
  [ 3, 3808788, 'λ2048', 'T2^23' ],
  [ 3, 3990220, 'λ2048', 'T2^24' ],
  [ 4, 3425290, 'λ2048', 'T2^22' ],
  [ 4, 3624513, 'λ2048', 'T2^23' ],
  [ 4, 3805928, 'λ2048', 'T2^24' ],
  [ 5, 3258901, 'λ2048', 'T2^22' ],
  [ 5, 3457628, 'λ2048', 'T2^23' ],
  [ 5, 3639150, 'λ2048', 'T2^24' ],
  [ 6, 3123341, 'λ2048', 'T2^22' ],
  [ 6, 3322730, 'λ2048', 'T2^23' ],
  [ 6, 3504721, 'λ2048', 'T2^24' ],
  [ 7, 3051765, 'λ2048', 'T2^22' ],
  [ 7, 3249727, 'λ2048', 'T2^23' ],
  [ 7, 3434858, 'λ2048', 'T2^24' ],
  [ 8, 3106944, 'λ2048', 'T2^22' ],
  [ 8, 3306964, 'λ2048', 'T2^23' ],
  [ 8, 3495372, 'λ2048', 'T2^24' ],
  [ 9, 3435971, 'λ2048', 'T2^22' ],
  [ 9, 3641697, 'λ2048', 'T2^23' ],
  [ 9, 3836446, 'λ2048', 'T2^24' ],
  [ 10, 4401008, 'λ2048', 'T2^22' ],
  [ 10, 4620917, 'λ2048', 'T2^23' ],
  [ 10, 4829026, 'λ2048', 'T2^24' ],
  [ 11, 7012471, 'λ2048', 'T2^22' ],
  [ 11, 7261398, 'λ2048', 'T2^23' ],
  [ 11, 7496699, 'λ2048', 'T2^24' ],
  [ 12, 14443978, 'λ2048', 'T2^22' ],
  [ 12, 14753404, 'λ2048', 'T2^23' ],
  [ 12, 15045944, 'λ2048', 'T2^24' ]
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
plt.axvline(x=7.00000001, linestyle='dotted', color='black')
plt.text(7.8, 15900000, 'Minimum', ha='right', fontsize=11)
# plt.axhline(y=2597132, linestyle='dotted', color='black')
# plt.axhline(y=2785754, linestyle='dotted', color='black')
# plt.axhline(y=2967443, linestyle='dotted', color='black')
plt.legend(title="T", fontsize=12, title_fontsize=12)
plt.xlabel('Delta', labelpad= 15, fontsize=13)
plt.ylabel('Gas Used ($10^7$)', labelpad= 15, fontsize=13)
plt.gca().yaxis.get_offset_text().set_visible(False)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# Adjust the bottom margin
plt.subplots_adjust(left=0.15)
plt.subplots_adjust(bottom=0.2)
plt.show()