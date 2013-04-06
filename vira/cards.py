# Cards file for V.I.R.A.

import json
import os
import requests
from wordnik import *

card_map = {
                'word'             : 'word',
                'define'           : 'define_word',
                'definition'       : 'define_word',
                'urban dictionary' : 'urban_dict',
                'urban'            : 'urban_dict',
                'book'             : 'book',
                'isbn'             : 'book',
                'vira'  	   	   : 'vira',
                'hash'		   	   : 'hash_str',
                'palindrome'       : 'is_palindrome',
                'weather'          : 'weather'
             }
             
def wolfram_alpha(options, inputx):
    
    api_key = os.environ.get('WOLFRAM_KEY')
    
    if api_key is None:
        
        raise Exception('Wolfram Alpha API Key not defined.')
    
    client = wolframalpha.Client(api_key)
    
    res = client.query(inputx)
        
    return res.pods[1].text


def weather(options, inputx):
            
    if not inputx.isdigit() and len(inputx) != 5:
        
        raise Exception("Invalid zip code.")
        
    api_key = os.environ.get('WUNDERGROUND_KEY')
    
    if api_key is None:
        
        raise Exception('Wunderground API Key not defined.')
                    
    data = requests.get('http://api.wunderground.com/api/%s/forecast/geolookup/conditions/q/%s.json' %
                        (api_key, inputx)).json()['current_observation']

    return [('Location: %s') % (inputx),
            ('Condition: %s') % (data['weather']),
            ('Temperature: %s') % (data['temperature_string']),
            ('Feels Like: %s') % (data['feelslike_string']),
            ('Wind: %s') % (data['wind_string']),
            ('Humidity: %s') % (data['relative humidity'])]


def is_palindrome(options, inputx):
    
    inputx = inputx.lower()
    
    if len(inputx) < 1:
        
        return 'That is a valid palindrome.'
        
    else:
        
        if inputx[0] == inputx[-1]:
            
            return is_palindrome(options, inputx[1:-1])
            
        else:
            
            return 'No siree! That is not a palindrome.'


def hash_str(options, inputx):

    import hashlib

    if options == 'md5':

        return hashlib.md5(inputx).hexdigest()

    elif options == 'sha1':
		
        return hashlib.sha1(inputx).hexdigest()
		
    elif options == 'sha224':
		
        return hashlib.sha224(inputx).hexdigest()
		
    elif options == 'sha256':
		
        return hashlib.sha256(inputx).hexdigest()
		
    elif options == 'sha384':
		
        return hashlib.sha384(inputx).hexdigest()
	
    elif options == 'sha512':
		
        return hashlib.sha512(inputx).hexdigest()

    else:
		
        raise Exception('Hash format (md5, sha1, sha224, sha256, sha384, sha512) is invalid.')


def vira(options, inputx):
   
    if options == 'authors':
    
        return 'Mihir Singh and David Goldman.'

    elif options == 'name':

        return 'V.I.R.A.'

    elif options == 'purpose':

        return 'To serve, educate, and advise.'

    else:

        raise Exception('Invalid option.')

def book(options, inputx):

    r = json.loads(requests.get('https://www.googleapis.com/books/v1/volumes?country=US&q=ISBN:%s' % (inputx)).text)

    return ['Title: %s' % (r['items'][0]['volumeInfo']['title']),
            'Author(s): %s' % (', '.join(r['items'][0]['volumeInfo']['authors'])),
            'Published: %s' % (r['items'][0]['volumeInfo']['publishedDate']),
            'Description: %s' % (r['items'][0]['volumeInfo']['description'])]

def define_word(options, inputx):

    apiUrl = 'http://api.wordnik.com/v4'
    apiKey = os.environ.get('WORDNIK_KEY')
    
    if apiKey is None:
      
	    raise Exception('Wordnik API Key not defined.')
    
    client = swagger.ApiClient(apiKey, apiUrl)
    
    wordApi = WordApi.WordApi(client)

    definitions = wordApi.getDefinitions(inputx, limit=1)
    
    if definitions == None:
      
		return 'No definitions found.'
    
    else:
      
		return definitions[0].text


def urban_dict(options, inputx):

    if options is None:

        options = 1

    r = json.loads(requests.get('http://api.urbandictionary.com/v0/define?term=%s' % (inputx)).text)

    if options == '#':

        return 'There are %s definitions for %s on Urban Dictionay.' % (len(r['list']), inputx)

    elif options.isdigit():

        if int(options)-1 < len(r['list']):

            return 'Definition #%s for %s is "%s"' % (options, inputx, r['list'][int(options)-1]['definition'].strip())

        else:

            raise Exception('Definition requested is out of bounds.')

    else:

        raise Exception('Invalid options passed.')


def word(options, inputx):

    if options is None:

        raise Exception('Option [define, synonyms, antonyms, etymology] not provided.')
    
    elif options.lower() == 'define':

        return define_word(None, inputx)

    elif options.lower() == 'urban' or options.lower() == 'urban dictionary':

        return urban_dict('1', inputx)
