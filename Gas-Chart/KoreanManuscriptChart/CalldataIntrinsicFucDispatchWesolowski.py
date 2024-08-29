# Copyright 2024 justin
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter

#  calldataSizeInBytes, IntrinsicGas
data = [
    [ 8932, 128812 ],
    [ 9316, 133429 ],
    [ 9700, 138107 ],
    [ 10084, 142758 ],
    [ 10468, 147479 ],
    [ 10852, 152070 ]
]

labels = ['calldata size (Bytes)', 'Intrinsic Gas']
colors = ['tab:red','tab:blue']
markers = ['o', '^', 's']  # circle, triangle, square
ts = ["$2^{20}$", "$2^{21}$", "$2^{22}$", "$2^{23}$", "$2^{24}$", "$2^{25}$"]
lineStyles = ['-', '--']

x = ts
y1 = [data[i][0] for i in range(0,6)]
y2 = [data[i][1] for i in range(0,6)]


#Define the width of the bars
bar_width = 0.2

# Set the positions of the bars and labels on the X axis
index = np.arange(len(labels))

# Create the figure and the two axes
fig, ax_gas = plt.subplots()

ax_gas.bar(index - 1.5*bar_width, y1, bar_width, label='Calldata Size (Bytes)', color=colors[0])
ax_gas.bar(index - 0.5*bar_width, y2, bar_width, label='Intrinsic Gas', hatch='xx', color=colors[1], edgecolor='black')

# Set the labels, title, and custom x-axis tick labels, etc.
ax_gas.set_xlabel('Exponentiation (τ)')



# fig, ax1 = plt.subplots()
# ax1.bar(x, y1, color=colors[0], label=labels[0])

# ax2 = ax1.twinx()
# ax2.bar(x, y2, color=colors[1], label=labels[1])


plt.show()