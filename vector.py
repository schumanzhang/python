from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coordinates = [x+y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))
    
    def normalized(self):
        try:
            magnitude = Decimal(self.magnitude())
            return self.times_scalar(Decimal('1.0')/magnitude)

        except ZeroDivisionError:
            raise Exception('cannot normalize the zero vector')

    def dot(self, v):
        return sum([x*y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = acos(u1.dot(u2))

            if in_degrees:
                degrees_per_radian = 180/pi 
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with zero vector')
            else:
                raise e

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v):
        return(
            self.is_zero() or
            v.is_zero() or
            self.angle_with(v) == 0 or
            self.angle_with(v) == pi
        )

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def project_parallel(self, v):
        unit_vector = self.normalized()
        dot_product = sum([x*y for x, y in zip(unit_vector.coordinates, v.coordinates)])
        return Vector([dot_product*x for x in unit_vector.coordinates])

    def project_orthogonal(self, v):
        parrallel_vector = self.project_parallel(v)
        return Vector([x-y for x, y in zip(v.coordinates, parrallel_vector.coordinates)])

    def component_parallel_to(self, basis):
        try:
            u = basis.normalized()
            weight = self.dot(u)
            return u.times_scalar(weight)
        
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e

    def cross_product(self, v):
        first_position = self.coordinates[1] * v.coordinates[2] - v.coordinates[1] * self.coordinates[2]
        second_position = -1 * (self.coordinates[0] * v.coordinates[2] - v.coordinates[0] * self.coordinates[2])
        third_position = self.coordinates[0] * v.coordinates[1] - v.coordinates[0] * self.coordinates[1]
        return Vector([first_position, second_position, third_position])

    def area_of_parallelogram(self, v):
        new_vector = self.cross_product(v)
        coordinates_squared = [x**2 for x in new_vector.coordinates]
        return sqrt(sum(coordinates_squared))

    def area_of_triangle(self, v):
        new_vector = self.cross_product(v)
        coordinates_squared = [x**2 for x in new_vector.coordinates]
        return 1/2 * sqrt(sum(coordinates_squared))


v = Vector(['8.462', '7.893', '-8.187'])
w = Vector(['6.984', '-5.975', '4.778'])
#print(v.cross_product(w))


v = Vector(['-8.987', '-9.838', '5.031'])
w = Vector(['-4.268', '-1.861', '-8.866'])
#print(v.area_of_parallelogram(w))


v = Vector(['1.5', '9.547', '3.691'])
w = Vector(['-6.007', '0.124', '5.772'])
#print(v.area_of_triangle(w))



    