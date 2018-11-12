from copy import deepcopy
import numpy as np
import operator
def find_keys(dictionary, sep="~", k=[]):
    aux = {}
    keys = dictionary.keys()
    for key in keys:
        k.append(key)
        if isinstance(dictionary[key], dict):
            aux.update(find_keys(dictionary[key], "~", k))
        else:
            if sep.join(k) not in aux:
                aux.update({sep.join(k): deepcopy(k)})
        del k[-1]
    return (aux)


def pretty_numeric(x, dec=3):
    if isinstance(x, list):
        lst = x
    elif isinstance(x, float) or isinstance(x, int):
        lst = [x]
    else:
        lst = list(x)
    if len(lst) > 1:
        return [round(i, dec) if not np.isnan(i) and not np.isinf(i) else None for i in lst]
    elif len(lst) == 1:
        return round(lst[0], dec) if not np.isnan(lst[0]) and not np.isinf(lst[0]) else None
    else:
        None


def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)


def setInDict(dataDict, mapList, value):
    if isinstance(value,dict):
        getFromDict(dataDict, mapList[:-1])[mapList[-1]].update(value)
    else:
        getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value


def unique(seq, idfun=None):
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       if str(marker) in seen: continue
       seen[str(marker)] = 1
       result.append(item)
   return result

def ensure_list(obj):
    if isinstance(obj,list):
        return obj
    else:
        return [obj]


def set_dict_from_list(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value