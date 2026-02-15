# Create a class that will receive pieces of a file and tell whether the file can be assembled from the pieces.

# What does the packet contain to have the information ? Like how do we know the sequendce of packets to be constructed for a file ?
# So if I get a jumbled up packet
# simplest way would be to sort the packets and then see if the pcakets are correct - I can put it in a set and check the set
#

import heapq
import copy


class FileAssembler:
    def __init__(self, file_size: int):
        # initialize with the total size of the file
        self.file_size = file_size
        self.packets = []

    def add_piece(self, start: int, end: int):
        # add a piece of the file
        # piece covers indexes from start to end-1
        self.packets.append([start, end - 1])

    def is_complete(self) -> bool:
        # return True if the file can be fully assembled
        # False otherwise
        deepPackets = copy.deepcopy(self.packets)
        heapq.heapify(deepPackets)

        file = []

        while deepPackets:
            interval = heapq.heappop(deepPackets)

            if not file:
                file.append(interval)
            else:
                start, end = interval
                fStart, fEnd = file.pop()

                if fEnd + 1 >= start:
                    file.append([min(fStart, start, max(fEnd, end))])
                else:
                    break

        if file[0][1] - file[0][0] >= self.file_size:
            return True

        return False
