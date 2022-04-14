import pyautogui as pg
import time

answer = pg.prompt(text='请输入课程中的答案', title='答案', default='')
answers = answer.split(',')


def click(image_path, grayscale=True, sleep_time=3):
    point = pg.locateCenterOnScreen(image_path, grayscale=grayscale)
    pg.click(point.x, point.y)
    time.sleep(sleep_time)
    return point


pg.hotkey('ctrl', 'w')
head = pg.locateCenterOnScreen('image/head.png')
contact = pg.Point(x=head.x, y=(head.y+95))
pg.click(contact.x, contact.y)

pg.moveTo(x=(contact.x+150), y=contact.y)
for s in range(100):
    pg.scroll(10000)

click('image/official_accounts.png')
click('image/qcsh.png')
click('image/send_message.png')
click('image/qndxx.png', sleep_time=10)
me = click('image/me.png')

pg.moveTo(x=me.x, y=me.y-100)
for s in range(10):
    pg.scroll(-100)
time.sleep(3)

click('image/learning_task.png')

no_more = pg.locateCenterOnScreen('image/no_more.png', grayscale=True)
pg.click(no_more.x, no_more.y-50)
time.sleep(3)

click('image/tark_part_in.png', sleep_time=10)
click('image/learning.png', sleep_time=10)

welcome = pg.locateCenterOnScreen('image/welcome.png', grayscale=True)
if welcome:
    pg.click(welcome.x, welcome.y+30)
    time.sleep(3)

    click('image/city.png')

    pg.click(welcome.x, welcome.y+60)

    click('image/area.png')
    click('image/enter.png', sleep_time=10)

click('image/start.png')

while True:
    if pg.locateCenterOnScreen('image/enter_answer.png', grayscale=True):
        break
    time.sleep(60)

for answer in answers:
    for i in answer:
        click('image/%s.png' % i)
    click('image/enter_answer.png', sleep_time=10)

click('image/continue.png', sleep_time=10, grayscale=False)

while True:
    if pg.locateCenterOnScreen('image/end.png', grayscale=True):
        break
    time.sleep(60)

pg.hotkey('alt', 'f4')
