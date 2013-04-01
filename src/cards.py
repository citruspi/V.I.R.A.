# Cards file for V.I.R.A.

import requests
import json
import os

card_map = {
                'word'             : 'word',
                'define'           : 'define_word',
                'definition'       : 'define_word',
                'urban dictionary' : 'urban_dict',
                'urban'            : 'urban_dict',
                'book'             : 'book',
                'isbn'             : 'book',
                'vira'  		   : 'vira'
             }

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

    from wordnik import *

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
