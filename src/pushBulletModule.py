from pushbullet import Pushbullet

class pushBulletController:
    def __init__(self):
        self.API_KEY = "o.otbOmfJ1shH9CPfjs3KbtneaoZcs5DQq"
        self.pb = Pushbullet(self.API_KEY)

    def sendNotification(self, Class, data):
        self.pb.push_note(Class, data)
    def mqttLostConnectionNotification(self, errorMessage):
        sendNotification("Auto Kamer Error", "MQTT Connection lost error message: \n" + errorMessage)

if __name__ == "__main__":
    pushBulletController = pushBulletController()
    pushBulletController.sendNotification("testing", "DIT IS EEN TEST")