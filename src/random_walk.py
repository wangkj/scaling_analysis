import numpy as np

class RandomWalk(object):
    """
    We consider a random walk, say rw, a process governed by a random variable generated via rnd such that:
    rw[i+1] = rw[i] + rnd()

    r_walk = RandomWalk()
    [r_walk.walk() for i in range(0, np.power(2,8))] 

    """

    def __init__(self, random_generator=np.random.normal, initial_point=0):
        self.rnd_gen = random_generator
        self.path = [initial_point]

    def __repr__(self):
        return str(self.path)
    
    def _is_power_2(self, num):
        """
        Checks if a given number is a power of 2, being 0 excluded based on the fact that all power 2 numbers  having
        only one bit set to one and all other bits to zero, therefore number-1 makes it 0. The check is done via &
        bitwise operator
        """
        return (num & (num-1) == 0) and (num != 0)

    def _walk(self, path_length):
        """
        A generator version of the random walk values

        @raises ValueError: if path_length is not a power of 2
        """

        if not self._is_power_2(path_length):
            #TODO: Book keep constants
            raise ValueError('The path length is not a power of two') 

        pos = self.path[0]

        for _ in xrange(path_length):
            yield pos
            pos = pos + self.rnd_gen()

        
    def walk(self, path_length):
        """
        Returns a list with the values of the realization of the walk
        """
        self.path = list(self._walk(path_length))

    def scale(self, power):
        """
        Scales the values of the random walk
        """
        self.path = [np.power(step, power) for step in self.path]
        print self.path


if __name__ == '__main__':
    r_walk = RandomWalk()
    r_walk.walk(np.power(2,3))
    r_walk.scale(2)

    bulk_walks = [RandomWalk() for _ in xrange(3)]
    [random_walk.walk(np.power(2,3)) for random_walk in bulk_walks]
