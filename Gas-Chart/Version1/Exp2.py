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

# x^( 2^300 )
# exp_by_square_iterative_gasestimate 1247890n
# exp_by_square_and_multiply_gasestimate 1125261n
# precompileModExpGasEstimate 137674n
# x^( 2^600 )
# exp_by_square_iterative_gasestimate 2783103n
# exp_by_square_and_multiply_gasestimate 2420795n
# precompileModExpGasEstimate 241934n
# x^( 2^900 )
# exp_by_square_iterative_gasestimate 4667388n
# exp_by_square_and_multiply_gasestimate 3923129n
# precompileModExpGasEstimate 345688n
# x^( 2^1200 )
# exp_by_square_iterative_gasestimate 6900928n
# exp_by_square_and_multiply_gasestimate 5632258n
# precompileModExpGasEstimate 450299n
# x^( 2^1500 )
# exp_by_square_iterative_gasestimate 9483084n
# exp_by_square_and_multiply_gasestimate 7548188n
# precompileModExpGasEstimate 554240n
# x^( 2^1800 )
# exp_by_square_iterative_gasestimate 12416276n
# exp_by_square_and_multiply_gasestimate 9671217n
# precompileModExpGasEstimate 658325n
# x^( 2^2100 )
# exp_by_square_iterative_gasestimate 15703848n
# exp_by_square_and_multiply_gasestimate 12000782n
# precompileModExpGasEstimate 763014n
# x^( 2^2400 )
# exp_by_square_iterative_gasestimate 19340227n
# exp_by_square_and_multiply_gasestimate 14537130n
# precompileModExpGasEstimate 867057n
# x^( 2^2700 )
# exp_by_square_iterative_gasestimate 23325466n
# exp_by_square_and_multiply_gasestimate 17280279n
# precompileModExpGasEstimate 971088n
# x^( 2^3000 )
# exp_by_square_iterative_gasestimate 27659939n
# exp_by_square_and_multiply_gasestimate 20230221n
# precompileModExpGasEstimate 1076176n

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
x = ["$x^{2^{300}}$", "$x^{2^{600}}$", "$x^{2^{900}}$", "$x^{2^{1200}}$", "$x^{2^{1500}}$", "$x^{2^{1800}}$", "$x^{2^{2100}}$", "$x^{2^{2400}}$", "$x^{2^{2700}}$", "$x^{2^{3000}}$"]
expBySquareIterative = [1247890, 2783103, 4667388, 6900928, 9483084, 12416276, 15703848, 19340227, 23325466, 27659939]
expBySquareAndMultiply = [1125261, 2420795, 3923129, 5632258, 7548188, 9671217, 12000782, 14537130, 17280279, 20230221]
precompileModExp = [137674, 241934, 345688, 450299, 554240, 658325, 763014, 867057, 971088, 1076176]
colors = ['#ff0000', '#008800', '#0000ff']
markers = ['o', '^', 's']  # circle, triangle, square

plt.plot(x, expBySquareIterative, color=colors[0], marker=markers[0], label="Square Iterative")
plt.plot(x, expBySquareAndMultiply, color=colors[1], marker=markers[1], label="Square And Multiply")
plt.plot(x, precompileModExp, color=colors[2], marker=markers[2], label="Precompile ModExp")

plt.legend(fontsize=13)
plt.xlabel('Exponentiation', labelpad= 15, fontsize=13)
plt.ylabel('Gas Used ($10^7$)', labelpad= 15, fontsize=13)
plt.gca().yaxis.get_offset_text().set_visible(False)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# margin
plt.subplots_adjust(left=0.15)
plt.subplots_adjust(bottom=0.2)
plt.show()