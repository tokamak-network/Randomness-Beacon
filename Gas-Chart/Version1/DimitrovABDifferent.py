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

# x^( 2^300 ) * y^( 2^1 )
# dimitrov estimateGasResult 1517379n
# precompile estimateGasResult 178651n
# x^( 2^600 ) * y^( 2^300 )
# dimitrov estimateGasResult 3134241n
# precompile estimateGasResult 384115n
# x^( 2^900 ) * y^( 2^600 )
# dimitrov estimateGasResult 4979723n
# precompile estimateGasResult 588672n
# x^( 2^1200 ) * y^( 2^900 )
# dimitrov estimateGasResult 7053996n
# precompile estimateGasResult 793631n
# x^( 2^1500 ) * y^( 2^1200 )
# dimitrov estimateGasResult 9357044n
# precompile estimateGasResult 999407n
# x^( 2^1800 ) * y^( 2^1500 )
# dimitrov estimateGasResult 11892318n
# precompile estimateGasResult 1204006n
# x^( 2^2100 ) * y^( 2^1800 )
# dimitrov estimateGasResult 14650470n
# precompile estimateGasResult 1409516n
# x^( 2^2400 ) * y^( 2^2100 )
# dimitrov estimateGasResult 17639964n
# precompile estimateGasResult 1614433n
# x^( 2^2700 ) * y^( 2^2400 )
# dimitrov estimateGasResult 20858221n
# precompile estimateGasResult 1819695n
# x^( 2^3000 ) * y^( 2^2700 )
# dimitrov estimateGasResult 24305268n
# precompile estimateGasResult 2025236n

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

x = ["$x^{2^{300}} * y^{2^1}$", "$x^{2^{600}} * y^{2^{300}}$", "$x^{2^{900}} * y^{2^{600}}$", "$x^{2^{1200}} * y^{2^{900}}$", "$x^{2^{1500}} * y^{2^{1200}}$", "$x^{2^{1800}} * y^{2^{1500}}$", "$x^{2^{2100}} * y^{2^{1800}}$", "$x^{2^{2400}} * y^{2^{2100}}$", "$x^{2^{2700}} * y^{2^{2400}}$", "$x^{2^{3000}} * y^{2^{2700}}$"]

dimitrov = [1517379, 3134241, 4979723, 7053996, 9357044, 11892318, 14650470, 17639964, 20858221, 24305268]
precompile = [178651, 384115, 588672, 793631, 999407, 1204006, 1409516, 1614433, 1819695, 2025236]

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