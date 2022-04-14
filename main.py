import pyautogui as pg
import time

answer=pg.prompt(text='请输入课程中的答案', title='答案' , default='')
answers=answer.split(',')
print(answers)


pg.hotkey('ctrl', 'w')
head = pg.locateCenterOnScreen('image/head.png')

contact = pg.Point(x=head.x, y=(head.y+95))
pg.click(contact.x, contact.y)

pg.moveTo(x=(contact.x+150), y=contact.y)
for s in range(100):
    pg.scroll(10000)

official_accounts = pg.locateCenterOnScreen('image/official_accounts.png',grayscale=True)
pg.click(official_accounts.x,official_accounts.y)

qcsh = pg.locateCenterOnScreen('image/qcsh.png',grayscale=True)
pg.click(qcsh.x,qcsh.y)
time.sleep(3)

send_message=pg.locateCenterOnScreen('image/send_message.png',grayscale=True)
pg.click(send_message.x,send_message.y)
time.sleep(3)

qndxx=pg.locateCenterOnScreen('image/qndxx.png',grayscale=True)
pg.click(qndxx.x,qndxx.y)
time.sleep(10)

me=pg.locateCenterOnScreen('image/me.png',grayscale=True)
pg.click(me.x,me.y)
time.sleep(3)

pg.moveTo(x=me.x, y=me.y-100)
for s in range(10):
    pg.scroll(-100)
time.sleep(3)

learning_task=pg.locateCenterOnScreen('image/learning_task.png',grayscale=True)
pg.click(learning_task.x,learning_task.y)
time.sleep(3)

no_more=pg.locateCenterOnScreen('image/no_more.png',grayscale=True)
pg.click(no_more.x,no_more.y-50)
time.sleep(3)

tark_part_in=pg.locateCenterOnScreen('image/tark_part_in.png',grayscale=True)
pg.click(tark_part_in.x,tark_part_in.y)
time.sleep(10)

learning=pg.locateCenterOnScreen('image/learning.png',grayscale=True)
pg.click(learning.x,learning.y)
time.sleep(10)

welcome = pg.locateCenterOnScreen('image/welcome.png',grayscale=True)
if welcome:
    pg.click(welcome.x,welcome.y+30)
    time.sleep(3)

    city = pg.locateCenterOnScreen('image/city.png',grayscale=True)
    pg.click(city.x,city.y)
    time.sleep(3)

    pg.click(welcome.x,welcome.y+60)

    area = pg.locateCenterOnScreen('image/area.png',grayscale=True)
    pg.click(area.x,area.y)
    time.sleep(3)

    enter = pg.locateCenterOnScreen('image/enter.png')
    pg.click(enter.x,enter.y)
    time.sleep(10)

start = pg.locateCenterOnScreen('image/start.png')
pg.click(start.x,start.y)

while True:
    if pg.locateCenterOnScreen('image/enter_answer.png',grayscale=True):
        break
    time.sleep(60)

for answer in answers:
    for i in answer:
        print(i)
        point=pg.locateCenterOnScreen('image/%s.png' % i,grayscale=True)
        pg.click(point.x,point.y)
    enter_answer=pg.locateCenterOnScreen('image/enter_answer.png',grayscale=True)
    pg.click(enter_answer.x,enter_answer.y)
    time.sleep(10)

continue_learning = pg.locateCenterOnScreen('image/continue.png')
pg.click(continue_learning.x,continue_learning.y)


while True:
    if pg.locateCenterOnScreen('image/end.png',grayscale=True):
        break
    time.sleep(60)

pg.hotkey('alt', 'f4')