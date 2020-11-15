class Storer:
    """
    Parent class
    """
    pass

class Keeper(Storer):

    """
    Keep data fresher longer.

    Extend `Storer`.  Class attribute `instances` keeps track
    of the number of `Keeper` objects instantiated.
    """

    instances = 0
    """How many `Keeper` objects are there?"""

    def __init__(self):
        """
        Extend `Storer.__init__()` to keep track of
        instances.  Keep count in `self.instances` and data
        in `self.data`.
        """
        Storer.__init__(self)
        self.instances += 1

        self.data = []
        """Store data in a list, most recent last."""
