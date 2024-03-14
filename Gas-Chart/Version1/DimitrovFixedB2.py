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

# x^( 2^400 )  y^(2)
# dimitrov estimateGasResult 1656460n
# precompile estimateGasResult 210963n
# x^( 2^800 )  y^(2)
# dimitrov estimateGasResult 3554545n
# precompile estimateGasResult 347911n
# x^( 2200 )  y^(2)
# dimitrov estimateGasResult 5820304n
# precompile estimateGasResult 485334n
# x^( 2600 )  y^(2)
# dimitrov estimateGasResult 8453679n
# precompile estimateGasResult 622035n
# x^( 2^2000 )  y^(2)
# dimitrov estimateGasResult 11454628n
# precompile estimateGasResult 758009n
# x^( 2^2400 )  y^(2)
# dimitrov estimateGasResult 14823922n
# precompile estimateGasResult 895242n
# x^( 2^2800 )  y^(2)
# dimitrov estimateGasResult 18560219n
# precompile estimateGasResult 1032168n

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

x = ["$x^{2^{400}}  y^{2}$", "$x^{2^{800}}  y^{2}$", "$x^{2^{1200}}  y^{2}$", "$x^{2^{1600}}  y^{2}$", "$x^{2^{2000}}  y^{2}$", "$x^{2^{2400}}  y^{2}$", "$x^{2^{2800}}  y^{2}$"]

dimitrov = [1656460, 3554545, 5820304, 8453679, 11454628, 14823922, 18560219]
precompile = [210963, 347911, 485334, 622035, 758009, 895242, 1032168]

colors = ['#ff0000','#0000ff']
markers = ['o', 's']

plt.plot(x, dimitrov, color=colors[0], marker=markers[0], label="Dimitrov")
plt.plot(x, precompile, color=colors[1], marker=markers[1], label="Precompile")

plt.legend(fontsize=13)
plt.xlabel('Multi Exponentiation', labelpad= 15 ,fontsize=13)
plt.ylabel('Gas Used ($10^7$)', labelpad= 15, fontsize=13)
plt.gca().yaxis.get_offset_text().set_visible(False)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# margin
plt.subplots_adjust(left=0.15)
plt.subplots_adjust(bottom=0.2)
plt.show()