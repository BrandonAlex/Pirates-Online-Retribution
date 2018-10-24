from panda3d.core import Thread
from pirates.piratesbase import EmoteGlobals as EG
DialogStringDict = {
    'rc.1visitJack.after': {
        0: {
            'dialog': "Ahh, I was just talking about you. Well not you in particular but someone much like you. I need help, mate. If ye pirate enough, eh?\x07Here's the skinny... seems that Jolly Roger has created a situation to draw me out. And it's a bloody catastrophe!\x07Jolly Roger's instituted a naval blockade - on rum. My sweet, innocent rum! Me and the other blokes 'round here are getting very... Thirsty!!!" },
        1: {
            'choice': 'How can I help?',
            'dialog': 'What can I do to help, Captain Sparrow?' },
        2: {
            'choice': "What's in it for me?",
            'dialog': "If I help, what's in it for me?",
            'emotes': [
                EG.EMOTE_SHOWMEMONEY] },
        3: {
            'dialog': "Good, good. Here's what we need to defeat Jolly...\x07...one of the Cursed Blades of El Patron himself. Perhaps you know him, tall... pointy beard... dead?\x07Only problem is you must go to Raven's Cove to find them. Dreadful place. But that's where they are. Now be off." },
        4: {
            'dialog': "Oh I'll make it worth your while for I need me rum, as do all these Pirates.\x07The only way to defeat Jolly is with one of El Patron's Cursed Blades. And the only place to find them is on...\x07...Raven's Cove. Dreadful place.\nBut that's where they are. Now be off." } },
    'rc.edwardBrittle.intro': {
        0: {
            'dialog': "BOOO! Booo! ye be not wanted\nThis place is vile, this island is haunted!\x07I be a ghost of horrible fame\nIf ye don't leave now, you'll end up the same!",
            'emotes': [
                EG.EMOTE_NED_CRAZY,
                EG.EMOTE_ANGRY] },
        1: {
            'choice': '\x01slant\x01Intimidate with Gun\x02',
            'dialog': "I'm not afraid of you besides, \x01slant\x01The Code\x02 says nothing about shooting ghosts, eh?" },
        2: {
            'choice': '\x01slant\x01Pretend to be a ghost\x02',
            'dialog': "You don't scare me 'cause I'm a ghost myself!",
            'emotes': [
                EG.EMOTE_ANGRY] },
        3: {
            'choice': '\x01slant\x01Run away fast\x02',
            'dialog': 'A g-g-g-g-host!? I think I soiled me pants!',
            'emotes': [
                EG.EMOTE_FART] },
        4: {
            'dialog': "Very well, brave soul, stay if ye must\nbut don't cry to me if your mission's a bust.\x07But a word of warning, ye hearty mate.\nAvoid red ghosts or doom be yer fate!",
            'emotes': [
                EG.EMOTE_FEAR,
                EG.EMOTE_CUTTHROAT] },
        5: {
            'choice': 'What happened here?',
            'dialog': 'What happened to this cursed island?' },
        6: {
            'choice': 'How do I get in the mines?',
            'dialog': 'How do I get in the mines IF the Cursed Blades are truly there?' },
        7: {
            'choice': 'Good bye',
            'dialog': 'Thanks Mr. Ghosty-crazy-miner-guy but I have to go.' },
        8: {
            'dialog': "There was a battle fierce for El Patron's guns.\nThe fighting went on from sun to sun.\x07But when the smoke cleared, the fight was a tie.\nAnd Jolly's anger began to fly.\x07He cursed the island but I survived\nto tell the tale to those alive.",
            'emotes': [
                EG.EMOTE_PETRIFIED,
                None,
                EG.EMOTE_YES] },
        9: {
            'choice': "Yikes, I'm outta here!",
            'dialog': 'No thanks, not interested... outta here! Bu-bye.' },
        10: {
            'dialog': 'The blades are there for I know these mines.\nFor I was a miner in happier times.\x07I will help ye if the others agree.\nOnly then will I willingly give you the key.',
            'emotes': [
                EG.EMOTE_YES,
                EG.EMOTE_SMILE] },
        11: {
            'choice': 'Others?!',
            'dialog': 'What do you mean by, others? I thought you were alone!' },
        12: {
            'dialog': "I may be daft but I know what I speak.\nThere are others who desire the blades that you seek.\x07Search the buildings and meet me fellow ghosts.\nThey might help you out and be good hosts.\x07But steer clear of ghosts you'll see in the streets.\nIf you happen upon them, hurry your feet... in other words, RUN!" },
        13: {
            'dialog': "Ahhh! Be ye alive or be ye dead?\nAre ye the ghosts of which I dread?\x07Why you're no spirit or ghostly diviner?\nNeither am I - I'm just a miner!\x07but I hold the key to the mine you seek\nwhere live the blades so cursed and bleak.",
            'emotes': [
                EG.EMOTE_NED_CRAZY,
                None,
                EG.EMOTE_NERVOUS] },
        14: {
            'choice': 'Calm down Old Man',
            'dialog': "Don't worry I'm no spirit, at least not yet.",
            'emotes': [
                EG.EMOTE_WAIT] },
        15: {
            'choice': '\x01slant\x01Pretend to be a ghost\x02',
            'dialog': "BOOO! Booo! I be a ghost of terrible fame!\nYee best be speaking or you'll end up the same!",
            'emotes': [
                EG.EMOTE_ANGRY] },
        16: {
            'choice': 'Bye bye, Crazy man',
            'dialog': "You're crazy! I'm sure I'll be able to find someone else sane to talk to.",
            'emotes': [
                EG.EMOTE_INSANE] },
        17: {
            'dialog': "If you find the oceans too vast and wide\nSearch for what the ravens hide\x07Shiny bits of metal broken\nBut once fit together you'll have a totem" } },
    'RavensCoveTotem.before': {
        0: {
            'dialog': "If you find the oceans too vast and wide\nSearch for what the ravens hide\x07Shiny bits of metal broken\nBut once fit together you'll have a totem" } },
    'RavensCoveTotem.after': {
        0: {
            'dialog': "Ah you've found the shiny baubles\nThey'll soon return you to these haunted hovels\x07Let me fix the pieces together\nAnd finish the totem with a raven's feather!" } },
    'rc.ghosts.fishmeister.catchFish.intro': {
        0: {
            'dialog': "Helping out ole Ned, are ya? He's daft, but no ghost. \nHow do I know that?\x07I'm one - and we know our own, we do. Now, help me with some fishing, and perhaps I'll help you...",
            'emotes': [
                EG.EMOTE_INSANE] },
        1: {
            'choice': 'Fishing? Why fishing?',
            'dialog': "Sorry to be nosey, mate but if you're a ghost, why do you need fish?",
            'emotes': [
                EG.EMOTE_HEADSCRATCH] },
        2: {
            'choice': 'I love fishing!',
            'dialog': "Just give me a pole and I'm happy to help!",
            'emotes': [
                EG.EMOTE_CELEBRATE] },
        3: {
            'dialog': "You see, in life, I was a fisherman and supplied the island with fish.\nBut when Jolly attacked, some of the townsfolk went in hiding... and starved.\x07I feel somehow... responsible and will \x01slant\x01never\x02 let that happen again.\n Help me and the other friendly ghosts and you'll get what you need.",
            'emotes': [
                None,
                EG.EMOTE_SAD] },
        4: {
            'dialog': "That's good news, mate! Catching fish for me and doing good deeds for the other \x01slant\x01friendly\x02 ghosts will grant you entrance to the mines!",
            'emotes': [
                EG.EMOTE_CLAP] } },
    'rc.ghosts.fishmeister.catchFish.after': {
        0: {
            'dialog': "Well done! Now help the other friendly ghosts if you haven't done so already and get into the mine...\x07Between you and me, whoever gets those cursed blades to Captain Sparrow will be a \x01slant\x01real\x02 hero, eh?",
            'emotes': [
                EG.EMOTE_CLAP] } },
    'rc.ghosts.zigana.brewPotions.intro': {
        0: {
            'dialog': "Shiver me bones! Are ye one of...\x01slant\x01the living\x02?\x07Must be, so I'll query a small favor of ye...\nHelp me restore me Voodoo staff that Jolly Roger broke and I'll help ye on that mine key. Deal?",
            'emotes': [
                EG.EMOTE_SCARED,
                EG.EMOTE_SMILE] },
        1: {
            'choice': 'No Problem.',
            'dialog': "You got a deal Madam, I'm off to the Potion Brewing tables right now!",
            'emotes': [
                EG.EMOTE_YES] },
        2: {
            'choice': 'What happened to you?',
            'dialog': "What happened to you during Jolly's attack?" },
        3: {
            'choice': "What if I don't?",
            'dialog': "Why should I help you? What's in it for me?",
            'emotes': [
                EG.EMOTE_SHRUG] },
        4: {
            'dialog': "When Jolly attacked I defended the town with me voodoo. Doin' well I was too, until Jolly faced me himself.\x07He laughed at me and snapped me staff like it was a twig then mocked me and took me life.\x07Help me make a new staff... one Ole Jolly himself won't find so funny!",
            'emotes': [
                EG.EMOTE_ANGRY] },
        5: {
            'dialog': "Why you feckless weasel, I ought to...\x07Sorry, I'm a bit testy since JOLLY ROGER CURSED ME!\nSo if ye want the key to the mine... do as I ask?",
            'emotes': [
                EG.EMOTE_ANGRY,
                EG.EMOTE_SNARL] },
        6: {
            'choice': 'Glad to help!',
            'dialog': "Sure, Madam Zigana, I'm glad to help!" },
        7: {
            'choice': 'No way I am gonna help you!',
            'dialog': "Sorry Madam, but I'm outta here!",
            'emotes': [
                EG.EMOTE_NO] } },
    'rc.ghosts.zigana.brewPotions.after': {
        0: {
            'dialog': 'So you got them all, eh? Well done, well done indeed.',
            'emotes': [
                EG.EMOTE_BLOWKISS] } },
    'rc.ghosts.fantifico.visitTiaDalma.intro': {
        0: {
            'dialog': "S\xc3\xad, I see you are a worthy Pirate. So you help Se\xc3\xb1or Fantifico, yes?\nWe help each other, yes?\x07I have something you want. You can help me get something I need, S\xc3\xad?\x07My need is simple - I merely want to...\x07LIVE AGAIN! You get me potion to live again, I help you with Ned's key. We have a deal, yes?",
            'emotes': [
                EG.EMOTE_YES,
                EG.EMOTE_SMILE,
                None,
                EG.EMOTE_ANGRY] },
        1: {
            'choice': 'Live again - seriously?',
            'dialog': "I will try my best but, I'm not sure that's possible!",
            'emotes': [
                EG.EMOTE_HEADSCRATCH] },
        2: {
            'choice': "What's your story?",
            'dialog': "You don't look like my most Pirates and Knaves around here, what's your story?",
            'emotes': [
                EG.EMOTE_LAUGH] },
        3: {
            'choice': 'Sure, we have a deal!',
            'dialog': 'I am ready and willing to help, Se\xc3\xb1or Fantifico!',
            'emotes': [
                EG.EMOTE_YES] },
        4: {
            'dialog': 'Oh but it is my amigo, it is! You just need to know the right people, yes?\x07A certain gypsy priestess can handle that, now please, the more time we waste talking, the longer I must remain a ghastly ghost.',
            'emotes': [
                EG.EMOTE_YES] },
        5: {
            'dialog': "You have a keen eye for a Pirate. Yes, Se\xc3\xb1or Fantifico was not like the rest - I have impeccable taste and flair, as you can see!\x07But alas, my life was cut short when I was...\x01slant\x01how should I say\x02, hiding from Jolly's attack? Yes, hiding.\x07But I can restore my life with your help and then, I will speak to Se\xc3\xb1or Loco Ned about your honorable deeds, yes?",
            'emotes': [
                EG.EMOTE_WINK,
                None,
                EG.EMOTE_YES] } },
    'rc.ghosts.fantifico.visitTiaDalma.after': {
        0: {
            'dialog': "Se\xc3\xb1or Fantifico!? Ha! He was a fool and seems to be one in death, too.\x07Help you I will, but not for his sake... for yours. I want you to get the Cursed Blades of El Patron.\x07It's our only hope to stop Jolly Roger. I will brew him a special potion.",
            'emotes': [
                EG.EMOTE_LAUGH] },
        1: {
            'choice': 'What kind of potion?',
            'dialog': 'What sort of potion are you talking about, and how can I help?',
            'emotes': [
                EG.EMOTE_HEADSCRATCH] },
        2: {
            'choice': 'Will that do the trick?',
            'dialog': "Are you sure that's all it takes? If so, I'll be right back, just tell me what needs to be done!" },
        3: {
            'dialog': "I've never done it on people - only animals, but it should work.\x07These are the ingredients I need for the ceremony that restores life.\nCollect them and return to me.",
            'emotes': [
                EG.EMOTE_SHRUG] } },
    'rc.ghosts.fantifico.PotionIngredients.after': {
        0: {
            'dialog': "You've done well, Pirate. All that remains is the sacred voodoo chant to restore life.\x07And you must learn it.\nListen as if your life depends on it!",
            'emotes': [
                EG.EMOTE_YES] },
        1: {
            'dialog': 'Ok, I am ready. Go ahead.',
            'emotes': [
                EG.EMOTE_YES] },
        2: {
            'dialog': 'Give Se\xc3\xb1or Fantifico the potion and chant this,\x07\x01slant\x01Live as live and die as die, time to make the spirits fly.\x02\x07I hope for your sake it works. Now go.',
            'emotes': [] } },
    'rc.ghosts.fantifico.deliverPotion.after': {
        0: {
            'dialog': 'You have done this, s\xc3\xad?! I am so happy, I dance!\x07Now give me the potion and speak the chant but be sure it is correct...\nor you may pay with your life, no?',
            'emotes': [
                EG.EMOTE_DANCE,
                EG.EMOTE_HANDITOVER] },
        1: {
            'dialog': 'Live as live and die as die, time to make the demons fly.' },
        2: {
            'dialog': 'Live as life and life so lived, time to make the spirits fib.' },
        3: {
            'dialog': 'Live as live and die as die, time to make the spirits fly.' },
        4: {
            'choice': 'What happened?!',
            'dialog': "Tia Dalma said she's never done it on people before, sorry!",
            'emotes': [
                EG.EMOTE_SHRUG] },
        5: {
            'choice': "That's hilarious!",
            'dialog': 'I guess your \x01slant\x01true\x02 self did come back to life since you were a \x01slant\x01chicken!\x02',
            'emotes': [
                EG.EMOTE_LAUGH] },
        6: {
            'choice': 'I did what you asked.',
            'dialog': 'Tell Crazy Ned to give me the key because you did get your life back,...\x07...Se\xc3\xb1or Clucks-a-lot!',
            'emotes': [
                None,
                EG.EMOTE_LAUGH] } },
    'rc.ghosts.threadbarren.RetrieveSails.intro': {
        0: {
            'dialog': "State yer business, Pirate!\nAh, so it's the key to the mine you be wantin'...\x07It's a fool's errand but it's yer life. Ye can help me by sinkin' every Undead ship around to pay back that vile Jolly Roger!",
            'emotes': [
                EG.EMOTE_SNARL] },
        1: {
            'choice': 'Glad to help!',
            'dialog': 'Yes! I hate Undead Ghost ships as much as you, Widow Threadbarren.',
            'emotes': [
                EG.EMOTE_CLAP] },
        2: {
            'choice': 'What happened?',
            'dialog': 'What did Jolly do to you when he attacked?',
            'emotes': [
                EG.EMOTE_HEADSCRATCH] },
        3: {
            'choice': "No thanks. I don't sink ships.",
            'dialog': 'No thanks, I am not that into sinking Undead ships right now. Bye.',
            'emotes': [
                EG.EMOTE_NO] },
        4: {
            'dialog': "Ye have the makings of a fine Pirate and sinkin' Jolly's vile ships will be a fittin' pay back for what he done to me, I say.",
            'emotes': [
                EG.EMOTE_SINCERETHANKS] },
        5: {
            'dialog': "Jolly Roger and his army rased the town sparing no one... except for me, the town's seamstress.\x07I was ordered to sew new sails for Jolly's damaged fleet. He swore I would live if I did his biddin' but alas...\x07...he lied, and snatched me life after finishin' the work.\nSink these undead ships and bring me back the sails I made for them.",
            'emotes': [
                EG.EMOTE_NERVOUS,
                None,
                EG.EMOTE_ANGRY] } },
    'rc.ghosts.threadbarren.RetrieveSails.after': {
        0: {
            'dialog': "Hmmm. That's odd. I don't feel at peace with this like I thought I would.\x07But I suppose there be more of those \x01slant\x01boneheads\x02 at the bottom of the sea now, and that is good. I suppose.",
            'emotes': [
                EG.EMOTE_HEADSCRATCH,
                EG.EMOTE_SHRUG] } },
    'rc.ghosts.clubhearts.disguise.intro': {
        0: {
            'dialog': "Ahoy mate, if ye have come to play cards, your luck has run out. But we may be able to help ye with ole Ned.\x07Get some of our gold back that Jolly cheated from us, and we'll do our part, savvy?",
            'emotes': [
                EG.EMOTE_WAVE,
                EG.EMOTE_SHOWMEMONEY] },
        1: {
            'choice': 'What can I do?',
            'dialog': "I'm glad to help just tell me what to do!",
            'emotes': [
                EG.EMOTE_SMILE] },
        2: {
            'choice': 'What happened with Jolly?',
            'dialog': 'What happened when Jolly attacked the island?' },
        3: {
            'dialog': "When Jolly's army overran the town we fled to the tavern. He threatened to burn the place down.\x07But once he saw it was a gambling den he offered to let us go if we beat him in a game of poker.\x07Of course the scoundrel stacked the deck! And with every hand we lost a little more of our souls until, we died.\x07Find the skeleton's poker game, win back our gold and we'll help you get the key to Ned's mine.\x07Be warned, the cursed won't welcome new players, but they know us, so you'll have to disguise yourself as one of us.",
            'emotes': [
                EG.EMOTE_SAD,
                None,
                EG.EMOTE_ANGRY,
                EG.EMOTE_YES] } },
    'rc.ghosts.clubhearts.disguise.after': {
        0: {
            'dialog': 'Hey! What do you want, stranger?',
            'emotes': [
                EG.EMOTE_GLARE] },
        1: {
            'choice': 'I want to play skeleton poker!',
            'dialog': 'I came here to play skeleton poker. Please grant me access to the parlor, or else!',
            'emotes': [
                EG.EMOTE_ANGRY] },
        2: {
            'dialog': "Sorry, I'm not ready for this. Bye!" },
        3: {
            'dialog': 'Welcome, Mr. Clubheart! Here is your access charm.',
            'emotes': [
                EG.EMOTE_SMILE] },
        4: {
            'dialog': 'Welcome, Mrs. Clubheart! Here is your access charm.',
            'emotes': [
                EG.EMOTE_SMILE] },
        5: {
            'dialog': "Sorry, mate. The skeleton parlor room is limited to special guests only and you don't look like anyone on the list." },
        6: {
            'dialog': 'Your shirt and your pants look familiar, but you seem to be missing something else. Sorry, but only special guests can enter.',
            'emotes': [
                EG.EMOTE_NO] },
        7: {
            'dialog': 'Your pants look familiar, but you seem to be missing something else. Sorry, but only special guests can enter.',
            'emotes': [
                EG.EMOTE_NO] },
        8: {
            'dialog': 'Your shirt looks familiar, but you seem to be missing something else. Sorry, but only special guests can enter.',
            'emotes': [
                EG.EMOTE_NO] },
        9: {
            'dialog': 'Your hat and your pants look familiar, but you seem to be missing something else. Sorry, but only special guests can enter.',
            'emotes': [
                EG.EMOTE_NO] },
        10: {
            'dialog': 'Your hat looks familiar, but you seem to be missing something else. Sorry, but only special guests can enter.',
            'emotes': [
                EG.EMOTE_NO] },
        11: {
            'dialog': 'Your hat and your shirt look familiar, but you seem to be missing something else. Sorry, but only special guests can enter.',
            'emotes': [
                EG.EMOTE_NO] },
        12: {
            'dialog': 'Your skirt and your boots look familiar, but you seem to be missing something else. Sorry, but only special guests can enter.',
            'emotes': [
                EG.EMOTE_NO] },
        13: {
            'dialog': 'Your boots look familiar, but you seem to be missing something else. Sorry, but only special guests can enter.',
            'emotes': [
                EG.EMOTE_NO] },
        14: {
            'dialog': 'Your skirt looks familiar, but you seem to be missing something else. Sorry, but only special guests can enter.',
            'emotes': [
                EG.EMOTE_NO] },
        15: {
            'dialog': 'Your blouse and your boots look familiar, but you seem to be missing something else. Sorry, but only special guests can enter.',
            'emotes': [
                EG.EMOTE_NO] },
        16: {
            'dialog': 'Your blouse looks familiar, but you seem to be missing something else. Sorry, but only special guests can enter.',
            'emotes': [
                EG.EMOTE_NO] },
        17: {
            'dialog': 'Your blouse and your skirt look familiar, but you seem to be missing something else. Sorry, but only special guests can enter.',
            'emotes': [
                EG.EMOTE_NO] } },
    'rc.ghosts.clubhearts.undeadPoker.after': {
        0: {
            'dialog': "Well done, good friend, well done!\nWe don't know how to thank you, only to say...\x07We're happy to tell Ned ye have been good to us. That should get you one step closer to the key and...\x07\x01slant\x01El Patron's Cursed Blades\x02.",
            'emotes': [
                EG.EMOTE_CLAP,
                EG.EMOTE_SINCERETHANKS] } },
    'rc.GhostsOfRavensCove.after': {
        0: {
            'dialog': "Ah, yer back, that's a good sign you see\x07For the only way you can get the key\n is if me ghostly friends agree\x07Now all have said your help was fine\nso take the key to that wretched mine!",
            'emotes': [
                EG.EMOTE_YES,
                None,
                EG.EMOTE_SMILE] } },
    'rc.talkToBellrog.after': {
        0: {
            'dialog': 'Ahoy, Pirate! State your business in here or my bodyguard, Kudgel, will run ya through!',
            'emotes': [
                EG.EMOTE_WAIT] },
        1: {
            'choice': 'Back off!',
            'dialog': "Back off or I'll send you and your bodyguard to Davy Jones' locker!" },
        2: {
            'choice': 'Ooops, sorry!',
            'dialog': 'Sorry, I was looking for the \x01slant\x01Cursed Blades of El Patron\x02.',
            'emotes': [
                EG.EMOTE_WAIT] },
        3: {
            'choice': 'Who are you?',
            'dialog': 'Who are you and what are you doing in the mines?',
            'emotes': [
                EG.EMOTE_HEADSCRATCH] },
        4: {
            'dialog': "Don't be absurd, Pirate. You're no match for Kudgel! But why not put away our weapons and talk like civilized souls, eh?",
            'emotes': [
                EG.EMOTE_LAUGH] },
        5: {
            'dialog': "Searching for the \x01slant\x01Cursed Blades of El Patron\x02 are you?\nIndeed. I will help you and you will help me but know this.\x07These old mining caves are haunted with the ghosts of El Patron's crew. Be careful or pay the devil, you will.",
            'emotes': [
                None,
                EG.EMOTE_CUTTHROAT] },
        6: {
            'dialog': "My name's Dr. Orwin Bellrog, and I am an explorer. My trusty bodyguard, Kudgel and I were exploring Raven's Cove when Jolly Roger invaded.\x07We hid inside this mine but got trapped by this cursed door! Now we're mere ghosts of our true selves. We can help you find the blades but you must help us, eh?\x07But know this, these old mining caves are haunted with the ghosts of El Patron's crew. Be careful or pay the devil, you will.",
            'emotes': [
                EG.EMOTE_FLEX,
                EG.EMOTE_ANGRY,
                EG.EMOTE_CUTTHROAT] },
        7: {
            'choice': 'Okay, but who are you?!',
            'dialog': "Okay, but... who you are and what you're doing in here?" },
        8: {
            'choice': "I'll keep it handy.",
            'dialog': "No, I'll keep it handy just in case. Now who are you and what's your story?" } },
    'rc.le.1findJournals.after': {
        0: {
            'dialog': 'So you got the journals, let me read them!',
            'emotes': [
                EG.EMOTE_HANDITOVER] },
        1: {
            'dialog': "Interesting! According to these journals El Patron was determined to guard the lost weapons for all eternity!\x07 So he sealed himself, the blades and his crew inside this mine.\x07 The crew mutinied but couldn't escape so they constructed this door, imprisoned El Patron behind it and each of four officers took one of the four idols needed to open it.\x07 To claim the first idol you defeat ten ghosts before the grave of the first officer." } },
    'rc.le.2LureGhosts.after': {
        0: {
            'dialog': 'Well done!',
            'emotes': [
                EG.EMOTE_CLAP] },
        1: {
            'dialog': 'Now, the second journal says the second officer of the Skeleton Crew was so hated by his men that...\x07...you must fend off their ghosts to acquire his idol. He was truly despised, indeed. ' } },
    'rc.le.3defendTraitor.after': {
        0: {
            'dialog': "You dispatched them with ease! I'm beginning to like you!",
            'emotes': [
                EG.EMOTE_SMILE] },
        1: {
            'dialog': "Now, the third journal says that this Skeleton officer's idol\x07...was snatched and buried by a dog! Ha, ha! And you just make your own divining rod to find it.",
            'emotes': [
                None,
                EG.EMOTE_LAUGH] } },
    'rc.le.4DowsingRodParts.after': {
        0: {
            'dialog': 'So you got all the parts! Well done, let me help you assemble the rod.' },
        1: {
            'dialog': 'Here you go. Now use it to find the third idol.',
            'emotes': [
                EG.EMOTE_YES] } },
    'rc.le.5useDowsingRod.after': {
        0: {
            'dialog': 'Excellent work, mate!' },
        1: {
            'dialog': "If only I could accompany you but, alas...\nI was but a coward in life and fear I am in the afterlife as well.\x07The fourth journal says you'll find an idol at the southernmost grave guarded by very vicious ghosts.\x07You will \x01slant\x01perish\x02 if you do not take some help with you! Heed my advice Pirate and, good luck.",
            'emotes': [
                EG.EMOTE_NERVOUS] } },
    'rc.le.6getLastIdol.after': {
        0: {
            'dialog': 'You found the last idol. Now we can finally open this door and get the treasure!',
            'emotes': [
                EG.EMOTE_CELEBRATE] },
        1: {
            'dialog': 'Glad I could be of service.' },
        2: {
            'dialog': 'Unfortunately, your services are no longer needed. Kudgel, dispose of this trash!',
            'emotes': [
                EG.EMOTE_CUTTHROAT] } },
    'rc.le.7defeatKudgel.after': {
        0: {
            'dialog': 'Please, spare me! I underestimated your strength, pirate!',
            'emotes': [
                EG.EMOTE_PETRIFIED] },
        1: {
            'dialog': 'Behind that door is the fearsome El Patron himself. If you defeat him, the \x01sland\x01Cursed Blades\x02 are yours!',
            'emotes': [
                EG.EMOTE_SNARL] } } }
