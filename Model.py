class Word:
    
    def __init__(self):
        self.id=-1
        self.vocabulary =""
        self.means = ""
        self.image = ""
        self.level_box = 0
        self.part_of_speech = ""
        self.eg=""
        self.next = None    

    # def __init__(self, id, vocabulary, means, image, level_box, part_of_speech):
    #     self.id = id
    #     self.vocabulary = vocabulary
    #     self.means = means
    #     self.image = image
    #     self.level_box = level_box
    #     self.part_of_speech = part_of_speech
    #     self.next = None    

class Review:
    def __init__(self, id_word, status):
        self.id_word = id_word
        self.status =status
        self.next = None

         
