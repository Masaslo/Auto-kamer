from pushbullet import Pushbullet
import time
class PushBulletController:
    def __init__(self):
        self.API_KEY = "o.otbOmfJ1shH9CPfjs3KbtneaoZcs5DQq"
        self.pb = Pushbullet(self.API_KEY)

    def send_notification(self, Class, data):
        self.pb.push_note(Class, data)

    def dismiss_push_from_index(self, index):
        pushes = pushBulletController.pb.get_pushes()
        pushBulletController.pb.dismiss_push(pushes[index].get("iden"))

    def get_push_from_index(self, index):
        pushes = pushBulletController.pb.get_pushes()
        return pushes[index]

    # def dismiss_push_from_id(self, title):
    #     pushes = pushBulletController.pb.get_pushes()


if __name__ == "__main__":
    pushBulletController = PushBulletController()
    pushBulletController.send_notification("testing", "DIT IS EEN TEST3 ")


