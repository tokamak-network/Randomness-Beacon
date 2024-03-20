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

# x^( 2^2 )
# exp_by_square_iterative_gasestimate 68598n
# exp_by_square_and_multiply_gasestimate 43084n
# precompileModExpGasEstimate 35023n
# x^( 2^4 )
# exp_by_square_iterative_gasestimate 75462n
# exp_by_square_and_multiply_gasestimate 49665n
# precompileModExpGasEstimate 35711n
# x^( 2^8 )
# exp_by_square_iterative_gasestimate 89532n
# exp_by_square_and_multiply_gasestimate 62855n
# precompileModExpGasEstimate 37087n
# x^( 2^16 )
# exp_by_square_iterative_gasestimate 117336n
# exp_by_square_and_multiply_gasestimate 89347n
# precompileModExpGasEstimate 39839n
# x^( 2^32 )
# exp_by_square_iterative_gasestimate 173593n
# exp_by_square_and_multiply_gasestimate 142774n
# precompileModExpGasEstimate 45343n
# x^( 2^64 )
# exp_by_square_iterative_gasestimate 288610n
# exp_by_square_and_multiply_gasestimate 251391n
# precompileModExpGasEstimate 56351n
# x^( 2^128 )
# exp_by_square_iterative_gasestimate 528584n
# exp_by_square_and_multiply_gasestimate 475681n
# precompileModExpGasEstimate 78063n
# x^( 2^256 )
# exp_by_square_iterative_gasestimate 1049846n
# exp_by_square_and_multiply_gasestimate 952660n
# precompileModExpGasEstimate 122537n
# x^( 2^512 )
# exp_by_square_iterative_gasestimate 2292591n
# exp_by_square_and_multiply_gasestimate 2019391n
# precompileModExpGasEstimate 211544n
# x^( 2^1024 )
# exp_by_square_iterative_gasestimate 5543589n
# exp_by_square_and_multiply_gasestimate 4604631n
# precompileModExpGasEstimate 389402n
# x^( 2^2048 )
# exp_by_square_iterative_gasestimate 15106065n
# exp_by_square_and_multiply_gasestimate 11582233n
# precompileModExpGasEstimate 745004n

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from matplotlib.ticker import FuncFormatter
x = ["$x^{2^2}$", "$x^{2^4}$", "$x^{2^8}$", "$x^{2^{16}}$", "$x^{2^{32}}$", "$x^{2^{64}}$", "$x^{2^{128}}$", "$x^{2^{256}}$", "$x^{2^{512}}$", "$x^{2^{1024}}$", "$x^{2^{2048}}$"]
expBySquareIterative = [68598, 75462, 89532, 117336, 173593, 288610, 528584, 1049846, 2292591, 5543589, 15106065]
expBySquareAndMultiply = [43084, 49665, 62855, 89347, 142774, 251391, 475681, 952660, 2019391, 4604631, 11582233]
precompileModExp = [35023, 35711, 37087, 39839, 45343, 56351, 78063, 122537, 211544, 389402, 745004]

colors = ['#ff0000', '#008800', '#0000ff']
markers = ['o', '^', 's']  # circle, triangle, square

plt.plot(x, expBySquareIterative, color=colors[0], marker=markers[0], label="Square Iterative")
plt.plot(x, expBySquareAndMultiply, color=colors[1], marker=markers[1], label="Square And Multiply")
plt.plot(x, precompileModExp, color=colors[2], marker=markers[2], label="Precompile ModExp")

plt.legend(fontsize=13)
plt.xlabel('Exponentiation', labelpad= 15, fontsize=13)
plt.ylabel('Gas Used ($10^6$)', labelpad= 15, fontsize=13)
plt.gca().yaxis.get_offset_text().set_visible(False)
def custom_formatter(x, pos):
    return '{:.0f}'.format(x * 1e-6)
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# margin
plt.subplots_adjust(left=0.17)
plt.subplots_adjust(bottom=0.2)
plt.grid(True, linestyle="--")
plt.savefig('2. modexp(log).png', dpi=500)
plt.show()