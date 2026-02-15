from collections import Counter

class Packaging:
  def __init__(self, listOfItems):
    self.ITEM_BOX_CONFIG = {
        'Cam': [{"size": 'L', "count": 2}, {"size": 'M', "count": 1}],
        'Game': [{"size": 'L', "count": 2}, {"size": 'M', "count": 1}],
        'Blue': [{"size": 'L', "count": 1}]
      };
    
    self.frequency = {key: count for key, count in Counter(listOfItems).items()}
    # self.frequency = {"Cam": 5}

  def packageHelper(self, id, count):
    if count <= 0:
      return 0
    
    minPackage = float('inf')
    
    for packageSize in self.ITEM_BOX_CONFIG[id]:
      minPackage = min(minPackage, 1 + self.packageHelper(id, count-packageSize["count"]))

    return minPackage

  def package(self):
    res = []
    for id, count in self.frequency.items():
      res.append([self.packageHelper(id, count), id])

    print(res)
    return res


# result = Packaging(["Cam", "Cam", "Cam", "Game", "Game", "Cam", "Cam", "Blue", "Blue"])
# result.package()