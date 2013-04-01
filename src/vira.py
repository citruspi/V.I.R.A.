import cards
import argparse

class VIRA(object):

    def __init__(self): 
        
        pass

    def solve(self,inputx):

        parts = inputx.split(':',3)

        try:

            if parts[0] in cards.card_map:

                func = getattr(__import__('cards'), cards.card_map[parts[0]])
                return func(parts[1], parts[2])

            else:

                raise Exception('Service is not mapped.')

        except Exception, e:
            
            return e

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='inputx')

    args = parser.parse_args()

    vira = VIRA()
    r = vira.solve(args.inputx)

    if hasattr(r, 'lower'): 

        response = [r]
    
    else:
    
        response = r

    for i in response:

        print i
