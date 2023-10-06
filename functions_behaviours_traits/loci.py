

class Locus:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def add_x_value(self, x):
        self.x = x

    def add_y_value(self, y):
        self.y = y

    def add_z_value(self, z):
        self.z = z

    def add_xy_values(self, x, y):
        self.add_x_value(x)
        self.add_y_value(y)

    def add_yz_values(self, y, z):
        self.add_y_value(y)
        self.add_z_value(z)

    def add_xz_values(self, x, z):
        self.add_x_value(x)
        self.add_z_value(z)

    def add_xyz_values(self, x, y, z):
        self.add_x_value(x)
        self.add_y_value(y)
        self.add_z_value(z)

    def get_position(self):
        return self.x, self.y, self.z

