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
  [ 0, 4340674, 'λ2048', 'T2^22' ],
  [ 0, 4557336, 'λ2048', 'T2^23' ],
  [ 0, 4751208, 'λ2048', 'T2^24' ],
  [ 1, 4133623, 'λ2048', 'T2^22' ],
  [ 1, 4349640, 'λ2048', 'T2^23' ],
  [ 1, 4541761, 'λ2048', 'T2^24' ],
  [ 2, 3930498, 'λ2048', 'T2^22' ],
  [ 2, 4143273, 'λ2048', 'T2^23' ],
  [ 2, 4334778, 'λ2048', 'T2^24' ],
  [ 3, 3735617, 'λ2048', 'T2^22' ],
  [ 3, 3943911, 'λ2048', 'T2^23' ],
  [ 3, 4133631, 'λ2048', 'T2^24' ],
  [ 4, 3546315, 'λ2048', 'T2^22' ],
  [ 4, 3752525, 'λ2048', 'T2^23' ],
  [ 4, 3942001, 'λ2048', 'T2^24' ],
  [ 5, 3372822, 'λ2048', 'T2^22' ],
  [ 5, 3578387, 'λ2048', 'T2^23' ],
  [ 5, 3768136, 'λ2048', 'T2^24' ],
  [ 6, 3230305, 'λ2048', 'T2^22' ],
  [ 6, 3436516, 'λ2048', 'T2^23' ],
  [ 6, 3626535, 'λ2048', 'T2^24' ],
  [ 7, 3152082, 'λ2048', 'T2^22' ],
  [ 7, 3356772, 'λ2048', 'T2^23' ],
  [ 7, 3549873, 'λ2048', 'T2^24' ],
  [ 8, 3200754, 'λ2048', 'T2^22' ],
  [ 8, 3407731, 'λ2048', 'T2^23' ],
  [ 8, 3603996, 'λ2048', 'T2^24' ],
  [ 9, 3523852, 'λ2048', 'T2^22' ],
  [ 9, 3736592, 'λ2048', 'T2^23' ],
  [ 9, 3939447, 'λ2048', 'T2^24' ],
  [ 10, 4483747, 'λ2048', 'T2^22' ],
  [ 10, 4710959, 'λ2048', 'T2^23' ],
  [ 10, 4927339, 'λ2048', 'T2^24' ],
  [ 11, 7091310, 'λ2048', 'T2^22' ],
  [ 11, 7348093, 'λ2048', 'T2^23' ],
  [ 11, 7592227, 'λ2048', 'T2^24' ],
  [ 12, 14520341, 'λ2048', 'T2^22' ],
  [ 12, 14839093, 'λ2048', 'T2^23' ],
  [ 12, 15141632, 'λ2048', 'T2^24' ]
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