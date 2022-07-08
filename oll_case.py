from random import randint


class OllCase:
  def __init__(self, code):
    self.code = code
  
  @classmethod
  def new_case(cls):
    return cls([0, 0, 0, 0, 0, 0, 0, 0, 0])

  @classmethod
  def random_case(cls):
    case = cls.new_case()
    n = randint(20, 30)
    for _ in range(0, n):
      case.flip_random_pair_of_edges()
      case.twist_random_trip_of_corners()
    return case

  @classmethod
  def is_equivalent(cls, case_a, case_b):
    rotation_b = case_b.copy()
    for _ in range(0, 4):
      rotation_b.rotate()
      if cls.is_exact(case_a, rotation_b):
        return True
    return False

  @classmethod
  def is_exact(cls, case_a, case_b):
    return case_a.code == case_b.code

  def copy(self):
    return OllCase(self.code.copy())

  def rotate(self):
    c = self.code
    new_code = [c[6], c[3], c[0], c[7], c[4], c[1], c[8], c[5], c[2]]
    self.code = new_code

  def flip_edge(self, edge_number):
    indices = (1, 3, 5, 7)
    index = indices[edge_number]
    self.code[index] = 1 - self.code[index]
    
  def flip_random_edge(self):
    edge_number = randint(0, 3)
    self.flip_edge(edge_number)

  def flip_random_pair_of_edges(self):
    self.flip_random_edge()
    self.flip_random_edge()

  def twist_corner(self, corner_number):
    indices = (0, 2, 6, 8)
    index = indices[corner_number]
    self.code[index] = (self.code[index] + 1) % 3

  def twist_random_corner(self):
    corner_number = randint(0, 3)
    self.twist_corner(corner_number)
  
  def twist_random_trip_of_corners(self):
    self.twist_random_corner()
    self.twist_random_corner()
    self.twist_random_corner()

  def __repr__(self) -> str:
    return str(self.code)