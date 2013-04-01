## V.I.R.A.

### Who am I?

I am V.I.R.A. - your __Virtual Information Retrieval Assistant__. 

### What Do I Do?

You can interact with my via specially formmated queries to get certain information like:

- the weather
- definitions of words
- translations of phrases
- movie times

### Why?

In 2013, the Wikimedia Foundation announced the Wikipedia Zero initiative.

> Wikipedia Zero is an initiative of the Wikimedia Foundation to enable mobile access, free of data charges, to Wikipedia in developing countries. The objective of the program is to reduce barriers to accessing free knowledge -- two of the largest barriers being cost of data usage and network speed.

Essentially, users would be able to query Wikipedia over SMS.

We wondered - _Why can't we do that with other information?_ We couldn't come up with an answer. So, we built a solution.

### What Can I Do?

V.I.R.A. was written with the original intent of retrieving basic information like definitions and weather conditions. But in no way is she limited to that.

You can make V.I.R.A. do nearly anything - if you can dream it, she can probably do it.

To learn how to add features to V.I.R.A., scroll down to the section on [extending her]().
    
## Usage

V.I.R.A. accepts specially formatted strings - `card:options:input`.

Cards are actions or verbs like `word`, `define`, `hash`, or `weather`.

Options are options for that card. An option for the `hash` function might be a hash type - `SHA1` or `MD5`.

Input is the actual input which will be processed - maybe the string the be hashed.

## Cards

The following cards are part of the official distribution:

### Word

| Option | Input | Sample | Output/Action |
|:-------|:------|:-------|:--------------|
| define | term to be defined | word:define:robot | Remaps to `define::robot` |
| urban | term to be defined | word:urban:robot | Remaps to `urban dictionary:1:robot` |

### Definition, Define

| Option | Input | Sample | Action |
|:-------|:------|:-------|:-------|
| | term to be defined | define::robot | Returns the definition of `robot` |

### Urban, Urban Dictionary

| Option | Input | Sample | Action |
|:-------|:------|:-------|:-------|
| | term to be defined | urban::robot | Remaps to`urban:1:robot` |
| # | term to be defined | urban:#:robot | Returns the number of definitions for `robot` on Urban Dictionary |
| 1+ | term to be defined | urban:5:robot | Returns the 5th definition of `robot` on Urban Dictionary |

### Book, ISBN

| Option | Input | Usage | Action |
|:-------|:------|:------|:-------|
| | 10 or 13 digit ISBN | book::0345342968 | Returns the `title`, `author`, `publish date`, and `description` for the work. |

## Implementations

### Python Script

    import vira

    vira = VIRA()
    vira.solve('define::robot')

## The Inner Working

### File Structure

    V.I.R.A./
    ├── vira.py
    ├── cards.py

### Flow

VIRA.py itself does nothing more than accept specially formatted input and parse it. From the input, it determines the correct _card_ (feature).

It then uses the _card map_ (a dictionary defined in `cards.py`) to map the card to a function defined in `card.py` which is then called dynamically.

### Example

Say, V.I.R.A. gets passed the string `define::robot`. She would parse it as follows:

| Card   | Options | Input |
|:-------|:--------|:------|
| define | None    | robot |

The `card_map` maps the `define` card to the `define_word` function which is defined in `cards.py`. 

So, V.I.R.A. would call `cards.define_word(None, 'robot')`.

### Extending

Extending V.I.R.A. is easy. Say we want to add a card which returns the SHA1 hash of a string.

First, we would map a function the to card: add `{'sha1' : 'sha1_str'}` to the `card_map` in `cards.py`.

Then define a function:

    def sha1_str(options, inputx):
    
        import hashlib
        
        return hashlib.sha1(inputx).hexdigest() 

That's it! Now, you can use it by passing `sha1::word` to V.I.R.A.
