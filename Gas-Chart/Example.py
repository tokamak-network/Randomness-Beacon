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

# Sample data (replace with your actual data)
T_values = [1, 2, 3, 4, 5]
gas_values = [[10, 15, 20, 25, 30],  # s0
              [12, 17, 22, 27, 32],  # s0+s1
              [14, 19, 24, 29, 34],  # s0+s1+s2
              [16, 21, 26, 31, 36],  # s0+s1+s2+s3
              [18, 23, 28, 33, 38],  # s0+s1+s2+s3+s4
              [20, 25, 30, 35, 40]]  # s0+s1+s2+s3+s4+s5

# Define lambda values for each strategy
lambda_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]  # example lambda values for each strategy

# Define colors for lambda values
lambda_colors = ['r', 'g', 'b', 'c', 'm', 'y']

# Plotting
for i in range(len(gas_values)):
    color = lambda_colors[i]
    for j in range(len(T_values) - 1):
        x1, x2 = T_values[j], T_values[j+1]
        y1, y2 = gas_values[i][j], gas_values[i][j+1]
        plt.plot([x1, x2], [y1, y2], color=color, linestyle='-', marker='o', markersize=5)

# Adding labels and legend
plt.xlabel('T')
plt.ylabel('gas')
plt.title('Gas Consumption for Different Strategies')

# Display the plot
plt.grid(True)
plt.show()