#!/usr/bin/env python
# coding: utf-8

#### Human labeled spurious words for each dataset
    
imdb_bad_pos = ['count', 'imax', 'spider', 'ages', 'secretary', 'cinema', 'sexual', 'thornberrys', 
               'animated', 'bride', 'pulls', 'history', 'son', 'pray', 'still', 'pacino', 'thanks', 
               'department', 'calls', 'vietnam', 'performances', 'spielberg', 'detailed',
               'speaks', 'alan', 'everyday', 'russian', 'martha', 'majidi', 'roles', 
               'photo', 'summer', 'profile', 'mike', 'examines', 'reminder', 'political',
               'form', 'bourne', 'popcorn', 'mamet', 'anime', 'am', 'medium', 'captures',
               'distinct', 'stylistic', 'guaranteed', 'smith', 'frailty', 'debate',
               'rhythm', 'spare', 'freedom', 'weeks', 'provides', 'confidence',
               'constructed', 'culture', 'open', 'conduct', 'help', 'grown', 'skin',
               'manages', 'tear']

imdb_bad_neg = ['pie', 'neither', 'too', 'disguise', 'product', 'tv', 'animal', 'schneider',
           'benigni', 'none', 'sheridan', 'seagal', 'god', 'college', 'demme', 'named', 'six',
           'wilder', 'numbers', 'apparently', 'merit', 'track', 'idea',
           'violence', 'title', 'snake', 'total', 'niro', 'guns', 'somewhere',
           'lust', 'alas', 'textbook', 'showtime', 'car', 'follows', 'quarter',
           'built', 'jonah', 'ballistic', 'sort', 'chosen', 'television', 'shifting',
           'pacing', 'affair', 'guess', 'independent', 'jay', 'evidence', 
           'purpose', 'add', 'premise', 'elaborate', 'putting', 'sequences', 'produce', 'sequence',
           'treats', 'john', 'etc', 'instead', 'thousand', 'pinocchio', 'requires',
           'already',  'pulp', 'unintentional', 'unintentionally', 'meant',
           'wannabe', 'unless', 'stunt', 'jokes', 'wasn', 'hasn', 'save', 'bits',
           'heavy']
           
kindle_bad_pos = ['admit','bedtime', 'born', 'boy', 'british', 'city', 'coming', 
       'continues', 'copy', 'creatures', 'cry', 'described', 'drug', 'everyone', 
       'exception',  'finds', 'forward', 'gluten', 'holds', 'hot', 'humans',
       'hurt', 'issues', 'jeff', 'jess', 'job','keeps', 'last', 'late', 'laura', 'lil', 'lucas', 'now',
       'options', 'pace', 'penny', 'play','points', 'put', 'putting', 'rainy','ride', 'safe',
       'sexy', 'sister', 'sitting', 'spy', 'stop','summer', 'tho', 'tips', 'turner', 'turning', 'tv',
       'twist', 'twists', 'us', 'usual', 'vampire', 'wait', 'wedding', 'whatever', 'worked', 'wrong',
        
       'caught', 'considering', 'definitely', 'down', 'explains', 'growth', 'guide', 'hanger', 'immediately', 
                  'ready', 'released', 'wished']

kindle_bad_neg = ['15', '99', 'against', 'app',
       'basic', 'basically', 'blurb','call', 'cents', 'chapter', 'chapters', 'deliver', 'dollar', 'draw',
       'effort', 'element', 'english', 'finish','free', 'girl', 'grammar', 'halfway',
       'hold', 'idea', 'kinds', 'let', 'load', 'loaded', 'looked', 'luck', 'maybe',
       'mother', 'near', 'pages','paid', 'particularly', 'pay', 'perhaps','positive', 
       'possibly', 'potential', 'premise', 'print','probably', 'product', 'purpose', 'rated', 'religious', 
       'reviews', 'sample', 'save', 'saying','seemed', 'sentence', 'sounded', 'sounds', 'standard',
       'substance', 'tastes', 'text', 'title',  'towards', 'weeks', 'younger', 'zero',
                 
       'didn', 'didnt', 'doesn', 'jumping', 'no', 'nor', 'not', 'nothing', 'shortly', 'unless', 'wasn', 'wasnt', 'wouldn']
       
