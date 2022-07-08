import py_compile
from PIL import Image, ImageDraw
from oll_case import OllCase

class Fragment:
  def __init__(self, shape, color):
    self.shape = shape
    self.color = color
  
def _get_square_shape(center, size):
  return [(center[0] - size/2, center[1] - size/2), (center[0] + size/2, center[1] + size/2)]

def _get_side_shape(center, width, height):
  return [(center[0] - width/2, center[1] - height/2), (center[0] + width/2, center[1] + height/2)]

def _get_grid(case, center, size):
  fragment = []
  yellow = "#ffff33"
  gray = "#333333"
  thickness = size / 3
  side_off = (size + thickness) / 2
  for j in range(-1, 2):
    for i in range(-1, 2):  
      piece_index = ((j + 1) * 3) + (i + 1)
      code = case.code[piece_index]
      color = yellow if code == 0 else gray
      sub_center = (center[0] + i*size, center[1] + j*size)
      f0 = Fragment(_get_square_shape(sub_center, size), color)
      fragment.append(f0)
      if i == -1:
        sideColor = yellow if piece_index == 0 and code == 1 or piece_index == 3 and code == 1 or piece_index == 6 and code == 2 else gray
        f1 = Fragment(_get_side_shape((sub_center[0] - side_off, sub_center[1]), thickness, size), sideColor)
        fragment.append(f1)
      if i == 1:
        sideColor = yellow if piece_index == 2 and code == 2 or piece_index == 5 and code == 1 or piece_index == 8 and code == 1 else gray
        f1 = Fragment(_get_side_shape((sub_center[0] + side_off, sub_center[1]), thickness, size), sideColor)
        fragment.append(f1)
      if j == -1:
        sideColor = yellow if piece_index == 0 and code == 2 or piece_index == 1 and code == 1 or piece_index == 2 and code == 1 else gray
        f1 = Fragment(_get_side_shape((sub_center[0], sub_center[1] - side_off), size, thickness), sideColor)
        fragment.append(f1)
      if j == 1:
        sideColor = yellow if piece_index == 6 and code == 1 or piece_index == 7 and code == 1 or piece_index == 8 and code == 2 else gray
        f1 = Fragment(_get_side_shape((sub_center[0], sub_center[1] + side_off), size, thickness), sideColor)
        fragment.append(f1)
      
  return fragment

def save_case(case, text, path, file_name):
  w, h = 400, 400
  center = (w/2, h/2)
  cube_size = 40
  fragments = _get_grid(case, center, cube_size)

  img = Image.new("RGB", (w, h))
  img1 = ImageDraw.Draw(img)  
  for fragment in fragments:
    img1.rectangle(fragment.shape, fill=fragment.color, outline ="black", width=4)
  img1.text((40, h-40), text, "#ffffff")
  img.save(path + "/" + file_name + ".jpg", "JPEG")