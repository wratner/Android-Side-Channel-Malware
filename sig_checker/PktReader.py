#!/usr/bin/env python

from MDPacket import MDPacket
import sys
from pprint import pprint
from collections import OrderedDict

class PktReader(object):

    def __init__(self, filename):
        self.total_pkts_sent = 0
        self.total_bytes_sent = 0
        self.total_pkts_received = 0
        self.total_bytes_received = 0
        self.input = open(filename, 'r')
        self.sent_count = 0
        self.rec_count = 0

        # initialize our packet counter using the first line in the packet file
        line = self.input.readline()
        timestamp, total_bytes_sent, total_bytes_received, total_pkts_sent, total_pkts_received = self.split_pkt(line)
        # Skip the first few packets if they're outliers
        while total_bytes_sent > 500000 or total_bytes_received > 500000:
            timestamp, total_bytes_sent, total_bytes_received, total_pkts_sent, total_pkts_received = self.split_pkt(self.input.readline())

        self.total_pkts_sent = total_pkts_sent
        self.total_bytes_sent = total_bytes_sent
        self.total_pkts_received = total_pkts_received
        self.total_bytes_received = total_bytes_received

    def __iter__(self):
        return self

    def next(self):
        return self.next_pkt()

    def split_pkt(self, line):
        """
        Returns the individual fields related to a packet from a line in the input file
        """
        pkt_data = line.split(';')
        timestamp = int(pkt_data[0])
        total_bytes_sent = int(pkt_data[1])
        total_bytes_received = int(pkt_data[2])
        total_pkts_sent = int(pkt_data[3])
        total_pkts_received = int(pkt_data[4].strip())
        return timestamp, total_bytes_sent, total_bytes_received, total_pkts_sent, total_pkts_received

    def next_pkt(self):
        line = self.input.readline()
        if line:
            timestamp, total_bytes_sent, total_bytes_received, total_pkts_sent, total_pkts_received = self.split_pkt(line)

            # Get the size of the packet (BYTES) (it may be sent or received - we have to compare the sizes to see)
            sent_size = total_bytes_sent - self.total_bytes_sent
            rec_size = total_bytes_received - self.total_bytes_received

            # Get the count of the packet (provide an ordering for sent and received packets)
            sent_diff = total_pkts_sent - self.total_pkts_sent
            rec_diff = total_pkts_received - self.total_pkts_received

            self.rec_count += rec_diff
            self.sent_count += sent_diff
            if rec_size > sent_size:
                # then this packet was one that was received
                pkt_kind = "received"
                pkt_size = rec_size
            else:
                # this packet was one that was sent
                pkt_kind = "sent"
                pkt_size = sent_size

            packet = MDPacket(timestamp, pkt_kind, pkt_size, self.sent_count)

            self.total_pkts_sent = total_pkts_sent
            self.total_bytes_sent = total_bytes_sent
            self.total_pkts_received = total_pkts_received
            self.total_bytes_received = total_bytes_received

            return packet
        else:
            raise StopIteration


def update_dict(the_set, the_dict):
    for item in the_set:
        if item in the_dict.keys():
            the_dict[item] += 1
        else:
            the_dict[item] = 1


def printDict(the_dict):
    order = OrderedDict(sorted(the_dict.items(), key=lambda t: t[1]))
    for k,v in order.iteritems():
        print "BYTES: %s in %s Files" % (k, v)


def recDiffs():
    print "===================================="
    print "REC DIFFS"
    print "===================================="

    total_abcess_rec_unique = dict()
    total_acute_rec_unique = dict()
    for i in range(1, 5):
        abcessReader = PktReader("testFiles/abcess%s.txt" % i)
        abcessPkts = []
        abcessRecSet = set()
        for pkt in abcessReader:
            abcessPkts.append(pkt)

        acuteReader = PktReader("testFiles/acute%s.txt" % i)
        acutePkts = []
        acuteRecSet = set()
        for pkt in acuteReader:
            acutePkts.append(pkt)

        for pkt in abcessPkts:
            if pkt.direction == 'received':
                abcessRecSet.add(pkt.size)

        for pkt in acutePkts:
            if pkt.direction == 'received':
                acuteRecSet.add(pkt.size)

        uniqueToAcute = acuteRecSet.difference(abcessRecSet)
        uniqueToAbscess = abcessRecSet.difference(acuteRecSet)
        update_dict(uniqueToAcute, total_acute_rec_unique)
        update_dict(uniqueToAbscess, total_abcess_rec_unique)

        # print "Unique to Acute: "
        # print uniqueToAcute
        # print "Unique to Abscess: "
        # print uniqueToAbscess
    print "=================================="
    print "Total Unique to Acute: "
    printDict(total_acute_rec_unique)
    print "=================================="
    print "Total Unique to Abscess: "
    printDict((total_abcess_rec_unique))


