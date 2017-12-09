import geoplotlib

class coordinates:
  def __init__(self, latitude, longitude):
    self.latitude = latitude
    self.longitude = longitude

  def __str__(self):
    return 'Latitude: {}, Longitude: {}'.format(self.latitude, self.longitude)

  def __add__(self, other):
    return 'Scalar: {} : {}'.format(self.latitude + other.latitude, self.longitude + other.longitude)

  def show_on_maps(self):
    data = {'lat':[self.latitude],'lon':[self.longitude]}
    geoplotlib.set_window_size(600, 600)
    geoplotlib.dot(data)
    geoplotlib.show()

geo_dot = coordinates(59.916270, 30.318245)
geo_dot_2 = coordinates(47.569773, -122.287456)

print(geo_dot.__add__(geo_dot_2))
geo_dot.show_on_maps()