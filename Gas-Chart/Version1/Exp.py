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

# x^( 2^1 )
# exp_by_square_iterative_gasestimate 65338n
# exp_by_square_and_multiply_gasestimate 39797n
# precompileModExpGasEstimate 34679n
# x^( 2^10 )
# exp_by_square_iterative_gasestimate 96263n
# exp_by_square_and_multiply_gasestimate 69467n
# precompileModExpGasEstimate 37775n
# x^( 2^100 )
# exp_by_square_iterative_gasestimate 421845n
# exp_by_square_and_multiply_gasestimate 376398n
# precompileModExpGasEstimate 68469n
# x^( 2^1000 )
# exp_by_square_iterative_gasestimate 5369851n
# exp_by_square_and_multiply_gasestimate 4469784n
# precompileModExpGasEstimate 380955n

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

x = ["$x^{2^1}$", "$x^{2^{10}}$", "$x^{2^{100}}$", "$x^{2^{1000}}$"]
expBySquareIterative = [65338, 96263, 421845, 5369851]
expBySquareAndMultiply = [39797, 69467, 376398, 4469784]
precompileModExp = [34679, 37775, 68469, 380955]
colors = ['#ff0000', '#008800', '#0000ff']
markers = ['o', '^', 's']  # circle, triangle, square

plt.plot(x, expBySquareIterative, color=colors[0], marker=markers[0], label="Square Iterative")
plt.plot(x, expBySquareAndMultiply, color=colors[1], marker=markers[1], label="Square And Multiply")
plt.plot(x, precompileModExp, color=colors[2], marker=markers[2], label="Precompile ModExp")

plt.legend()
plt.xlabel('Exponentiation', labelpad= 15)
plt.ylabel('Gas Used', labelpad= 15)

# margin
plt.subplots_adjust(left=0.15)
plt.subplots_adjust(bottom=0.15)
plt.show()