# Save time typing on macos with a plist of keyboard shorctuts

Pass an input file defining all words you use (each word on a new line). The script will create a plist mapping all "unique paths" to a word.

For example, if your entire dictionary of words was just "met", "meteor" and "meteors" you would have two shortcuts, a mapping of me -> met and mete -> meteor. 

``
    met
    meteor
    meteors
``

``
    me -> met;
    mete -> meteor
``

I.e. the moment you type a combination of letters that is not a complete word and that follows a unique path you "skip ahead" to where the path is no longer unique.


### Data sources/credits

Dataset of unigram words pulled from kaggle dataset https://www.kaggle.com/datasets/rtatman/english-word-frequency?resource=download

20k.txt dataset pulled from https://github.com/first20hours/google-10000-english
