from mycroft import MycroftSkill, intent_file_handler

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
        utterance = message.data.get('utterance')
        self.log.info(utterance)
        self.speak_dialog('is.who', {"status": utterance})

def create_skill():
    return WhoIs()

