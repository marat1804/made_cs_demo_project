import datetime


def now():
	print(f"Now - {datetime.datetime.now()}")


def tomorrow():
	print(f"{datetime.datetime.now() + datetime.timedelta(days=1)}")


if __name__ == '__main__':
	now()
	tomorrow()

