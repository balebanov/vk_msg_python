import vk_api, datetime, random

global randnum1
randnum1 = random.randrange(100,100000000) #ключ, чтобы не было одинаковых сообщений, и вк не банил

def send_mes():
	try:
		vk_session = vk_api.VkApi('login', 'password')
		vk_session.auth()
		vk = vk_session.get_api()
		vk.messages.send(user_id=128605250,random_id=randnum1,message='TEST main prog random')
		sys.exit()
	except:
		pass

def realtim():
	global realtime
	now = datetime.datetime.now()
	realtime = str(now.hour)+":"+str(now.minute)+":"+str(now.second)

while True:
	realtim()
	if realtime == '23:31:30': #время
		try:
			send_mes()
			break
		except:
			pass
	else:
		pass
