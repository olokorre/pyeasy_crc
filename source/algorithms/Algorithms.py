from source.algorithms.Algorithm import Algorithm
from source.algorithms.cdma2000 import CDMA2000
from source.algorithms.ebu import EBU
from source.algorithms.i_code import I_CODE
from source.algorithms.itu import ITU
from source.algorithms.maxim import MAXIM
from source.algorithms.rohc import ROHC
from source.types.AlgorithmKeys import AlgorithmKeys

algorithms: dict[AlgorithmKeys, Algorithm] = {
   'I-CODE': I_CODE,
   'ROHC': ROHC,
   'CDMA2000': CDMA2000,
   'EBU': EBU,
   'ITU': ITU,
   'MAXIM': MAXIM
}
