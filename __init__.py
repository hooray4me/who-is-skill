from mycroft import MycroftSkill, intent_file_handler

WORDS = {
    'steve': ('steve'),
    'darren dean': ('darren'),
    'darren deen': ('darren'),
    'darin deen': ('darren'),
    'rob hedrick': ('rob'),
    'rob headrick': ('rob'),
    'rob head rick': ('rob')
}
def words_in_utt(utterance):
    utterance = utterance.lower()
    for key in WORDS:
        if key in utterance:
            return key
    return None

class WhoIs(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('is.who.intent')
    def handle_is_who(self, message):
        utt = message.data.get('utterance')
        t = words_in_utt(utt)
        self.log.info(t)
        self.speak_dialog('is.who', {"status": t})

def create_skill():
    return WhoIs()

