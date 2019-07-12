import os
from PIL import Image


os.system('adb shell screencap -p /sdcard/screen.png')
os.system('adb pull /sdcard/screen.png')
image = Image.open('screen.png').size
print(image)

# 下一步  (1500, 910)
# 闯关    (1440, 870)
# 跳过    (1840, 45)
# 自动    (1780, 43)
# 再次挑战       (1630, 1000)
# 可以持续点击的点  (1513, 1023)

