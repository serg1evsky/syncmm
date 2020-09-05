#   Written by Sergievsky&Finogenova
#   https://github.com/yepiwt
#   2020


from yandex_music import Client

#Удаление ненужной информации
import logging
logger = logging.getLogger('yandex_music')
logger.setLevel(logging.ERROR)

class smmyandex(object):

	__slots__ = ('client','albums','favs')

	def __init__(self,log,pas):
		client = captcha_key = captcha_answer = None
		while not client:
			try:
				client = Client.from_credentials(log,pas,captcha_answer,captcha_key)
			except Captcha as e:
				e.captcha.download('captcha.png')
				captcha_key = e.captcha.x_captcha_key
				captcha_answer = input('Число с картинки:')
		self.client = client

	def get(self):
		self.get_favs()
		self.get_albums()
		return True

	def get_favs(self):
		self.favs = []
		lib = self.client.users_likes_tracks()
		art = ''
		for obj in lib:
			artists = self.client.tracks(str(obj['id'])+':'+str(obj['album_id']))[0]['artists']
			group = self.client.tracks(str(obj['id'])+':'+str(obj['album_id']))[0]['title']
			for artist in artists:
				art += artist['name'] + ','
				art[:-2]
			self.favs.append([art, group])
			art = ''
		return self.favs

	def get_albums(self):
		self.albums = []
		songs = []
		lib = self.client.users_likes_albums()
		for album in lib:
			album_tracks = self.client.albumsWithTracks(album['album']['id'])
			for k in range(int(album_tracks['track_count'])):
				songs.append(album_tracks['volumes'][0][k]['title'])
			artist = album['album']['artists'][0]['name']
			title = album['album']['title']
			self.albums.append([artist,title,songs])
			songs = []
		return self.albums

if __name__ == "__main__":
	print('This is module smm-yandex. Smoke docs')
