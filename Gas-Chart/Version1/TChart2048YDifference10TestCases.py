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

dataOneT = [
  [ 3788252, 'λ2048', 'T2^20' ],
  [ 3789054, 'λ2048', 'T2^20' ],
  [ 3787319, 'λ2048', 'T2^20' ],
  [ 3780632, 'λ2048', 'T2^20' ],
  [ 3784345, 'λ2048', 'T2^20' ],
  [ 3787801, 'λ2048', 'T2^20' ],
  [ 3782021, 'λ2048', 'T2^20' ],
  [ 3787490, 'λ2048', 'T2^20' ],
  [ 3788698, 'λ2048', 'T2^20' ],
  [ 3801350, 'λ2048', 'T2^20' ],
  [ 3986631, 'λ2048', 'T2^21' ],
  [ 3990170, 'λ2048', 'T2^21' ],
  [ 4006341, 'λ2048', 'T2^21' ],
  [ 3991224, 'λ2048', 'T2^21' ],
  [ 3998147, 'λ2048', 'T2^21' ],
  [ 3990975, 'λ2048', 'T2^21' ],
  [ 3998807, 'λ2048', 'T2^21' ],
  [ 3981315, 'λ2048', 'T2^21' ],
  [ 3993595, 'λ2048', 'T2^21' ],
  [ 3976968, 'λ2048', 'T2^21' ],
  [ 4189498, 'λ2048', 'T2^22' ],
  [ 4182714, 'λ2048', 'T2^22' ],
  [ 4199992, 'λ2048', 'T2^22' ],
  [ 4192202, 'λ2048', 'T2^22' ],
  [ 4189041, 'λ2048', 'T2^22' ],
  [ 4193200, 'λ2048', 'T2^22' ],
  [ 4191750, 'λ2048', 'T2^22' ],
  [ 4189759, 'λ2048', 'T2^22' ],
  [ 4191299, 'λ2048', 'T2^22' ],
  [ 4184532, 'λ2048', 'T2^22' ],
  [ 4398999, 'λ2048', 'T2^23' ],
  [ 4399595, 'λ2048', 'T2^23' ],
  [ 4384392, 'λ2048', 'T2^23' ],
  [ 4393079, 'λ2048', 'T2^23' ],
  [ 4391225, 'λ2048', 'T2^23' ],
  [ 4400912, 'λ2048', 'T2^23' ],
  [ 4391690, 'λ2048', 'T2^23' ],
  [ 4404701, 'λ2048', 'T2^23' ],
  [ 4393701, 'λ2048', 'T2^23' ],
  [ 4388301, 'λ2048', 'T2^23' ],
  [ 4584429, 'λ2048', 'T2^24' ],
  [ 4586027, 'λ2048', 'T2^24' ],
  [ 4598287, 'λ2048', 'T2^24' ],
  [ 4606285, 'λ2048', 'T2^24' ],
  [ 4610835, 'λ2048', 'T2^24' ],
  [ 4580867, 'λ2048', 'T2^24' ],
  [ 4593114, 'λ2048', 'T2^24' ],
  [ 4592281, 'λ2048', 'T2^24' ],
  [ 4598470, 'λ2048', 'T2^24' ],
  [ 4603166, 'λ2048', 'T2^24' ],
  [ 4809455, 'λ2048', 'T2^25' ],
  [ 4797312, 'λ2048', 'T2^25' ],
  [ 4800873, 'λ2048', 'T2^25' ],
  [ 4803371, 'λ2048', 'T2^25' ],
  [ 4802379, 'λ2048', 'T2^25' ],
  [ 4803652, 'λ2048', 'T2^25' ],
  [ 4794267, 'λ2048', 'T2^25' ],
  [ 4787658, 'λ2048', 'T2^25' ],
  [ 4795554, 'λ2048', 'T2^25' ],
  [ 4815858, 'λ2048', 'T2^25' ]
]

