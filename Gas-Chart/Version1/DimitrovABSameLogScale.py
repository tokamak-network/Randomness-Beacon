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

# x^( 2^1 )  y^( 2^1 )
# dimitrov estimateGasResult 105955n
# precompile estimateGasResult 76872n
# x^( 2^2 )  y^( 2^2 )
# dimitrov estimateGasResult 110180n
# precompile estimateGasResult 78344n
# x^( 2^4 )  y^( 2^4 )
# dimitrov estimateGasResult 118643n
# precompile estimateGasResult 79493n
# x^( 2^8 )  y^( 2^8 )
# dimitrov estimateGasResult 135595n
# precompile estimateGasResult 81931n
# x^( 2^16 )  y^( 2^16 )
# dimitrov estimateGasResult 169624n
# precompile estimateGasResult 86562n
# x^( 2^32 )  y^( 2^32 )
# dimitrov estimateGasResult 238171n
# precompile estimateGasResult 98725n
# x^( 2^64 )  y^( 2^64 )
# dimitrov estimateGasResult 377215n
# precompile estimateGasResult 119691n
# x^( 2^128 )  y^( 2^128 )
# dimitrov estimateGasResult 663106n
# precompile estimateGasResult 164192n
# x^( 2^256 )  y^( 2^256 )
# dimitrov estimateGasResult 1266459n
# precompile estimateGasResult 251858n
# x^( 2^512 )  y^( 2^512 )
# dimitrov estimateGasResult 2597720n
# precompile estimateGasResult 425679n
# x^( 2^1024 )  y^( 2^1024 )
# dimitrov estimateGasResult 5759928n
# precompile estimateGasResult 775910n
# x^( 2^2048 )  y^( 2^2048 )
# dimitrov estimateGasResult 14083184n
# precompile estimateGasResult 1476808n

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

x = ["$x^{2}$$y^{2}$", "$x^{2^2}  y^{2^2}$", "$x^{2^4}  y^{2^4}$", "$x^{2^8}  y^{2^8}$", "$x^{2^{16}}  y^{2^{16}}$", "$x^{2^{32}}  y^{2^{32}}$", "$x^{2^{64}}  y^{2^{64}}$", "$x^{2^{128}}  y^{2^{128}}$", "$x^{2^{256}}  y^{2^{256}}$", "$x^{2^{512}}  y^{2^{512}}$", "$x^{2^{1024}}  y^{2^{1024}}$", "$x^{2^{2048}}  y^{2^{2048}}$"]

dimitrov = [105955, 110180, 118643, 135595, 169624, 238171, 377215, 663106, 1266459, 2597720, 5759928, 14083184]
precompile = [76872, 78344, 79493, 81931, 86562, 98725, 119691, 164192, 251858, 425679, 775910, 1476808]

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