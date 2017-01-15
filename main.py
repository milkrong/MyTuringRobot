import json
import urllib2

class MyRobot():
    'my tu ling robot'
    def __init__(self, user_id):
        self.api_key = 'a1cd6f4ead7e4277aaed7e100a5a6b92'
        self.api_url = 'http://www.tuling123.com/openapi/api'
        self.input = ''
        self.answer = ''
        self.user_id = user_id

    def get_input(self):
        print "me:"
        self.input = raw_input()
        if self.input == ('q') :
            print '- Goodbye'
            return
        else:
            return self.input

    def send_input_get_answer(self):
        #make a data json
        info = self.get_input()
        data_send = {
            "key" : self.api_key,
            "info" : info,
            "userid" : self.user_id
        }
        #make a json post
        api_send = urllib2.Request(self.api_url)
        api_send.add_header('Content-Type', 'Application/json')
        response = urllib2.urlopen(api_send, json.dumps(data_send))
        self.answer = json.loads(response.read())

    def run(self):
        self.send_input_get_answer()
        print ("Milk:" + self.answer['text'])


if __name__ == '__main__':
    while True:
        robot = MyRobot(12345)
        robot.run()