dataTInProof = [
  [ 3794603, 'λ2048', 'T2^20' ],
  [ 3795406, 'λ2048', 'T2^20' ],
  [ 3793671, 'λ2048', 'T2^20' ],
  [ 3786982, 'λ2048', 'T2^20' ],
  [ 3790698, 'λ2048', 'T2^20' ],
  [ 3794155, 'λ2048', 'T2^20' ],
  [ 3788372, 'λ2048', 'T2^20' ],
  [ 3793838, 'λ2048', 'T2^20' ],
  [ 3795047, 'λ2048', 'T2^20' ],
  [ 3807707, 'λ2048', 'T2^20' ],
  [ 3993337, 'λ2048', 'T2^21' ],
  [ 3996877, 'λ2048', 'T2^21' ],
  [ 4013054, 'λ2048', 'T2^21' ],
  [ 3997932, 'λ2048', 'T2^21' ],
  [ 4004855, 'λ2048', 'T2^21' ],
  [ 3997683, 'λ2048', 'T2^21' ],
  [ 4005515, 'λ2048', 'T2^21' ],
  [ 3988019, 'λ2048', 'T2^21' ],
  [ 4000303, 'λ2048', 'T2^21' ],
  [ 3983674, 'λ2048', 'T2^21' ],
  [ 4196576, 'λ2048', 'T2^22' ],
  [ 4189791, 'λ2048', 'T2^22' ],
  [ 4207075, 'λ2048', 'T2^22' ],
  [ 4199282, 'λ2048', 'T2^22' ],
  [ 4196118, 'λ2048', 'T2^22' ],
  [ 4200281, 'λ2048', 'T2^22' ],
  [ 4198828, 'λ2048', 'T2^22' ],
  [ 4196842, 'λ2048', 'T2^22' ],
  [ 4198380, 'λ2048', 'T2^22' ],
  [ 4191607, 'λ2048', 'T2^22' ],
  [ 4406601, 'λ2048', 'T2^23' ],
  [ 4407196, 'λ2048', 'T2^23' ],
  [ 4391987, 'λ2048', 'T2^23' ],
  [ 4400679, 'λ2048', 'T2^23' ],
  [ 4398822, 'λ2048', 'T2^23' ],
  [ 4408512, 'λ2048', 'T2^23' ],
  [ 4399289, 'λ2048', 'T2^23' ],
  [ 4412300, 'λ2048', 'T2^23' ],
  [ 4401298, 'λ2048', 'T2^23' ],
  [ 4395899, 'λ2048', 'T2^23' ],
  [ 4592259, 'λ2048', 'T2^24' ],
  [ 4593859, 'λ2048', 'T2^24' ],
  [ 4606121, 'λ2048', 'T2^24' ],
  [ 4614122, 'λ2048', 'T2^24' ],
  [ 4618674, 'λ2048', 'T2^24' ],
  [ 4588699, 'λ2048', 'T2^24' ],
  [ 4600947, 'λ2048', 'T2^24' ],
  [ 4600111, 'λ2048', 'T2^24' ],
  [ 4606305, 'λ2048', 'T2^24' ],
  [ 4611002, 'λ2048', 'T2^24' ],
  [ 4817673, 'λ2048', 'T2^25' ],
  [ 4805526, 'λ2048', 'T2^25' ],
  [ 4809092, 'λ2048', 'T2^25' ],
  [ 4811593, 'λ2048', 'T2^25' ],
  [ 4810596, 'λ2048', 'T2^25' ],
  [ 4811874, 'λ2048', 'T2^25' ],
  [ 4802485, 'λ2048', 'T2^25' ],
  [ 4795873, 'λ2048', 'T2^25' ],
  [ 4803774, 'λ2048', 'T2^25' ],
  [ 4824082, 'λ2048', 'T2^25' ]
]

BitSize = [2048]
colors = ['#ff0000', '#0000ff']
markers = ['o', 's']  # circle, triangle, square
ts = ["$2^{20}$", "$2^{21}$", "$2^{22}$", "$2^{23}$", "$2^{24}$", "$2^{25}$"]
lineStyles = ['-', '--']

x = []
y = []

for i in range(0, len(dataOneT), 10):
    y_sum = 0
    print(i)
    for j in range(0,10):
        y_sum += dataTInProof[i+j][0] - dataOneT[i+j][0]
    x.append(ts[i//10])
    y.append(y_sum/10)

plt.plot(x, y, color=colors[0], marker=markers[0], linestyle=lineStyles[0])

plt.xlabel('T', labelpad= 15, fontsize=13)
plt.ylabel('Gas Difference', labelpad= 15, fontsize=13)
plt.legend(fontsize=12)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
# Adjust the bottom margin
plt.subplots_adjust(left=0.2)
plt.subplots_adjust(bottom=0.2)
plt.show()