# terms for toxic wiki comment (single sentences)
toxic_bad_pos = ['18', 'accomplish', 'allah', 'allows', 'appropriate','boys', 'brothers',
       'burning', 'crowd', 'crying', 'develop','dnc', 'dude','economics', 'educated',
       'enemies','flood', 'gop', 'hearts','heterosexuals', 'historical', 'holds', 'homophobic',
       'injustice', 'jew', 'jihadi', 'killings', 'knowing','lifetime',  'march', 'million', 'mohammad', 'mongering',
       'narrative', 'nationalism', 'nyc', 'obsessed', 'opposition',
       'partisan', 'peace','perpetual', 'piece', 'preach', 'promoting', 'proves',
       'pulled', 'referred', 'repent','residents','rohingya', 'root','secret',
       'shooter','sisters', 'stake', 'taliban', 'throw', 'thrown', 'tolerant',
       'tone', 'toting', 'twitter', 'uniform', 'unrelated','violates', 'voted', 'water','wide',
                
        'gangs', 'intelligence', 'murders', 'subjugation']

toxic_bad_neg = []

# terms for toxic wiki comment (multiple sentences)
# toxic_bad_pos = ['gay', 'blacks', 'vagina', 'pedophile', 'kill', 'gays',
#                     'ignorance', 'pile', 'raped', 'rape', 'hugh', 'muslims',
#                     'negro', 'grab', 'oral', 'homosexual', 'black', 'liberalism',
#                     '02', 'forever', 'lesbians', 'lesbian', 'muslim', 'yea',
#                     'sexual', 'streets', 'audience', 'reilly', 'irish',
#                     'handed', 'walks', 'olds', 'bags', 'ing', 'con', '1000',
#                     'sheriff', 'homosexuality', 'bag', 'buck', 'obey', 'principal',
#                     'speaks', 'belong', 'kiss', 'hippies', 'double', 'ergo', 
#                     'transgender', 'till']

toxic_tw_bad_pos = ['realdonaldtrump', 'mouth', 'three', 'donaldjtrumpjr', 'lady', 'jihadi', 'handle', 'cum', 
                   'house', 'showing', 'gop', 'typical', 'blocked', 'america', 'fans', 'deleted', 'la', 'goofy', 
                   'arianagrande', 'corny', 'learn', 'profile', 'citizens', 'fire', 'thinks', 'plz', 'sexy', 
                   'spot', 'realize', 'wat', 'attractive', 'everyday', 'article', 'nobody', 'indians', 
                   'hahahaha', 'cnn', 'debt', 'car', 'image', 'face', 'michael', 'pure', 'off', 'violence',
                   'text', 'bye', 'piece', 'neither', 'yesterday', 'light', 'grown', 'african', 'sarri', 
                   'fortnitegame', 'stirring', 'except', 'big', 'movies', 'sleeping', 'story', 'jackposobiec', 
                   'fa', 'most', 'person', 'racist', 'piersmorgan', 'wet', 'pink', 'unlike', 'link', 'community', 
                   'til', 'youtube', 'dailymirror', 'example', 'sitting', 'period', 'major', 'care', 'fault', 
                   'bc', 'pregnant', 'dogs', 'per', 'sacked', 'followed', 'towards', 'takes', 'touch', 'comment',
                   'kno', 'national', 'kepa', 'build', 'themichaelowen', 'goal', 'lil', 'parents', 'air', 'send',
                   'choice', 'hi', 'peta', 'blame', 'ban', 'biggest', 'thick', 'mans', 'deserves', 'issues',
                   'chest', 'alphaworshiper', 'side', 'edkrassen', 'rights', 'bet', 'mr', 'aint', 'between',
                   'internet', 'post', 'explains', 'acting', 'put', 'selling', 'rather', 'plus', 'ill', 'lick', 
                   'business', 'tf', 'pull', 'keeps', 'numbers', 'running', 'eu', 'gay', 'teammates']

toxic_tw_bad_neg = []


def get_spurious_words():

    spurious_words_map = {}
    spurious_words_map['imdb_bad_pos'] = imdb_bad_pos
    spurious_words_map['imdb_bad_neg'] = imdb_bad_neg
    spurious_words_map['kindle_bad_pos'] = kindle_bad_pos
    spurious_words_map['kindle_bad_neg'] = kindle_bad_neg
    spurious_words_map['toxic_bad_pos'] = toxic_bad_pos
    spurious_words_map['toxic_bad_neg'] = toxic_bad_neg
    spurious_words_map['toxic_tw_bad_pos'] = toxic_tw_bad_pos
    spurious_words_map['toxic_tw_bad_neg'] = toxic_tw_bad_neg
    
    return spurious_words_map

