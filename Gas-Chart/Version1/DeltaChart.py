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
# delta, gasUsed, lambda, t
data = [
  [ 0, 4193578, 'λ2048', 'T2^22' ],
  [ 0, 4403125, 'λ2048', 'T2^23' ],
  [ 0, 4588586, 'λ2048', 'T2^24' ],
  [ 1, 3992228, 'λ2048', 'T2^22' ],
  [ 1, 4201281, 'λ2048', 'T2^23' ],
  [ 1, 4384775, 'λ2048', 'T2^24' ],
  [ 2, 3793120, 'λ2048', 'T2^22' ],
  [ 2, 3998905, 'λ2048', 'T2^23' ],
  [ 2, 4181976, 'λ2048', 'T2^24' ],
  [ 3, 3598872, 'λ2048', 'T2^22' ],
  [ 3, 3800217, 'λ2048', 'T2^23' ],
  [ 3, 3981504, 'λ2048', 'T2^24' ],
  [ 4, 3404088, 'λ2048', 'T2^22' ],
  [ 4, 3602890, 'λ2048', 'T2^23' ],
  [ 4, 3783960, 'λ2048', 'T2^24' ],
  [ 5, 3212507, 'λ2048', 'T2^22' ],
  [ 5, 3410301, 'λ2048', 'T2^23' ],
  [ 5, 3591080, 'λ2048', 'T2^24' ],
  [ 6, 3027064, 'λ2048', 'T2^22' ],
  [ 6, 3224512, 'λ2048', 'T2^23' ],
  [ 6, 3404924, 'λ2048', 'T2^24' ],
  [ 7, 2855772, 'λ2048', 'T2^22' ],
  [ 7, 3049824, 'λ2048', 'T2^23' ],
  [ 7, 3231708, 'λ2048', 'T2^24' ],
  [ 8, 2707247, 'λ2048', 'T2^22' ],
  [ 8, 2899354, 'λ2048', 'T2^23' ],
  [ 8, 3081199, 'λ2048', 'T2^24' ],
  [ 9, 2604238, 'λ2048', 'T2^22' ],
  [ 9, 2794209, 'λ2048', 'T2^23' ],
  [ 9, 2975659, 'λ2048', 'T2^24' ],
  [ 10, 2597132, 'λ2048', 'T2^22' ],
  [ 10, 2785754, 'λ2048', 'T2^23' ],
  [ 10, 2967443, 'λ2048', 'T2^24' ],
  [ 11, 2776764, 'λ2048', 'T2^22' ],
  [ 11, 2963661, 'λ2048', 'T2^23' ],
  [ 11, 3145417, 'λ2048', 'T2^24' ],
  [ 12, 3352210, 'λ2048', 'T2^22' ],
  [ 12, 3537561, 'λ2048', 'T2^23' ],
  [ 12, 3722199, 'λ2048', 'T2^24' ],
  [ 13, 4844745, 'λ2048', 'T2^22' ],
  [ 13, 5031036, 'λ2048', 'T2^23' ],
  [ 13, 5217754, 'λ2048', 'T2^24' ],
  [ 14, 8464045, 'λ2048', 'T2^22' ],
  [ 14, 8645321, 'λ2048', 'T2^23' ],
  [ 14, 8826940, 'λ2048', 'T2^24' ]
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

#plt.plot(data[i][0], data[i][1], color=colors[i%3], label=data[i][3][1:], marker=markers[i%3])