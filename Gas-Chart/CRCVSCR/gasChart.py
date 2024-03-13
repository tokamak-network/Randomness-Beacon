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
# commitLen, delta, gasUsedInitialize, gasUsedRequestRandomWord, gasUsedCommitSum, gasUsedRevealSum, gasUsedCalculateOmega, totalRevealCalculateUsed
CommitRevealCalculate = [
  [
          2,       8,
    2541515,  113828,
    1069787, 2105682,
    1980069, 4085751
  ],
  [
          2,       9,
    2460985,  113828,
    1069787, 2105682,
    1980069, 4085751
  ],
  [
          2,      10,
    2471392,  113828,
    1069787, 2105682,
    1980069, 4085751
  ],
  [
          3,       8,
    2541515,  113828,
    1626022, 3122969,
    2837841, 5960810
  ],
  [
          3,       9,
    2460985,  113828,
    1626022, 3122969,
    2837841, 5960810
  ],
  [
          3,      10,
    2471392,  113828,
    1626022, 3122969,
    2837841, 5960810
  ],
  [
          4,       8,
    2541515,  113828,
    2201147, 4137196,
    3695601, 7832797
  ],
  [
          4,       9,
    2460985,  113828,
    2201147, 4137196,
    3695601, 7832797
  ],
  [
          4,      10,
    2471392,  113828,
    2201147, 4137196,
    3695601, 7832797
  ],
  [
          5,       8,
    2541515,  113828,
    2795114, 5152787,
    4555761, 9708548
  ],
  [
          5,       9,
    2460985,  113828,
    2795114, 5152787,
    4555761, 9708548
  ],
  [
          5,      10,
    2471392,  113828,
    2795114, 5152787,
    4555761, 9708548
  ],
  [
          6,        8,
    2541515,   113828,
    3408055,  6171427,
    5416028, 11587455
  ],
  [
          6,        9,
    2460985,   113828,
    3408055,  6171427,
    5416028, 11587455
  ],
  [
          6,       10,
    2471392,   113828,
    3408055,  6171427,
    5416028, 11587455
  ],
  [
          7,        8,
    2541515,   113828,
    4039778,  7187288,
    6275964, 13463252
  ],
  [
          7,        9,
    2460985,   113828,
    4039778,  7187288,
    6275964, 13463252
  ],
  [
          7,       10,
    2471392,   113828,
    4039778,  7187288,
    6275964, 13463252
  ]
]
# commitLen, delta, gasUsedInitialize, gasUsedRequestRandomWord, gasUsedCommitSum, gasUsedRecover
CommitRecover = [
  [ 2, 8, 2541515, 113828, 1069787, 3158979 ],
  [ 2, 9, 2460985, 113828, 1069787, 3076871 ],
  [ 2, 10, 2471392, 113828, 1069787, 3086807 ],
  [ 3, 8, 2541515, 113828, 1626022, 3324857 ],
  [ 3, 9, 2460985, 113828, 1626022, 3244832 ],
  [ 3, 10, 2471392, 113828, 1626022, 3254846 ],
  [ 4, 8, 2541515, 113828, 2201147, 3494511 ],
  [ 4, 9, 2460985, 113828, 2201147, 3412866 ],
  [ 4, 10, 2471392, 113828, 2201147, 3423138 ],
  [ 5, 8, 2541515, 113828, 2795114, 3659843 ],
  [ 5, 9, 2460985, 113828, 2795114, 3576655 ],
  [ 5, 10, 2471392, 113828, 2795114, 3587245 ],
  [ 6, 8, 2541515, 113828, 3408055, 3827881 ],
  [ 6, 9, 2460985, 113828, 3408055, 3744619 ],
  [ 6, 10, 2471392, 113828, 3408055, 3754921 ],
  [ 7, 8, 2541515, 113828, 4039778, 3994753 ],
  [ 7, 9, 2460985, 113828, 4039778, 3910278 ],
  [ 7, 10, 2471392, 113828, 4039778, 3919549 ]
]

#compare totalRevealCalculateUsed and gasUsedRecover by drawing chart
#xticks : commitLen
#yticks : gasUsedRecover, totalRevealCalculateUsed
#three lines: delta(8,9,10)

colors = ['#ff0000', '#008800', '#0000ff']
markers = ['o', '^', 's']  # circle, triangle, square
lineStyles = ['-', '--']
xCommitRevealCalculate = [[],[],[]]
yCommitRevealCalculate = [[],[],[]]
xCommitRecover = [[],[],[]]
yCommitRecover = [[],[],[]]
for i in range(len(CommitRecover)):
    xCommitRevealCalculate[i%3].append(CommitRevealCalculate[i][0])
    yCommitRevealCalculate[i%3].append(CommitRevealCalculate[i][7])
    xCommitRecover[i%3].append(CommitRecover[i][0])
    yCommitRecover[i%3].append(CommitRecover[i][5])

for i in range(3):
    plt.plot(xCommitRevealCalculate[i], yCommitRevealCalculate[i], color=colors[i], marker=markers[i], label="delta="+str(i+8)+", CommitRevealCalculate", linestyle=lineStyles[0])
    plt.plot(xCommitRecover[i], yCommitRecover[i], color=colors[i], marker=markers[i], label="delta="+str(i+8)+", CommitRecover", linestyle=lineStyles[1])

plt.xlabel('Commit Num', labelpad= 15, fontsize = 13)
plt.ylabel('Gas Used', labelpad= 15, fontsize = 13)
plt.legend(title="delta", fontsize=12, title_fontsize=12)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
plt.subplots_adjust(left=0.15, bottom=0.2)
plt.show()