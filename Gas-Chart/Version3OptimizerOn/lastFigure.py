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
import numpy as np

# Data for baseline and optimized models
baseline = [
    [37.46773, 32.87890625, '$2^{20}$'],
    [39.38570, 34.44140625, '$2^{21}$'],
    [41.28530, 36.00390625, '$2^{22}$'],
    [43.35338, 37.56640625, '$2^{23}$'],
    [45.21524, 39.12890625, '$2^{24}$'],
    [47.36685, 40.69140625, '$2^{25}$']
]
optimized = [
    [19.70912, 5.84765625, '$2^{20}$'],
    [21.33110, 6.22265625, '$2^{21}$'],
    [22.96936, 6.59765625, '$2^{22}$'],
    [24.69646, 6.97265625, '$2^{23}$'],
    [26.24667, 7.34765625, '$2^{24}$'],
    [28.03507, 7.72265625, '$2^{25}$']
]

# Splitting the data into separate lists for plotting
baseline_gas, baseline_size, labels = zip(*baseline)
optimized_gas, optimized_size, labels = zip(*optimized)

## Let's fix the code to ensure both gas usage and tx size are displayed.
# We will plot gas usage on the left y-axis and tx size on the right y-axis.

# Define the width of the bars
bar_width = 0.2

# Set the positions of the bars and labels on the X axis
index = np.arange(len(labels))

# Create the figure and the two axes
fig, ax_gas = plt.subplots()

# Plotting the gas usage
bars_gas_baseline = ax_gas.bar(index - 1.5*bar_width, baseline_gas, bar_width, label='Baseline Gas Usage', color='black')
bars_gas_optimized = ax_gas.bar(index - 0.5*bar_width, optimized_gas, bar_width, label='Optimized Gas Usage', hatch='xx', color='silver', edgecolor='black')

# Set the labels, title, and custom x-axis tick labels, etc.
ax_gas.set_xlabel('Exponentiation (τ)')
ax_gas.set_ylabel('Gas Usage ($10^5$)', color='black')
#ax_gas.set_title('Comparison of Gas Usage and Proof Size Between Baseline and Optimized Models')
ax_gas.set_xticks(index)
ax_gas.set_xticklabels(labels)
ax_gas.tick_params(axis='y', labelcolor='black')

# Create another axes that shares the same x-axis for tx size
ax_size = ax_gas.twinx()


# Create line plots on top of the bars for tx size to make them visible
line_size_baseline = ax_size.bar(index + 0.5*bar_width, baseline_size, bar_width, label='Baseline Proof Size', color='gray')
line_size_optimized = ax_size.bar(index + 1.5*bar_width, optimized_size, bar_width, label='Optimized Proof Size', hatch='////', color='silver', edgecolor='black')

# Set the y-axis label for the proof size
ax_size.set_ylabel('Calldata Size (KB)', color='black')
ax_size.tick_params(axis='y', labelcolor='black')

# Combine legends from both axes
handles_gas, labels_gas = ax_gas.get_legend_handles_labels()
handles_size, labels_size = ax_size.get_legend_handles_labels()
ax_size.legend(handles_gas + handles_size, labels_gas + labels_size, loc='upper left')

fig.set_figwidth(10)
plt.tight_layout()
plt.savefig('figure.png', dpi=200)
plt.show()