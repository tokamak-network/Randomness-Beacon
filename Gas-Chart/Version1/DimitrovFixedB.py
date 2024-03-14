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

# x^( 2^1 ) * y^(2^1)
# dimitrov estimateGasResult 102587n
# precompile estimateGasResult 75242n
# x^( 2^300 ) * y^(2^1)
# dimitrov estimateGasResult 1239443n
# precompile estimateGasResult 177021n
# x^( 2^600 ) * y^(2^1)
# dimitrov estimateGasResult 2559385n
# precompile estimateGasResult 279400n
# x^( 2^900 ) * y^(2^1)
# dimitrov estimateGasResult 4086815n
# precompile estimateGasResult 382029n
# x^( 2^1200 ) * y^(2^1)
# dimitrov estimateGasResult 5820304n
# precompile estimateGasResult 485334n
# x^( 2^1500 ) * y^(2^1)
# dimitrov estimateGasResult 7760682n
# precompile estimateGasResult 587045n
# x^( 2^1800 ) * y^(2^1)
# dimitrov estimateGasResult 9908788n
# precompile estimateGasResult 689640n
# x^( 2^2100 ) * y^(2^1)
# dimitrov estimateGasResult 12262745n
# precompile estimateGasResult 792881n
# x^( 2^2400 ) * y^(2^1)
# dimitrov estimateGasResult 14823922n
# precompile estimateGasResult 895242n
# x^( 2^2700 ) * y^(2^1)
# dimitrov estimateGasResult 17591537n
# precompile estimateGasResult 997423n
# x^( 2^3000 ) * y^(2^1)
# dimitrov estimateGasResult 20566346n
# precompile estimateGasResult 1099790n

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

x = ["$x^{2^1} * y^{2^1}$", "$x^{2^{300}} * y^{2^1}$", "$x^{2^{600}} * y^{2^1}$", "$x^{2^{900}} * y^{2^1}$", "$x^{2^{1200}} * y^{2^1}$", "$x^{2^{1500}} * y^{2^1}$", "$x^{2^{1800}} * y^{2^1}$", "$x^{2^{2100}} * y^{2^1}$", "$x^{2^{2400}} * y^{2^1}$", "$x^{2^{2700}} * y^{2^1}$", "$x^{2^{3000}} * y^{2^1}$"]

dimitrov = [102587, 1239443, 2559385, 4086815, 5820304, 7760682, 9908788, 12262745, 14823922, 17591537, 20566346]
precompile = [75242, 177021, 279400, 382029, 485334, 587045, 689640, 792881, 895242, 997423, 1099790]

colors = ['#ff0000','#0000ff']
markers = ['o', 's']

plt.plot(x, dimitrov, color=colors[0], marker=markers[0], label="Dimitrov")
plt.plot(x, precompile, color=colors[1], marker=markers[1], label="Precompile")

plt.legend()
plt.xlabel('Multi Exponentiation', labelpad= 15)
plt.ylabel('Gas Used', labelpad= 15)
# margin
plt.subplots_adjust(left=0.15)
plt.subplots_adjust(bottom=0.15)
plt.show()