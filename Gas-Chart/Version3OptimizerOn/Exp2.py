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
# exp_by_square_iterative_gasestimate 1226396n
# exp_by_square_and_multiply_gasestimate 980023n
# precompileModExpGasEstimate 136827n
# x^( 2^4 )
# exp_by_square_iterative_gasestimate 2730094n
# exp_by_square_and_multiply_gasestimate 2145516n
# precompileModExpGasEstimate 241084n
# x^( 2^8 )
# exp_by_square_iterative_gasestimate 4571128n
# exp_by_square_and_multiply_gasestimate 3530228n
# precompileModExpGasEstimate 345504n
# x^( 2^16 )
# exp_by_square_iterative_gasestimate 6749650n
# exp_by_square_and_multiply_gasestimate 5135291n
# precompileModExpGasEstimate 449446n
# x^( 2^32 )
# exp_by_square_iterative_gasestimate 9265294n
# exp_by_square_and_multiply_gasestimate 6959573n
# precompileModExpGasEstimate 553389n
# x^( 2^64 )
# exp_by_square_iterative_gasestimate 12119852n
# exp_by_square_and_multiply_gasestimate 9004518n
# precompileModExpGasEstimate 658107n
# x^( 2^128 )
# exp_by_square_iterative_gasestimate 15315802n
# exp_by_square_and_multiply_gasestimate 11268411n
# precompileModExpGasEstimate 762162n
# x^( 2^256 )
# exp_by_square_iterative_gasestimate 18848994n
# exp_by_square_and_multiply_gasestimate 13752645n
# precompileModExpGasEstimate 866205n
# x^( 2^512 )
# exp_by_square_iterative_gasestimate 22719401n
# exp_by_square_and_multiply_gasestimate 16456097n
# precompileModExpGasEstimate 970236n
# x^( 2^1024 )
# exp_by_square_iterative_gasestimate 26927315n
# exp_by_square_and_multiply_gasestimate 19379901n
# precompileModExpGasEstimate 1075323n

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from matplotlib.ticker import FuncFormatter
x = ["$x^{2^{300}}$", "$x^{2^{600}}$", "$x^{2^{900}}$", "$x^{2^{1200}}$", "$x^{2^{1500}}$", "$x^{2^{1800}}$", "$x^{2^{2100}}$", "$x^{2^{2400}}$", "$x^{2^{2700}}$", "$x^{2^{3000}}$"]
expBySquareIterative = [1226396, 2730094, 4571128, 6749650, 9265294, 12119852, 15315802, 18848994, 22719401, 26927315]
expBySquareAndMultiply = [980023, 2145516, 3530228, 5135291, 6959573, 9004518, 11268411, 13752645, 16456097, 19379901]
precompileModExp = [136827, 241084, 345504, 449446, 553389, 658107, 762162, 866205, 970236, 1075323]
colors = ['#ff0000', '#008800', '#0000ff']
markers = ['o', '^', 's']  # circle, triangle, square

plt.plot(x, expBySquareIterative, color=colors[0], marker=markers[0], label="Baseline Model")
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
plt.savefig('1. modexp.png', dpi=500)
plt.show()