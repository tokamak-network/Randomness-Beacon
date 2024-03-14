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

# x^( 2^1 ) * y^( 2^1 )
# dimitrov estimateGasResult 105955n
# precompile estimateGasResult 76872n
# x^( 2^300 ) * y^( 2^300 )
# dimitrov estimateGasResult 1483360n
# precompile estimateGasResult 281609n
# x^( 2^600 ) * y^( 2^600 )
# dimitrov estimateGasResult 3093676n
# precompile estimateGasResult 485967n
# x^( 2^900 ) * y^( 2^900 )
# dimitrov estimateGasResult 4932718n
# precompile estimateGasResult 691292n
# x^( 2^1200 ) * y^( 2^1200 )
# dimitrov estimateGasResult 7000468n
# precompile estimateGasResult 896840n
# x^( 2^1500 ) * y^( 2^1500 )
# dimitrov estimateGasResult 9296968n
# precompile estimateGasResult 1101548n
# x^( 2^1800 ) * y^( 2^1800 )
# dimitrov estimateGasResult 11822795n
# precompile estimateGasResult 1307316n
# x^( 2^2100 ) * y^( 2^2100 )
# dimitrov estimateGasResult 14576813n
# precompile estimateGasResult 1512050n
# x^( 2^2400 ) * y^( 2^2400 )
# dimitrov estimateGasResult 17559539n
# precompile estimateGasResult 1717079n
# x^( 2^2700 ) * y^( 2^2700 )
# dimitrov estimateGasResult 20770980n
# precompile estimateGasResult 1922839n
# x^( 2^3000 ) * y^( 2^3000 )
# x^( 2^3000 ) * y^( 2^3000 )
# dimitrov estimateGasResult 24211139n
# precompile estimateGasResult 2127343n

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

x = ["$x^{2^1} * y^{2^1}$", "$x^{2^{300}} * y^{2^{300}}$", "$x^{2^{600}} * y^{2^{600}}$", "$x^{2^{900}} * y^{2^{900}}$", "$x^{2^{1200}} * y^{2^{1200}}$", "$x^{2^{1500}} * y^{2^{1500}}$", "$x^{2^{1800}} * y^{2^{1800}}$", "$x^{2^{2100}} * y^{2^{2100}}$", "$x^{2^{2400}} * y^{2^{2400}}$", "$x^{2^{2700}} * y^{2^{2700}}$", "$x^{2^{3000}} * y^{2^{3000}}$"]

dimitrov = [105955, 1483360, 3093676, 4932718, 7000468, 9296968, 11822795, 14576813, 17559539, 20770980, 24211139]
precompile = [76872, 281609, 485967, 691292, 896840, 1101548, 1307316, 1512050, 1717079, 1922839, 2127343]

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