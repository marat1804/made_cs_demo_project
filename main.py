import datetime


def now():
	print(f"Now - {datetime.datetime.now()}")


def pre_yesterday():
	print(f"Yesterday - {datetime.datetime.now() - datetime.timedelta(days=2)}")



def tomorrow():
	print(f"Tomorrow - {datetime.datetime.now() + datetime.timedelta(days=1)}")


if __name__ == '__main__':
	now()
	tomorrow()

