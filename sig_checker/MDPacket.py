class MDPacket(object):
    def __init__(self, timestamp, direction, size, direction_count):
        """
        Timestamp is the timestamp of the reading,
        direction is sent or received,
        size is the est. sized of the pkt,
        direction_count provides a total ordering of packets going in self.direction
        """
        self.timestamp = timestamp
        self.direction = direction
        self.size = size
        self.direction_count = direction_count

    def __str__(self):
        return "TIME: %s, DIRECTION: %s, BYTES: %s, ORDER: %s" % (self.timestamp, self.direction, self.size, self.direction_count)
