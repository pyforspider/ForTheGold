import time
import os


# 模拟点击
def click(x, y):
	os.system('adb shell input tap {} {}'.format(x, y))


def run(count):
	# 点击下一步
	click(1500, 910)
	time.sleep(1)

	# 闯关加载
	click(1440, 870)
	print('画面加载中...')
	time.sleep(10)

	# 不停点击
	print('英雄玩命打钱中...')
	while count:
		click(1630, 1000)  # 持续点击 <再次挑战>
		time.sleep(1)

		click(1440, 870)  # 持续点击 <闯关>
		time.sleep(1)

		count -= 1


if __name__ == '__main__':
	# 一次循环2秒，设置脚本持续时间3h
	run(3*1800)