def sendDiffs():
    print "===================================="
    print "SEND DIFFS"
    print "===================================="

    total_abcess_rec_unique = dict()
    total_acute_rec_unique = dict()
    for i in range(1, 5):
        abcessReader = PktReader("testFiles/abcess%s.txt" % i)
        abcessPkts = []
        abcessRecSet = set()
        for pkt in abcessReader:
            abcessPkts.append(pkt)

        acuteReader = PktReader("testFiles/acute%s.txt" % i)
        acutePkts = []
        acuteRecSet = set()
        for pkt in acuteReader:
            acutePkts.append(pkt)

        for pkt in abcessPkts:
            if pkt.direction == 'sent':
                abcessRecSet.add(pkt.size)

        for pkt in acutePkts:
            if pkt.direction == 'sent':
                acuteRecSet.add(pkt.size)

        uniqueToAcute = acuteRecSet.difference(abcessRecSet)
        uniqueToAbscess = abcessRecSet.difference(acuteRecSet)
        update_dict(uniqueToAcute, total_acute_rec_unique)
        update_dict(uniqueToAbscess, total_abcess_rec_unique)

        # print "Unique to Acute: "
        # print uniqueToAcute
        # print "Unique to Abscess: "
        # print uniqueToAbscess
    print "=================================="
    print "Total Unique to Acute: "
    printDict(total_acute_rec_unique)
    print "=================================="
    print "Total Unique to Abscess: "
    printDict((total_abcess_rec_unique))


def sizeAdder(filename, direction, cutoff):
    reader = PktReader(filename)
    count = 0
    for pkt in reader:
        if pkt.direction == direction:
            if pkt.size < cutoff:
                count += pkt.size

    return count


def recAdder(filename):
    return sizeAdder(filename, "received", 3000)


def sentAdder(filename):
    return sizeAdder(filename, "sent", 3000)

if __name__ == '__main__':
    # abcessReader = PktReader(sys.argv[1])
    # abcessPkts = []
    # abcessRecSet = set()
    # for pkt in abcessReader:
    #     abcessPkts.append(pkt)
    #
    # acuteReader = PktReader(sys.argv[2])
    # acutePkts = []
    # acuteRecSet = set()
    # for pkt in acuteReader:
    #     acutePkts.append(pkt)
    #
    # for pkt in abcessPkts:
    #     if pkt.direction == 'sent':
    #         abcessRecSet.add(pkt.size)
    #
    # for pkt in acutePkts:
    #     if pkt.direction == 'sent':
    #         acuteRecSet.add(pkt.size)
    #
    # uniqueToAcute = acuteRecSet.difference(abcessRecSet)
    # uniqueToAbscess = abcessRecSet.difference(acuteRecSet)
    #
    # print "Unique to Acute: "
    # print uniqueToAcute
    # print "Unique to Abscess: "
    # print uniqueToAbscess
    #
    # print "REC ACUTE:"
    # b = list(acuteRecSet)
    # b.sort()
    # print b
    #
    # print "REC ABSCESS:"
    # a = list(abcessRecSet)
    # a.sort()
    # print a
    recDiffs()
    sendDiffs()

    print "==============================="
    print "ABCESS PACKETS:"
    for i in range(1, 5):
        filename = 'testFiles/abcess%s.txt' % i
        reader = PktReader(filename)
        for pkt in reader:
            print pkt
        print "TOTAL SENT %s" % (sentAdder(filename))
        print "TOTAL RECEIVED %s" % (recAdder(filename))
        print ""

    print "==============================="
    print "ACUTE PACKETS:"
    for i in range(1, 5):
        filename = 'testFiles/acute%s.txt' % i
        reader = PktReader(filename)
        for pkt in reader:
            print pkt
        print "TOTAL SENT %s" % (sentAdder(filename))
        print "TOTAL RECEIVED %s" % (recAdder(filename))
        print ""




