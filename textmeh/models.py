from django.db import models

class UserLanguage(models.Model):
	user = models.ForeignKey('auth.User')
	language_code = models.CharField(max_length=2)
	language = models.CharField(max_length=50)

	def __str__(self):
		return str(self.language)

	def getLanguageName(code):
		return DICTIONARY[code]

	def getLanguageCode(name):
		return INV_DICTIONARY[name]

	def getLanguageList():
		return INV_DICTIONARY.keys()


class Chat(models.Model):
	sender = models.ForeignKey('auth.User')
	receiver = models.ForeignKey('auth.User', related_name='receiver_user')
	message = models.CharField(max_length=5000)
	translation = models.CharField(max_length=5000)
	time = models.DateTimeField()

	def __str__(self):
		return "Sender: " + str(self.sender) + " | Receiver: " + str(self.receiver) + " | Message: " + self.message

DICTIONARY = { 'af': 'Afrikaans',
'ar': 'Arabic',
'bs-Latn': 'Bosnian (Latin)',
'bg': 'Bulgarian',
'ca': 'Catalan',
'zh-CHS': 'Chinese Simplified',
'zh-CHT': 'Chinese Traditional',
'hr': 'Croatian',
'cs': 'Czech',
'da': 'Danish',
'nl': 'Dutch',
'en': 'English',
'et': 'Estonian',
'fi': 'Finnish',
'fr': 'French',
'de': 'German',
'el': 'Greek',
'ht': 'Haitian Creole',
'he': 'Hebrew',
'hi': 'Hindi',
'mww': 'Hmong Daw',
'hu': 'Hungarian',
'id': 'Indonesian',
'it': 'Italian',
'ja': 'Japanese',
'sw': 'Kiswahili',
'tlh': 'Klingon',
'tlh-Qaak': 'Klingon (pIqaD)',
'ko': 'Korean',
'lv': 'Latvian',
'lt': 'Lithuanian',
'ms': 'Malay',
'mt': 'Maltese',
'no': 'Norwegian',
'fa': 'Persian',
'pl': 'Polish',
'pt': 'Portuguese',
'otq': 'Querétaro Otomi',
'ro': 'Romanian',
'ru': 'Russian',
'sr-Cyrl': 'Serbian (Cyrillic)',
'sr-Latn': 'Serbian (Latin)',
'sk': 'Slovak',
'sl': 'Slovenian',
'es': 'Spanish',
'sv': 'Swedish',
'th': 'Thai',
'tr': 'Turkish',
'uk': 'Ukrainian',
'ur': 'Urdu',
'vi': 'Vietnamese',
'cy': 'Welsh',
'yua': 'Yucatec Maya' }

INV_DICTIONARY = {v: k for k, v in DICTIONARY.items()}