
class SigChecker(object):

    def __init__(self, reader):
        self.pkt_reader = reader
        self.diseases_related_symptoms_pkt_size = [
            {'name': 'acute-kidney-failure', 'size': 889},
            {'name': 'abscess', 'size': 492}
        ]

    def generate_guess(self):
        """
        Generates a guess for the given FileReader object
        """
        for pkt in self.pkt_reader:
            if pkt.direction == 'received':
                if self.check_range(self.diseases_related_symptoms_pkt_size[0]['size'], 10, pkt.size):
                    return self.diseases_related_symptoms_pkt_size[0]['name']
                elif self.check_range(self.diseases_related_symptoms_pkt_size[1]['size'], 10, pkt.size):
                    return self.diseases_related_symptoms_pkt_size[1]['name']


    def check_range(self, num, width, guess):
        return (num - width) <= guess <= (num + width)
