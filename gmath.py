import math
from display import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

# lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
  amb = calculate_ambient(ambient, areflect)
  diff = calculate_diffuse(light, dreflect, normal)
  spec = calculate_specular(light, sreflect, view, normal)
  color = []
  
  for i in range(0, 3):
    color.append(amb[i] + diff[i] + spec[i])
  print color
  
  return limit_color(color)


def calculate_ambient(alight, areflect):
  aLight = []
  for i in range(0, 3):
    aLight.append(alight[i] * areflect[i])
  return limit_color(aLight)


def calculate_diffuse(light, dreflect, normal):
  dflect = []
  for i in range(0, 3):
    dflect.append(light[COLOR][i] * dreflect[i] * dot_product(normalize(normal), normalize(light[LOCATION])))
  return limit_color(dflect)


def calculate_specular(light, sreflect, view, normal):
  n = normalize(normal)
  l = normalize(light[LOCATION])
  v = normalize(view)
  
  p = []
  s = []
  NdotL = 2 * dot_product(n, l)
    
  for i in range(0, 3):
    p.append(NdotL * n[i] - l[i])
  cos = dot_product(p, v)
    
  for i in range(0, 3):
    s.append(light[COLOR][i] * sreflect[i] * (cos ** SPECULAR_EXP))
  return limit_color(s)


def limit_color(color):
  for i in range(0, 3):
    n = int(color[i])
    if (n < 0):
      n = 0
    elif (n > 255):
      n = 255
    color[i] = n
  return color

#vector functions
def normalize(vector):
  a = float(vector[0])
  b = float(vector[1])
  c = float(vector[2])
  c = math.sqrt(a*a + b*b + c*c)
  
  r = [0,0,0]
  r[0] = vector[0]/c
  r[1] = vector[1]/c
  r[2] = vector[2]/c
  
  return r

def dot_product(a, b):
   return a[0] * b[0] + a[1]*b[1] + a[2]*b[2]

def calculate_normal(polygons, i):
  A = [0, 0, 0]
  B = [0, 0, 0]
  N = [0, 0, 0]

  A[0] = polygons[i+1][0] - polygons[i][0]
  A[1] = polygons[i+1][1] - polygons[i][1]
  A[2] = polygons[i+1][2] - polygons[i][2]

  B[0] = polygons[i+2][0] - polygons[i][0]
  B[1] = polygons[i+2][1] - polygons[i][1]
  B[2] = polygons[i+2][2] - polygons[i][2]

  N[0] = A[1] * B[2] - A[2] * B[1]
  N[1] = A[2] * B[0] - A[0] * B[2]
  N[2] = A[0] * B[1] - A[1] * B[0]

  return N
