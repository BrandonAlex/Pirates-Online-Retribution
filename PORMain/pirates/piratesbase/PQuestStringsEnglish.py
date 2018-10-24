from panda3d.core import Light, Material, Thread
from pirates.quest.QuestConstants import NPCIds
from pirates.piratesbase import EmoteGlobals
Reward_Gold = 'Gold'
Reward_XP = 'Notoriety'
Reward_Both = 'Gold & Notoriety'
Teleport_Reward_Tortuga = 'Tortugan Teleport Totem, Gold & Notoriety'
Teleport_Reward_PortRoyal = 'Port Royal Teleport Totem, Gold & Notoriety'
Teleport_Reward_Cuba = 'Cuba Teleport Totem, Gold & Notoriety'
Teleport_Reward_PadresDelFuego = 'Padres Del Fuego Teleport Totem, Gold & Notoriety'
Playing_Card_Reward = 'A Playing Card, Gold & Notoriety'
Collection_Reward_Rogues = 'Nine Rogues Collection Unlock & Notoriety'
Collection_Reward_Medals = 'Navy Medals Collection Unlocked, Gold & Notoriety'
Collection_Reward_Teeth = "Rudyard's Teeth Collection Unlocked, Gold & Notoriety"
Collection_Reward_Rings = 'Rhineworth Rings Collection Unlocked & Notoriety'
Collection_Reward_Chess = 'Chess Collection Unlocked & Notoriety'
Collection_Reward_Figurines = "Tia Dalma's Menagerie Collection Unlocked & Notoriety"
Weapon_Reward_Doll = 'A Voodoo Doll & Notoriety'
Weapon_Reward_Dagger = 'A Dagger & Notoriety'
Weapon_Reward_Grenade = 'A Grenade & Notoriety'
Weapon_Reward_Staff = 'A Voodoo Staff & Notoriety'
Jewelry_Reward = 'Jewelry'
QuestStrings = {
    '': {
        'description': 'Return additional cure ingredients.',
        'stringAfter': "Good. I'll mix it for you. You'll only muck it up. Here...",
        'title': 'Return to Fabiola' },
    '0': {
        'description': 'Defeat the skeletons lurking about Port Royal.',
        'stringAfter': 'Thank you.',
        'stringBefore': 'These skeletons are getting out of hand. \nThe people of Port Royal need your help.',
        'title': 'Hunt Skeletons' },
    '1': {
        'stringBefore': "Boatswain Bill usually skulks behind these buildings. He'll have somethin' fer you to do." },
    '1120608041.7npavlov': {
        'stringAfter': "Ooh, ye brought me an aspirin!  Hmm... your kindness is a pleasant surprise.  \x07Here, have a priceless magical amulet passed down many generations that's conveniently lying in my top drawer.",
        'stringBefore': 'Go away!  I have a headache.  Yar.',
        'stringDuring': 'Ohhh, this headache be killing me!  Why do ye insist on bothering me!' },
    '1141357511.36sdnaik': {
        'stringBefore': "Nyaaaaar.   Look how ugly yer face be.   Must be needin' to kill some skeletons!",
        'title': 'Defeat 10 Skeletons' },
    '1141416661.17sdnaik': {
        'description': "Find Yellow Dan's lost earring that he buried somewhere on Port Royal.",
        'stringBefore': 'Some of those undead ruffians accosted Dan,\nstealing one of his favorite earrings. \x07Out of fear, he buried the other. Retrieve both of them\nso I can surprise him for his birthday.',
        'title': 'The Curse of Yellow Dan' },
    '1141781456.75sdnaik': {
        'description': "Find Yellow Dan's stolen earring.",
        'stringAfter': "Great! I'll go find him straight away.",
        'title': 'The Curse of Yellow Dan' },
    '12': {
        'stringAfter': "Arr, me sea chart! Thank ye! Here's somethin' fer helpin'.",
        'stringBefore': "Jolly Roger's skeletons have taken me sea chart. Arr!",
        'stringDuring': 'Have ye found me chart?',
        'title': 'Lost Chart' },
    '13': {
        'stringAfter': "Arr, 'tis true, a fearsome pirate ye be.",
        'stringBefore': 'So ye be a pirate, eh? Why should I believe ye?',
        'title': 'Sink Ship' },
    '14': {
        'stringAfter': "Guess you had it in ye after all. Here's a fine reward.",
        'stringBefore': "Think ye can hold your own with the card sharps 'round here? Don't bet on it!",
        'title': 'The Gambler' },
    '15': {
        'stringAfter': 'Thanks for delivering that rum for me. I owe ye a favor.',
        'stringBefore': 'I need a Pirate like yerself to do a little job for me. Deliver some rum to Port Royal.',
        'title': 'Deliver Rum' },
    '16': {
        'stringAfter': 'Thanks for smuggling that rum for me. I owe ye a favor.',
        'stringBefore': 'I need a Pirate like yerself to do a little job for me. Smuggle some rum into Port Royal.',
        'title': 'Smuggle Rum' },
    '17': {
        'stringAfter': 'Thanks for plundering that rum for me. I owe ye a favor.',
        'stringBefore': 'I need a Pirate like yerself to do a little job for me. Plunder some rum from a ship.',
        'title': 'Plunder Rum' },
    '18': {
        'stringAfter': 'Thanks for marooning that scallywag for me. I owe ye, mate.',
        'stringBefore': 'I need a Pirate like yerself to do a little job for me. Maroon this scallywag.',
        'title': 'Maroon' },
    '19': {
        'stringAfter': 'Thanks for finding that rum. I owe ye one.',
        'stringBefore': 'I need a Pirate like yerself to do a little job for me. Search for some rum.',
        'title': 'Search For Rum' },
    '2': {
        'description': "Retrieve Sam's Key from a Navy soldier.",
        'stringAfter': 'My key! Thanks.',
        'stringBefore': 'One of those villainous Navy men stole a key of mine.\nCould you get it back for me?',
        'title': 'Treacherous Navy' },
    '20': {
        'stringAfter': 'Thanks for finding that rum. I owe ye one.',
        'stringBefore': 'I need a Pirate like yerself to do a little job for me. Search for some rum.',
        'title': "Search For Jolly's Rum" },
    '21': {
        'stringAfter': 'Thanks for defeating those Navy ships. I owe ye dearly.',
        'stringBefore': 'I need a Pirate like yerself to do a little job for me.',
        'title': 'Defeat Navy Ships' },
    '22': {
        'stringAfter': 'Thanks - I owe ye one.',
        'stringBefore': 'Doggerel Dan has joined the Navy. Capture him from a Navy ship.',
        'title': 'Capture Doggerel Dan' },
    '514': {
        'stringAfter': 'Gimme! Off ye go.',
        'stringBefore': 'Go get me stuff.',
        'stringDuring': 'Well, where is it?' },
    '515': {
        'stringBefore': 'Hi there!',
        'title': 'Help Friend' },
    'AttractingCustomers': {
        'description': 'Alexander Thayer has found that sales at his shop increase when pirates lose at the card tables. Win a huge amount of gold at poker and blackjack tables to stir up business.',
        'stringAfter': "That should do the trick, I may even have to keep the store open late.\x07I wonder how well you handle yourself with that pistol...\x07I have been looking for a pirate to catch people's attention for the sake of the shop.\x07My customers know you and will assume that your pistol came from my shop.\x07If other pirates notice your pistol skills, it might increase business a bit!",
        'title': 'Attracting Customers' },
    'BlackMack': {
        'description': 'Acquire a cheat card from Black Mack.',
        'reward': 'A Playing Card, Gold & Notoriety',
        'stringAfter': 'You are a card player!\x07... I suppose you still want your cheat card, eh?\x07Here you go. You best not try and use it against ole Mack.',
        'title': 'Cheat Card: Black Mack' },
    'BlackMarketInks': {
        'description': "Mecedes Corazon's customers have been asking about exotic inks that she cannot obtain legally. Assist her in acquiring some exotic ink for her shop.",
        'stringAfter': "Thank you again for your help.\x07My customers have been pouring in to get my exotic ink.\x07Not being responsible for Olivier's lost arm is also a plus.\x07Here is the special tattoo I promised you. Return to me whenever you want to put it on.",
        'title': 'Black Market Ink' },
    'BladeIngredients': {
        'description': 'John Wallace is crafting you a blade using the fine steel you brought him, all he needs now is for you to acquire some final ingredients to finish the job.',
        'stringAfter': "That will do it. I must say, this dagger is my finest work.\x07I have a small proposition for you, normally I would charge a bit of gold for the work I have done...\x07Unfortunately for me though, I have run into a bit of Navy trouble.\x07Let's just say I made some bad deals and now there are several warrants out for my arrest.\x07If you can recover them for me, then the dagger is yours.",
        'title': 'Finishing The Job' },
    'Chapter 1': {
        'title': 'Tutorial' },
    'Chapter 2': {
        'description': "Acquire a ship and learn to master her as soon as you can. Because a pirate who can't sail is nothing more than a landlocked landlubber too busy toiling away at life to actually live it!",
        'title': 'Story Quest: Set Sail' },
    'Chapter 3': {
        'description': 'Help Captain Jack Sparrow round up his crew and liberate the Black Pearl from a secret Navy outpost.',
        'title': 'Story Quest: The Black Pearl Crew' },
    'Chapter 4': {
        'description': 'The next story quest of the Pirates Online Retribution Adventure is on the way!',
        'title': 'Next Story Quest: Coming Soon!' },
    'Chapter1.rung1': {
        'title': 'Make A Pirate' },
    'Chapter1.rung2': {
        'description': "Get your sea chest from Doggerel Dan - the island's only bartender.",
        'title': 'Grab Your Sea Chest' },
    'Chapter1.rung3': {
        'description': "Get to the docks and find Captain Bo Beck - he'll get you off the island.",
        'title': 'Catch A Ship' },
    'ConstructDestructionSpell': {
        'description': "Gather the components for Tia's Relic Destruction Spell",
        'title': 'Acquire Components for Destruction Spell' },
    'ConstructLocationSpell': {
        'description': "Gather the components for Tia's Spell for Locating the Relic",
        'stringAfter': 'The relic taken from me has been broken up into many pieces.\x07The first piece may prove difficult to acquire. I can only tell you that Jolly Roger has trusted it to a skeleton gypsy.\x07Once you have the first piece, you will be drawn to the rest.\x07Return to me with all of the pieces. Perhaps the damage may be undone',
        'title': "Locating Tia's Relic" },
    'CrabClearOut': {
        'description': 'John Smith needs you to cleanup some of the pests on Driftwood Island. Defeat some Crabs and bring him back Crab Claws and Shells as proof.',
        'stringAfter': "I must say, this place is looking pretty good!\x07You should probably get back to the shop. I'm sure there is work for you there. Give Callecutter my best!",
        'title': 'Crab Cleanup' },
    'CutlassUnlockL5': {
        'description': "Utilize the secret of Spanish sword smithing to upgrade to 'Pirate Blade' cutlass.",
        'reward': '',
        'stringAfter': "Excellent work, mate. Here's yer sword.\x07 Be careful, eh? Don't want it fallin' into the wrong hands.",
        'title': 'Pirate Blade Upgrade: Spanish Smithing' },
    'DaggerUnlockL5': {
        'description': 'Ferrera needs your help to recover some stolen daggers.',
        'reward': '',
        'stringAfter': "Well done, my friend!\x07 You're sure to become the most notorious pirate in all the Caribbean.  Enjoy your reward.",
        'title': 'Bloodletter Upgrade: Stolen Daggers' },
    'DajinMingJewels': {
        'description': 'Dajin Ming has requested that you help him with some of his partners duties during his absence.',
        'reward': 'Jewelry',
        'stringAfter': 'I have to apologize, I did not think you would get this far.\x07Your efforts will ensure our place on this island.',
        'title': 'Helping Dajin Ming' },
    'DajinMingsCompetition': {
        'description': 'Dajin Ming has learned that EITC is helping someone open a new jewelry shop on Tortuga. Help him with his efforts to prevent it from opening.',
        'reward': 'Jewelry',
        'stringAfter': 'Hopefully they got the message. Your work here is done.\x07I hope this piece of jewelry is a fitting reward. Take care.',
        'title': "Dajin Ming's Competition" },
    'DarbyDrydocksTasks': {
        'description': 'Gather the components Darby needs for his new ship.',
        'reward': 'Gold',
        'stringAfter': 'Good doing business with you.',
        'title': "Darby Drydock's New Ship" },
    'DoubleCross2': {
        'animSetAfter': [
            None,
            65000],
        'description': "Many years ago, a Spanish Conquistador named El Patron used Padres del Fuego as a base camp to search the New World. He left on his journey with many unpaid debts. When El Patron didn't return, the townsfolk took the arms as payment. Not just any weapons, they were the finest collection of Spanish swords, Italian pistols and muskets in the world! Legend has it that whoever finds them will rule the Caribbean.",
        'stringAfter': "You work fast, mate. My boss wanted to personally thank you but...\x07He's a wee bit busy. Here's your reward. Now go...\x07...and say \x01slant\x01nothin' to nobody\x02, savvy?",
        'title': "El Patron's Lost Weapons" },
    'DoubleCrossA': {
        'description': "Captain Ezekiel Rott is the head of the Casa de Muertos clan that has just arrived on the shores of Port Royal. The guild is funded by a secretive, rich merchant from England who has a major interest in the Caribbean. Rumor has it they're a vile group of battled hardened men, banded in every civilized country on earth. So if you work with them, expect large gold rewards, but also... watch yer back!",
        'stringAfter': "HA! HA! That was easy!\x07Jolly good show. I should make ye me first mate!\x07Visit some other of me guild members when ye gets stronger.\x07They'll give ye more chores and more handsome payouts...\x07...if ye dare!",
        'title': 'Casa de Muertos Guild' },
    'DoubleCrossB': {
        'description': "Samuel Shaw is the First Mate of the Casa de Muertos Guild and Captain Rott's right-hand man. Help Shaw rid the island of some powerful voodoo relics and your legend - and gold stash - will grow quickly.",
        'stringAfter': "Oh, me-o-my, mate! The curse is about to be broken and me soul is lifted!\x07But don't stop yet, there's lots more relics to recover... and more gold.\x07Lots more. Savvy? Go see other guild members fer some more tasks if you haven't already done so.",
        'title': 'Port Royal Voodoo Relics' },
    'DoubleCrossC': {
        'description': "Bill Barrett is the half-wit cousin of Captain Rott. He's not the sharpest sword in the scabbard, but he's loyal and an excellent fighter. Help him find more of the voodoo relics and remember... he's almost always hungry.",
        'stringAfter': 'Well done, Billy is pleased and ye be even richer!',
        'title': 'Break Protection Curse' },
    'DoubleCrossD': {
        'description': "The Casa de Muertos Guild needs you to help them sabotage the Navy's defenses and distract them long enough so the guild can do their business on Port Royal.",
        'stringAfter': "Yer no fool, yer a stand up pirate, I'd say! Ye deserves such a big reward.",
        'title': 'Sabotage the Navy' },
    'DoubleCrossE': {
        'description': 'Thinning out the ranks of Navy ships will help the Casa de Muertos do their pirating more efficiently. Like any good pirate affair, eliminating anything that stands in the way of success - is vital.',
        'stringAfter': 'Excellent work, yes, yes indeed.\x07Yer gold is well deserved. If ye want to stay alive...\x07Stay out of our way when ye sees the signs. Savvy?\x07Yer no fool...\x07Ha, ha! Or are ye? Time will tell.',
        'title': 'Disrupt Navy Fleet' },
    'EITCManifests': {
        'description': 'For Callecutter to know where his needed materials can be found, Bingham has instructed you to recover EITC manifests and a diary from a mine on Port Royal named Royal Caverns.',
        'stringAfter': "I'll take that diary. I hope for your sake you didn't have a peek...\x07The EITC manifests you found will point Callecutter to the materials his shop needs.\x07I think we are done here. Leave now, please.",
        'title': 'Dirty Work' },
    'EITCShipments': {
        'description': "Manifests show that EITC ships sailing around the Caribbean contain the materials Callecutter's shop needs. Recover them for him.",
        'stringAfter': "That is about everything we need! I believe Callecutter almost has your shirt done.\x07Go check with Callecutter and see if there's anything else that he needs to finish.",
        'title': 'EITC Shipments' },
    'ErrandsForLuckyDeck': {
        'description': "In exchange for returning Nathaniel Truehound's lucky deck, William Turk wants you to retrieve fine rum, bone shavings and prison keys for him.",
        'stringAfter': "Alright, a deal's a deal, mate. Never had much luck with this deck anyhow.\x07Return it to Truehound. He'll be thrilled and maybe the deck will change his luck.",
        'title': 'Errands for a Lucky Deck' },
    'ExcentricTasks': {
        'description': 'Edward Shackleby has presented you with a scavenger hunt to prove your plundering prowess. Recover antique pistols, EITC manuals, rare feathers and compasses.',
        'stringAfter': 'Jolly good! A pirate has to be prepared to scavenge junk as well as precious plunder.\x07Visit Truehound and tell him, Edward Shackleby says, ye be a true pirate in my eyes.',
        'title': 'Excentric Plunder' },
    'ExtractionSpell': {
        'description': "Acquire the components for Roland's energy extraction spell",
        'stringAfter': 'The Orb clings to its strength. Its will is great. I will need a greater spell to achieve my purpose.\x07Gather these more potent components.',
        'title': 'Energy Extraction Spell' },
    'FathersDay2008': {
        'description': "Father's Day Quest",
        'stringDuring': 'Have you delivered the card yet?',
        'title': "Father's Day" },
    'FathersDay2008.1visitGiladoga': {
        'description': "Talk to Giladoga - He's a regular at the Ratskellar tavern on Padres del Fuego.",
        'stringAfter': "Err... Teague can have quite the temper. I would hate for 'im to find out who revealed his whereabouts. Perhaps ye could make it worth my while?\x07I'm in need of a few things. An Undead Witchdoctor took me favorite crab recipe.\x07Recover it for me, along with some o' that sweet crab meat, of course.",
        'stringBefore': "I'm glad ye be here. I could use yer services. Could ye deliver this card to Capt. Teague?\x07I be too busy and bein' that he's a foul mood most times, I'd rather not go me-self.\x07I'd like to keep this hush, hush... savvy?\x07So, let's just keep this fathers day card between us, ey? Well... best be off.\x07Oh, I forgot to mention... not quite sure where he is. Yer best bet is to talk to Giladoga. He might be able to point ye in the right direction.",
        'title': "Father's Day" },
    'FathersDay2008.2giladogaList': {
        'description': 'Giladoga knows where Capt. Teague is, but he needs some help from you before he reveals the location',
        'stringAfter': "Ahh, well, a deal's a deal. Capt. Teague is headin' to Driftwood Island. He's conductin' his yearly run to collect a few barrels of his\x07favorite drink; he has a secret stash there. Hired Bronze John to transport him and his cargo, he did",
        'title': 'Return to Giladoga' },
    'FathersDay2008.3visitBronzeJohn': {
        'description': 'Visit Bronze John',
        'stringAfter': "Hmm... I think I know the man you're referring to. Perhaps you could help me remember?",
        'title': 'Visit Bronze John' },
    'FathersDay2008t1.1RockCrabs': {
        'description': 'Collect three Rock Crabs',
        'title': 'Collect three Rock Crabs' },
    'FathersDay2008t1.2WitchDoctor': {
        'description': 'Defeat Undead Witchdoctor',
        'title': 'Defeat Undead Witchdoctor' },
    'FathersDay2008t2.1bribeBronzeJohn': {
        'description': 'Bribe Bronze John',
        'stringAfter': "Ahh.. Yes, I remember now; the scary looking bloke with the dreadlocks and a guitar. Unfortunate you missed him...\x07He was escorted away by some Navy lads. Quite the scene...\x07Luckily he paid me in advance for my services. I can only imagine what'll become of him. They left on a huge ship.\x07Don't know the name, but it was at a Frigate or Galleon. If you're going after him, you'll need some help.",
        'title': 'Bribe Bronze John' },
    'FathersDay2008t4.1sinkShips': {
        'description': 'Find the ship that arrested Capt. Teague. Optionally, use the crewing system to find some help.',
        'title': 'Find Navy Ship with Capt. Teague' },
    'FeatsOfStrength': {
        'description': "John Wallace won't sell any of his higher end daggers to just any pirate. Do what's necessary to prove yourself to him.",
        'stringAfter': "Perfect Timing! I just finished your dagger. Fine work I must say.\x07Thank you again for recovering the arrest warrants. Hopefully that was all of them.\x07Here's your dagger. Be careful out there.",
        'title': 'Coltello Upgrade: Feats of Strength' },
    'FurtherExtraction': {
        'description': 'Acquire the components for a more powerful extraction spell',
        'title': 'Potent Energy Extraction Spell' },
    'GamblingByChallenge': {
        'description': 'William Turk wants to see you risk your neck. Challenge the Navy and EITC as part of his test.',
        'stringAfter': "Well done! Gave those scurvy dogs a good thrashin', you did!\x07Now, return to Truehound the tailor, and he'll keep you on course to finish that outfit. Fair winds, mate!",
        'title': "Turk's Challenge" },
    'GamblingTasks': {
        'description': 'To prove your worth as a true pirate, William Turk wants you to win at blackjack and poker.',
        'stringAfter': "Cleaned 'em out you did!\x07If a pirate's worth be judged on card skills, you'd own half the Caribbean!\x07But there's more to great piratin' than cards\x07Gotta risk your neck too, so have a go at some Navy and EITC blokes, savvy?",
        'title': "Pirate's Play Cards" },
    'GarbageManTasks': {
        'description': 'Edward Stormhawk collects all kinds of junk. Retrieve the items he wants.',
        'stringAfter': "Ah, lovely! A fine addition to my collection.\x07Ye be a solid pirate in my book. Give Nathaniel Truehound me best. Fair sailin'.",
        'title': 'Garbage Man' },
    'GettingMckiddsAttention': {
        'description': 'Billy McKidd will not speak to you as he is busy watching card games. Win at poker and blackjack in order to catch his attention.',
        'stringAfter': "I must say I be impressed. Not many pirates handle themselves so well with a deck of cards.\x07Don't know why you be wasting your time with this book, but it's your life.\x07The rest of the pages are the few I found back when I be much like yourself.\x07Buried them around in safe places. Figured they'd be useful bargaining chips one day.\x07They don't mean much to me anymore. If you be willing to handle some of me work, you can have the rest of your silly book.\x07The Navy has been using me to keep some of the jungles safe. Seems that I can still handle a cutlass.\x07How about we make this interesting? I be a betting man.\x07Let's see you take care of this list using only your cutlass. Then you'll get your precious pages.",
        'title': "Getting McKidd's Attention" },
    'GettingRevenge': {
        'description': 'Dog Lockgrim has learned the identities of who is behind his shipwreck. They are currently residing in a cave on Tormenta Isle. Eliminate them all.',
        'stringAfter': "Good work mate! Hopefully those undead vermin have learned a lesson or two.\x07Maggie and I couldn't have done it without you.\x07Oh, Good news! I've heard from Adoria Dolores that she is finished with your belt. Go visit her.",
        'title': 'Getting Revenge' },
    'GoodForBusiness': {
        'description': 'Alexander Thayer has hired you to help with his shop duties that would normally require him to close up for the day.',
        'stringAfter': 'Thank you mate! My family will be thrilled to hear of the news.\x07I cleaned up one of my finest pistols for you, be careful, it will pack more of a punch then your old one.',
        'title': 'Tri-Barrel Upgrade: Good For Business' },
    'HelpingMercedesCorazon': {
        'description': "Mercedes Corazon's shop is in risk of being closed down. Her deed has been stolen and it's only a matter of time before she's thrown out. Help her track down her deed before it's too late.",
        'stringAfter': 'You recovered the deed! I cannot thank you enough.\x07I hope this tattoo is a fitting reward. Bless you!',
        'title': 'Helping Mercedes Corazon' },
    'IntroFeats': {
        'description': 'To exhibit your ability with a dagger, John Wallace wants you to prove your skills in combat. Defeat the listed enemies using your dagger.',
        'stringAfter': "You made quick work of that list. You must be quite capable with that dagger.\x07Imagine what you could do with one of my fine daggers?\x07You have proven to me that you're not just going to end up another dead pirate with a fancy dagger.\x07I am willing to craft you one of my masterpieces, though you will need to help a bit.\x07Some of the ingredients are hard to find to say the least.\x07To start, we will need to acquire some fine steel.\x07The only chap that I know of that still has some is Shochett Prymme. Visit him.",
        'title': 'Dagger Prowess' },
    'JewelerSmittyDebt': {
        'description': 'Jeweler Smitty has got himself in a bind with the Navy. Assist him with resolving his debts to them and he will reward you with some of his finest jewelry.',
        'reward': 'Jewelry',
        'stringAfter': 'My debts are gone? Well done my friend.\x07I wish I knew of more hard working pirates like you.\x07Here is the jewelry I promised, enjoy.',
        'title': 'Helping Jeweler Smitty' },
    'JosieMcReedyErrands': {
        'description': 'Help Josie McReedy Restock',
        'reward': 'Gold',
        'stringAfter': 'Thanks for the help, me darlin.',
        'title': "Josie McReedy's Restocking" },
    'KingHeadTeleport': {
        'description': '',
        'title': 'Secret of Kingshead Teleportation' },
    'LalaLovelsBrother': {
        'description': "Lala's brother, Slim, has failed to pay his debts to a man named Jack Redrat. Help slim out by paying off his debts with Redrat.",
        'stringAfter': "Thank you! Slim is not the smartest bloke around.\x07Think I'll handle his money for him from now on.\x07Here's the tattoo I promised you, come back whenever you want to put it on.",
        'title': "Lala's Brother" },
    'LostExplorers': {
        'description': "Dr. Bellrog heard that the door to El Patron's treasure will only open if you can obtain the four idols. Search the area around you for clues so you can help Dr. Bellrog and find the treasure.",
        'title': 'Lost Explorers' },
    'LovelsNeighbor': {
        'description': "Lala Lovel has gotten complaints about some tattoos she gave using a batch of bad ink. The ink caused illness and nasty infections for her customers, and now they're angry. Lala is losing business and will give you a rare tattoo if you can satisfy their complaints.",
        'stringAfter': "Finally, they've been running off new customers for months.\x07Thanks to you, maybe I get to business now.\x07Here's the rare tattoo I promised you.\x07Visit my store if you ever want to put it on.",
        'title': "Lala's Bad Ink" },
    'LucindaErrands': {
        'description': 'Gather ingredients for Lucinda.',
        'reward': 'Gold',
        'stringAfter': 'You have done well. Thank you.',
        'title': "Lucinda's Ingredients" },
    'MainStory': {
        'description': "The Black Pearl's been confiscated by the Navy and hidden. The Pearl's more than a ship but a symbol of the freedom pirates everywhere embody... and Jack needs your help to find his crew and recapture her. No easy task. Besides battling Jolly's undead army, the Navy's trying to impose order and taxes! Even worse, the East Inda Trading Company (EITC) has a brutal, private army to maintain their grip on trade. It's the end of the Golden Age of Pirates and Sparrow's calling on all brigands, buccaneers and pirates to keep the Caribbean wild & free... forever!",
        'stringAfter': "The veritable hero of the hour returns, having liberated the Pearl from the Navy's nefarious clutches.\x07As a token of my gratitude, I am prepared to offer a gift of substantial value...\x07A promotion...in my estimation of you. It seems I sold you short, eh mate?\x07And now... everyone! Raise your glasses to the pirate who made the Pearl free once again!\x07I'm sure these gentlemen will appreciate your generosity...\x07...and for my part, I look forward to working with you again when the opportunity presents itself.",
        'title': 'The Liberation of the Black Pearl' },
    'MercJob1': {
        'description': 'Perform this task for Josie and be kindly rewarded.',
        'reward': 'Gold',
        'title': 'Work For Hire: Defeat Enemies' },
    'MercJob2': {
        'description': 'Perform this task for Josie and be kindly rewarded',
        'reward': 'Gold',
        'title': 'Work For Hire: Defeat Naval Vessels' },
    'MercJob3': {
        'description': 'Perform this task for Johnny and be kindly rewarded',
        'reward': 'Gold',
        'title': 'Johnny McVane Work For Hire' },
    'MercJob4': {
        'description': 'Perform this task for Johnny and be kindly rewarded',
        'reward': 'Gold',
        'title': 'Johnny McVane Work For Hire' },
    'MercJobEM': {
        'description': 'Perform this task for Captain Job and be kindly rewarded.',
        'reward': 'Gold',
        'stringAfter': "Good work! Here's your payment.",
        'title': 'Work For Hire: Defeat Enemies' },
    'OQA.defeatBrinescum': {
        'description': 'Dog Lockgrim has learned the identities of who is behind his shipwreck. Two of them are Brinescums currently residing in a cave on Tormenta Isle. Eliminate them.',
        'title': 'Brinescum Battle' },
    'OQA.defeatFlotsam': {
        'description': 'Dog Lockgrim has learned the identities of who is behind his shipwreck. Two of them are Flotsams currently residing in a cave on Tormenta Isle. Eliminate them.',
        'title': 'Finding Flotsam' },
    'OQA.defeatKelpbrain': {
        'description': 'Dog Lockgrim has learned the identities of who is behind his shipwreck. Two of them are Kelpbrains currently residing in a cave on Tormenta Isle. Eliminate them.',
        'title': 'Kelpbrain Kill' },
    'OQA.defeatNavyGuards': {
        'description': "Defeat Navy Veterans so that they'll leave Valentina alone. You can find them patrolling around Fort Dundee on Padres Del Fuego.",
        'stringAfter': "Maybe now they'll leave me alone! I have work to do!\x07An order for a very important client needs to go out and I need some materials that're hard to get.\x07Cursed wood is an essential ingredient for the chest I'm making. It must be perfect!\x07You can get some from undead skeleton ships sailing around the Caribbean. Don't return without it!",
        'title': 'A Message to the Navy' },
    'OQA.defeatSpikeskull': {
        'description': 'Dog Lockgrim has learned the identities of who is behind his shipwreck. Two of them are Spineskulls currently residing in a cave on Tormenta Isle. Eliminate them.',
        'title': 'Spineskull Search' },
    'OQA.deliverChest': {
        'description': "Valentina has made a chest for Captain Barbossa and she needs you to deliver it. He can be found in a cave on Devil's Anvil.",
        'stringAfter': "A fine cursed chest this is! Valentina continues to impress me.\x07She must think highly of ye to entrust ye with me chest.\x07Here's a hat of mine to show me gratitude. Ye won't be findin' these in any tailor 'round these parts.\x07Take care, mate. Give Valentina me love, ey.",
        'title': 'A Chest for Captain Barbossa' },
    'OQA.deliverCompass': {
        'description': "Maggie Rigrage's dullard of a husband, Dog LockGrim, has managed to keep them stranded on Outcast Isle. Deliver a compass to him for Adoria Dolores.",
        'stringAfter': "Thanks mate! I can't tell you how helpful this will be. We didn't stand a chance without it!\x07Maggie and I are beginning to believe our shipwreck was sabotage.\x07A friend of mine swears he knows who's behind this. He even sent me a letter explaining it all but I've lost it!\x07Don't tell Maggie. She's mad enough as is. You have to recover it for me!\x07I saw a dread scorpion carrying it. Get the letter back, please!",
        'title': 'Still Stranded' },
    'OQA.deliverKrakenCloth': {
        'description': 'Romany Bev wants you to deliver a piece of kraken cloth to Adoria Dolores.',
        'stringAfter': "Fresh Kraken cloth! Romany Bev always manages to get some. I wish she'd tell me where, though.\x07That hat Captain Barbossa gave you must be impressive. You know, there's more to that outfit of his.\x07I can help you recreate the rest of the outfit if you don't mind helping me out with a few more things.\x07We'll start with the shirt and vest. I'll just need your help acquiring some of the more hard to find ingredients.\x07Recover some cursed buttons, bone dust, hides and cursed bark to start. All can be found on Padres Del Fuego.",
        'title': 'Kraken Cloth' },
    'OQA.deliverRumBarrel': {
        'description': 'Adoria Dolores owes a bit of rum to her distant cousin Gunner. Deliver what she has to him. Gunner can be found in his shack on Padres del Fuego.',
        'stringAfter': "ME HEARIN' MAY BE BAD, MATE, BUT I CAN SEE THIS AIN'T GONNA BE ENOUGH! COUSIN OR NOT... \x07ADORIA OWES ME A LARGE STASH OF RUM\x07YER GONNA HAVE TO GATHER THE REST 'CAUSE I CAN'T BE LEAVIN' ME SHACK. TOO RISKY.\x07GET WHAT YE CAN FROM EITC SHIPS AND THE REST FROM SOME OF THOSE NAVY SWINE!",
        'title': 'Rum for Gunner' },
    'OQA.deliverTentacles': {
        'description': 'Deliver the tentacles Adoria Dolores needs to finish your boots.',
        'title': "Barbossa's Boots" },
    'OQA.deliverVoodooArtifact': {
        'description': "Valentina has found one of Romany Bev's voodoo artifacts that went missing. Deliver it to Romany Bev. She can be found around the corner from Valentina on Padres Del Fuego.",
        'stringAfter': "I still suspect Valentina has something to do with all of this!\x07Her story of finding one of the artifacts washed up on the shore right after they went missing. Smells a bit fishy to me.\x07According to Valentina, the rest of my artifacts are in the hands of EITC and Navy ships.\x07Bring them back to me. I can't be separated from them for much longer!",
        'title': 'Lost Artifacts' },
    'OQA.playBlackjack': {
        'description': 'Morris has lost everything at the card tables to cheats. Get some revenge for Morris by winning at the blackjack tables.',
        'title': 'Blackjack Revenge' },
    'OQA.playPoker': {
        'description': 'Morris has lost everything at the card tables to cheats. Get some revenge for Morris by winning at the poker tables.',
        'title': 'Poker Revenge' },
    'OQA.recoverBoneDust': {
        'description': "To create the rest of Barbossa's outfit, Adoria Dolores needs you to recover some skeleton bone dust.",
        'title': 'Bone Dust' },
    'OQA.recoverButtons': {
        'description': "To create the rest of Barbossa's outfit, Adoria Dolores needs you to recover some cursed buttons from skeletons.",
        'title': 'Cursed Buttons' },
    'OQA.recoverCursedBark': {
        'description': "To create the rest of Barbossa's outfit, Adoria Dolores needs you to recover some cursed bark from stumps.",
        'title': 'Cursed Bark' },
    'OQA.recoverCursedCloth': {
        'description': 'To finish your shirt and vest, Adoria Dolores needs you to acquire cursed cloth from skeleton ships.',
        'title': 'Cursed Cloth' },
    'OQA.recoverCursedNeedles': {
        'description': 'To finish your shirt and vest, Adoria Dolores needs cursed needles from high level skeletons.',
        'stringAfter': "Here's your new shirt and vest I promised. I hope they match the hat.\x07The funny thing about a promise is that sometimes people don't honor them.\x07From what Romany Bev tells me, Valentina still hasn't closed her shop!\x07I trusted you to handle this situation mate. I can't help you out with anymore of this outfit until this is handled for good.\x07Go speak to Valentina. Maybe you can talk some sense into her.",
        'title': 'Cursed Needles' },
    'OQA.recoverCursedThreads': {
        'description': 'To finish your shirt and vest, Adoria Dolores needs you to acquire cursed thread from skeleton ships.',
        'title': 'Cursed Thread' },
    'OQA.recoverCursedWood': {
        'description': 'Valentina needs some cursed wood to create a chest for her most important client. Recover some from undead skeleton ships sailing around the Caribbean.',
        'stringAfter': "This will work! I've never produced such a fine chest.\x07I'll need you to help me out with one more thing before I move my shop.\x07I need you to deliver this chest to a very important client. His name is Captain Barbossa.\x07Perhaps you've heard of him? Hopefully I don't need to remind you to keep this quiet, mate!\x07If you're lucky he may even give you a tip. He's been known to do that in the past.\x07You can find him in a cave on Devil's Anvil. Hurry! I don't want to keep him waiting.",
        'title': 'Cursed Wood' },
    'OQA.recoverFamilyHeirloomsA': {
        'description': 'Maggie Rigrage needs some help gathering her family heirlooms. Some have been picked up by nearby Navy ships. Recover them.',
        'title': 'Navy Heirlooms' },
    'OQA.recoverFamilyHeirloomsB': {
        'description': 'Maggie Rigrage needs some help gathering her family heirlooms. Some have been picked up by nearby EITC ships. Recover them.',
        'title': 'EITC Heirlooms' },
    'OQA.recoverFamilyHeirloomsC': {
        'description': 'Maggie Rigrage needs help gathering her family heirlooms. Some of the heirlooms have been picked up by nearby Skeleton ships. Recover them.',
        'title': 'Skeleton Heirlooms' },
    'OQA.recoverFamilyHeirloomsD': {
        'description': 'Maggie Rigrage needs you to acquire the rest of her family heirlooms. She suspects some have been picked up by stumps.',
        'title': 'Stump Heirlooms' },
    'OQA.recoverFamilyHeirloomsE': {
        'description': 'Maggie Rigrage needs you to acquire the rest of her family heirlooms. She suspects some have been picked up by dread scorpions.',
        'title': 'Dread Scorpion Heirlooms' },
    'OQA.recoverFlyTrapRoots': {
        'description': 'Olivier needs you to recover roots from fly traps as part of his remedy.',
        'title': 'Fly Trap Roots' },
    'OQA.recoverGatorSaliva': {
        'description': 'Olivier needs you to recover saliva from big alligators as part of his remedy.',
        'title': 'Gator Saliva' },
    'OQA.recoverHides': {
        'description': "To create the rest of Barbossa's outfit, Adoria Dolores needs you to recover some dread scorpion hides.",
        'title': 'Scorpion Hides' },
    'OQA.recoverLockgrimsLetter': {
        'description': "Dog Lockgim has lost a letter containing information about who's behind he and Maggie's shipwreck.",
        'stringAfter': "You found it! Hope Maggie didn't see you scurrying about the island. I'm in deep enough waters with her.\x07The letter points out the pests that're behind all this. Supposedly they're hold up in a cave on Isla Tormenta.\x07Eliminate them for me and Maggie. Once we get off this rock we don't want to tangle with them again!",
        'title': "Lockgrim's Mistake" },
    'OQA.recoverNavyChestKeys': {
        'description': 'The Navy chests you recovered are locked. Recover the keys for Adoria Dolores from high level Navy guards.',
        'stringAfter': "Didn't have any luck opening the chests on my own. Thankfully you found the keys!\x07With these I can get started on your boots. There's one more ingredient we'll need, though.\x07I've heard stories that those who seek it often don't come back...\x07If you want an authentic version of Barbossa's outfit, it's a must. We'll need a good amount of fresh tentacles.\x07Go speak to Shochett Prymme. He can be found near his shop on Padres. He'll know where to get them.",
        'title': 'Navy Keys' },
    'OQA.recoverNavyChests': {
        'description': 'Adoria Dolores needs some rare ingredients that are being hoarded by the Navy. Recover chests from Navy ships sailing around the Caribbean.',
        'stringAfter': "They're locked! Curse those Navy bilge rats! We'll have to recover the keys as well.\x07Most Navy men should have a key to open one of these chests.\x07Recover the keys for me while I try to open them the hard way.",
        'title': 'Navy Hoarding' },
    'OQA.recoverRottenMeat': {
        'description': 'Olivier needs you to recover rotten meat from skeletons as part of his remedy.',
        'title': 'Rotten Meat' },
    'OQA.recoverRumBarrels': {
        'description': 'Gunner needs you to get the rest of the rum Adoria Dolores owes him. Gather barrels of rum from EITC ships sailing around the Caribbean.',
        'title': 'Barrels of Rum' },
    'OQA.recoverRumBottles': {
        'description': 'Gunner needs you to get the rest of the rum Adoria Dolores owes him. Gather bottles of rum from high level Navy guards.',
        'title': 'Bottles of Rum' },
    'OQA.recoverShopApplication': {
        'description': "Recover a shop application for Valentina's shop. It should be hidden in a container somewhere in Fort Dundee on Padres Del Fuego.",
        'stringAfter': "Rubbish! I can't believe she was able to open her shop.\x07You're going to have to go talk to her. See if you can get her to close down her shop or at least move it!",
        'title': "Valentina's Application" },
    'OQA.recoverTentaclesA': {
        'description': 'To finish your boots, Adoria Dolores needs you to gather tentacles from Seabeards.',
        'title': 'Seabeard Tentacles' },
    'OQA.recoverTentaclesB': {
        'description': 'To finish your boots, Adoria Dolores needs you to gather tentacles from Molusks.',
        'title': 'Molusk Tentacles' },
    'OQA.recoverTentaclesC': {
        'description': 'To finish your boots, Adoria Dolores needs you to gather tentacles from Urchinfists.',
        'title': 'Urchinfist Tentacles' },
    'OQA.recoverUrchinfistEye': {
        'description': 'As payment for his information, Shochett Prymme wants you to bring him an eye from an Urchinfist.',
        'title': 'Eye of Urchinfist' },
    'OQA.recoverVoodooArtifactsA': {
        'description': "Some of Romany Bev's voodoo artifacts have been stolen by EITC ships. Recover them from EITC ships sailing around the Caribbean.",
        'title': 'EITC Theft' },
    'OQA.recoverVoodooArtifactsB': {
        'description': "Some of Romany Bev's voodoo artifacts have been stolen by Navy ships. Recover them from Navy ships sailing around the Caribbean.",
        'title': 'Navy Theft' },
    'OQA.visitAdoriaDolores': {
        'description': "To show her appreciation, Adoria Dolores has created a coat for your outfit. Visit her, she's expecting you.",
        'stringAfter': "I hope this coat is a fitting reward for your efforts. My family is grateful.\x07You almost have Barbossa's entire outfit now. Just a few more items to go.\x07Luckily, I have a few more family members that could use your help.\x07One of them is my cousin Morris. He can normally be found drowning his sorrows in the Ratskellar tavern... \x07on Padres, please help him.",
        'title': "Barbossa's Coat" },
    'OQA.visitAdoriaDoloresB': {
        'description': "Return to Adoria Dolores now that you've helped her cousin Morris.",
        'stringAfter': "That bloke Morris is pretty useless, eh? Family is family, though.\x07This next chap is a... distant cousin of mine. His name is Gunner.\x07I owe him a bit of rum. Actually a lot of rum. Bring this to him, it's all I have. Hopefully it will be enough.\x07You can find Gunner in his shack on Padres Del Fuego.",
        'title': 'Cousin Avenged' },
    'OQA.visitAdoriaDoloresC': {
        'description': 'Inform Adoria Dolores that she no longer owes Gunner any rum.',
        'stringAfter': "Gunner's a good chap even if he is half-deaf.\x07I'm just about to start on your pants. Captain Barbossa will be jealous!\x07While I'm working on that I could use your help again. Another one of my relatives needs a hand.\x07His name is Olivier. He's been sick for quite some time and he needs to find a remedy fast!\x07Olivier can normally be found loitering 'round the docks in Padres Del Fuego.",
        'title': 'The Rum Is Gone' },
    'OQA.visitAdoriaDoloresD': {
        'description': 'Adoria Dolores has finished your new pair of pants. Visit her to claim them.',
        'stringAfter': "Thank you for helping Olivier. I hope you didn't catch anything from him.\x07I've just finished your pants! They should be a perfect fit. Only a belt and a pair of boots to go!\x07After that there's nothing more for me to bribe you with. I'll have to get the most out of what's left.\x07Sadly, Maggie Rigrage's woes continue. Her dullard of a husband, Dog Lockgrim, has managed to keep them stranded on that beastly island.\x07Deliver this compass to Dog Lockgrim on Outcast Isle. Meanwhile, I'll be working on your belt.",
        'title': 'A New Pair of Pants' },
    'OQA.visitAdoriaDoloresE': {
        'description': 'Adoria Dolores has finished your new belt. Go visit her in her tailor shop on Padres Del Fuego.',
        'stringAfter': "My family can be quite a handful! I cannot thank you enough.\x07I hope this belt shows my deep appreciation. Only a pair of boots left!\x07Thankfully, I'm fresh out of pesky family members for you to help. Making these boots won't be a walk in the park though.\x07They call for some rare ingredients. Only the best for Captain Barbossa, of course.\x07These ingredients are horded by the Navy. One way or another, we need to get them.\x07You're sure to find what we need in chests smuggled throughout the Caribbean by the Navy.\x07Recover these chests from Navy ships. I'll be waiting for you...",
        'title': 'A Better Belt' },
    'OQA.visitMaggieRigrage': {
        'description': 'Romany Bev and Adoria Dolores need you to help out with another one of their needy family members. Maggie Rigrage can be found on Outcast Isle. Go visit her.',
        'stringAfter': "I'm so thankful! It's been ages since I've seen a new face here.\x07My husband and I washed up on this island some time ago.\x07Our ship sank along with all of our family heirlooms! We've been searching for them ever since.\x07We fear the rest has been scavenged by nearby ships. See if you can recover what's been picked up by ships sailing nearby.",
        'title': 'Maggie Is Stranded' },
    'OQA.visitMorris': {
        'description': 'Adoria Dolores has another family member in need. Visit her cousin Morris. He can be found in Ratskellar on Padres Del Fuego.',
        'stringAfter': "I've lost everything! Those scurvy dogs cleared me out!\x07They cheated... I know it! What I wouldn't give to see someone give them a taste of their own medicine!\x07You look like you'd be quite dangerous with a deck of cards.\x07Show them they're not the only card sharps around here!",
        'title': 'Helping Morris' },
    'OQA.visitOlivier': {
        'description': 'Adoria Dolores needs you to help out her relative Olivier. Olivier has been sick for quite some time and needs to find a remedy. Visit Olivier by the docks in Padres Del Fuego.',
        'stringAfter': "I'd stand back a few steps mate. I've managed to catch something awful.\x07Unfortunately you can't just buy what I need off of a shelf.\x07I know the ingredients I need to make the remedy at least.\x07Would you mind gathering these for me? I barely have the strength to stand to be honest.",
        'title': 'A Remedy for Olivier' },
    'OQA.visitRomanyBev': {
        'description': 'Adoria Dolores is overwhelmed running her shop and needs some help with her family. Visit her sister Romany Bev. She can be found on Padres Del Fuego.',
        'stringAfter': "Adoria has a lot on her plate these days, so... \x07I'm glad she sent you, though. Another shopkeeper has been encroaching on my business.\x07Valentina has decided to open up a shop right around the corner!\x07I find it hard to believe that wench was able to even get a permit for that pathetic excuse for a shop.\x07See if you can find her shop application. It should be hidden somewhere in a container in Fort Dundee on Padres Del Fuego.",
        'stringBefore': "My family is quite a handful. Between them and the shop, I barely have any time to myself these days!\x07I'll assume you don't want to help out around here. Pirates tend to have a bit of difficulty with a needle and thread.\x07You could help me out with my family, though. I'm sure I can repay you in some way.\x07My sister, Romany Bev the Gypsy, seems to have some problems with another local shop. She is located on Padres Del Fuego. Go visit her.",
        'title': "Adoria's Family" },
    'OQA.visitRomanyBevB': {
        'description': "Valentina has promised to move her shop away from Romany Bev's shop. Visit Romany Bev and inform her of this.",
        'stringAfter': "She'll move her shop? Good work. I didn't think she'd budge.\x07Maybe now she'll stop stealing my customers.\x07I'll be sure to tell Adoria Dolores of how helpful you've been.\x07Deliver this Kraken cloth to her for me. She's expecting it.",
        'title': "Valentina's Promise" },
    'OQA.visitRomanyBevC': {
        'description': 'Maggie Rigrage has all of the family heirlooms she was looking for. Return to Romany Bev to find out what you should do next.',
        'stringAfter': 'Thanks mate! Maggie was in dire need of some assistance.\x07Adoria Dolores has sent word that she has finished your coat.\x07Visit her to claim your reward!',
        'title': 'Heirlooms Found' },
    'OQA.visitShochett': {
        'description': 'To finish your boots, Adoria Dolores needs you to gather fresh tentacles. Go speak to Shochett Prymme about where to find some. He can be found near his shop on Padres Del Fuego.',
        'stringAfter': "I don't get asked for tentacles very often...\x07These days it's not worth the risk. But if you're willing to risk your neck, some can still be found.\x07They must be gathered from some dangerous pests infesting a cave on Isla Tormenta.\x07I'll provide you with a list of targets if you bring me back something I desire while you're there.\x07Bring me back an Urchinfist eye. If you don't get killed trying...",
        'title': 'Fresh Tentacles' },
    'OQA.visitValentina': {
        'description': 'Romany Bev wants you to talk to Valentina about closing her shop. She is located around the corner from Romany Bev on Padres Del Fuego.',
        'stringAfter': "Romany Bev doesn't own Padres Del Fuego! Last time I checked no one even goes to her shop.\x07You're going to have to make it well worth my time if you want me gone.\x07To start, Romany Bev has been quite friendly with some Navy chaps. She's managed to pit them against me.\x07Now I find myself being followed by them even when I'm not at my shop!\x07Send them a message for me so they'll leave me alone. You can find them in Fort Dundee on Padres Del Fuego.",
        'title': 'Close Competition' },
    'OQA.visitValentinaB': {
        'description': "Even though she promised, Valentina still hasn't closed her shop. Go speak to her and see why she broke her promise to Romany Bev.",
        'stringAfter': "To be honest, I never had any intention of keeping that promise. Romany Bev has no right to put me out of business!\x07We used to be friends until Romany Bev accused me of being a thief!\x07She had a collection of voodoo artifacts that went missing and she's accusing me. I'm no thief!\x07I was able to find one of them. It washed up on shore one morning. My guess is that EITC and Navy ships have picked up the rest.\x07Romany Bev can have the one voodoo artifact I have. Deliver it to her.",
        'title': 'Broken Promises' },
    'OQA.visitValentinaC': {
        'description': "Return to Valentina now that you've acquired Captain Barbossa's hat.",
        'stringAfter': "Thank you mate! It's lovely having someone to do my deliveries.\x07You can inform Romany Bev that I'll move my shop if it bothers her that much. I promise...",
        'title': "Barbossa's Thanks" },
    'OQB.challengingEITC': {
        'description': 'William Turk wants to see you risk your neck. Challenge some EITC guards as part of his test.',
        'title': 'EITC Challenge' },
    'OQB.challengingEITCShips': {
        'description': 'William Turk wants to see you risk your neck. Challenge some EITC ships as part of his test.',
        'title': 'EITC Ship Challenge' },
    'OQB.challengingNavy': {
        'description': 'William Turk wants to see you risk your neck. Challenge some Navy guards as part of his test.',
        'title': 'Navy Challenge' },
    'OQB.challengingNavyShips': {
        'description': 'William Turk wants to see you risk your neck. Challenge some Navy ships as part of his test.',
        'title': 'Navy Ship Challenge' },
    'OQB.defeatAlligators': {
        'description': 'As part of your final challenge, Will Turner wants you to defeat alligators.',
        'title': 'Pesky Alligators' },
    'OQB.defeatBats': {
        'description': 'As part of your final challenge, Will Turner wants you to defeat bats.',
        'title': 'Pesky Bats' },
    'OQB.defeatCrabs': {
        'description': 'As part of your final challenge, Will Turner wants you to defeat crabs.',
        'title': 'Pesky Crabs' },
    'OQB.defeatEITC': {
        'description': 'As part of your next challenge, Will Turner wants you to defeat EITC guards.',
        'title': 'EITC Guards' },
    'OQB.defeatEITCShipsB': {
        'description': 'As part of his final challenge, Darby Drydock wants you to take down a large amount of EITC ships.',
        'title': 'EITC Takedown' },
    'OQB.defeatNavy': {
        'description': 'As part of your next challenge, Will Turner wants you to defeat Navy guards.',
        'title': 'Navy Guards' },
    'OQB.defeatNavyShips': {
        'description': 'For his first challenge, Will Turner wants you to take down some Navy ships sailing around the Caribbean.',
        'stringAfter': "Fine work, indeed. Now, here's the challenge I've concocted that's fitting a pirate like yourself.\x07Let's start with some basics; take down some Navy Guards, some EITC guards and skeletons.\x07Watch your back, don't want that new shirt to get bloody, do we?",
        'title': 'Overpriced Ships' },
    'OQB.defeatNavyShipsB': {
        'description': 'As part of his final challenge, Darby Drydock wants you to take down a large amount of Navy ships.',
        'title': 'Navy Takedown' },
    'OQB.defeatScorpions': {
        'description': 'As part of your final challenge, Will Turner wants you to defeat scorpions.',
        'title': 'Pesky Scorpions' },
    'OQB.defeatSkeleton': {
        'description': 'As part of your next challenge, Will Turner wants you to defeat skeletons.',
        'title': 'Skeletons' },
    'OQB.defeatWasps': {
        'description': 'As part of your final challenge, Will Turner wants you to defeat wasps.',
        'title': 'Pesky Wasps' },
    'OQB.deliverLuckyDeckToNathaniel': {
        'description': "William Turk has agreed to give Nathaniel Truehound his lucky deck. Deliver Turk's lucky deck to Nathaniel Truehound.",
        'stringAfter': "Me lucky deck! Never thought I'd see it again. Many thanks, mate.\x07Here's your hat. Should be a good start to that new outfit so fittin' a good pirate.\x07Now go visit Will Turner at his warehouse on Port Royal.\x07He'll help find a proper pirate shirt for you.",
        'title': 'Lucky Deck Delivery' },
    'OQB.makeBlackjackMoney': {
        'description': 'To prove your worth as a true pirate, William Turk wants you to win at poker.',
        'title': 'Pirate Poker' },
    'OQB.makePokerMoney': {
        'description': 'To prove your worth as a true pirate, William Turk wants you to win at blackjack.',
        'title': 'Pirate Blackjack' },
    'OQB.recoverBoneShavings': {
        'description': "In exchange for returning Nathaniel Truehound's lucky deck, William Turk wants you to retrieve bone shavings from skeletons for him.",
        'title': 'Bone Shavings for Turk' },
    'OQB.recoverFineRum': {
        'description': "In exchange for returning Nathaniel Truehound's lucky deck, William Turk wants you to retrieve fine rum from EITC ships for him.",
        'title': "Turk's Fine Rum" },
    'OQB.recoverPrisonKey': {
        'description': "In exchange for returning Nathaniel Truehound's lucky deck, William Turk wants you to retrieve prison keys from Navy guards for him.",
        'title': "Turk's Prison Keys" },
    'OQB.retrieveAntiquePistol': {
        'description': "As part of Edward Shackleby's test, he wants you to recover antique pistols from EITC ships.",
        'title': 'Pistol Plunder' },
    'OQB.retrieveBatGuanoFromBats': {
        'description': 'To finish his work for the day, Bartholomew needs you to acquire some guano from bats.',
        'title': 'Bat Guano' },
    'OQB.retrieveBileFromScorpions': {
        'description': 'To finish his work for the day, Bartholomew needs you to acquire some bile from scorpions.',
        'title': 'Scorpions Bile' },
    'OQB.retrieveClothFromNavyShip': {
        'description': 'As part of his final challenge, Nathaniel Truehound wants you to recover cloth from Navy ships for him.',
        'title': 'Cloth from Navy Ships' },
    'OQB.retrieveCoinBagsFromEITCGuards': {
        'description': 'As part of his final challenge, Nathaniel Truehound wants you to recover coin bags from EITC guards for him.',
        'title': 'Coin Bags from EITC Guards' },
    'OQB.retrieveCompass': {
        'description': "As part of Edward Shackleby's scavenger test, he wants you to recover compasses from Navy guards.",
        'title': 'Compass Plunder' },
    'OQB.retrieveCottonFromEITCShip': {
        'description': 'As part of his final challenge, Nathaniel Truehound wants you to recover cotton from EITC ships for him.',
        'title': 'Cotton from EITC Ships' },
    'OQB.retrieveCursedSailClothFromUndead': {
        'description': 'To finish his work for the day, Bartholomew needs you to acquire some cursed sail cloth.',
        'title': 'Cursed Sail Cloth' },
    'OQB.retrieveEITCEmptyFlasks': {
        'description': "As part of Edward Stormhawk's list of junk, he wants you to collect EITC empty flasks from EITC ships.",
        'title': 'EITC Empty Flasks' },
    'OQB.retrieveEITCManual': {
        'description': "As part of Edward Shackleby's scavenger test, he wants you to recover manuals from EITC guards.",
        'title': 'EITC Plunder' },
    'OQB.retrieveEITCParchment': {
        'description': "As part of Edward Stormhawk's list of junk, he wants you to collect EITC parchments from EITC soldiers.",
        'title': 'EITC Parchment' },
    'OQB.retrieveFabricFromNavyGuards': {
        'description': 'As part of his final challenge, Nathaniel Truehound wants you to recover fabric from Navy guards for him.',
        'title': 'Fabric from Navy Guards' },
    'OQB.retrieveGatorSalivaFromGators': {
        'description': 'To finish his work for the day, Bartholomew needs you to acquire some saliva from alligators.',
        'title': 'Gator Saliva' },
    'OQB.retrieveNavyAnchors': {
        'description': "As part of Edward Stormhawk's list of junk, he wants you to collect Navy anchors from Navy ships.",
        'title': 'Navy Anchors' },
    'OQB.retrieveNavyShoeStrings': {
        'description': "As part of Edward Stormhawk's list of junk, he wants you to collect Navy shoestrings from Navy guards.",
        'title': 'Navy Shoestrings' },
    'OQB.retrievePlanksFromNavyShips': {
        'description': "As part of Darby Drydock's challenge, he wants you to retrieve planks from Navy ships.",
        'title': 'Planks from Navy Ships' },
    'OQB.retrieveRareFeather': {
        'description': "As part of Edward Shackleby's scavenger test, he wants you to recover rare feathers from Navy ships.",
        'title': 'Rare Feather Plunder' },
    'OQB.retrieveSailsFromEITCShips': {
        'description': "As part of Darby Drydock's challenge, he wants you to retrieve sails from EITC ships.",
        'title': 'Sails from EITC Ships' },
    'OQB.retrieveThreadFromUndead': {
        'description': 'As part of his final challenge, Nathaniel Truehound wants you to recover thread from skeletons for him.',
        'title': 'Thread from Skeletons' },
    'OQB.retrieveVenomFromWasps': {
        'description': 'To finish his work for the day, Bartholomew needs you to acquire some venom from wasps.',
        'title': 'Wasp Venom' },
    'OQB.retrieveWheelFromUndeadShips': {
        'description': "As part of Darby Drydock's challenge, he wants you to retrieve ship wheels from skeleton ships.",
        'title': 'Wheels from Skeleton Ships' },
    'OQB.visitBartholomewWatkins': {
        'description': 'While Nathaniel Truehound finishes your new pair of shoes, he wants you to help his friend Bartholomew Watkins. Visit Bartholomew outside a shop on Port Royal.',
        'stringAfter': "I be hearin' good things about ye from me old shipmate, Nathaniel. Thanks for helpin'.\x07If I don't recover some of these stolen items, I'll lose me job, or me head!\x07Here's what I need: some cursed sail cloth, scorpion bile, wasp venom, bat guano and gator spit.\x07All in a day's work, ey mate?",
        'title': 'Helping Batholomew' },
    'OQB.visitDarbyDryDock': {
        'description': 'Your next challenge will revolve around your skills on the high seas. Visit Darby Drydock to receive your first challenge.',
        'stringAfter': "So, ye call yerself a sailor, ey?  Not in my book.\x07Gotta prove yer skills to me by gatherin' a list of items from Navy ships, EITC ships and those dreadful skeleton ships.\x07Got the stomach for it? Excellent. Good luck.",
        'title': "Darby Drydock's Challenge" },
    'OQB.visitEdwardShackleby': {
        'description': "Visit Edward Shackleby for your next challenge. He can by found on a bench outside the Governor's Mansion.",
        'stringAfter': "A true pirate plunders not just gold and jewels but...\x07all sorts of valuable things others might overlook, like antique pistols, a soldier's manual, exotic feathers and a fine compass.\x07Plunder these and I'll help ye finish yer quest.",
        'title': 'Plundering for Shackleby' },
    'OQB.visitEdwardStormhawk': {
        'description': 'For your next challenge Nathaniel Truehound wants you to track down some hard to find items for Edward Stormhawk. Visit Edward Stormhawk standing near the beach on Port Royal.',
        'stringAfter': "Junk, ey? Them pirates know nothin'! There may not be a big demand, but I be a bit of a collector of usable odds and ends.\x07Find me some Navy men's shoestrings and their ship anchors. Also, some parchment and empty flasks.\x07No, I'm not daft! Now be off!",
        'title': 'Garbage Man' },
    'OQB.visitNathanielA': {
        'description': 'William Turk has put you through his tests. Return to Nathaniel Truehound to see what you should do next.',
        'stringAfter': "Put on quite a show at the tavern I hear. Don't be gettin' cocky, mate. Yer test is FAR from over.\x07To get a real pirate outfit ye must start at the top. Ye need a hat fittin' a true pirate.\x07I'll fashion ye a new one IF ye recover somethin': me lucky card deck.\x07Lost it in a card game to that cheatin' swine, Will Turk. Recover the deck and the hat's yers.",
        'title': "Turk's Approval" },
    'OQB.visitNathanielB': {
        'description': "You've passed Will Turner's tests. Return to Nathaniel Truehound to collect your reward.",
        'stringAfter': "This shirt's fit for a pirate of such standing. Ye earned it, and the admiration of Will Turner, no less!\x07Visit me old friend Edward Shackleby for yer next set of challenges.\x07He's usually up to no good 'round the Governor's Mansion.",
        'title': "Turner's Approval" },
    'OQB.visitNathanielC': {
        'description': "You've passed Edward Shackleby's challenge. Return to Nathaniel Truehound and inform him of your progress.",
        'stringAfter': "This next bloke has a love for junk. But he's one sail short of a full rig so that explains his odd taste.\x07Find Edward Stormhawk near the beach on Port Royal while I start on yer pantaloons.",
        'title': "Shackleby's Approval" },
    'OQB.visitNathanielD': {
        'description': "You've gathered all of the junk Edward Stormhawk desired. Return to Nathaniel Truehound and claim your new pants.",
        'stringAfter': "A fine bit of plunderin', I must say! These pantaloons are a fittin' reward.\x07Now all ye need is shoes and a belt to complete the outfit.\x07Next ye must prove yer skills on the high seas. So visit me ole chum Darby Drydock.\x07Pass his test and earn a belt that's essential fer good piratin'. He's the shipwright on Port Royal, in case ye didn't know.",
        'title': "Stormhawk's Best" },
    'OQB.visitNathanielE': {
        'description': "You've passed Darby Drydock's challenges. Return to Nathaniel Truehound to claim your belt.",
        'stringAfter': "Good timin', mate. Just finished yer belt. Excellent fit!\x07Ye be a force to reckon with behind the ship's wheel.\x07Now, only a few more challenges to finish yer outfit.\x07I be needin' some materials to make the shoes.\x07Here's a list of items: cloth, thread, needles, and so on.\x07Hurry back, or stay barefoot, ye will!",
        'title': 'A Seasoned Pirate' },
    'OQB.visitNathanielF': {
        'description': "You've finished all of Nathaniel Truehound's challenges. Return to him to claim your new shoes.",
        'title': 'New Shoes' },
    'OQB.visitWillTurnerA': {
        'description': 'Will Turner will be heading up your next challenge to prove your worth as a pirate. Visit him in his warehouse on Port Royal.',
        'stringAfter': "A challenge that's fitting a fine shirt? I know, while I ponder it, here's a task you will enjoy.\x07Sink some of those overpriced Navy ships.\x07When you return, I'll have a more proper challenge for a pirate of such reputation.",
        'title': "Turner's Test" },
    'OQB.visitWilliamTurkA': {
        'description': "Visit Truehound's friend William Turk for your first test. William Turk can be found in the Rowdy Rooster on Port Royal.",
        'stringAfter': "Hello, mate. Nathaniel speaks well of you, he does.\x07Hate to see you lose your shirt, so I'll tell you a secret...\x07Play the cards close to your chest. There's lots of cheats around.\x07Win some gold and win a good reputation, you will.\x07Now get to it. Time's a wastin'!",
        'stringBefore': "So ye want to dress the part of a true pirate, ey?\x07Then I'll be needin' to prove yer worth to match the clothes.\x07Let's start by seeing how savvy ye are 'round a deck of cards.\x07First thing, visit Will Turk over at the Rowdy Rooster.\x07Be careful there. Many a folk on Port Royal will rob ye blind!",
        'title': 'Pirate Life' },
    'OQB.visitWilliamTurkB': {
        'description': 'Nathaniel Truehound needs you to retrieve a lucky deck of cards he lost to William Turk. William Turk can be found in Rowdy Rooster on Port Royal.',
        'stringAfter': "Me, a cheat? Won that deck fair and square, I did! I'll gladly hand it over, fer a few items I be needin'.\x07Some rum, some bone shavin's, and prison keys.\x07Now shove off while I finish me grog in peace!",
        'title': "Turk's Lucky Deck" },
    'OQI.bribeBingham': {
        'description': "Bingham has mentioned there are ways around Callecutter's blacklist problems, but his information is not free.",
        'stringAfter': "What you want my friend is out on the high seas. EITC ships of course. Stocked to the deck with cargo.\x07Knowing what ship contains what is the tough part. The last thing you want is to take down an empty ship.\x07If you can get your hands on the manifests from EITC guards, Callecutter will know where he can get everything he needs.\x07I'll tell you where to find these manifests under one condition. You return with something of mine.\x07It's a diary I buried some time ago and now I hear there's mining in the same area.\x07You can imagine why I'd rather avoid some scoundrel stumbling across it.\x07Both the EITC manifests and my diary can be found in a mine on Port Royal named Royal Caverns. I'll be waiting...",
        'title': "Bingham's Blacklist Bribe" },
    'OQI.bribeScarlet': {
        'description': "Before she'll talk to you about resolving Callecutter's debt to her, Scarlet demands a bribe from you.",
        'stringAfter': "Callecutter's debt to me is rather large. I'm feeling a bit generous today though...\x07I'm willing to have you work off his debt so long as you don't muck it up.\x07There are four scurvy pirates who owe me money. They think they can hide from me and not pay!\x07I've heard two are disguised as Navy Soldiers and the others as EITC Thugs.\x07You should be able to identify them if they have a letter from me. Defeat them and we'll talk.",
        'title': 'Money Up Front' },
    'OQI.deliverCoinBag': {
        'description': "Isaiah Callecutter and Amelia Sunfellow have a silent partner named John Smith. Deliver John's payment. He can be found on Driftwood Island.",
        'stringAfter': "It's about time! I've seen no payment in weeks. I was starting to think the shop closed.\x07So you work for the shop I take it? Technically that would make you my employee...\x07As my employee, I could use your assistance on a thing or two before you return.\x07For one, I've managed to lose track of where I buried some personal effects of mine.\x07They're buried somewhere on this island. Find them for me!",
        'title': 'A Silent Partner' },
    'OQI.deliverManifests': {
        'description': "Deliver the EITC manifests you've recovered to Amelia Sunfellow. They contain the locations of the materials needed for Callecutter's shop.",
        'stringAfter': "What are we supposed to do with these EITC manifests? Do you see a ship around here?\x07Sorry mate but you're going to have to set sail for this one.\x07Bring these items back to me and I'll start work on a special shirt for you!",
        'title': "A Tailor's Manifest" },
    'OQI.findJohnsStuff': {
        'description': 'John Smith forgot where he buried some personal effects of his on Driftwood Island. Recover them for him before you leave the island.',
        'stringAfter': "There it is! I'll have to draw myself a map next time I bury it.\x07My memory isn't what it used to be. Too long in the sun I suppose...\x07Before you go, would you mind taking care of some of these pests?\x07The island is infested with Wasps of all types! I can't take it much longer.\x07Oh, and make sure you bring me back some proof!",
        'title': 'Forgetful John' },
    'OQI.playBlackjack': {
        'description': 'To make his tavern appear busy, Johnny McVane wants you to fill a seat at a Blackjack table.',
        'title': 'Blackjack For Feathers' },
    'OQI.playPoker': {
        'description': 'To make his tavern appear busy, Johnny McVane wants you to fill a seat at a Poker table.',
        'title': 'Poker For Feathers' },
    'OQI.recoverAlligatorHides': {
        'description': 'Isaiah Callecutter needs you to recover alligator hides in order to make shoes from the EITC designs you recovered.',
        'title': 'Alligator Hides' },
    'OQI.recoverBeltBuckles': {
        'description': 'To finish her latest batch of belts, Amelia Sunfellow needs buckles. She says you can find some buried on Isla Cangrejos.',
        'stringAfter': "You couldn't pay me to go to Isla Cangrejos! The crabs disgust me!\x07Your belt is finished. The buckles you recovered fit perfectly.\x07I overheard Isaiah Callecutter talking about starting some new pairs of shoes. They won't last long once they've hit the shelves.\x07You should check if there is anything he needs. I'm sure you could get a pair out of it!",
        'title': 'Cangrejos Buckles' },
    'OQI.recoverBinghamsTip': {
        'description': 'Bingham wants you to recover a diary he buried some time ago in a mine on Port Royal named Royal Caverns.',
        'title': "Bingham's Tip" },
    'OQI.recoverBoltsOfCloth': {
        'description': 'Manifests show that EITC ships sailing around the Caribbean contain Bolts of Cloth. Recover them for Callecutter.',
        'title': 'EITC Cloth' },
    'OQI.recoverBoneShavings': {
        'description': 'Isaiah Callecutter needs you to recover bone shavings in order to make shoes from the EITC designs you recovered.',
        'title': 'Bone Shavings' },
    'OQI.recoverChickensForPhil': {
        'description': "As part of working off Callecutter's debt, Big Phil wants you to recover chickens from EITC ships for him.",
        'title': 'Chickens for Phil' },
    'OQI.recoverCrabClaws': {
        'description': 'John Smith needs you to cleanup some of the pests on Driftwood Island. Defeat some Crabs and bring him back Crab Claws as proof.',
        'title': 'Crab Claws' },
    'OQI.recoverCrabShells': {
        'description': 'John Smith needs you to cleanup some of the pests on Driftwood Island. Defeat some Crabs and bring him back Crab Shells as proof.',
        'title': 'Crab Shells' },
    'OQI.recoverFineScissors': {
        'description': 'Manifests show that EITC ships sailing around the Caribbean contain Fine Scissors. Recover them for Callecutter.',
        'title': 'EITC Fine Scissors' },
    'OQI.recoverFlyTrapThread': {
        'description': 'To begin making his popular hats, Callecutter needs some fly trap thread.',
        'title': 'Fly Trap Thread' },
    'OQI.recoverHatSupplies': {
        'description': 'To begin making his popular hats, Callecutter needs some fresh alligator hides and fly trap thread.',
        'stringAfter': "These are some fine materials. I hope those alligators didn't give you too much of a fight.\x07These hats may be the finest I've made yet. They only need one more thing...\x07Any hat leaving this shop is topped with a rare feather. My customers have come to expect it!\x07These feathers are going to be rather hard to find though.\x07A chap named Johnny McVane may know where to find some. Speak to him.",
        'title': "Callcutter's Special" },
    'OQI.recoverHides': {
        'description': 'To begin making his popular hats, Callecutter needs some fresh alligator hides.',
        'title': 'Fresh Hides' },
    'OQI.recoverManifests': {
        'description': 'For Callecutter to know where his needed materials can be found, Bingham has instructed you to recover EITC manifests from EITC guards located in a mine on Port Royal named Royal Caverns.',
        'title': 'EITC Manifests' },
    'OQI.recoverNeedles': {
        'description': 'To finish your shirt, Isaiah Callecutter needs to acquire some needles. Recover them for him from scorpions.',
        'stringAfter': "I hope you like the shirt! It's the finest one I've produced in some time.\x07At this rate you'll have the entire outfit before you know it.\x07The shop still has two problems, though. Scarlet and Big Phil.\x07I owe money to both and my profits are down.\x07Could you can work off the money I owe them? There's a vest and a pair of pants for you if you do.",
        'title': 'Needed Needles' },
    'OQI.recoverPigsForPhil': {
        'description': "As part of working off Callecutter's debt, Big Phil wants you to recover pigs from EITC ships for him.",
        'title': 'Pigs for Phil' },
    'OQI.recoverRareFeathers': {
        'description': 'Rare feathers can be found on EITC ships sailing around the Caribbean. Recover the needed rare feathers for Callecutter.',
        'stringAfter': "These will be perfect! Thanks mate. A rare feather is the perfect accent to any pirate's hat. My customers will be pleased.\x07Amelia Sunfellow has something for you to show our thanks. Go visit her.",
        'title': 'Rare Goods' },
    'OQI.recoverScarletsPearlA': {
        'description': 'Scarlet has recently lost her necklace in the jungle and now fears some of the pearls have been swallowed by Skeletons. Recover the pearls for her.',
        'title': 'Skeletons Eat Pearls' },
    'OQI.recoverScarletsPearlB': {
        'description': 'Scarlet has recently lost her necklace in the jungle and now fears some of the pearls have been swallowed by Vampire Bats. Recover the pearls for her.',
        'title': 'Vampire Bats Eat Pearls' },
    'OQI.recoverScarletsPearlC': {
        'description': 'Scarlet has recently lost her necklace in the jungle and now fears some of the pearls have been swallowed by Big Alligators. Recover the pearls for her.',
        'title': 'Big Alligators Eat Pearls' },
    'OQI.recoverScarletsPearlD': {
        'description': 'Scarlet has recently lost her necklace in the jungle and now fears some of the pearls have been swallowed by Fly Traps. Recover the pearls for her.',
        'title': 'Fly Traps Eat Pearls' },
    'OQI.recoverScarletsPearlE': {
        'description': 'Scarlet has recently lost her necklace in the jungle and now fears one of the pearls has been swallowed by a Giant Crab. Recover the pearl for her.',
        'title': 'Giant Crabs Eat Pearls' },
    'OQI.recoverScorpionShells': {
        'description': 'Isaiah Callecutter needs you to recover scorpion shells in order to make shoes from the EITC designs you recovered.',
        'title': 'Scorpion Shells' },
    'OQI.recoverShoeDesigns': {
        'description': "Isaiah Callecutter's shoe designs are outdated. Recover some fine shoe designs from EITC ships sailing around the Caribbean.",
        'stringAfter': "These designs require some rare ingredients, and they're not what I normally keep in the shop.\x07You should be able to find everything you need on Tortuga, though.\x07See if you can recover all of this for me. I'll be waiting...",
        'title': 'Design Heist' },
    'OQI.recoverSilkThread': {
        'description': 'Manifests show that EITC ships sailing around the Caribbean contain Silk Thread. Recover them for Callecutter.',
        'title': 'EITC Silk Thread' },
    'OQI.recoverVampireBatGuano': {
        'description': 'Isaiah Callecutter needs you to recover vampire bat guano in order to make shoes from the EITC designs you recovered.',
        'title': 'Vampire Bat Guano' },
    'OQI.recoverWaspEggs': {
        'description': 'John Smith needs you to cleanup some of the pests on Driftwood Island. Defeat some Wasps and bring him back Wasp Eggs as proof.',
        'title': 'Wasp Eggs' },
    'OQI.recoverWaspEssence': {
        'description': 'John Smith needs you to cleanup some of the pests on Driftwood Island. Defeat some Wasps and bring him back Wasp Essence as proof.',
        'title': 'Wasp Essence' },
    'OQI.recoverWaspWings': {
        'description': 'John Smith needs you to cleanup some of the pests on Driftwood Island. Defeat some Wasps and bring him back Wasp Wings as proof.',
        'title': 'Wasp Wings' },
    'OQI.returnIsaiah': {
        'description': "Check with Isaiah Callecutter to see if there is anything else he needs to finish the shirt that he's making for you.",
        'stringAfter': "I wish I could say I've started your shirt.\x07Unfortunately I am in need of needles before I can begin! Not much a Tailor can do without them.\x07Recover some needles for me and I'll have your shirt finished in no time!",
        'title': 'A New Shirt' },
    'OQI.returnIsaiahB': {
        'description': 'Inform Isaiah Callecutter that his debt to Scarlet is now gone.',
        'stringAfter': "Well, that takes care of one of them. At least I won't have to avoid Scarlet from now on.\x07Once we take care of what I owe Big Phil, maybe I can start showing my face again.\x07You'll also have a new vest and a pair of pants when you return!\x07Phil usually stands in front of my shop, tending to his livestock. Go speak to him.",
        'title': 'Scarlet Is Happy' },
    'OQI.returnIsaiahC': {
        'description': "Isaiah Callecutter's debt to Big Phil is now gone. Inform Callecutter and collect your new vest and pair of pants.",
        'stringAfter': 'Nice work! Hopefully Scarlet and Big Phil will stop by the shop now that the debt is gone.\x07They were always good customers of mine.\x07Oh, Amelia is starting on a new batch of belts. You could use a new one... No offense.\x07Go speak to her. I believe she needs your assistance to finish up.',
        'title': 'Vest and Pants' },
    'OQI.returnIsaiahD': {
        'description': 'Isaiah Callecutter is starting on some new pairs of shoes. Check with him to see if there is anything he needs.',
        'stringAfter': "I hope that belt fits you nicely. By now I'd like to think we know your size.\x07The only thing left I can help you with is shoes. Unfortunately our designs are a bit... outdated.\x07Lately everyone is talking about some new shoes the EITC has been distributing.\x07If we can steal some of their designs, it may help to stir up some business!\x07Recover some fine shoe designs from EITC ships sailing around the Caribbean.",
        'title': 'Pirate Boots' },
    'OQI.scarletsLettersA': {
        'description': 'Scarlet has a long list of pirates who owe her money. Two of them are disguised as Navy Soldiers who can be found in Thieves Den on Tortuga.',
        'title': "Scarlet's Soldiers" },
    'OQI.scarletsLettersB': {
        'description': 'Scarlet has a long list of pirates who owe her money. Two of them are disguised as EITC Thugs who can be found in Thieves Den on Tortuga.',
        'title': "Scarlet's Thugs" },
    'OQI.sinkEITCShips': {
        'description': 'Isaiah Callecutter needs to prevent the EITC from selling shoes based off the designs you stole. Sink enough EITC ships to disrupt their sales.',
        'title': 'Disrupting Sales' },
    'OQI.visitAmeliaSunfellow': {
        'description': 'To show his appreciation for your efforts, Callecutter wants to give you a special gift. He has left it with Amelia Sunfellow. Go visit her.',
        'stringAfter': "I hope this hat shows our appreciation. It's the finest of the batch!\x07Callecutter seems to like you. Just make sure you don't get caught up in his problems.\x07He has made his fair share of enemies.\x07It's gotten to the point that we have trouble purchasing the goods we need. Seems we've been blacklisted...\x07You know, that hat is part of a larger outfit. The rest would look quite sharp on you...\x07If you can continue helping us out with materials, you'll have the entire outfit in no time!\x07The best place to start would be with Navy Guard Bingham. He'll be able to shine some light on our blacklist situation.",
        'title': "Callecutter's Appreciation" },
    'OQI.visitAmeliaSunfellowB': {
        'description': 'Amelia is starting on a new batch of belts. Check with her to see if there is anything she needs you to do.',
        'stringAfter': "I hope you're enjoying the new clothing. Soon you'll have the entire outfit mate!\x07I'm sure Callecutter told you about the batch of belts I'm starting.\x07I have one with your name on it of course, but first I need a little help.\x07We need to send payment to our silent partner, John Smith.\x07Deliver this bag of coins to him. John can be found on Driftwood Island.",
        'title': 'Batch of Belts' },
    'OQI.visitAmeliaSunfellowC': {
        'description': "John Smith no longer requires your services. Return to Amelia Sunfellow and see if there's anything the shop needs of you.",
        'stringAfter': "I hope John Smith didn't give you too much trouble. I'm just glad he stays on Driftwood Island...\x07Oh, I'm almost done with my batch of belts! Unfortunately we have no buckles though.\x07A belt's not much good without a buckle, but...\x07I know of a small stash of belt buckles on Isla Cangrejos. Not exactly convenient, but it's our only option.\x07You should find enough belt buckles buried around Isla Cangrejos.\x07I'll have your belt ready when you return!",
        'title': 'Coming Home' },
    'OQI.visitBigPhil': {
        'description': "Isaiah Callecutter also owes Big Phil a bit of money. See if there is a way you can work off this debt for him. He is located outside Callecutter's shop on Tortuga.",
        'stringAfter': "I'd rather have the money that Callecutter owes me, but I guess I'll take what I can get.\x07My needs are fairly simple. I deal in livestock as you can see.\x07Bring me some chickens and pigs. You can find them on EITC ships sailing around the Caribbean.",
        'title': "Big Phil's Money" },
    'OQI.visitBingham': {
        'description': "Callecutter's shop continues to find it hard to acquire new materials. Speak to Navy Guard Bingham about helping Callecutter and his business.",
        'stringAfter': "Callecutter's made quite a few enemies since opening that rag shop of his.\x07I see you must be a regular there. Please excuse me if I fail to sound surprised.\x07Unfortunately for Callecutter, some of the people he crossed had a bit of influence on what comes in and out of Tortuga.\x07EITC chaps most likely. They've managed to nearly drive Callecutter out of business.\x07If you've come to ask me how you can fix this for him, you can save your breath.\x07Of course there are ways around all of this, but that's not free information in my estimation.",
        'title': "Bingham's Blacklist" },
    'OQI.visitIsaiah': {
        'description': 'Amelia Sunfellow and Isaiah Callecutter have run into some problems acquiring new materials for their Tailor shop. Visit Isaiah Callecutter to find out how you can help.',
        'stringAfter': "Hats used to be our most popular item. We couldn't keep enough of them on the shelf to be honest.\x07These days I can barely come up with enough material to make a pair of cheap gloves!\x07I guess that's just business for you. If you think you can help, the first hat I make will be yours.\x07All I need is some fresh alligator hides and fly trap thread to start.",
        'stringBefore': "My name is Amelia. I help Isaiah Callecutter with what needs to be done around here.\x07We pride ourselves on making the finest clothing a pirate can find on this island.\x07Sadly we find ourselves in a bind with acquiring new materials.\x07Our distributor was bought out by a fellow that isn't too pleased with Isaiah Callecutter.\x07If you are willing to help us out, I'll make sure that outfit of yours gets an update.",
        'title': 'Clothing Fit for a Pirate' },
    'OQI.visitJohnnyMcVane': {
        'description': 'Isaiah Callecutter needs some rare feathers to finish his latest batch of hats. Go speak to Johnny McVane to find out where you might be able to find some.',
        'stringAfter': "Rare feathers! Do you see any birds flying around this tavern?\x07I've been known to find a thing or two, but rare feathers don't just fall out of the sky...\x07Maybe I can use your help. The tavern has been dreadfully slow lately and I need to make this place look busy.\x07Fill a seat at the card tables for a while and I may just be able to find those feathers for you.",
        'title': 'Seeking Rare Feathers' },
    'OQI.visitScarlet': {
        'description': "Callecutter owes some money to Scarlet and cannot pay her. See if there's a way you can work off his debt. Scarlet is located outside of Callecutter's shop in Tortuga.",
        'stringAfter': "Isaiah Callecutter's one of many scurvy pirates that owe me money.\x07I don't think I'll be speaking to you unless it's worth my time...",
        'title': "Scarlet's Money" },
    'OQI.winAtCards': {
        'description': 'To make his tavern appear busy, Johnny McVane wants you to fill a seat at a Poker table and a Blackjack table. In return he will tell you were you can find the rare feathers Callecutter needs.',
        'stringAfter': "Looks like you've managed to win some gold. Maybe I'm not getting such a good deal here...\x07A deal is a deal though. Those rare feathers can be found, if you're willing to go get them.\x07The EITC has been shipping rare items like this for some time now.\x07Sink the right ship and you'll surely find your feathers.",
        'title': 'Cards For Feathers' },
    'OutfitQuestAdvanced': {
        'description': 'Adoria Dolores is overwhelmed running her shop and needs some help with her family. Help out her family members that are in need.',
        'stringAfter': "I'm glad to see you mate! I was worried Shochett Prymme sent you on a suicide mission.\x07These tentacles will do just fine. With this you'll have yourself an entire authentic Barbossa outfit!\x07I wish there was more to the outfit, though. It's been nice having someone around to help with my family. We are all grateful for you.\x07Enjoy the outfit and keep safe mate. Thanks again.",
        'title': "Adoria's Family" },
    'OutfitQuestBasic': {
        'description': "Nathaniel Truehound wants to put you to the test before he'll provide you with an outfit fit for a true pirate.",
        'stringAfter': "Well done! I must say, I didn't think ye had the metal.\x07May these shoes protect ye on yer journey.  Good luck, mate.",
        'title': 'Pirate Life' },
    'OutfitQuestIntermediate': {
        'description': 'Amelia Sunfellow and Isaiah Callecutter have run into some problems acquiring new materials for their Tailor shop. Assist them in keeping their business afloat.',
        'stringAfter': 'I must say, I rarely come across such a fine pirate like yourself.\x07I can only imagine what fate the shop would have fallen to without you!\x07Here are the shoes I made you. I hope they show my appreciation.\x07The shop will prosper with your efforts. Amelia and I thank you!',
        'title': 'Clothing Fit for a Pirate' },
    'PerlaAlodiaJewels': {
        'description': 'Perla Alodia could use some help around her shop. In return for helping her, she will pay you in jewelry.',
        'reward': 'Jewelry',
        'stringAfter': 'Thank you! The shop will surely thrive now. Here is a fine piece of jewelry to show my thanks.',
        'title': 'Helping Perla Alodia' },
    'PerlaAlodiaTrouble': {
        'description': 'Perla Alodia needs some help with one of her side businesses. For your efforts, she will reward you with a special piece of jewelry.',
        'reward': 'Jewelry',
        'stringAfter': 'I must thank you again for your help.\x07A smuggling ring is a tough task for just me and Olivier.\x07Here is the piece of jewelry I promised you. I hope you enjoy it.',
        'title': "Perla Alodia's Side Business" },
    'PeterChipparrAssailant': {
        'description': 'Help Peter Chipparr get some payback.',
        'reward': 'Gold',
        'stringAfter': 'Thank you for taking care of that for me. Come back and I might have more work for you.',
        'title': "Peter Chipparr's Vengeance" },
    'PhilsAnimals': {
        'description': "To work off Callecutter's debt, Big Phil wants you to recover live stock from EITC ships for him.",
        'stringAfter': "Nice live stock! They'll do just fine.\x07Tell Isaiah Callecutter that he can start showing his face around here again. His debt to me is gone.",
        'title': "Phil's Animals" },
    'PirateLore': {
        'description': 'Will Turner needs your help acquiring the book of Pirate Lore. It was thought to be lost, but recent rumors have him thinking otherwise. If you assist him, he will reward you with a new cutlass.',
        'stringAfter': "Wonderful! It has been years since I began the quest to piece together this text.\x07I can assure you, this book will not fall into the wrong hands again.\x07I must thank you again my friend. Here's the cutlass I promised you. May it always find you safe and well.",
        'title': 'Fine Cutlass Upgrade: Pirate Lore' },
    'PirateValentine': {
        'animSetAfter': [
            60668,
            60670],
        'description': "Erin Amorous has tasked you with playing cupid on this Valentine's Day.",
        'stringAfter': "I cannot believe me ears!  Good news mate, good news! \x07I am forever in yer debt. Here's yer shirt. Visit any tailor to have it fitted.",
        'title': 'A Pirate Valentine' },
    'PistolUnlockL5': {
        'description': 'Erasmus would like to build you a new pistol with your assistance.',
        'reward': '',
        'stringAfter': 'Fine work, mate.  Enjoy yer new pistol, some of me best work, it is.',
        'title': "Grand Pistol Upgrade: Erasmus' Pistol" },
    'PlunderingTasksA': {
        'description': 'As part of his final challenge, Nathaniel Truehound wants you to recover shop materials for him.',
        'stringAfter': "Thanks, mate! I be thinkin' there's no challenge ye can't overcome!\x07While I finish with yer shoes, help out me old friend Bartholomew Watkins.\x07I'll have finished those shoes when ye return.",
        'title': "Truehound's Materials" },
    'PlunderingTasksB': {
        'description': 'Bartholomew Watkins needs some help finishing his work for the day. Retrieve a list of items for him so that he can finish.',
        'stringAfter': 'Good show, mate. I be impressed!\x07Return to Nathaniel Truehound for a just reward. Fair winds!',
        'title': "Bartholomew's Overwhelmed" },
    'PortRoyalPCTier1': {
        'description': 'Aid Shane as he prepares to liberate one of his crew.',
        'reward': 'A Playing Card, Gold & Notoriety',
        'stringAfter': 'Let me express in advance the gratitude of my mate.\x07 Thanks to you, he will soon taste the free air of the sea!',
        'title': 'Prison Break (Easy)' },
    'PortRoyalPCTier1Tasks': {
        'description': 'Perform tasks to assist Shane in his prison break attempt.',
        'title': 'Prison Break Preparation' },
    'PortRoyalPCTier2': {
        'description': 'Help Shane prepare a heist involving Fort Charles.',
        'reward': 'A Playing Card, Gold & Notoriety',
        'title': 'Port Royal Fort Heist (Medium)' },
    'PortRoyalPCTier2Tasks': {
        'description': "Having gained Shane's confidence, you have received additional tasks from Shane to assist in his heist.",
        'title': 'Additional Tasks' },
    'PortRoyalPCTier3': {
        'description': 'Assist Shane in organizing a crime wave in Port Royal.',
        'reward': 'A Playing Card, Gold & Notoriety',
        'stringAfter': "They're on their way? That is just brilliant. Well done!",
        'title': 'Port Royal Crime Wave (Hard)' },
    'PuttingItAllTogether': {
        'description': "According to Billy McKidd, the rest of the book of Pirate Lore can be found buried somewhere on Kingshead Island, Rumrunner's Isle and Isla Cangrejos.",
        'stringAfter': "Let's see... Looks like you have yourself a complete book here.\x07I never thought I would see it with me own eyes.\x07Couple of years ago I probably would've double crossed you and taken it...\x07You should probably leave before I change me mind.",
        'title': 'Putting It All Together' },
    'QuidProQuo': {
        'description': 'In exchange for the locations of the rest of the Pirate Lore pages, Billy McKidd wants you to defeat some enemies as part of his duties to the Navy.',
        'stringAfter': "Looks like it may be a late night at the tavern for me. You should take care of me work more often!\x07The pages you be looking for are safe, buried by me own hands.\x07Here's a list of their locations. Good luck mate.",
        'title': 'Quid Pro Quo' },
    'RSmithErrands': {
        'description': 'Acquire new tools and raw materials for Smith',
        'reward': 'Gold',
        'stringAfter': "Thanks. You've been a great help.",
        'title': 'New Tools for Smith' },
    'RavenCoveStory': {
        'description': "Jack needs The Cursed Blades of El Patron in order to defeat Jolly Roger and end the Rum Blockade.\n\n To find them you must journey to Raven's Cove and search for survivors in a town decimated by Jolly's invasion.",
        'title': "Story Quest: Raven's Cove" },
    'RavensCoveTotem': {
        'description': "Complete the quest if you want easy access to Raven's Cove.",
        'dialogAfter': 'RavensCoveTotem.after',
        'title': "Secret of Raven's Cove Teleportation" },
    'ScarletsLetters': {
        'description': 'Scarlet has a long list of pirates who owe her money. Four of them can be found disguised as Navy and EITC in Thieves Den on Tortuga.',
        'stringAfter': "That'll teach them to hide from me! Maybe that'll send a message to the others that owe me money.\x07One more small little request and then you can inform Callecutter that his debt is clear.\x07I recently lost my favorite necklace in the jungle and I cannot find it!\x07A friend of mine saw a giant crab and some other cursed creatures with my pearls.\x07Please recover all of my necklace before it's gone forever!",
        'title': "Scarlet's Loose Ends" },
    'ScarletsPearls': {
        'description': 'Scarlet has recently lost her necklace in the jungle and now fears the pearls have been swallowed by Skeletons, Vampire Bats, Big Alligators, Fly Traps and a Giant Crab. Recover all of the pearls for her.',
        'stringAfter': "Well, I didn't think I'd see you back so quickly. Good work mate!\x07I was starting to think I'd never see that necklace again. You can inform Isaiah Callecutter that his debt to me is now gone.",
        'title': "Scarlet's Necklace" },
    'SeabonesErrand2': {
        'description': 'Help Sam Seabones make Port Royal a better place.',
        'reward': 'Gold',
        'title': 'Helping Sam Seabones' },
    'SeabonesErrand3': {
        'description': 'Help Sam Seabones make Port Royal a better place.',
        'reward': 'Gold',
        'stringAfter': "Great! I'll go find him right now.",
        'title': 'Helping Sam Seabones' },
    'SeabonesErrand4': {
        'description': 'Help Sam Seabones make Port Royal a better place.',
        'reward': 'Gold',
        'title': 'Helping Sam Seabones' },
    'ShipLegend': {
        'description': "Solomon O'Dougal's family has had some heirlooms stolen from them by the EITC. Help Solomon recover these items and he will reward you with a rare tattoo.",
        'stringAfter': 'What? I cannot believe what I be seeing. Thought this painting was lost forever.\x07It must have been some journey to recover them, me family thanks ye.\x07Return to me cousin Solomon to ink that tattoo he promised.',
        'title': 'Family Valuables' },
    'ShipTasksA': {
        'description': 'For the first part of his challenge, Darby Drydock wants you to recover planks, sails and ship wheels from ships sailing around the Caribbean.',
        'stringAfter': "Well done. Impressive. Hope ye didn't damage your vessel 'cause there be more to do.\x07Yer final challenge is to sink more EITC and Navy ships.\x07Many more. So best be gettin' busy, mate.",
        'title': 'High Seas Challenge' },
    'ShipTasksB': {
        'description': 'For his final challenge, Darby Drydock wants you to take down a large amount of EITC and Navy ships sailing around the Caribbean.',
        'stringAfter': "As far as I be concerned, yer a seasoned pirate.\x07I'd be happy to have ye on me crew any day!\x07Return to Nathaniel Truehound. He has somethin' useful for ye.",
        'title': 'Making Waves' },
    'ShirtVestIngredientsA': {
        'description': "To create the vest and shirt from Barbossa's outfit, Adoria Dolores needs you to recover some rare ingredients.",
        'stringAfter': "Good work mate! I hope you didn't have too much trouble acquiring these.\x07This will give me something to start on.\x07The rest of the materials will be a bit more difficult to get.\x07We'll need to get our hands on cursed cloth, cursed needles and cursed thread.\x07All of these can be found on skeleton ships sailing around the Caribbean. Return them to me.",
        'title': 'A Fine Shirt and Vest' },
    'ShirtVestIngredientsB': {
        'description': 'To finish your shirt and vest, Adoria Dolores needs you to acquire some cursed items from skeleton ships.',
        'stringAfter': "I forgot an ingredient! It's a crucial one as well.\x07I can't work with any cursed materials without a good supply of cursed needles.\x07You should be able to acquire these from higher level skeletons.",
        'title': 'Finishing Up' },
    'ShochettsHides': {
        'description': 'In exchange for the last of his fine steel, Shochett Prymme wants you to gather some items for his shop.',
        'stringAfter': "Wonderful, to be honest I didn't have the energy to do that myself.\x07Enjoy the fine steel, you will not be able to find much more in these parts.",
        'title': 'Finding Hides' },
    'SmittyIsSick': {
        'description': 'Jeweler Smitty has fallen ill and Sarah does not have the time to tend to him. Assist Smitty in recovering.',
        'stringAfter': 'I must thank you. I do not believe Smitty would have made it without you.\x07I forbid him from exploring the seas until the illness has passed.\x07Here is the piece of jewelry I promised you. Take care.',
        'title': "Smitty's Troubles" },
    'SpecialInk': {
        'description': "Solomon O'Dougal has promised to give you some rare tattoos if you can help him out. He will need you to gather ingredients for the needed ink and possibly more.",
        'stringAfter': 'A fine tattoo pattern this is. William must have liked you.\x07I must thank you again for the fine ink.\x07Come back to my store if you want to wear this tattoo.',
        'title': 'Special Ink' },
    'SpecialVisionSpell': {
        'description': "Acquire the components for Roland's Spell of Sight",
        'stringAfter': 'I can see it. The Company knows it is important. It is secured below deck...\x07Below the deck of an East India Warship.',
        'title': "Roland's Vision Spell" },
    'StirringUpTrouble': {
        'description': 'Alexander Thayer wants you to defeat some Navy and EITC guards so that they will purchase some extra defenses from him.',
        'stringAfter': "That'll show those Navy and EITC dogs.\x07Getting back at them and selling a few guns on the side will make my day.\x07The EITC, along with Navy assistance, managed to force my family to sell a stock of antique pistols.\x07They had been in my family for generations.\x07If you can recover them for me, I will give you one of my finest pistols.",
        'title': 'Stirring Up Trouble' },
    'StoreEndorsement': {
        'description': 'Since his customers know you and your association with the shop, Alexander Thayer wants you to defeat some tough enemies using your pistol in hopes it will bring in business.',
        'stringAfter': "Nice job, I have already received some orders based off the show you put on.\x07Business is doing better now, but not great.\x07There is not much more we can do... Well... There is one idea...\x07The Navy and EITC have had it too good lately. Not many pirates around brave enough to mess with them.\x07If we can scare them a bit though, they'll surely rush to stock up on some guns.\x07Defeat some Navy and EITC guards for me, be careful though.",
        'title': 'Store Endorsement' },
    'TPT_CubaUnlock': {
        'description': 'Learn the Secret of Transportation to Cuba.  Acquire a totem that will allow you to get around the Caribbean more quickly.',
        'reward': 'Cuba Teleport Totem, Gold & Notoriety',
        'stringAfter': 'Well done!\x07I have created a totem so that you might return here whenever you wished. It is yours, as promised.',
        'title': 'Secret of Cuba Teleportation' },
    'TPT_PadresDelFuegoUnlock': {
        'description': 'Learn the Secret of Transportation to Padres Del Fuego.  Acquire a totem that will allow you to get around the Caribbean more quickly.',
        'reward': 'Padres Del Fuego Teleport Totem, Gold & Notoriety',
        'stringAfter': 'Hold the Eye in your hands. I will perform the ritual to release the chains on its power... \x07...I am finished. While you possess the Eye of Nabai, you have the power of teleportation to Padres Del Fuego. \x07Good luck in your travels.',
        'title': 'Secret of Padres Del Fuego Teleportation' },
    'TPT_PortRoyalUnlock': {
        'description': 'Learn the Secret of Transportation to Port Royal.  Acquire a totem that will allow you to get around the Caribbean more quickly.',
        'reward': 'Port Royal Teleport Totem, Gold & Notoriety',
        'stringAfter': 'You have returned. Hand me the medal. \x07Wait while I perform the incantation to join the energies of the medal with the spirit of the island... \x07...It is done. Port Royal is never more than a clear thought away.',
        'title': 'Secret of Port Royal Teleportation' },
    'TeleportTotem': {
        'description': 'Learn the Secret of Transportation to Tortuga. Acquire a totem that will allow you to get around the Caribbean more quickly.',
        'reward': 'Tortugan Teleport Totem, Gold & Notoriety',
        'stringAfter': 'Back so soon? Did you miss Tia?\x07I see you found the Tortugan artifact I asked for. \x07With this spell, it will be your key to that far away place ...\x07...Look now! The totem is yours.',
        'title': 'Secrets of Tortuga Teleportation' },
    'TreasureChess': {
        'description': 'Recover priceless pieces from the game of kings.',
        'reward': 'Chess Collection Unlocked & Notoriety',
        'stringAfter': "You just might be the game-playin' scourge I'm looking for! So, here's the deal.\x07You find the pieces of this wondrous chess set...\x07... and I'll take care of the fence. Wouldn't want the law catching us with such high-profile plunder now would we?\x07Fair winds, mate!",
        'title': 'Treasure Unlock: Treasured Chess Set' },
    'TreasureChess2': {
        'description': 'Find pieces from the game of kings.',
        'stringAfter': "Well, I see you've done your part...\x07... but I was not so successful. \x07No fink, swindler, brigand  or braggart wants to touch our pretty chess set. I don't have a buyer.\x07And to think they call it the game of kings!\x07Well, you can hold onto it for now if you like...\x07... I wouldn't let the Navy know you have it, if I be you.\x07Nice doin' business with you!",
        'title': 'Treasured Chess Set' },
    'TreasureFigurines': {
        'description': "Unearth the precious figurines from Tia Dalma's Menagerie.",
        'reward': "Tia Dalma's Menagerie Collection Unlocked & Notoriety",
        'stringAfter': "When you hear Tia call, come quickly.\x07You think Tia powerful? \x07Power be in the knowin'... knowin' the earth... and knowin' the creatures that be livin' there.\x07Tia had a collection, carved from wood and stone. Not pretty, but powerful in its own way...\x07... a collection of the beasts of the earth. \x07Tia wants her carvings back - or at least away from the dogs that stole them.\x07You will help Tia, no? You help Tia... then she will help you.",
        'title': "Treasure Unlock: Tia's Menagerie" },
    'TreasureFigurines2': {
        'description': "Recover the precious figurines from Tia Dalma's Menagerie.",
        'stringAfter': 'That is my collection, yes? Them animals, they have a power... make you strong against your enemies.\x07Keep them... and when Tia calls again, you come.',
        'title': "Tia Dalma's Menagerie" },
    'TreasureMedals': {
        'description': 'Complete a collection of obscure and valuable Navy medals.',
        'reward': 'Navy Medals Collection Unlocked, Gold & Notoriety',
        'stringAfter': "Good, you're here. I assumed that a treasure seeker such as you would find this interesting.\x07It's a Navy medal. They give them out for \x01slant\x01meritorious\x02 conduct... as defined by the Navy of course.\x07I'm not certain the rest of us would agree that the recipients of these medals are so very noble.\x07So here is the interesting part. This particular medal happens to be made of \x01slant\x01white gold\x02, which is extremely rare... and extremely valuable.\x07I recognized it from working with white gold on sword hilts for rich noblemen.\x07I'm quite certain the Navy had no idea the value of these medals when they handed them out.\x07Find them, and we'll melt them down into a treasure fit for the king himself...\x07... and I will use my share to buy a ship and get off of this rock!",
        'title': 'Treasure Unlock: Navy Medals' },
    'TreasureMedals2': {
        'description': 'Collect rare and valuable Navy medals.',
        'stringAfter': "Well done, mate. This won't take long. The fire is already very hot...\x07Okay, that should do nicely. Here is your share. Guard it well...\x07... and watch your back!",
        'title': 'Navy Medals' },
    'TreasureRings': {
        'description': 'Learn what happens when the infamous Rhineworth Rings are reunited.',
        'reward': 'Rhineworth Rings Collection Unlocked & Notoriety',
        'stringAfter': "Lend me your ear, mate.\x07I won't actually be takin' your ear... not yet. But listen close and you'll walk away the richer for it.\x07What do ye know of the Rhineworth rings?\x07Of course they're cursed! It's said that whoever holds all ten... well, no one's sure what happens \x01slant\x01exactly\x02...\x07Let's just say that if the legend be true, I'd like to find out...",
        'title': 'Treasure Unlock: The Rhineworth Rings' },
    'TreasureRings2': {
        'description': 'Learn what happens when the infamous Rhineworth Rings are reunited.',
        'stringAfter': "A fine bit of piratin', mate. A deal's a deal and here be your share of the loot.\x07I'd be careful who I showed those rings to...\x07Fare thee well!",
        'title': 'The Rhineworth Rings' },
    'TreasureRogues': {
        'description': "Recover the famous portraits of the 'Nine Rogues'.",
        'reward': 'Nine Rogues Collection Unlock & Notoriety',
        'stringAfter': 'The appearance of the signature on each of The Nine Rogues portraits is all Luther knew?\x07I had hoped for more, but it will have to suffice.\x07Find the paintings. Bring word of my father, and the Rogues are yours to do with as you choose.\x07Good luck!',
        'title': 'Treasure Unlock: The Nine Rogues' },
    'TreasureRogues2': {
        'description': "Recover the famous 'Nine Rogues'.",
        'stringAfter': "You found each of the Nine Rogues?\x07Yes, they are beautiful... in their way. Not something I'd hang in my drawing room.\x07Any word of my father? I fear I have been holding out false hope...\x07I must be strong. Keep the paintings and go.",
        'title': 'The Nine Rogues' },
    'TreasureTeeth': {
        'description': "Pursue Captain Rudyard's golden teeth.",
        'reward': "Rudyard's Teeth Collection Unlocked, Gold & Notoriety",
        'stringAfter': "From all these teeth this beauty is undoubtedly one of Rudyard's teeth.\x07Now you know what to look for. The others should be easy. Our usual split arrangement applies of course.",
        'title': "Treasure Unlock: Rudyard's Teeth" },
    'TreasureTeeth2': {
        'description': "Pursue Rudyard's golden teeth.",
        'stringAfter': "A lovely sight! So here's your third... and keep the teeth. I'm feeling magnanimous!",
        'title': "Rudyard's Teeth" },
    'ValentineParts': {
        'animSetAfter': [
            65000,
            60665,
            60670],
        'description': "Gather the ingredients for Sid's handmade Valentine Heart - Alligator hide for the base and a red coat to cover it, some bones and brass buttons to decorate, and the scorpion blood for glue.",
        'stringAfter': 'Fine work.  Now waits a bit while I make it\x07...there! Beautiful, ey? A heart to melt her heart.\x07Now go and return to me with her love!',
        'title': 'Valentine Ingredients' },
    'VoodooDollUnlockL4': {
        'description': 'Tia Dalma has been robbed of something very important to her. Get it back and she will reward you.',
        'stringAfter': 'I fear the spirit shard remains in captivity. My heart sinks.\x07Nevertheless, you have aided me and deserve reward.\x07Come back again. This business be far from complete.',
        'title': 'Pirate Doll Upgrade: Stolen Relic' },
    'VoodooDollUnlockL5': {
        'description': "Tia Dalma wages war on the Generals of Jolly Rogers' armies.",
        'reward': '',
        'stringAfter': "Excellent work!  Here's your reward.  You becoming notorious my friend and you help my friend's soul.\x07 Return again after you grown stronger, so that we might discover why Jolly Roger's want his spirit so bad.",
        'stringBefore': '',
        'title': 'Taboo Doll Upgrade: The Generals' },
    'VoodooStaffUnlockL4': {
        'description': 'A man named Roland Raggart will give you the power you seek, but he has his own ambitions for power',
        'stringAfter': 'I have freed her energies. And they have a new owner. Me!\x07Oh yes, here is your prize. You have more than earned it.',
        'title': "Vile Staff Upgrade: Roland's Cloudy Orb" },
    'VoodooStaffUnlockL5': {
        'description': 'Roland Raggart has more mysterious errands for you revolving around the orb you acquired for him previously.',
        'reward': '',
        'stringAfter': "Here's your new staff.\x07With your help, I grow close to my goal...my own army of undead EITC soldiers!\x07With this Orb, I will raise an undead army to rival Jolly Roger's, the soon-to-be former ruler of undead in the Caribbean!\x07I'm sure you can understand now why I had to keep my cards close to the vest, as the gamblers say.",
        'stringBefore': '',
        'title': 'Dire Staff Upgrade: Unlocking the Orb' },
    'WaspClearOut': {
        'description': 'John Smith needs you to cleanup some of the pests on Driftwood Island. Defeat some Wasps and bring him back Wasp Wings, Wasp Eggs and Wasp Essence as proof.',
        'stringAfter': "Good show! You showed those scurvy pests.\x07Maybe I'll scatter these Wasp Wings about the island as a warning to the other Wasps...\x07Take care of the crabs as well and we'll call it even.\x07Remember to bring me back some proof as well.",
        'title': 'Wasp Cleanup' },
    'WatkinsErrand1': {
        'description': 'Help Bartholomew find explosive powder.',
        'reward': 'Gold',
        'title': "Bartholomew's Powder Errand" },
    'WatkinsErrand2': {
        'description': 'Help Bartholomew acquire cotton.',
        'reward': 'Gold',
        'title': "Bartholomew's Cotton Errand" },
    'WatkinsErrand3': {
        'description': 'Help Bartholomew acquire iron.',
        'reward': 'Gold',
        'title': "Bartholomew's Iron Errand" },
    'WeaponDagger': {
        'description': 'Learn the deadly art of the dagger.',
        'reward': 'A Dagger & Notoriety',
        'stringAfter': 'Dear Will does the finest work...\x07You have begun the journey toward the mastery of the deadly art of the dagger. But this journey has only just begun...\x07...Continue to practice and your skills will improve.',
        'title': 'Weapon Unlock: Dagger' },
    'WeaponDoll': {
        'description': 'Learn how to construct and use the fearsome voodoo doll.',
        'reward': 'A Voodoo Doll & Notoriety',
        'stringAfter': 'Brave you have been... and true. The doll is finished.\x07Use it wisely. Now go!',
        'title': 'Weapon Unlock: Voodoo Doll' },
    'WeaponGrenade': {
        'description': "Learn how to cook up and 'serve' devastating grenades.",
        'reward': 'A Grenade & Notoriety',
        'stringAfter': "What took so long? I nearly lost my neck to a pack of rabid tree squirrels in the jungle yesterday - true story.\x07Is that all Ewan could spare for a dear old friend? Well, times are tight, and lips are loose...\x07... so don't go flapping yours about, savvy?",
        'title': 'Weapon Unlock: Grenade' },
    'WeaponStaff': {
        'description': 'Learn how to wield the mysterious voodoo staff.',
        'reward': 'A Voodoo Staff & Notoriety',
        'stringAfter': 'Here is your staff. Use it with strength... and wisdom!',
        'title': 'Weapon Unlock: Voodoo Staff' },
    'WillCreatureTasks': {
        'description': 'For your final challenge, Will Turner wants you to defeat alligators, bats, scorpions, crabs and wasps.',
        'stringAfter': "Excellent work! A better pirate I know not! Nathaniel Truehound will know you are solid in my eyes.\x07Go see him quickly.  He's expecting you.",
        'title': 'Pesky Creatures' },
    'WillFightTasks': {
        'description': 'As part of your next challenge, Will Turner wants you to defeat Navy guards, EITC guards and skeletons.',
        'stringAfter': "You made quick work of that challenge, mate. This next one won't be so easy...\x07To finish, let's see how you handle some of the more 'pesky' creatures lurking around Port Royal. Good luck!",
        'title': 'Foes with Two Legs' },
    'at1.0visitThayer': {
        'description': 'Alexander Thayer is known to have high quality pistols. Find him and learn his price.',
        'stringAfter': "You call that a pistol? I have seen more impressive weaponry on a common skeleton.\x07Better arms can be found you know, for a price that is.\x07My price isn't gold though. What I really need is someone to help with my shop.\x07There are many duties that require me to leave the shop.\x07Normally, I would need to close up, but with your help, I could keep the shop open.\x07To start, Navy guard Bingham needs his order picked up. Return it to me.",
        'title': 'Visit Alexander Thayer' },
    'at1.defeatBigAlligators': {
        'description': 'Since his customers know you, Alexander Thayer wants you to defeat some Alligators using your pistol in hopes it will bring in business.',
        'title': 'Advertising With Alligators' },
    'at1.defeatEITC': {
        'description': 'Alexander Thayer wants you to defeat some EITC guards so that the EITC will purchase some extra defenses from him.',
        'title': 'Scaring The EITC' },
    'at1.defeatFlyTrap': {
        'description': 'Since his customers know you, Alexander Thayer wants you to defeat some Fly Traps using your pistol in hopes it will bring in business.',
        'title': 'Advertising With Fly Traps' },
    'at1.defeatNavy': {
        'description': 'Alexander Thayer wants you to defeat some Navy guards so that the Navy will purchase some extra defenses from him.',
        'title': 'Scaring The Navy' },
    'at1.defeatScorpion': {
        'description': 'Since his customers know you, Alexander Thayer wants you to defeat some Scorpions using your pistol in hopes it will bring in business.',
        'title': 'Advertising With Scorpions' },
    'at1.defeatSkeletons': {
        'description': 'Since his customers know you, Alexander Thayer wants you to defeat some Skeletons using your pistol in hopes it will bring in business.',
        'title': 'Advertising With Skeletons' },
    'at1.defeatVampireBat': {
        'description': 'Since his customers know you, Alexander Thayer wants you to defeat some Vampire Bats using your pistol in hopes it will bring in business.',
        'title': 'Advertising With Vampire Bats' },
    'at1.deliverOrderA': {
        'description': 'Alexander Thayer needs you to deliver an order to one of his customers. Deliver a gun to Bingham on Port Royal.',
        'stringAfter': 'Thayer may not have the best arms on Tortuga, but at least he is cheap. Forget about a tip.',
        'title': "Bingham's Gun" },
    'at1.deliverOrderB': {
        'description': 'Alexander Thayer needs you to deliver an order to one of his customers. Deliver a gun to Jack Redrat, he lives in a jungle in Tortuga.',
        'stringAfter': "Most shops don't deliver to these woods. Thank Thayer for me. Here's a tip for your efforts.",
        'title': "Redrat's Order" },
    'at1.deliverOrderC': {
        'description': 'Alexander Thayer needs you to deliver an order to one of his customers. Deliver a gun to Olivier. He can be found on the docks in Padres Del Fuego.',
        'stringAfter': 'It gets dangerous out on the docks at night you know...\x07Hopefully I will not need to use this any time soon. Sorry, no tip.',
        'title': "Olivier's Order" },
    'at1.deliverOrderD': {
        'description': 'Alexander Thayer needs you to deliver an order to one of his customers. Deliver a gun to Billy McKidd, he can be found in a tavern on Cuba.',
        'stringAfter': "Turns out luck was not on me side, and lost me last pistol at these poker tables.\x07That'll not happen again though, I be feeling lucky. Thanks for the delivery, mate.  Here's yer tip.",
        'title': "McKidd's Order" },
    'at1.deliverOrderE': {
        'description': "Alexander Thayer needs you to deliver an order to one of his customers. Deliver a gun to Bastien Craven, he lives on Rumrunner's Isle.",
        'stringAfter': 'Just in time! It was getting old fending off crabs with sticks and coconuts.\x07I would tip you if I could, good luck.',
        'title': "Craven's Order" },
    'at1.deliverOrderF': {
        'description': 'Alexander Thayer needs you to deliver an order to one of his customers. Deliver a gun to Orinda Le Juene, she can be found on the docks in Tortuga.',
        'stringAfter': "Marvelous, just in time.\x07This'll make a fine present for me husband. Take this tip.",
        'title': "Orinda's Order" },
    'at1.playBlackjack': {
        'description': 'Alexander Thayer has found that sales at his shop increase when pirates lose at the card tables. Win a huge amount of gold at blackjack tables to stir up business.',
        'title': 'Blackjack Trouble' },
    'at1.playPoker': {
        'description': 'Alexander Thayer has found that sales at his shop increase when pirates lose at the card tables. Win a huge amount of gold at poker tables to stir up business.',
        'title': 'Poker Trouble' },
    'at1.recoverAntiquePistols': {
        'description': "The EITC, along with Navy assistance managed to force Alexander Thayer's family to sell a stock of antique pistols. Recover these pistols.",
        'title': 'Antique Pistols' },
    'at1.returnOrder': {
        'description': 'Bingham has given you his gun order. Deliver it to Alexander Thayer.',
        'stringAfter': "Bingham cannot seem to hold onto a pistol these days.\x07You'll not hear any complaints from me though.\x07Deliver Bingham's gun order along with the others that need to go out today.",
        'title': "Bingham's Order" },
    'at1.visitBingham': {
        'description': 'Alexander Thayer has hired you to help with his shop duties. Navy guard Bingham needs his gun order picked up. Return it to Thayer.',
        'stringAfter': 'I lost my old pistol dealing with some... unwelcome pirates.\x07This will be the second time in a month I have had to purchase a new one.\x07A few more and the other guards will never let me hear the end of it. Take this order to Alexander Thayer.',
        'stringBefore': 'DIALOGUE ERROR',
        'title': "Thayer's Special" },
    'at1.visitThayer': {
        'description': 'You have delivered all of the guns that Alexander Thayer needed you to deliver. Return to him and inform him of your progress.',
        'stringAfter': 'Good work. Customers always appreciate a timely delivery.\x07The shop has been a little slow lately, but there is a solution.\x07If there is one thing that gets a pirate to purchase a pistol, it is losing at the card tables.\x07Stir up some business by cleaning up at the Poker and Blackjack tables.',
        'title': 'Done Deliveries' },
    'branch.1test': {
        'description': 'This is choice A from branched quests',
        'stringAfter': 'This was a good choice bro',
        'title': 'Branched Quest A' },
    'branch.2test': {
        'description': 'This is choice B from branched quests',
        'stringAfter': 'This was a horrible choice bro',
        'title': 'Branched Quest B' },
    'branch.3test': {
        'description': 'This is a quest after branched quests',
        'stringAfter': 'So this is next thing you gonna do...',
        'title': 'After Branched Quests' },
    'branch.4test': {
        'description': 'This is the last quest after branched quests',
        'stringAfter': 'So long sucka!',
        'title': 'Last Quests' },
    'branch.completeLaddersQuest': {
        'customTask': 'Test for custom task',
        'description': 'In order to complete this quest you need to complete other ladders.',
        'title': 'Complete Ladders' },
    'branch.firstQuest': {
        'description': 'Testing Branching with Dialogs',
        'dialogAfter': 'branch.firstQuest.after',
        'title': 'Branch First Quest' },
    'branch2.1test': {
        'description': 'This is choice A from branched quests 2',
        'stringAfter': 'This was a good choice bro',
        'title': 'Branched Quest A 2' },
    'branch2.2test': {
        'description': 'This is choice B from branched quests 2',
        'stringAfter': 'This was a horrible choice bro',
        'title': 'Branched Quest B 2' },
    'bw1.1recovercotton': {
        'description': 'Defeat an EITC ship in order to acquire a yard of cotton.',
        'stringAfter': "Thanks. Here's your payment.",
        'stringBefore': "I need a yard of cotton to make fuses with. EITC ships are your best bet for this.\x07Get me some cotton and I'll give you a nice reward.",
        'title': "Bartholomew's Cotton Errand" },
    'bw1.1recoveriron': {
        'description': 'Defeat a Navy ship in order to acquire iron bars.',
        'stringAfter': "Thanks. Here's your payment.",
        'stringBefore': 'I need some iron from a Navy Ferret.',
        'title': "Bartholomew's Iron Errand" },
    'bw1.1recoverpowder': {
        'description': 'Defeat a Navy ship in order to acquire explosive powder.',
        'stringAfter': "Thanks. Here's your payment.",
        'stringBefore': 'Could you find me some explosive powder for me? Navy Ships carry plenty.',
        'title': "Bartholomew's Powder Errand" },
    'c2.10visitDockworker': {
        'description': 'Launch your ship from a dinghy located at the docks.',
        'title': 'Launch Your Ship' },
    'c2.11visitBarbossa': {
        'description': "Barbossa is in a cave on Devil's Anvil island - a ray of light will guide you there.",
        'title': 'Find Captain Barbossa' },
    'c2.2defeatSkeletons': {
        'blockerMessage': 'Use your new cutlass to defeat 3 skeletons before seeking Tia Dalma.',
        'description': 'Use your new cutlass to defeat 3 skeletons before seeking Tia Dalma.',
        'title': 'Defeat 3 Skeletons' },
    'c2.4recoverOrders': {
        'description': "Steal impound release orders for the Black Pearl from Navy soldiers near the Governor's mansion.",
        'title': 'Recover Release Orders' },
    'c2.5deliverOrders': {
        'description': "Validate the release orders with the Governor's stamp - a ray of light will guide you to the Governor's mansion.",
        'title': "Get Governor's Stamp" },
    'c2.6visitDarby': {
        'description': 'Find the shipwright Darby Drydock - a ray of light will guide you to him.',
        'stringAfter': "What's that? Miss Swann sent ye?\x07Well, I do owe her a favor... she got me out of a spot of trouble with the authorities recently...\x07But I can't help ye with that \x01slant\x01Harbormaster\x02 breathin' down my neck...\x07Ye might be able to \x01slant\x01distract\x02 his attention with some scratch, if ye take my meaning...",
        'title': 'Visit The Shipwright' },
    'c2.7visitHarbormaster': {
        'description': 'Find the harbormaster near the smaller Port Royal dock - a ray of light will guide you to him.',
        'stringAfter': "Drydock sent ye, did he? I've got my \x01slant\x01eye\x02 on him, and that's a fact.\x07Go soft on him, ye say? Well, that will \x01slant\x01cost\x02 ye a pretty penny says I...",
        'title': 'Talk To The Harbormaster' },
    'c2.8bribeHarbormaster': {
        'description': "Select the 'Bribe' button to bribe the harbormaster.",
        'stringAfter': "Well now! I suppose I could be too busy to bother lookin' after the dealings of that scurvy shipwright...\x07Now get out of me sight 'fore I changes me mind!",
        'title': 'Bribe The Harbormaster' },
    'c2.9visitDarby': {
        'description': 'Find shipwright Darby Drydock - a ray of light will guide you to him.',
        'title': 'Visit Darby Drydock' },
    'c2_chatTutorial': {
        'description': 'Learn the Basics of In-Game Chat',
        'title': 'Chat Tutorial' },
    'c2_visit_tia_dalma': {
        'blockerMessage': 'Find Tia Dalma in the jungle - a ray of light will guide you to the jungle entrance.',
        'description': "Find Tia Dalma in the King's Run jungle - a ray of light will guide you to the jungle entrance.",
        'title': 'Find Tia Dalma' },
    'c2_visit_will_turner': {
        'blockerMessage': 'Finish the cutlass tutorial.',
        'description': 'Get a cutlass from Will Turner in the warehouse outside - a ray of light will guide you to him.',
        'title': 'Arm Yourself' },
    'c3.4captureMontrose': {
        'description': 'Capture Captain Montrose (again) aboard his Navy ship.',
        'title': 'Capture Captain Montrose' },
    'c3.5maroonMontrose': {
        'description': "Maroon Captain Montrose so he'll give up the map to the Black Pearl.",
        'title': 'Maroon Captain Montrose' },
    'c3.6deliverMap': {
        'description': 'Bring the Black Pearl Map back to Joshamee Gibbs.',
        'stringAfter': "Now there's but one thing left to do.\x07Follow this map to our ship... and bring her home!\x07Fair winds, mate!",
        'title': 'Deliver Map' },
    'c3.7recoverPearl': {
        'description': 'Steal the Black Pearl back from the Navy.',
        'title': 'Recover The Black Pearl' },
    'c3.8visitJack': {
        'description': 'Meet with Jack Sparrow and Joshamee Gibbs in the Faithful Bride on Tortuga.',
        'title': 'Visit Jack' },
    'c3r1.1sinkNavyShips': {
        'description': 'Navy ships have red and white sails and can be found off the coast of Tortuga.',
        'stringAfter': 'Maybe I should give ye a harder assignment next time...',
        'stringBefore': 'Yer not on the Navy payroll by chance, eh?',
        'title': 'Sink A Navy Ship' },
    'c3r1.2defeatNavyGuards': {
        'description': 'Navy soldiers can be found on Tortuga and in its jungles.',
        'stringAfter': 'Not bad - ye may turn out to be a pirate yet.',
        'stringBefore': 'Have ye tested your mettle against the Navy yet?',
        'title': 'Defeat Navy Soldiers' },
    'c3r1Joshamee': {
        'description': 'Demonstrate to Joshamee that you are trustworthy by giving trouble to the Navy.',
        'items': 'Tasks',
        'stringAfter': "Looks like ye know how to deal with the Navy, eh?\x07Navy is one thing... 'tis a fool's errand to be taking the Pearl back from Beckett himself.\x07So I reckon we need at least nine strong for a proper crew.\x07First bloke to look for's named \x01slant\x01Pidgeley\x02...\x07If memory serves, our bartender Carver used to know the bloke... I'd start by talking to him.",
        'title': 'Prove Loyalty' },
    'c3r2.5.5visitOrinda': {
        'description': 'Find Orinda Le Jeune down at the Tortuga docks and ask her about a Navy captain.',
        'stringAfter': "Aye, I know the captain you speak of. Name's \x01slant\x01Montrose\x02.\x07He's sailn' these waters somewhere.\x07Good luck, mate.",
        'title': 'Visit Orinda' },
    'c3r2.5captureMontrose': {
        'description': 'Capture Captain Montrose from a Navy ship.',
        'stringAfter': 'Before we talk, would ye mind fetching me a pint?',
        'title': 'Capture Captain Montrose' },
    'c3r2.6visitCarver': {
        'description': 'Fetch a pint for Gibbs from Carver the bartender.',
        'stringAfter': 'A pint for Master Gibbs? On the house, I say!',
        'title': 'Fetch A Pint' },
    'c3r2.7deliverPint': {
        'description': 'Take Gibbs his pint.',
        'stringAfter': "I thank ye kindly, mate!\x07Seems our dear Captain Montrose didn't know much, but it's a start.\x07Truth be told, I've been so \x01slant\x01busy\x02 here at the Bride that I've made little progress on the other crew prospects.\x07Maybe ye will have better luck findin' these deck rats.\x07We be needin' a man who's handy with the cannon...\x07... And nobody's handier with a cannon than \x01slant\x01Gunner\x02.\x01Ye will need to speak up if ye find 'im. Gunner's a bit hard-o-hearin'...\x07Occupational hazard, I reckon...\x07Gunner used to loiter about down by the docks. \x01slant\x01Orinda\x02 might know where he be found now.",
        'title': 'Deliver Pint' },
    'c3r2Joshamee': {
        'description': 'Recruit crew members for the Black Pearl for Joshamee.',
        'items': 'Crew Members',
        'stringAfter': "So Doc sent someone else in his place he did? Lucky for us. I won't ask what \x01slant\x01methods\x02 you used but...\x07Next crewman we need is Gunner, and he's our... gunner. Clever, ey?\x07Orinda might know about his whereabouts so I would start there.",
        'title': 'The List' },
    'c3r2r1.10maroonSteadman': {
        'description': "Maroon Captain Steadman on any wild island - and after he calms down - he'll cave in and give the location of the list.",
        'title': 'Maroon Captain Steadman' },
    'c3r2r1.11stealList': {
        'description': 'Find a list of ships from a desk in the EITC hideout disguised as a common house in Tortuga. The desk is well guarded so be careful.',
        'stringAfter': "Excellent work, mate. That'd be the list alright... Now send those ships to Davy Jones locker!\x07And bring back the warrants for the arrest of ole James Pidgeley...\x07I wouldn't want 'em falling into the wrong hands, savvy?",
        'title': 'Steal List of Ships' },
    'c3r2r1.12recoverWarrants': {
        'description': 'Steal back each copy of the arrest warrants for Pidgeley from Navy ships and save his scrawny neck!',
        'stringAfter': "Well done, but unfortunately... that was the \x01slant\x01easy\x02 part!\x07It's come to my attention... that there's another gent looking for our \x01slant\x01friend\x02 Mr. Pidgeley...\x07It would be best if his search was \x01slant\x01called off\x02 so I've added his name to your journal. Make haste, there is no time to spare.",
        'title': 'Recover Arrest Warrants' },
    'c3r2r1.13visitGrog': {
        'description': "Have Doc Grog concoct a lotion to remove Carver's tattoo... and yours.",
        'stringAfter': "Remove a tattoo? Only seen it done once... didn't end well for that sailor's arm.\x07It will cost. Miracles don't come cheap mate and you must gather the ingredients.\x07The undead have what I need. Here's a list.",
        'title': 'Tattoo Removal' },
    'c3r2r1.14.5stealWarrant': {
        'description': "Steal a warrant from a heavily guarded desk inside the Outpost in Thieves' Den cave on Tortuga",
        'stringAfter': "I'll be sure to give this to \x01slant\x01Pidgeley\x02, if I sees 'im, that is...\x07Oh, and ye can tell \x01slant\x01Jack Sparrow\x02 he'll have one \x01slant\x01James Pidgeley\x02 accounted for on his crew.  Farewell, mate.",
        'title': 'Steal Final Warrant' },
    'c3r2r1.14deliverRemedy': {
        'description': 'Take the tattoo remedy to Carver.',
        'stringAfter': "That's gonna burn, no doubt. One more thing... turns out there's another warrant for the arrest of our friend \x01slant\x01Pidgeley\x02.\x07Bad news is, it's heavily guarded. The EITC's got it inside this fort in a cave on Tortuga called the \x01slant\x01Thieves' Den\x02.\x07All ye need to do is fight yer way in, find it in a desk and bring it here...\x07... and then I will be free to join any crew I likes.",
        'title': 'Deliver Tattoo Remedy' },
    'c3r2r1.15visitJoshamee': {
        'description': 'Return to Joshamee Gibbs and tell him Pidgeley is ready to join the crew.',
        'title': 'Visit Joshamee Gibbs' },
    'c3r2r1.1visitScarlet': {
        'description': "Ask Carver if he knows the whereabouts of James Pidgeley. He's essential if you're to help recaputre the \x01slant\x01Black Pearl\x02 from the Navy.",
        'stringAfter': "Knew a Pidgeley once, I did. Handsome devil.\x07If you want this bloke on your crew, I need to know I can trust you.\x07Go and get this tattoo to prove you're no EITC spy. Visit Tattoo Bonita, she'll help.",
        'title': 'Talk to Carver' },
    'c3r2r1.3visitCarver': {
        'description': 'Visit Carver the barkeep in the Faithful Bride tavern in Tortuga.',
        'stringAfter': "Pidgeley sail with Jack Sparrow?  That's a laugh!\x07Look, mate - make yourself useful.  Take this shrapnel to Doc Grog and I'll make it worth your effort...",
        'title': 'Talk to Carver' },
    'c3r2r1.4deliverGrog': {
        'description': 'Deliver a bag of coins to Doc Grog in his office across from the Faithful Bride.',
        'stringAfter': "Carver sent ye?  Why don't ye ask him his real name, eh?",
        'title': 'Deliver coins to Doc Grog' },
    'c3r2r1.5visitCarver': {
        'description': 'Ask Carver if his real name is James Pidgeley.',
        'stringAfter': "Yep!  The scalawag you're lookin' for is me! My real name is Pidgeley.\x07If you want Pidgeley on Sparrow's crew... Carver needs to know he can trust you.\x07What can ye to prove trustworthiness?  Acquire a new tattoo, says I...\x07Take this pattern to Bonita.  She'll know what to do.",
        'title': 'Confront Carver' },
    'c3r2r1.6.5bribeBonita': {
        'description': "Bonita the tattoo artist hears all sorts of gossip and rumors. She also does a mean tattoo and will give you an exact copy of Carver's unique tattoo.",
        'stringAfter': "This is no ordinary design mate, it's... well, best keep quiet 'bout that.\x07Ye need to gather some ingredients fer me first... bone dust and scorpion blood for ink.\x07Now go. That tattoo scares off me other customers.",
        'title': 'Visit Bonita' },
    'c3r2r1.6deliverBonita': {
        'description': "Ask Bonita the tattoo artist to copy Carver's tattoo - a ray of light will guide you to Bonita's shack.",
        'stringAfter': "No-no-no-no-no-no-NO! NO! Are ye tryin' to get ME killed?\x07This is the mark of the Black Guard, Lord Beckett's top assassins!  But... I'll tell ye how to mark yerself... for a price.",
        'title': 'Find Tattoo Artist' },
    'c3r2r1.7visitCarver': {
        'description': "Return to Carver and show him the tattoo but don't ask too many questions - the walls have ears.",
        'stringAfter': "Speak softly, mate. There be spies among us. This tattoo is \x01slant\x01special\x02 ey?\x07 Return to me with flags from Navy Bulwarks and I'll explain more.\x07Why? If you want Carver, ask no more questions. Now go.",
        'title': 'Show Tattoo to Carver' },
    'c3r2r1.8recoverFlag': {
        'description': "Sink Navy ships and recover their flags to prove you're no Navy spy either.",
        'stringAfter': "Interesting \x01slant\x01tapestry\x02 there, mate! Hang on to that... might be useful one day...\x07I was an assassin for the East India Trading Company... a member of the \x01slant\x01Black Guard\x02.\x07...until I discovered that Lord Cutler Beckett was the one giving the orders... and they weren't \x01slant\x01right\x02.\x07That's when I \x01slant\x01severed ties\x02 with the organization. Problem is, they came after me, so I changed me name to Carver...\x07Before I sail with Sparrow... I need to clear up a few things... \x07Actually six things. \x01slant\x01six\x02 ships with orders to hang James Pidgeley...\x07Only we don't know \x01slant\x01which\x02 six, precisely. Best find that \x01slant\x01list\x02 post haste...\x07Captain Steadman will know where the list is kept... but you'll have to maroon him to get him to talk.",
        'title': "Capture Ship's Flag" },
    'c3r2r1.8recoverFlags': {
        'description': "Sink Navy ships and recover their flags to prove you're no Navy spy either.",
        'stringAfter': "Well done, mate. I know I can trust ye now... here's the truth 'bout Mr. Pidgeley...\x07He was an assassin for the East India Trading Company... a member of the \x01slant\x01Black Guard\x02.\x07...until he discovered that Lord Beckett was in cahoots with... none other than the devil himself!\x07That's when I \x01slant\x01severed ties\x02 with them. That's right... Pidgeley is me and they weren't so keen on me leavin', so I changed me name.\x07Before I sail with Sparrow, I need to clear me old name. There's a list of all who possess me warrants.\x07Find Captain Steadman. He'll know where the list is stowed... but you'll have to maroon him to get him to talk.",
        'title': 'Navy Ship Flags' },
    'c3r2r1.9captureSteadman': {
        'description': "Captain Steadman knows the location of the list of ships that carry a death warrant for James Pidgeley. Steadman sails an EITC ship and you'll have to sink it to capture the lout.",
        'title': 'Capture Captain Steadman' },
    'c3r2r1.BernardBrothers': {
        'description': 'The Bernard brothers are the only people left in the Caribbean who knew Carver when he was still Pidgeley so you must defeat them. Each of them captains an EITC ship.',
        'stringAfter': "You sail as well as you fight. I'm impressed. Now, there's the matter of a certain \x01slant\x01tattoo\x02...\x07Best find a way to \x01slant\x01burn my tattoo off, and ye would be wise to remove yours as well\x02... Go see if Doc Grog can cook something up...",
        'title': 'The Bernard Brothers' },
    'c3r2r1Carver': {
        'description': "James Pidgeley is an excellent crewman, skilled in ways most pirates are not - but most of all he never questions his Captain's orders and rarely speaks - just the way Captain Jack likes 'em. Pidgeley's past is a mystery as well, but rumor has it he's well versed in subterfuge and weaponry.",
        'stringAfter': "Changed his name, did he?  To Carver? Not much better, I think.\x07Now the next lad fer ye to round up is \x01slant\x01Gordon Greer\x02.\x07Greer went to Port Royal to visit his sister and never returned - locked up in Fort Charles, he is.\x07Mind you, it's dangerous business speaking to prisoners.",
        'stringDuring': 'Has Pidgeley signed up yet?',
        'title': 'Black Pearl Recruit: James Pidgeley' },
    'c3r2r1r1.1recoverClaw': {
        'description': 'Recover some bone dust from skeletons.  You might find some in the swamps of Tortuga.',
        'title': 'Bone Dust' },
    'c3r2r1r1.1tattoo': {
        'description': 'Recover some bone dust from skeletons. The dust helps to deepen the color but also... deepens the pain.',
        'title': 'Bone Dust' },
    'c3r2r1r1.2recoverRod': {
        'description': 'Steal a copper rod from a Navy ship to bite on while getting your tattoo.',
        'title': 'Copper Rod' },
    'c3r2r1r1.2tattoo': {
        'description': 'Recover some scorpion blood to use as tattoo ink. Cursed scorpion blood is unlike anything else - whatever it touches, it stains... forever.',
        'title': 'Scorpion Blood' },
    'c3r2r1r1.3recoverBlood': {
        'description': 'Recover a measure of scorpion blood to use as tattoo ink.  Try the jungles of Tortuga to find some.',
        'title': 'Scorpion Blood' },
    'c3r2r1r1.Tattoo': {
        'description': "Gather material to recreate Carver's tattoo.",
        'stringAfter': "Curse it, yer back! Didn't think ye had the nerve.\x07Alright, I'll do it. But do \x01slant\x01not\x02 tell anyone where you got it. Especially those \x01slant\x01Black Guard\x02 vermin. They makes me skin shiver.",
        'title': 'Acquire Tattoo' },
    'c3r2r1r1Tattoo': {
        'description': "Gather material to recreate Carver's tattoo.",
        'stringAfter': "Curse it, yer back! Didn't think ye had the nerve, mate.\x07Look - ye will only muck it up.  Don't want anyone thinking I've lost me touch...\x07So I'll paint yer \x01slant\x01pretty\x02 picture... Just be careful who ye show it to.",
        'title': 'Acquire Tattoo' },
    'c3r2r1r2.1ArcisHenchmen': {
        'description': "Claude D'Arcis is always protected by battle hardened henchmen. It would be wise to defeat them before tangling with the assassin.",
        'title': "Claude D'Arcis's Henchmen" },
    'c3r2r1r2.1Carrou': {
        'description': 'Capture assassin Jehan Carrou from a Navy ship.',
        'title': 'Jehan Carrou' },
    'c3r2r1r2.2ClaudeDArcis': {
        'description': "The dread assassin Claude D'Arcis resides in his lair inside Thieves Den. But approach with care, he's dangerous and a very clever fighter!",
        'title': "Claude D'Arcis" },
    'c3r2r1r2.2DArcis': {
        'description': "Defeat assassin Claude D'Arcis who is hiding in Thieves Den on Tortuga.",
        'title': "Claude D'Arcis" },
    'c3r2r1r2.3Coteau': {
        'description': 'Confirm with Andros Mallet that Coteau is deceased - Mallet is in the Tortuga Graveyard.',
        'title': 'Lothar du Coteau' },
    'c3r2r1r2.Assassin': {
        'description': "Defeat the assassin who's after Carver, or James Pidgeley, or whatever he goes by these days.",
        'stringAfter': "You dispatched that task with ease. Now, there be something else...\x07There's three blokes, the Bernard brothers, who served with me. They're the only ones left who can identify ole Pidgeley.\x07Each one captains an EITC Viper. Sink 'em and I'd be very grateful.",
        'title': 'Black Guard Assassin' },
    'c3r2r1r2Assassins': {
        'description': 'Defeat three assassins that are after Carver.',
        'items': 'Assassins',
        'stringAfter': 'All these writs describe Pidgeley as tall, brown hair, above-average intelligence... sounds like a fine gent!\x07They also mention a certain \x01slant\x01tattoo\x02... one that looks a lot like me own... a little too much, eh?\x07Best find a way to \x01slant\x01burn my tattoo off\x02... Go see if Doc Grog can cook something up...',
        'title': 'Defeat 3 Assassins' },
    'c3r2r1r3.1Guano': {
        'description': 'Recover fresh bat guano from cave bats.',
        'title': 'Cave Bat Guano' },
    'c3r2r1r3.1tattooRemoval': {
        'description': "The Undead Mutineers always carry a vial of liver oil to restore their fighting power - it's used in many island remedies",
        'title': 'Vials of Liver Oil' },
    'c3r2r1r3.2Hair': {
        'description': 'Recover hairs from undead skeletons.',
        'title': "Dead Man's Hair" },
    'c3r2r1r3.2tattooRemoval': {
        'description': 'Undead Pirate hair is known for its medicinal combination of salt and bile',
        'title': 'Patch of Hair' },
    'c3r2r1r3.3Blood': {
        'description': 'Recover some giant scorpion blood.',
        'title': 'Giant Scorpion Blood' },
    'c3r2r1r3.TattooRemoval': {
        'description': 'Gather the necessary ingredients for a potent tattoo removal potion.',
        'items': 'Ingredients',
        'stringAfter': "Just pour this on what you want to \x01slant\x01go away\x02... then hope it don't \x01slant\x01all go away\x02... to the bone that is... ha!",
        'title': 'Tattoo Removal' },
    'c3r2r1r3TattooRemoval': {
        'description': 'Gather the necessary ingredients for tattoo removal.',
        'items': 'Ingredients',
        'stringAfter': "Just pour this on what you want to \x01slant\x01go away\x02... then hope it don't \x01slant\x01all go away\x02... the stuff burns!",
        'title': 'Tattoo Removal Recipe' },
    'c3r2r2.10.1disruptRitual': {
        'description': 'Defeat the Undead Brigands before their numbers grow.',
        'title': 'Defeat Undead Brigands' },
    'c3r2r2.10.2disruptRitual': {
        'description': 'General Bloodless is the Undead Brigand Boss and must be defeated before the ritual is complete!',
        'title': 'General Bloodless' },
    'c3r2r2.10.51visitBlakeley': {
        'description': 'Go ask Lieutenant Blakeley to release Greer.',
        'stringAfter': "Let that brigand go? On June's orders?!\x07I may be smitten with her but I take orders from only my superiors.\x07Who are gone at present. So, I'll release Greer on one condition... you do a job for me first.\x07While the Navy doesn't officially recognize the undead vermin on Port Royal, I am \x01slant\x01unofficially\x02 charged with eliminating them.\x07Confusing, I know. But deep in a cave called \x01slant\x01Murky Hollow\x02 is where undead pirates muster.\x07Distrupt their unholy ritual and you can buy Greer's freedom.",
        'title': 'Visit Blakeley' },
    'c3r2r2.10.52disruptRitual': {
        'description': 'Disrupt the skeleton summoning ritual deep in the caves of Murky Hollow on Port Royal.',
        'stringAfter': "I didn't expect to see you again.\x07\x01slant\x01Jolly Roger\x02 you say? Impossible! You must be mistaken...\x07... go on and get your friend Greer...\x07I don't want to lay eyes on him or you again!",
        'title': 'Disrupt Ritual' },
    'c3r2r2.10.53visitGreer': {
        'description': 'Return to Greer.',
        'stringAfter': "I can't believe I'm actually looking forward to sailing with Captain Jack...\x07... it usually ends badly, sailing with him, I mean.\x07Fair winds to you, mate!",
        'title': 'Return to Greer' },
    'c3r2r2.10.5visitJune': {
        'description': "Tell June that Greer's wrongs have been addressed.",
        'stringAfter': "So you've undone what my brother did.\x07Not sure he deserves a friend such as you... but I gave my word.\x07Tell my Lieutenant Blakeley that my brother has his forgiveness.",
        'title': 'Visit June' },
    'c3r2r2.10.DisruptRitual': {
        'description': "Jolly Roger's undead minions dance and sing a war ritual - disrupt it at your own risk!",
        'stringAfter': "I didn't expect to see you again.\x07\x01slant\x01Jolly Roger\x02 you say? Impossible! You must be mistaken...\x07... go on and get your friend Greer...\x07I don't want to lay eyes on him or you again!",
        'title': 'Disrupt Ritual' },
    'c3r2r2.11visitJoshamee': {
        'description': 'Let Joshamee know that Greer has joined the crew.',
        'title': 'Return To Joshamee' },
    'c3r2r2.1visitGreer': {
        'description': 'Gordon Greer is held up indefinitely for being a petty thief, liar and swindler - all the qualities Jack looks for in a good crewman.',
        'stringAfter': "I'll not be joinin' any crew in my present condition. In fact, you best work something out with \x01slant\x01Bingham\x02...\x07Or he'll throw you in the stocks just fer talkin' to me.",
        'title': 'Find Gordon Greer' },
    'c3r2r2.2.5bribeBingham': {
        'description': 'Bribe Bingham so you can talk to Greer.',
        'stringAfter': 'Oh, and bring me some rum, and lots of it... some for drinking and some for trade. NOW!',
        'title': 'Bribe Bingham' },
    'c3r2r2.2visitBingham': {
        'description': 'Get permission from Sgt. Bingham before talking to Greer.',
        'stringAfter': "Greer's busy. But there's a few \x01slant\x01golden\x02 ways you can talk to him. Savvy?",
        'title': 'Go See Bingham' },
    'c3r2r2.3recoverRum': {
        'description': "Bingham's so corrupt he's not above sinking even Navy ships to get what he wants - and most carry the rum to drink or to trade for goods and services.",
        'stringAfter': "Took you long enough! Me and Greer are gettin' downright parched! Aren't we Greer?\x07Well... go on, talk to your mate before I change me mind.",
        'title': 'Bring Bingham Rum' },
    'c3r2r2.4blackjack': {
        'description': 'Win money playing Blackjack.',
        'stringAfter': 'Well done mate!  That certainly takes some of the sting out of it.\x07We never had this conversation, by the way.',
        'title': 'Win For Bingham' },
    'c3r2r2.5visitGreer': {
        'description': "Learn Greer's story from the man himself... if it's true that is.",
        'stringAfter': "It would be my pleasure to join up with Sparrow again. But I'm \x01slant\x01stuck here\x02...\x07Bingham's not the real problem. You'll have to convince \x01slant\x01Lt. Blakeley\x02.\x07Blakeley's smitten with me sister and she's convinced him to keep me locked up 'til I've \x01slant\x01changed\x02 me \x01slant\x01pirate ways\x02\x07See I... stole from her and she's angry. Help me patch things up with her, ey?",
        'title': 'Talk to Greer' },
    'c3r2r2.6visitBlakeley': {
        'description': "Meet with Lieutenant Peter Blakeley to plead for Greer's release. He has an apartment in Port Royal.",
        'stringAfter': "Release Greer? That vermin steals from his own sister! It's for his own good, you see...\x07I told June I'd keep an eye on him but if you could prove he's \x01slant\x01changed\x02 I'd have to let him go but...\x07...you'd have to take it up with \x01slant\x01her\x02.",
        'title': 'Visit Blakeley' },
    'c3r2r2.7visitJune': {
        'description': "Greer's sister June is a sweet young thing but when it comes to her thieving brother, she's tough as nails. But doing her some favors will help win his release.",
        'stringAfter': "Gordon? \x01slant\x01Changed\x02? That's doubtful! But I \x01slant\x01might\x02 change me mind if he returned everything he \x01slant\x01stole\x02.\x07Some of these aren't worth much but they do have \x01slant\x01sentimental\x02 value... like me ring.\x07It was a gift from Gordon. To replace it, you'll need to see a jeweler name of \x01slant\x01Smitty\x02.",
        'title': 'Meet June' },
    'c3r2r2.9deliverList': {
        'description': 'The list contains the names of people that Greer has wronged. See if he is willing to make appropriate amends.',
        'stringAfter': "Right all me wrongs? All of 'em? That be many folks indeed!\x07I need some help for, as you can see... I'm not able to make amends in person.\x07Could ye lend me a hand and visit each of them?",
        'title': 'Deliver List to Greer' },
    'c3r2r2Greer': {
        'description': 'Restore Gordon Greer to the crew by freeing him from the humiliating stocks.',
        'stringAfter': "Well done, mate! Gordon Greer's an excellent addition to the crew.\x07Next bloke's name is \x01slant\x01Hendry Cutts\x02...\x07Rumor on Cutts is he got himself married. Poor devil.\x07Talk to his bride, Millie to find him.",
        'stringDuring': 'No luck springing Greer, eh?',
        'title': 'Black Pearl Recruit: Gordon Greer' },
    'c3r2r2r1.1recoverRum': {
        'description': 'Bingham gets mighty thirsty watching Greer all day in the brutal Caribbean sun.',
        'title': 'Rum from Bulwarks' },
    'c3r2r2r1.2recoverRum': {
        'description': "Navy Panthers are swift ships that carry officer's rum, some of the best in the islands.",
        'title': 'Fine Rum from Panthers' },
    'c3r2r2r1.RecoverRum': {
        'description': "Navy ships are known to carry good quality rum on board. Plunder couple of them to satisfy Bingham's request.",
        'stringAfter': "Finally! I was gettin' downright parched!\x07Well... go on, talk to your mate before I change me mind.",
        'title': 'Bring Bingham Rum' },
    'c3r2r2r10GreersWrongs': {
        'description': "Right Greer's wrongs with other townsfolk.",
        'items': 'Victims',
        'stringAfter': "Salted ribs make the broth for me most potent healing elixir.\x07Excellent work! If ye ever tire of helping Greer, I'll give ye a job. Farewell.",
        'title': "Right Greer's Wrongs" },
    'c3r2r2r10r1.1visitBowdash': {
        'description': "Go see Andrew Bowdash in the King's Arm tavern on Tortuga - a ray of light will guide you to him.",
        'stringAfter': "Greer's cheated me so many times I've lost count!\x07I've been having some trouble with the Navy...\x07... and if you take care of it, I think I can find it in my heart to forgive, even a scalawag as vile as Greer! HA!",
        'title': 'Visit Bowdash' },
    'c3r2r2r10r1.1visitWilliam': {
        'description': 'William Turk is a scoundrel but a very wealthy trader. Be careful when dealing with Turk - and never turn your back on him!',
        'stringAfter': "That scallywag Greer has cheated me so often I've lost count!\x07But I've been having some trouble with the Navy. Take care of them for me and...\x07I'll forgive his thieving ways! HA!",
        'title': 'Visit William Turk' },
    'c3r2r2r10r1.2sinkNavyShips': {
        'description': 'Turk cheated some Navy Captains at Blackjack one night and they vowed revenge.',
        'stringAfter': "Well, well, for a scruffy pirate... you did good. Much obliged!\x07Tell Greer's he's forgiven but...\\s1slant\x01NEVER\x02... to return to this tavern!",
        'title': 'Sink Navy Ships' },
    'c3r2r2r10r1.2sinkShips': {
        'description': 'Help Bowdash with his Navy troubles by sinking ships.',
        'stringAfter': "Tell Greer we're even... 'course, I've said that a few times before! HA!",
        'title': 'Sink Navy Ships' },
    'c3r2r2r10r1.3visitGreer': {
        'description': 'Tell Greer the good news.',
        'title': 'Return To Greer' },
    'c3r2r2r10r1.WilliamTurk': {
        'description': "Straighten things out with William Turk for Greer's sake.",
        'stringAfter': "Well, well, for a scruffy pirate... you did good. Much obliged!\x07Tell Greer he's forgiven but...\x01slant\x01NEVER\x02... to return to this tavern!",
        'title': 'William Turk' },
    'c3r2r2r10r1Bowdash': {
        'description': 'Straighten things out with Andrew Bowdash.',
        'stringAfter': "Glad to hear I'm square with Bowdash... now how can I take advantage of this situation?\x07\x01slant\x01Doc Grog\x02 should be easy. He fixes people, right? He should appreciate the proposition that I want to fix things with him.\x07'Course, I did accelerate the demise of more than one of his patients...\x07Wasn't good for business, I suppose. See if there is anything we can do for 'im...",
        'stringBefore': "Let's start with \x01slant\x01Bowdash\x02.\x07At least he has a sense of fair play, in contrast to yours truly... I have a keen sense of \x01slant\x01unfair\x02 play...\x07... which is how I've cheated him so many times... buy perhaps I can make it up to him!",
        'title': 'Andrew Bowdash' },
    'c3r2r2r10r2.1visitDocGrog': {
        'description': 'Doc Grog is next on the list. Go see him in his office on Tortuga.',
        'stringAfter': "Greer? Why should I give that swine another chance?\x07But ye seem sincere, so here's what I'll do... business is booming and I can't leave so...\x07Fetch these ingredients for me medicines and I'll be straight with ole Greer. Savvy?",
        'title': 'Visit Doc Grog' },
    'c3r2r2r10r2.1visitGrog': {
        'description': 'Go see Doc Grog in his office in Tortuga - a ray of light will guide you to him.',
        'stringAfter': "I've worked hard to forget that name...\x07You asked me if I knew Greer once... and I said no. That's the result of \x01slant\x01diligence\x02 in the form of many pints of grog.\x07My plan almost worked!\x07But... I'll help you if you help me. I have a patient who needs something...",
        'title': 'Visit Doc Grog' },
    'c3r2r2r10r2.3plunderRum': {
        'description': 'Plunder bottles of fine rum for Doc Grog from Navy ships.',
        'title': 'Recover Rum' },
    'c3r2r2r10r2.3recoverRum': {
        'description': 'Plunder bottles of fine rum for Doc Grog from Navy soldiers.',
        'stringAfter': "Done then. Greer? Never heard of 'im...\x07Now off with ye! Leave me to my rum!",
        'title': 'Recover Rum' },
    'c3r2r2r10r2.4visitGreer': {
        'description': 'Return to Greer',
        'title': 'Return To Greer' },
    'c3r2r2r10r2.DocGrog': {
        'description': 'Straighten things out with Doc Grog.',
        'stringAfter': 'We be done now. Greer? Forgotten. Him and his doings...\x07Now off with ye! Leave me to my rum!',
        'title': 'Doc Grog' },
    'c3r2r2r10r2Grog': {
        'description': 'Straighten things out with Doc Grog.',
        'stringAfter': "That's a relief! It's never good to have the only doctor in town on your bad side, eh?\x07\x01slant\x01Orinda\x02 could be a tough one...\x07She is not inclined to \x01slant\x01forgive\x02... but maybe she can look past my former transgressions...\x07... with an offer of assistance regarding her li'l brother? The brat! That's her weakness, mate!\x07He's the biggest li'l pirate of all. Always pretending to be ill. What a laugh!\x07But maybe she'll take the bait...",
        'stringBefore': "\x01slant\x01Doc Grog\x02 should be easy. He fixes people, right? He should appreciate the proposition that I was to fix things with him.\x07'Course, I did accelerate the demise of more than one of his patients...\x07Wasn't good for business, I suppose. See if there is anything we can do for 'im...",
        'title': 'Doc Grog' },
    'c3r2r2r10r2r2.1recoverWaspEggs': {
        'description': 'Recover dire wasp eggs.',
        'stringAfter': 'Fine specimens, these.',
        'stringBefore': "We'll be needin' dire wasp eggs, as big as you can find...",
        'title': 'Dire Wasp Eggs' },
    'c3r2r2r10r2r2.1remedy': {
        'description': "Doc needs the fabled 'Eye of Newt' that resides in some Undead Brigands.",
        'title': 'Eye Sockets' },
    'c3r2r2r10r2r2.2recoverCrabBile': {
        'description': 'Recover sand crab bile.',
        'stringAfter': "Whew! That's potent stuff!",
        'stringBefore': 'Get some sand crab bile, if you can manage it.',
        'title': 'Sand Crab Bile' },
    'c3r2r2r10r2r2.2remedy': {
        'description': "Doc knows the best herbs are found in the Big Alligator's toenails. Get some from the beasties.",
        'title': 'Set of Toenails' },
    'c3r2r2r10r2r2.3recoverSaliva': {
        'description': 'Recover swamp alligator saliva.',
        'stringAfter': 'They sure have fine saliva, those swamp gators...',
        'stringBefore': 'Saliva, you know, spit, from one of those nasty swamp gators.',
        'title': 'Swamp Alligator Saliva' },
    'c3r2r2r10r2r2.Remedy': {
        'description': 'Doc Grog needs some ingredients for his medicines.',
        'items': 'Ingredients',
        'stringAfter': "Fine work. Now fetch me some bottles of fine rum... and I'll do my best to oblige ye in the \x01slant\x01Greer\x02 matter.\x07Those Navy blokes seem to always have the good stuff...",
        'title': 'Medicine Ingredients' },
    'c3r2r2r10r2r2Remedy': {
        'description': "Gather ingredients for Doc Grog's medicine.",
        'items': 'Ingredients',
        'stringAfter': "Forgive and forget? Better fetch me a good bottle of rum... and I'll do my best to oblige you.\x07Those Navy blokes seem to always have the good stuff...",
        'title': 'Medicine Ingredients' },
    'c3r2r2r10r3.1visitOrinda': {
        'description': 'Orinda Le Jeune is the next person that Greer has wronged. Go see her at the docks of Tortuga.',
        'stringAfter': "Forgive his lies... in exchange for what?\x07I need something. If you help, I'll say whatever you want...\x07A lady pirate, goes by the name \x01slant\x01Althea\x02, she stole a bracelet of mine. Last I heard she found work aboard a Navy ship.",
        'title': 'Visit Orinda' },
    'c3r2r2r10r3.2captureAlthea': {
        'description': 'Capture Althea from an EITC ship.',
        'title': 'Capture Althea' },
    'c3r2r2r10r3.2captureAltheaNew': {
        'description': "Althea masquerades as a cabin boy aboard a Navy Greyhound ship, but she'll never surrender so sink it to find her.",
        'title': 'Capture Althea' },
    'c3r2r2r10r3.3maroonAlthea': {
        'description': 'The only way Althea will fork over the bracelet is facing what she fears most - being marooned on a crab invested island.',
        'stringAfter': "Alright, alright! Here's the bracelet - worthless piece of junk bought me nothing but bad luck!",
        'title': 'Maroon Althea' },
    'c3r2r2r10r3.4visitFlatts': {
        'description': 'Althea sold the bracelet to Ben Flatts. Ask him for it - a ray of light will guide you to his office in Tortuga.',
        'stringAfter': 'You can have the bracelet... but I need you to make a delivery for me first.',
        'title': 'Visit Ben Flatts' },
    'c3r2r2r10r3.5smuggleRum': {
        'description': 'Smuggle rum to Port Royal for Ben Flatts - The rum has been loaded on your ship. Sail to Port Royal, and then dock there to complete the quest.',
        'stringAfter': "Okay mate. Deal's a deal. Here's your bracelet.",
        'title': 'Smuggle Rum' },
    'c3r2r2r10r3.6deliverBracelet': {
        'description': 'Bring the bracelet back to Orinda.',
        'title': 'Deliver Bracelet' },
    'c3r2r2r10r3.7visitGreer': {
        'description': 'Let Greer know of your success.',
        'stringAfter': '\x01slant\x01Lucinda\x02 could be the toughest one of all... I broke her heart I did!\x07No amount of sweet talk can float that sunken ship...\x07But give your best, mate! Looks like June has the upper hand!',
        'title': 'Return to Greer' },
    'c3r2r2r10r3Orinda': {
        'description': "Straighten things out with Orinda Le Jeune. Orinda is in the employ of the EITC collecting fees from anyone not sanctioned by the EITC. But her heart is with the Pirates. She's a fountain of information because she sees everything that comes and goes from Tortuga.",
        'stringAfter': "I don't care if it's real or not. I'm just glad to have it back. As for Greer...\x07I'll always loathe him for breakin' me heart but, if June asks... we're square.",
        'title': 'Orinda Le Jeune' },
    'c3r2r2r10r4.1stolenVoodoo': {
        'description': 'EITC Grunts get an extra sugar ration to make their drinks taste better and Lucinda needs it for a healing potion.',
        'title': 'Recover Sugar' },
    'c3r2r2r10r4.1visitLucinda': {
        'description': 'Lucinda has a powerful hatred for Jolly Roger and his undead minions and will forgive any transgression for help in ridding the Caribbean of the undead.',
        'stringAfter': "You want me to \x01slant\x01forgive\x02 Greer, again!? There's nothing you can do...\x07Wait, there is. I be needing some items for my powerful healing potion.\x07Gather 'em for me, and I'll forget his indiscretions.",
        'title': 'Visit Lucinda' },
    'c3r2r2r10r4.2stolenVoodoo': {
        'description': "Navy Veterans always carry an extra measure of gunpowder which is the 'special' ingredient in Lucinda's finest health potions.",
        'title': 'Recover Gunpowder Pouches' },
    'c3r2r2r10r4.2visitDaisy': {
        'description': "Find out what Daisy needs - a ray of light will guide you to Daisy's tattoo shop in Port Royal.",
        'stringAfter': "Lucinda sent you, did she? Well, I could use a bit of help...\x07I was gathering herbs in the jungle and I was attacked by some nasty folk...\x07... those wretched skeletons. I escaped, but they took my tattoo needles.\x07If you return them to me, I'd be grateful.",
        'title': 'Visit Daisy' },
    'c3r2r2r10r4.3recoverNeedles': {
        'description': "Recover Daisy's tattoo needles from skeletons.",
        'stringAfter': "I'll be sure to tell Lucinda you did right by me...",
        'title': 'Recover Tattoo Needles' },
    'c3r2r2r10r4.3recoverRareItem': {
        'description': 'Salted ribs are rare and are only found in the sailors that man the Phantom ships.',
        'title': 'Ribs of Undead' },
    'c3r2r2r10r4.3stolenVoodoo': {
        'description': 'Lucinda needs some empty rum bottles to let her health potions ferment.',
        'title': 'Find Empty Rum Bottles' },
    'c3r2r2r10r4.4visitLucinda': {
        'description': 'Return to Lucinda.',
        'stringAfter': 'Daisy told me you helped her... thank you!\x07Whatever you want me to tell June about her brother is fine by me...\x07I consider his debt repaid...',
        'title': 'Return to Lucinda' },
    'c3r2r2r10r4.5visitGreer': {
        'description': 'Return to Greer.',
        'title': 'Return to Greer' },
    'c3r2r2r10r4.StolenVoodoo': {
        'description': "Gather items for Lucinda's voodoo potions.",
        'stringAfter': "My customers thank ye. Now, one more item, and Greer's as good as free...\x07Salted rib bones from undead sailors. Easy enough for a pirate like ye, eh?",
        'title': 'Items for Lucinda' },
    'c3r2r2r10r4Lucinda': {
        'description': 'Right things between Greer and Lucinda.',
        'title': 'Lucinda' },
    'c3r2r2r8.4recoverPig': {
        'description': "Replace June's stolen pig by plundering large Navy ships.",
        'stringAfter': "What shall I call him? Oscar? That's a fine name for a pig.\x07Now, about the necklace...\x07It was my favorite. \x01slant\x01Lucinda\x02 would know how to make it.\x07Only she might be upset when you ask, 'cause it was first intended for her.",
        'stringBefore': 'Can you believe he stole my pig, too?',
        'title': 'Replacement Pig' },
    'c3r2r2r8.7recoverDinghy': {
        'description': "Replace June's dinghy by plundering ships.",
        'stringAfter': "That's even better than my old one!",
        'stringBefore': "I've been landlocked since Gordon stole my boat.",
        'title': "June's Dinghy" },
    'c3r2r2r8JunesList': {
        'description': 'June has a long list of things that Greer stole from her and sold for grog and gambling. They are now scattered to the 4 winds and could be anywhere.',
        'items': 'Stolen Items',
        'stringAfter': 'I knew my Peter would enjoy them. Now, the next item on the list is... a necklace.',
        'title': "June's Stolen Items (Part 1)" },
    'c3r2r2r8JunesList2': {
        'description': 'June has a long list of things that Greer stole from her and sold for grog and gambling. They are now scattered to the 4 winds and could be anywhere.',
        'items': 'Stolen Items',
        'stringAfter': "You're set like flint on gettin' him out, eh?\x07Well, in that case, I've got another one...\x07I surely miss my parrot... pretty as a picture, she was.",
        'title': "June's Stolen Items (Part 2)" },
    'c3r2r2r8JunesList3': {
        'description': 'June has a long list of things that Greer stole from her and sold for grog and gambling. They are now scattered to the 4 winds and could be anywhere.',
        'items': 'Stolen Items',
        'stringAfter': "I guess I can forgive him. But there are lots of other people he's wronged...\x07And until Gordon makes things right with them... he's still a pirate.\x07Take this list to him... if he has really changed his ways he'll know what to do!",
        'title': "June's Stolen Items (Part 3)" },
    'c3r2r2r8r1.1ringMaterials': {
        'description': 'Navy Marines in the Royal Caverns carry iron ore bits to ward off the undead.',
        'title': 'Recover Navy Ore' },
    'c3r2r2r8r1.1visitSmitty': {
        'description': "Have a jeweler re-create June's ring.",
        'stringAfter': "Ah... the \x01slant\x01Greer\x02 diamond... that's what I like to call it. Ha! Utterly \x01slant\x01worthless\x02!\x07Why bother with it? I could make you one... but I usually don't work in \x01slant\x01glass\x02 and \x01slant\x01tin\x02.\x07Get these items and I'll fashion ye one...",
        'title': 'Visit A Jeweler' },
    'c3r2r2r8r1.2ringMaterials': {
        'description': "Smitty needs refined sand the Navy posseses to recreate the glass for June's ring.",
        'title': 'Steal Refined Sand' },
    'c3r2r2r8r1.3deliverRing': {
        'description': "Once you return the ring to June, she'll be forever in your debt - so don't tarry.",
        'title': 'Deliver Ring' },
    'c3r2r2r8r1.RingMaterials': {
        'description': "Acquire materials to re-create June's ring.",
        'items': 'Materials',
        'stringAfter': "Ye did a fine job gathering the materials. Give me a moment...\x07Here. Take June the ring. She won't know it from the original.",
        'title': 'Ring Materials' },
    'c3r2r2r8r11.1visitGreer': {
        'description': "Ask Greer about June's red dress.",
        'stringAfter': "I almost feel bad about this one... it was June's \x01slant\x01favorite\x02 dress and all...\x07But it looked real nice on \x01slant\x01Cassandra\x02...\x07Oh me festerin' soul! Not much there for Jolly Roger to scavenge!\x07HA! What a lot of rot! Toss off!",
        'title': 'Visit Greer' },
    'c3r2r2r8r11.2visitCassandra': {
        'description': "Ask Cassandra to return June's red dress - Cassandra can be found near the Royal Anchor on Port Royal.",
        'stringAfter': "Wants it back, does he?\x07Well, I hope you're prepared to pay me...\x07Two gentlemen from the East India Trading Company stopped by to collect... taxes.\x07But I'm in the market for a refund in the form of a pair of earrings.\x07Bring 'em back and you can have the red dress.",
        'title': 'Visit Cassandra' },
    'c3r2r2r8r11.3recoverEarrings': {
        'description': "Steal Cassandra's earrings back from the East India company - EITC soldiers can be found in Fort Charles on Port Royal.",
        'stringAfter': 'You might want to wash that dress before you wear it.',
        'title': "Recover Cassandra's Earrings" },
    'c3r2r2r8r11.4deliverDress': {
        'description': 'Give June back her red dress',
        'title': "Return June's Dress" },
    'c3r2r2r8r11Dress': {
        'description': "Return June's favorite red dress.",
        'stringAfter': "I never thought I'd see that dress again!",
        'stringBefore': 'Ask my sorry excuse for a brother what he did with my favorite red dress.',
        'title': 'Red Dress' },
    'c3r2r2r8r1Ring': {
        'description': "Jeweler Smitty in Port Royal might be able to replace June's ring",
        'stringAfter': 'A perfect replica! Beautiful, ey? Now, next on me list... I had a nice flock of chickens, lovely little things that were like me pets.\x07Gordon stole them as well. Replace me flock so I can give the eggs to my beloved, Peter.',
        'stringBefore': "I so miss my ring. 'Twas a gift from Gordon, actually.\x07To replace it, you'll need to see a jeweler... name's \x01slant\x01Smitty\x02.",
        'title': "June's Ring" },
    'c3r2r2r8r1r2.1recoverTin': {
        'description': 'Recover a shipment of tin by sinking Navy ships.',
        'stringAfter': 'Mmm, low grade tin... perfect!',
        'stringBefore': "I'll need a shipment of tin to start.",
        'title': 'Shipment of Tin' },
    'c3r2r2r8r1r2.2recoverSand': {
        'description': 'Recover shipments of sand by sinking East India Trading Company (EITC) ships.',
        'stringAfter': "This will do for the glass we're making.",
        'stringBefore': 'We need sand, only not the common stuff you find on the beach... but for glass-making.',
        'title': 'Shipment of Sand' },
    'c3r2r2r8r1r2RingMaterials': {
        'description': "Acquire materials to re-create June's ring.",
        'items': 'Materials',
        'stringAfter': "Okay, with these I can make it, sure.\x07Not putting my seal on it - this is a worthless piece of trash. But I'll make it, sure.",
        'stringBefore': "I'll need a shipment of tin to start.",
        'title': 'Ring Materials' },
    'c3r2r2r8r2.1.5bribeCraven': {
        'description': 'Pay Bastien Craven\'s "Fee" for his services.',
        'stringAfter': "Now, driftwood comes in two varieties... fresh, and not so fresh.\x07You'll speed things up if you \x01slant\x01make\x02 some \x01slant\x01fresh\x02 driftwood, if you follow...",
        'title': 'Pay Bastien Craven' },
    'c3r2r2r8r2.1visitCraven': {
        'description': "Locate driftwood sculptor Bastien Craven on Rumrunner's Isle - a ray of light will guide you there.",
        'stringAfter': 'Driftwood, eh? I should be able to help you there... for a fee, of course...',
        'title': 'Visit Bastien Craven' },
    'c3r2r2r8r2.2sinkShips': {
        'description': 'Sink ships in the area to create fresh driftwood.',
        'stringAfter': "Your driftwood attracted the attention of some blokes from the Navy. I put up a good fight...\x07... but I gave 'em your name in the end!\x07You might want to tie up some loose ends if you know me meanin'...\x07... meanwhile, I'll be working on your plates.",
        'title': 'Sink Ships' },
    'c3r2r2r8r2.3sinkNavyShips': {
        'description': 'Sink Navy ships to cover the trail.',
        'stringAfter': "All done! Here you go... they're not pretty, but at least they won't give you splinters, eh?",
        'title': 'Sink Navy Ships' },
    'c3r2r2r8r2.4deliverPlates': {
        'description': 'Deliver plates to June.',
        'title': 'Deliver Plates' },
    'c3r2r2r8r2Plates': {
        'description': "Replace June's wooden dinner plates.",
        'stringAfter': "I'll be able to set a fine table once again with this lot!",
        'stringBefore': "I'll be able to set a fine table once again with this lot, but...\x07I sure miss having fresh eggs... but don't bother with the scrawny chickens running about town.\x07You'll need to find healthy chickens that can lay eggs.",
        'title': 'Wooden Dinner Plates' },
    'c3r2r2r8r3.1chickenCrates': {
        'description': 'June is obsessed with eggs, and chickens, and you must help her to free Greer.',
        'stringAfter': "Aren't they lovely? The chickens I mean. So noble and handsome...\x07Reminds me of Peter. Please gather some more chickens for my beloved. He loves eggs.",
        'title': 'Find Chickens in Crates' },
    'c3r2r2r8r3.1recoverChickens': {
        'description': 'Plunder chickens by searching crates around Port Royal - crates that are searchable will highlight with a green circle.',
        'stringAfter': "That lot is pretty good, but my Peter \x01slant\x01loves\x02 his eggs, so you'll need to find more.",
        'title': 'Plunder Chickens' },
    'c3r2r2r8r3.2recoverChicken': {
        'description': 'June thinks that her beloved Lt. Blakeley loves eggs... so plunder more from Navy ships',
        'stringAfter': 'These chickens are even more adorable!\x07Bring these eggs to Peter, he will be grateful.',
        'title': 'Plunder Chickens from Navy' },
    'c3r2r2r8r3.2recoverChickens': {
        'description': 'Plunder chickens from Navy ships.',
        'stringAfter': "Bring Peter this basket of eggs for me, will you?\x07You know... the surest path to a man's heart is through his stomach.\x07Hurry! They're fresh!",
        'title': 'Plunder Chickens' },
    'c3r2r2r8r3.3deliverEggs': {
        'description': 'Deliver fresh eggs to Peter Blakeley.',
        'stringAfter': "Me eat eggs? Are you mad? I only tolerate them because my dear June thinks otherwise\x07So I keep up the charade. Now leave. I've had my fill of you, pirate.",
        'title': 'Deliver Eggs' },
    'c3r2r2r8r3.4visitJune': {
        'description': 'Return to June after delivering eggs.',
        'title': 'Return to June' },
    'c3r2r2r8r3Chickens': {
        'description': "Replace June's flock of chickens.",
        'stringAfter': 'I knew my Peter would enjoy them. Now, the next item on the list is... a necklace.',
        'title': 'Chickens' },
    'c3r2r2r8r5.1.5bribeLucinda': {
        'description': "Bribe Lucinda to help you make June's necklace.",
        'stringAfter': "Fine then, here's what ye need to do...\x07Teeth! We needs lots of teeth!",
        'title': 'Bribe Lucinda' },
    'c3r2r2r8r5.1necklaceMaterials': {
        'description': 'The skeleton teeth are a staple in island jewelry.',
        'title': 'Recover Undead Teeth' },
    'c3r2r2r8r5.1visitLucinda': {
        'description': "Lucinda should know how to make June's necklace.",
        'stringAfter': 'Greer! I loathe that bilge rat! To help you help \x01slant\x01him\x02 will cost you... some favors, mate.',
        'title': 'Visit Lucinda' },
    'c3r2r2r8r5.2necklaceMaterials': {
        'description': "Inside the shakers are valuable stones Lucinda needs for June's replacement necklace.",
        'title': 'Recover Gourd Shakers' },
    'c3r2r2r8r5.3deliverNecklace': {
        'description': 'Deliver the tooth necklace to June.',
        'title': 'Deliver Necklace' },
    'c3r2r2r8r5.3necklaceMaterials': {
        'description': 'Bile is the base for a rare but amazingly strong glue used in jewelry making.',
        'title': 'Recover Bile Sacks' },
    'c3r2r2r8r5.NecklaceMaterials': {
        'description': 'Gather materials needed to make a replacement necklace.',
        'stringAfter': "Now that ye have gathered all the parts for June's necklace...\x07String it together yerself! Now be gone and good riddance!",
        'title': 'Necklace Materials' },
    'c3r2r2r8r5Necklace': {
        'description': "Replace June's favorite necklace.",
        'stringAfter': "Strange, I don't remember it being so... ugly.\x07Now... Gordon also stole me jewelry box with all me keepsakes inside - a piece of lace, me grandma's brooch and a few other things.\x07Find all the items for me, won't you?",
        'title': "June's Necklace" },
    'c3r2r2r8r5r2.1recoverTeeth': {
        'description': 'Recover cave bat teeth for the necklace - bats live in a cave beyond the jungle in Port Royal.',
        'title': 'Cave Bat Teeth' },
    'c3r2r2r8r5r2.2recoverTeeth': {
        'description': 'Recover swamp alligator teeth for the necklace.',
        'title': 'Swamp Alligator Teeth' },
    'c3r2r2r8r5r2NecklaceMaterials': {
        'description': 'Gather materials needed to make a replacement necklace.',
        'title': 'Necklace Materials' },
    'c3r2r2r8r5r3.1recoverSpecial': {
        'description': 'Gordon can only remember that the men that bested him at poker sailed on EITC Corvettes - plunder them to get the items returned.',
        'title': 'Recover Jewelry Box Items' },
    'c3r2r2r8r5r3.2recoverSpecial': {
        'description': 'Love letters Blakeley wrote to June were in the box and they might be embarrassing if revealed to others. Navy Captains now hold them with the intent to blackmail Blakeley when the time is right!',
        'title': "Find June's love letters" },
    'c3r2r2r8r5r3.RecoverSpecial': {
        'description': "Gordon Greer sold his sister's jewelry box. The box was worthless but some of the items in it were very important to June. Greer quickly lost them all in a poker game to some EITC sailors.",
        'stringAfter': "Ah, all the things from me jewelry box - so precious to me! Thank ye so kindly!\x07And the uh, \x01slant\x01letters\x02 as well. Excellent. Next on the list...\x07Gordon stole a voodoo doll from me that's powerful indeed. Recover it, but be careful.",
        'title': "June's Jewelry Box" },
    'c3r2r2r8r6.1visitGreer': {
        'description': 'Ask Greer where the doll is.',
        'stringAfter': "Stole a doll, eh? Oh... \x01slant\x01that\x02 doll. What a piece of bad luck that was...\x07See, I \x01slant\x01borrowed\x02 it from Fabiola, \x01slant\x01lent\x02 it to June... then I \x01slant\x01repossessed\x02 it from June and \x01slant\x01stole\x02 it from Fabiola.\x07So I didn't actually \x01slant\x01steal\x02 it from June, see?\x07I guess she didn't want an explanation so much as she wanted her doll back, eh? So who has it, eh?\x07That be \x01slant\x01Mallet\x02, mate.\x07I \x01slant\x01sold\x02 it to Andros Mallet. What he's done with it... can't say.\x07Good luck, mate!",
        'title': 'Visit Greer' },
    'c3r2r2r8r6.1visitStormhawk': {
        'description': 'Greer sold the voodoo doll to the scavenger Edward Stormhawk and it has cursed his taste buds.',
        'stringAfter': "Curse that scalawag, Greer! Ever since he sold me this cursed voodoo doll, me grog tastes like dirt.\x07Biscuits are like sand, everything tastes wretched! Help me lift this curse and ye can have the doll!\x07Go ask \x01sland\x01Angel O'Bonney\x02. She'll know what to do.",
        'title': 'Visit Stormhawk' },
    'c3r2r2r8r6.2visitAngel': {
        'description': "Ask Angel O'Bonney to help cure Stormhawk's taste bud curse - before he starves to death!",
        'stringAfter': "Stormhawk's grog tastes like dirt?\x07Hold on... does this have anything to do with the doll Greer stole from me?\x07The pox on him! This favor will cost you plenty...",
        'title': 'Visit Angel' },
    'c3r2r2r8r6.2visitMallet': {
        'description': 'Find Andros Mallet in the graveyard on Tortuga - the graveyard is in the center jungle on Tortuga - a ray of light will guide you.',
        'stringAfter': "Cursed doll!\x07Curse that scalawag Greer. Ever since he sold me this cursed voodoo doll, me grog tastes like dirt.\x07Nothin' \x01slant\x01tastes\x02 proper. These biscuits, here, taste like... well, you don't wanna know...\x07I need a way to lift the curse... find it and I'll gladly give up the doll.\x07\x01slant\x01Fabiola\x02 will know how - go ask her.",
        'title': 'Visit Mallet' },
    'c3r2r2r8r6.3.5bribeFabiola': {
        'description': "Bribe Fabiola to help cure Mallet's curse.",
        'stringAfter': "Okay, here's what we'll need...",
        'title': 'Bribe Fabiola' },
    'c3r2r2r8r6.3visitFabiola': {
        'description': "Ask Fabiola to help cure Mallet's curse - find Fabiola near her wagon in Tortuga.",
        'stringAfter': "Mallet's grog tastes like dirt?\x07... maybe he should start tipping his bartender!\x07Does this have something to do with the doll Greer stole from me?\x07The pox on him! This favor will cost you plenty...",
        'title': 'Visit Fabiola' },
    'c3r2r2r8r6.4deliverCure': {
        'description': 'Put Edward Stormhawk out of his misery by delivering him the cure to the taste bud curse.',
        'stringAfter': "Ahhhh! I can taste the bitterness of this potion so...\x07I must be cured! Well done, mate! Here's yer stinkin' doll - glad to be rid of it!",
        'title': 'Deliver Cure' },
    'c3r2r2r8r6.5deliverDoll': {
        'description': 'Give June her voodoo doll.',
        'title': 'Deliver Doll' },
    'c3r2r2r8r6.5deliverRemedy': {
        'description': 'Deliver cure to Mallet for his curse.',
        'stringAfter': 'How can I be sure it worked?\x07Go fetch me a pint of grog...',
        'title': 'Deliver Cure' },
    'c3r2r2r8r6.6.5bribeCarver': {
        'description': 'Pay for grog for Mallet.',
        'stringAfter': 'Here you go.',
        'title': 'Pay For Grog' },
    'c3r2r2r8r6.6visitCarver': {
        'description': 'Buy grog for Mallet from Carver the barkeep at the Faithful Bride tavern in Tortuga - a ray of light will guide you.',
        'stringAfter': 'Pay up, mate.',
        'title': 'Buy Some Grog' },
    'c3r2r2r8r6.7deliverGrog': {
        'description': "Deliver grog to Mallet to see if he's cured.",
        'stringAfter': "It don't taste like dirt! It's not that good either but...at least it don't taste like dirt!\x07Here you go... me taste buds say thanks, mate!",
        'title': 'Deliver Grog' },
    'c3r2r2r8r6.8deliverDoll': {
        'description': 'Deliver doll to June in Port Royal.',
        'title': 'Deliver Doll' },
    'c3r2r2r8r6.Doll': {
        'description': "Replace June's Voodoo doll.",
        'stringAfter': "You're set like flint on gettin' him out, eh?\x07Well, in that case, I've got another one...\x07I surely miss my parrot... pretty as a picture, she was.",
        'title': "June's Doll" },
    'c3r2r2r8r6Doll': {
        'description': "Replace June's Voodoo doll.",
        'stringAfter': 'Oh... smashing! Thank you!',
        'stringBefore': 'Only \x01slant\x01Gordon\x02 knows where that doll is now.',
        'title': "June's Doll" },
    'c3r2r2r8r6r3.1curseCure': {
        'description': "Killer Wasp stingers are the main ingredient in Angel's curse breaking potion.",
        'title': 'Wasp Stingers' },
    'c3r2r2r8r6r3.2curseCure': {
        'description': "Scorpion venom is crucial to breaking the voodoo doll's curse on Stormhawk.",
        'title': 'Scorpion Venom' },
    'c3r2r2r8r6r3.3curseCure': {
        'description': 'Vampire bats are not part of the cure, Angel just despises them - consider it a favor for her instance.',
        'title': 'Vampire Bat Favor' },
    'c3r2r2r8r6r3.CurseCure': {
        'description': "Gather ingredients for the remedy that can cure Stormhawk's curse.",
        'items': 'Ingredients',
        'stringAfter': "Now I have the ingredients, I can make Stormhawk a cure...\x07And thanks for helping rid the island of those dreadful Vampire bats...\x07They're vile creatures, indeed.",
        'title': 'Curse Remedy' },
    'c3r2r2r8r6r4.1recoverWings': {
        'description': "Gather dire wasp wings for Fabiola's cure.",
        'stringAfter': 'Excellent!',
        'stringBefore': "We'll need dire wasp wings.",
        'title': 'Dire Wasp Wings' },
    'c3r2r2r8r6r4.2recoverScales': {
        'description': "Gather swamp alligator scales for Fabiola's cure.",
        'stringAfter': 'Is that all you could get?',
        'stringBefore': 'Swamp alligator scales will do nicely for this bit.',
        'title': 'Swamp Alligator Scales' },
    'c3r2r2r8r6r4.3recoverPoison': {
        'description': "Gather giant scorpion poison for Fabiola's cure.",
        'stringAfter': "Careful, don't spill it.",
        'stringBefore': "Be careful handling scorpion poison... 'tis strong medicine.",
        'title': 'Scorpion Poison' },
    'c3r2r2r8r6r4.4recoverClaw': {
        'description': "Gather crab claws for Fabiola's cure.",
        'stringAfter': 'These will do.',
        'stringBefore': "We'll grind crab claws into dust for the cure.",
        'title': 'Crab Claws' },
    'c3r2r2r8r6r4.5recoverMud': {
        'description': "Get some cold mud for Fabiola's cure - recover mud from the belly of a big alligator.",
        'stringAfter': "That's good mud, you've done well.",
        'stringBefore': "Can't cure this curse without some cold swamp mud.\x07It works best if you get it from the belly of a big alligator - don't ask.",
        'title': 'Cold Mud' },
    'c3r2r2r8r6r4CurseCure': {
        'description': "Gather ingredients for a remedy for Mallet's curse.",
        'items': 'Ingredients',
        'stringAfter': 'Okay, now we need a few more things...',
        'title': 'Curse Remedy' },
    'c3r2r2r8r6r4CurseCure2': {
        'description': "Gather more ingredients for a remedy for Mallet's curse.",
        'items': 'Ingredients',
        'stringAfter': 'Good. Mallet dropped off your doll for me to hand over once his cure was secured. Be careful with it.',
        'title': 'Curse Remedy #2' },
    'c3r2r2r8r8.1recoverJewelry': {
        'description': 'Some EITC thugs stole her earings for their sweethearts - get them back!',
        'title': "Cassandra's Earings" },
    'c3r2r2r8r8.1visitCassandra': {
        'description': "Go see if Cassandra knows where June's parrot is.",
        'stringAfter': "What would you want with that ugly parrot? Either way it's going to cost you.\x07Bring me back some barrels of fine honey, that sounds fair.",
        'title': 'Visit Cassandra' },
    'c3r2r2r8r8.1visitGreer': {
        'description': "Go ask Greer about June's parrot.",
        'stringAfter': "That parrot was quite a talker...\x07Painted him \x01slant\x01blue\x02 I did, and sold 'im to \x01slant\x01Orinda\x02, seeing as she was in the market for a \x01slant\x01blue\x02 one.\x07Stupid parrot was screamin' \x01slant\x01'Red!'\x02 over and over! That bird spilled his guts, he did...\x07And she might have spilled \x01slant\x01my\x02 guts... 'cept I told her that 'Red' was the name of his previous owner...\x07She believed me! ... and the exchange went through, so to speak.\x07I didn't know she needed a blue one, on account of her sick \x01slant\x01brother\x02... but no harm done in the end.\x07Talk to \x01slant\x01Orinda\x02 in Tortuga... best not mention I'm involved though, eh mate?",
        'title': 'Visit Greer' },
    'c3r2r2r8r8.2recoverHoney': {
        'description': "Cassandra wants some honey in exchange for information about June's parrot.",
        'stringAfter': "Excellent! Now I want what every \x01slant\x01lady\x02 wants... some trinkets.\x07Don't look like I'm daft! I want the jewelry returned that was stolen from me!",
        'title': 'Plunder Honey' },
    'c3r2r2r8r8.2recoverJewelry': {
        'description': 'Some Navy bullies stole her rings one night when she took them off to bathe.',
        'title': "Cassandra's Rings" },
    'c3r2r2r8r8.2visitOrinda': {
        'description': 'Go see if Orinda knows where the parrot is - Orinda works at the docks in Tortuga.',
        'stringAfter': 'What would you want with that ugly parrot? Either way its going to cost you.\x07Bring me back 20 barrels of fine honey, that sounds fair.',
        'title': 'Visit Orinda' },
    'c3r2r2r8r8.3visitTomas': {
        'description': "Ask Tomas to return the parrot - a ray of light will guide you to Tomas' shack near the docks in Tortuga.",
        'stringAfter': "You can't take me Juniper! NO! No! No!\x07Save me!\x07I wouldn't part with her for 10 barrels of the finest honey!\x07PARROT: 20 barrels! 20 barrels!\x07Mmmm... \x01slantP barrels\x02 of honey. Oh how I love honey!\x07PARROT: Mmmmmmmm...\x07Yes, I do think I would part with my dearest Juniper for 20 barrels of fine honey!\x07Navy's bound to have a shipment or two of honey on the move.",
        'title': 'Visit Tomas' },
    'c3r2r2r8r8.5deliverParrot': {
        'description': "Return June's parrot to her.",
        'title': 'Deliver Parrot' },
    'c3r2r2r8r8.RecoverJewelry': {
        'description': 'In exchange for helping you, Cassandra needs some precious jewelry recovered.',
        'stringAfter': "My rings! My earrings! I have them again! I'm overwhelmed with gratitude!\x07Go on, take the bird. Never liked it, truth be told.",
        'title': 'Recover Jewelry for Cassandra' },
    'c3r2r2r8r8Parrot': {
        'description': "Get back June's parrot.",
        'stringAfter': "I guess I can forgive him. But there are lots of other people he's wronged...\x07And until Gordon makes things right with them... he's still a pirate.\x07Take this list to him... if he has really changed his ways he'll know what to do!",
        'stringBefore': 'I surely miss my parrot... pretty as a picture, she was.',
        'title': "June's Parrot" },
    'c3r2r2r8r8r4.1recoverHoneyShips': {
        'description': 'Sink Navy ships to recover honey.',
        'stringAfter': "10 barrels? Delicious!\x07Now where to get 10 more...\x07A smuggler's bound to have honey. I'd try \x01slant\x01Ben Flatts\x02.",
        'stringBefore': "The Navy's bound to have a shipment or two of honey on the move",
        'title': 'Plunder 10 Barrels of Honey' },
    'c3r2r2r8r8r4Honey': {
        'description': 'Acquire 10 of the barrels of honey to trade for the parrot.',
        'stringAfter': "Mmmm... that is \x01slant\x01fine\x02 honey... Here's your parrot.",
        'title': 'Acquire 10 Barrels of Honey for Orinda' },
    'c3r2r2r8r8r4r2.1visitMarsh': {
        'description': "See if Ben Flatts will sell honey - a ray of light will guide you to Flatts' office in Tortuga.",
        'stringAfter': "Let me see... I seem to remember having a shipment of the King's finest honey somewhere...\x07Might help my memory if ye produced some gold, eh?",
        'title': 'Visit Ben Flatts' },
    'c3r2r2r8r8r4r2.2bribeMarsh': {
        'description': 'Pay Ben Flatts for the rest of the honey.',
        'stringAfter': 'Ye drive a hard bargain, mate. Enjoy the honey.',
        'title': 'Pay Flatts' },
    'c3r2r2r8r8r4r2.3deliverHoney': {
        'description': 'Deliver the 10 barrels of honey to Orinda.',
        'stringAfter': "I'll miss her.",
        'title': 'Deliver Honey' },
    'c3r2r2r8r8r4r2Bribe': {
        'description': 'Buy contraband honey from the smuggler Ben Flatts.',
        'stringBefore': "A smuggler's bound to have honey. I'd try your luck at bribing \x01slant\x01Ben Flatts\x02.",
        'title': 'Buy 10 Barrels of Honey' },
    'c3r2r2r8r9.1visitGreer': {
        'description': "Ask Greer about June's lucky dice.",
        'stringAfter': "I know it sounds strange but I lost me dice at cards...\x07... then the bloke that won 'em got himself jumped by some skeletons in the jungle.\x07That's where I'd start looking if I wanted to get 'em back.",
        'title': 'Visit Greer' },
    'c3r2r2r8r9.2recoverDice': {
        'description': "Recover June's lucky dice from skeletons in the jungle.",
        'stringAfter': "Good work mate. Give 'em to June with my blessing.",
        'title': 'Recover Dice' },
    'c3r2r2r8r9.3deliverDice': {
        'description': 'Return the lucky dice to June.',
        'title': 'Deliver Dice' },
    'c3r2r2r8r9Dice': {
        'description': "Return June's set of lucky dice.",
        'stringAfter': "Aye, those are the very dice. Now hand 'em over...\x07... and ask my sorry excuse for a brother what he did with my favorite red dress.",
        'stringBefore': 'Who knows what Gordon did with my dice... and they were lucky too.',
        'title': 'Lucky Dice' },
    'c3r2r3.10deliverJack': {
        'description': 'Take the document to Jack Sparrow in the Faithful Bride.',
        'stringAfter': "This gibberish the best you could find? Okay, a deal's a deal. So here's your pearl.\x07Tell Cutts he's a living proof that love is indeed blind!",
        'title': 'Deliver Document' },
    'c3r2r3.11deliverPearl': {
        'description': 'Take the last pearl to Hendry Cutts.',
        'stringAfter': "You've done right by me, mate. Take this necklace to \x01slant\x01Millie\x02 and tell her I'll miss her...\x07...but not enough to stay, ha!",
        'title': 'Deliver Pearl To Cutts' },
    'c3r2r3.12deliverMillie': {
        'description': 'The necklace should please Millie enough to let Hendry go.',
        'stringAfter': "I can't believe it! I don't know what you want with my husband but you can have 'im!\x07All this just to serve \x01slant\x01under\x02 Jack Sparrow! Believe me, it's not worth it...",
        'title': 'Deliver Necklace' },
    'c3r2r3.13visitCutts': {
        'description': 'Tell Cutts he is free to go.',
        'stringAfter': "Free at last! Tell Joshamee I'll stop by to sign the papers.",
        'title': 'Visit Cutts' },
    'c3r2r3.14visitJoshamee': {
        'description': 'Let Joshamee know that Cutts is ready to sign up.',
        'title': 'Return To Joshamee' },
    'c3r2r3.1navyDocument': {
        'description': 'Rumor has it that the 1st Mate on a Navy Vanguard has the papers Jack needs. But to impress Captain Sparrow, sink 3 of them for good measure!',
        'title': 'Navy Vanguards' },
    'c3r2r3.1visitScarlet': {
        'description': 'Ask Scarlet about Cutts - Scarlett is walking around in front of the Faithful Bride tavern in Tortuga.',
        'stringAfter': "Yes, I know him. What do you want with him?\x07I will help you... but you need to do me a favor first.\x07There's an old chest buried near my sister Millie's place...\x07Bring me what's inside.",
        'title': 'Ask Scarlet' },
    'c3r2r3.2navyDocument': {
        'description': 'Jack heard from his spies that some other vital document is aboard a Navy Centurion.',
        'title': 'Hidden Document' },
    'c3r2r3.2recoverEffects': {
        'description': "Buried chests appear as a green circle under your feet when you walk over them, or even near them. Look for this chest near Hendry's home.",
        'stringAfter': 'Is this everything? Okay, I guess this should do.\x07If you want to speak to Hendry, you should speak first to his wife.\x07Go talk to my sister Millie',
        'title': 'Return Contents of Chest' },
    'c3r2r3.3visitMillie': {
        'description': 'Ask Millie about her husband, Hendry Cutts.',
        'stringAfter': "Hmmm.  Okay, I give you permission to speak with Hendry.\x07He's choppin' wood up the path to town. It's all he's good for, I say.",
        'title': 'Talk To Millie' },
    'c3r2r3.4visitCutts': {
        'description': "Hendry Cutts is busily chopping wood near Millie's cottage in Tortuga.",
        'stringAfter': "Sparrow, wants me back, eh? Last I saw him we drank too much grog and when I woke up...\x07...he was gone and I was married! Seems that I promised her a certain necklace if she'd marry me.\x07Had it once, then it was stolen and sold off, one pearl at a time, and I bought back one single pearl.\x07Help me get the rest of the necklace and she'll let me go... I know it in me bones.",
        'title': 'Talk To Cutts' },
    'c3r2r3.8visitJack': {
        'description': 'Jack Sparrow has the final pearl that Cutts needs.',
        'stringAfter': "Cutts isn't the only one who wants his pearl back.\x07Look, I'll make you a deal that's sure to please his barracuda of a bride...\x07Find my pearl and I'll give you his - savvy?\x07The Navy's holding the Black Pearl somewhere... and the Navy does nothing without paperwork.\x07Find me said papers and we'll know where to look for my wayward bride... the \x01slant\x01Black Pearl\x02.",
        'title': 'Visit Jack Sparrow' },
    'c3r2r3.9recoverPapers': {
        'description': 'Plunder Navy ships to find a document that could lead to the Black Pearl.',
        'title': 'Recover Document' },
    'c3r2r3.NavyDocument': {
        'description': "The Navy's holding the Black Pearl in a secret location. Earn Jack Sparrow's respect and trust by finding the Pearl's paper trail.",
        'stringAfter': "3 Vanguards? I am impressed. Of course, I sunk 4 with nothing but a whalebone and corset.\x07Don't ask how. These documents will help but they're just a start.\x07Here's your pearl, and tell Cutts he's living proof that love is indeed... blind.",
        'title': 'Black Pearl Documents' },
    'c3r2r3Cutts': {
        'description': 'Liberate Hendry Cutts from an overbearing wife.',
        'stringAfter': "Ole' Cutts owes ye one for this, I'll wager. Got another one for you now...\x07\x01slant\x01Nill Offrill\x02's somewhat of a gambler. Never wins though, so I'll wager he's run up some debt by now.",
        'stringBefore': 'Rumor on Cutts is he got himself married.\x07Married or not, Scarlet will know his whereabouts.',
        'title': 'Black Pearl Recruit: Hendry Cutts' },
    'c3r2r3r1.1RecoverSkeletons': {
        'description': 'Steal back a pair of pearls from skeletons.',
        'stringAfter': "You found the pearls I lost, eh? Good.\x07\x01slant\x01Bowdash\x02 has a pair of pearls that he wears as cufflinks.\x07Unlikely he'll want to part with them though...",
        'stringBefore': "I had a few more on me... but I was attacked by bandits in the jungle...\x07And they weren't living beings neither, if you get me drift.",
        'title': 'Stolen By Skeletons' },
    'c3r2r3r1.1recoverPearls': {
        'description': 'Steal back a pair of pearls from skeletons.',
        'stringAfter': "You found 4 of me precious pearls? Good start. Now...\x07\x01slant\x01Bowdash\x02 has a pair of pearls he wears as cufflinks, so it's unlikeley he'll part with them easily...",
        'title': 'Stolen Pearls' },
    'c3r2r3r1.3pearlsOnShips': {
        'description': 'A pearl was given to 3 EITC Captains as a reward for a raid on Tortuga. Sink their ships to get revenge... and the pearls for Hendry.',
        'title': 'Pearls At Sea' },
    'c3r2r3r1.3recoverShips': {
        'description': 'Six pearls ended up at sea - sink large Navy ships to recover them.',
        'stringAfter': "Didn't think I'd be seeing you again... you be tougher than you look.",
        'title': 'Pearls At Sea' },
    'c3r2r3r1.4pearlsOnNavy': {
        'description': "Some Navy Veterans got possesion over some of Cutt's pearls. Get them back!",
        'stringAfter': "Impressive work, mate. For the other pearls, I have no clue where they be.\x07But Rumrunners know 'bout everything that moves through the Caribbean', and...\x07\x01slant\x01Ben Flatts\x02 knows all about that profession. Speak to him.",
        'title': 'Navy Soldiers' },
    'c3r2r3r1.4recoverNavy': {
        'description': 'Steal a pair of pearls back from Navy soldiers on Port Royal.',
        'stringAfter': "Good work, now for more pearls...\x07If there's anyone who knows where to find a scrap of plunder... it's a rumrunner.\x07They've got their hands on everything that moves through the Caribbean... everything.\x07Go talk to \x01slant\x01Orinda\x02. She'll know who dabbles in this particular sort of knick-knack.",
        'stringBefore': "I overheard some Navy blokes talking about a ship carrying some strange looking pearls...\x07They're being held in Fort Charles by now I'll wager.",
        'title': 'Navy Soldiers' },
    'c3r2r3r1Pearls': {
        'description': 'Help Hendry Cutts get his pearls back',
        'stringAfter': "Well, well, aren't you a scrappy one? Tougher than you look, I'd say.\x07Only a few more and the necklace is done and me freedom is won...\x07Hey, that rhymes!",
        'title': "Recover Cutts' Pearls" },
    'c3r2r3r1Pearls2': {
        'stringAfter': "Good work, mate! Almost there, now...\x07I heard about this bloke once... who collected pearls.\x07They were an obsession with 'im. Worth more than gold to 'im they was...\x07Problem is... he's got killed.\x07Go see if \x01slant\x01Mallet\x02 the gravedigger remembers who I'm talkin' about.\x07Maybe one of \x01slant\x01them\x02 pearls... is \x01slant\x01our\x02 pearls.",
        'title': "Recover Cutts' Pearls" },
    'c3r2r3r1r2.1sinkShips': {
        'description': "Sinking a few EITC ships will send a loud and clear message to 'back off Bowdash!'",
        'title': 'Sink EITC Corvettes' },
    'c3r2r3r1r2.1visitBowdash': {
        'description': "Ask Andrew Bowdash for Cutts' pearls in his cufflinks.",
        'stringAfter': "What's with you and Cutts? Why do you care so much about a pair of common pearls?\x07Well, I just lost lots of gold to a bloke at the poker table.\x07Earn some of me money back and I'll give you the pearls as a reward.",
        'title': 'Visit Bowdash' },
    'c3r2r3r1r2.2poker': {
        'description': "Win back some of Bowdash's money at Tortuga Hold 'Em Poker.",
        'stringAfter': 'Blimey, you did good for an amateur, but...\x07Not good enough for the cufflinks yet, mate. I need some help keeping the EITC tax collectors from pestering me, savvy?',
        'title': 'Win At Poker' },
    'c3r2r3r1r2.2sinkShips': {
        'description': "EITC Sentinel captains told Bowdash that for a decent bribe they'd turn a blind eye to his disreputable business ventures. Sink their ships to send a strong message.",
        'title': 'Sink EITC Sentinels' },
    'c3r2r3r1r2.3poker': {
        'description': "Win more of Bowdash's money at poker.",
        'stringAfter': "You're really killing 'em in there, but still no pearls.\x07They can't have much gold left at this point...",
        'title': 'Win Again At Poker' },
    'c3r2r3r1r2.4poker': {
        'description': 'Win still more money back for Bowdash at poker.',
        'stringAfter': "Finally! Well, go ahead and keep the links, you've earned 'em.\x07And give me regards to Cutts.",
        'title': 'Win Yet Again At Poker' },
    'c3r2r3r1r2.5deliverCutts': {
        'description': 'Deliver cufflinks to Cutts.',
        'title': 'Deliver the Cufflinks' },
    'c3r2r3r1r2.SinkShips': {
        'description': 'EITC tax collectors have been pressing Bowdash for money and bribes',
        'stringAfter': "You did that with speed and agility. Fine work. Here's the cufflinks.\x07And if you ever need work I could use someone with your \x01slant\x01talents\x02.",
        'title': "Bowdash's Payback" },
    'c3r2r3r1r2Cufflinks': {
        'description': 'Convince Bowdash to give up his cufflinks.',
        'stringAfter': "Very gracious of Bowdash to return these. Now, I needs 3 pearls on 3 different ships...\x07And these be no oridinary ships mind you, but Bloodhounds, so don't get careless.",
        'stringBefore': "\x01slant\x01Bowdash\x02 has a pair that he wears as cufflinks.\x07Unlikely he'll want to part with them though...",
        'title': 'The Bowdash Cufflinks' },
    'c3r2r3r1r5.1curseRemoval': {
        'description': "Saliva from Big Gators makes the base for Fabiola's cure.",
        'title': 'Gather Gator Saliva' },
    'c3r2r3r1r5.1visitOrinda': {
        'description': 'Visit Orinda Le Jeune to contact a rumrunner - she can be found at the Tortuga docks.',
        'stringAfter': "Pearls? There's one pirate who specializes in jewelry-type plunder. His name is \x01slant\x01Ben Flatts\x02.\x07You can find him in his \x01slant\x01office\x02 in the town square.",
        'title': 'Visit Orinda' },
    'c3r2r3r1r5.2curseRemoval': {
        'description': 'The man-eating Fly Traps have venom sacks with mythical powers.',
        'title': 'Venom sacks from Fly Traps' },
    'c3r2r3r1r5.2visitFlatts': {
        'description': 'Ben Flatts the rumrunner runs his own business on Tortuga. Visit him in his office.',
        'stringAfter': 'Interesting... looks like they make a necklace, eh? Or a bracelet?\x07I think I know where to find your pearls... but I need you to do me a small favor first...',
        'title': 'Visit Ben Flatts' },
    'c3r2r3r1r5.3curseRemoval': {
        'description': 'Undead Brigands blood works best for this potion because... well, only Fabiola knows.',
        'title': 'Dried blood from Brigands' },
    'c3r2r3r1r5.3sinkNavyShips': {
        'description': 'Distract the Navy by sinking some of their ships.',
        'stringAfter': "Fine work... couldn't have done a better job me-self...\x07Don't actually have them pearls on me person... but I can tell you where they are...\x07...they're on the arm of a man I killed.\x07He's buried with 'em. You'll have to dig 'im up I guess...",
        'title': 'Distract the Navy' },
    'c3r2r3r1r5.3sinkShips': {
        'description': 'Ben Flatts plans to smuggle some grog to Port Royal. He wants you to distract the Navy by sinking some of their ships.',
        'stringAfter': "Well done... now, about the pearls. I don't actually have them on me person but...\x07The fellow who copped the pearls from me stashed 'em in the ground for safe keeping. Dig 'em up and they're yours.",
        'title': 'Distract the Navy' },
    'c3r2r3r1r5.4recoverArm': {
        'description': 'Some of the pearls were buried somewhere in a treasure chest. Look around for any digging location and retrieve them.',
        'stringAfter': 'Oh, one small detail I forgot to mention; that treasure chest had a voodoo curse and by digging it up...\x07...the curse passed to you. Ask \x01slant\x01Fabiola\x02 the gypsy to undo the spell. Good luck, mate and a bit of advice, never trust the Undead or...\x07...\x07...a Rumrunner! Ha!',
        'title': 'Dig Up Buried Treasure' },
    'c3r2r3r1r5.5visitFabiola': {
        'description': 'See if Fabiola can lift the curse.',
        'stringAfter': "Cursed pearls from a buried treasure chest? That be a powerful spell.\x07It'll cost you, but first... gather me the ingredients to cleanse the pearls...",
        'title': 'Visit Fabiola For A Cure' },
    'c3r2r3r1r5.7deliverCutts': {
        'description': 'Deliver pearls to Cutts.',
        'title': 'Deliver Pearls' },
    'c3r2r3r1r5.CurseRemoval': {
        'description': 'Gather ingredients for Fabiola to cure the curse of the buried treasure.',
        'items': 'Ingredients',
        'stringAfter': 'Good... now take this elixir to a high point on the island, place it on the ground, and run around the container in a circle 20 times.\x07The circle will cleanse the cure... and the pearls will be ready for human use.',
        'title': 'Cure The Curse' },
    'c3r2r3r1r5Smuggler': {
        'description': 'Try and recover some of the pearls from smugglers.',
        'stringAfter': "Looks like you survived your ordeal with the rumrunners... doesn't always end well with that lot.\x07Now \x01slant\x01Carver\x02 mentioned to me he thought he'd seen some earrings looked like me pearls.",
        'stringBefore': "If there's anyone who knows where to find a scrap of plunder... it's a rumrunner.\x07They've got their mitts on everything that moves through the Caribbean... everything.\x07Go talk to \x01slant\x01Orinda\x02. She'll know who dabbles in this particular sort of knick-knack.",
        'title': 'Rumrunners' },
    'c3r2r3r1r5r6.1GatorSaliva': {
        'description': 'Get saliva from a swamp alligator.',
        'stringBefore': "You'll need some saliva from a swamp alligator...\x07They don't give this out without a fight, mind you.",
        'title': 'Swamp Alligator Saliva' },
    'c3r2r3r1r5r6.2WaspVenom': {
        'description': 'Get venom from a Terror wasp.',
        'stringBefore': 'Those Terror wasps are nasty... but their venom is useful.',
        'title': 'Dire Wasp Venom' },
    'c3r2r3r1r5r6.3ScorpionBlood': {
        'description': 'Get the blood of a giant scorpion.',
        'stringBefore': 'Ahh, scorpion blood - the staple of many a voodoo cure...',
        'title': 'Scorpion Blood' },
    'c3r2r3r1r5r6CurseRemoval': {
        'description': 'Gather ingredients for Fabiola to cure the curse of the severed arm.',
        'items': 'Ingredients',
        'stringAfter': 'Take these to a high point on the island, place the items on the ground, and run around them in a circle 20 times.\x07Then go to the Faithful Bride and have yourself a drink.\x07The circle will cure the curse... the grog will fix the dizziness from the cure...',
        'title': 'Cure The Curse' },
    'c3r2r3r1r6.1visitCarver': {
        'description': 'Ask Carver about some pearl earrings - Carver is the barkeep in the Faithful Bride tavern on Tortuga.',
        'stringAfter': "Pearls eh? You should ask \x01slant\x01Fabiola\x02... she has a set of pearl earrings...\x07I'm not one to notice these things... but I'm fairly certain she's wearing them now. She was just in here.",
        'title': 'Ask Carver' },
    'c3r2r3r1r6.2visitFabiola': {
        'description': 'Ask Fabiola for her earrings',
        'stringAfter': "I didn't point out me earings 'cause you didn't ask!\x07Perhaps if you paid more attention you could've save yourself a trip, ey? I'll let you buy 'em, or rather I should say, earn 'em.\x07Deliver me some \x01slant\x01cursed wood\x02 lots of it, and I'll give you me pearl earrings.",
        'title': "Fabiola's Earrings" },
    'c3r2r3r1r6.3phantomShips': {
        'description': "Skeleton ships are made from cursed wood. You need to sink couple of them to satisfy Fabiola's needs.",
        'stringAfter': "That's enough to keep me in business for some time now.\x07Here, take the earrings... and I hope it helps your scheme to aid Cutts. Poor devil, married to that ninny.",
        'title': 'Gather Cursed Wood' },
    'c3r2r3r1r6.3recoverSkeletonShips': {
        'description': 'Sink skeleton ships to gather cursed wood.',
        'stringAfter': "That's enough to keep me in business for some time now.\x07Here, you can have the earrings... but I hope Millie chokes on 'em.",
        'title': 'Gather Cursed Wood' },
    'c3r2r3r1r6.4deliverCutts': {
        'description': 'Deliver pearls to Cutts.',
        'title': 'Deliver Pearls' },
    'c3r2r3r1r6Earrings': {
        'description': 'Locate a pair of fancy earrings made from pearls.',
        'stringAfter': "Good work, mate! Almost there, now...\x07I heard 'bout this bloke once... who collected pearls, obsession with 'em. Problem is... he's got himself killed.\x07Go see if \x01slant\x01Mallet\x02 the gravedigger remembers the chap.",
        'title': 'Fancy Earrings' },
    'c3r2r3r1r7.1albertosRemains': {
        'description': 'Alberto buried most of his pearls in a treasure chest on this wild, wind swept island, hoping to return one day to retrieve them.',
        'title': "Alberto's Pearls" },
    'c3r2r3r1r7.1visitMallet': {
        'description': 'Andros Mallet the gravedigger should have some more information on the mysterious pearl collector. He works the graveyard on Tortuga.',
        'stringAfter': "I do remember a fellow... name was \x01slant\x01Alberto\x02. Yeah, that's it.\x07Heard he was a serious collector of pearls. Came to a bad end, he did. Got eaten by scorpions on Rumrunner's Isle.\x07But legend has it that he buried most of his pearls on Rumrunner's before they finished him off, and...\x07He probably had more on him while he was being eaten. Too bad... for the pearls I mean.",
        'title': 'Visit Mallet' },
    'c3r2r3r1r7.2albertosRemains': {
        'description': "Alberto always had some pearls with him. Since he was eaten by scorpions, you'll find some of Cutts' pearls in their bodies because they can never be digested!",
        'title': "Alberto's Remains" },
    'c3r2r3r1r7.2deliverFabiola': {
        'description': 'See if Fabiola can help decipher the strange map - she stands near her wagon in Tortuga.',
        'stringAfter': "A map? I can read this one with my third eye...\x07In the jungle... beneath a big tree... lies a chest full of... what, I don't know.",
        'title': 'Take Map To Fabiola' },
    'c3r2r3r1r7.3recoverEffects': {
        'description': "Dig up the strangel chest and return with Alberto's personal effects - the chest is buried on Tortuga island somewhere.",
        'stringAfter': "Someone with the \x01slant\x01sight\x02 can know how someone died by the touch of a personal trinket.\x07I can tell you Alberto died at the hands... or claws rather... of giant crabs.\x07That's where you'll find his remains.",
        'title': "Alberto's Personal Effects" },
    'c3r2r3r1r7.4recoverCrabs': {
        'description': "Kill rock crabs on wild islands to recover Alberto's remains.",
        'title': "Alberto's Remains" },
    'c3r2r3r1r7.5deliverCutts': {
        'description': 'Deliver pearls to Cutts.',
        'title': 'Deliver Pearls' },
    'c3r2r3r1r7.AlbertosRemains': {
        'description': "Alberto the pearl collector was last seen on Rumrunner's Isle where he buried his treasure trove of pricey pearls.",
        'stringAfter': "I'm glad you found what you were lookin' for, mate.\x07Now leave me to my diggin', I've much to do if you haven't noticed.",
        'title': "Alberto's Pearls on Rumrunner's" },
    'c3r2r3r1r7Alberto': {
        'description': "Find the pearl collector's collection.",
        'stringAfter': "You got them all, mate...\x07...well, almost all. There's one more, see I didn't mention the last one because Jack Sparrow himself has it...\x07...ask him to return it and uh... don't mention me predicament, ey?",
        'title': 'The Pearl Collector' },
    'c3r2r4.10deliverDice': {
        'description': "Return Nill's lucky dice.",
        'stringAfter': "My luck's changed! And without me dice! Keep 'em, mate!\x07I'm not leaving till me good luck changes...",
        'title': 'Deliver Dice' },
    'c3r2r4.11poker': {
        'description': 'Win more money at poker than Nill to dissuade him from staying.',
        'stringAfter': "Okay, count me in...\x07Captain Sparrow's lucky to 'ave me back...",
        'title': 'Win At Poker' },
    'c3r2r4.12visitJoshamee': {
        'description': 'Let Joshamee know that Offrill has joined the crew.',
        'title': 'Return To Joshamee' },
    'c3r2r4.1bastiensRequest': {
        'description': 'The island overrun with wasp, help get rid of them!',
        'title': 'Defeat Wasps' },
    'c3r2r4.1visitCarver': {
        'description': 'Ask Carver the barkeep in the Faithful Bride tavern in Tortuga for permission to talk to Nill.',
        'stringAfter': "Offrill said to say he isn't here...\x07Care to play a little game? It's called -- how many gold coins am I \x01slant\x01not\x02 holding behind me back?\x07I'll give you a hint... it's more than \x01slant\x01Nil\x02. Get it? More than NIL? Like Nill Offrill...\x07Look - pay up or I'm not letting you talk to him.",
        'title': 'Talk To Carver' },
    'c3r2r4.2bastiensRequest': {
        'description': 'Craven is tired of the pesky scorpions, defeat some of them!',
        'title': 'Defeat Scorpions' },
    'c3r2r4.2bribeCarver': {
        'description': 'Pay off Carver to gain access to Nill.',
        'stringAfter': "If you play cards, be prepared to ante up big money. It's the house rules.\x07Well, the house \x01slant\x01guidelines\x02, anyway...",
        'title': 'Bribe Carver' },
    'c3r2r4.3bastiensRequest': {
        'description': "Craven stashed his favorite rum, now he can't find it!",
        'title': 'Find Hidden Rum' },
    'c3r2r4.3visitNill': {
        'description': "Try to convince Nill Offrill to join Jack's crew.",
        'stringAfter': "Working for Jack, are you? Don't know if I trust you or Jack, but I do trust...\x07Black Jack. Show me your card skills and we'll talk, ey?",
        'title': 'Talk To Nill' },
    'c3r2r4.4blackjack': {
        'description': "Win in blackjack to convince Nill you're trustworthy.",
        'stringAfter': "You're a lucky one. That's good. Me own luck ain't so good.\x07Almost \x01slant\x01died\x02 about a few weeks back and, I've been on a bad losing streak since.\x07I'll considering sailing with Captain Sparrow again if you clear up few debts of mine...\x07Lost at cards to many blokes and I owe Doc Grog for saving me sorry life...\x07...reckon we can settle with him first, ey?",
        'title': 'Win At Blackjack' },
    'c3r2r4.5poker': {
        'description': "Win in poker to convince Nill you're trustworthy - press the 'Lookout' button (spyglass picture) to find a game.",
        'stringAfter': "I almost \x01slant\x01died\x02 about a week back...\x07Bet you think that makes me a lucky bloke... me being alive, and all.\x07Well, I'd probably even lose \x01slant\x01that\x02 bet because I'm \x01slant\x01not\x02 lucky. Think about \x01slant\x01that\x02.\x07Been on a bloody losing streak since I set foot on Tortuga.\x07Sail with Captain Sparrow again?\x07If you clear a few debts for me... I'll go. Otherwise, I'm stuck here...\x07... me luck's \x01slant\x01got to\x02 change eventually...\x07These are the blokes I'm into for a bit of coin.\x07\x01slant\x01Doc Grog\x02 loaned me some money on account of I owed him for a cure for me illness.\x07We can settle with him first, eh?",
        'title': 'Win At Poker' },
    'c3r2r4.7visitNill': {
        'description': 'Tell Nill that the debt with Bowdash has been settled.',
        'stringAfter': "Thanks for settling up with \x01slant\x01King\x02 Bowdash... a mad cracker he is, ey?\x07Now go see Karbay Benedek but I warn ye, he's got a mean streak a mile wide!",
        'title': 'Return To Nill' },
    'c3r2r4.9visitBastien': {
        'description': 'Offrill lost his lucky dice to his one-time friend, Bastien Craven.',
        'stringAfter': "Lucky dice?!\x07If they be so lucky why am I still stranded here?\x07I'll return Nill's dice... but first I need you to do some \x01slant\x01housekeeping\x02 chores for me, ey?",
        'title': 'Visit Craven' },
    'c3r2r4.9visitJohn': {
        'description': "Go retrieve Nill's lucky dice from Bronze John on Driftwood Island.",
        'stringAfter': "I'll not fight ye again. Here - you can have 'em.",
        'title': 'Visit Bronze John' },
    'c3r2r4.BastiensRequest': {
        'description': "Basien Craven needs you to do some 'chores\x092 before he returns Offirill\x092s dice",
        'stringAfter': "Thanks to you mate, I feel safer now... and happier! Special thanks for recovering me rum, ey!\x07Here's to you! And here's Nill's dice. Hope they return his luck.",
        'title': 'Chores for Craven' },
    'c3r2r4Offrill': {
        'description': 'Get Nill Offrill out of debt.',
        'stringAfter': "We'll be doing Nill a favor getting him off shore!\x07Next on the list... Captain Jack wants a doctor aboard...\x07...but the only doctor around these parts is that rum-soaked lunatic \x01slant\x01Doc Grog\x02.",
        'stringBefore': "Nill Offrill's something of a gambler. He never can manage to win...\x07... or stop gambling. He's run up some debt by now I reckon.",
        'title': 'Black Pearl Recruit: Nill Offrill' },
    'c3r2r4r6Creditors': {
        'description': "Settle Nill's debts with his creditors.",
        'items': 'Creditors',
        'stringAfter': "Now \x01slant\x01that's\x02 a diamond, mate! HA!\x07Tell my loyal subject Offrill we're settled up but not to show his ugly face again 'round here or...\x07I'll have me cat eat it right off, HA!",
        'title': "Settle Nill's Debts" },
    'c3r2r4r6r1.10visitGrog': {
        'description': 'Return to Doc Grog.',
        'stringAfter': "Half empty? That jar was half full!\x07I suppose I did skim a bit off the top for me-self.\x07Well then, we shall remedy that in short order. And by \x01slant\x01we\x02 I mean \x01slant\x01you\x02.\x07That jar was full of crab liver bile... it's like snake oil, only it tastes better!\x07Alright, go find some crabs - the bigger the better - and slice 'em up with that oversized scalpel you've got there.\x07Cut out the livers... and only keep the \x01slant\x01black\x02 ones. You'll need quite a few of them. Good luck!",
        'title': 'Return To Doc Grog' },
    'c3r2r4r6r1.11recoverCrabs': {
        'description': 'Kill crabs to gather black crab bile.',
        'stringAfter': "Good work. Looks like one of these ate some \x01slant\x01dice\x02... I suppose they're yours now...\x07Why are you so interested in Offrill anyway? Are you sure you're a pirate? I mean, you do \x01slant\x01smell\x02 like a pirate...\x07No matter. I seem to be fresh out of bile, go fetch me some while I think of what to have you do next.",
        'title': 'Gather Black Crab Bile' },
    'c3r2r4r6r1.12deliverJar': {
        'description': 'Deliver the jar of black crab bile to Orinda Le Jeune.',
        'stringAfter': 'This is for Doc Grog...',
        'title': 'Deliver Jar' },
    'c3r2r4r6r1.13deliverMoney': {
        'description': 'Deliver payment to Doc Grog.',
        'stringAfter': "Perhaps you're thinkin' I should be lettin' Offrill off the hook... well, not yet.\x07Healin' people's not like stealin' from people - it's a lot of hard work. So let's get to it...\x07Go find \x01slant\x01Mallet\x02 again. Give him this. He knows you are coming.",
        'title': 'Deliver Payment' },
    'c3r2r4r6r1.14deliverPaper': {
        'description': "Deliver piece of paper to Mallet that reads: '\x01slant\x01that\x02 thing \x01slant\x01from\x02 that \x01slant\x01day\x02'.",
        'stringAfter': "The leg bone, eh? Grind it, eh?\x07Ol' Grog loves to sprinkle the shavings in his coffee.\x07Just a joke, mate. I don't know what he uses it for... 'cept he is a doctor, right?\x07I don't have time for the shavings. Better take it to \x01slant\x01Brown's\x02 shop.\x07If he asks, tell him it's for Grog - his pig died...",
        'title': 'Deliver Paper' },
    'c3r2r4r6r1.15deliverBone': {
        'description': "Deliver a leg bone to Butcher Brown for grinding - Butcher Brown has a vendor's tent in the shanty part of Tortuga - a ray of light will guide you to him.",
        'stringAfter': 'His pig? How many legs does that thing have...?',
        'title': 'Deliver Leg Bone' },
    'c3r2r4r6r1.16bribeButcher': {
        'description': 'Pay the butcher to grind the bone.',
        'stringAfter': 'Thank you, kindly. Here are your shavings.',
        'title': 'Pay Butcher' },
    'c3r2r4r6r1.17deliverShavings': {
        'description': 'Deliver bone shavings to Doc Grog.',
        'stringAfter': "Excellent. You know, that leg came from a former patient of mine. Real tall fellow.\x07Not quick enough with his sword, though...\x07Okay, one last thing - and I know what you're thinkin' - oh no, not another jar...\x07Well, this time it's scorpions, right? When you've filled up the jars... bring them to \x01slant\x01Bronze John\x02... he's got strange yellow eyes...\x07...and a bit of an abrasive personality... but make sure he takes all of the jars... good luck!",
        'title': 'Deliver Shavings' },
    'c3r2r4r6r1.18recoverBile': {
        'description': 'Kill giant scorpions for their bile.',
        'stringAfter': "Okay. I know I said that was the \x01slant\x01last\x02 thing... I lied. \x01slant\x01Yes\x02, I \x01slant\x01am\x02 a doctor, but I'm a pirate doctor... what can I say?\x07See, I used to sail with the Navy... until they forced me into early \x01slant\x01retirement\x02...\x07Problem is... I had this really nice set of tools... \x01slant\x01doctoring\x02 tools, see?\x07I still have the key, but not its counterpart... I'm talking about a \x01slant\x01chest\x02...\x07Go find it.",
        'title': 'Recover Green Bile' },
    'c3r2r4r6r1.19deliverBile': {
        'description': 'Take the jar of green scorpion bile to Bronze John - John is on the beach of Driftwood Island - a ray of light will guide you to him.',
        'stringAfter': 'Thank you. Here...',
        'title': 'Deliver Green Bile' },
    'c3r2r4r6r1.1grogsRequest': {
        'description': 'Defeat undead critters to help Doc make another batch of elixir',
        'title': 'Collect Bat Bile' },
    'c3r2r4r6r1.1visitGrog': {
        'description': "Go ask Doc Grog how to settle Nill's debt.",
        'stringAfter': "I thought Offrill was the luckiest, scurviest dog that ever sail the seven seas. But wrong I was!\x07Spent plenty on that scoundrel to make him well and even gave him some gold to live on...\x07and he lost it all playing cards!\x07Fetch me some \x01slant\x01ingredients\x02, for me elixirs and I'll consider forgivin' his debt! ",
        'title': 'Visit Doc Grog' },
    'c3r2r4r6r1.20deliverPayment': {
        'description': "Take Bronze John's payment back to Doc Grog.",
        'stringAfter': "Okay. I know I said that was the \x01slant\x01last\x02 thing... I lied. \x01slant\x01Yes\x02, I \x01slant\x01am\x02 a doctor, but I'm a pirate doctor... what can I say?\x07See, I used to sail with the Navy... until they forced me into early \x01slant\x01retirement\x02...\x07Problem is... I had this really nice set of tools... \x01slant\x01doctoring\x02 tools, see?\x07I still have the key, but not its counterpart... I'm talking about a \x01slant\x01chest\x02...\x07Go find it.",
        'title': 'Deliver Payment' },
    'c3r2r4r6r1.21recoverChest': {
        'description': "Sink Navy ships to recover Grog's chest.",
        'stringAfter': "Okay, here's the key. Open it!\x07(chest contents: 40 year old port, half-smoked cigar, 5 Spanish coins)\x07Alright... enough! Even an old scalawag like meself can see it's time to let you off the hook, so to speak.\x07I consider Offrill's debt covered... now please leave me to my drink.",
        'title': "Recover Grog's Chest" },
    'c3r2r4r6r1.22visitNill': {
        'description': "Inquire about Nill Offrill's next creditor.",
        'title': 'Return To Nill' },
    'c3r2r4r6r1.2grogsRequest': {
        'description': 'Defeat Big Gators for their prized bile sacks',
        'title': 'Collect Gator Bile' },
    'c3r2r4r6r1.2visitCarver': {
        'description': "Fetch a pint of Grog's 'medication' from Carver in the Faithful Bride.",
        'stringAfter': "A pint of the doc's \x01slant\x01medication\x02, eh? I don't suppose he gave you any money for it, did he?",
        'title': "Fetch Grog's Medication" },
    'c3r2r4r6r1.3bribeCarver': {
        'description': "Pay for Grog's medication.",
        'stringAfter': "I suppose you could say I'm the doc's doctor.",
        'title': "Purchase Grog's Medication" },
    'c3r2r4r6r1.3grogsRequest': {
        'description': "Sink Navy ships to recover Grog's chest.",
        'stringAfter': "Okay, here's the key. Open it!\x07Let's see, there be some 40 year old port, a half-smoked cigar, and ah-ha... Spanish coins!\x07I've seen enough! Even an old scalawag like meself can see it's time to let Offrill's off the hook. \x07Consider his debt forgiven, now go, I have work to do.",
        'title': "Recover Grog's Chests" },
    'c3r2r4r6r1.4deliverMedicine': {
        'description': "Deliver Grog's medication.",
        'items': 'Ingredients',
        'stringAfter': "As I said, Offrill owes me quite a bit of money. But I am willing to overlook this... for a price.\x07First, deliver this jar to \x01slant\x01Orinda\x02 at the docks. It's only half full but she won't notice...\x07Hurry up!",
        'title': "Deliver Grog's Medication" },
    'c3r2r4r6r1.5visitMallet': {
        'description': 'Fetch a pint of thick grog from Mallet - Mallet is in the Tortuga graveyard in the center jungle on Tortuga.',
        'stringAfter': 'Doc Grog, eh? He likes my own special recipe. Appreciates the \x01slant\x01care\x02 and \x01slant\x01attention\x02 I give it, he does.\x07First, pay up, mate.',
        'title': 'Fetch Thick Grog' },
    'c3r2r4r6r1.6bribeMallet': {
        'description': 'Pay for the thick grog.',
        'stringAfter': 'Tell Grog I have the \x01slant\x01thing\x02 he asked for on that \x01slant\x01day\x02 way back \x01slant\x01when\x02...',
        'title': 'Purchase Thick Grog' },
    'c3r2r4r6r1.7deliverGrog': {
        'description': 'Deliver thick grog to Grog.',
        'stringAfter': "As I said, Offrill owes me quite a bit of money. But I am willing to overlook this... for a price.\x07First, deliver this jar to \x01slant\x01Orinda\x02 at the docks. It's only half full but she won't notice...\x07Hurry up!",
        'title': 'Deliver Thick Grog' },
    'c3r2r4r6r1.8deliverJar': {
        'description': 'Deliver a jar of medicine to Orinda Le Jeune at the Tortuga docks.',
        'stringAfter': "Who are you?\x07Why should I pay for... whatever this is... when it's half-empty?\x07Well, it's a start. Tell Doc Grog he'll get his money when I get the other half...",
        'title': 'Deliver Jar' },
    'c3r2r4r6r1.9deliverJar': {
        'description': 'Deliver a half-full jar of medicine to Tomas in his shack near the Tortuga docks - a ray of light will guide you.',
        'stringAfter': 'Thank you, kindly. Please give Doc Grog my best.',
        'title': 'Deliver Jar' },
    'c3r2r4r6r1.GrogsRequest': {
        'description': 'Doc is running low on elixir so you must help him to clear Nill\x0c2\x092s debt.',
        'stringAfter': 'Back already? Blimey, a fine pirate ye are! \x07Now, I has a few other items for me elixir before I let that whelp off the hook!  But the ingredients are inside...\x07Navy sea chests. Are ye up to the task?',
        'title': 'Collect Elixir ingredients' },
    'c3r2r4r6r1Grog': {
        'description': 'Settle up with Doc Grog.',
        'stringAfter': "He's a fine doctor... I'm glad to be squared up with him.\x07Now, I've been doing me best to avoid \x01slant\x01Bowdash\x02 lately, so talk to him next.",
        'stringBefore': '\x01slant\x01Doc Grog\x02 loaned me some money on account of I owed him for a cure for me illness.',
        'title': 'Indebted to Doc Grog' },
    'c3r2r4r6r2.10deliverMoney': {
        'description': "Take Bronze John's payment to Bowdash.",
        'stringAfter': "From the looks of you... it must have been a pleasant chat with Bronze John. HA!\x07The \x01slant\x01key\x02 to my next \x01slant\x01decree\x02... is inside the belly of a vicious beast! Interested?\x07That wasn't a \x01slant\x01real\x02 question. The Royal We call it... a \x01slant\x01hypothetical\x02. Or maybe it's \x01slant\x01rhetorical\x02.\x07Can't remember! But I'm the King! It doesn't matter, does it? HA!\x07Look, one of my \x01slant\x01subjects\x02 was swallowed whole by one of those giant gators... inside its belly is the \x01slant\x01key\x02. \x07Bring me that key!",
        'title': 'Deliver Payment' },
    'c3r2r4r6r2.11recoverKey': {
        'description': "Kill a Huge Alligator looking for Bowdash's key.",
        'stringAfter': 'Good work. Still have all of your limbs, HA!\x07Now go fetch me the contents of my chest and make it snappy.',
        'title': 'Recover A Key' },
    'c3r2r4r6r2.12deliverKey': {
        'description': 'Deliver the key and a note from Bowdash to Scarlet - Scarlet stands near the Faithful Bride tavern in Tortuga.',
        'stringAfter': "(Scarlet slaps you)\x07Tell Bowdash that there's not a key in all the Caribbean that'll open this chest!\x07Though I \x01slant\x01do\x02 wonder what lies behind this particular lock...",
        'title': 'Deliver Key And Note' },
    'c3r2r4r6r2.13deliverKey': {
        'description': 'Return the key to Bowdash.',
        'stringAfter': "She said what? I have half a mind to shoot the messenger... and that means YOU, scrapper!\x07Well, I suppose 'tis a case of unrequited love... what can a pirate do? HA!\x07I bet she'd think twice if she knew what was inside that chest...\x07Go fetch it for me.",
        'title': 'Return The Key' },
    'c3r2r4r6r2.14recoverDiamond': {
        'description': "Find Bowdash's chest and return with the treasure.",
        'stringAfter': "Now \x01slant\x01that's\x02 a diamond, mate! HA!\x07Tell my loyal subject Offrill we\x0c2\x092re settled up but not to show his ugly face again 'round here or...\x07I\x0c2\x092ll have me cat eat it right off, HA!",
        'title': 'Recover Treasure' },
    'c3r2r4r6r2.15stealCigars': {
        'description': "Steal a box of cigars back from Bowdash's butler - the cigars are hidden in a cabinet in Bowdash's 'mansion' on Tortuga.",
        'stringAfter': "My cigars! Very good then.\x07Alright fair loyal subject...\x07... if you complete this last task, Nill Offrill's offenses to the royal treasury shall be overlooked.\x07We have recently come into possession of a map... a map where X does \x01slant\x01not\x02 mark the spot.\x07Truth is... I spilled me grog on the thing! HA! See for yourself... (the map is barely legible)\x07You shall travel to the farthest reaches of my kingdom... and bring back the \x01slant\x01black\x02 chest.\x07Good luck!",
        'title': 'Steal Cigars' },
    'c3r2r4r6r2.16recoverChest': {
        'description': 'Seek the Black Chest for Bowdash - the chest is buried on Isla Cangrejos - a ray of light will guide you to the island.',
        'stringAfter': 'I hereby decree that said scalawag Nill Offrill is free and clear of binding contractual obligations...\x07... to the royal treasury and all pilfered items, jewels and such, that lay within. Now go!',
        'title': 'Recover The Black Chest' },
    'c3r2r4r6r2.1visitBowdash': {
        'description': "Ask the mad Andrew Bowdash to forgive Offrill's debt.",
        'stringAfter': "Offrill?! He frittered away me gold... hence, his head shall roll.\x07HA! If I weren't \x01slant\x01already\x02 the King of Tortuga... I'd have to crown myself King!\x07But ye looks to be a trustworthy mate so, tell ye what'll do...\x07If ye sink ships from the East India Trading Company, I'll consider erasing Offrill's debt - soft hearted king that I am, HA!",
        'title': 'Visit Andrew Bowdash' },
    'c3r2r4r6r2.2recoverFlags': {
        'description': 'Sink EITC ships and bring their flags to Bowdash.',
        'stringAfter': "The King is pleased... but there's more things I need done.\x07Some time ago, a certain Navy Captain \x01slant\x01Billington\x02 sank my favorite vessel and took me \x01slant\x01scepter\x02.\x07Find him, sink his bloody ship and maroon the scoundrel! And...\x07Return me the scepter, HA!",
        'title': 'Recover Flags' },
    'c3r2r4r6r2.3captureBillington': {
        'description': "Capture Captain Billington from a Navy ship or Offrill's still in debt.",
        'title': 'Capture Captain Billington' },
    'c3r2r4r6r2.4maroonBillington': {
        'description': "Maroon Captain Billington on a wild island so he'll hand over \x01slant\x01King\x02 Bowdash's scepter.",
        'title': 'Maroon Captain Billington' },
    'c3r2r4r6r2.5deliverScepter': {
        'description': 'Deliver the scepter (actually a hook arm) to Bowdash.',
        'stringAfter': "HA! You're becoming me favored subject.\x07Now the \x01slant\x01key\x02 to me next \x01slant\x01decree\x02... is inside the belly of a vicious beast!\x07One of my \x01slant\x01subjects\x02 was returning it when he was swallowed whole by a huge gator... inside its belly is the \x01slant\x01key\x02.\x07Defeat the beast and bring it to me, HA!",
        'title': 'Deliver Scepter' },
    'c3r2r4r6r2.6deliverMap': {
        'description': "Deliver Bowdash's map to Orinda Le Jeune at the Tortuga docks.",
        'stringAfter': "Delivery for the King? We'll load your ship right away.",
        'title': 'Deliver Map' },
    'c3r2r4r6r2.7smuggleRum': {
        'description': 'Smuggle a shipment of rum to Port Royal.',
        'title': 'Smuggle Rum' },
    'c3r2r4r6r2.8visitBowdash': {
        'description': 'Return to Bowdash.',
        'stringAfter': 'The delivery was made? And you have the map? Excellent!\x07One of my subjects has neglected to pay monetary tribute to his royal benefactor...\x07His name is \x01slant\x01Bronze John\x02... find him... and tell him his duty has come due. HA!',
        'title': 'Return To Bowdash' },
    'c3r2r4r6r2.9visitJohn': {
        'description': "Track down Bronze John on Driftwood Island and make him pay his 'taxes'.",
        'stringAfter': "Bowdash? Arrrgghhhh!\x07(Bronze John fights you and knocks the dice out of your pocket)\x07Take this gold to Bowdash... but I'm keeping your dice.",
        'title': 'Find Bronze John' },
    'c3r2r4r6r2Bowdash': {
        'description': 'Square things for Offrill with Andrew Bowdash.',
        'stringAfter': "Now \x01slant\x01that's\x02 a diamond, mate! HA!\x07Tell my loyal subject Offrill we\x0c2\x092re settled up but not to show his ugly face again 'round here or...\x07I\x0c2\x092ll have me cat eat it right off, HA!",
        'title': 'Indebted to Andrew Bowdash' },
    'c3r2r4r8.10deliverMoney': {
        'description': "Deliver Ben Flatt's money to Benedek.",
        'stringAfter': "Sounds like ole Ben was pleased to settle up with me.\x07Here's another person I need you to track down...Walter O'Henry. Fine bloke..\x07...back when he was alive! Dead or not... he still owes me!\x07And I hear he still sails the seas with others of his kind... \x01slant\x01dead\x02, or undead, that is.",
        'title': "Deliver Ben's Money" },
    'c3r2r4r8.11captureOHenry': {
        'description': "Capture the ghost of O'Henry by sinking skeleton ships.",
        'stringAfter': "Fine work... for a bilge rat like you!\x07One last favor... and I will overlook Offrill's debt... find Orly McFarthing, or what remains of him.\x07Eaten by a giant flytrap, he was. Had some rings of mine that were a gift from me dear ole mum.",
        'title': "Capture O'Henry" },
    'c3r2r4r8.12recoverBling': {
        'description': "Benedek's mum gave him some rings that Orly stole and you must recover it.",
        'stringAfter': "Ah... me rings... they're mine again! I'm so happy I could...\x07...weep!\x07Now that Offrill's debt has been covered. Go... I want to be alone.",
        'title': 'Recover Rings' },
    'c3r2r4r8.12recoverChain': {
        'description': "Recover Benedek's gold chain from Venus Fly Traps.",
        'stringAfter': "Ah... me necklace... it's mine again!  I\x092m so happy I could\x0c2\x085\x07\x0c2\x085weep!   So now Offrill\x0c2\x092s debt has been covered. Now go...\x07I want to be alone.",
        'title': 'Recover Chain' },
    'c3r2r4r8.13visitNill': {
        'description': 'Return to Nill Offrill and tell him the good news.',
        'title': 'Return To Nill' },
    'c3r2r4r8.1visitBenedek': {
        'description': "Talk to Karbay Benedek about forgiving Nill's debt.",
        'stringAfter': "You wish to repay Offrill's debt?\x07Sounds to me like you're mad, but...\x07...if you are willing to \x01slant\x01repay\x02 his debt... I am in need of some assistance\x02.\x07There is a Navy Lieutenant - a pirate, really... calls himself \x01slant\x01Wallace\x02...\x07...owes me even more than Offrill. Find him. Then leave him for dead on a wild island, savvy?",
        'title': 'Visit Karbay Benedek' },
    'c3r2r4r8.2captureWallace': {
        'description': 'Captain Wallace sails on an EITC ship.',
        'title': 'Capture Wallace' },
    'c3r2r4r8.3maroonWallace': {
        'description': "Maroon Wallace to get him to hand over Benedek's money.",
        'title': 'Maroon Wallace' },
    'c3r2r4r8.4deliverMoney': {
        'description': "Deliver Wallace's payment to Benedek.",
        'stringAfter': "Well done, \x01slant\x01pirate\x02, so... I've another task if you're to settle Offrill's debt.\x07Someone owes me, but I bloody well cannot remember who! \x07Only clue I have is this rum he gave me, and the label's unreadable...\x07Seen some Undead scum drinking it so defeat them and bring me a bottle so I can remember who owes me.\x07Better make it 3 mate, 'cause I like the taste.",
        'title': 'Deliver Payment' },
    'c3r2r4r8.5recoverBottles': {
        'description': "Defeat Undead to get their rum - and quench Benedek's thirst.",
        'stringAfter': 'Ha! Now I remember, Ben Flatts... what a night!\x07Oh huh... find that smuggler and get the gold that he owes me... now!!',
        'title': 'Recover Rum' },
    'c3r2r4r8.5recoverRum': {
        'description': 'Acquire another bottle of rum with the same label from Navy ships to find its maker.',
        'title': 'Recover Rum' },
    'c3r2r4r8.6visitBenFlatts': {
        'description': 'Go talk to Ben Flatts in his office on Tortuga',
        'stringAfter': "Benedek says I owe him? I do but I was hoping he was too drunk at the time to remember.\x07I'll pay back that shark... if you'll do me a favor.\x07Sink a few ships that've been harassing me \x01slant\x01almost legal\x02 import business.",
        'title': 'Visit Ben Flatts' },
    'c3r2r4r8.6visitMarsh': {
        'description': "Graham Marsh's stamp was on the label of the rum bottle - Marsh is in his office in Port Royal - a ray of light will guide you.",
        'stringAfter': "That's my stamp, indeed...\x07But that rum was made by none other than \x01slant\x01Ben Flatts\x02.\x07Do me a favor first, and I'll arrange a meeting with him.\x07You see, the Navy's been interfering with some of my activities in the area...",
        'title': 'Visit Graham Marsh' },
    'c3r2r4r8.7sinkNavyShips': {
        'description': 'Sink some Navy ships for Graham Marsh.',
        'stringAfter': "Okay, you did your part - you'll find \x01slant\x01Ben Flatts\x02 in his 'office' in Tortuga... you can tell 'im I sent you.",
        'title': 'Sink Navy Ships' },
    'c3r2r4r8.7sinkShips': {
        'description': 'Ben Flatts is a smuggler and needs your help sinking the ships that are cutting into his profits.',
        'stringAfter': 'Fine work, mate.  Now I can get back to my affairs and...\x07...make some money to replace what I owe that scoundrel. Here. Now go.',
        'title': 'Sink Ships for Flatts' },
    'c3r2r4r8.8visitFlatts': {
        'description': 'Go talk to Ben Flatts in his office in Tortuga - a ray of light will guide you there.',
        'stringAfter': "Benedek is looking for me? I was hoping he was too drunk at the time to remember his generosity.\x07I'll pay back that shark... if you can win back me money - I lost it at cards, see?",
        'title': 'Visit Ben Flatts' },
    'c3r2r4r8.9poker': {
        'description': "Play poker to win back Ben Flatt's money.",
        'stringAfter': 'Okay, mate. You win - keep the money. Tell Benedek I hope he chokes on it!',
        'title': "Win Back Ben's Money" },
    'c3r2r4r8Benedek': {
        'description': 'Square up with Karbay Benedek.',
        'stringAfter': "I have a feelin' me luck's about to change...but I must have me lucky dice to seal the deal.\x07Get them back from that rum-soaked, sun baked vermin, Bastien Craven.",
        'title': 'Indebted to Karbay Benedek' },
    'c3r2r5.10administerRemedy': {
        'description': "Give the 'medicine' to Le Cerdo in the back room of Doc Grog's office.",
        'stringAfter': "What is that horrid smell?!\x07Ahhh! Get that stuff away from me! You're not gonna... ahhhh! That's disgusting! Where do I sign?\x07What did I sign!?\x07Where? With, with... Sparrow!?\x07I'll get you, you yellow-bellied-barnacle-infested-swine!!",
        'title': 'Administer Medicine' },
    'c3r2r5.11visitJoshamee': {
        'description': 'Let Joshamee know that Le Cerdo was signed up as doctor.',
        'title': 'Return To Joshamee' },
    'c3r2r5.1visitGrog': {
        'description': "Inquire if Doc Grog is willing to join Jack Sparrow's crew.",
        'stringAfter': "On me honor, I'll never go back to sea... not with Sparrow, or anyone!\x07I gets sick as a dog just lookin' at waves. But I know just the man for the job...\x07His name is \x01slant\x01Le Cerdo\x02. Used to be a ship surgeon's assistant. Now he just soaks up me grog and food.\x07Been here for weeks he has, \x01slant\x01pretending\x02 to be sick, so we'll Shanghai him.\x07First, I be needin' some eyes of a \x01slant\x01Kraken\x02, to make a potion that'll make Le Cerdo \x01slant\x01want\x02 to serve, ha!",
        'title': 'Visit Doc Grog' },
    'c3r2r5.2krakenEyes': {
        'description': "Sink EITC ships in search of Kraken's eyes.",
        'stringAfter': "Nice find, these are some fine eyes.\x07I'll need to dry them out on the beach for a bit, though...\x07You can pass the time gatherin' some more ingredients... now go!",
        'title': 'Kraken Eyes' },
    'c3r2r5.3deliverJack': {
        'description': "Take Doc Grog's list to Jack Sparrow in the Faithful Bride tavern on Tortuga.",
        'stringAfter': "Doc Grog said that I, Jack Sparrow, screamed like a schoolgirl? Really?!\x07Like the little girl who vanished from under the eyes of seven agents of the East India Trading Company?\x07Like the little girl who sacked Nassau Port without firing a single shot?\x07Surely he's mistaken. As a matter of fact, I \x01slant\x01love\x02 leeches. Keep three or four on me person at all times. Truly.\x07\x01slant\x01Still\x02... I'd rather keep this whole thing \x01slant\x01quiet\x02, if you catch my drift.\x07Let's just take care of this and we'll call it even...\x07So then... five items for Doc Grog? I'll take half then, and you take these other four... Fair?",
        'title': 'Deliver List To Jack Sparrow' },
    'c3r2r5.4recoverEyes': {
        'description': "Recover Dread Scorpion Eyes for Doc Grog's medicine.",
        'title': 'Recover Dread Scorpion Eyes' },
    'c3r2r5.5deliverJack': {
        'description': 'Take the scorpion eyes to Jack Sparrow.',
        'stringAfter': "Here's my half, mate. Nice bit of pirating...\x07I'll tell you this... \x01slant\x01Scarlet\x02 is more of a doctor than that rummy... and she certainly has better bedside manner.\x07Off with you then... tell that bilge rat to keep the tip!",
        'title': 'Deliver Scorpion Eyes' },
    'c3r2r5.6deliverEyes': {
        'description': 'Deliver giant scorpion eyes to Doc Grog.',
        'stringAfter': "Scorpion eyes? How delightful! Please thank Jack for me, if he's alive next time ye see him.\x07Just administer our \x01slant\x01Persuasion Potion\x02 and a ship's surgeon ye will have.",
        'title': 'Deliver Giant Scorpion Eyes' },
    'c3r2r5.6recoverShips': {
        'description': 'Doc has a personal vendetta with the EITC and sinking them will make him work faster.',
        'stringAfter': "Sent 'em all to Davy Jones locker, ey? Good riddance, I say!\x07Now, for the final step of our \x01slant\x01Persuasion Potion\x02, But you might want to take some mates with you to find these...\x07...tough ones, they are.",
        'title': 'Sink EITC ships' },
    'c3r2r5.7deliverMallet': {
        'description': 'Ask Mallet to bury the medicine in the Tortuga graveyard.',
        'stringAfter': "For who? Ole Grog? Aye, I'll do what ye ask... for a price.",
        'title': 'Bury Medicine' },
    'c3r2r5.8bribeMallet': {
        'description': 'Pay Mallet to do the deed.',
        'stringAfter': "Okay mate, 'ere it is... I'd not drink a drop of that swill me'self.",
        'title': 'Pay Mallet' },
    'c3r2r5.8visitJack': {
        'description': "Tell Jack Sparrow about the progress you're making gathering his crew for the Black Pearl.",
        'stringAfter': "Ah, it's you. Sorry, you're name again is?\x07Oh right. Yes, so you've found me a surgeon but it's not Doc Grog?!\x07Bloody well grateful for that. Barbossa's monkey is a better surgeon.\x07Say, while you're idle, could you do me a \x01slant\x01smallish\x02 favor?",
        'title': 'Visit Jack Sparrow' },
    'c3r2r5.9deliverRemedy': {
        'description': 'Take the fermented medicine back to Doc Grog.',
        'stringAfter': '(whispering) Listen. \x01slant\x01Le Cerdo\x02 is too ornery for me to administer the elixir. Ye must do it...',
        'title': 'Deliver Medicine' },
    'c3r2r5Grog': {
        'description': 'Help Doc Grog cure an intractable patient.',
        'title': 'Black Pearl Recruit: Doc Grog' },
    'c3r2r5r2.10recoverEggs': {
        'description': 'Recover giant scorpion eggs.',
        'stringAfter': "Easy there! Don't break 'em!",
        'stringBefore': 'Those eight-legged vermin have eggs that will nearly finish the job. Get me some...',
        'title': 'Giant Scorpion Eggs' },
    'c3r2r5r2.11recoverMoney': {
        'description': 'Steal ill-gotten treasure still covered in blood from EITC ships.',
        'stringAfter': "We'll need to dispose of this quickly...",
        'stringBefore': 'EITC ships are loaded with blood-stained booty.',
        'title': 'Bloody Treasure' },
    'c3r2r5r2.12recoverNightshade': {
        'description': 'Steal nightshade from skeletons.',
        'stringAfter': "Don't get any of that on yer hands... at least not if ye be plannin' to lick those dirty fingers.",
        'stringBefore': "Get me three pints of the poisonous nectar found inside the bittersweet nightshade.\x07Bloody skeletons always carry it 'round with...must they think it makes 'em invincible.",
        'title': 'Nightshade' },
    'c3r2r5r2.13recoverWhiskers': {
        'description': 'Pluck whiskers from a red-headed Navy Sergeant.',
        'stringAfter': "Ye call that red? Well, I guess it'll have to do.",
        'stringBefore': 'The whiskers of a Navy Sergeant. Rouge whiskers, mate.',
        'title': 'Red Whiskers' },
    'c3r2r5r2.2recoverCrocwater': {
        'description': 'Retrieve water from the belly of a big alligator.',
        'stringAfter': "Whew! Big Gators smell worse on the inside than they do on the outside, eh?\x07Now I need some entrails, special ones.\x07These be entrails of shark victims from a disaster at sea.\x07Trouble is, entrails get eaten by rock crabs as soon as they wash ashore...\x07\x01slant\x01Driftwood Island's\x02 surrounded by shark-infested waters... I'd start there.",
        'title': 'Big Alligator Water' },
    'c3r2r5r2.3recoverEntrails': {
        'description': 'Recover entrails left over from a shark attack from giant crabs on Driftwood Island - a ray of light will guide you to the island.',
        'stringBefore': "I need the entrails from shark infested seas.\x07Trouble is, entrails get eaten by rock crabs as soon as they wash ashore...\x07\x01slant\x01Mullet Island's\x02 surrounded by shark-infested waters.",
        'title': 'Entrails From A Shark Attack' },
    'c3r2r5r2.4recoverGuano': {
        'description': 'Recover muddy bat guano from vampire bats - look for bats in the Tortuga caves.',
        'stringAfter': 'Vampire bat guano makes the best sort of mud, it does.',
        'stringBefore': 'I need cave mud, mixed with vampire bat guano.',
        'title': 'Vampire Bat Guano' },
    'c3r2r5r2.5recoverSplinter': {
        'description': "Recover a splinter from the crow's nest of a skeleton ship.",
        'stringAfter': "Careful with that splinter, mate. Don't wanna find out what that does if it breaks yer skin...",
        'stringBefore': "Another ingredient I need is a splinter from the crow's nest of a skeleton ship.",
        'title': 'Splinter From Skeleton Ship' },
    'c3r2r5r2.6recoverDust': {
        'description': 'Recover graveyard dust from skeletons.',
        'stringAfter': "Yeah, it's best when scraped directly from the undead.",
        'stringBefore': "The dust from grave sites have a healing power unmatched by anything I've seen. Bring me some...",
        'title': 'Graveyard Dust' },
    'c3r2r5r2.7recoverEarth': {
        'description': 'Gather earth from beneath the roots of a giant venus flytrap.',
        'stringAfter': '',
        'stringBefore': 'I need earth from beneath one of them giant venus flytraps. Why? Because that earth be soiled properly!',
        'title': 'Flytrap Root Soil' },
    'c3r2r5r2.8recoverLichens': {
        'description': 'Scrape lichen from huge alligators.',
        'stringAfter': "Not sure 'bout the origins of huge alligators, but they carry a fair ration of lichen.",
        'stringBefore': 'Get me some lichen. That fungus can cure anything, it can.',
        'title': 'Lichens' },
    'c3r2r5r2.9recoverWater': {
        'description': 'Recover salt water from a place of battle - sink EITC Corvette ships to create places of battle.',
        'stringAfter': "Aye, that's the proper kind of salt water.",
        'stringBefore': 'Get salt water from where a EITC ship is sent to Davy Jones. The departed spirits is what does it...',
        'title': 'Salt Water Touched By Battle' },
    'c3r2r5r2Medicine': {
        'description': 'Gather ingredients for some medicine to cure Le Cerdo.',
        'stringAfter': "Say, that's some fine work!\x07Here's the next batch to work on...",
        'title': 'Gather Medicinal Ingredients' },
    'c3r2r5r2Medicine2': {
        'description': 'Gather more ingredients for some medicine to cure Le Cerdo.',
        'stringAfter': "I'll be rid of that scallywag Le Cerdo soon at this rate!\x07Here be some more things we need...",
        'title': 'Gather Medicinal Ingredients' },
    'c3r2r5r2Medicine3': {
        'description': 'Gather more ingredients for some medicine to cure Le Cerdo.',
        'stringAfter': 'Well done! Almost ready... just a few more items...',
        'title': 'Gather Medicinal Ingredients' },
    'c3r2r5r2Medicine4': {
        'description': 'Gather more ingredients for some medicine to cure Le Cerdo.',
        'stringAfter': "One last thing, yer friend Sparrow still owes me for the \x01slant\x01last\x02 time I fixed him up...\x07... ask him yourself. I'm quite certain he'll remember the \x01slant\x01leech\x02. Screamed like a schoolgirl, he did!\x07And if not... tell him that I can put the bugger back again!\x07Here's the list of what I need from Captain Jack.",
        'title': 'Gather Medicinal Ingredients' },
    'c3r2r5r2r1.1recoverEyeShips': {
        'description': "Sink Navy ships in search of a kraken's eye.",
        'stringAfter': "Nice find, this is a fine eye.\x07I'll need to dry it out on the beach for a bit, though...\x07You can pass the time killin' crabs!",
        'title': 'Recover Eye From Ships' },
    'c3r2r5r2r1.2defeatCrabs': {
        'description': 'Kill crabs to pass the time while the kraken eye dries on the beach.',
        'title': 'Dry The Eye While Killing Crabs' },
    'c3r2r5r2r1.3deliverEye': {
        'description': "Take the dried kraken eye to Blacksmith Flinty to grind it into powder - a ray of light will guide you to Flinty's shop on Tortuga.",
        'stringAfter': "That nasty thing? Smells like old barnacles! It'll cost ye...",
        'title': 'Grind The Eye' },
    'c3r2r5r2r1.4bribeBlacksmith': {
        'description': 'Pay Blacksmith Flinty to do the job.',
        'stringAfter': 'Okay, there yer powder. Now get that rot outta here!',
        'title': 'Pay Blacksmith Flinty' },
    'c3r2r5r2r1.5deliverPowder': {
        'description': 'Return the powder to Doc Grog.',
        'title': 'Deliver Powder' },
    'c3r2r5r2r1KrakenEye': {
        'description': 'Obtain and prepare an eye from a Kraken.',
        'stringAfter': "That wasn't so hard now, was it?\x07Now take this jar and fill it with water from the belly of a gator... make sure it's a big 'un.",
        'stringBefore': "We need the eye of a \x01slant\x01kraken\x02. Aye, I know a kraken is no sea-turtle. But you're a pirate, ey?\x07Some Navy surgeons keep 'em in a jar aboard-ship. For what purpose I know not.",
        'title': "Kraken's Eye" },
    'c3r2r5r3.1grogsMedicineA': {
        'description': "Hair of Undead Brigands has mystical powers needed for Doc's potion.",
        'title': 'Gather Undead Hair' },
    'c3r2r5r3.2grogsMedicineA': {
        'description': 'Big alligator saliva is the base for many potent medicines and potions.',
        'title': 'Gather Gator Saliva' },
    'c3r2r5r3.GrogsMedicineA': {
        'description': 'Gather ingredients for a potion to persuade Le Cerdo to serve.',
        'stringAfter': "Well done, for a pirate! Now... a few more things I needs for me \x01slant\x01 Persuasion Potion\x02, as I calls it.\x07And hurry... me potion goes bad if it's not finished quickly!",
        'title': 'Ingredients for Grog' },
    'c3r2r5r4.1grogsMedicineB': {
        'description': 'Wasp stingers give the potion a tangy taste.',
        'title': 'Wasp Stingers' },
    'c3r2r5r4.2grogsMedicineB': {
        'description': 'When distilled properly the bile acts as a truth serum - something every pirate fears more than death!',
        'title': 'Crab Bile' },
    'c3r2r5r4.GrogsMedicineB': {
        'description': 'Doc Grog needs more ingredients for the next step in his potion making process.',
        'items': 'Ingredients',
        'stringAfter': "Ah, good, good! These will work fine. Now all I need is a few more items and we'll be able to \x01slant\x01persuade\x02 Le Cerdo...\x07...that he'd make a fine addition to Captain Sparrow's crew.",
        'title': 'Ingredients for Grog' },
    'c3r2r5r5.1grogsMedicineC': {
        'description': 'Gather some bone dust from the Undead in the swamps.',
        'title': 'Recover Bone Dust' },
    'c3r2r5r5.2grogsMedicineC': {
        'description': "Croc water is found in the Huge Gator's stomach - and it reeks!",
        'title': 'Recover Croc Water' },
    'c3r2r5r5.3grogsMedicineC': {
        'description': 'Randic Fly Traps venom has no medicinal purpose but the foul stench makes pirates think the medicine is really good!',
        'title': 'Recover Fly Trap Venom' },
    'c3r2r5r5.GrogsMedicineC': {
        'description': 'These ingredients are critical to making the potion as disgustingly undrinkable as possible.',
        'items': 'Ingredients',
        'stringAfter': "Ey-ah! That smell's horrible!\x07Perfect! The worse it smells, the more it will press Le Cerdo to \x01slant\x01recover\x02 quickly.\x07I need to mix up this brew and then, it's almost finished. While it cures, make yourself useful...\x07...go rid the seas of those EITC scabs for me!",
        'title': 'Critical Ingredients' },
    'c3r2r5r7.1grogsMedicineD': {
        'description': 'Scrambled crab eggs add protein and more disgusting odor.',
        'title': 'Recover Crab Eggs' },
    'c3r2r5r7.2grogsMedicineD': {
        'description': 'A bile sack from a Giant Crab Boss packs a gigantinc voodoo powers.',
        'title': 'Recover Crab Bile' },
    'c3r2r5r7.3grogsMedicineD': {
        'description': 'The final piece of the potion requires some splintered wood from an Undead Phantom ship.',
        'title': 'Recover Splinters' },
    'c3r2r5r7.GrogsMedicineD': {
        'description': "The last step of Doc's Persuasion Potion requires 3 ingredients.",
        'items': 'Ingredients',
        'stringAfter': 'All done so quickly? Good work. And now, our potion for Le Cerdo should be ready...\x07Sorry, still \x01slant\x01curing\x02.\x07Go find Jack Sparrow and tell him of our plan. Jack will have his surgeon.',
        'title': 'Final Ingredients' },
    'c3r2r5r9.1undeadJob': {
        'description': 'Duelists have been assigned to find and assassinate Jack - get to them first!',
        'title': 'Defeat Duelists' },
    'c3r2r5r9.2undeadJob': {
        'description': 'The Conquistadors are angry with Jack for taking an Aztec amulet that belonged to them.',
        'title': 'Defeat Conquistadors' },
    'c3r2r5r9.3undeadJob': {
        'description': 'The pesky Bandidos swarmed Jack last time he landed there - so end their miserable existence!',
        'title': 'Defeat Bandidos' },
    'c3r2r5r9.UndeadJob': {
        'description': "Jolly Roger's minions have increased their efforts to find Jack and he needs your help!",
        'stringAfter': "Right, you again. Thanks for the assistance. Return to Doc Grog with me compliments for \x01slant\x01not\x02 sailing with us and...\x07Here's a smallish gift for Grog as a token of my esteem, savvy?",
        'title': 'Favors for Jack' },
    'c3r3Joshamee': {
        'description': 'Recruit the remaining crew members for the Black Pearl.',
        'items': 'Crew Members',
        'stringAfter': "Well done, mate!  Now that we've got a crew, let's get us a ship!\x07We've learned the Navy's holding the Pearl in a secret location...\x07... and our old friend Captain Montrose has the map!\x07Find that scallywag Montrose, capture and maroon 'im. He'll give up the map, sure as the sea.",
        'title': 'Second List' },
    'c3r3r1.10sinkShips': {
        'description': "Sink EITC ships on Duchamps' behalf.",
        'stringAfter': "Against my better judgment, I'll tell you where to find Gunner...\x07hiding out in a shack in town... maybe you can help jog his memory, that lousy ingrate carcass!",
        'title': 'Sink EITC Ships' },
    'c3r3r1.11visitGunner': {
        'description': "Find Gunner's shack out in Padres Del Fuego.",
        'stringAfter': "DO WHAT? SPEAK UP, MATE! BIT HARD OF HEARING! OCCUPATIONAL HAZARD I'D SAY\x07WHAT'S THAT? ...DUCHAMPS! HE'S THE REASON I'M HIDING. THINKS I STOLE HIS RUM!\x07I DIDN'T STEAL NOTHIN'. FOR ONCE!\x07TOO MANY CANNON BLASTS IS WHAT DONE THE STEALIN'...\x07...OF ME HEARING AND MEMORY, AYE!\x07HELP ME REPLACE DUCHAMPS RUM COLLECTION SO'LL BE FREE TO SERVE JACK!\x07IT INCLUDED SOME FISH RUM I BURIED 'ROUND THE ISLAND, RECOVER THAT FIRST, EY?",
        'title': 'Visit Gunner' },
    'c3r3r1.14deliverRum': {
        'description': 'Deliver 67 bottles of common rum to Duchamps.',
        'stringAfter': "That brainless barnacle has you cleanin' up after 'im, eh?\x07You must be ten times as witless as him...\x07I'll take your grog... but how do you plan on replacin' my lost bottle of \x01slant\x01Cutler 100\x02?\x07Not all rum's made of sugar and water, mate.\x07Now, leave here 'fore I report you as well!",
        'title': 'Deliver Rum To Duchamps' },
    'c3r3r1.15visitGunner': {
        'description': 'Go back to Gunner and ask about Cutler 100.',
        'stringAfter': "CUTLER 100 IS A VERY RARE BOTTLE, INDEED. BUT I'M WORKIN' ON A PLAN...\x07IN THE MEANTIME, THERE'S PLENTY MORE RUMS IN THE CARIBBEAN.\x07GO SEE \x01slant\x01PAUPER PEDRO\x02 AT THE RATSKELLAR.\x07.. HE'LL GIVE YOU THE NAME OF A HONEST 'RUNNER...\x07... IF THERE IS SUCH A THING!",
        'title': 'Visit Gunner' },
    'c3r3r1.16visitPedro': {
        'description': 'Ask Pedro the barkeep in the Ratskellar Tavern on Padres about an honest rumrunner.',
        'stringAfter': "I can't sell you more than 1 bottle. Fernando was just here and drank three himself!\x07But I'll give you the name of a good runner for a tip, shall we say...",
        'title': 'Visit Pedro' },
    'c3r3r1.17bribePedro': {
        'description': "Pay Pedro to give the name of an 'honest' rumrunner.",
        'stringAfter': "... 'is name is \x01slant\x01Fernando\x02... you can find 'im 'ere on Padres.",
        'title': 'Bribe Pedro' },
    'c3r3r1.18visitFernando': {
        'description': "Find Fernando, the 'honest' rumrunner.",
        'stringAfter': "Aye, I'll sell ye rum straight up. It'll cost ye plenty...",
        'title': 'Visit Fernando' },
    'c3r3r1.19bribeFernando': {
        'description': 'Pay Fernando for some rum.',
        'stringAfter': "Here it be. I'd not drink it all meself, if I were ye.",
        'title': 'Pay Fernando' },
    'c3r3r1.1visitOrinda': {
        'description': 'Ask Orinda if she knows the whereabouts of her old friend, Gunner.',
        'stringAfter': "I do know and I'll tell you but first... I need you to do me a \x01slant\x01favor\x02.\x07Some blaggard Navy blokes stole three valuable chests of mine.\x07I need you to recover 'em for me... and send them to Davy Jones locker!!",
        'title': 'Talk To Orinda' },
    'c3r3r1.20.5visitGunner': {
        'description': 'Return to Gunner and ask him about how to replace skeleton rum for Duchamps.',
        'stringAfter': "WE NEED TO REPLACE SOME OF DUCHAMPS'S \x01slant\x01UNCOMMON\x02 INVENTORY.\x07THAT MEANS SKELETON RUM. ONLY TWO WAYS TO ACQUIRE SKELETON RUM.\x07THAR'S STEALIN' IT... FROM JOLLY ROGER'S ARMY...\x07AND THE OTHER WAY IS TO \x01slant\x01MAKE IT\x02... ONLY I DON'T HAVE A RECIPE...\x07IF YOU WANT TO TRY MAKIN' IT... I SUGGEST YOU SPEAK TO \x01slant\x01ROMANY BEV\x02.",
        'title': 'Return To Gunner' },
    'c3r3r1.20deliverRum': {
        'description': 'Deliver 14 more bottles of common rum to Duchamps.',
        'stringAfter': "Not bad for a beginner...\x07... but I'll bet you won't find \x01slant\x01skeleton\x02 rum so easy to get 'hold of.",
        'title': 'Deliver Rum To Duchamps' },
    'c3r3r1.22deliverRum': {
        'description': 'Deliver the skeleton rum to Duchamps.',
        'stringAfter': "Excellent... I've been \x01slant\x01dying\x02 for a swig of this vintage!\x07Now ask Gunner 'bout my \x01slant\x01Singaporean\x02 rum.",
        'title': 'Deliver Rum' },
    'c3r3r1.23visitGunner': {
        'description': 'Return to Gunner with skeleton rum.',
        'stringAfter': "ALRIGHT MATE, WE GOTS OUR SKELETON RUM. NOW WE NEEDS SOME SINGAPOREAN RUM.\x07I KNOW NOTHIN' ABOUT THE STUFF SO...\x07GO ASK PEDRO, WORKS IN A TAVERN. HE'LL KNOW!",
        'title': 'Deliver Skeleton Rum' },
    'c3r3r1.24visitJoshamee': {
        'description': 'Ask Joshamee Gibbs about Singaporean rum.',
        'stringAfter': "Singaporean rum! They say it be made of unicorn milk... if ye believe such things.\x07To be honest, even \x01slant\x01I\x02 don't believe that one...\x07After all, I've made it me-self!\x07And I've not looked in a mirror fer a while, but I be certain there's no horn atop me head.\x07Right then... Singaporean rum. Two ways to stab it, mate...\x07Steal it or make it... both harder than skinnin' a Kraken.\x07I've heard of a \x01slant\x01Captain Archer\x02 in the Navy who has a weakness for it...\x07Here's how I make it... should Archer turn out to be more trouble than he's worth...",
        'title': 'Visit Joshamee' },
    'c3r3r1.26deliverRum': {
        'description': 'Deliver 5 bottles of Singaporean rum to Duchamps.',
        'stringAfter': "You're a better pirate than you look, mate.\x07Well, I've got another one for ole Gunner.\x07Tell him I want my voodoo rum back too - all 5 bottles!",
        'title': 'Deliver Singaporean Rum' },
    'c3r3r1.27visitGunner': {
        'description': 'Return to Gunner with singaporean rum.',
        'stringAfter': "BEGAD YOU GOT THAT SINGAPOREAN RUM QUICKLY.\x07TIME TO REPLACE THE VOODOO RUM.\x07BEST NOT TO \x01slant\x01STEAL\x02 IT... YOU'LL LIKELY END UP CURSED.\x07TRUTH IS... THAR'S TIMES WHEN IT'S BROUGHT ME A STREAK OF GOOD LUCK...\x07OTHER TIMES... NOT SO MUCH...\x07IF I WERE YE...I'D ASK ROMANY AGAIN ABOUT HOW TO MAKE A BATCH.",
        'title': 'Deliver Singaporean Rum' },
    'c3r3r1.28visitRomany': {
        'description': 'Romany Bev knows a lot about dark magic including what it takes to make a batch of voodoo rum.',
        'stringAfter': "Oh, it's you again! ...voodoo rum you say?!\x07You're playin' with some dark magic here, better hope it won't be hauntin' you back.\x07Get me those ingredients and I will see what I can do.",
        'title': 'Talk to Romany Bev' },
    'c3r3r1.29deliverRum': {
        'description': 'Deliver 5 bottles of voodoo rum to Duchamps.',
        'stringAfter': "Voodoo rum... excellent stuff.\x07Don't make it me-self any more... Always forget to turn widdershins and my head grows four sizes too large.\x07Ruined four or five of my favorite hats that way.\x07Now, back to business. I don't suppose Gunner still has my 25 year rum, eh?",
        'title': 'Deliver Voodoo Rum' },
    'c3r3r1.2deliverCargo': {
        'description': 'Deliver cargo to Graham Marsh.',
        'stringAfter': "This is for \x01slant\x01Orinda\x02. Be sure she gets it... or I'll have you keelhauled!\x07Plenty of Navy about... be swift!",
        'title': 'Deliver Cargo' },
    'c3r3r1.2recoverChests': {
        'description': "Steal Orinda's chests back from the Navy.",
        'stringAfter': "Okay mate, well done. Ye can find Gunner but...\x07He's in hiding. Got into some trouble with \x01slant\x01Duchamps\x02, the rumrunner...\x07I suspect he gave up Gunner to the East India Trading Company... 'cause he's not been seen since.\x07Go ask Duchamps. He's over on Padres Del Fuego. But a word of warning... it will cost ye.",
        'title': 'Recover Chests' },
    'c3r3r1.30deliverGunner': {
        'description': 'Return to Gunner with voodoo rum.',
        'stringAfter': "BLIMEY, YE BE GOOD AT THIS!\x07OLE JACK WILL BE RECRUITIN' YE AS WELL!\x07TIME TO REPLACE THE 25 YEAR OLD RUM. GO SEE IF FERNANDO HAS SOME IN HIS STASH.",
        'title': 'Deliver Voodoo Rum' },
    'c3r3r1.30visitGunner': {
        'description': "Ask Gunner about Duchamps' 25 year rum.",
        'stringAfter': "25 YEAR RUM... ONLY KNOW OF \x01slant\x01TWO\x02 MEN WHO'VE EVER TASTED IT...\x07THAT BE JOSHAMEE GIBBS... AND A 'RUNNER NAMED BEN FLATTS.\x07FLATTS... HE FOUND HIMSELF CORNERED WITH NO WEAPON BUT THAT BOTTLE OF 25...\x07... CRACKED IT OVER A SKELETON'S HEAD, HE DID!\x07LOST MOST OF THE 25 YEAR OF COURSE... BUT WAS ABLE TO ENJOY THE LAST SIP...\x07... AFTER DISPATCHING SAID SKELETON.\x07SO YE HAVE THREE OPTIONS, MATE...\x07SPEAK TO FLATTS AND GIBBS - THEY MAY BE ABLE TO HELP YE FIND SOME...\x07OR TRY \x01slant\x01MAKIN'\x02 IT IF YE HAVE GOT THE \x01slant\x01PATIENCE\x02...\x07ON SECOND THOUGHT, YOU REALLY JUST HAVE TWO OPTIONS - NO PIRATE'S GOT THAT MUCH PATIENCE!",
        'title': 'Visit Gunner' },
    'c3r3r1.32deliverRum': {
        'description': 'Take the bottle of 25 year old rum to Duchamps.',
        'stringAfter': "25 year old rum... amazing! I'm impressed, mate!\x07Still... 25 year old rum is common as sand compared to a bottle of Barbossa's own...\x07Let's see you come back with that in hand!\x07Get caught stealin' from Barbossa and you'll have no hands to carry!",
        'title': 'Deliver Rum' },
    'c3r3r1.33visitGunner': {
        'description': "Ask Gunner about Barbossa's rum.",
        'stringAfter': "WELL, BEST TO SPEAK TO BARBOSSA HIMSELF...\x07LAST PIRATE WHO TRIED TO WREST THE RECIPE FROM BARBOSSA'S GRIP...\x07WELL THEY DON'T HAVE MUCH TO GRIP WITH NOW...\x07OL' BARBOSSA LOPPED OFF THEIR HANDS, HE DID!\x07AS I SAID... BEST ASK 'IM YERSELF...",
        'title': 'Return To Gunner' },
    'c3r3r1.34visitBarbossa': {
        'description': 'Ask Barbossa about his personal rum.',
        'stringAfter': "So you want my rum?! First I be needin' something from you!\x07Now, thar's this rascal... calls himself \x01slant\x01Trent\x02...\x07He took somethin' of mine... I want it back.\x07Double-crossed me he did... now you'll be doin' the double-crossin'...\x07He's locked up... Navy's got him on a ship someplace.\x07I want you to spring him out. But when you get 'im on your ship...\x07... all alone... and he thinks he be headed back to Tortuga, all safe and sound...\x07Send him to Davy Jones! Or maroon him! I don't care... whatever you choose.\x07Only make sure you take a \x01slant\x01small key\x02 from around 'is neck first.\x07Aye... it's a double-cross!",
        'title': 'Visit Barbossa' },
    'c3r3r1.35captureTrent': {
        'description': 'Capture Trent from a Navy ship.',
        'title': 'Capture Trent' },
    'c3r3r1.36maroonTrent': {
        'description': 'Maroon Trent on any wild island to compel him to give up his key.',
        'title': 'Maroon Trent' },
    'c3r3r1.37deliverKey': {
        'description': 'Take Barbossa his key.',
        'stringAfter': "And the key?\x07Ah... I'll tell you one day what the key be for...\x07... but I suspect you'll be wantin' your rum...\x07Now be gone!",
        'title': 'Deliver Key' },
    'c3r3r1.38deliverRum': {
        'description': "Take the bottle of Barbossa's rum to Duchamps.",
        'stringAfter': "Impressive! That's some pirating to talk Barbossa himself out of a bottle o' his finest rum!\x07Still... Barbossa is at least a pirate. I doubt Beckett will be so hospitable...",
        'title': 'Deliver Rum' },
    'c3r3r1.39visitGunner': {
        'description': 'Return to Gunner with a 25 year old rum.',
        'stringAfter': "THAT'S SOME QUALITY 25 YEAR OLD RUM!\x07THE NEXT ONE IS RATHER SPECIAL, \x01slant\x01CUTLER 100\x02 IT'S CALLED AND I HAVE A GOOD PLAN TO RECOVER IT.\x07SOMEONE MUST MAKE THE CUTLER 100 FOR BECKETT SO...\x07SINK AN EAST INDIA TRADING COMPANY SHIP UNTIL YE FINDS A CAPTAIN JONES.\x07JONES IS EITHER MAKIN' IT FOR HIM, OR KNOWS WHO IS.",
        'title': 'Deliver 25 Year Old Rum' },
    'c3r3r1.3deliverCoins': {
        'description': 'Deliver payment to Orinda.',
        'stringAfter': "Good work. I have something else for you...\x07Navy stole a chest from me... I'd like it back.",
        'title': 'Deliver Payment' },
    'c3r3r1.40captureJones': {
        'description': 'See if Captain Jones knows who is making the Cutler 100 rum.',
        'title': 'Capture Captain Jones' },
    'c3r3r1.41visitMorris': {
        'description': 'Captain Jones said to talk to Morris about the Cutler 100 rum.',
        'stringAfter': "Cutler 100? Ha, that's rich. But...\x07I might tell ye more, swabbie, if ye will do me a little favor, ey?",
        'title': 'Visit Morris' },
    'c3r3r1.42recoverFlags': {
        'description': 'Sink 12 EITC ships for Morris in retaliation for stopping 12 of his most profitable shipments.',
        'stringAfter': "Well done, a fine pirate ye will make.\x07I don't know about the rum but I do know there's a secret scheduling list that tells all.\x07Steal it, and that'll be yer key.",
        'title': 'Recover Flags' },
    'c3r3r1.42visitPedro': {
        'description': 'Buy Morris a drink.',
        'stringAfter': "That'll cost a few coins, mate.",
        'title': 'Buy Drink' },
    'c3r3r1.43bribePedro': {
        'description': 'Pay the bartender.',
        'stringAfter': 'Here you go, mate.',
        'title': 'Buy Drink' },
    'c3r3r1.44deliverDrink': {
        'description': 'Take Morris his drink.',
        'stringAfter': "Right then... so you're lookin' for a bottle of Cutler 100 and you figured ol' Morris'd have one...\x07Do ye think I'd be seated here, at this pigsty, if I had me such a prize?\x07Cutler! I despise that beast.  Said I be lucky he didn't hang me from the yardarms, he did!\x07And for what? A quick sip of the good stuff?\x07Course, I am guilty... but who could resist?\x07Now is me time for some...revenge\x07I want Sir Stinkbeckett to feel the sting a bit.\x07Yes, a good helpin' of \x01slant\x01revenge\x02 is what we need...",
        'title': 'Deliver Drink' },
    'c3r3r1.45recoverFlags': {
        'description': 'Sink East India Trading Company ships and return with their flags.',
        'stringAfter': "Jolly good, mate! How 'bout another round...",
        'title': 'Recover Flags' },
    'c3r3r1.46visitPedro': {
        'description': 'Buy Morris a drink.',
        'stringAfter': "That'll cost a few coins.",
        'title': 'Buy Drink' },
    'c3r3r1.47bribePedro': {
        'description': 'Pay the bartender.',
        'stringAfter': 'Here you go, mate.',
        'title': 'Buy Drink' },
    'c3r3r1.48deliverDrink': {
        'description': 'Take Morris his drink.',
        'stringAfter': "Four flags, four ships... I feel four times better!\x07Bottle of 100 is it? Ok... here's what to do.\x07Cutler has the stuff made on some island near Cuba...\x07All I knows is that a case of 100 arrives... \x01slant\x01about\x02 once a month.\x07There's a bloke whose name I can't recall... who has a copy of the schedule...\x07Used to work up in Fort Dundee on Padres Del Fuego.",
        'title': 'Deliver Drink' },
    'c3r3r1.49stealSchedule': {
        'description': "The shipping schedule for Beckett's rum should reveal some useful information.",
        'stringAfter': "Aye, that's the schedule all right. Look! That's the ship you want mate, the \x01slant\x01EITC Marauder\x02.",
        'title': 'Steal Shipping Schedule' },
    'c3r3r1.4recoverChest': {
        'description': "Steal Orinda's chest back from the Navy.",
        'stringAfter': "Ok ye done well. I'll tell ye where to find Gunner.\x07He's in hiding. Got into some trouble with \x01slant\x01Duchamps\x02, the rumrunner...\x07I suspect Duchamps gave his name to the East India Trading Company... 'cause he hasn't been seen since.\x07Since Duchamps got him \x01slant\x01noticed\x02, maybe he might also know where to find him.\x07Duchamps operates out of \x01slant\x01Padres Del Fuego\x02, the volcano island.",
        'title': 'Recover Chest' },
    'c3r3r1.50plunderRum': {
        'description': 'EITC Marauders should carry the rum you are looking for.',
        'title': 'Recover Cutler 100' },
    'c3r3r1.50recoverRum': {
        'description': "Sink East India ships until you come across the Royal Barbados carrying Beckett's Cutler 100 rum.",
        'title': 'Recover Cutler 100' },
    'c3r3r1.51deliverRum': {
        'description': 'Take Duchamps the bottle of Cutler 100.',
        'stringAfter': "Most impressive! I've half a mind to hire you on my crew!\x07Well, you tell that half wit Gunner that he's a free man as far's I'm concerned.\x07I'll take care of things with the East India thugs for him.",
        'title': 'Deliver The Cutler 100' },
    'c3r3r1.52visitGunner': {
        'description': 'Return to Gunner with the Cutler 100 rum.',
        'stringAfter': "WELL DONE! WELL DONE! I OWE YOU ONE, MATE!\x07I WILL GIVE ALL THAT RUM STASH BACK TO DUCHAMPS FREEING ME OF ALL OBLIGATIONS.\x07YOU CAN TELL OLE MASTER GIBBS HE'S GOT HIMSELF A FIRST RATE GUNNER!",
        'title': 'Deliver The Cutler 100' },
    'c3r3r1.53visitJoshamee': {
        'description': 'Tell Joshamee Gibbs that Gunner is ready to go.',
        'title': 'Return To Gibbs' },
    'c3r3r1.5visitDuchamps': {
        'description': 'See if Duchamps knows where Gunner is hiding.',
        'stringAfter': "Gunner? That addled old fool!\x07I trusted him with the most valuable rum... and he plundered it!\x07...then claimed to \x01slant\x01forget\x02 where he hid the stash! So I informed some East India gents as to his whereabouts.\x07But time has soothed me anger and old Gunner's managed to avoid Beckett's men so far.\x07I'll let on to his whereabouts, if ye help eliminate some of me \x01slant\x01competition\x02, savvy?",
        'title': 'Talk To Duchamps' },
    'c3r3r1.6visitOlivier': {
        'description': "Ask Olivier at the docks about Duchamps' barrel.",
        'stringAfter': "Aye, I know the barrel Duchamps speaks of. Won't be easy to find... ever visit Rumrunner's Isle?\x07Not much there, at least not above ground.",
        'title': 'Talk To Olivier' },
    'c3r3r1.7recoverBarrel': {
        'description': "Dig up Duchamps' barrel on Rumrunner's Isle.  Return it to Olivier on Padres Del Fuego.",
        'stringAfter': "That's the one. Quick - take it to \x01slant\x01Duchamps\x02. Wouldn't want any Navy blokes catching you with it.",
        'title': "Recover Duchamps' Barrel" },
    'c3r3r1.8deliverBarrel': {
        'description': 'Take Duchamps his barrel.',
        'stringAfter': "That was a proper bit of pirating, mate! I'm warming up to you...\x07... but if you want to speak to Gunner, I'll be needing one more thing...",
        'title': 'Deliver Barrel' },
    'c3r3r1.9sinkShips': {
        'description': 'Sink Navy ships to clear the trade route for Duchamps.',
        'stringAfter': "Not bad... for a scab like you!\x07One last task... and I'll tell you how to find Gunner and his rotten stinkbucket of a brain.",
        'title': 'Eliminate Competition' },
    'c3r3r1Gunner': {
        'description': 'Help Gunner settle his rum obligations.',
        'stringAfter': "Good, mate, fine work! We got ourselves a Gunner!\x07Now I hear \x01slant\x01Scary's\x02 last crew marooned her and left her for dead. \x07Begad she's a strange one but ole Jack has a shine for her, so see if ye can track her down.\x07\x01slant\x01Orinda\x02 might have an idea where to find the hag... er uh, lady.",
        'title': 'Black Pearl Recruit: Gunner' },
    'c3r3r1r12.1fishRum': {
        'description': 'Find the spot in Padres Del Fuego where Gunner buried his bottle of fish rum and recover it. He said he buried it around town somewhere.',
        'stringAfter': "AHHH! REMINDS ME OF THE SEA!\x07AND BY THAT I MEANS THE FINE SMELL OF DECAYIN' FISH!\x07DUCHAMPS' COLLECTION INCLUDED SOME COMMON RUM, LET'S DEAL WITH RECOVERIN' THOSE FIRST.",
        'title': 'Fish Rum' },
    'c3r3r1r12.2Grog': {
        'description': 'Recover a bottle of grog.',
        'stringAfter': 'THE STINKIER THE BETTER, WHEN IT COMES TO GROG!',
        'title': 'Grog' },
    'c3r3r1r12.3lightRum': {
        'description': 'Recover a bottle of light rum.',
        'stringAfter': 'SEE HOW IT CATCHES THE LIGHT, EH?',
        'stringBefore': "LIGHT RUM'S THE PRETTIEST OF THE LOT.\x07NAVY BLOKES FAVOR THE STUFF.",
        'title': 'Light Rum' },
    'c3r3r1r12.4darkRum': {
        'description': 'Recover a bottle of dark rum.',
        'stringAfter': 'BETTER GO EASY ON THIS STUFF, MATE.',
        'stringBefore': "DARK RUM'S THICK. STICKS TO YER RIBS, IT DOES.\x07A BIT MORE RARE THAN THE LIGHT STUFF. I'D TRY STEALIN' IT FROM THE EAST INDIA COMPANY.",
        'title': 'Dark Rum' },
    'c3r3r1r12.5fiveYearRum': {
        'description': 'Recover a bottle of 5-year old rum.',
        'stringAfter': 'TAKES PATIENCE TO LET A FINE BOTTLE GO UNCORKED LIKE THAT.',
        'stringBefore': 'WHEN YOU AGE RUM, IT GETS EVEN BETTER.\x07THE GOOD STUFF IS RESERVED FOR NAVY CAPTAINS AND THE LIKE.',
        'title': '5-Year Old Rum' },
    'c3r3r1r12.6tenYearRum': {
        'description': 'Recover a bottle of 10-year old rum.',
        'stringAfter': "A PIRATE WOULD GIVE 'IS HAND FOR A BOTTLE OF THIS FINE RUM",
        'stringBefore': "NOW 10-YEAR OLD RUM, THAT'S SOMETHING SPECIAL!\x07YOU'D NEED TO BE AN EAST INDIA COMPANY CAPTAIN TO HAVE A BOTTLE OF THIS.",
        'title': '10-Year Old Rum' },
    'c3r3r1r12.7skeletonRum': {
        'description': 'Recover a bottle of skeleton rum.',
        'stringAfter': 'NEVER KNOW WHAT YE WILL GET IN A BOTTLE OF SKELETON RUM!',
        'stringBefore': 'SKELETON RUM - TASTY BUT DANGEROUS.',
        'title': 'Skeleton Rum' },
    'c3r3r1r12LearnRum': {
        'description': 'The only way for Duchamps to forgive Gunner for loosing his stash is to recreate his impressive rum collection.',
        'items': 'Bottles',
        'stringAfter': "YER GETTIN' SOME GOOD PROGRESS, MATE! BUT THERE IS STILL A LOT LEFT.\x07DUCHAMPS' COLLECTION ALSO INCLUDED SOME EITC AND NAVY BRANDED RUM.",
        'title': "Duchamps' Rum Collection" },
    'c3r3r1r12r2.1recoverRum': {
        'description': "Grog is a watered down version of rum, and it stinks, a sure sign that it's good!",
        'title': 'Grog' },
    'c3r3r1r12r2.2recoverRum': {
        'description': "Light rum's the prettiest of the lot. Navy blokes favor this variety.",
        'title': 'Light Rum' },
    'c3r3r1r12r2.3recoverRum': {
        'description': "Dark rum's thick, almost syrupy and is a bit more rare than the light stuff.",
        'title': 'Dark Rum' },
    'c3r3r1r12r2.RecoverRum': {
        'description': "Recover different kinds of common rum to replace Duchamps' rum collection.",
        'stringAfter': "VERY GOOD! TIME TO RECOVER THE MORE \x01slant\x01EXOTIC\x02 SEA FEARIN' VARIETIES!",
        'title': 'Common Rum' },
    'c3r3r1r12r3.1recoverRum': {
        'description': 'When you age rum, it gets even better. The good stuff is reserved for Navy Captains.',
        'title': 'Five Year Old Rum' },
    'c3r3r1r12r3.2recoverRum': {
        'description': "10-year old rum is something special. You'd need to be an EITC captain just to have a bottle... if not, you'd be severely punished!",
        'title': 'Ten Year Old Rum' },
    'c3r3r1r12r3.3recoverRum': {
        'description': 'Bone rum - tasty but dangerous. You never know what you will get in a bottle of bone rum, might even be death!',
        'title': 'Bone Rum' },
    'c3r3r1r12r3.RecoverRum': {
        'description': "Recover different kinds of more exotic rum from Duchamps' collection.",
        'stringAfter': 'EXCELLENT WORK, MATE! I SEE WHY CAPTAIN JACK HAS TAKEN TO THE LIKES OF YE!',
        'title': 'Exotic Rum' },
    'c3r3r1r13Rum': {
        'description': "To replace Duchamps' rum collection, you need to brew some rum on your own.",
        'items': 'Cases of Rum',
        'stringAfter': "VERY GOOD! NOW, WE'VE GOTTA GET OUR HANDS ON SOME...\x07SKELETON RUM!\x07I AGREE MATE, DISGUSTING! BUT WE GOTS TO HAVE IT. ASK ROMANY BEV, SHE KNOWS ALL ABOUT IT.",
        'title': 'Brewing Rum' },
    'c3r3r1r13r1.1visitRico': {
        'description': 'Go see Rico about buying rum from rumrunners.',
        'stringAfter': "You need \x01slant\x01how many\x02 bottles? Where be the festivities?\x07I can't sell you more than three bottles. Runnin' low me-self.\x07But I'll give you the name of a good rumrunner for a few coins...",
        'title': 'Talk To Rico' },
    'c3r3r1r13r1.2bribeRico': {
        'description': 'Bribe Rico to give you the name of a good rumrunner.',
        'stringAfter': "... 'is name is \x01slant\x01Garrett\x02...\x07... just \x01slant\x01Garrett\x02.",
        'title': 'Bribe Rico' },
    'c3r3r1r13r1.3visitGarrett': {
        'description': 'Talk to Garrett about buying some rum.',
        'stringAfter': 'You need how much? Cost you dearly, that will.',
        'title': 'Talk To Garrett' },
    'c3r3r1r13r1.4bribeGarrett': {
        'description': 'Buy rum from Garrett.',
        'stringAfter': 'You drive a hard bargain, mate.',
        'title': 'Pay Garrett' },
    'c3r3r1r13r1.5deliverRum': {
        'description': 'Take the purchased rum to Gunner.',
        'title': 'Deliver Rum To Gunner' },
    'c3r3r1r13r1buyRum': {
        'description': 'Buy rum from rumrunners.',
        'stringAfter': 'THAT LOT MUST HAVE COST YE A PRETTY PENNY!',
        'stringBefore': "BUY IT? YE MUST 'AVE COME ACROSS A NICE PIECE OF PROFIT, AYE?\x07WATCH YER BACK, MATE! IN MY EXPERIENCE, THE GOOD TIMES DON'T LAST LONG...\x07GO VISIT CARVER AT THE FAITHFUL BRIDE. HE'LL POINT YE TO A 'RUNNER.",
        'title': 'Buy Rum' },
    'c3r3r1r13r2.1findRum': {
        'description': 'The Navy commissioned local rum makers to make their own brand and Duchamps bribed Navy guards to get some - Gunner lost them too.',
        'title': 'Navy Rum' },
    'c3r3r1r13r2.1recoverRum': {
        'description': 'Steal Rum from the Navy.',
        'stringAfter': "NAVY BLOKES WILL BE MISSIN' THIS... TRUST ME!",
        'title': 'Steal Navy Rum' },
    'c3r3r1r13r2.2findRum': {
        'description': 'Duchamps did a brisk business selling bottles of EITC rum they brew for themselves - Gunner lost those as well and must be replaced.',
        'title': 'EITC Rum' },
    'c3r3r1r13r2.2recoverRum': {
        'description': 'Steal Rum from the East India Trading Company.',
        'title': 'Steal EITC Rum' },
    'c3r3r1r13r2.FindRum': {
        'description': "Recover Navy and EITC branded rums for Duchamps' collection.",
        'stringAfter': "I DON'T THINKS MUCH OF THE NAVY OR THE EITC BUT...\x07THOSE BLAGGARDS SURE KNOW GOOD RUM!\x07BUT IT'S STILL NOT ENOUGH, LET'S MAKE OUR OWN, EY?!\x07GOTTA HAVE SOMETHIN' TO PUT THE RUM IN SO...\x07START WITH FINDIN' SOME GOOD GLASS BOTTLES... THEN THE INGREDIENTS!",
        'title': 'Branded Rum' },
    'c3r3r1r13r2stealRum': {
        'description': 'Steal Rum.',
        'stringAfter': "THAT'S SOME GOOD PIRATIN'!",
        'stringBefore': "STEAL IT, AYE? GOOD CHOICE...\x07NOTHIN' SAYS 'PIRATE' LIKE LIFTIN' A BOTTLE OF GOOD RUM!\x07BEST PLACE TO NAB YOURSELF A BOTTLE IS THE TRADE ROUTES.\x07EAST INDIA LIKES TO SKULK ABOUT IN 'EM, AND NAVY TOO.",
        'title': 'Steal Rum' },
    'c3r3r1r13r3.1poker': {
        'description': 'Win at poker in order to acquire stashed rum.',
        'stringAfter': "YE MUST'VE CLEANED OUT MOST THEM POKER PLAYERS...\x07... BEST TRY BLACKJACK THEN.",
        'title': 'Win Rum At Poker' },
    'c3r3r1r13r3.2blackjack': {
        'description': 'Win at blackjack in order to acquire stashed rum.',
        'title': 'Win Rum At Blackjack' },
    'c3r3r1r13r3winRum': {
        'description': 'Win Rum at the card table.',
        'stringAfter': 'YE BE LUCKIER THAN YE LOOK, MATE!',
        'stringBefore': "CARD SHARK EH? I'VE HAD A BAD STREAK OF LUCK, MESELF...\x07GUESS THAT'S WHY I BE STUCK HERE AND YE BE \x01slant\x01OUT THERE\x02, SAVIN' ME SCURVY HIDE.\x07WELL, LET'S HOPE YER LUCK HOLDS, MATE!\x07YE CAN FIND A GAME IN ANY TAVERN ON TORTUGA...\x07GET THE RIGHT PLAYER TO OWE YE... AND THEY'LL BE FORCED TO PAY UP WITH THEIR RUM STASH!",
        'title': 'Win Rum' },
    'c3r3r1r13r4.1getEmptyBottles': {
        'description': "To make your own rum, you've got to gather the ingredients, starting with... empty rum bottles.",
        'stringAfter': "GROG IS THE EASIEST TO MAKE, LET'S START WITH THAT!",
        'title': 'Acquire Empty Bottles' },
    'c3r3r1r13r4.1recoverLadle': {
        'description': 'Steal a big ladle from a Navy ship.',
        'stringAfter': "ALL RIGHT! NOW WE CAN GET STARTED!\x07GROG IS THE EASIEST RUM TO MAKE!\x07HERE'S HOW IT'S DONE...\x07 8 CUPS OF SUGAR, 3 CUPS WATER, 1 FISTFUL OF MUD, 1 BOTTLE, AND BURY IT FOR 10 MINUTES IN THE SUN.\x07WE THROW MUD IN THERE TO SPEED THINGS UP!\x07GROG IS A GOOD DRINK FOR IMPATIENT TYPES...",
        'title': 'Acquire A Ladle' },
    'c3r3r1r13r4makeRum': {
        'description': 'Make your own rum.',
        'stringAfter': "I THINKS YE MISSED YER CALLING, MATE - SHOULD'VE BEEN A RUMMY!",
        'title': 'Make Rum' },
    'c3r3r1r13r4r2.1grogIngredients': {
        'description': 'Steal sugar from Spanish Undead Bandidos who consume it by the barrels to stay upright and ready for fighting.',
        'title': 'Sugar' },
    'c3r3r1r13r4r2.1recoverSugar': {
        'description': 'Steal sugar from a Navy ship.',
        'stringAfter': "THAT'S PLENTY! WELL DONE, MATE!",
        'stringBefore': 'SUGAR BE FOUND ABOARD NAVY SHIPS.',
        'title': '8 Cups of Sugar' },
    'c3r3r1r13r4r2.2grogIngredients': {
        'description': 'Steal water from Undead Duelists but be careful - they are expert swordsmen!',
        'title': 'Water Canteens' },
    'c3r3r1r13r4r2.2recoverWater': {
        'description': 'Steal water from EITC goons.',
        'stringAfter': 'LOOKS GOOD ENOUGH TO DRINK!',
        'stringBefore': "YE NEED THE PURIST WATER AVAILABLE... EAST INDIA MAGGOTS ALWAYS HAVE PURE WATER ON 'EM!",
        'title': '3 Water Canteens' },
    'c3r3r1r13r4r2.3grogIngredients': {
        'description': 'Acquire the savory mud that Undead Piratas collect on their boney feet.',
        'title': 'Fistful of Mud' },
    'c3r3r1r13r4r2.3recoverMud': {
        'description': 'Fetch mud from beneath a giant Venus Flytrap.',
        'stringAfter': "IT'S WORTH THE EXTRA EFFORT, MATE!",
        'stringBefore': "ANY MUD WILL DO, BUT MUD FROM BENEATH ONE OF THEM GIANT MAN-EATING PLANTS...\x07WELL, IT JUST TASTES BETTER. DON'T ASK ME WHY.",
        'title': '1 Fistful of Mud' },
    'c3r3r1r13r4r2.4recoverBottle': {
        'description': 'Steal a bottle from Navy guards.',
        'stringAfter': "RUM'S NO BETTER THAN THE BOTTLE IT COMES IN, I SAYS!",
        'stringBefore': "YE BE NEEDIN' A STURDY BOTTLE, LIKE THE ONES NAVY GUARDS CARRY.",
        'title': '1 Bottle' },
    'c3r3r1r13r4r2.GrogIngredients': {
        'description': 'Recover the ingredients to make grog.',
        'items': 'Ingredients',
        'stringAfter': "AACH! BLECH! MAYBE NOT SO MUCH MUD NEXT TIME, ME BUCKO!\x07NOW LET'S BREW UP A BATCH OF LIGHT RUM, SORT OF LIKE GROG...\x07BUT TAKES A BIT LONGER TO MAKE.",
        'title': 'Make Grog' },
    'c3r3r1r13r4r2makeGrog': {
        'description': 'Recover the ingredients to make grog.',
        'items': 'Ingredients',
        'stringAfter': "AACH! BLECH! MAYBE NOT SO MUCH MUD NEXT TIME, MATE!\x07NOW LIGHT RUM, THAT'S A BETTER CHOICE...\x07SORT OF LIKE GROG... BUT TAKES A BIT LONGER.",
        'title': 'Make Grog' },
    'c3r3r1r13r4r3.1lightRumIngredients': {
        'description': 'EITC ships import the finest molasses from the northeastern colonies of America.',
        'title': 'Molasses' },
    'c3r3r1r13r4r3.1recoverMolasses': {
        'description': 'Steal molasses from Navy ships.',
        'stringAfter': 'NASTY STUFF, MOLASSES!',
        'stringBefore': 'MOLASSES IS MIGHTY HARD TO COME BY. BEST TRY NAVY SHIPS.',
        'title': 'Cups of Molasses' },
    'c3r3r1r13r4r3.2lightRumIngredients': {
        'description': 'Navy ships have perfected the water storage in these well-crafted barrels - best water in the Caribbean!',
        'title': 'Water Barrels' },
    'c3r3r1r13r4r3.2recoverWater': {
        'description': 'Steal water from EITC goons.',
        'stringAfter': "THAT'S THE BEST, MATE!",
        'stringBefore': "WE'LL NEED MORE OF THAT GOOD EAST INDIA WATER.",
        'title': '8 Water Canteens' },
    'c3r3r1r13r4r3.3lightRumIngredients': {
        'description': 'The best vanilla comes from the Spice Islands, another place where the EITC has a trade monopoly.',
        'title': 'Splash of Vanilla' },
    'c3r3r1r13r4r3.3recoverVanilla': {
        'description': 'Steal vanilla from EITC ships.',
        'stringAfter': 'NO LIGHT RUM WITHOUT VANILLA!',
        'stringBefore': "VANILLA, NOW THAT'S SOMETHIN' EAST INDIA MIGHT BE CARRYIN' AT SEA.",
        'title': '1 Splash of Vanilla' },
    'c3r3r1r13r4r3.4recoverBottle': {
        'description': 'Steal a bottle from Navy guards.',
        'stringAfter': "I DON'T KNOW HOW THEY MAKE 'EM SO SMOOTH!",
        'stringBefore': 'ANOTHER BOTTLE, MATE, FROM THE NAVY.',
        'title': '1 Bottle' },
    'c3r3r1r13r4r3.LightRumIngredients': {
        'description': 'Recover the ingredients to make light rum.',
        'items': 'Ingredients',
        'stringAfter': "THAT'S NOT HALF BAD! YE BE STARTIN' TO LEARN, MATE!\x07OKAY, LET'S TRY MAKIN' SWEET, DARK RUM. I DON'T FANCY IT... BUT HERE'S HOW TO MIX IT...",
        'title': 'Make Light Rum' },
    'c3r3r1r13r4r3makeLightRum': {
        'description': 'Recover the ingredients to make light rum.',
        'items': 'Ingredients',
        'stringAfter': "THAT'S NOT HALF BAD! YE BE STARTIN' TO LEARN, MATE!\x07OKAY, LET'S TRY MAKIN' SWEET, DARK RUM. I DON'T FANCY IT... BUT HERE'S HOW TO MIX IT...",
        'title': 'Make Light Rum' },
    'c3r3r1r13r4r4.1darkRumIngredients': {
        'description': "Collect this aged molasses that's stronger and thicker than ordinary varieties.",
        'title': 'Cups of Molasses' },
    'c3r3r1r13r4r4.1recoverMolasses': {
        'description': 'Steal molasses from Navy ships.',
        'stringAfter': "THAT'LL DO.",
        'stringBefore': "WE'LL NEED MORE OF THAT NAVY MOLASSES.",
        'title': '4 Cups Molasses' },
    'c3r3r1r13r4r4.2darkRumIngredients': {
        'description': 'The water carried by these Navy men gets tinny but it brings out the flavor of the other ingredients.',
        'title': 'Water Canteens' },
    'c3r3r1r13r4r4.2recoverWater': {
        'description': 'Steal water from EITC goons.',
        'stringAfter': 'GOOD. KEEP IT COMING, MATE.',
        'stringBefore': "WE'LL NEED MORE OF THAT GOOD EAST INDIA WATER.",
        'title': '10 Water Canteens' },
    'c3r3r1r13r4r4.3darkRumIngredients': {
        'description': "Recover vanilla that's stored deep in the Quarry, but be careful, it's very valuable and well guarded.",
        'title': 'Splash of Vanilla' },
    'c3r3r1r13r4r4.3recoverVanilla': {
        'description': 'Steal vanilla from EITC ships.',
        'stringAfter': 'ALMOST DONE, MATE, ALMOST... ',
        'stringBefore': 'WE NEED MORE OF THAT EAST INDIA VANILLA.',
        'title': '1 Splash of Vanilla' },
    'c3r3r1r13r4r4.4recoverBottle': {
        'description': 'Steal a bottle from Navy guards.',
        'stringAfter': "FINE BOTTLES, AIN'T THEY?",
        'stringBefore': 'ANOTHER BOTTLE, MATE, FROM THE NAVY.',
        'title': '1 Bottle' },
    'c3r3r1r13r4r4.DarkRumIngredients': {
        'description': 'Recover the ingredients to make dark rum.',
        'items': 'Ingredients',
        'stringAfter': 'THIS BE SOME FINE RUM!',
        'title': 'Make Dark Rum' },
    'c3r3r1r13r4r4makeDarkRum': {
        'description': 'Recover the ingredients to make dark rum.',
        'items': 'Ingredients',
        'stringAfter': 'THIS BE SOME FINE RUM. TAKE THIS TO DUCHAMPS!',
        'title': 'Make Dark Rum' },
    'c3r3r1r21.2recoverSkeletonRum': {
        'description': 'Steal skeleton rum from skeletons.',
        'title': 'Steal Skeleton Rum' },
    'c3r3r1r21r1.1visitRomany': {
        'description': 'Ask Romany Bev how to make skeleton rum.',
        'stringAfter': "A recipe for \x01slant\x01skeleton\x02 rum, eh? Dangerous stuff...\x07\x01slant\x01skeleton\x02 rum... it \x01slant\x01turns\x02 real quick... and kills real quick.\x07It goes rotten if it's sittin' around more than a few days.\x07That's why it's so rare... and things that're rare cannot be acquired on the cheap.\x07I want you to do a few \x01slant\x01dangerous\x02 things fer me.\x07I need these ingredients before we can begin.",
        'title': 'Visit Romany Bev' },
    'c3r3r1r21r1.2recoverSplinters': {
        'description': 'Recover splinters from flytraps for Romany Bev.',
        'stringAfter': "Don't ask me what I do with these - you don't wanna know.\x07Okay, here's what you need to make skeleton rum.",
        'title': 'Recover Splinters' },
    'c3r3r1r21r1.2skelRumIngredientsA': {
        'description': 'Skeleton rum is mystical as well as potent, so if some of the ingredients sound like they belong in a potion... they do!',
        'stringAfter': 'These are some fine splinters. Now gather me some hairs...\x07...from Undead. I hope ye are well acquainted with that cutlass of yers.',
        'title': 'Recover Splinters' },
    'c3r3r1r21r1makeSkeletonRum': {
        'description': 'Make skeleton rum.',
        'title': 'Make Skeleton Rum' },
    'c3r3r1r21r1r2.1recoverMolasses': {
        'description': 'Steal molasses from Navy ships.',
        'stringAfter': 'That will do.',
        'stringBefore': "We'll need some of that good Navy molasses.",
        'title': '5 Barrels of Molasses' },
    'c3r3r1r21r1r2.2recoverWater': {
        'description': 'Recover stagnant water from the belly of a flytrap.',
        'stringAfter': "It's hard to get, but worth it.",
        'stringBefore': 'Stagnant water is required, best from the belly of a giant venus flytrap.',
        'title': '3 Cups Stagnant Water' },
    'c3r3r1r21r1r2.3recoverDust': {
        'description': 'Get bone dust from undead skeletons.',
        'stringAfter': 'That should work just fine.',
        'stringBefore': 'Bone dust goes in there too. Just a pinch, but it needs to be the right sort of dust.',
        'title': '10 Pinches Of Bone Dust' },
    'c3r3r1r21r1r2.4recoverGas': {
        'description': 'Capture swamp gas from the belly of giant venus flytraps.',
        'stringAfter': 'It smells bad but works wonders.',
        'stringBefore': "Those giant flytraps also have the best swamp gas in 'em - bring me some.",
        'title': '1 Belch Of Swamp Gas' },
    'c3r3r1r21r1r2.5recoverStingers': {
        'description': 'Recover stingers from terror wasps.',
        'stringAfter': "Stingers give the rum it's kick.",
        'stringBefore': 'Terror Wasp stingers go in there too.',
        'title': '10 Terror Wasp Stingers' },
    'c3r3r1r21r1r2.6recoverBladder': {
        'description': 'Cut the bladder from a big alligator.',
        'stringAfter': 'Not as pretty as a bottle, but it does the job.',
        'stringBefore': 'We need to mix it all in a big gator bladder.',
        'title': '1 Big Alligator Bladder' },
    'c3r3r1r21r1r2ingredients': {
        'description': 'Gather ingredients to make skeleton rum.',
        'items': 'Ingredients',
        'stringAfter': 'Okay, here you go. For best results, be sure and bury it in a cemetery for 1 night...',
        'title': 'Skeleton Rum Ingredients' },
    'c3r3r1r21r1r3.1skelRumIngredientsB': {
        'description': 'Hair of the undead is essential in gypsy potions and beverages.',
        'title': 'Recover Undead Hair' },
    'c3r3r1r21r1r3.2skelRumIngredientsB': {
        'description': 'Bone dust is also a common element in gypsy potions, elixirs and... rum!',
        'title': 'Recover Bone Dust' },
    'c3r3r1r21r1r3.3skelRumIngredientsB': {
        'description': 'Undead toenails mellow out the other harsh flavors in skeleton rum.',
        'title': 'Recover Toenails' },
    'c3r3r1r21r1r3.SkelRumIngredientsB': {
        'description': 'Gather ingredients to make skeleton rum.',
        'items': 'Ingredients',
        'stringAfter': "Funny thing toenails - like bones, they almost never decay.\x07Those were only the mystical parts. Now we need the rum ingredients... if ye're still up to the challenge?",
        'title': 'Skeleton Rum Ingredients' },
    'c3r3r1r21r1r4.1skelRumIngredientsC': {
        'description': "The Rancid Fly Trap have a gas in their stomachs that's the perfect base for strong rum.",
        'title': 'Recover Gas' },
    'c3r3r1r21r1r4.2skelRumIngredientsC': {
        'description': "Stingers give the rum it's biting after taste and add to the potency.",
        'title': 'Recover Stingers' },
    'c3r3r1r21r1r4.3skelRumIngredientsC': {
        'description': 'Alligator bladders contain an acid that helps speed the fermentation process of the rum.',
        'title': 'Recover Bladders' },
    'c3r3r1r21r1r4.SkelRumIngredientsC': {
        'description': 'Gather ingredients to make skeleton rum.',
        'items': 'Ingredients',
        'stringAfter': '',
        'title': 'Skeleton Rum Ingredients' },
    'c3r3r1r21skeletonRum': {
        'description': 'Acquire replacement skeleton rum.',
        'items': 'Choices',
        'stringAfter': "Ahhh... all the ingredients for the skeleton rum. I'll mix it up quick, but do not...\x07...under any circumstances taste it on yer way back to Gunner. Lest ye die!",
        'title': 'Skeleton Rum' },
    'c3r3r1r25.1visitPauper': {
        'description': 'Pedro knows all kinds of exotic drinks and can help you find it for Gunner.',
        'stringAfter': "I'll not help a swab like you, but if it's for Gunner...\x07I will. Gather the ingredients first, but be warned... they are many.",
        'title': 'Talk to Pauper' },
    'c3r3r1r25SingaporeanRum': {
        'description': 'Replace Duchamps Singaporean rum.',
        'items': 'Choices',
        'stringAfter': 'Pedro thanks you for your \x01slant\x01concern\x02 for Gunner.\x07Give him my regards, and this fine rum.',
        'title': 'Singaporean Rum' },
    'c3r3r1r25r1.1visitCarver': {
        'description': 'Fetch a pint for Gibbs from Carver the bartender.',
        'stringAfter': "Gibbs? Put it on his tab, eh?  I suppose he's good for it...",
        'title': 'Fetch A Pint' },
    'c3r3r1r25r1.2deliverPint': {
        'description': 'Take Gibbs his pint.',
        'stringAfter': "Now that's more like it! Here's what we be needin' to start...",
        'title': 'Deliver Pint' },
    'c3r3r1r25r1makeSingaporeanRum': {
        'description': 'Make your own Singaporean Rum.',
        'title': 'Make Singaporean Rum' },
    'c3r3r1r25r1r3.1recoverMolasses': {
        'description': 'Steal molasses from Navy ships.',
        'stringAfter': 'Well done, mate.',
        'stringBefore': 'We need molasses. Navy ships carry it.',
        'title': '4 Barrels of Molasses' },
    'c3r3r1r25r1r3.2recoverHoney': {
        'description': 'Steal honey from EITC ships.',
        'stringAfter': 'Excellent work.',
        'stringBefore': 'We need honey. East India ships carry the stuff.',
        'title': '4 Barrels of Honey' },
    'c3r3r1r25r1r3.3recoverWater': {
        'description': 'Steal fresh water from EITC ships.',
        'stringAfter': 'The moonlit part is just for good measure.',
        'stringBefore': 'We need water. East India ships carry the freshest water.',
        'title': '2 Cups Moonlit Freshwater' },
    'c3r3r1r25r1r3.4recoverCinnamon': {
        'description': 'Steal cinnamon from Navy guards.',
        'stringAfter': 'Good job.',
        'stringBefore': "We need cinnamon. Navy blokes will have cinnamon on 'em. They fancy it in their tea.",
        'title': '12 Pinches of Cinnamon' },
    'c3r3r1r25r1r3.5recoverCoconut': {
        'description': 'Steal a coconut from EITC ships.',
        'stringAfter': "Surprisingly hard to find, seein' as how these islands 're full of coconuts.",
        'stringBefore': 'East India might be shipping coconuts. We just need one',
        'title': '4 Coconuts' },
    'c3r3r1r25r1r3.6recoverFeather': {
        'description': 'Steal a parrot feather from Navy guards.',
        'stringAfter': "Are ye sure that's from a parrot?",
        'stringBefore': "A parrot feather's the clincher, mate. Sometimes Navy will keep 'em fer good luck.",
        'title': '1 Parrot Feather' },
    'c3r3r1r25r1r3ingredients': {
        'description': 'Recover ingredients to make Singaporean rum.',
        'stringAfter': "Customarily we would bury this lot in sand fer two days, but I reckon nobody'll be the wiser.",
        'title': 'Singaporean Rum Ingredients' },
    'c3r3r1r25r2.1captureArcher': {
        'description': 'Capture Captain Archer from a Navy ship.',
        'title': 'Capture Captain Archer' },
    'c3r3r1r25r2.1singapRumIngredientsA': {
        'description': 'Navy ships bring in cane sugar from Cuba on a regular basis.',
        'title': 'Recover Cane Sugar' },
    'c3r3r1r25r2.2maroonArcher': {
        'description': 'Maroon Captain Archer to make him give up his stash of Singaporean rum.',
        'title': 'Maroon Captain Archer' },
    'c3r3r1r25r2.2singapRumIngredientsA': {
        'description': 'Capture barrels of imported Madagascar honey.',
        'title': 'Recover Honey' },
    'c3r3r1r25r2.3singapRumIngredientsA': {
        'description': 'EITC imports nutmeg from the Far East and it gives this Rum a unique flavor.',
        'title': 'Recover Nutmeg' },
    'c3r3r1r25r2.SingapRumIngredientsA': {
        'description': 'Gather ingredients to make singaporean rum.',
        'items': 'Ingredients',
        'stringAfter': "Not bad for a swabbie like you.\x07But there's more ingredients to be had. Here's a list.",
        'title': 'Singaporean Rum Ingredients' },
    'c3r3r1r25r2stealSingaporeanRum': {
        'description': 'Steal Singaporean Rum from the East India Trading Company.',
        'title': 'Steal Singaporean Rum' },
    'c3r3r1r25r3.1singapRumIngredientsB': {
        'description': 'Navy Veterans use a pinch of cinnamon to help their stamina on a hot, muggy day - which is every day in the islands.',
        'title': 'Recover Cinnamon' },
    'c3r3r1r25r3.2singapRumIngredientsB': {
        'description': 'Coconut juice gives the Singaporean rum its unique flavor.',
        'title': 'Recover Coconuts' },
    'c3r3r1r25r3.3singapRumIngredientsB': {
        'description': 'Another ingredient is two feathers from the Kanto Talca bird, thought to be sacred by gypsies and other superstitious types.',
        'title': 'Recover Feathers' },
    'c3r3r1r25r3.SingapRumIngredientsB': {
        'description': 'Gather ingredients to make singaporean rum.',
        'items': 'Ingredients',
        'stringAfter': '',
        'title': 'Singaporean Rum Ingredients' },
    'c3r3r1r28.1recoverMolasses': {
        'description': 'Steal molasses from Navy ships.',
        'stringAfter': 'I SUPPOSE WE SHOULD FIND AN EASIER WAY TO GET THIS STUFF!',
        'stringBefore': 'MOLASSES! ALWAYS NEED MOLASSES!',
        'title': '3 Barrels of Molasses' },
    'c3r3r1r28.1voodooRumIngredientsA': {
        'description': 'Navy Monarchs returning from the Spanish Main carry dark brown sugar that, unbeknownst to them, was cursed by a Voodoo Priest.',
        'title': 'Recover Cursed Sugar' },
    'c3r3r1r28.2recoverWater': {
        'description': 'Recover croc water from the bellies of giant gators.',
        'stringAfter': 'MAKES A GOOD SOUP TOO, THIS CROC WATER.',
        'stringBefore': 'CROC WATER GOES IN THERE TOO.',
        'title': '2 Cups Croc Water' },
    'c3r3r1r28.2voodooRumIngredientsA': {
        'description': 'Dread bitters is a natural herb used in medicines and drinks and EITC Marauder ships import it from Africa.',
        'title': 'Recover Bitters' },
    'c3r3r1r28.3recoverBarnacles': {
        'description': 'Recover cursed barnacles from skeleton ships.',
        'stringAfter': "CRUSH 'EM UP BEFORE GOING INTO THE MIX.",
        'stringBefore': 'WE NEED BARNACLES. CURSED ONES. YOU GET THEM OFF SKELETON SHIPS, MATE.',
        'title': '1 Cup Cursed Barnacles' },
    'c3r3r1r28.3voodooRumIngredientsA': {
        'description': "Sink a Revenant Ghost ship to recover the cursed barnacles clinging to it's grotesque hull.",
        'title': 'Recover Cursed Barnacles' },
    'c3r3r1r28.5recoverFleas': {
        'description': 'Recover fleas from skeleton pirates.',
        'stringAfter': 'CAREFUL WITH THEM FLEAS, MATE!',
        'stringBefore': "WE NEED FLEAS! A CUP OF FLEAS!\x07I'D TRY SKELETON PIRATES... THEY MAY BE DEAD, BUT THEY'RE STILL PIRATES!",
        'title': '6 Fleas' },
    'c3r3r1r28.6recoverTail': {
        'description': 'Recover the stinger from a dread scorpion.',
        'stringAfter': "THAT THAR'S A BEAUTY!",
        'stringBefore': 'DREAD SCORPION TAIL, WELL ACTUALLY THE STINGER. IT MUST BE FRESH!',
        'title': '1 Dread Scorpion Stinger' },
    'c3r3r1r28.7recoverTooth': {
        'description': 'Recover an alligator tooth.',
        'stringAfter': 'A FINE TOOTH YOU ACQUIRED, MATE!',
        'stringBefore': 'GATOR TOOTH GOES IN THE MIX TOO. THE BIGGER, THE BETTER.',
        'title': '1 Gator Tooth' },
    'c3r3r1r28.VoodooRumIngredientsA': {
        'description': 'Gather ingredients to make voodoo rum.',
        'items': 'Ingredients',
        'stringAfter': "Aye, that's the right stuff alright! Glad it was you and not me.\x07Only a few more things and we be done!",
        'title': 'Voodoo Rum Ingredients' },
    'c3r3r1r28makeVoodooRum': {
        'description': 'Gather ingredients to make voodoo rum.',
        'items': 'Ingredients',
        'stringAfter': "OKAY... NOW WE'RE GETTIN' SOMEWHERE!\x07A FEW MORE INGREDIENTS NOW...",
        'title': 'Make Voodoo Rum' },
    'c3r3r1r28makeVoodooRum2': {
        'description': 'Gather more ingredients to make voodoo rum.',
        'items': 'Ingredients',
        'stringAfter': 'WELL DONE, MATE! NOW BE QUICK AND TAKE THE LOT TO DUCHAMPS WITH MY APOLOGIES!',
        'title': 'Make Voodoo Rum' },
    'c3r3r1r28r4.1visitTomas': {
        'description': 'Ask June for hairballs from her parrot.',
        'stringAfter': "What's that? Hairballs? From my parrot?\x07You making rum or something? Well, no matter. Take as many as you like.",
        'title': 'Visit June' },
    'c3r3r1r28r4.2deliverHairballs': {
        'description': 'Take the hairballs back to Gunner.',
        'title': 'Deliver Hairballs' },
    'c3r3r1r28r4hairballs': {
        'description': 'Acquire 4 hairballs from parrots.',
        'stringAfter': 'GOOD WORK! FINE PARROT, EY?',
        'stringBefore': "THIS ONE'S ODD, BUT IMPORTANT. GO SEE \x01slant\x01JUNE\x02 IN TORTUGA ABOUT GETTING SOME HAIRBALLS FROM HER PARROT.",
        'title': '4 Hairballs Hocked Up By Parrots' },
    'c3r3r1r29.1voodooRumIngredientsB': {
        'description': 'Livers from the fleas that cover the Undead add a tangy flavor to the voodoo rum.',
        'title': 'Recover Fleas' },
    'c3r3r1r29.2voodooRumIngredientsB': {
        'description': 'Dread Scorpion stingers make the voodoo rum very potent and therefore, highly prized.',
        'title': 'Recover Stingers' },
    'c3r3r1r29.3voodooRumIngredientsB': {
        'description': 'No voodoo recipe would be complete without some ground up Undead teeth.',
        'title': 'Recover Teeth' },
    'c3r3r1r29.VoodooRumIngredientsB': {
        'description': 'Gather ingredients to make voodoo rum.',
        'items': 'Ingredients',
        'stringAfter': "Excellent! Here is your bottle.\x07Better try not to drop it on your way to Gunner if you don't want to find yourself cursed!",
        'title': 'Voodoo Rum Ingredients' },
    'c3r3r1r31r1.1visitJoshamee': {
        'description': 'Find Joshamee Gibbs in the Faithful Bride tavern.',
        'stringAfter': "A 25 year old rum is a rare find in these parts. Pirates aren't blessed with a good deal of patience.\x07It takes a bit of luck to find yourself a 25 year old...\x07But there is one gent who \x01slant\x01might\x02 help... \x01slant\x01Gerard\x02. The good news is... he's dead.\x07They say he was keepin' a bottle of 25 year for a special occasion...\x07I suppose that occasion came and went, ey!\x07Find Gerard and ye will find yer rum...\x07I'd start by asking \x01slant\x01Benedek\x02 here. He knew the man.",
        'title': 'Visit Joshamee Gibbs' },
    'c3r3r1r31r1.2visitBenedek': {
        'description': 'Ask Karbay Benedek about Gerard.',
        'stringAfter': "Gerard owed me \x01slant\x01not a little\x02 bit of money. But he died in a nasty place...\x07... so I haven't bothered to recover any of it... if there \x01slant\x01is\x02 anything to recover!\x07You bring me the gold and keep whatever else you find...",
        'title': 'Talk To Benedek' },
    'c3r3r1r31r1.3recoverEffects': {
        'description': "Dig up Gerard's hidden stash and return it to Benedek (keeping the rum for yourself). Gerard may have hid it behind a house in Tortuga.",
        'stringAfter': "These coins are worthless! Are you sure there wasn't anything else of value in the stash?\x07Don't lie, scoundrel!\x07Alright, you can go, but you've earned my... \x01slant\x01interest\x02...",
        'title': "Recover Gerard's Stash" },
    'c3r3r1r31r1Joshamee': {
        'description': 'Ask Joshamee Gibbs about how to acquire a bottle of 25 year rum.',
        'stringAfter': "These coins are worthless! Are you sure there wasn't anything else of value in the stash?\x07Don't lie, scoundrel!\x07Alright, you can go, but you've earned my... \x01slant\x01interest\x02...",
        'title': 'Joshamee Gibbs' },
    'c3r3r1r31r2.1fernandoChores': {
        'description': 'Fernando has a vendetta with the Navy so sink them - for pirate honor!',
        'title': 'Sink Navy Ships' },
    'c3r3r1r31r2.1visitFernando': {
        'description': 'Go see Fernando about a bottle of 25 year old rum.',
        'stringAfter': "25 year old rum? I've got none \x01slant\x01for sale\x02...\x07'Course, I might have a bottle laying around... for \x01slant\x01barter\x02.\x07I take it you have nothing of real value... \x07so perhaps I can offer a trade of said \x01slant\x01good\x02...\x07...for certain \x01slant\x01services\x02 that I shall enumerate...?\x07Right then. Here's a rather \x01slant\x01long\x02 list of chores! Fair winds, mate!",
        'title': 'Talk To Fernando' },
    'c3r3r1r31r2.2fernandoChores': {
        'description': "The EITC once imprisoned Fernando for smuggling some weapons into the islands and it's time for his revenge.",
        'title': 'Sink EITC Ships' },
    'c3r3r1r31r2.3fernandoChores': {
        'description': 'Like all good pirates and smugglers, they despise the Skeleton armies and their ships and want them all sunk.',
        'title': 'Sink Undead Ships' },
    'c3r3r1r31r2.FernandoChores': {
        'description': 'Do chores for Fernando in exchange for 25 year old rum.',
        'items': 'Chores',
        'stringAfter': '',
        'title': "Fernando's Chores" },
    'c3r3r1r31r2Fernando': {
        'description': 'Fernando is the person to go to when it comes to a 25 year old rum.',
        'title': 'Fernando De La Vega' },
    'c3r3r1r31r2r2.1sinkNavyShips': {
        'description': 'Sink Navy ships for Fernando.',
        'stringBefore': "Navy's always giving me trouble.",
        'title': 'Sink Navy Ships' },
    'c3r3r1r31r2r2.2sinkEITCShips': {
        'description': 'Sink EITC ships for Fernando.',
        'stringBefore': 'I resent competition from other parties, the East India Trading Company in particular.',
        'title': 'Sink EITC Ships' },
    'c3r3r1r31r2r2.3sinkSkeletonShips': {
        'description': 'Sink Skeleton ships for Fernando.',
        'stringBefore': 'Those skeleton ships are a menace! Not at all good for business.',
        'title': 'Sink Skeleton Ships' },
    'c3r3r1r31r2r2.4smuggleRum': {
        'description': 'Smuggle rum into Port Royal for Fernando.',
        'stringBefore': 'I have a shipment of rum bound for Port Royal.',
        'title': 'Smuggle Rum' },
    'c3r3r1r31r2r2.5smuggleHoney': {
        'description': 'Smuggle honey into Port Royal for Fernando.',
        'stringBefore': "I don't limit myself to rum these days.",
        'title': 'Smuggle Honey' },
    'c3r3r1r31r2r2.6smuggleCinnamon': {
        'description': 'Smuggle cinammon into Port Royal for Fernando.',
        'stringBefore': 'Black market cinnamon sells well to those Navy chaps.',
        'title': 'Smuggle Cinnamon' },
    'c3r3r1r31r2r2chores': {
        'description': 'Do chores for Fernando in exchange for 25 year old rum.',
        'items': 'Chores',
        'stringAfter': "Not bad, for a bloke like you. Got a few more and we'll be square.",
        'title': "Fernando's Chores" },
    'c3r3r1r31r2r2chores2': {
        'description': 'Do chores for Fernando in exchange for 25 year old rum.',
        'items': 'Chores',
        'stringAfter': 'Okay, mate. You can have your rum.',
        'title': "Fernando's Chores" },
    'c3r3r1r31twentyFiveRum': {
        'description': "Replace Duchamps' bottle of 25 year old rum.",
        'items': 'Sources',
        'stringAfter': "Not bad, for a bloke like you. Here's yer 25 year old rum.\x07Don't taste it or ye'll never want the cheap stuff again!",
        'title': '25 Year Old Rum' },
    'c3r3r1r6.1duchampsCompetition': {
        'description': "Sink Navy ships on Duchamps' behalf and earn his favor.",
        'title': 'Sink Navy Ships' },
    'c3r3r1r6.2duchampsCompetition': {
        'description': "Sink EITC ships on Duchamps' behalf and earn his trust.",
        'title': 'Sink EITC Ships' },
    'c3r3r1r6.DuchampsCompetition': {
        'description': 'Sink Navy and EITC cargo ships to clear the trade route for Duchamps.',
        'stringAfter': 'Not bad... for a scab like you!\x07Gunner is in hiding... on this very island.',
        'title': 'Eliminate Competition' },
    'c3r3r2.10maroonBiggleton': {
        'description': 'Maroon Captain Biggleton to compel him to talk about Scary Mary.',
        'title': 'Maroon Biggleton' },
    'c3r3r2.11captureNorman': {
        'description': 'Capture Captain Norman at sea on his Navy ship.',
        'title': 'Capture Norman' },
    'c3r3r2.12maroonNorman': {
        'description': 'Maroon Captain Norman to compel him to talk about Scary Mary.',
        'title': 'Maroon Norman' },
    'c3r3r2.13captureFitzpatrick': {
        'description': 'Capture Captain Fitzpatrick at sea on his East India Trading Company ship.',
        'title': 'Capture Fitzpatrick' },
    'c3r3r2.14maroonFitzpatrick': {
        'description': 'Maroon Captain Fitzpatrick to compel him to talk about Scary Mary.',
        'title': 'Maroon Fitzpatrick' },
    'c3r3r2.15captureHamilton': {
        'description': 'Capture Captain Hamilton at sea on his East India Trading Company ship.',
        'title': 'Capture Hamilton' },
    'c3r3r2.16maroonHamilton': {
        'description': 'Maroon Captain Hamilton to compel him to talk about Scary Mary.',
        'title': 'Maroon Hamilton' },
    'c3r3r2.17visitJohn': {
        'description': 'Go ask Bronze John on Driftwood Island about Scary Mary.',
        'stringAfter': "Scary Mary! I'd rather drink bilge water than sail with her again!\x07Aye, I loaned her a ship, too. She was gonna do some rumrunnin' for me.\x07Only I didn't count on her crew castin' her off me ship and keepin' the rum for themselves!\x07Get me my rum back, and I'll help you find Mary.",
        'title': 'Visit Bronze John' },
    'c3r3r2.18recoverRum': {
        'description': 'Steal rum for Bronze John to replace his losses.',
        'stringAfter': "Scary Mary, eh? She's made grown men shiver in fear. I know. I be one. Still wanna find her?\x07I hear she was marooned in an out-of-the-way place called, Isla Perdida.",
        'title': 'Recover Rum' },
    'c3r3r2.19visitMary': {
        'description': 'Find Scary Mary on Isla Perdida.',
        'stringAfter': "Who told ye I was here?!!\x07Was it that daft fool, Woodruff?!!! He always despised me!!! Achhhh!\x07What's that? Join Sparrow's crew, you say? Achhhh!\x07I'll not join another crew 'til I gets me revenge! Eccchh!\x07'Course ye could do it for me... that way they won't see it comin'!\x07Here's me list of those devils who'll feel the wrath of Scary Mary's vengeance!!!",
        'title': 'Find Scary Mary' },
    'c3r3r2.1visitFabiola': {
        'description': 'Ask Fabiola where to look for Scary Mary.',
        'stringAfter': "Aye, I know of her.\x07Turned straight, she did. Mary signed on with the Navy... that didn't end so well.\x07Then she sailed with the East India Trading Company as a deck-hand... ended even worse.\x07I hear she was captured by skeletons, but even they couldn't deal with her!\x07She had to get her own ship 'cause no one else would take her on.\x07As you might expect Mary's sint as a captain ended badly, in mutiny and maroonin'...\x07... and no one's seen her since.\x07\x01slant\x01Orinda\x02 might know more. She was the last one in Tortuga to speak with Mary.",
        'title': 'Visit Fabiola' },
    'c3r3r2.20.5recoverBelongings': {
        'description': 'Before Mary will leave Perdida you must dig up her belongings that she buried in the Perdida jungle.',
        'stringAfter': "Okay, mate! Ye can tell Captain Jack he'll have ole Mary Lash aboard as soon as...\x07Ye recover a couple of things taken from me by those horrid wasps! Achhhh!!!",
        'title': 'Recover Belongings' },
    'c3r3r2.21visitJoshamee': {
        'description': 'Tell Joshamee Gibbs that Scary Mary is ready to join the crew.',
        'title': 'Return To Joshamee' },
    'c3r3r2.22captureDennison': {
        'description': "Captain Dennison was once Mary's sweetheart - and even she can't stand to harm him but marooning him should teach him a lesson.",
        'title': 'Capture Dennison' },
    'c3r3r2.23maroonDennison': {
        'description': 'Make the wretch Captain Dennison suffer for leaving Mary for another woman!',
        'stringAfter': "That should teach that scumbag a lesson!\x07Now, before I leave, I be needin' me personal belongings. I buried them in the jungle, so bring them for me.",
        'title': 'Maroon Dennison' },
    'c3r3r2.2visitOrinda': {
        'description': 'Ask Orinda Le Jeune down at the Tortuga docks if she knows where to find Scary Mary.',
        'stringAfter': "Aye, I know the wretched lass.\x07Some say Mary's so scary she'd make a kraken squirt ink!\x07Disguised herself as a man and sailed with the Navy on 7 voyages...\x07...and each Captain got rid of her first chance they had!\x07I only know of one of them - a scallywag named Reginald.\x07But you'll have to maroon the man to get him to tell you her whereabouts. He too fears her.",
        'title': 'Visit Orinda' },
    'c3r3r2.3captureReginald': {
        'description': "Capture Captain Reginald at sea on his Navy ship and shake loose his memory of Scary Mary's location.",
        'title': 'Capture Reginald' },
    'c3r3r2.4maroonReginald': {
        'description': 'Maroon Captain Reginald to compel him to talk about Scary Mary.',
        'title': 'Maroon Reginald' },
    'c3r3r2.5captureDennison': {
        'description': 'Capture Captain Dennison at sea on his Navy ship.',
        'title': 'Capture Dennison' },
    'c3r3r2.5visitWoodruff': {
        'description': 'Captain Reginald sends you to see Woodruff for more information on the whereabouts of Scary Mary.',
        'stringAfter': "Aye, I knew Mary 'fore she was scary. But, she marooned me and some other blokes on this wretched island.\x07They got eaten by the giant crabs. I somehow survived.\x07Before I give you the information you seek, first you must do me some \x01slant\x01favors\x02, savvy?",
        'title': 'Visit Woodruff' },
    'c3r3r2.6maroonDennison': {
        'description': 'Maroon Captain Dennison to compel him to talk about Scary Mary.',
        'title': 'Maroon Dennison' },
    'c3r3r2.7captureHedley': {
        'description': 'Capture Captain Hedley at sea on his Navy ship.',
        'title': 'Capture Hedley' },
    'c3r3r2.7woodruffsRequest': {
        'description': "Ole Woodruff gets thirsty for rum stranded on this island. Get him some and then perhaps he'll talk.",
        'stringAfter': "Ahhhh! That's some fine rum, I'd say.\x07You'll find Scary Mary on a scrappy island called, \x01slant\x01Isla Perdida\x02.\x07But when you see her, don't mention me name, ey?",
        'title': 'Woodruffs Rum' },
    'c3r3r2.8maroonHedley': {
        'description': 'Maroon Captain Hedley to compel him to talk about Scary Mary.',
        'title': 'Maroon Hedley' },
    'c3r3r2.9captureBiggleton': {
        'description': 'Capture Captain Biggleton at sea on his Navy ship.',
        'title': 'Capture Biggleton' },
    'c3r3r2Mary': {
        'description': "Find 'Scary' Mary Lash and get her to join the crew.",
        'stringAfter': "Can't say I'm glad you found Scary Mary me-self, but that was a good bit of piratin' to bring her in.\x07Now \x01slant\x01Giladoga\x02, our next prospect, hasn't been seen around here for a while. \x07Carver was friendly with Giladoga once so you might ask him.",
        'title': 'Black Pearl Recruit: Mary Lash' },
    'c3r3r2r20.1sinkNavy': {
        'description': 'Sink Navy ships for Scary Mary.',
        'stringAfter': "Good! They had it coming to 'em.",
        'stringBefore': 'I hate the Navy! Should never have signed up with those mongrels!',
        'title': 'Revenge Against The Navy' },
    'c3r3r2r20.1waspIssues': {
        'description': 'The Terror Wasps have terrorized Mary from the first day she arrived. Defeat them and give no quarter!',
        'title': 'Defeat Terror Wasps' },
    'c3r3r2r20.2sinkEITC': {
        'description': 'Sink East India Trading Company ships for Scary Mary.',
        'stringAfter': 'Good! Got what they deserved, they did.',
        'stringBefore': "The East India Trading Company!? Hate 'em worse than the stinkin' Navy!",
        'title': 'Revenge Against The EITC' },
    'c3r3r2r20.2waspIssues': {
        'description': 'The Soldier Wasps have joined ranks to try and drive Mary from the island - be as cruel to them as they were to her!',
        'title': 'Defeat Soldier Wasps' },
    'c3r3r2r20.3sinkSkeleton': {
        'description': 'Sink skeleton ships for Scary Mary.',
        'stringAfter': 'Good! They got their just rewards.',
        'stringBefore': "Nasty skeletons! Don't know how to treat a lady!",
        'title': 'Revenge Against The Skeletons' },
    'c3r3r2r20.WaspIssues': {
        'description': "Mary's been stung hundreds of times by the wasps and she wants a punishing revenge on them without delay!",
        'stringAfter': "That'll show those vermin that Mary is \x01slant\x01not to be trifled with!!\x02\x07Now let's start my quest for vengeance on...\x07Humans!!!",
        'title': 'Wasp Problem' },
    'c3r3r2r20revenge': {
        'description': 'Help Scary Mary get revenge.',
        'items': 'Tasks',
        'stringAfter': "Sent 'em all to the bottom, did ye?! Ecchhh!\x07Thanks, but I can't leave without me belongings...\x07... buried 'em in this wasp infested jungle, I did!\x07Dig 'em up, and I'd be glad to leave this pergatory! Acchhh!",
        'title': "Mary's Revenge" },
    'c3r3r2r21.1maryRevenge': {
        'description': 'Sink ships of the Captains that marooned her for disobeying orders - she thought the orders were stupid.',
        'title': 'Sink Kingfishers' },
    'c3r3r2r21.2maryRevenge': {
        'description': "Mary's old shipmates jumped to the EITC after their Navy stint was up and they now sail on the Marauder class ships.",
        'title': 'Sink Marauders' },
    'c3r3r2r21.3maryRevenge': {
        'description': "Three of Scary Mary's tormentors are now Undead and Captain the Revenant class skeleton ships.",
        'title': 'Sink Revenants' },
    'c3r3r2r21.MaryRevenge': {
        'description': "Scary Mary needs you to hunt down all the ship Captains who dismissed or insulted her before she'll join Jack's crew.",
        'stringAfter': "Sent 'em all to the bottom, did ye?! Ecchhh!\x07I thanks ye from the bottom of me black heart!\x07Only one more wretched fool to pay back and I can leave this purgatory! Acchhh!\x07Name's Captain Dennison, sails a Barracuda - fittin' for that scab!",
        'title': "Mary's Revenge" },
    'c3r3r2r24.1missingTreasure': {
        'description': "The Hive Queen awarded gold medallions to her troops that she'd taken from Mary in a fierce battle.",
        'title': 'Recover Medallions' },
    'c3r3r2r24.2missingTreasure': {
        'description': "The Hive Queen's most prized human possesion is a gold chain she found on the beach after a shipwreck - and now Mary wants it for her own.",
        'title': 'Recover Chain' },
    'c3r3r2r24.MissingTreasure': {
        'description': 'Mary had some of her treasure stolen by the wasps, and something that she lusts after that belongs to the killer queen on the nest... The Hive Queen.',
        'stringAfter': "The chain, it's finally mine - and all me lovely things! Precious lovely things! Achhhh!!!\x07Tell Sparrow and Mr. Gibbs I be ready to join up!!",
        'title': 'Missing Treasure' },
    'c3r3r2r6.1woodruffsRequest': {
        'description': 'The vicious Devourer Crabs have tried to have Woodruff for lunch lately and you must send them a strong message!',
        'title': 'Defeat Crabs' },
    'c3r3r2r6.2woodruffsRequest': {
        'description': 'Croquette De Crabe is the leader of all crabs on the island, killing him would send a strong message.',
        'title': 'Defeat Croquettes De Crabe' },
    'c3r3r2r6.WoodruffsRequest': {
        'description': "Do Woodruff some housecleaning favors before he'll tell you Mary's whereabouts.",
        'stringAfter': 'Aye, many thanks. And these be mighty tasty.\x07Care for some? No?\x07Just as well, more for me. Now all I need is some rum...\x07...if you want to find Mary, that is.',
        'title': "Woodruff's Favors" },
    'c3r3r3.10recoverChest': {
        'description': 'Sink skeleton ships to recover the haunted chest with a key.',
        'title': 'Recover Haunted Chest' },
    'c3r3r3.11deliverChest': {
        'description': "The key's inside a haunted sea chest and he'll just use some of the left over potion!",
        'stringAfter': "It may be a vexed chest but, I still has some of Romany Bev's potion and...\x07Thar she blows! Well done. But...\x07IT'S NOT IT!\x07Curses... now, only one left that I know about, may be \x01slant\x01the key\x02.",
        'title': 'Deliver Haunted Chest' },
    'c3r3r3.11deliverToRomany': {
        'description': "The letter of forgiveness must be read, and burned to restore Romany Bev's full powers.",
        'stringAfter': 'Ahh, the letter. Now I can get back me powers...\x07...and break the curse on this key for me old friend, Giladoga.\x07Return to him with the key and, some extra potion in case he needs it later.',
        'title': 'Deliver Letter' },
    'c3r3r3.11visitJack': {
        'description': 'Find Jack in the Faithful Bride tavern and ask him for the final key.',
        'stringAfter': "Giladoga? Always on the lookout for \x01slant\x01something\x02, that one.\x07Which key, mate? Knowing \x01slant\x01which\x02 key is the key to the key, savvy?\x07For the record - there's a mutt 'round here you'd \x01slant\x01think\x02 could help you, but trust me... won't never happen.\x07Ah... William Parker you say? Always thought W.P. stood for \x01slant\x01wicked pirate\x02... or maybe something \x01slant\x01French\x02...\x07Hmmmm... it so happens that I was recently in possession of a key like the one you describe.\x07Thing is... I use it to scratch me back... hard to find a key like that. It gets that place you can never quite reach. \x07\x01slant\x01Very\x02 valuable, savvy? But... if you replace \x01slant\x01my\x02 key, I'll \x01slant\x01find\x02 yours...",
        'title': 'Visit Jack' },
    'c3r3r3.12recoverKey': {
        'description': 'Sink Skeleton frigates to find a replacement key for Jack.',
        'stringAfter': "Here you go... we're square.\x07Took well over an hour to unweave this key from my chest hair... near resorted to voodoo... consider that, mate!\x07Off you go... we're losing time. Much to plunder and little crew to show for it...",
        'title': "Replace Jack's Key" },
    'c3r3r3.13deliverKey': {
        'description': 'Take the last key to Giladoga.',
        'stringAfter': "That's the last key! We're there, mate!\x07Parker's treasure... it's been so many years!\x07I owe you me life!\x07Tell Joshamee I'll be seein' 'im in a fortnight!",
        'title': 'Deliver Key' },
    'c3r3r3.14visitJoshamee': {
        'description': 'Tell Joshamee Gibbs that Giladoga is ready to go.',
        'title': 'Return To Gibbs' },
    'c3r3r3.1visitCarver': {
        'description': 'Ask Carver about Giladoga.',
        'stringAfter': "...his \x01slant\x01real\x02 name's Gil Derga. But Captain Jack calls him...\x07\x01slant\x01Giladoga\x02 'cause he was so full of grog one night, he couldn't pronounce it!\x07Giladoga is an odd bird, he is. Obsessed with the memory of an old sea-dog William Parker.\x07But truth be told, he's obsessed with finding his resting place and...\x07...treasure! Some Navy Captain is rumored to have a map to the ole pirate's grave.\x07Last I heard Giladoga's over on Padres. Fancies the grog in a tavern called, Ratskellar.",
        'title': 'Visit Carver' },
    'c3r3r3.2visitMcVane': {
        'description': 'Ask Johnny McVane about Giladoga.',
        'stringAfter': "Giladoga? Open yer eyes, mate.  He's right behind ye!",
        'title': 'Visit McVane' },
    'c3r3r3.3visitGiladoga': {
        'description': 'Try and convince Giladoga to join the crew.',
        'stringAfter': "What scurvy dog put you up to this?\x07Gibbs eh!? I'm not going \x01slant\x01anywhere\x02 without William Parker's treasure, savvy?\x07He be the greatest pirate \x01slant\x01ever\x02.\x07Lead a brilliant raid on Cadiz, Spain and carried off a King's fortune!\x07Some say he lived it up in Singapore but I say he died with his treasure... somewhere in these islands.\x07I have a chest, rumored to be, \x01slant\x01Parker's\x02 own. And I have a key... should work, but doesn't. Find out why.",
        'title': 'Visit Giladoga' },
    'c3r3r3.4deliverKey': {
        'description': "Take Giladoga's key to Blacksmith Flinty to see if he has any leads.",
        'stringAfter': "Does this look like a charity I'm running here?",
        'title': 'Take Key To Blacksmith' },
    'c3r3r3.4keyDelivery': {
        'description': "Take Giladoga's key to Romany to see if she thinks it's \x01slant\x01the key\x02.",
        'stringAfter': "Aye, this key won't open anything because...\x07...this key 'tis cursed. You'll need to tease the \x01slant\x01fire\x02 out of the key so it might return to its proper form...\x07... only then will the curse be lifted. To do so... ye must wash it in different types of water...",
        'title': 'Take Key To Romany Bev' },
    'c3r3r3.5bribeFlinty': {
        'description': "Bribe Blacksmith Flinty for information about Giladoga's key.",
        'stringAfter': "Aye, I'll look at yer key. Spanish style it is...\x07Never come across this metal before, though. Highly unusual which usually means it's cursed!\x07Get it out of me sight 'fore this cursed thing ruins me good luck at the tables!\x07Take it to someone experienced in the dark arts - like that gypsy \x01slant\x01Fabiola\x02.",
        'title': 'Bribe The Blacksmith' },
    'c3r3r3.5romanysRequestA': {
        'description': 'Water from a sinking Revenant ghost ship holds some powerful voodoo magic.',
        'stringAfter': "Aye, this water is just what we need... to start.\x07I'd tell you but me memory wanes from time to time so,...\x07Here be a list of other waters to \x01slant\x01wash\x02 away the curse.",
        'title': 'Revenant Water' },
    'c3r3r3.6deliverKey': {
        'description': "Take Giladoga's key to Fabiola to see if she has any leads.",
        'stringAfter': "Aye 'tis cursed. Best be careful with a key such as this...\x07You'll need to tease the \x01slant\x01fire\x02 out of the key so it might return to its proper form...\x07...only then will the curse be lifted.\x07To do so... ye must wash it in different types of water...",
        'title': 'Take Key To Fabiola' },
    'c3r3r3.7romanysRequestC': {
        'description': 'Romany Bev needs brass from the nautical instruments found on the Monarch ships.',
        'stringAfter': "Yes, these will do fine.\x07The curse will be broken...\x07...soon. So while you wait, I owe a favor to Fernando the tavern keeper.\x07Get him to \x01slant\x01forgive\x02 my heartless act and restore me powers.\x07Then I'll return to you Giladoga's \x01slant\x01clean\x02 key.",
        'title': 'Acquire Navy Brass' },
    'c3r3r3.8deliverKey': {
        'description': 'Take the repaired key back to Giladoga.',
        'stringAfter': "Fine work mate but...\x07It doesn't work. Parker must 'ave dropped other keys in bottles...\x07...and threw them into the sea.\x07If I'm right, the current probably swept 'em all over the Caribbean!",
        'title': 'Deliver Key To Giladoga' },
    'c3r3r3.8visitFernando': {
        'description': 'Fernando had his heart broken by Romany Bev and must be persuaded to forgive her or her voodoo powers will be weak.',
        'stringAfter': "She says \x01slant\x01hello\x02? Well ain't that fine!\x07Listen mate, I am still angry with her but will forgive her if...\x07Ye do me a few \x01slant\x01favors\x02, ey?",
        'title': 'Visit Fernando' },
    'c3r3r3.9winAtPoker': {
        'description': 'Fernando lost much of his earnings to poker cheats and you must replace it.',
        'stringAfter': "You're a fine one with the cards.\x07Are you sure you didn't cheat?\x07I despise cheats! Anyway, here's a few more things I needs help with...",
        'title': 'Win Poker' },
    'c3r3r3Giladoga': {
        'description': 'Recruit Giladoga to join the crew.',
        'stringAfter': "William Parker, eh? Sounds like gettin' Giladoga was quite an adventure.\x07Next name's \x01slant\x01John Smith\x02.\x07Ol' Smith got himself into a \x01slant\x01situation\x02 with Andrew Bowdash. Ask Smith why he and Bowdash are at odds.",
        'title': 'Black Pearl Recruit: Giladoga' },
    'c3r3r3r10.1fernandosRequest': {
        'description': 'Fernando was exploring in the Catacombs and was attacked by some Grenadiers and he wants vengeance!',
        'title': 'Defeat Undead Grenadiers' },
    'c3r3r3r10.2fernandosRequest': {
        'description': 'The Undead Gypsies put a curse on Fernando that made him unlucky at cards - and love - defeat them to break the curse.',
        'title': 'Defeat Undead Gypsies' },
    'c3r3r3r10.3fernandosRequest': {
        'description': "The Slashers slashed and killed Fernando's favorite pet turtle - and Fernando wants you to repay their evil deed.",
        'title': 'Defeat Undead Slashers' },
    'c3r3r3r10.FernandosRequest': {
        'description': 'Help Fernando forgive Romany Bev so her voodoo powers will be restored to their fullness.',
        'stringAfter': 'Many thanks, my friend. The Undead are a menace to us all.\x07Take this letter to Romany. It says I forgive her, so she can get on with her life...\x07...and her voodoo magic.',
        'title': 'Help Fernando' },
    'c3r3r3r12.1lastKey': {
        'description': 'To find the key you must first defeat the gypsies to decrease the voodoo powers surrounding its guardian.',
        'title': 'Defeat Gypsies' },
    'c3r3r3r12.2lastKey': {
        'description': 'The Undead Executioners guard the keeper of \x01slant\x01the final key\x02, and you must defeat them to acquire it!',
        'title': 'Defeat Executioners' },
    'c3r3r3r12.3lastKey': {
        'description': "The Undead Boss Bonerattler keeps the key on his boney body, but don't try it alone, he's powerful!",
        'title': 'Defeat Bonerattler' },
    'c3r3r3r12.LastKey': {
        'description': "The last key is also in the possession of Jolly Roger's Undead minions, inside the dreaded, \x01slant\x01Catacombs\x02.",
        'stringAfter': "The last key!!!\x07It works!\x07But there be nothin' inside except...\x07SAND! It's bloody empty! William Parker's chest is EMPTY!!!\x07Tell Joshamee I'll be along directly...\x07Soon as I finish me mourning.",
        'title': 'The Last Key' },
    'c3r3r3r6.1romanysRequestB': {
        'description': "To break the key's curse, Romany Bev must have waters from those who touched it - in this case Navy Officers.",
        'title': 'Navy Water' },
    'c3r3r3r6.2romanysRequestB': {
        'description': 'Waters from the stomach of Huge Alligators are essential in the curse washing process',
        'title': 'Gator Water' },
    'c3r3r3r6.3romanysRequestB': {
        'description': 'The water in the Rancid Fly Trap helps wash the curse with its putrid, acidic qualities.',
        'title': 'Fly Trap Water' },
    'c3r3r3r6.RomanysRequestB': {
        'description': "Different waters from different sources are required to break the curse placed on Giladoga's key.",
        'stringAfter': 'Fine waters, they are, but...\x07I need one more thing. Brass found on Navy ships.\x07The brass settles the waters and calms the spirits.\x07Now go, we be almost done with breaking this curse.',
        'title': 'Waters for Romany' },
    'c3r3r3r7.4recoverWater': {
        'description': 'Kill terror wasps to recover terror wasp water.',
        'stringAfter': 'Thanks.  A few stings to get this water was a welcome trade, ey?',
        'stringBefore': 'Get us some wasp water... from terror wasps, mate!',
        'title': 'Recover Terror Wasp Water' },
    'c3r3r3r7r1.1visitOrinda': {
        'description': 'Ask Orinda where to find the proper type of skeleton ship for the water you need.',
        'stringAfter': 'Water from the lowest levels of a skeleton ship...?\x07Can something that thick and dark still be called water?\x07Come to think of it, I just heard rumors of just such a ship...',
        'title': 'Visit Orinda' },
    'c3r3r3r7r1.2recoverWater': {
        'description': 'Sink skeleton ships to recover water from the lowest deck.',
        'title': 'Recover Skeleton Water' },
    'c3r3r3r7r1.3deliverWater': {
        'description': 'Take the skeleton water to Fabiola.',
        'title': 'Deliver Skeleton Water' },
    'c3r3r3r7r1skeletonWater': {
        'description': 'Collect a jar of water from the lowest, darkest deck of a skeleton ship.',
        'stringAfter': 'Good work.',
        'stringBefore': "Go speak with \x01slant\x01Orinda\x02. She'll know where to find the proper ship for this water.",
        'title': 'Skeleton Ship Water' },
    'c3r3r3r7r2.1visitCarver': {
        'description': 'Ask Carver where to get Navy latrine water.',
        'stringAfter': "In my Navy days, we made the new recruits drink from the latrines...\x07... made men out of 'em, savvy? Navy recruits carry latrine water on 'em in their canteens.",
        'title': 'Visit Carver' },
    'c3r3r3r7r2.2recoverWater': {
        'description': 'Steal latrine water from Navy Cadets.',
        'title': 'Recover Navy Latrine Water' },
    'c3r3r3r7r2.3deliverWater': {
        'description': 'Take the latrine water to Fabiola.',
        'title': 'Deliver Latrine Water' },
    'c3r3r3r7r2latrineWater': {
        'description': 'Collect Navy latrine water.',
        'stringAfter': 'Good work.',
        'stringBefore': 'Go speak with \x01slant\x01Carver\x02. He was in the Navy and should know a thing or two about latrine water',
        'title': 'Navy Latrine Water' },
    'c3r3r3r7r3.1visitBenedek': {
        'description': 'Ask Karbay Benedek where to find shark water.',
        'stringAfter': "Most folks think ye need to find sharks to get shark water. Not true!\x07You can get shark water from other places... like crabs.\x07The crabs eat the sharks when they wash up on shore, so all ye need to do is kill crabs 'til ye find some!",
        'title': 'Visit Benedek' },
    'c3r3r3r7r3.2recoverWater': {
        'description': 'Kill giant crabs to recover shark water.',
        'title': 'Recover Shark Water' },
    'c3r3r3r7r3.3deliverWater': {
        'description': 'Take the shark water to Fabiola.',
        'title': 'Deliver Shark Water' },
    'c3r3r3r7r3sharkWater': {
        'description': "Collect water from a shark's belly.",
        'stringAfter': 'Good work.',
        'stringBefore': "Visit \x01slant\x01Karbay Benedek\x02. He'll know where to find shark-water I reckon.",
        'title': 'Shark Water' },
    'c3r3r3r7r5.1visitMallet': {
        'description': 'Ask Andros Mallet for crypt water.',
        'stringAfter': "I may have just the crypt for ye... it'll cost ye though!",
        'title': 'Visit Mallet' },
    'c3r3r3r7r5.2bribeMallet': {
        'description': 'Pay Mallet for some crypt water.',
        'stringAfter': "Alright, it's yours... the water of a scurvy pirate with 100 years of rot!",
        'title': 'Buy Crypt Water' },
    'c3r3r3r7r5.3deliverWater': {
        'description': 'Deliver the crypt water to Fabiola.',
        'title': 'Deliver Crypt Water' },
    'c3r3r3r7r5cryptWater': {
        'description': 'Collect water from a water-logged crypt.',
        'stringAfter': 'Good work.',
        'stringBefore': "Visit \x01slant\x01Mallet\x02 in the graveyard. He'll set ye up with crypt water.",
        'title': 'Crypt Water' },
    'c3r3r3r7r6.1visitScarlet': {
        'description': 'Ask Scarlet where to find honeysuckle.',
        'stringAfter': "There's honeysuckle all over Tortuga... at least there was...\x07'til those nasty wasps ate it all! There's plenty in their sap... and venom!",
        'title': 'Visit Scarlet' },
    'c3r3r3r7r6.2recoverHoneysuckle': {
        'description': 'Kill wasps to recover honeysuckle.',
        'title': 'Recover Honeysuckle' },
    'c3r3r3r7r6.3deliverHoneysuckle': {
        'description': 'Deliver the honeysuckle to Fabiola.',
        'title': 'Deliver Honeysuckle' },
    'c3r3r3r7r6honeysuckle': {
        'description': 'Collect honeysuckle.',
        'stringAfter': 'Sweet as sugar.',
        'stringBefore': "Visit \x01slant\x01Scarlet\x02. She'll know where to find honeysuckle.",
        'title': 'Honeysuckle' },
    'c3r3r3r7r7.1visitBowdash': {
        'description': 'Ask Andrew Bowdash for rubber tree sap.',
        'stringAfter': "Why are you bothering me!? Go win a hand or two at poker and I'll make it easy for you...",
        'title': 'Visit Bowdash' },
    'c3r3r3r7r7.2poker': {
        'description': 'Win at poker to impress Andrew Bowdash.',
        'stringAfter': "Here... I used to have a small orchard of rubber trees... until Jolly Roger cursed them!\x07Plenty of sap... but the natives aren't too friendly! HA!",
        'title': 'Win At Poker' },
    'c3r3r3r7r7.3recoverSap': {
        'description': 'Kill skeletons to recover sap from rubber trees.',
        'title': 'Recover Rubber Sap' },
    'c3r3r3r7r7.4deliverSap': {
        'description': 'Deliver the sap to Fabiola.',
        'title': 'Deliver Sap' },
    'c3r3r3r7r7rubber': {
        'description': 'Collect sap from a rubber tree.',
        'stringAfter': 'Well done!',
        'stringBefore': "Visit \x01slant\x01Bowdash\x02. He's the only bloke 'round these parts who might have rubber trees.",
        'title': 'Rubber Tree Sap' },
    'c3r3r3r7water': {
        'description': 'Gather jars of different types of water to cleanse the cursed key.',
        'items': 'Types',
        'stringAfter': 'Okay, we need a few more jars of water...',
        'title': 'Gather Water' },
    'c3r3r3r7water2': {
        'description': 'Gather jars of different types of water to cleanse the cursed key.',
        'items': 'Types',
        'stringAfter': 'Good work... be careful now with this key.',
        'title': 'Gather Water' },
    'c3r3r3r9keys': {
        'description': "Round up a host of potential \x01slant\x01Parker's Chest\x02 keys that are all over the Caribbean!",
        'items': 'Keys',
        'stringAfter': "BILGE RATS!!! This one doesn't work either!\x07Alas, I have some bad news...\x07I hear Jolly Roger's minions have the last two keys! Seems they was looking for Parker's chest as well...\x07I heard they keep 'em in one on of these haunted ships. Or was it in a haunted chest? Not sure...",
        'title': 'Round Up Keys' },
    'c3r3r3r9r1.1visitCraven': {
        'description': "Visit Bastien Craven on Rumrunner's Isle.",
        'stringAfter': "I have plenty of keys... but none like yours.\x07Wait, let me see that again. Aye! I found a key like that many years back...\x07Sold it to that devilin' rumrunner \x01slant\x01Flatts\x02. Best ask him.",
        'title': 'Visit Bastien Craven' },
    'c3r3r3r9r1.1visitGarrett': {
        'description': "Rumor has it that Garrett knows the whereabouts to one of William Parker's lost keys.",
        'stringAfter': 'Which key?\x07Ahh yes, I \x01slant\x01sorta\x02 remembers where that is...\x07And I can \x01slant\x01definitely\x02 remember... with yer help. Savvy?',
        'title': 'Visit Garrett' },
    'c3r3r3r9r1.2visitFlatts': {
        'description': 'Visit rumrunner Ben Flatts in Tortuga.',
        'stringAfter': "Aye, I've got yer key. But I expect a return on my investment...\x07I'll be makin' a run soon... do me a small favor and you can have the key. Deal?",
        'title': 'Visit Ben Flatts' },
    'c3r3r3r9r1.3sinkNavyShips': {
        'description': 'Sink Navy ships for Ben Flatts.',
        'stringAfter': 'Good work. You may be pirate material yet...\x07Now, take this shipment to Port Royal. Stay out of trouble on the way...\x07... and bring back me payment from \x01slant\x01Graham Marsh\x02.',
        'title': 'Sink Navy Ships' },
    'c3r3r3r9r1.4deliverRum': {
        'description': 'Deliver a shipment of rum to Graham Marsh in Port Royal.',
        'stringAfter': "Flatts, eh? Here's yer payment, mate.",
        'title': 'Deliver Rum' },
    'c3r3r3r9r1.5deliverMoney': {
        'description': 'Deliver payment to Ben Flatts in Tortuga.',
        'stringAfter': "You callin' me a liar? Well, I'm a pirate as much as you then, aren't I?\x07Suppose I did exaggerate a bit on the small favor... it wasn't so small!\x07Here, take your precious key. May you find a chest full of rot to put 'er in...",
        'title': 'Deliver Payment' },
    'c3r3r3r9r1.6deliverKey': {
        'description': "Take Garrett's key to Giladoga.",
        'title': 'Deliver Key' },
    'c3r3r3r9r1key': {
        'description': 'One strange looking key is said to be in the hands of a very forgetful smuggler named Garrett.',
        'stringAfter': "Good, good, let's try this key and...\x07Ahhhh! This is \x01slant\x01not\x02 the one! Keep trying, mate.",
        'title': 'Key #1' },
    'c3r3r3r9r1r2.1garrettsRequest': {
        'description': "Garrett needs these pesky Marauder ships sunk so he can continue his midnight runs that border on illegal - who are we kidding - he's a smuggler!",
        'title': 'Sink Marauders' },
    'c3r3r3r9r1r2.2garrettsRequest': {
        'description': 'Garrett once used bribes to get the EITC Barracuda Captains to look the other way but a new set of Captains are clamping down on smuggling.',
        'title': 'Sink Barracudas' },
    'c3r3r3r9r1r2.3garrettsRequest': {
        'description': 'The Man-O-War ships provide firepower for the smaller vessels and Garrett needs them out of the way to continue his illicit business.',
        'title': 'Sink Man-O-Wars' },
    'c3r3r3r9r1r2.GarrettsRequest': {
        'description': 'To jog his addled memory, you must help Garrett with a few, select tasks.',
        'stringAfter': "Fine work, mate. Now they are out of the way...\x07I can get back to smugglin'... er uh, I meant to say, importin' and exportin', ey.\x07Here be the key, as promised.",
        'title': 'Help Garrett Remember' },
    'c3r3r3r9r2.1visitMallet': {
        'description': 'Go see Andros Mallet in the Tortuga graveyard.',
        'stringAfter': "Are you accusing me? Think I make \x01slant\x01all\x02 my money by robbing graves?\x07Actually only \x01slant\x01most\x02 of me money...\x07So... yeah... I've dug up that scallywag Jenkins. Had some strange key around his neck...\x07.... only thing is... I gave that to \x01slant\x01Karbay Benedek\x02 to settle a debt I owed...",
        'title': 'Visit Andros Mallet' },
    'c3r3r3r9r2.1visitRico': {
        'description': "Rico's heard talk that someone on Padres knows of yet another of William Parker's keys.",
        'stringAfter': 'Aye, I do know, but it will cost ye.\x07Return to me with the sea chest from an Ogre class ship and...\x07I will tell ye.',
        'title': 'Visit Rico' },
    'c3r3r3r9r2.2ricosRequest': {
        'description': "Rico's mother and father had all their worldly possessions illegally taken from them by an EITC Ogre Captain.",
        'stringAfter': "That's the one. Many thanks! And now fer my end of the bargain...\x07Go see the gypsy Pelagia. She'll know more about \x01slant\x01the key\x02.",
        'title': 'Recover Chest' },
    'c3r3r3r9r2.2visitBenedek': {
        'description': 'Visit Karbay Benedek in the Faithful Bride tavern.',
        'stringAfter': "You want something from Karbay Benedek? Then remember this...\x07Nothing is free in this world... and anything from ol' Benedek will cost you dearly!\x07There's an East India Trading Company shipment that I want...\x07This ship carries a certain chest... that is most certainly filled with jewels.\x07Bring me the contents of that chest.",
        'title': 'Visit Karbay Benedek' },
    'c3r3r3r9r2.3recoverChest': {
        'description': 'Sink East India Trading Company ships to recover the chest Benedek wants.',
        'stringAfter': 'Listen, you slimy barnacle! I loaned some money to a certain voodoo priest...\x07... only he paid me back in gold that was cursed! Get rid of the curse...',
        'title': 'Recover Chest' },
    'c3r3r3r9r2.3visitPelagia': {
        'description': "If it's mystical, magical or good gossip, Pelagia knows about it - ask her.",
        'stringAfter': "I know of this key of which you speak.\x07What does it mean to you?\x07If what you say is true, I'll help you \x01slant\x01if\x02 ye will help me, ey?",
        'title': 'Visit Pelagia' },
    'c3r3r3r9r2.4deliverFabiola': {
        'description': "Go see Fabiola about undoing the curse on Benedek's gold.",
        'stringAfter': "I don't think I want to be in the business of helping people like Karbay Benedek...\x07... but I am in the business of my business... and my business is voodoo.\x07So let me \x01slant\x01do\x02 some \x01slant\x01voo\x02doo for you...",
        'title': 'Deliver Gold To Fabiola' },
    'c3r3r3r9r2.5deliverItem': {
        'description': "Pelagia wants you to deliver the rings and ask Rico about the next key to Parker's Treasure.",
        'stringAfter': "Pinky rings? From my love?!\x07They are sooo beautiful...\x07I want to weep tears of joy!\x07The key? Yes, I'll tell you what I know \x01slant\x01if\x02 you do a small job, or uh jobs for me.",
        'title': 'Deliver Rings' },
    'c3r3r3r9r2.6deliverGold': {
        'description': 'Take the gold back to Karbay Benedek.',
        'stringAfter': "Ok. Next thing, here's a map to a chest I buried.\x07Dig it up and bring me the bag of coins that's in it.\x07There's plenty of skeletons around... eliminate them, lest they see the spot...\x07Should any skeleton dig up me gold... X will mark the spot on \x01slant\x01your neck\x02, savvy?",
        'title': 'Return Gold To Benedek' },
    'c3r3r3r9r2.6recoverSome': {
        'description': "Rico's forgotten where he buried a small gem - it's not worth much but it's important to the sensitive bartender.",
        'stringAfter': "Ahhh, my gem...\x07Colored glass really but it was me prized possession when I was lad!\x07The key? Yes, uh...\x07I need yet another favor, mate before I tell you what I know.\x07Can't leave me post so, recover some money I lost, ey?",
        'title': 'Recover Gem' },
    'c3r3r3r9r2.7recoverCoins': {
        'description': "Benedek's gold is located in a buried chest near the gypsy in Tortuga.",
        'stringAfter': "You have to be a shark before you can be a loan shark...\x07There's a pirate who owes me money... and I want him to owe me more.\x07Go play 'im in cards until you win a bagful. Then he'll come crawlin'!",
        'title': "Dig Up Benedek's Chest" },
    'c3r3r3r9r2.7winAtBlackjack': {
        'description': 'Win back some gold Rico lost while playing cards earlier this week.',
        'stringAfter': "You are handy with the cards, thanks. Now, listen closely...\x07I have it on me person, I do.\x07Take it to Giladoga, and don't tarry or someone may steal it, savvy?",
        'title': 'Win Blackjack' },
    'c3r3r3r9r2.8blackjack': {
        'description': 'Win money in Blackjack to help Benedek drum up business.',
        'stringAfter': "If you worked any harder for this key... I'd start to want it myself.\x07Seeing as I'm not in the business of buried treasure... you'd best take it.\x07I guess you've earned your loathsome key...",
        'title': 'Win At Blackjack' },
    'c3r3r3r9r2.9deliverKey': {
        'description': 'Take the key to Giladoga.',
        'title': 'Deliver Key' },
    'c3r3r3r9r2key': {
        'description': 'Rico the pumped up bartender knows where to find yet another strange looking key.',
        'stringAfter': 'Fine work, mate... and insert the key and...\x07No! Drat. Sorry mate, back to the grind, ey?',
        'title': 'Key #2' },
    'c3r3r3r9r2r4.1pelagiasRequest': {
        'description': "The Undead kneecaps are vital to capping the potency of Pelagia's newest batch of health potion.",
        'title': 'Recover Kneecaps' },
    'c3r3r3r9r2r4.2pelagiasRequest': {
        'description': "A fungus found on Undead ribs have a rare mineral that's used in the tastiest potions and elixirs.",
        'title': 'Recover Ribs' },
    'c3r3r3r9r2r4.3pelagiasRequest': {
        'description': 'Defeat the Undead Executioners because Pelagia despises them and they sometimes wear pinky rings she needs as a gift.',
        'title': 'Recover Pinky Rings' },
    'c3r3r3r9r2r4.PelagiasRequest': {
        'description': 'Pelagia is brewing up a new potion and needs help gathering her materials.',
        'stringAfter': "Good, ye have gathered all my ingredients including...\x07...the pinky rings from those undead scum.\x07Take the rings to Rico, my new sweetheart.\x07He'll tell you the location of the key.",
        'title': "Pelagia's Request" },
    'c3r3r3r9r2r5.1recoverHair': {
        'description': 'Recover 5 terror wasp hairs.',
        'stringAfter': 'That will do.',
        'stringBefore': 'We need 5 terror wasp hairs.',
        'title': 'Terror Wasp Hair' },
    'c3r3r3r9r2r5.2recoverTears': {
        'description': 'Recover 3 huge alligator tears.',
        'stringAfter': "Careful you don't spill them.",
        'stringBefore': "We need 3 tears from a huge alligator. They'll not give them up without a fight.",
        'title': 'Huge Alligator Tears' },
    'c3r3r3r9r2r5.3recoverBlood': {
        'description': 'Recover the blood of a dread scorpion.',
        'stringAfter': 'That will do.',
        'stringBefore': 'Bring me the blood of a dread scorpion.',
        'title': 'Dread Scorpion Blood' },
    'c3r3r3r9r2r5.4recoverGuano': {
        'description': 'Recover vampire bat guano.',
        'stringAfter': 'The guano really holds everything together.',
        'stringBefore': 'Vampire bat guano! Fantastic stuff!',
        'title': 'Vampire Bat Guano' },
    'c3r3r3r9r2r5ingredients': {
        'description': 'Gather voodoo ingredients for Fabiola.',
        'items': 'Ingredients',
        'stringAfter': "There you go, pirate! Now you're free to fritter your gold away!\x07... only, don't cross Benedek... he has a nasty temper!",
        'title': 'Voodoo Ingredients' },
    'c3r3r3r9r3.1visitBowdash': {
        'description': "Go ask Andrew Bowdash if he has one of Parker's keys.",
        'stringAfter': "Of course I have the key!\x07And of course you can't just have it! HA!\x07Tell you what you can have...\x07A decree from the king! A scurvy dog I bested in poker ran off without paying...\x07Maroon him! Take my money! That be the key to gettin' your key! HA!",
        'title': 'Visit Bowdash' },
    'c3r3r3r9r3.1visitDuchamps': {
        'description': "Go ask Duchamps if he has one of Parker's keys.",
        'stringAfter': "Of course I have the key!\x07And of course you can't just have it!\x07Tell you what you can have...\x07A small task - a scurvy Navy man I bested in poker ran off without paying me...\x07Maroon the scab and return my money! That be the key to gettin' your key - funny ey?!",
        'title': 'Visit Duchamps' },
    'c3r3r3r9r3.2capturePenrod': {
        'description': 'Sink Navy ships until you capture Penrod.',
        'title': 'Capture Penrod' },
    'c3r3r3r9r3.2capturePenrodNew': {
        'description': 'Captain Penrod conveniently forgot to pay Duchamps his gambling debt and you must recover it.',
        'title': 'Capture Penrod' },
    'c3r3r3r9r3.3maroonPenrod': {
        'description': "Maroon Penrod on Rumrunner's Isle and take his gold.",
        'title': 'Maroon Penrod' },
    'c3r3r3r9r3.3maroonPenrodNew': {
        'description': 'Penrod has an iron will and refuses to pay up unless you maroon him.',
        'title': 'Maroon Penrod' },
    'c3r3r3r9r3.4deliverGold': {
        'description': "Deliver Penrod's gold to Andrew Bowdash.",
        'stringAfter': "I don't remember saying the key'd be yours. A king without a key is a keyless king! HA!\x07Sink some of those Navy pigs and I'll think about it.\x07The first duty of the King is to keep Tortuga clear of their brand of brigand!",
        'title': 'Deliver Gold To Bowdash' },
    'c3r3r3r9r3.4deliverMoney': {
        'description': "Return Captain Penrod's debt to Duchamps.",
        'stringAfter': "Good but...\x07I don't remember saying the key'd be yours for only \x01slant\x01one\x02 favor.\x07Sink some of those rat infested Navy ships and I'll think about it.",
        'title': 'Deliver Money' },
    'c3r3r3r9r3.5sinkNavyShips': {
        'description': "Sink Navy ships for Bowdash's pleasure.",
        'stringAfter': "Okay okay, I \x01slant\x01promise\x02 if you do one more thing, the key is yours. Honor bright and all that! HA!\x07I'm hosting a card tournament that you're going to help me win. Do that, and the key is mine no longer. HA!",
        'title': 'Sink Navy Ships' },
    'c3r3r3r9r3.6poker': {
        'description': 'Win at poker for Bowdash.',
        'stringAfter': "Ha ha! Good show! They never suspected a thing!\x07On the other hand, pirates are a suspicious lot... so they probably \x01slant\x01did\x02 suspect...\x07... but they didn't \x01slant\x01suspect\x02 the right hand, did they? \x01slant\x01Your\x02 hand! HA!\x07Do you want a job? No? Just the key then. Take the stupid thing! HA!",
        'title': 'Win At Poker' },
    'c3r3r3r9r3.6winAtPoker': {
        'description': 'Win at poker for Duchamps.',
        'stringAfter': "Good show! They never suspected a thing!\x07Here's what I owe... one old, rusty key!\x07Heaven knows why you'd want it but, take it and be gone.",
        'title': 'Win At Poker' },
    'c3r3r3r9r3.7deliverKey': {
        'description': 'Bring Giladoga the key from Duchamps.',
        'title': 'Deliver Key to Giladoga' },
    'c3r3r3r9r3key': {
        'description': 'Recover the next key whose whereabouts is known to a rascal and smuggler named Duchamps.',
        'stringAfter': "It's so rusty but it may work...\x07No. Sorry. Onward to the next key that may be - how shall I say it?\x07Tricky? It's inside the sea chest of ole \x01slant\x01Black Sam\x02 Bellamy, and that's inside...\x07...the belly of a nasty Gator boss. Good luck... you'll be needin' it.",
        'title': 'Key #3' },
    'c3r3r3r9r3r5.1duchampsRequest': {
        'description': 'Duchamps wants the Navy off his back so you must sink them to clear up his smuggling routes.',
        'title': 'Sink Monarchs' },
    'c3r3r3r9r3r5.2duchampsRequest': {
        'description': 'Clear out the Man-O-War ships that cruise the coast looking for smugglers.',
        'title': 'Sink Man-O-Wars' },
    'c3r3r3r9r3r5.3duchampsRequest': {
        'description': "One Predator recently confiscated Duchamps' prized sloop and he wants revenge!",
        'title': 'Sink Predator' },
    'c3r3r3r9r3r5.DuchampsRequest': {
        'description': "Sink Navy ships to help Duchamp's business",
        'stringAfter': "Okay okay, I \x01slant\x01promise\x02 if you do one more thing, the key is yours. Honor bright and all that!\x07I'm hosting a card tournament that you're going to help me win. Do that, and the key is yours.",
        'title': 'Sink Navy Ships' },
    'c3r3r3r9r4.10deliverRum': {
        'description': 'Take Doc Grog his rum.',
        'stringAfter': 'Well done then... enjoy! I recommend you take those eggs with a hearty toast!',
        'title': 'Deliver Rum' },
    'c3r3r3r9r4.11deliverOil': {
        'description': 'Take the ingredients back to Fabiola.',
        'stringAfter': 'Ahhhh... Now all ye need is the breath of a woman frustrated in love...\x07That be me! Hehhhhhh...\x07There you go then... What? All that for just a key?',
        'title': 'Deliver Ingredients' },
    'c3r3r3r9r4.12deliverKey': {
        'description': 'Take the key to Giladoga.',
        'title': 'Deliver Key' },
    'c3r3r3r9r4.1recoverChest': {
        'description': "Fight fearsome alligators to recover Bellamy's chest.",
        'stringAfter': "This chest is encrusted with the Worm's Bay parasite.\x07Just imagine! A worm that lives inside a beast like that giant alligator!\x07If you have any chance of opening that chest... you'll need some special oils and salves...\x07Try \x01slant\x01Fabiola\x02... it's not voodoo but she'll know where to find them.",
        'title': "Recover Bellamy's Chest" },
    'c3r3r3r9r4.1recoverChestNew': {
        'description': "Dreadtooth is the bad gator boss who swallowed another gator who swallowed the famed pirate's chest... in one gulp!",
        'stringAfter': "I must say, I am impressed that a swabbie like you...\x07Bested a gator boss like that! Hope you didn't bleed... too much.\x07Now take the chest to Romany and get her to open it for us.",
        'title': "Recover Bellamy's Chest" },
    'c3r3r3r9r4.2deliverChest': {
        'description': 'Deliver the chest you recovered to Romany Bev to open it.',
        'stringAfter': "I be thinkin' everthing poor ole Giladoga touches is cursed!\x07Before I can break the curse, I need some items...\x07What were you expectin'? Somethin' easy?!\x07Now get goin' you snifflin' wretch!!",
        'title': 'Deliver Chest' },
    'c3r3r3r9r4.2visitFabiola': {
        'description': 'See if Fabiola knows how to open the encrusted chest.',
        'stringAfter': "I've only got one of the things you will need...\x07Here's a list of the others.",
        'title': 'Visit Fabiola' },
    'c3r3r3r9r4.4deliverList': {
        'description': "Take Fabiola's list to Doc Grog.",
        'stringAfter': "Pus from a festering wound! Grog dregs! Tortoise eggs? These things don't grow on trees, mate!\x07Fetch me a dram of 25-year-old rum from the Faithful Bride and I'll think it over...",
        'title': 'Deliver List To Grog' },
    'c3r3r3r9r4.5visitCarver': {
        'description': 'Go buy a dram of 25-year-old rum from Carver in the Faithful Bride tavern.',
        'stringAfter': "25-year-old? For the Doc? That'll cost ye.",
        'title': 'Buy Rum' },
    'c3r3r3r9r4.6bribeCarver': {
        'description': "Pay Carver for Grog's rum.",
        'stringAfter': "Here's yer rum, mate.",
        'title': 'Pay For Rum' },
    'c3r3r3r9r4.7deliverRum': {
        'description': 'Take Doc Grog his rum.',
        'stringAfter': "Alright, you can have the groggy yeast! Take it!\x07And here's a full jar of pus for ye! Don't ask!\x07As for the tortoise eggs... they're hard to part with, see?\x07Fetch me a \x01slant\x01bottle\x02 of this 25-year and I'll forgo me favored turtle-egg omelet!",
        'title': 'Deliver Rum' },
    'c3r3r3r9r4.8visitCarver': {
        'description': 'Go buy a bottle of 25-year-old rum from Carver in the Faithful Bride tavern.',
        'stringAfter': "An entire bottle? Let's see the money first, mate?",
        'title': 'Buy Rum Bottle' },
    'c3r3r3r9r4.9bribeCarver': {
        'description': "Pay Carver for Grog's rum.",
        'stringAfter': 'Hope the doc enjoys his rum. Here you go.',
        'title': 'Pay For Rum' },
    'c3r3r3r9r4key': {
        'description': 'Recover key from inside a chest that belonged to the infamous pirate, Black Sam Bellamy - a black hearted man who never gave quarter to his victims.',
        'stringAfter': "I'll wage that was a hard one to get, indeed, hope it's the one...\x07Sadly, it's not to be.\x07I had another key once and gave it to ole Morris for safekeeping now...\x07The toad can't remember where he put it! Too much grog addles the memory, ey?!\x07Find him a memory cure. Ask Pelagia.",
        'stringBefore': 'Did hear of another key...\x07In a chest carried by a pirate named Susan Bellamy. She was snapped in two by the jaws of a mighty giant alligator...',
        'title': 'Key #4' },
    'c3r3r3r9r4r3.1openChest': {
        'description': 'A group of Hired-Guns tried to open it with their daggers - bring Romany Bev their daggers to break the curse.',
        'title': 'Recover Daggers' },
    'c3r3r3r9r4r3.1recoverCologne': {
        'description': 'Recover perfume from defeated Navy guards.',
        'stringAfter': "Not the way I'd like to be smellin'.",
        'stringBefore': 'We need scented oil. Those dandy Navy Guards are drenched in the stuff!',
        'title': 'Perfume' },
    'c3r3r3r9r4r3.2openChest': {
        'description': "Navy officers fought over the famous pirate's chest and a man was killed, so Romany Bev needs their swords to break the curse.",
        'title': 'Recover Swords' },
    'c3r3r3r9r4r3.2recoverOil': {
        'description': 'Recover oil from terror wasps.',
        'stringAfter': 'Good! Good!',
        'stringBefore': 'Terror Wasp oil, to make it smooth.',
        'title': 'Terror Wasp Oil' },
    'c3r3r3r9r4r3.3openChest': {
        'description': 'Using their brass buttons as gambling chips the Mercenaries played cards to determine who got the chest. Romany Bev needs them to break the curse.',
        'title': 'Recover Buttons' },
    'c3r3r3r9r4r3.3recoverBile': {
        'description': 'Recover rock crab liver bile.',
        'stringAfter': 'Smelly stuff, that bile.',
        'stringBefore': 'Rock Crab liver bile will make it thick.',
        'title': 'Rock Crab Liver Bile' },
    'c3r3r3r9r4r3.OpenChest': {
        'description': 'The chest was cursed with a closing spell to keep unrighteous hands from opening it, so you must gather items from those who tried to crack it open.',
        'stringAfter': "Well done, pirate. Not only did ye get me the elements to break the curse...\x07the Caribbean is rid of some unrighteous vermin.\x07Here's the key. Take it to Giladoga.",
        'title': 'Opening The Cursed Chest' },
    'c3r3r3r9r4r3oils': {
        'description': 'Gather oils and salves to help open the encrusted chest.',
        'items': 'Oils',
        'stringAfter': "Now you'll need a few things from \x01slant\x01Doc Grog\x02. Take this list to him.",
        'title': 'Gather Oils And Salves' },
    'c3r3r3r9r5.1visitGrog': {
        'description': 'Go see Doc Grog about a memory cure.',
        'stringAfter': "You again?! Can't you see I'm busy? East India shipment just came in...\x07I'm allowed a bit of their special rum... for medicinal purposes.\x07Memory?... whose memory? Retavick? Ah... I remember now!\x07He's a difficult case... get me these things and you've got a chance of recovering it for 'im.",
        'title': 'Visit Doc Grog' },
    'c3r3r3r9r5.1visitPelagia': {
        'description': 'Go see Pelagia about a memory cure.',
        'stringAfter': "Begad, that Giladoga is taken up too much of me time!!\x07But alas, I'll do me best. Least I can do for saving me skin.\x07I need some ingredients to fix ole Morris' memory, Here be the list...",
        'title': 'Visit Pelagia' },
    'c3r3r3r9r5.3deliverMemoryCure': {
        'description': 'Give Morris the herbal memory cure and tell him to stop drinking so much grog!',
        'stringAfter': "Acckkk!!!\x07Why are you trying to poison me?\x07Ha, ha! Now I remember! Parker's key! Thanks, mate!\x07It was stolen from me by skeletons at sea!\x07Get it back from those devils and its yours.",
        'title': 'Deliver Memory Cure' },
    'c3r3r3r9r5.3deliverRemedy': {
        'description': 'Take the memory remedy to Retavick in the Faithful Bride tavern.',
        'stringAfter': "Why are you trying to poison me?\x07Ahhhh! Now I remember! Thanks, mate!\x07As for the key... I'd rather not recall but recall I do...\x07It was taken from me by skeletons at sea!\x07Get it back from those devils and its yours.",
        'title': 'Deliver Remedy' },
    'c3r3r3r9r5.4recoverKey': {
        'description': 'Sink a Storm Reaper Skeleton ship to get the key stolen from Morris.',
        'title': 'Recover Key' },
    'c3r3r3r9r5.5deliverKey': {
        'description': 'Take key to Giladoga.',
        'title': 'Deliver Key' },
    'c3r3r3r9r5key': {
        'description': 'Morris is said to know about the next key, however he is known to suffer from some momory issues.',
        'stringAfter': "Thanks but it's not \x01slant\x01the key\x02, either.\x07Don't lose heart mate. One will fit, I know this much 'tis true!\x07Visit Adoria Dolores. I heard she came upon one of the keys as well.",
        'title': 'Key #5' },
    'c3r3r3r9r5r2.1cureMemory': {
        'description': "This hay is for Navy Officers' horses and is imported from Ireland, perfect for Pelagia's natural memory cure.",
        'title': 'Recover Hay' },
    'c3r3r3r9r5r2.1recoverTeeth': {
        'description': 'Recover alligator teeth to be ground into powder.',
        'stringAfter': "Now we just grind 'em into powder.",
        'stringBefore': "We'll need gator teeth. Lots of 'em.",
        'title': 'Alligator Teeth' },
    'c3r3r3r9r5r2.2cureMemory': {
        'description': 'Every Officer carries a small medicine kit that contains some Flax Oil Seed for memory enhancement and good blood flow.',
        'title': 'Recover Kits' },
    'c3r3r3r9r5r2.2recoverVenom': {
        'description': 'Recover venom from a Dread Scorpion.',
        'stringAfter': "Venom to some... but add it to a pint of grog, and... well that's another story.",
        'stringBefore': 'I need you to collect the juice of a Dread Scorpion... a special venom they secrete...',
        'title': 'Dread Scorpion Venom' },
    'c3r3r3r9r5r2.3cureMemory': {
        'description': 'The EITC Mercenaries trained in China and learned many things like, the power of a herb called Ginseng to help their memories.',
        'title': 'Recover Herbs' },
    'c3r3r3r9r5r2.3recoverSap': {
        'description': 'Recover sap from a Flytrap.',
        'stringAfter': 'Well done! Well done!',
        'stringBefore': "Now fetch me the sap from a Flytrap...\x07... but be careful, as you might imagine, those devils don't like their sap taken.",
        'title': 'Flytrap Sap' },
    'c3r3r3r9r5r2.CureMemory': {
        'description': "Pelagia has a natural cure for Morri's temporary memory loss and needs help gathering the ingredients.",
        'stringAfter': 'Good, good, all the ingredients... mixed together and...\x07Wah-lah! A memory fix without any voodoo, just plants and herbs.\x07Take it to Morris and tell him to ease up on the grog, ey?',
        'title': 'Memory Cure' },
    'c3r3r3r9r5r2ingredients': {
        'description': "Gather ingredients for Doc Grog's memory cure.",
        'items': 'Ingredients',
        'stringAfter': "Take this. Your friend's memory will be as good as new.",
        'title': 'Memory Cure' },
    'c3r3r3r9r6.1adoriasRequest': {
        'description': "The worse of the Undead rabble, Adoria wants you to defeat the Executioners for her husbands's sake!",
        'title': 'Defeat Executioners' },
    'c3r3r3r9r6.1visitAdoria': {
        'description': 'Ask Adoria Dolores about her key.',
        'stringAfter': "Oh, my poor, dear husband, Javier! Snatched from this life by them undead scum!\x07Drive those skeletons back to the devil and I'll help find your key.",
        'title': 'Visit Adoria Dolores' },
    'c3r3r3r9r6.1visitAnne': {
        'description': 'Ask seamstress Anne about her key.',
        'stringAfter': "Oh, my poor, dear husband! He was a good man, right here in Tortuga if you can believe that!\x07Oh won't you drive those skeletons away from his grave? I fear for what they do there at night.\x07Do this and I'll help you.",
        'title': 'Visit Seamstress Anne' },
    'c3r3r3r9r6.2adoriasRequest': {
        'description': 'Some people say that the Gypsies put a curse on Javier before he was killed, now they must pay!',
        'title': 'Defeat Gypsies' },
    'c3r3r3r9r6.2defeatSkeletons': {
        'description': 'Defeat skeletons near the Tortuga graveyard.',
        'stringAfter': "Oh thank you!\x07Certainly, I have that bottle. There was a note inside if you'd like that as well...\x07After losing me husband, I don't have the heart for buried treasure any more.\x07Oh, wait! Here be the key, you can have it in peace.",
        'title': 'Defeat Skeletons' },
    'c3r3r3r9r6.3deliverKey': {
        'description': 'Take the key to Giladoga.',
        'title': 'Deliver Key' },
    'c3r3r3r9r6.AdoriasRequest': {
        'description': 'Help Adoria Dolores avenge the death of her husband.',
        'stringAfter': 'I thank you, so kindly. Now my husband can rest in peace.\x07Had the key right here all the time. Take it to Giladoga, with my regards.',
        'title': "Adoria's Revenge" },
    'c3r3r3r9r6key': {
        'description': 'Recover key Adoria Dolores found in the pocket of a dead pirate when she was fitting his burial suit and gave it to her husband for safekeeping.',
        'stringAfter': "Arrrrr! That's not it either! Keep slogging away until we find \x01slant\x01the one\x02!",
        'title': 'Key #6' },
    'c3r3r3r9r7.1visitMercedes': {
        'description': 'Mercedes Corazon is passionate about her tattoos, jewerly and love.',
        'stringAfter': "Aye, I found such a key once. Stumbled upon it in the woods, and it was so pretty, I kept it.\x07Made myself a necklace with it, I did.\x07But the necklace was stolen...\x07...along with my heart, by that scurvy bilge rat, \x01slant\x01Collier\x02...\x07He skipped town with 'em both and joined the EITC!",
        'title': 'Visit Mercedes Corazon' },
    'c3r3r3r9r7.1visitScarlet': {
        'description': 'Ask Scarlet if she knows of any keys.',
        'stringAfter': 'Aye, I found such a key once. Stumbled upon it in the woods, and it was so pretty, I kept it.\x07Made myself a necklace with it, I did.\x07But if you want the necklace ask that scurvy sea rat, \x01slant\x01Collier\x02...\x07He skipped town with it and joined the Navy!',
        'title': 'Visit Scarlet' },
    'c3r3r3r9r7.2captureCollier': {
        'description': 'Capture Collier at sea on a Navy ship.',
        'title': 'Capture Collier' },
    'c3r3r3r9r7.2captureCollierNew': {
        'description': "Capture Collier who's now a bowswain on an EITC Ogre.",
        'title': 'Capture Collier' },
    'c3r3r3r9r7.3maroonCollier': {
        'description': "Maroon Collier to recover Scarlet's necklace.",
        'title': 'Maroon Collier' },
    'c3r3r3r9r7.3maroonCollierNew': {
        'description': "Maroon Collier to recover Mercedes's necklace, and teach him a lesson for breaking Mercedes' heart.",
        'title': 'Maroon Collier' },
    'c3r3r3r9r7.4deliverNecklace': {
        'description': 'Take Scarlet her necklace.',
        'stringAfter': "Well... thanks for retrieving it but sadly, it brings back too many bad memories.\x07If I only I could buy myself a new necklace, I'd be grateful.",
        'title': 'Deliver Necklace' },
    'c3r3r3r9r7.4deliverNecklaceNew': {
        'description': 'Bring Mercedes her necklace.',
        'stringAfter': "Well... thanks for retrieving it but sadly, it brings back too many bad memories.\x07Take it please... but I am soothed somewhat to know...\x07...he's marooned on a barren island!!!",
        'title': 'Deliver Necklace' },
    'c3r3r3r9r7.5bribeScarlet': {
        'description': 'Pay Scarlet for her necklace.',
        'stringAfter': "Right then, it's yours...",
        'title': 'Buy The Necklace' },
    'c3r3r3r9r7.6deliverKey': {
        'description': 'Take the key to Giladoga.',
        'title': 'Deliver Key' },
    'c3r3r3r9r7key': {
        'description': 'Rumor has it that another key was once held by the tattoo vixen, Mercedes Corazon.',
        'stringAfter': "Neigh, this doesn't work either. It's becoming comical, ey?\x07Try Pauper Pedro. He knows 'bout another key, but...\x07...poor bloke's all tied up in knots after being drafted by the Navy!\x07First, destroy his enlistment papers then he'll relax enough to help us.",
        'title': 'Key #7' },
    'c3r3r3r9r8.1recoverOrders': {
        'description': "Sink Navy ships to recover Woodruff's orders.",
        'stringAfter': "These look proper. Says here these orders apply to \x01slant\x01Lt. Blakeley\x02 as well.\x07I'd have a word with him right away. Don't tell 'im I sent you.",
        'title': "Recover Woodruff's Orders" },
    'c3r3r3r9r8.1recoverOrdersNew': {
        'description': "Poor ole Pedro has been drafted to the English Navy - and he's Spanish! Find and destroy his enlistment papers!",
        'stringAfter': 'Good work, mate. Now go to Pedro and tell him the good news...\x07...and gets me key. Off ye go!',
        'title': "Recover Pedro's Orders" },
    'c3r3r3r9r8.2visitBlakeley': {
        'description': 'Ask Peter Blakeley about Woodruff.',
        'stringAfter': "Woodruff's no Navy man! He was court marshaled for stealing the Admiral's rum. He's marooned on Isla Cangrejos.",
        'title': 'Visit Peter Blakeley' },
    'c3r3r3r9r8.2visitPauper': {
        'description': 'Pedro the humble bartender knows where another key is.',
        'stringAfter': 'Amigo, I am so indebted to you for destroying that paper trail but...\x07I have a little \x01slant\x01chore\x02 that must be done before I give you information about the key. \x01slant\x01Si\x02?',
        'title': 'Visit Pauper' },
    'c3r3r3r9r8.3paupersRequest': {
        'description': 'Pedro worried so much about being drafted he got a serious skin rash and needs the salve to sooth his aching burn.',
        'stringAfter': '\x01slant\x01Aye-chi-hauhau\x02!!! That feels.... goooood!\x07Thanks swabbie! I buried the key right here on Padres.\x07Recover the chest and the key is yours.',
        'title': 'Recover Salve' },
    'c3r3r3r9r8.3visitWoodruff': {
        'description': 'Find Woodruff marooned on Isla Cangrejos.',
        'stringAfter': "Oh thank heavens you found me! Jolly Roger left me to the vultures!\x07Thought I was going to die here... help me!\x07The locals told me about some sand beetles. The crabs who eat them have a healing salve in their bellies...\x07... that's why the natives live so long!",
        'title': 'Visit Woodruff' },
    'c3r3r3r9r8.4recoverKey': {
        'description': "Pedro hid one of Parker's keys in a buried chest in case he ever needed it as a bargain chip.",
        'title': 'Recover Buried Key' },
    'c3r3r3r9r8.4recoverSalve': {
        'description': 'Kill rock crabs to recover healing salve for Woodruff.',
        'stringAfter': "I feel better!\x07I have your key, but it's buried in a chest...\x07... and Jolly Roger... put a stinkin' curse on the lock.\x07But I've made a mold of the inside workin's of that lock with my earwax... take it!\x07And take a lock of my hair as well. Find someone who knows the dark arts and we'll be able to open it!",
        'title': 'Recover Salve' },
    'c3r3r3r9r8.5deliverWax': {
        'description': 'Take the earwax mold of the cursed lock to Fabiola in Tortuga.',
        'stringAfter': "Sure I can break the curse... but it's going to cost you...",
        'title': 'Deliver Wax' },
    'c3r3r3r9r8.6bribeFabiola': {
        'description': "Pay Fabiola to break the curse on Woodruff's lock.",
        'stringAfter': "Here's your key. Not much voodoo involved, truth be told.\x07The hair should hold the wax in place... but be quick about it or the wax will melt.",
        'title': 'Pay Fabiola For Help' },
    'c3r3r3r9r8.7deliverKey': {
        'description': 'Take the key to the cursed lock to Woodruff on Isla Cangrejos.',
        'stringAfter': "Good! That will open the chest alright.\x07Now all you need to do is dig up the chest... and mind the murderous crabs... they'll drive you mad!",
        'title': 'Deliver Key' },
    'c3r3r3r9r8.8recoverKey': {
        'description': "Find and dig up Woodruff's chest to recover the key.",
        'title': 'Dig Up Chest' },
    'c3r3r3r9r8.9deliverKey': {
        'description': 'Take the key to Giladoga.',
        'title': 'Deliver Key' },
    'c3r3r3r9r8key': {
        'description': "Pauper Pedro found the key while strolling the beach one day but, he won't hand it over unless he's off Navy \x01slant\x01entanglements\x02.",
        'title': 'Key #8' },
    'c3r3r4.10recoverCannons': {
        'description': 'Recover cannons for the Retch by sinking ships.',
        'stringAfter': "Ever closer, mate, ever closer...\x07Every ship needs a prow figure... sort of a spirit that guides her in times of distress...\x07I guess the prow figure of \x01slant\x01The Retch\x02 wanted to go for a swim... 'cause she fell into the water at first impact.\x07Dirty skeletons picked her up, they did. I want her back, mate.",
        'title': 'Cannons' },
    'c3r3r4.10recoverRum': {
        'description': "Smith needs something to sooth Bowdash's anger when he returns, and some fine rum will do the trick.",
        'stringAfter': 'Right then, good work. Bowdash will be pleased and...\x07My neck will be pleased as well. I can sail back to get on with life...\x07...soon as I get me stolen rudder, that is.',
        'title': 'Recover Rum' },
    'c3r3r4.11recoverFigure': {
        'description': "Steal back the Retch's prow figure from a skeleton ship.",
        'stringAfter': "What's a ship without supplies?\x07We don't need much... just enough to get us to Tortuga... but ye will wanna add some ballast...\x07I'll take care of the supplies... ye take care of the ballast.\x07The ballast \x01slant\x01was\x02 rum. But truth be told... I drank most of it!\x07We need the equivalent of 10 barrels of rum to sail...",
        'title': 'Prow Figure' },
    'c3r3r4.12.51recoverKey': {
        'description': 'Search for a key that Davy Jones is seeking buried in a cave on Isla Tormenta',
        'stringAfter': "You found it! Well done mate!\x07This is a happy day for the King!\x07Go tell Smith he's free...\x07... as long as my ship's in port by sundown! HAH!",
        'title': "Davy Jones' Key" },
    'c3r3r4.12.52visitSmith': {
        'description': "Tell John Smith that he's in the clear as soon as the ship is delivered to Tortuga",
        'stringAfter': "Great work, mate! Tell Gibbs I'll join Sparrow's crew soon as I deliver this tub!",
        'title': 'Return to John Smith' },
    'c3r3r4.12.5visitBowdash': {
        'description': 'Tell Andrew Bowdash in Tortuga that his ship has been repaired',
        'stringAfter': "As good as new. HAH!\x07Don't know if I buy your story...\x07... lucky for you something has come up.\x07The king seems to have gotten himself in a bad way with a nasty fellow...\x07\x01slant\x01Davy Jones\x02 himself! Gave me the \x01slant\x01Black Spot\x02!\x07So I figure what I need is some \x01slant\x01leverage\x02 with Jones...\x07... something he wants more than me! HAH!\x07There's a \x01slant\x01key\x02 Jones has his heart set on finding, and I happen to know where it's buried.\x07Go to \x01slant\x01Isla Tormenta\x02 and find a cave...\x07... the key should be buried there.\x07Bring me the key and I'll give you John Smith wrapped in a bow! HAH!",
        'title': 'Bowdash' },
    'c3r3r4.12recoverRum': {
        'description': 'Steal 10 barrels of rum to use as ballast.',
        'stringAfter': "Okay, while I rig the ship for sail...\x07Could ye deliver a message?\x07Tell \x01slant\x01Andrew Bowdash\x02 his ship's as good as new...\x07... and will be delivered to him this very week!",
        'title': 'Ballast' },
    'c3r3r4.13visitJoshamee': {
        'description': 'Return to Joshamee Gibbs and tell him John Smith will join the crew.',
        'title': 'Return To Joshamee' },
    'c3r3r4.1visitBowdash': {
        'description': 'Go ask Andrew Bowdash if he knows where Smith is.',
        'stringAfter': "I don't suppose you mean the John Smith I hired to build me a ship?\x07Build me a ship, says I. Two \x01slant\x01weeks\x02 says he...\x07... That was \x01slant\x01months\x02 ago! HA!\x07Only heard this morning as to his whereabouts...\x07The scalawag has run ashore with only the shell of a ship... my ship!\x07If you want Smith... bring me my vessel!\x07\x01slant\x01Driftwood Island\x02, they call it.",
        'title': 'Visit Andrew Bowdash' },
    'c3r3r4.2visitSmith': {
        'description': 'Find John Smith on Driftwood Island.',
        'stringAfter': "Bowdash knows me whereabouts? I'm done for...\x07I was puttin' the finishing touches on the ship of his, when I decided to uh...\x07...test her seaworthiness with an easy rum run...\x07...just my luck to get shot by the Navy!\x07She used to be called \x01slant\x01The Gretchen\x02 on account of her future owner...\x07A gift for Bowdash's sweetheart but the cannons blew off the other letters...\x07...so now she's \x01slant\x01The _retch__\x02!\x07Help me get her into shape and I'll join with Sparrow, I will. We'll start with the starboard hull.",
        'title': 'Visit John Smith' },
    'c3r3r4.3.5visitSmith': {
        'description': 'Talk to John Smith about the Port Side Repairs.',
        'stringAfter': "Look close and ye can see The Retch listin' to one side...\x07It's due to the lack of weight on her port... she's missing a good bit of her paneling there.\x07We'd best work on \x01slant\x01that\x02 next... before we move on to the decks and so forth...\x07The port was put together much the same way... only it was pulled apart... much \x01slant\x01worse\x02!\x07We'll need more than just planks this time... the cannonade damaged a bit of the frame.\x07And frame repair means \x01slant\x01beams\x02 and \x01slant\x01bolts\x02... they're harder to find...\x07... but ye can find 'em in the same places as \x01slant\x01planks\x02 and \x01slant\x01nails\x02!",
        'title': 'Consult John Smith' },
    'c3r3r4.4.5visitSmith': {
        'description': 'Return to John Smith.',
        'stringAfter': "Well, now at least we have something that floats... with luck!\x07The next step is to make some repairs to the cabin...\x07Seein' as \x01slant\x01The _Retch__\x02 was intended for her ladyship... Bowdash had the cabin carved out of teak.\x07Looks real nice when yer done but I'd rather sniff kraken breath all day than repeat that business...\x07But luck was with me... when I got yer help!\x07Remember now, what's the first order of business?",
        'title': 'Return To Smith' },
    'c3r3r4.5.5visitSmith': {
        'description': 'Return to John Smith.',
        'stringAfter': "She sure looks pretty... for a \x01slant\x01tub\x02.\x07Ships need sails... and sails need masts... and masts need beams... and beams need bolts!\x07Get to it before the weather turns... my head itches when the weather turns.\x07So either the weather's about to change... or I have lice!\x07Off ye go, mate!",
        'title': 'Return To Smith' },
    'c3r3r4.7visitSmith': {
        'description': 'Return to John Smith to complete the building of the ship.',
        'stringAfter': "Let's get the sails and rigging together now.\x07The \x01slant\x01mainsail\x02... she's a big piece of cloth, aye!\x07I'm not going to suggest making the mainsail... takes too much \x01slant\x01discipline\x02 for a pirate!\x07Sail comes in yards... and mainsails are \x01slant\x01huge\x02 so they come in \x01slant\x01lots\x02 of yards!\x07Ye be needin' many yards of coarse sailcloth for the mainsails. There's also \x01slant\x01fine\x02 sailcloth...\x07... but that's not necessary for this tub!",
        'title': 'Return To Smith' },
    'c3r3r4.8recoverSails': {
        'description': 'Recover sailcloth by sinking ships.',
        'stringAfter': "Nice work! \x01slant\x01The Retch\x02 has sails... but can she sail?\x07Not without rigging says I...\x07\x01slant\x01Rigging's\x02 a cinch if done right...",
        'title': 'Sails' },
    'c3r3r4.9recoverRopes': {
        'description': 'Recover ropes to use as rigging on the Retch by sinking ships.',
        'stringAfter': "\x01slant\x01The Retch\x02 was intended as a sort of \x01slant\x01pleasure craft\x02... \x07Bowdash didn't want her weighed down by heavy guns...\x07But if we're gonna get her back to Tortuga in one piece... we'd better alter that intention, savvy?",
        'title': 'Rigging' },
    'c3r3r4Smith': {
        'description': 'Help John Smith build a ship for Andrew Bowdash.',
        'stringAfter': 'Always good to have a man who can handle a hammer aboard. Well done!',
        'stringBefore': "Ol' Smith got himself into a \x01slant\x01situation\x02 with Andrew Bowdash - that's who'd know where to find Smith.",
        'title': 'Black Pearl Recruit: John Smith' },
    'c3r3r4r11.1davyJonesArmy': {
        'description': "Defeat the barnacle head Dregs to find The Retch's rudder.",
        'title': 'Defeat Dregs' },
    'c3r3r4r11.2davyJonesArmy': {
        'description': 'Spineskulls were the brains behind stealing the rudder, something they plan to use once they get the Flying Dutchman seaworthy again.',
        'title': 'Defeat Spineskulls' },
    'c3r3r4r11.3davyJonesArmy': {
        'description': "Get the rudder back stolen from The Retch by Davy Jones' horrid henchmen!",
        'title': 'Recover Rudder' },
    'c3r3r4r11.DavyJonesArmy': {
        'description': 'Smith needs to get his rudder back before he can sail, since some henchmen of Davy Jones stole this vital piece',
        'stringAfter': "Ahhh! Well done, mate! Well done indeed!\x07Now I can return this wretched Retch and get back to Jack's crew!",
        'title': 'Recover Rudder' },
    'c3r3r4r3r1.1recoverMeat': {
        'description': 'Get some rock crab meat for lunch.',
        'stringAfter': "You've never had to make repairs on your own, have ye...\x07Well good thing you've got me then, mate.\x07I'll try to make this as \x01slant\x01simple\x02 as possible... So listen close!\x07\x01slant\x01Three parts\x02 to repairin' a ship - the wood, something to secure them, like nails and bolts, and the \x01slant\x01pitch\x02.\x07Being a pirate, you have a distinct advantage in that... you can steal it all!\x07The Navy, East India agents, skeletons - they're all good sources of supplies for ship repair.\x07Get the nails and bolts first, ey? If not, they'll rust...",
        'title': 'Get Lunch' },
    'c3r3r4r3r1.1shipMaterials': {
        'description': 'Smith needs the planks from the sturdy hulls of the Marauder ships, defeat them and bring him the planks!',
        'stringAfter': "Odds, bobs, hammers and tongs, that's some fine wood!\x07And you're a fine pirate indeed. Now, time for some...\x07Food! Get us some crab meet, I'm real hungry!",
        'title': 'Gather Materials' },
    'c3r3r4r3r1.2needFood': {
        'description': 'Get some crab meat for lunch.',
        'stringAfter': "You've never had to make repairs on your own, have ye...\x07Well good thing you've got me then, mate.\x07I'll try to make this as \x01slant\x01simple\x02 as possible... So listen close!\x07\x01slant\x01Three parts\x02 to repairin' a ship - the wood, the nails, and the \x01slant\x01pitch\x02.\x07The nails hold the wood together and the pitch stops the leaking... got it?\x07Being a pirate, you have a distinct advantage in that... you can steal it all!\x07The Navy, East India agents, skeletons - they're all good sources of supplies for ship repair.",
        'title': 'Get Lunch' },
    'c3r3r4r3r1build': {
        'description': 'Rebuild the Starboard hull of The Retch yourself.',
        'title': 'Build It Yourself' },
    'c3r3r4r3r1r2.1recoverWood': {
        'description': 'Recover planks of pine from ships.',
        'stringAfter': 'Well done, mate!',
        'stringBefore': 'So... 20 \x01slant\x01panks of pine\x02...\x07Navy ships is a good source. In fact, any ships will do. \x07Course, ye risk damage to yer \x01slant\x01own\x02 ship that way...',
        'title': 'Planks Of Pine' },
    'c3r3r4r3r1r2.2recoverNails': {
        'description': 'Recover rusty nails from rock crabs.',
        'stringAfter': 'Well done, mate!',
        'stringBefore': "Aye, \x01slant\x01nails\x02 it is...\x07Nails be found pretty much anywhere nails be used...\x07Thar's two types... \x01slant\x01rusty\x02 and \x01slant\x01not rusty\x02. The rusty ones wash up on beaches.\x07Rock crabs love to eat them... which means we \x01slant\x01love\x02 rock crabs. Easy way to score a rusty nail.",
        'title': 'Rusty Nails' },
    'c3r3r4r3r1r2.3recoverNails': {
        'description': 'Recover new nails from ships.',
        'stringAfter': 'Well done, mate!',
        'stringBefore': "Aye, \x01slant\x01nails\x02 it is...\x07Nails be found pretty much anywhere nails be used...\x07Thar's two types... \x01slant\x01rusty\x02 and \x01slant\x01not rusty\x02.\x07\x01slant\x01New\x02 nails are stronger, so ye don't need as many... but they're also harder to find.",
        'title': 'New Nails' },
    'c3r3r4r3r1r2.4recoverPitch': {
        'description': 'Recover pitch from Navy barrels.',
        'stringAfter': 'Well done, mate!',
        'stringBefore': "Ah, the sweet smell of \x01slant\x01pitch\x02... it brings back memories of me dear \x01slant\x01Mother\x02.\x07That's what I called \x01slant\x01me first dinghy\x02 as a young lad... \x01slant\x01Mother\x02. I named her meself!\x07And she leaked like a chicken stuck with a cutlass... which is why I needed lots of pitch!\x07\x01slant\x01Where\x02 to get it... that's \x01slant\x01the thing\x02 with pitch. It doesn't float... so sinkin' ships tends to sink the pitch as well.\x07Better off stealin' it from Navy forts.",
        'title': 'Pitch' },
    'c3r3r4r3r1r2materials': {
        'description': 'Gather materials for repairing the hull.',
        'items': 'Materials',
        'stringAfter': 'Looks like we have all we need now.',
        'stringBefore': "You've never had to make repairs on your own, have ye...\x07Well good thing ye have me then, mate.\x07I'll try to make this as \x01slant\x01simple\x02 as possible... So listen close!\x07\x01slant\x01Three parts\x02 to repairin' a ship - the wood, the nails, and the \x01slant\x01pitch\x02.\x07The nails hold the wood together and the pitch stops the leaking... got it?\x07Pirates have a distinct advantage in that... ye can steal it all!\x07The Navy, East India agents, skeletons - they're all good sources of supplies for ship repair.",
        'title': 'Gather Materials' },
    'c3r3r4r3r1r3.1starboardMaterials': {
        'description': 'Monarchs are cargo ships as well as war vessels and they usually carry nails for ship repairs.',
        'title': 'Recover Nails' },
    'c3r3r4r3r1r3.2starboardMaterials': {
        'description': 'The extra long, extra hard nails are only found in Man-O-Wars holds because they need them for repairing their hulls.',
        'title': 'Recover Bolts' },
    'c3r3r4r3r1r3.StarboardMaterials': {
        'description': 'Gather materials for repairing the hull.',
        'items': 'Materials',
        'title': 'Gather Materials' },
    'c3r3r4r3r2.1visitOMalley': {
        'description': "Hire shipwright O'Malley in Tortuga to rebuild the starboard hull of The Retch.",
        'stringAfter': "Smith sent ye, did he? Did he mention I don't \x01slant\x01like\x02 to do repairs on remote islands...?\x07Fact is, I \x01slant\x01hate\x02 it!\x07... so this will cost ye dearly. Here's what I be thinkin' for me \x01slant\x01fee\x02... take it or leave it.",
        'title': "Visit O'Malley" },
    'c3r3r4r3r2hire': {
        'description': 'Hire a master shipbuilder to rebuild the Starboard hull.',
        'stringBefore': "If ye wanna \x01slant\x01hire\x02 a master shipbuilder... I recommend \x01slant\x01O'Malley\x02...\x07... but he don't come cheap. For starters, he hates the sea!\x07Never \x01slant\x01have\x02 been able to understand that one... a man who \x01slant\x01builds\x02 ships but doesn't sail?\x07Ye will find him at the shipwright building in Tortuga. ",
        'title': 'Hire A Shipbuilder' },
    'c3r3r4r3r2r2.1recoverSaw': {
        'description': "Recover O'Malley's saw from an East India company ship.",
        'stringAfter': "Me saw! I've missed this little lady.",
        'stringBefore': 'Two gents from the East India Trading Company paid me a visit to collect certain \x01slant\x01taxes\x02...\x07What taxes they be, says I? \x01slant\x01Whatever\x02 taxes we \x01slant\x01say\x02 they says...\x07They skulked away with me best saw... and I want it back.',
        'title': 'Recover Saw' },
    'c3r3r4r3r2r2.2deliverShip': {
        'description': 'Deliver a ship in a bottle to Darby Drydock in Port Royal.',
        'stringAfter': "Darby's a good man - always pays in cash.",
        'stringBefore': "I just finished a ship I need delivered...\x07I'd like you to do the deliverin'... thing is, this customer's a bit odd.\x07His name's \x01slant\x01Ringo\x02. Odd name for a pirate, eh? Make sure you get there in one piece...\x07I'm not going to say anything...\x07On second thought, take the ship to \x01slant\x01Darby Drydock\x02 in Port Royal.\x07He'll know how to get it to Ringo.",
        'title': 'Deliver Ship' },
    'c3r3r4r3r2r2.3recoverChest': {
        'description': "Dig up a chest of Jacaranda wood for O'Malley.",
        'stringAfter': 'Fine wood, ey?',
        'stringBefore': "Jacaranda wood is rare 'round these parts...\x07Few folks have 'eard of it... and none can pronounce it!\x07... but it carves real nice and I'd like to get me hands on some.\x07I know of a chest made of Jacaranda wood said to be buried not far from here...",
        'title': 'Recover Chest' },
    'c3r3r4r3r2r2.4bribeOMalley': {
        'description': "Pay O'Malley in gold.",
        'stringAfter': "Nice doin' business with ye.",
        'stringBefore': "Now there's the matter of me own finances...",
        'title': "Pay O'Malley" },
    'c3r3r4r3r2r2payment': {
        'description': "Compensate shipwright O'Malley.",
        'items': 'Tasks',
        'stringAfter': 'Okay, mate. Ye got yerself a shipwright!',
        'title': "Pay O'Malley" },
    'c3r3r4r3starboardHull': {
        'description': 'Rebuild the Starboard hull of The Retch.',
        'items': 'Choices',
        'stringAfter': "I'll get to work on the starboard hull.\x07While I'm doing that mate, you go gather the materials for the port side hull.",
        'title': 'Rebuild Starboard Hull' },
    'c3r3r4r4portHull': {
        'description': 'Rebuild the Port hull of The Retch.',
        'items': 'Choices',
        'stringAfter': "I'll start on the port hull.\x07The main cabin is next but, in the meantime...\x07Me belly is aching once again. More crabs, please.",
        'title': 'Rebuild Port Hull' },
    'c3r3r4r4r1.1recoverMeat': {
        'description': 'Get some rock crab meat... for energy.',
        'stringAfter': 'We will need a few items... but I already drew up a list.\x07Where do ye wanna start?',
        'title': 'Get Rock Crab Meat' },
    'c3r3r4r4r1build': {
        'description': 'Rebuild the Port hull of The Retch.',
        'title': 'Build It' },
    'c3r3r4r4r1r2.1portHullMaterials': {
        'description': 'Defeat and pillage the special fire cured planks of wood found only on the Barracuda ships.',
        'title': 'Gather Planks' },
    'c3r3r4r4r1r2.1recoverWood': {
        'description': 'Recover planks of pine from ships.',
        'stringAfter': 'Well done, mate!',
        'stringBefore': 'So... 30 \x01slant\x01panks of pine\x02...\x07Navy ships is a good source. In fact, any ships will do. Course, you risk damage to your \x01slant\x01own\x02 ship that way...',
        'title': 'Planks Of Pine' },
    'c3r3r4r4r1r2.2portHullMaterials': {
        'description': "When the Navy guards aren't looking, steal some barrels of pitch for Smith's repairs.",
        'title': 'Recover Pitch' },
    'c3r3r4r4r1r2.2recoverNails': {
        'description': 'Recover coffin nails from skeletons.',
        'stringAfter': 'Fine work, mate!',
        'stringBefore': "Sometimes skeletons carry coffin nails around with 'em... those'll work just as well...",
        'title': 'Nails' },
    'c3r3r4r4r1r2.3portHullMaterials': {
        'description': "Smith needs 16 spools of wire - not sure what it's for but if he needs it... get it for him.",
        'title': 'Recover Wire' },
    'c3r3r4r4r1r2.3recoverBeams': {
        'description': 'Recover wooden beams from Fly Traps.',
        'stringAfter': 'Those Fly Traps be hard to bring down, ey?',
        'stringBefore': "Flytrap's a \x01slant\x01hard\x02 wood... so look for big, nasty Fly Traps...\x07As you might imagine, they tend to live in the swamps and wooded areas.\x07Right then, best be gettin' on, mate...",
        'title': 'Oak Beams' },
    'c3r3r4r4r1r2.4recoverBolts': {
        'description': 'Recover bolts from East India ships.',
        'stringAfter': 'Fine load of bolts you got there, mate!',
        'stringBefore': "Bolts. We need bolts to hold 'er tight.\x07No bolts better than East India Trading Company bolts... they bring 'em in from Singapore. Don't ask.",
        'title': 'Bolts' },
    'c3r3r4r4r1r2.PortHullMaterials': {
        'description': 'Gather materials for repairing the hull.',
        'items': 'Materials',
        'title': 'Gather Materials' },
    'c3r3r4r4r1r2materials': {
        'description': 'Gather materials for repairing the hull.',
        'items': 'Materials',
        'stringAfter': 'Looks like we have all we need now.',
        'stringBefore': 'Well then... a few bits and pieces to pick up first...',
        'title': 'Gather Materials' },
    'c3r3r4r4r2.1visitOMalley': {
        'description': "Hire shipwright O'Malley in Tortuga to rebuild the port hull of The Retch.",
        'stringAfter': "I figured you'd be back... the other side of that ship is going to take some work...\x07I'm in a spot of trouble... if ye help me out... I'll scratch yer back, savvy?\x07I delivered a boat to a rumrunner... name's \x01slant\x01Bronze John\x02.\x07Thing is... he filled it with too many barrels and the Navy caught up with him....\x07... seems all that rum slowed him down. Now he's blamin' me!\x07Two hundred barrels of rum straight down to Davy's Locker.\x07Can't possibly repay Bronze John... but I want ye to offer yer services, to calm him down a bit!",
        'title': "Visit O'Malley" },
    'c3r3r4r4r2.2visitJohn': {
        'description': 'Find Bronze John on Driftwood Island.',
        'stringAfter': "I'm so mad I could bite the head off a kraken!\x07O'Malley sent you \x01slant\x01here\x02? That stinkin' wretch sent \x01slant\x01you\x02 to calm \x01slant\x01me\x02 down?\x07The only thing that'd calm me down is getting my rum back...\x07That... and Barts, the Navy aggressor who transgressed against my rum...\x07I'd like you to bring 'im here...\x07Bring me Captain James Tollington Barts!",
        'title': 'Visit Bronze John' },
    'c3r3r4r4r2.3captureBarts': {
        'description': 'Capture Captain Barts at sea by sinking Navy ships.',
        'title': 'Capture Captain Barts' },
    'c3r3r4r4r2.4maroonBarts': {
        'description': 'Maroon Captain Barts on Driftwood Island.',
        'title': 'Maroon Captain Barts' },
    'c3r3r4r4r2.5visitOMalley': {
        'description': "Return to shipwright O'Malley.",
        'stringAfter': "I got word from Bronze John that he's in a much better state...\x07Ok, I consider yer services paid for... they will be rendered in short order...\x07As soon as I receive me fee, that is.",
        'title': "Return To O'Malley" },
    'c3r3r4r4r2.6bribeOMalley': {
        'description': "Pay O'Malley to repair the port hull of the Retch.",
        'stringAfter': "Thanks, mate. I'm on me way.",
        'title': "Pay O'Malley" },
    'c3r3r4r4r2hire': {
        'description': 'Hire a master shipbuilder to rebuild the Port hull.',
        'stringBefore': "The interior work is gonna be complicated... I hope O'Malley's up for it...\x07See if he can help...",
        'title': 'Hire A Shipbuilder' },
    'c3r3r4r5cabin': {
        'description': 'Rebuild the cabin of The Retch.',
        'items': 'Choices',
        'stringAfter': "I expect the main cabin to go smoothly.\x07Come back quickly. There is still a bit to do...\x07but before ye go...\x07I'm famished mate.\x07I know but, it takes lots of energy to build a ship, ey?\x07Get me some more crab meat.",
        'title': 'Rebuild Cabin' },
    'c3r3r4r5r1.1needMoreFood': {
        'description': 'Smith is working around the clock and takes several food breaks during the day to keep his strength up.',
        'stringAfter': "Ye-ouw-wee! That's some tasty looking crabs ya got there! Thanks! Now on to the main cabin repairs...",
        'title': 'Defeat Crabs' },
    'c3r3r4r5r1.1recoverMeat': {
        'description': "Recover a meal's worth of rock crab meat.",
        'stringAfter': 'We will need a few items... but I already drew up a list.\x07Where would ye like to start?',
        'title': 'Get Rock Crab Meat' },
    'c3r3r4r5r1build': {
        'description': 'Rebuild the cabin of The Retch.',
        'stringBefore': "Do it yourself, eh? In that case, we'll need something to eat!\x07Go fetch us some crab meat, mate!",
        'title': 'Build It Yourself' },
    'c3r3r4r5r1r2.1cabinMaterials': {
        'description': 'Ogre wood is very hard and rare, something Smith needs for the interior.',
        'title': 'Defeat Ogres' },
    'c3r3r4r5r1r2.1recoverWood': {
        'description': 'Recover planks of teak from larger ships.',
        'stringAfter': 'Well done, mate!',
        'stringBefore': "Teak is similar to straight planks... just more expensive...\x07... and smaller ships are mostly made of pine, so if you do find teak, ye won't find much.\x07We need to go after the larger ships to have a chance of finding teak.",
        'title': 'Planks Of Teak' },
    'c3r3r4r5r1r2.2cabinMaterials': {
        'description': 'Get Smith the beams from the Predators because they are the exact same size as The Retch.',
        'title': 'Defeat Predators' },
    'c3r3r4r5r1r2.2recoverNails': {
        'description': 'Recover brass nails from larger ships.',
        'stringAfter': 'Well done, mate!',
        'stringBefore': "\x01slant\x01Brass nails\x02 don't tend to wash up on beaches... so if ye look for 'em there, it'll be a long, hard look.\x07Course, the larger vessels will have brass nails... though in varying quantities...\x07... and often times, East India Trading Company ships will be \x01slant\x01carrying\x02 them as cargo.",
        'title': 'Brass Nails' },
    'c3r3r4r5r1r2.CabinMaterials': {
        'description': 'Gather the materials Smith needs to fix the main cabin.',
        'stringAfter': '',
        'title': 'Cabin Materials' },
    'c3r3r4r5r1r2materials': {
        'description': 'Gather materials for repairing the cabin.',
        'items': 'Materials',
        'stringAfter': 'Looks like we have all we need now.',
        'stringBefore': "Lots to do... let's get started.",
        'title': 'Gather Materials' },
    'c3r3r4r5r2.1visitOMalley': {
        'description': "Hire shipwright O'Malley in Tortuga to rebuild the cabin of The Retch.",
        'stringAfter': "He told ye me first name's \x01slant\x01Teek\x02?\x07I mean it is... that \x01slant\x01is\x02 my name. But that's not \x01slant\x01funny\x02. He's been in the sun too long.\x07Let's get to business... \x01slant\x01The Retch's\x02 cabin is made of teak... a lot of it, too...\x07So it will cost you, of course.\x07But first... I'd like to drum up some new business...",
        'title': "Visit O'Malley" },
    'c3r3r4r5r2.2sinkShips': {
        'description': "Sink East India Trading Company ships for O'Malley.",
        'stringAfter': "It has occurred to me that sinkin' ships is an ill-conceived plan for getting business.\x07I've got a new plan...\x07Why don't ye just pay me? That's business, isn't it?",
        'title': 'Sink East India Trading Company Ships' },
    'c3r3r4r5r2.3bribeOMalley': {
        'description': "Pay O'Malley to repair the cabin of the Retch.",
        'stringAfter': 'See? Business is better already!',
        'title': "Pay O'Malley" },
    'c3r3r4r5r2hire': {
        'description': 'Hire a master shipbuilder to rebuild the cabin.',
        'stringBefore': "Tough to find someone who works in \x01slant\x01teak\x02... but it just so happens that \x01slant\x01O'Malley's\x02 first name \x01slant\x01is\x02 Teek.\x07Honor bright! His name is T-e-e-k... and he \x01slant\x01works\x02 in T-e-a-k the wood.\x07That's not quite as funny as when it entered me head. Maybe I should take cover from the sun, ey?",
        'title': 'Hire A Shipbuilder' },
    'c3r3r4r6masts': {
        'description': 'Rebuild the masts of The Retch.',
        'items': 'Choices',
        'stringAfter': "Once I get these masts up, we'll be ready to add the finishing touches.\x07While I'm stepping the mast, you can step lively and gather some sail cloth and rigging.",
        'title': 'Rebuild Masts' },
    'c3r3r4r6r1.1needMoreFood': {
        'description': "Smith needs more crab meat to keep his strength up - he's got a hearty appetite!",
        'stringAfter': "Well done, mate. I haven't had such good crab meat since...\x07Last time you brought me some... ha, ha!",
        'title': 'Crab Meat' },
    'c3r3r4r6r1.1recoverMeat': {
        'description': "Recover a meal's worth of crab meat.",
        'stringAfter': "Building a mast \x01slant\x01isn't\x02 like runnin' aground with a deep keel in shallow water - it's hard.\x07You'll need to commandeer the necessary necessities... that be several mast beams and buckets of bolts.",
        'title': 'Get Crab Meat For Lunch' },
    'c3r3r4r6r1build': {
        'description': 'Rebuild the masts of The Retch.',
        'title': 'Build It' },
    'c3r3r4r6r1r2.1mastMaterials': {
        'description': 'Storm Reapers have bowsprits that when lashed together make a suitable mast for The Retch.',
        'title': 'Sink Storm Reapers' },
    'c3r3r4r6r1r2.1recoverBeams': {
        'description': 'Recover mast beams from large ships.',
        'stringAfter': 'Well done, mate!',
        'stringBefore': 'When you sink a ship to steal her mast, make sure not to break the mast in the process!',
        'title': 'Mast Beams' },
    'c3r3r4r6r1r2.2mastMaterials': {
        'description': 'To secure the bowsprits you must have strong steel bands from another cursed ship and Revenants carry the best.',
        'title': 'Sink Revenants' },
    'c3r3r4r6r1r2.2recoverBolts': {
        'description': 'Recover bolts from large ships.',
        'stringAfter': 'Well done, mate!',
        'stringBefore': 'The bolts should be easy.',
        'title': 'Bolts' },
    'c3r3r4r6r1r2.MastMaterials': {
        'description': 'The mizzenmast was so damaged it cannot be rebuilt so you must gather materials for a new one.',
        'title': 'Mast Materials' },
    'c3r3r4r6r1r2materials': {
        'description': 'Gather materials for repairing the masts.',
        'items': 'Materials',
        'stringAfter': 'Looks like we have all we need now.',
        'title': 'Gather Materials' },
    'c3r3r4r6r2.1visitOMalley': {
        'description': "Hire shipwright O'Malley in Tortuga to rebuild the masts of The Retch.",
        'stringAfter': "Aye, I can help ye with the masts. It's going to cost ye, though.",
        'title': "Visit O'Malley" },
    'c3r3r4r6r2.3bribeOMalley': {
        'description': "Pay O'Malley to repair the masts of the Retch.",
        'stringAfter': "Those masts'll be up in no time!",
        'title': "Pay O'Malley" },
    'c3r3r4r8.1sailMaterials': {
        'description': 'Mercenaries carry some of the finest hemp ropes in the world and Smith needs them for his rigging.',
        'title': 'Recover Ropes' },
    'c3r3r4r8.2sailMaterials': {
        'description': "Dragoons' jacket linings are made of a special material that's strong, light and water resistant - perfect for sails!",
        'title': 'Recover Cloth' },
    'c3r3r4r8.SailMaterials': {
        'description': 'John needs you to gather some materials to refit The Retch with sails and rigging.',
        'stringAfter': "Good job... now, let's finish The Retch with some... uh...\x07finishing touches!",
        'title': 'Sail Materials' },
    'c3r3r4r9.1shipArmor': {
        'description': "Smith only needs two cannons, the other two he'll melt down and fashion into some armor to strengthen the ship's hull.",
        'title': 'Recover Cannons' },
    'c3r3r4r9.2shipFigure': {
        'description': "Smith needs a figurehead for The Retch because it's bad luck to sail without one and... it looks awesome!",
        'title': 'Recover Figurehead' },
    'c3r3r4r9.ShipMaterials': {
        'description': 'Gather materials to put the finishing touches on The Retch.',
        'stringAfter': "Well done, mate. I'm impressed!\x07Now just a few more odds and bobs and she'll be ready to sail.",
        'title': 'Finish Materials' },
    'c3visitJack': {
        'description': 'Jack is in the Faithful Bride tavern on Tortuga - a ray of light will guide you there.',
        'title': 'Find Jack Sparrow' },
    'c3visitJoshamee': {
        'description': 'Gibbs is the First Mate of the Black Pearl.  He can usually be found playing cards at a corner table in the Faithful Bride Tavern on Tortuga.',
        'stringAfter': "So Captain Jack Sparrow told ye we're going after the \x01slant\x01Pearl\x02, did he?\x07I'm not sayin' we is... and I'm not sayin' we isn't.\x07Ol' Jack has earned many enemies over the years...\x07But I like the cut of yer jib so I'll let ye prove yer trustworthiness...",
        'title': 'Speak With Joshamee Gibbs' },
    'c4.1visitValentina': {
        'description': 'Find the mystic Valentina on Padres Del Fuego island.',
        'stringAfter': "Good. You're here.",
        'title': 'Visit Valentina' },
    'cards.prt1.defeatCadets': {
        'description': 'Thin the hordes of Navy Cadets protecting the Fort.',
        'stringBefore': "One of my mates has been picked up by Navy officials.\x07 I intend to pluck him from the jaws of capture.\x07 If you could assist me, I'd be grateful.\x07 In fact, I have poker cards that a resourceful player might find handy.\x07 The local cadets are under the watch of Navy Sergeants that have access to the Prison.\x07 Cause a distraction fighting the cadets\n then snatch a prison key from one of their Sergeants.",
        'title': 'Prison Break (Easy)' },
    'cards.prt1.retrievekey': {
        'description': 'Retrieve a prison key from a Navy Guard',
        'stringAfter': "Of course that's where they'd put it. I could have guessed that!\x07 Anyway, here's your reward. Don't waste it.",
        'title': 'Retrieve Prison Key' },
    'cards.prt2.earnTrust': {
        'description': 'Return to Shane with the Muskets.',
        'stringAfter': "Quality muskets! I'm confident you are the pirate for this job.\x07 Acquire the rest of the disguises we need and the location of the Navy coin.",
        'title': 'Return to Shane' },
    'cards.prt2.recoverABadge': {
        'description': "Acquire the badge from a Navy Sergeant that identifies their rank to complete Shane's disguise.",
        'title': 'Acquire A Sergeants Badge' },
    'cards.prt2.recoverLocationDocument': {
        'description': 'Defeat Navy Veterans to find the document with the treasure stash.',
        'stringAfter': "This is everything. You've done great, and well earned your prize.",
        'title': 'Acquire Treasure Location' },
    'cards.prt2.recoverNavyCoats': {
        'description': 'Acquire from Navy Guards their coats as part of a disguise.',
        'title': 'Acquire Navy Coats' },
    'cards.prt2.recoverNavyMuskets': {
        'description': 'Shane has asked you to obtain Navy-issue muskets.',
        'stringAfter': "Quality muskets! I'm confident you are the pirate for this job.\x07 Acquire the rest of the disguises we need and the location of the Navy coin.",
        'stringBefore': "The Navy has a local stash of coin in Fort Charles.\x07 My mates and I intend on making off with it.\x07 However, we do not know where it is nor have the means to fight our way to it.\x07 If you could assist us in overcoming these shortcomings, I'll make it worth your while.\x07 I'll give you a cheat card of considerable value.\x07 First, acquire some muskets, a critical part of our disguise.",
        'title': 'Port Royal Fort Heist (Medium)' },
    'cards.prt2.recoverNavyPants': {
        'description': 'Acquire from Navy Guards their pants as part of a disguise.',
        'title': 'Acquire Navy Pants' },
    'cards.prt3.captureCaptain': {
        'description': 'Capture Commander Gentry, who is known to command a Level 13 caliber ship.',
        'title': 'Capture Commander Gentry' },
    'cards.prt3.defeatVeterans': {
        'description': 'Disturb the Veteran Navy ranks.',
        'stringAfter': 'Excellent work. But we still need to address the Navy forces just beyond these shores.\x07 Acquire their schedule and cause a void in their leadership. Once this is done, inform my contact in Tortuga that we can begin.',
        'title': 'Defeat Navy Veterans' },
    'cards.prt3.getReward': {
        'description': 'Get your reward from Shane.',
        'title': 'Return to Shane' },
    'cards.prt3.maroonCaptain': {
        'description': 'Maroon Commander Gentry on any wild island.',
        'title': 'Maroon Commander Gentry' },
    'cards.prt3.startCrimeWave': {
        'description': "Tell Shane's Contact in Tortuga To Head Out.",
        'stringAfter': "Return to Shane and let him know we're on our way.",
        'title': "Report to Shane's Contact" },
    'cards.prt3.stealGuardSchedule': {
        'description': 'Defeat local Navy Sergeants to acquire a local guard patrol schedule.',
        'stringBefore': "A Cadre of my associates await the opportunity to plunder the coin of Port Royal.\x07 If you could assist me in creating that opportunity, I could make you almost unbeatable at poker...\x07 at least for a game.\x07 We need the guard schedule. Acquire it, disturb the Navy\n chain of command while you're at it, then return to me.",
        'title': 'Port Royal Crime Wave (Hard)' },
    'cards.prt3.stealShipSchedule': {
        'description': 'Steal a Navy Patrol Ship Schedule. They are carried by Level 7 or greater Navy vessels.',
        'title': 'Steal the Navy Patrol Ship Schedule' },
    'ccbm.1poker': {
        'description': "Win money at poker to prove you're a card player.",
        'stringAfter': "I know, I know I said I'd give ye something...\x07... only these skeletons, they've been provokin' me.\x07Go get one of 'em and I'll give ye your prize.",
        'stringBefore': "So, fancy yerself a card player, eh?\x07We'll see about that, we will.\x07Try winnin' a few hands at poker, then come back and I'll give ye something.",
        'title': 'Win At Poker' },
    'ccbm.1winAtPoker': {
        'description': "Win money at poker to prove you're a card player.",
        'stringAfter': "I know, I know I said I'd give ye something...\x07... only these skeletons, they've been provokin' me.\x07Go get one of 'em and I'll give ye your prize.",
        'title': 'Win At Poker' },
    'ccbm.2defeatSkeleton': {
        'description': 'Defeat a skeleton for Black Mack.',
        'title': 'Defeat A Skeleton' },
    'ccbm.2defeatUndead': {
        'description': 'Defeat the malevolent Undead Mutineers who keep harassing Black Mack.',
        'title': 'Defeat Undead' },
    'cul5.1visitBalthasar': {
        'description': 'Balthasar Bollard is the resident shipwright of Padres Del Fuego.',
        'stringAfter': "So ye be needing a new cutlass, eh?  I can help...but it will cost ya.\x07 I be needin' supplies.  Sailcloth from some navy ships, and also some plankin' as well.  Best quality, they are.\x07Then I'll be needing some ropes and rigging that's only found on East India vessels.\x07Now go and be quick about it!",
        'title': 'Visit Balthasar Bollard' },
    'cul5.2visitMiguel': {
        'description': 'Miguel Montoya is swapping stories with the local blacksmiths on Padres.',
        'stringAfter': "Bollard sent you, eh?  Rascal.\x07I'll not divulge my secret without some assistance getting out of a mess of my own.\x07I have a debt to repay.\x07Seeing how my debtor's son was killed by the French muerte,  could you defeat some of these diablos in my name?\x07This might just free me of my debt.",
        'title': 'Visit Miguel Montoya' },
    'cul5.3defeatUndeadFrench': {
        'description': 'Undead French have been sighted on Isla Cangrejos',
        'stringAfter': 'Gracias.  Listen closely-all my secrets I passed off to my apprentice,  Fuller,  the Port Royal smith.\x07He will get you what you need.  Vaya con Dios, Amigo.',
        'title': 'Undead French' },
    'cul5.4visitPhillip': {
        'description': 'Blacksmith Phillip Fuller has a thriving shop on Port Royal.',
        'stringAfter': "Spanish swords?  Yeah, I can make 'em.  But it ain't easy.  Takes the finest steel.\x07Bring me some premium Navy steel.  It's in a crate on Kingshead.\x07And I needs the bones of an undead Brigand for the handle. Savvy?  Go on now, don't tarry.",
        'title': 'Visit Phillip Fuller' },
    'cul5.5defeatBossScorpion': {
        'description': 'Venom Lash, one of the nastiest Dread Scorpions in the Caribbean.',
        'title': 'Venom Lash' },
    'cul5.6visitGrog': {
        'description': 'Return the dread scorpion blood to Doc Grog so he can finish his elixir.',
        'stringAfter': "Finally! Can't finish me elixir without this blood.\x07Fine work.  Now off ya go to Fuller and he'll reward ya right properly.",
        'title': 'Visit Doc Grog' },
    'cul5.7visitFuller': {
        'description': 'All you have to do now is return to Fuller on Port Royal to get your just rewards!',
        'title': 'Visit Phillip Fuller' },
    'cul5r1.1acquireSailcloth': {
        'description': 'Find Navy ships in Caribbean shipping lanes.',
        'title': 'Sail Cloth' },
    'cul5r1.2acquireWoodPlanks': {
        'description': 'Find Navy ships in Caribbean shipping lanes.',
        'title': 'Wood Planks' },
    'cul5r1.3acquireRopes': {
        'description': 'Find EITC ships in Caribbean shipping lanes.',
        'title': 'Ropes' },
    'cul5r1.4acquireRigging': {
        'description': 'Find EITC ships in Caribbean shipping lanes',
        'title': 'Rigging' },
    'cul5r1ShipParts': {
        'description': "Hunt Navy and EITC ships for Balthasar's parts.",
        'stringAfter': 'Nice work, mate.  Now find a gent name of Miquel Montoya, here on Padres.\x07Got into some trouble, he did.\x07But if you can help him, he holds the secret to making top-notch Spanish swords.',
        'title': "Balthasar's Ship Parts" },
    'cul5r2.1findNavySteel': {
        'description': 'Fuller told you to search the crates in Kingshead.',
        'title': 'Navy Steel' },
    'cul5r2.2acquireBoneHandle': {
        'description': "Undead Brigands can be found in the Rat's Nest on Tortuga.",
        'title': 'Bone Handle' },
    'cul5r2SwordParts': {
        'description': "Undead Brigands can be found in the Rat's Nest, on Tortuga.",
        'stringAfter': "Ah yes that's what I be needin' and, while I'm making your sword, I owe a favor to my old chum, Doc Grog.\x07He's brewin' a new healin' potion and needs the blood of a dread scorpion.\x07Find this nasty bugger on Rumrunner's Isle named 'Venom Lash' and then give it to Doc and we'll be square.",
        'title': 'Sword Components' },
    'dc1r1.1governorsMessage': {
        'description': "Navy Cadets are young and inexperienced and, well, haven't enough influence to bother bribing so, they'll try to stop you from finding the message.",
        'title': 'Thin Navy Ranks' },
    'dc1r1.2governorsMessage': {
        'description': "Captain Rott's EITC double agent always leaves his messages in a barrel out front of the Governor's Mansion.",
        'title': 'Find Secret Message' },
    'dc1r1.GovernorsMessage': {
        'description': 'The Casa de Muertos Guild has several key spies in the Caribbean. One is an island official who acts as a double agent. He feeds Captain Rott strategic information about the comings and goings of Navy troops and ships.',
        'stringAfter': "Some fine work, mate. More souls for...\x07uh, forget that, um, the message says that the Navy's defense plans be easy to steal...\x07fer a hearty pirate like yerself. Return those to me and...\x07...give no quarter to anyone who wants to stop ye!!",
        'stringBefore': "Listen close, mate. I must say somethin' that's \x01slant\x01not\x02 for all ears, savvy?\x07I be the Guildmaster fer the Casa de Muertos Guild. We be new to these parts.\x07Our patron is a wealthy ...uh, merchant of sorts who needs some \x01slant\x01favors\x02.\x07If ye be willin' to do some, we pay handsomely. Only thing is...\x07...just do as yer told and don't ask questions, ey?",
        'title': "Governor's Message" },
    'dc1r2.1defensePlans': {
        'description': 'The defense plans will be guarded, eliminate some of the Navy soldiers to make sure there were no witnesses.',
        'title': 'Defeat Navy Soldiers' },
    'dc1r2.2defensePlans': {
        'description': "The Navy's defense plans were poorly hidden one night by a drunken Watch Commander in the bookshelf in Fort Charles.",
        'title': 'Steal Defense Plans' },
    'dc1r2.DefensePlans': {
        'description': "The Navy's secret defense plans are hidden away in a bookshelf inside Fort Charles. Anyone who has the plans can find ways to easily defeat the Navy, making it a very useful document indeed.",
        'title': 'Defense Plans' },
    'dc2r1.1voodooRelics': {
        'description': 'Navy Marines are specially tasked with guarding the Royal Caverns and will probably attack if you go digging for the relic.',
        'title': 'Defeat Marines' },
    'dc2r1.2voodooRelics': {
        'description': 'Digging up and returning the voodoo relic to Sam Shaw - who wil sell them for a big profit - will help break the powerful hex placed on Port Royal.',
        'title': 'Recover Relic' },
    'dc2r1.VoodooRelics': {
        'description': "Famous Voodoo Princess, Tia Dalma, buried powerful relics on every island around the Caribbean to ward off evil spirits. The Casa de Muertos Guild's patron is very superstitious and wants them removed so he can do business on Port Royal.",
        'stringAfter': 'Ah-ha! The first relic is gone! Gone forever but...\x07We cannot celebrate until the others are found and removed from the ground.\x07Only that will break the wicked spell, and fill your pockets with gold!',
        'stringBefore': "Me name's Sam Shaw but everyone calls me \x01slant\x01Pierce\x02.\x07Captain Rott says yer a fine pirate ...and discrete. I likes discrete.\x07Killed a man once who couldn't shut his yap!\x07Here's yer next task... find a hidden voodoo relic, part of a set called, The Spiral Stones\x07 Buried long ago to ward off evil spirits and now...\x07...they fetch a fine price to a superstitious collector, ey?",
        'title': 'Voodoo Relics' },
    'dc2r2.1voodooRelics': {
        'description': 'To prove you are trustworthy, Sam Shaw wants you to defeat some Navy Soldiers even if they are too lazy to confront you.',
        'title': 'Defeat Navy Soldiers' },
    'dc2r2.2voodooRelics': {
        'description': 'Removing the second voodoo relic will weaken the powerful island hex and allow the Casa de Muertos Guild to operate more freely.',
        'title': 'Recover Second Relic' },
    'dc2r2.VoodooRelics': {
        'description': 'Tia Dalma buried several voodoo relics on Port Royal. All of them must be removed from the ground and sold to break her powerful curse.',
        'title': 'Voodoo Relics' },
    'dc3.2voodooRelics': {
        'description': 'The relics are buried in Murky Hollow - and they will be well guarded by various nasty creatures, so bring some serious firepower, or a mate.',
        'title': 'Recover Murky Hollow Relics' },
    'dc3r1.1voodooRelics': {
        'description': 'Billy Barrett has always had an appetite for strange meat - alligator meat in this case - the tougher the better.',
        'title': 'Defeat Tasty Gators' },
    'dc3r1.2voodooRelics': {
        'description': "Billy Barrett loves scorpion meat like pirates love pork - and he likes gobs and gobs of the vile, disguisting meat. It's a mystery why but you have to get it if you're to collect the major gold reward.",
        'title': 'Defeat Tasty Scorpions' },
    'dc3r1.3voodooRelics': {
        'description': "With every voodoo relic that's recovered, the more powerful the Casa de Muertos Guild grows - and that makes their patron \x01slant\x01very\x02 happy.",
        'title': 'Recover Hidden Relics' },
    'dc3r1.VoodooRelics': {
        'description': 'Help the Casa de Muertos Guild get a foothold in Port Royal by finding voodoo relics and help Bill Barrett fill his empty stomach.',
        'stringAfter': "Ya-hoooo! Meat, meat, meat! I'm so happy I gotta dance!\x07Enough of that, ole Billy's belly is full so on to business...\x07If ye know what I mean, ey?\x07No? Oh, me neither. Reminds me of a story.\x07A funny story but... I forgot, sooo...\x07Uh, one more job mate and thar be gold a plenty in return.",
        'stringBefore': "Hello, mate. Glad to see yer still alive... I mean not dead\x07I mean, uh, never mind. As I was sayin'...\x07Ole Billy Barrett be second in command, he is. Make that 3rd...\x07Or was it 4th? Me mind's a bit mushy fer details.\x07So here's the job... find some of them voodoo relics and...\x07Some food for ole Billy, ey?",
        'title': 'Find Relics & Food' },
    'dc4r1.1poisonNavy': {
        'description': 'Sergeants are key players because they assign all the rank-and-file soldiers to their stations. Defeating them will disrupt the entire chain of command and throw the Navy into chaos.',
        'title': 'Defeat Navy Sergeants' },
    'dc4r1.2poisonNavy': {
        'description': "These elite EITC troops are the ones who guard the barrels of Officer's rum stashed inside the Royal Caverns.",
        'title': 'Defeat EITC Thugs' },
    'dc4r1.3poisonNavy': {
        'description': 'Find the Officer rum barrels and add the poison given to you by the Casa de Muertos clan.',
        'title': 'Poison Rum Barrels' },
    'dc4r1.PoisonNavy': {
        'description': "There are two ways to get the Navy men off the Casa de Muertos' back and flat onto their own: defeating them, thinning the Navy ranks, and spiking their rum with a mild poison.",
        'stringAfter': 'Ha! Ha! Those Navy dogs will be puking their guts out...\x07...while we do our business! But yer not finished mate.\x07To collect your \x01slant\x01substantial\x02 reward, thar be more Navy men to vex... I mean poison.',
        'stringBefore': 'I have a task fer you... if ye be pirate enough, ey?\x07We needs the Navy, uh, \x01slant\x01indisposed\x02 while we do our business.\x07Savvy? So we need yer help putting a touch of \x01slant\x01medicine\x02 in their rum.\x07We will make it well worth yer troubles.',
        'title': 'Disable Navy Men' },
    'dc4r2.1poisonFortCharles': {
        'description': 'Navy Veterans guard the commoner rum barrels, often in pairs, so consider bringing along a mate.',
        'title': 'Defeat Veterans' },
    'dc4r2.2poisonFortCharles': {
        'description': "Drop the poison into the barrels when no one's looking - remember - this is a secret mission so once you're done, run like the wind!",
        'title': 'Poison Rum Barrels' },
    'dc4r2.PoisonFortCharles': {
        'description': 'Disabling Fort Charles is critical because of its strategic location and lookout posts.',
        'title': 'Disable Fort Charles Guards' },
    'dc5r1.1defeatNavy': {
        'description': "Vanguards - as you can tell by the name - are out front guarding the Navy's key interests and not just their rum.",
        'title': 'Sink Navy Vanguards' },
    'dc5r1.2defeatNavy': {
        'description': 'Send the pesky Navy Centurions to Davy Jones locker!',
        'title': 'Sink Navy Centurions' },
    'dc5r1.3defeatNavy': {
        'description': 'Sinking one of the Kingfisher ships will cause a lot of distruption inside the Navy fleet.',
        'title': 'Sink Navy Kingfisher' },
    'dc5r1.DefeatNavy': {
        'description': 'The stolen Navy defense papers say that three classes of Navy ships in particular need to be sunk to insure success for the Casa de Muertos brotherhood.',
        'stringBefore': "Hallo mate! Name's Dedman.\x07Wanna continue helping us, ey? Fine, fine, yes.\x07We'll start with the list you found earlier. The Navy manifest says that...\x07Vanguards, Kingfishers and Centurions are our best targets.\x07We needs those scabs out of the way to do our job. So...\x07STOP GAWKING AND GET TO THE DINGHY!!!",
        'title': 'Defeat Navy Ships' },
    'dc6.10visitJeremiah': {
        'animSetAfter': [
            None,
            65000,
            None,
            None,
            60602],
        'description': 'Jeremiah Dedman, another esteemed member of the Casa de Muertos Guild, is an expert at reading coded maps.',
        'stringAfter': "Sam sent you, eh? That means the map is for real.\x07Seems like efforts to silence the people that know about it failed, because by now, everyone knows about it!\x07The weapons are buried on a wretched island named Raven's Cove.\x07What I hear, the Navy and the EITC are already on their way!\x07Sink their ships to slow them down until we regroup!",
        'title': 'Jeremiah Dedman' },
    'dc6.12sinkPrizedShip': {
        'description': "The Ogre is the toughest, most well armed ship the EITC commands and if you don't sink it, the weapons will soon be in the hands of the double-dealing EITC.",
        'title': 'Sink Prized Ship' },
    'dc6.1duchamps': {
        'animSetAfter': [
            60640,
            None,
            None,
            65000],
        'description': 'Duchamps, the rum smuggler, is believed to have some inside knowledge about the lost weapons.',
        'stringAfter': "So, Rott sent you, he did.\x07You know he works for... the dark side.\x07If you're fine with it, so am I.\x07I be in it for the money. If you're smart, you should too.\x07A man I once knew said the weapons are buried right here on Padres.\x07But be warned, Lord Beckett is asking about them weapons, too.",
        'stringBefore': "So, you wanna work for Jolly Roger, do ya?\x07Don't be shy mate, you either works with Jolly, or against him.\x07Best to be on the winning side. Most folks refuse to talk.\x07And they will pay. First off, go see that scab smuggler, Duchamps.\x07I hear he has solid information.",
        'title': "Duchamps' Knowledge" },
    'dc6.2ezekielRott': {
        'animSetAfter': [
            60602,
            None,
            65000],
        'description': "Jolly Roger and the head of the EITC, Lord Cutler Beckett, have been working together to rid the Caribbean of the pirates. Now Beckett competes for these weapons because even a scoundrel like him doesn't want Jolly to get his boney hands on them!",
        'stringAfter': "He says Beckett's after the weapons too!\x07If it's true, the Casa de Muertos will have his head for this betrayal!\x07Find me proof and I'll tear him limb from limb!\x07Beckett's known to scatter his coded orders between many ships.",
        'title': 'Return to Ezekiel Rott' },
    'dc6.4visitNathan': {
        'animSetAfter': [
            None,
            60665],
        'description': 'Nathan Gould, another member of the dreaded Casa de Muertos Guild, has been spying on the Navy outside Fort Dundee on Padres.',
        'stringAfter': "Yes, this barrel is the place to be, eh?\x07Now, here's the skinny... the Navy's got their eye on the lost weapons too.\x07But no one seems to know where the weapons are stashed.\x07Steal some secret records for me to confirm all this.\x07And I'll make sure you're taken care of.",
        'title': 'Nathan Gould' },
    'dc6.7visitSamuel': {
        'animSetAfter': [
            None,
            65000],
        'description': "Samuel Shaw is posing as a common laborer in the EITC owned mines on Padres looking for clues on the whereabouts of El Patron's Lost Weapons.",
        'stringAfter': "Ahoy, so Nathan sent you, he did.\x07Good enough for me. Here's what I've dug up...\x07Beckett has sent his troops in here to find clues...\x07...of the exact location where El Patron's Lost Weapons are buried.\x07But you need to take out some of these soldiers so I can find these 'Excavation Records', eh?",
        'title': 'Samuel Shaw' },
    'dc6r11.1sinkExpedition': {
        'description': "Three top-level Navy Commanders are aboard the Kingfishers and must be sunk before reaching Raven's Cove.",
        'title': 'Kingfisher Ships' },
    'dc6r11.2sinkExpedition': {
        'description': 'Three high-level EITC Officers with gold enough to bribe the entire Caribbean are aboard the Marauders and must be sunk.',
        'title': 'Marauder Ships' },
    'dc6r11.SinkExpedition': {
        'animSetAfter': [
            60640,
            None,
            None,
            None,
            60657],
        'description': "The expedition to find the lost weapons has already left the port and must be stopped! Sink all the ships that make up this armada bound for Raven's Cove.",
        'stringAfter': "Sent them to Davy Jones' locker, ya did!\x07Now, there's but one small bit of sinking left to do...\x07...an EITC Ogre that carries all the troops.\x07But for a pirate like you, shouldn't be a problem, and...\x07...I will make it worth your while.",
        'title': "Raven's Cove Island Expedition" },
    'dc6r3.1getInfo': {
        'description': "Navy Vanguard ships hold three of the coded messages but you'll have to sink them before the Captain will give them up!",
        'title': 'Navy Coded Orders' },
    'dc6r3.2getInfo': {
        'description': "Beckett's direct orders specifying his plans are on two Bloodhound ships. Sink them to recover the orders.",
        'title': 'EITC Coded Orders' },
    'dc6r3.GetInfo': {
        'animSetAfter': [
            None,
            60602,
            None,
            None,
            65000],
        'description': "Lord Beckett is a crafty old fox and wrote out his true intentions in a series of messages to the Navy and put them on several different ships. Without all of them, you'll never crack the code and prove Beckett's betrayal.",
        'stringAfter': "This confirms it. Beckett is tryin' to snatch the weapons first.\x07Me boss does not like being double crossed!\x07Tell you what mate... Let's find out who else wants those weapons.\x07Go find Nathan Gould, hanging 'round Fort Dundee.\x07See if he's got any more scuttlebutt info.",
        'title': 'Recover Information' },
    'dc6r5.1gatherInfo': {
        'description': "Some secret documents are scattered around Navy Veterans that tell of the Navy's efforts to find the weapons. Now you must find and recover them.",
        'title': 'Secret Records' },
    'dc6r5.2gatherInfo': {
        'description': 'The final bits of intelligence found in these documents will help you piece together exactly what the Navy knows... and their intentions.',
        'title': 'Guarded Intelligence' },
    'dc6r5.GatherInfo': {
        'animSetAfter': [
            60654],
        'description': "On direction from Jolly Roger himself, the Casa de Muertos Guild has been spying on the EITC and the Navy, hoping to find out information about El Patron's Lost Weapons and how to get their hands on it first.",
        'stringAfter': "Ahhh!! What's this!? We've been discovered!\x07The Navy knows we've been spying and now...\x07They've sent word for reinforcements!\x07Stop them! Intercept the ships carrying those orders, now!",
        'title': 'Gather Information' },
    'dc6r6.1interceptMessages': {
        'description': 'Find and destroy the messages outlining the Casa de Muertos spy efforts.',
        'title': 'Intercept the Navy Messages' },
    'dc6r6.2interceptMessages': {
        'description': 'The Officers on Padres sent messages to the Navy headquarters and to Sir Cutler Beckett, head of the EITC.',
        'title': 'Intercept the EITC Messages' },
    'dc6r6.InterceptMessages': {
        'animSetAfter': [
            None,
            60665],
        'description': 'Ships carrying the details of the Casa de Muertos Guild plot to find the weapons are already on their way to Navy officials on Port Royal.',
        'stringAfter': 'Well done, mate. Now we can continue to spy as needed.\x07Next task? Find ole Sam Shaw, another member of our esteemed guild, to see what he knows.',
        'title': 'Intercept Messages' },
    'dc6r8.1defeatResistance': {
        'description': 'Some Navy Officers got word from their spies to be on the lookout for the Casa de Muertos Guild. Defeat them before they arrest Samuel Shaw.',
        'title': 'Navy Opposition' },
    'dc6r8.2defeatResistance': {
        'description': 'EITC Hired-guns are about to close in on Shaw and must be defeated first!',
        'title': 'EITC Opposition' },
    'dc6r8.3defeatResistance': {
        'description': "Sam Shaw overheard some men muttering about 'Excavation Records', a detailed account of everything unearthed in the mines. He needs these to complete his mission.",
        'title': 'Excavation Records' },
    'dc6r8.DefeatResistance': {
        'animSetAfter': [
            60614],
        'description': "Some of the Navy and EITC men suspect the Shaw's up to no good and have been getting too close for comfort.",
        'stringAfter': "Well done, mate. These excavation records tell of everything they've uncovered in here.\x07And there's... a map.\x07Find the map and defeat everyone that knows of it.",
        'title': 'Defeat Resistance' },
    'dc6r9.1disruptDefenses': {
        'description': 'These highly skilled, battle hardened Mercenaries guard the map and must be defeated!',
        'title': "Defeat Beckett's Mercenaries" },
    'dc6r9.2disruptDefenses': {
        'description': 'Dragoons are some of the fiercest fighters in the Navy and some know of the secret map.',
        'title': 'Defeat Navy Dragoons' },
    'dc6r9.3disruptDefenses': {
        'description': "The talk among the Navy and EITC Intelligence Officers is that Padres is not the final resting place of El Patron's Lost Weapons. They suspect a map hidden here reveals the location.",
        'title': 'The Lost Map' },
    'dc6r9.DisruptDefenses': {
        'animSetAfter': [
            60668],
        'description': "Samuel Shaw of the Casa de Muertos clan need you to recover a special map and defeat those men knowing about it. This meticulous map holds the secret location to the El Patron's Lost Weapons.",
        'stringAfter': "Excellent work, mate. Jolly will be delighted!\x07Now we can get those weapons!\x07If only I could read it. It's written in code. Take the map to Jeremiah Dedman.",
        'title': 'The Secret Map' },
    'dd.1crewtutorial': {
        'description': 'Learn How To Form A Crew And Set Sail',
        'stringBefore': "The high seas are a dangerous place. That's why any Captain worth his salt needs a good crew. \x07Go, and find somebody to join your crew.",
        'title': 'Darby Teaches About Crew Members' },
    'dd.2crewtutorial': {
        'description': 'Find A Crew Member',
        'title': 'Find Crew' },
    'dd.3crewtutorial': {
        'description': 'Have Your Crew Member Board A Ship',
        'title': 'Board The Ship' },
    'dd.4crewtutorial': {
        'description': 'Add Your Crew Member To Your Friends List',
        'title': 'Make Friends' },
    'dd1.recovercloth': {
        'description': 'Sink a ship in order to acquire sail cloth.',
        'stringAfter': 'Nice doing business with ye, mate.',
        'title': 'Acquire Cloth for a Sail' },
    'dd1.recovercopper': {
        'description': 'Sink ships in order to acquire a copper rod.',
        'stringAfter': 'The last thing I need is cloth for ship sails.',
        'title': 'Acquire Copper Rod' },
    'dd1.recoveriron': {
        'description': 'Sink ships in order to acquire iron bars.',
        'stringAfter': "Good job. Now, acquire a copper rod and I'll pay ye well for it.",
        'title': 'Acquire Iron Bars' },
    'dd1.recoverwood': {
        'description': 'Sink ships in order to acquire wood planks.',
        'stringAfter': "That's a good start. Next, return with an iron bar.",
        'stringBefore': "Lookin' for work, are ye?\x07I be lookin' to build a new ship and have need of parts for this.\x07Let's start with ye bringing me back some wood planks.",
        'title': 'Acquire Wood Planks' },
    'dm1.defeatEITCShips': {
        'description': 'Dajin Ming has contracted you to sink EITC ships containing the cargo of his competitors.',
        'stringAfter': "You made short work of that, I'm impressed.\x07Dajin will want to talk with you, he has some new problems that you could help with.",
        'title': 'Risky Business' },
    'dm1.defeatNavyShips': {
        'description': 'Dajin Ming has caught the attention of the Navy with his business practices. He needs you to sink some of their fleet to get their attention off of him.',
        'stringAfter': 'Perfect! That should serve as a suitable distraction from my business.\x07Orinda is holding the piece of jewelry I promised to you.\x07I am sure it will serve as a proper reward, cheers!',
        'title': 'Distracting The Navy' },
    'dm1.sinkEITCShipA': {
        'description': "Sink a EITC Corvette that is carrying the cargo of one of Dajin Ming's competitors.",
        'title': 'EITC Corvette cargo' },
    'dm1.sinkEITCShipB': {
        'description': "Sink a EITC Sea Viper that is carrying the cargo of one of Dajin Ming's competitors.",
        'title': 'EITC Sea Viper cargo' },
    'dm1.sinkEITCShipC': {
        'description': "Sink a EITC Marauder that is carrying the cargo of one of Dajin Ming's competitors.",
        'title': 'EITC Marauder cargo' },
    'dm1.sinkEITCShipD': {
        'description': "Sink a EITC Barracuda that is carrying the cargo of one of Dajin Ming's competitors.",
        'title': 'EITC Barracuda cargo' },
    'dm1.sinkFirstEITCShip': {
        'description': 'Orinda wants to test you out by destroying one of the target EITC ships. If you succeed, she will provide you with the full list.',
        'stringAfter': "Blimey, you're alive! I must admit I had me doubts.\x07This list will be a bit longer, but I'm sure you can handle it.",
        'title': 'Testing The Waters' },
    'dm1.visitDajinMing': {
        'description': 'Orinda wants you to inform Dajin of your progress. He also has some new problems for you to handle.',
        'stringAfter': "You seem to have handled yourself quite well out there, too bad EITC isn't the only problem.\x07Turns out the Navy doesn't take kindly to my business practices.\x07Give them something else to worry about and you will be rewarded well.",
        'title': 'Returning To Dajin' },
    'dm1.visitJohnnyMcvane': {
        'description': 'Dajin Ming is asking for your services while his partner is away. Go speak with Johnny McVane to learn more about what needs to be done.',
        'stringAfter': "So Dajin has picked you to help out while his partner is away?\x07We have a bit of a partnership ourselves you know.\x07Some of Dajin's business isn't exactly legit you see.\x07Dajin's partner contracted me to arrange some raids on EITC ships roaming around Tortuga.\x07These ships contain the cargo of some of his competitors.\x07In the absence of his partner, you will be leading up these raids.\x07Go speak to Orinda Le Jeune by the docks and she will provide you with the targets.",
        'stringBefore': 'I could show you our normal items...\x07Or I could show you something a bit more rare.\x07If you would be interested that is. All I ask is that you assist with some small tasks.\x07See, my old partner has not shown up for weeks and I fear the worse.\x07Help me with his duties and I will give you something I normally hold for my richer clients.',
        'title': 'Picking Up The Slack' },
    'dm1.visitOrindaLeJeune': {
        'description': "Johnny McVane has informed you that Orinda Le Juene will provide you with a list of target EITC ships. These ships contain competitor's jewelry cargo that Dajin Ming wants destroyed.",
        'stringAfter': "So, here to sink some EITC ships, you are?\x07Best be careful so you do not end up like Dajin's partner.\x07Why don't we start with one, if you make it back alive, there will be more.",
        'title': 'EITC Jewelry Raids' },
    'dm1.visitOrindaLeJeune2': {
        'description': 'Orinda is holding on to your payment. Go visit her at the docks to pick it up.',
        'title': 'Collecting Payment' },
    'dm2.defeatEITC': {
        'description': 'Dajin Ming wants you to send a message to the EITC to force them off of the jewelry trade in Tortuga.',
        'title': 'Sending a message' },
    'dm2.deliverCoinBag': {
        'description': "Boatswain Bill needs you to take care of some of his duties. Deliver Big Phil's payment to him and take care of whatever work he needs done.",
        'stringAfter': "It's about time Boatswain Bill decided to pay up.\x07I see he decided not to include interest, I guess you'll be working it off then?\x07My business is livestock, bring me some chickens and pigs and that should cover it.",
        'title': 'Delivering Payment' },
    'dm2.deliverContract': {
        'description': 'Boatswain Bill has signed a contract stating he will not open a jewelry shop in Tortuga. Deliver this to Dajin Ming.',
        'stringAfter': "Hah... Boatswain Bill folded pretty easily.\x07Maybe my shop isn't doomed.\x07This doesn't cover our EITC problems though.\x07They obviously have some intentions of closing me down.\x07Send them a message for me and I will reward you well.",
        'title': 'Jewelry Contract' },
    'dm2.deliverShopApplication': {
        'description': 'Return the shop application you recovered to Dajin Ming. It holds the identity of who is opening the new jewelry shop.',
        'stringAfter': 'Boatswain Bill? What business does he have opening up a jewelry shop?\x07I need to do whatever I can to prevent him from opening his shop.\x07I cannot compete with his partnership with the EITC.\x07Go speak with him and see if there is a comprise we can come to.',
        'title': 'Shop Application' },
    'dm2.recoverAlligatorHides': {
        'description': "To clear out Boatswain Bill's obligations to Seamstress Anne, she wants you to bring her some fresh alligator hides.",
        'title': 'Alligator Hides' },
    'dm2.recoverBatHides': {
        'description': "To clear out Boatswain Bill's obligations to Seamstress Anne, she wants you to bring her some fresh bat hides.",
        'title': 'Bat Hides' },
    'dm2.recoverChickens': {
        'description': 'To cover the interest owed to Boatswain Bill, he has requested that you gather chickens for his business.',
        'title': 'Chicken Interest' },
    'dm2.recoverCoinBag': {
        'description': "Recover Big Phil's payment before delivering it to him. It can be found in a desk in Boatswain Bill's house.",
        'title': "Phil's Payment" },
    'dm2.recoverFarmAnimals': {
        'description': 'Big Phil has requested that you gather some livestock for his business in order to cover the interest owed to him by Boatswain Bill.',
        'stringAfter': 'Some fine livestock.\x07This should cover the interest, inform Boatswain Bill that his debt to me is gone.',
        'title': "Phil's Farm Animals" },
    'dm2.recoverFlyTrapHides': {
        'description': "To clear out Boatswain Bill's obligations to Seamstress Anne, she wants you to bring her some fresh fly trap hides.",
        'title': 'Fly Trap Hides' },
    'dm2.recoverHides': {
        'description': "To clear out Boatswain Bill's obligations to Seamstress Anne, she wants you to bring her some fresh animal hides.",
        'stringAfter': 'I hope you did not get injured gathering these. Better you than me though.\x07Tell Boatswain Bill he can show his face around here. Take care.',
        'title': "Anne's Hides" },
    'dm2.recoverPigs': {
        'description': 'To cover the interest owed to Boatswain Bill, he has requested that you gather pigs for his business.',
        'title': 'Pig Interest' },
    'dm2.recoverShopApplication': {
        'description': 'Help Dajin Ming recover the application in order to find the identity of the new shop owner. The application can be found in a desk in the EITC fort in Thieves Den.',
        'stringBefore': 'Seems EITC is backing a new jewelry shop in Tortuga.\x07Tolerating competitors has never been my best quality.\x07Find the shop application so we can find out who is planning this shop.\x07The applications are normally stored in a desk in the EITC fort in Thieves Den.',
        'title': 'Eliminating The Competition' },
    'dm2.visitBoatswainBill': {
        'description': 'Boatswain Bill, along with EITC support, is planning to open a new jewelry shop in town. Meet with Boatswain Bill and see if there is a way to prevent him from opening his shop.',
        'stringAfter': "That's a very lucrative offer ye be asking me to turn down.\x07The EITC doesn't align itself very often with the likes of me.\x07Of course better deals always come along, don't they?\x07If ye can take care of some of me duties, I'll agree to back out of the new shop.\x07First, I owe a bit of money and work to Big Phil, take care of this for me to start.\x07The payment be found in me desk.",
        'title': 'Compromised Business' },
    'dm2.visitBoatswainBill2': {
        'description': "Boatswain Bill's obligations to Big Phil are complete. Inform him of your progress.",
        'stringAfter': "Avoiding Phil was getting a bit old. Guess it was about time I paid up.\x07Seamstress Anne has also been pestering me. Turns out me last payment to her was a tad short.\x07You will have to work off that debt to her as well, me funds aren't what they used to be.",
        'title': 'Money Owed' },
    'dm2.visitBoatswainBill3': {
        'description': 'Boatswain Bill no longer has any financial obligations to Seamstress Anne. Inform him of your progress.',
        'stringAfter': 'Walking around town will no longer be a game of dodging people I owe.\x07Dajin Ming can stay as the sole jeweler in Tortuga for now.\x07Bring him this contract I signed. It should be enough to quiet his concerns.',
        'title': 'Finished Obligations' },
    'dm2.visitDajinMing': {
        'description': 'visitDajinMing description',
        'stringAfter': 'visitDajinMing stringAfter',
        'stringBefore': 'visitDajinMing stringBefore',
        'title': 'visitDajinMing title' },
    'dm2.visitSeamstressAnne': {
        'description': 'Boatswain Bill owes Seamstress Anne for some purchases he did not pay for. He needs you to work off the debt for him. Visit her to find out what needs to be done.',
        'stringAfter': "What do you want? Can't you see that I'm working?\x07Boatswain Bill has owed me for months. I figured he wasn't going to pay up.\x07There's not much I need besides fabric and animal hides.\x07Bring me some fresh hides for my shop and we'll call it even.",
        'title': 'Seamstress Issues' },
    'dul5.10.5bribeGrimm': {
        'description': 'Bribe the jailer for information about the daggers.',
        'stringAfter': "Thanks much, mate.  I buried the daggers here on Port Royal somewhere 'round the Governors mansion.\x07Don't know where exactly seeing as how I was full of grog at the time.  Cheers!",
        'title': 'Bribe Ensign Grimm' },
    'dul5.10visitGrimm': {
        'description': 'Ensign Grimm is passing the time pretending to do his duty guarding the Port Royal jail.',
        'stringAfter': "Why should I tell you, you filthy pirate?!  Hey, sorry about the remark,  you seem like a decent chap.\x07But I needs some gold coins to loosen my tongue.  Slip me a proper sum and I'll tell ya where I buried the goods.  Honest.",
        'title': 'Visit Ensign Grimm' },
    'dul5.11findDaggers': {
        'description': "Look for a green circle around the Governor's Mansion.  Once found, return the daggers to Ferrera.",
        'title': 'Excavate Stolen Daggers' },
    'dul5.12visitFerrar': {
        'description': 'Return to Ferrera on Padres Del Fuego.',
        'title': 'Visit Ferrera' },
    'dul5.1visitFerrar': {
        'description': 'Ferrera can be found in his shop in Padres Del Fuego.',
        'stringAfter': "Daggers? Just made a few but some bilge rat stole 'em.  Not sure who, you'll have to help.\x07If you return them, one's yours. Start off by finding a necklace that once belonged to my friend - Orinda on Port Royal.\x07Gov. Swann stole it and buried it in the Governor's Garden.\x07Find her necklace and maybe that will loosen up her tongue and lead you to the daggers.  Fair winds!",
        'title': 'Visit Ferrera' },
    'dul5.2findNecklace': {
        'description': "The Governor's Garden is behind Swann's mansion on Port Royal.  Be careful digging because its haunted by the undead and patrolled by Navy Guards.",
        'title': "Orinda's Necklace" },
    'dul5.3visitOrinda': {
        'description': 'Orinda can be found on the docks of Tortuga.',
        'stringAfter': "My necklace, at last! Now I can pay me debts.\x07But before I tell you what I know, I need a favor.\x07My late husband Timothy is now in Jolly Roger's undead army.  Find the poor bloke and put him out of his misery!\x07That'll make me-talkative.",
        'title': 'Visit Orinda' },
    'dul5.4defeatExHusband': {
        'description': 'Undead Timothy Dartan can be found on the dangerous, abandoned village on the far side of Padres Del Fuego.',
        'stringAfter': "Many thanks, mate.\x07Now go to Cuba and find Billy McKidd.  He's well informed about such matters.\x07He's almost always in the La Bodeguita Tavern, drinkin' and talkin' to anyone who'll listen.",
        'title': 'Defeat Timothy Dartan' },
    'dul5.5visitMcKidd': {
        'description': 'Find Billy McKidd telling his tall tales in the Cuban Tavern named, La Bodeguita.',
        'stringAfter': "Tell you where the daggers are?  What's in it for me?\x07Here's a plan-Find me old Navy boss, Captain Swain, or swine as I like to call him.  Find that pig and maroon him on a wild island.\x07Yeah, then I'll give you an answer.  Now shove off!",
        'title': 'Visit Billy McKidd' },
    'dul5.6captureSwain': {
        'description': "Find Navy Captain Swain and maroon him on the closest wild island.  It's more kindness than he deserves!",
        'title': 'Capture Captain Swain' },
    'dul5.7maroonSwain': {
        'description': "Find Navy Captain Swain and maroon him on the closest wild island.  It's more kindness that he deserves!",
        'stringAfter': "Back so soon? Blimey, you're good.\x07  I know who knows about the stolen daggers.  Tia Dalma.\x07 But don't tell her I sent you.  That witch despises me.",
        'title': 'Maroon Captain Swain' },
    'dul5.8visitTia': {
        'description': 'Tia Dalma makes her home in the swamps of Cuba.',
        'stringAfter': "Yes, I know who stole da daggers but I ain't tellin' without no gift.\x07Do a favor for Tia first - find an undead witchdoctor name of Bonerattler who's been vexing me spirits.\x07Get rid of him and I tell you who stole da daggers.  Hurry now. It's your destiny!",
        'title': 'Visit Tia Dalma' },
    'dul5.9defeatWitchdoctorBoss': {
        'description': 'Bonerattler was last seen in the Catacombs on Padres.  Watch your back!  He has lots of friends.',
        'stringAfter': 'I thank you, and so do my  spirits.  Da man who stole da daggers guards the jail on Port Royal.\x07A pitiful thieving Navy man named, Grimm, Ensign Grimm.',
        'title': 'Defeat Bonerattler' },
    'familyPaintings': {
        'description': "You have found the locations of Solomon O'Dougal's paintings. Recover them for him and he will reward you with a rare tattoo.",
        'stringAfter': 'I never thought I would see these paintings again, thank you.\x07Before you go, could you deliver this painting to my cousin?\x07His name is Jim Wavemonger and you should be able to find him in a Port Royal mine named Royal Caverns.',
        'title': 'Buried Portraits' },
    'french.ShipPVPMainLadder': {
        'description': 'Pierre le Porc has accepted you as one of his French recruits. Complete his challenges for you to prove your worth and skill to him.',
        'stringAfter': 'Well, it appears as though there is not much more I can teach you for now.\x07You have proven yourself to be a fine soldier. France thanks you dearly.\x07You can now also wear the mark of the French! Go to any Tattoo Artist for a tattoo only my finest pirates have.\x07Check back with me in the future. I may just have more for you to do.',
        'title': 'Fight for the French!' },
    'french.ShipPVPTaskA': {
        'description': 'Pierre le Porc wants you to damage Spanish ships as the start of his challenges for you.',
        'stringAfter': "Nice work, my friend. These waters can be quite unforgiving.\x07Dealing just plain damage to the Spanish is easy though. I think you are in need of something a bit more challenging.\x07Before, you were not given any restrictions aside from fighting in the name of France.\x07This time, I want you to target ships specifically.\x07To make it even more interesting, let's have you do it with your ship and a cannon. Is that enough for you?",
        'stringBefore': "So, I see you think you are good enough to join the fight. The French are proud to have you!\x07Many of my finest soldiers started out as scrappy pirates such as yourself.\x07I put all my fresh recruits through a gauntlet of challenges, some even make it through to the end.\x07Let's start you off with something light to get your feet wet.\x07Don't forget though, using a dinghy on this island will throw you right into battle and you will only be able to dock at this island.\x07If you have a desire to visit those scurvy Spanish pirates, be sure to teleport to their miserable excuse for an island. ",
        'title': 'Getting Your Feet Wet' },
    'french.ShipPVPTaskB': {
        'description': 'As your next challenge, Pierre le Porc wants you to sink Spanish ships using only your ship skills.',
        'title': 'Sailing Skills' },
    'french.ShipPVPTaskB_C': {
        'description': 'Pierre le Porc wants to give you a challenge after your first task. Sink Spanish ships using only your ship.',
        'stringAfter': "Good show! So far I must say you have exceeded my expectations. Unfortunately my next challenge may not be as forgiving.\x07Any of my soldiers can take to the seas and sink a Spanish ship or two eventually.\x07It takes true skill to do it without sinking though. Not much celebrating a pirate can do after sinking you know.\x07Let's see you take down some Spanish ships without sinking that fancy boat of yours.\x07You'll loose credit for Spanish ships sunk if you do. Give the cannon a rest also. Use only your ship for this challenge.",
        'title': 'Specific Targets' },
    'french.ShipPVPTaskC': {
        'description': 'As your next challenge, Pierre le Porc wants you to sink Spanish ships using only your cannon skills.',
        'title': 'Cannon Skills' },
    'french.ShipPVPTaskD': {
        'description': 'Pierre le Porc wants to see if you can target Spanish pirates using only your ship skills.',
        'title': 'Broadsides For Pirates' },
    'french.ShipPVPTaskD_E': {
        'description': 'Pierre le Porc wants to see if you can target Spanish pirates using your ship and cannon skills.',
        'stringAfter': "I can almost hear those scurvy Spanish pirates whimpering. Good show!\x07So far I must say you have exceeded my expectations. Unfortunately my next challenge may not be as forgiving.\x07Any of my soldiers can take to the seas and sink a Spanish ship or two eventually.\x07It takes true skill to do it without sinking though. Not much celebrating a pirate can do after sinking you know.\x07Let's see you take down some Spanish ships without sinking that fancy boat of yours.\x07You'll loose credit for Spanish ships sunk if you do. Give the cannon a rest also. Use only your ship for this challenge.",
        'title': 'Unlucky Spanish Pirates' },
    'french.ShipPVPTaskE': {
        'description': 'Pierre le Porc wants to see if you can target Spanish pirates using only your cannon skills.',
        'title': 'Cannons For Pirates' },
    'french.ShipPVPTaskF': {
        'description': 'Pierre le Porc wants you to sink Spanish ships using only your ship skills. He wants you to do this without sinking your ship.',
        'stringAfter': "I bet those Spanish misfits are starting to worry. If only I had more soldiers like you.\x07Keep it up and we will have these islands in no time.\x07I think it is time you dust off that cannon. Let's see you take down some more Spanish ships without sinking.\x07This time though, use only your cannon skills to do it. Good luck.",
        'title': 'Sinking Is Easy' },
    'french.ShipPVPTaskG': {
        'description': 'Pierre le Porc wants you to sink Spanish ships using only your cannon skills. He wants you to do this without sinking your ship.',
        'stringAfter': 'Very impressive my friend. I hear Garcia shaking in his boots as we speak.\x07If we hit them hard now, we might just be able to tip this battle in our favor.\x07Use the skills you have gained to deal a large amount of damage to Spanish ships using your ship and your cannon skills.',
        'title': 'Cannon Streak' },
    'french.ShipPVPTaskH': {
        'description': 'Pierre le Porc wants you to defeat Spanish pirates using only your ship skills. He wants you to do this without sinking your ship.',
        'stringAfter': 'Finally, some decent progress being made around here! Nothing like the smell of fresh French gunpowder.\x07I hope you did not wear out a broadside or two. This time I will have you use only your cannon again.\x07Defeat some more Spanish pirates using only your cannon skills and of course, do it without sinking.',
        'title': 'Pirate Broadside Streak' },
    'french.ShipPVPTaskI': {
        'description': 'Pierre le Porc wants you to defeat Spanish pirates using only your cannon skills. He wants you to do this without sinking your ship.',
        'stringAfter': 'Very impressive my friend. I hear Garcia shaking in his boots as we speak.\x07If we hit them hard now, we might just be able to tip this battle in our favor.\x07Use the skills you have gained to deal a large amount of damage to Spanish ships using your ship and your cannon skills.',
        'title': 'Pirate Cannon Streak' },
    'french.ShipPVPTaskJ': {
        'description': 'Pierre le Porc wants you to deal a large amount of damage to Spanish ships using only your ship.',
        'title': 'Massive Ship Damage' },
    'french.ShipPVPTaskJ_K': {
        'description': 'Pierre le Porc wants you to deal a large amount of damage to Spanish ships using your ship and cannons.',
        'stringAfter': 'At times like this I think this battle will never end. Gacria and his Spanish pirates matched your efforts and more.\x07We need a grand display of destruction if we are to hold this island.\x07Head to the seas. A great deal of ship damage against the Spanish onslaught without sinking should put them back in their place.',
        'title': 'Massive Damage' },
    'french.ShipPVPTaskK': {
        'description': 'Pierre le Porc wants you to deal a large amount of damage to Spanish ships using only your cannons.',
        'title': 'Massive Cannon Damage' },
    'french.ShipPVPTaskL': {
        'description': 'Pierre le Porc wants you to use your ship to deal a large amount of damage to Spanish ships without sinking.',
        'stringAfter': 'Glorious! I believe that almost did the job.\x07Each time those Spanish swine launch an attack we need to ensure our response is fitting.\x07Finish our response by dealing more damage to Spanish ships without sinking. This time though, use only your cannon.',
        'title': 'Ship Damage Streak' },
    'french.ShipPVPTaskM': {
        'description': 'Pierre le Porc wants you to use your cannons to deal a large amount of damage to Spanish ships without sinking.',
        'stringAfter': 'At last, we are starting to see a difference out there! Your efforts have proven to be one of a well trained soldier.\x07Hopefully next time they attack, I will have you at my disposal.\x07You are nearing the end of my challenges, but as always, I have saved the hardest for last.\x07Show me you are as good as I think you are. Defeat a large amount of Spanish ships. Feel free to use any means to do so.',
        'title': 'Cannon Damage Streak' },
    'french.ShipPVPTaskN': {
        'description': 'Pierre le Porc wants you to sink a large amount of Spanish ships. You can use any means to do so.',
        'stringAfter': 'Well mon amie, our time together is coming to an end, for now.\x07I have only one more challenge for you, one that I save for my most talented recruits.\x07Accomplish this challenge and you will be forever honored in the hearts of Frenchmen everywhere.',
        'title': 'Ships In Bulk' },
    'french.ShipPVPTaskN_O': {
        'description': 'Pierre le Porc wants you to defeat a large amount of Spanish ships and Spanish pirates. You can use any means to do so.',
        'stringAfter': 'Well mon amie, our time together is coming to an end, for now.\x07I have only one more challenge for you, one that I save for my most talented recruits.\x07Accomplish this challenge and you will be forever honored in the hearts of Frenchmen everywhere.',
        'title': 'Bulking Up' },
    'french.ShipPVPTaskO': {
        'description': 'Pierre le Porc wants you to defeat a large amount of Spanish pirates. You can use any means to do so.',
        'title': 'Pirates In Bulk' },
    'french.ShipPVPTaskP': {
        'description': 'As your final challenge, Pierre le Porc wants you to deal a large amount of damage to Spanish ships without sinking.',
        'title': 'A True Frenchman' },
    'jm1.1recoverrumbarrels': {
        'description': 'Sink ships in order to acquire rum barrels.',
        'stringAfter': 'We need some whiskey too.',
        'stringBefore': "Could ye be a dear and help me restock? \x07We be runnin' terribly short on rum.",
        'title': 'Acquire Rum Barrels' },
    'jm1.3recoverwhiskeybarrels': {
        'description': 'Sink ships in order to acquire whiskey barrels.',
        'stringAfter': "We've lost a lot of glasses with all of the brawlin' in here. \x07Be a dear and fetch me some new ones.",
        'title': 'Acquire Whiskey Barrels' },
    'jm1.5recoverglasses': {
        'description': 'Sink ships in order to acquire a set of bar glasses.',
        'stringAfter': 'Now I just need to re-supply me sweetener. Honey should do.',
        'title': 'Acquire Bar Glasses' },
    'jm1.7recoverhoney': {
        'description': 'Sink ships in order to acquire honey barrels.',
        'stringAfter': 'Thanks for the help, me darlin.',
        'title': 'Acquire Honey Barrels' },
    'js1.defeatBinghamListA': {
        'description': "Bingham needs you to defeat some skeletons as part of the Navy's daily rounds.",
        'title': 'Skeleton Hunt' },
    'js1.defeatBinghamListB': {
        'description': "Bingham needs you to defeat some scorpions as part of the Navy's daily rounds.",
        'title': 'Scorpion Hunt' },
    'js1.defeatBinghamListC': {
        'description': "Bingham needs you to defeat some bats as part of the Navy's daily rounds.",
        'title': 'Bat Hunt' },
    'js1.defeatBinghamListD': {
        'description': "Bingham needs you to defeat some wasps as part of the Navy's daily rounds.",
        'title': 'Wasp Hunt' },
    'js1.defeatBinghamListE': {
        'description': "Bingham needs you to defeat some alligators as part of the Navy's daily rounds.",
        'title': 'Alligator Hunt' },
    'js1.defeatBinghamsList': {
        'description': "The Navy is having you take care of some of their daily duties as part of paying off Jeweler Smitty's debt.",
        'stringAfter': "Well,  I did not expect to see you so soon.  Don't worry, though.  I have more for you.\x07I owe some favors to a fellow named Jim Wavemonger.\x07He is expecting you.  Go see him and come back to me when he is done with you.",
        'title': 'Navy Rounds' },
    'js1.defeatWarmongerListA': {
        'description': 'Jim Wavemonger needs you to gather some copper rods so he and others can extend their camp.',
        'title': 'Stealing Copper' },
    'js1.defeatWarmongerListB': {
        'description': 'Jim Wavemonger needs you to gather some oil so he and others can extend their camp.',
        'title': 'Stealing Oil' },
    'js1.defeatWarmongerListC': {
        'description': 'Jim Wavemonger needs you to gather some steel rods so he and others can extend their camp.',
        'title': 'Stealing Steel' },
    'js1.defeatWarmongerListD': {
        'description': 'Jim Wavemonger needs you to gather some coal so he and others can extend their camp.',
        'title': 'Stealing Coal' },
    'js1.defeatWavemongersList': {
        'description': 'Jim Wavemonger needs you to gather some supplies so he and others can extend their camp. Destroy EITC ships and gather the needed supplies.',
        'stringAfter': 'Nice work, mate. Bingham expressed his doubts but it seems like you handled yourself well.\x07Inform Bingham that his obligations to me are gone.\x07Now scram! Let me get back to my beauty sleep.',
        'title': 'Building Supplies' },
    'js1.visitBingham': {
        'description': 'Jeweler Smitty has built up some debt playing poker with the Navy. As he cannot pay, they have decided to have him work off the debt. He has asked you to help work off the rest of the debt.',
        'stringAfter': "So, Smitty is having you handle the rest of his debts,  is he?\x07I hope you're more talented than him at a poker table...\x07Here is part of what Smitty needs to finish. Do not mess it up.",
        'stringBefore': 'Unfortunately I seem to have taken on a bit of debt from the local Navy.\x07One cannot be too careful at the poker tables you know.\x07Seeing as I cannot pay them, they have chosen to have me work it off.\x07If you could help me with some of the jobs, I would be willing to part with some of my finest wares.\x07Visit Bingham and he will tell you what is left to clear out the debt.',
        'title': "Smitty's Debt" },
    'js1.visitBingham2': {
        'description': 'Meet with Bingham and inform him of your progress with Jim Wavemonger.',
        'stringAfter': "Finally, I was starting to think you gave up.\x07Smitty's lucky he found you, inform him that his debts with me are paid.",
        'title': 'Checking In With Bingham' },
    'js1.visitJewelerSmitty': {
        'description': "Jeweler Smitty's debts with the Navy are now gone. Return to him to inform him of the news and to collect your payment.",
        'title': 'Taking Care Of Business' },
    'js1.visitJimWavemonger': {
        'description': "Bingham owes some favors to Jim Wavemonger.  As part of paying off Smitty's debt,  he wants you to handle them.  Jim Wavemonger can be found in a mine in Port Royal named Royal Caverns.",
        'stringAfter': "What?! Oh, sorry, you startled me. I don't get many chances to take a nap.\x07Bingham wants you to take care of his obligations to me? Sounds like him.\x07I guess it makes no difference to me who does what.\x07As you can tell, resources are a bit sparse here.\x07We'll need some building supplies in order to extend the camp. We also would rather not pay.\x07Take down some EITC ships and recover some building supplies and Bingham will be square with me.",
        'title': 'Navy Obligations' },
    'js2.bribeEdward': {
        'description': 'Edward Shackleby knows where the medical supplies you need can be found. Bribe him so you can get this information from him.',
        'stringAfter': 'All of these medical supplies you need can be found on EITC ships.\x07The supplies are not coming here though, instead most are being sent to the rich.\x07A bit unfair for the poor folk around Port Royal, but that is why there are pirates like yourself.',
        'title': 'Hidden Costs' },
    'js2.defeatNavyGuards': {
        'description': 'The message delivered to Edward Stomhawk is a list of orders from when he was a mercenary. Having retired, he needs you to finish the job.',
        'title': 'Mercenary Duties' },
    'js2.deliverBloodSample': {
        'description': 'Jeweler Smitty has seen several doctors to address his illness and none have helped. Bring his blood sample to Lucinda to see if there is something she can do.',
        'stringAfter': 'There has been one wicked sickness going around this island.\x07Pirates have been returning from sea with the same symptoms.\x07Unfortunately I do not have the necessary supplies here to help.\x07Go speak with Edward Shackleby, he will know where to get what you need.',
        'title': 'Blood Run' },
    'js2.deliverList': {
        'description': "To cure Smitty's illness, you need to acquire some medical supplies Lucinda does not have. Deliver a list of medical supplies to Edward Shackleby, he can tell you were to find what you need.",
        'stringAfter': "Hmmfff... Sorry, just catching up on some sleep.\x07These supplies will be hard to come by.\x07EITC shipments have been moving slowly since the illness broke out.\x07Normally I would retrieve these items for you, at a cost of course.\x07But I am not going to risk catching what has been going around.\x07At least make it worth my time and I'll tell you where to find these items.",
        'title': 'Dire Needs' },
    'js2.deliverMessage': {
        'description': "Having forgotten about the chest, Smitty's message to Edward Stormhawk was never delivered. Deliver it for him and Sarah will reward you.",
        'stringAfter': "A bit late, no?\x07Looks to be a list of orders from when I was a mercenary.\x07Those times are behind me. I mostly just wander about Port Royal these days.\x07How 'bout taking care of this fer me seein' as how it's a couple years late?",
        'title': "Smitty's Overdue Message" },
    'js2.findSmittysStuff': {
        'description': 'Smitty has forgotten where he buried some personal items. Help him find them, they are buried somewhere on Port Royal.',
        'stringAfter': "A message? I don't think Smitty ever sent this.\x07It is for Edward Stormhawk, it is a couple years late...\x07Better late the never though.\x07Deliver this to Edward Stormhawk and I will reward you with the jewelry I promised.",
        'title': "Smitty's Forgotten Treasure" },
    'js2.gatherMedicalSupplies': {
        'description': 'The EITC has not been sending medical supplies to Port Royal so you must retrieve what is needed for Smitty to recover.',
        'stringAfter': "Many thanks, indeed! I must say Smitty was getting close to the end.\x07The illness has also seemed to impact his memory. He's been searching for a chest he buried.\x07Unfortunately he cannot seem to find it.\x07Could you recover it? The chest should be buried somewhere around Port Royal.",
        'title': 'Medical Supplies' },
    'js2.recoverBandages': {
        'description': 'The EITC has not been sending bandages to Port Royal so you must retrieve some for Smitty.',
        'title': "Smitty's Bandages" },
    'js2.recoverMedicalTools': {
        'description': 'The EITC has not been sending medical tools to Port Royal so you must retrieve some for Smitty.',
        'title': "Smitty's Medical Tools" },
    'js2.recoverMedicine': {
        'description': 'The EITC has not been sending medicine to Port Royal so you must retrieve some for Smitty.',
        'title': "Smitty's Medicine" },
    'js2.visitSmitty': {
        'description': 'Jeweler Smitty has fallen ill and Sarah needs someone to help him. Speak with Smitty and find out what he needs done to get better.',
        'stringAfter': 'Seems like I have been sick for weeks now. Too much time out at sea I suppose.\x07I have been to several doctors and nothing has seemed to help.\x07Lucinda the Gypsy is my last hope. Bring her this blood sample of mine.',
        'stringBefore': "I am glad you came. My partner Smitty has fallen ill and there is not much I can do.\x07Tending to the shop's needs has taken all of my time.\x07If you can help Smitty recover, I would be willing to part with a fine piece of jewelry.\x07Go speak with Smitty, he can give you more information.",
        'title': "Smitty's Sickness" },
    'jw1.defeatAlligators': {
        'description': 'To prove your skill with a dagger, John Wallace wants you to defeat some alligators using your dagger.',
        'title': 'Gator Gladiator' },
    'jw1.defeatCrabs': {
        'description': 'To prove your skill with a dagger, John Wallace wants you to defeat some crabs using your dagger.',
        'title': 'Crab Killer' },
    'jw1.defeatScorpions': {
        'description': 'To prove your skill with a dagger, John Wallace wants you to defeat some scorpions using your dagger.',
        'title': 'Scorpion Smasher' },
    'jw1.defeatSkeletons': {
        'description': 'To prove your skill with a dagger, John Wallace wants you to defeat some skeletons using your dagger.',
        'title': 'Skeleton Crusher' },
    'jw1.defeatWasps': {
        'description': 'To prove your skill with a dagger, John Wallace wants you to defeat some wasps using your dagger.',
        'title': 'Wasp Warrior' },
    'jw1.deliverBackgroundCheck': {
        'description': "Bingham has provided you with a background check that should pass John Wallace's scrutiny. Deliver it to him.",
        'stringAfter': "Ah, the head of your class I see, very impressive.\x07Well, at least I know you are not a complete savage.\x07This alone does not speak for your skills with a dagger though.\x07I cannot have you fumbling around with one of my fine daggers, I have a reputation you know.\x07Let's just see how well you perform with that butter knife you call a dagger.",
        'title': 'A Proper Pirate' },
    'jw1.deliverFineSteelBars': {
        'description': 'Shochett Prymme has given you the last of his fine steel. Deliver the fine steel to John Wallace.',
        'stringAfter': "This is a fine metal. A shame it's so hard to find these days.\x07To finish the job I will need supplies for the handles and such.\x07I will start on the blade while you are gone.",
        'title': 'Steel Delivery' },
    'jw1.deliverShipPlans': {
        'description': 'In exchange for a clean background check, Bingham wants you to deliver the plans for his new boat to a Shipwright named John Smith on Driftwood Island.',
        'stringAfter': 'It may not look like much, but I have built many fine vessels on this island.\x07It is not the tools that make the craftsman you know.\x07Inform Bingham I will begin work on his boat immediately.',
        'title': "Bingham's Bonus" },
    'jw1.recoverArrestWarrant': {
        'description': 'Arrest warrants have been issued for John Wallace and he needs help getting them. Recover the arrest warrants from Navy guards and the dagger is yours.',
        'title': 'Wanted Wallace' },
    'jw1.recoverBladeSharpener': {
        'description': 'John Wallace is crafting you a blade using your fine steel, all he needs now is for you to acquire some blade sharpeners to finish the job.',
        'title': 'A Sharp Blade' },
    'jw1.recoverBoneDust': {
        'description': 'In exchange for the last of his fine steel, Shochett Prymme wants you to gather some skeleton bone dust for his shop.',
        'title': 'Skeleton Bone Dust' },
    'jw1.recoverCursedWood': {
        'description': 'John Wallace is crafting you a blade using your fine steel, all he needs now is for you to acquire some cursed wood to finish the job.',
        'title': 'Fine Handle' },
    'jw1.recoverHidesA': {
        'description': 'In exchange for the last of his fine steel, Shochett Prymme wants you to gather some scorpion hides for his shop.',
        'title': 'Scorpion Hides' },
    'jw1.recoverHidesB': {
        'description': 'In exchange for the last of his fine steel, Shochett Prymme wants you to gather some fly trap hides for his shop.',
        'title': 'Fly Trap Hides' },
    'jw1.recoverHidesC': {
        'description': 'In exchange for the last of his fine steel, Shochett Prymme wants you to gather some alligator hides for his shop.',
        'title': 'Alligator Hides' },
    'jw1.recoverLeatherStraps': {
        'description': 'John Wallace is crafting you a blade using your fine steel, all he needs now is for you to acquire some leather straps to finish the job.',
        'title': 'Leather Goods' },
    'jw1.visitBingham': {
        'description': 'John Wallace will not sell any of his higher end daggers to just any pirate. He requires that you bring him a background check from the Navy before he will proceed.',
        'stringAfter': "Vouch for you? Now why would I do an absurd thing like that?\x07I'm sorry to say that nothing is free in life, my friend.\x07On top of that, your background holds a few things John Wallace may not find proper.\x07I'll tell you what though, handle a small bit of business of mine and I will make it worth your time.\x07In exchange, even I would hire you based off of your background check.\x07Well... probably not, but at least John Wallace would...\x07Turns out I had an extra bit of gold this year, decided on a nice new ship for myself.\x07I need to drop off some plans to a Shipwright named John Smith on Driftwood Island.\x07I will have your background check ready for you when you return.",
        'stringBefore': 'DIALOGUE ERROR',
        'title': 'Feats of Strength' },
    'jw1.visitBingham2': {
        'description': "Return to Bingham and inform him of John Smith's progress. He will reward you with a clean background check for John Wallace.",
        'stringAfter': "Well, that took you long enough. I was about to go myself.\x07Here is your background check, free of your wrongdoings. Let's just hope John Wallace believes it...",
        'title': 'Boat Work' },
    'jw1.visitJohnWallace': {
        'description': 'John Wallace has high-end daggers that he may be willing to part with. Seek him out and learn their price.',
        'stringAfter': "Let me guess, you look like you're after some of my high end daggers?\x07Well I don't sell them to just any pirate, they are meant for the more... noble.\x07You are going to have to get me a background check from the Navy before I even begin to trust you.\x07Speak to Bingham, he can provide you with one.",
        'title': 'Visit John Wallace' },
    'jw1.visitShochett': {
        'description': 'Visit Shochett Prymme and enquire about obtaining some fine steel for John Wallace. Shochett Prymme can be found near his shop on Padres Del Fuego.',
        'stringAfter': 'Fine steel? Not many pirates seeking that these days.\x07The mines have stopped producing it around here and the price has become rather outrageous.\x07Luckily for you though, I have a small amount, took it in a trade from a pirate in Cuba.\x07You look like you can handle a weapon a bit better then I.\x07How about you help stock my shop and we will call it even?',
        'title': 'Fine Steel Deal' },
    'll1.gatherGypsySupplies': {
        'description': "Gather some supplies from EITC ships to convince Fabiola to drop her complaints with Lala Lovel's.",
        'stringAfter': "These will do just fine.\x07I don't know if it was worth all the effort though.\x07Inform Lala Lovel that we have a deal.",
        'title': "Fabiola's Supplies" },
    'll1.gatherMeat': {
        'description': 'In order to drop his complaint against Lala Lovel, Butcher Brown requires you to gather some exotic meats for his shop.',
        'stringAfter': 'You made quick work of that, you did.\x07Tell Lala that I will stop pestering her, for now...',
        'title': 'Exotic Meats' },
    'll1.recoverAlligatorMeat': {
        'description': 'In order to drop his complaint against Lala Lovel, Butcher Brown requires you to gather some exotic meats for his shop.',
        'title': 'Alligator Meat' },
    'll1.recoverBatMeat': {
        'description': 'In order to drop his complaint against Lala Lovel, Butcher Brown requires you to gather some exotic meats for his shop.',
        'title': 'Bat Meat' },
    'll1.recoverBattleSaltWater': {
        'description': "Gather some battle-touched salt water from EITC ships to convince Fabiola to drop her complaints with Lala Lovel's.",
        'title': 'Battle Salt Water' },
    'll1.recoverBoneDust': {
        'description': "Gather some bone dust from EITC ships to convince Fabiola to drop her complaints with Lala Lovel's.",
        'title': 'Bone Dust Cargo' },
    'll1.recoverFlyTrapMeat': {
        'description': 'In order to drop his complaint against Lala Lovel, Butcher Brown requires you to gather some exotic meats for his shop.',
        'title': 'Fly Trap Meat' },
    'll1.recoverIronBars': {
        'description': "In order for him to forget Lala's deeds, Blacksmith Flinty needs a decent supply of iron bars to make it worthwhile to him. They can be found buried around Tortuga Island.",
        'stringAfter': "Just in time. I'm almost out of iron.\x07This will buy Lala my forgiveness, but don't let her think she can walk all over me.",
        'title': 'Digging Up Iron' },
    'll1.recoverRockCrabMeat': {
        'description': 'In order to drop his complaint against Lala Lovel, Butcher Brown requires you to gather some exotic meats for his shop.',
        'title': 'Rock Crab Meat' },
    'll1.recoverSkeletonMeat': {
        'description': 'In order to drop his complaint against Lala Lovel, Butcher Brown requires you to gather some exotic meats for his shop.',
        'title': 'Skeleton Meat' },
    'll1.recoverTar': {
        'description': "Gather some tar from EITC ships to convince Fabiola to drop her complaints with Lala Lovel's.",
        'title': 'Tar Cargo' },
    'll1.recoverWax': {
        'description': "Gather some wax from EITC ships to convince Fabiola to drop her complaints with Lala Lovel's.",
        'title': 'Wax Cargo' },
    'll1.visitBlacksmithFlinty': {
        'description': "Lala Lovel needs you to deal with Blacksmith Flinty's complaints over the rancid ink as well.",
        'stringAfter': "Me? Forgive her? I was retching me guts out for three days!\x07And I lost plenty of business, I tell you.\x07 Bring me a decent supply of iron bars and she'll not hear from me again.",
        'title': 'One More To Go' },
    'll1.visitButcherBrown': {
        'description': 'Lala Lovel gave Butcher Brown a tattoo using the rancid ink. Visit him and see what you can do to make him stop his complaints.',
        'stringAfter': "Wants me to forgive and forget she does? Not without some compensation, mate. Here's me terms...\x07bring me back some exotic meats for my shop I'll leave her be.\x07That should make up for bein' sick as a sea dog from her rancid ink!",
        'stringBefore': "I'm having problems with some of my customers. Turns out a batch of ink I used in their tattoos was rancid.\x07Wasn't my fault, I tell them but still, all my island customers are angry!\x07Anyway, see if you can get them to forgive me and I'll give you a rare tattoo as a reward.",
        'title': 'Butchered Tattoo' },
    'll1.visitFabiola': {
        'description': 'Lala Lovel also gave Fabiola the gypsy a tattoo with the bad ink. See if you can get her to stop pestering Lala.',
        'stringAfter': "You can tell Lala I am only speaking the truth!\x07But if you make it worth my time, I'll agree to forget about it.\x07Gather some supplies from EITC ships and we'll call it a deal.",
        'title': 'Gypsy Issues' },
    'll1.visitLala': {
        'description': 'Butcher Brown has decided to stop bad-mouthing Lala Lovel to new customers. Return to her to see who else needs to be hushed.',
        'stringAfter': "Butcher Brown was terrible about talkin' me down to new customers. But he's matched only by Fabiola.\x07See if you can get her to stop bad-mouthing me work as well.",
        'title': 'One Down' },
    'll1.visitLala2': {
        'description': 'Return to Lala Lovel and say that Fabiola will no longer be bad-mouthing her.',
        'stringAfter': "I knew she'd forgive me.\x07Well, that just leaves one more angry customer in my life.\x07Blacksmith Flinty's bad tattoo left him sick for three solid days!\x07See if you can find a way to repay him as well.",
        'title': 'Two Down' },
    'll1.visitLala3': {
        'description': "All of Lala Lovel's angry customers have, after some persuasion, agreed to stop their bad-mouthing and complaints about her. Inform her of this and she will reward you with a rare tattoo.",
        'title': 'Last Stop' },
    'll2.1cleanupWildwoods': {
        'description': "Jack Redrat's wife always wished that Wildwoods was a bit safer. Defeat some scorpions from Wildwoods.",
        'title': 'Scorpion Trouble' },
    'll2.2cleanupWildwoods': {
        'description': "Jack Redrat's wife always wished that Wildwoods was a bit safer. Defeat some skeletons from Wildwoods.",
        'title': 'Skeleton Trouble' },
    'll2.CleanupWildwoods': {
        'description': 'In memory of his wife, Jack Redrat wants you to cleanup Wildwoods like she would have wanted. Defeat some of the enemies around Wildwoods.',
        'stringAfter': 'My wife would have been proud.\x07We also always had a desire to build a larger house. This is not much more then a large shack.\x07Acquire some building supplies for me and we will call it even.',
        'title': 'A Better Tomorrow' },
    'll2.buildWildwoods': {
        'description': "Jack Redrat has always wanted to build a larger home to live in. Recover some building supplies for him and Slim's debt to him will be gone.",
        'stringAfter': 'Nice Job. This will make a fine start on a new house.\x07You can inform that plague of a pirate Slim that our business relationship is over.\x07Take care.',
        'title': 'Home Improvement' },
    'll2.cleanupWildwoods': {
        'description': 'In memory of his wife, Jack Redrat wants you to cleanup Wildwoods like she would have wanted. Defeat some of the enemies around Wildwoods.',
        'stringAfter': 'My wife would have been proud.\x07We also always had a desire to build a larger house. This is not much more then a large shack.\x07Acquire some building supplies for me and we will call it even.',
        'title': 'A Better Tomorrow' },
    'll2.defeatWildWoodA': {
        'description': "Jack Redrat's wife always wished that Wildwoods was a bit safer. Defeat some scorpions from Wildwoods.",
        'title': 'Scorpion Trouble' },
    'll2.defeatWildWoodB': {
        'description': "Jack Redrat's wife always wished that Wildwoods was a bit safer. Defeat some skeletons from Wildwoods.",
        'title': 'Skeleton Trouble' },
    'll2.defeatWildWoodC': {
        'description': 'Defeat some alligators.',
        'title': 'Alligator Trouble' },
    'll2.defeatWildWoodD': {
        'description': 'Defeat some bats.',
        'title': 'Bat Trouble' },
    'll2.deliverCoinBag': {
        'description': 'Slim has given you what gold he has to go towards his debt to Jack Redrat. Deliver it to him and work off the rest of the debt for Slim.',
        'stringAfter': "This isn't even enough to cover what he owes!\x07I have been dealing with that no good scurvy pirate for some time now. Never pays on time, if at all.\x07I have a long list of work to do here in Wildwoods, so you are going to have to work off the rest.\x07For starters, my wife buried a diary somewhere in Wildwoods, it has been driving me insane trying to find it.\x07Bring it back to me, I will be waiting.",
        'title': 'Partial Payment' },
    'll2.recoverBeams': {
        'description': 'Jack Redrat needs some beams to build a larger house in Wildwoods. Recover some beams for him.',
        'title': 'Beams For Redrat' },
    'll2.recoverDiary': {
        'description': "Jack Redrat's wife buried a diary somewhere in Wildwoods and he cannot find it. Help Jack Redrat by finding the chest buried somewhere in Wildwoods.",
        'stringAfter': 'My wife was very fond of this jungle. She passed away last spring.\x07Many of her diary entries were about how she wanted to improve these parts.\x07The skeletons and scorpions alone make it a tough place to live.\x07How about you cleanup this jungle a bit like she would have wanted?',
        'title': 'Forgotten Wishes' },
    'll2.recoverNails': {
        'description': 'Jack Redrat needs some nails to build a larger house in Wildwoods. Recover some nails for him.',
        'title': 'Nails For Redrat' },
    'll2.recoverPlanks': {
        'description': 'Jack Redrat needs some planks to build a larger house in Wildwoods. Recover some planks for him.',
        'title': 'Planks For Redrat' },
    'll2.recoverSaw': {
        'description': 'Jack Redrat needs some saws to build a larger house in Wildwoods. Recover some saws for him.',
        'title': 'Saws For Redrat' },
    'll2.recoverTin': {
        'description': 'Jack Redrat needs some tin to build a larger house in Wildwoods. Recover some tin for him.',
        'title': 'Tin For Redrat' },
    'll2.visitLala': {
        'description': "Slim's debt to Jack Redrat is now gone. Return to Lala Lovel and collect your reward.",
        'title': 'Cleared Debts' },
    'll2.visitSlim': {
        'description': "Lala's brother, Slim, has failed to pay his debts to a man named Redrat. Visit Slim, in exchange for your help, Lala Lovel will reward you with a rare tattoo.",
        'stringAfter': "Ouch... I cannot describe how much... Ouch... this hurts, so let's make this short.\x07Unfortunately I owe a bit of... ouch... money to a pirate named Jack... ouch... Redrat.\x07He is threatening to take... ouch... Lala's shop.\x07Take this gold to him, it will not cover everything but I am sure you can... ouch... work off the rest.",
        'stringBefore': "Slim's my brother. He's the bloke getting a tattoo beside you.\x07Seems he's run into a bit of trouble lately.\x07Built up a bit of debt to a man named Redrat. Redrat's not taken too kindly to Slim not paying.\x07Help Slim out and I'll reward you with a rare tattoo.\x07Slim can fill you in on the details about his woes.",
        'title': "Lala's Brother" },
    'lu1.recoveralligatortails': {
        'description': 'Kill alligators in order to acquire some alligator tails.',
        'stringAfter': 'Very good. The last ingredient I need is scorpion blood.',
        'title': 'Alligator Tails for Lucinda' },
    'lu1.recovercrabshells': {
        'description': 'Kill crabs to acquire some crab shells.',
        'stringAfter': 'You are doing quite well. Next, you must get for me some alligator tails.',
        'stringBefore': 'I need ingredients. Crab shells are especially important. \x07Child, might you be able to help me with that?',
        'title': 'Crab Shells for Lucinda' },
    'lu1.recoverscorpionblood': {
        'description': 'Kill scorpions in order to acquire scorpion blood.',
        'stringAfter': 'You have done well. Thank you.',
        'title': 'Scorpion Blood for Lucinda' },
    'mc1.ShochettsList': {
        'description': "Shochett Prymme knows where you should go next in order to locate Mercedes Corazon's shop deed. Help his store out and he will provide you with the information you need.",
        'stringAfter': 'Good work. With you on her side, Mercedes might just get through this.\x07Sadly, I do not know the exact location of her deed, I do know where you should go next though.\x07Turns out the Navy scoundrel responsible for this is currently undercover as an EITC spy.\x07You should be able to find a document outlining Navy spys somewhere in Fort Dundee. That should be a good start.',
        'title': 'Shop Stock' },
    'mc1.bribeRico': {
        'description': 'Rico is willing to decipher the document, but not for free. Pay Rico to decrypt the document for you.',
        'stringAfter': "Let's see what we have here. Seems to be a list of EITC soldier names.\x07I would use caution my friend, EITC business is a dangerous area for a pirate to dwell in for too long.",
        'title': 'Pay Rico' },
    'mc1.defeatAlligators': {
        'description': 'Before he is willing to help, Shochett Prymme needs you to help out acquiring some alligator tails for his shop.',
        'title': "Shochett's Alligator Tails" },
    'mc1.defeatDreadScorpions': {
        'description': 'Before he is willing to help, Shochett Prymme needs you to help out acquiring some dread scorpion venom for his shop.',
        'title': "Shochett's Dread Scorpion Venom" },
    'mc1.defeatFlyTrapsA': {
        'description': 'Before he is willing to help, Shochett Prymme needs you to help out acquiring some fly trap roots for his shop.',
        'title': "Shochett's Fly Trap Roots" },
    'mc1.defeatFlyTrapsB': {
        'description': 'Before he is willing to help, Shochett Prymme needs you to help out acquiring some fly trap leaves for his shop.',
        'title': "Shochett's Fly Trap Leaves" },
    'mc1.defeatSkeletons': {
        'description': 'Before he is willing to help, Shochett Prymme needs you to help out acquiring some skeleton bone shavings for his shop.',
        'title': "Shochett's Bone Shavings" },
    'mc1.defeatVampireBat': {
        'description': 'Before he is willing to help, Shochett Prymme needs you to help out acquiring some vampire bat wings for his shop.',
        'title': "Shochett's Bat Wings" },
    'mc1.deliverDeed': {
        'description': "You have found Mercedes Corazon's shop deed. Return it to her to collect your reward.",
        'title': 'Delivering The Deed' },
    'mc1.deliverDocument': {
        'description': "The list you recovered from Fort Dundee is encrypted. Shochett Prymme informs you to visit Rico in Skull's Thunder as he cannot decipher it himself.",
        'stringAfter': 'Encrypted secret Navy documents... You want me to decipher them for you?\x07How about making it worth my time?',
        'title': 'List Encryption' },
    'mc1.recoverDeed': {
        'description': "Mercedes Corazon's deed is located in a locked desk somewhere in Fort Dundee. Now that you have the key, find the desk and recover the deed for Mercedes.",
        'title': "Mercedes Corazon's Deed" },
    'mc1.recoverDeskKey': {
        'description': "Mercedes Corazon's shop deed is located in a locked desk in Fort Dundee. Locate the key in a barrel somewhere in Fort Dundee.",
        'title': 'Hidden Key' },
    'mc1.recoverEITCList': {
        'description': "A document can be found somewhere in Fort Dundee that outlines all the EITC spys the Navy employs. This list should contain the identity of who stole Mercedes Corazon's deed.",
        'stringAfter': "What is this rubbish?\x07It seems to be encrypted with some Navy code. Not much I can do, mate.\x07Go speak to Rico, he tends the bar at Skull's Thunder and might be able to decipher this.",
        'title': 'Recover EITC Spy Document' },
    'mc1.recoverInformation': {
        'description': "The location of Mercedes Corazon's deed can be found on an undercover Navy soldier dressed as a EITC soldier.",
        'stringAfter': 'According to the message, the deed is hidden in a locked desk somewhere in Fort Dundee.\x07Find the key and then the desk and you should have the deed.',
        'title': 'Deed Location' },
    'mc1.visitShochettPrymme': {
        'description': "The deed to Mercedes Corazon's store has mysteriously disappeared and she's at risk of being thrown out. Help her recover the deed and Mercedes will reward you with a fine tattoo.",
        'stringAfter': 'My shop use to be a bit more impressive then what you see.\x07Like Mercedes, my deed was stolen right out from under me.\x07I am willing to help but I also need to look out for myself.\x07If you can help out my shop duties, I will help with what I can.',
        'stringBefore': "Think you're up for a challenge do you?\x07The local authorities are pressuring me out of my store.\x07Worst part is the deed was stolen from me and without it I may lose the shop.\x07A fine tattoo would be yours if you could help me recover it. Without it I am done for.\x07Shochette Prymme used to own a building on this island as well until he was forced out. He may be able to help.",
        'title': 'Deed Issues' },
    'mc2.deliverSalve': {
        'description': 'Mercedes Corazon needs you to deliver this salve to a customer of hers with an infected tattoo. She will reward you with a special tattoo when you return.',
        'stringAfter': "It is about time!\x07I didn't think I was risking a limb by getting a tattoo.\x07I would steer clear of Mercedes Corazon's tattoo shop if I was you.",
        'title': 'Salve Delivery' },
    'mc2.exoticInk': {
        'description': "Fernando has provided you with the list of ingredients for Mercedes Corazon's exotic ink. Venom from dread scorpions, crab claws from giant crabs and bone dust from skeletons.",
        'stringAfter': "I don't know why this ink is so popular. It does not seem worth all of the effort if you ask me.\x07I need your help on one more thing before you go.\x07One of my customers has come down with quite a nasty infection from one of my tattoos.\x07I can only think of one more remedy to try, but I need some items to make it.\x07Take this list. And watch your back.",
        'title': 'Exotic Ingredients' },
    'mc2.playBlackjack': {
        'description': 'Fernando wants you to prove your wits at the blackjack tables before he will tell you where to get the ingredients you need.',
        'stringAfter': "Nice play mate. I hope you're in the mood for some sailing.\x07The ingredients you need are scattered around several islands.\x07Fair winds.",
        'title': 'Card Savviness' },
    'mc2.recoverBarnacles': {
        'description': "One of Mercedes Corazon's customers has an infection from one of her tattoos. Recover some barnacles from Navy ships.",
        'title': 'Navy Barnacles' },
    'mc2.recoverBoneDust': {
        'description': "One of the ingredients for Mercedes Corazon's exotic ink is bone dust from skeletons.",
        'title': 'Skeleton Bone Dust' },
    'mc2.recoverClaw': {
        'description': "One of the ingredients for Mercedes Corazon's exotic ink is crab claws from giant crabs.",
        'title': 'Crab Claw' },
    'mc2.recoverCursedWood': {
        'description': "One of Mercedes Corazon's customers has an infection from one of her tattoos. Recover some cursed wood from Undead ships.",
        'title': 'Undead Cursed Wood' },
    'mc2.recoverSaltWater': {
        'description': "One of Mercedes Corazon's customers has an infection from one of her tattoos. Recover some battle-touched water.",
        'title': 'Navy Battle-touched Water' },
    'mc2.recoverVenom': {
        'description': "One of the ingredients for Mercedes Corazon's exotic ink is venom from dread scorpions.",
        'title': 'Scorpion Venom' },
    'mc2.tattooInfection': {
        'description': "One of Mercedes Corazon's customers has an infection from one of her tattoos. Recover the needed ingredients for a salve that will heal him.",
        'stringAfter': 'Thank you much, indeed! Olivier was getting upset about the prospect of losing an arm.\x07It might not be great for business either with him whimpering like a dog.\x07Deliver this salve to him and I will reward you well.',
        'title': 'Tattoo Infection' },
    'mc2.visitFernando': {
        'description': "Mercedes Corazon needs some illegal exotic inks for her shop. Fernando is known to be involved in black market purchases, speak to him about Mercedes Corazon's needs.",
        'stringAfter': "Normally I do not deal with pirates just walking in off the street.\x07The black market is a dangerous place for a pirate to be doing business.\x07The ingredients you need are not easy to come by. All I can help you with is where to find them.\x07How about you prove your wits at the blackjack tables and I'll help you out.",
        'stringBefore': "My customers have been asking about some exotic inks lately. Problem is they're not legal in these parts.\x07One must look to the black markets for such a purchase.\x07An upstanding business owner like myself can't be involved in such deals now can I?\x07A pirate like yourself would fit right in though, don't you think?\x07Track down what I need to make this exotic ink and I will give you one of my finest tattoos.\x07A pirate by the name of Fernando handles these types of deals, go speak to him.",
        'title': 'Black Market' },
    'mc2.visitMercedes': {
        'description': 'Mercedes Corazon has promised you a special tattoo for helping her out. Return to her to claim your reward.',
        'title': 'Tattoo Payment' },
    'mercenary_job': {
        'description': 'Defeat enemies as Josie requested.',
        'stringAfter': 'Thank you dear.',
        'stringBefore': 'Take care of this job for me.',
        'title': 'Work For Hire: Defeat Enemies' },
    'mercenary_job_em': {
        'description': 'Defeat enemies as Captain Job requested.',
        'stringBefore': "Take care of this job for me. I'll make it worth your time if you do.",
        'title': 'Work For Hire: Defeat Enemies' },
    'mercenary_job_tortuga': {
        'description': 'Defeat enemies as Johnny requested.',
        'stringAfter': 'Thanks, mate.',
        'stringBefore': 'Take care of this job for me.',
        'title': 'Defeat Enemies' },
    'naval_mercenary_job': {
        'description': 'Defeat enemy ships as Josie requested.',
        'stringAfter': 'Thank you dear.',
        'stringBefore': 'Take care of this job for me.',
        'title': 'Work For Hire: Defeat Naval Vessels' },
    'naval_mercenary_job_tortuga': {
        'description': 'Defeat enemy ships as Johnny requested.',
        'stringAfter': 'Thanks, mate.',
        'stringBefore': 'Take care of this job for me.',
        'title': 'Defeat Naval Vessels' },
    'om1.defeatFrenchShipA': {
        'description': 'The infestation on Isla Cangrejos has overflowed into the surrounding seas. Sink a French Skeleton Shadow Crow to push back the infestation.',
        'stringAfter': 'Wish I could know what it was like to sink a ship full of these pests!\x07One less of those ships wandering around the Caribbean is a step in the right direction.\x07Take down a French Skeleton Cerberus now. Ye should find one circling this island. Good luck!',
        'title': 'French Skeleton Shadow Crow' },
    'om1.defeatFrenchShipB': {
        'description': 'The infestation on Isla Cangrejos has overflowed into the surrounding seas. Sink a French Skeleton Cerberus to push back the infestation.',
        'stringAfter': "One more down! I hope these vermin are starting to get the point.\x07I saw another ship from the shore, a French Blood Scourge.\x07It doesn't sound too friendly to me... I am sure ye can make quick work of it though.\x07Sink a French Skeleton Blood Scourge that be found circling this island.",
        'title': 'French Skeleton Cerberus' },
    'om1.defeatFrenchShipC': {
        'description': 'The infestation on Isla Cangrejos has overflowed into the surrounding seas. Sink a French Skeleton Blood Scourge to push back the infestation.',
        'stringAfter': 'Isla Cangrejos thanks ye kindly. The crabs and I can sleep a bit sounder tonight.\x07I wish I could say the same about Cutthroat Isle. The infestation there has taken a similar turn and is now overflowing into the seas.\x07See if ye can hold back the infestation there as well. Spanish skeleton ships be found circling Cutthroat Isle, looking for blood.',
        'title': 'French Skeleton Blood Scourge' },
    'om1.defeatFrenchUndeadA': {
        'description': 'To help fight the new infestation of skeletons on Isla Cangrejos, Woodruff wants you to kill French Quarter Masters.',
        'stringAfter': 'Good work! The crabs and I thank ye. It turns out this infestation is the work of a chap named Pierre le Porc.\x07I hear he is the leader of a group of French pirates causing trouble throughout the Caribbean.\x07Scurvy dog uses this once tranquil island to dump his fallen pirates.\x07Help us out a bit more by clearing out some of the French Undead Maitres. Good luck!',
        'title': 'French Undead Quarter Masters' },
    'om1.defeatFrenchUndeadB': {
        'description': 'To help fight the new infestation of skeletons on Isla Cangrejos, Woodruff wants you to kill French Undead Maitres.',
        'stringAfter': "That'll show them! Maybe these parts will be a bit safer, though there's still work to be done.\x07We must take down some of their leaders if we want to make some progress.\x07French Undead Lieutenants can be found around this island. They be a good start to cleaning up this place.",
        'title': 'French Undead Maitres' },
    'om1.defeatFrenchUndeadC': {
        'description': 'To help fight the new infestation of skeletons on Isla Cangrejos, Woodruff wants you to kill French Undead Lieutenants.',
        'stringAfter': "Turns out there be more to this story. The pirates Pierre le Porc buries here come from a fierce sea battle on the outskirts of the Caribbean.\x07As for the identity of who is killing all of these French pirates, I am not certain...\x07Some say there is another island littered with the graves of Pierre's enemies.\x07The loss of all those French Undead Lieutenants has helped, but it turns out their leaders haunt this island also.\x07French Undead Captaines command most of the infestation on this island.\x07The crabs and I would be grateful if ye could put them in their place. ",
        'title': 'French Undead Lieutenants' },
    'om1.defeatFrenchUndeadD': {
        'description': 'To help fight the new infestation of skeletons on Isla Cangrejos, Woodruff wants you to kill French Undead Captaines.',
        'stringAfter': "What ye see around here turns out to be only half the problem.\x07Pierre le Porc's enemy has revealed himself. His name is Garcia de la Avaricia, a Spanish pirate lord up to no good.\x07Pierre and Garcia have been battling it out in the Caribbean for some time now and it is pirates like yerself that suffer.\x07They'll enlist any old pirate willing to risk their neck. As ye can see though, it does not always work out for them.\x07Garcia de la Avaricia handles his fallen pirates much like Pierre does, stashing them on a small wild island.\x07Cutthroat Isle is now infested with Spanish undead and is in need of help.\x07Go see if ye can make a difference there. I am going to see if I can find out more about this battle...",
        'title': 'French Undead Captaines' },
    'om1.defeatSpanishShipA': {
        'description': 'The infestation on Cutthroat Isle has overflowed into the surrounding seas. Sink a Spanish Skeleton Shadow Crow to push back the infestation.',
        'title': 'Spanish Skeleton Shadow Crow' },
    'om1.defeatSpanishShipB': {
        'description': 'The infestation on Cutthroat Isle has overflowed into the surrounding seas. Sink a Spanish Skeleton Cerberus to push back the infestation.',
        'title': 'Spanish Skeleton Cerberus' },
    'om1.defeatSpanishShipC': {
        'description': 'The infestation on Cutthroat Isle has overflowed into the surrounding seas. Sink a Spanish Skeleton Blood Scourge to push back the infestation.',
        'title': 'Spanish Skeleton Blood Scourge' },
    'om1.defeatSpanishShips': {
        'description': 'The infestation on Cutthroat Isle has overflowed into the surrounding seas. Help Woodruff out by sinking Spanish Skeleton ships to push back the infestation.',
        'title': 'Spanish Skeleton Ships' },
    'om1.defeatSpanishUndead': {
        'description': 'Woodruff wants you to help fight the new infestation of skeletons on Cutthroat Isle.',
        'stringAfter': "Cutthroat Isle has seen better days. Yer efforts, though, ensure it's not lost.\x07The Caribbean continues to be threatened, though. The infestation is starting to overflow into the sea.\x07French ships full of these scurvy undead pirates can be found circling around Isla Cangrejos.\x07As long as they hold their routes, we have no chance of taking back this island.\x07Sink a French Skeleton Shadow Crow, and defeat the crew as well to finish the job.",
        'title': 'Cutthroat Isle Infestation' },
    'om1.defeatSpanishUndeadA': {
        'description': 'To help fight the new infestation of skeletons on Cutthroat Isle, Woodruff wants you to kill Spanish Undead Conquistadors.',
        'title': 'Spanish Undead Conquistadors' },
    'om1.defeatSpanishUndeadB': {
        'description': 'To help fight the new infestation of skeletons on Cutthroat Isle, Woodruff wants you to kill Spanish Undead Bandidos.',
        'title': 'Spanish Undead Bandidos' },
    'om1.defeatSpanishUndeadC': {
        'description': 'To help fight the new infestation of skeletons on Cutthroat Isle, Woodruff wants you to kill Spanish Undead Piratas.',
        'title': 'Spanish Undead Piratas' },
    'om1.defeatSpanishUndeadD': {
        'description': 'To help fight the new infestation of skeletons on Cutthroat Isle, Woodruff wants you to kill Spanish Undead Captains.',
        'title': 'Spanish Undead Captains' },
    'om1.undeadFrenchSpanish': {
        'description': 'The Caribbean is experiencing a new infestation of skeletons not seen before. Help in the efforts to keep the Caribbean safe.',
        'stringAfter': 'Fantastic! The Caribbean may still stand a chance with pirates like yerself.\x07This infestation may not be over, but yer efforts have proven to be invaluable. Thanks, mate!',
        'title': 'Skeleton Infestation' },
    'om1.visitWoodruff': {
        'description': 'The Caribbean is experiencing a new infestation of skeletons never seen before. Go speak to Woodruff on Isla Cangrejos, he can fill you in with the details. ',
        'stringAfter': "A visitor! It gets very lonely here... mainly I just argue with the crabs and wander about.\x07I must tell ye though, things have taken a turn for the worse lately. The crabs and I are worried!\x07Suddenly we find ourselves overrun with skeletons and I'm no longer at the top of the food chain.\x07Aside from amassing a crab army, there is not much I can do...\x07Think perhaps ye could help us out a bit? Start with clearing out some of the French Undead Quarter Masters.",
        'stringBefore': 'It looks like ye be in need of something to do...\x07I might just be able to point ye in the direction of some work...\x07The Caribbean can be very cruel to yer average pirate and it seems like things have taken a turn for the worse.\x07Pirates everywhere have been sharing tales of close calls with skeletons never seen before.\x07Thankfully they have been held back to only infesting two wild islands.\x07Isla Cangrejos is one of these islands. A marooned chap named Woodruff can be found there, that is if he is still alive...\x07Go speak to him. He can fill you in on what needs to be done.',
        'title': 'Skeleton Infestation' },
    'pa1.bribeOlivier': {
        'description': 'Information does not come cheap, you will need to bribe Olivier to find the gems.',
        'stringAfter': 'The gems... yes, now I remember. Seems a crew of pirates lost their way recently.\x07They ended up stashing some of their cargo of precious gems around Padres Del Fuego.\x07Chances are you can still find some if you look hard enough.',
        'stringBefore': 'bribeOlivier dialog before',
        'title': 'Bribe Olivier' },
    'pa1.defeatPerlasEnemy': {
        'description': "Lately Perla's customers have been avoiding the shop due to some recent skeleton raids. She has asked you to take care of them for her.",
        'stringAfter': 'defeatPerlasEnemy dialog after',
        'stringBefore': 'defeatPerlasEnemy dialog before',
        'title': "Perla's Protection" },
    'pa1.gatherAmethystStones': {
        'description': 'Recover Amethysts from buried treasure chest hidden somewhere on Padres Del Fuego.',
        'stringAfter': 'You found them! Amethysts are one of my favorite gems you know.\x07I like them almost as much as I like Sapphires.\x07Think you can find some for me?',
        'stringBefore': 'gatherAmethystStones dialog before',
        'title': 'Buried Amethyst' },
    'pa1.gatherRubyStones': {
        'description': 'Recover Rubies from buried treasure chests hidden somewhere on Padres Del Fuego.',
        'stringAfter': "Some fine rubies indeed. These alone though will not save the shop.\x07Bring me some Amethysts as well and we'll talk.",
        'stringBefore': 'gatherRubyStones dialog before',
        'title': 'Buried Rubies' },
    'pa1.gatherSapphireStones': {
        'description': 'Recover Sapphires from buried treasure chests hidden somewhere on Padres Del Fuego.',
        'stringAfter': 'Perfect, these are just lovely.\x07I could use your help on one last thing before you go on your way though.\x07Lately some skeletons have been harassing my customers and driving away business.\x07Deal with them for me and I will pay you handsomely.',
        'stringBefore': 'gatherSapphireStones dialog before',
        'title': 'Buried Sapphires' },
    'pa1.returnToPerla': {
        'description': 'returnToPerla description',
        'reward': 'Jewelry',
        'stringAfter': 'returnToPerla dialog after',
        'stringBefore': 'returnToPerla dialog before',
        'title': 'returnToPerla title' },
    'pa1.trackDownJewels': {
        'description': 'Go speak with Olivier and see what you can find out about the precious gems. Perla will pay you in jewelry if you recover them for her.',
        'stringAfter': "Buried gems you say? Well... I don't know much about that.\x07Of course a bit of persuasion seems to always help my memory.",
        'stringBefore': "Looking for a job? I just might have something for you.\x07See, business has been a bit slow lately, honestly dreadful at times.\x07Recently I overheard Olivier going on about rumors of chests of precious gems buried about the island.\x07Such a find would definitely turn business around you know.\x07Olivier can be found loitering around the docks. Now get going, you're scaring away customers.",
        'title': 'Precious Treasures' },
    'pa2.recoverClothes': {
        'description': 'Perla Alodia and Olivier need to outfit their smuggling crew. Gather Navy and EITC outfits before they can go back to business.',
        'stringAfter': 'Perfect.  We are almost ready to set sail.\x07We would have left already if were it not for the fact that half of our crew is in jail.\x07This tends to happen often when your crew is made up of pirates.\x07I need to get my hands on their warrants as well as some prison keys so I can break them out.\x07You should be able to find all these items hidden somewhere in Fort Dundee.\x07Be careful though.  The Navy does not take too kindly to pirates lurking around.',
        'title': 'Smuggling Disguises' },
    'pa2.recoverEITCCoats': {
        'description': 'Perla Alodia and Olivier need to outfit their smuggling crew with EITC outfits. Gather EITC outfits before they can go back to business.',
        'title': 'EITC Coats' },
    'pa2.recoverEITCFlags': {
        'description': 'Perla Alodia and Olivier need EITC flags to continue their smuggling ring. Recover some from EITC ships.',
        'title': 'EITC Flags' },
    'pa2.recoverEITCPants': {
        'description': 'Perla Alodia and Olivier need to outfit their smuggling crew with EITC outfits. Gather EITC outfits before they can go back to business.',
        'title': 'EITC Pants' },
    'pa2.recoverFlags': {
        'description': 'Perla Alodia and Olivier need you to acquire Navy and EITC flags for their smuggling ring.',
        'stringAfter': 'These will do just fine.\x07Our ships will pass right by those Navy and EITC vultures.\x07Unfortunately we need to outfit our crew in the same fashion.\x07Gather some EITC and Navy outfits for the crew.',
        'title': 'Stolen Flags' },
    'pa2.recoverNavyCoats': {
        'description': 'Perla Alodia and Olivier need to outfit their smuggling crew. Gather Navy outfits before they can go back to business.',
        'title': 'Navy Coats' },
    'pa2.recoverNavyFlags': {
        'description': 'Perla Alodia and Olivier need Navy flags to continue their smuggling ring. Recover some from Navy ships.',
        'title': 'Navy Flags' },
    'pa2.recoverNavyPants': {
        'description': 'Perla Alodia and Olivier need to outfit their smuggling crew. Gather Navy outfits before they can go back to business.',
        'title': 'Navy Pants' },
    'pa2.recoverPrisonKeys': {
        'description': "Half of Perla Alodia and Olivier's crew is in jail.  Recover prison keys so they can break them out.",
        'title': 'Prison Keys' },
    'pa2.recoverSchedule': {
        'description': "Half of Perla Alodia and Olivier's crew is in jail.  Recover a Navy schedule from a container in Fort Dundee so they can break them out.",
        'title': 'Navy Schedule' },
    'pa2.recoverSupplies': {
        'description': "Half of Perla Alodia and Olivier's crew is in jail.  To break them out,  they need to acquire the crew's warrants,  some prison keys and a Navy schedule.",
        'stringAfter': 'Right on time.  The crew is getting a bit rowdy in prison I hear.\x07Go speak with Perla.  She just got in your reward.',
        'title': 'Prison Break' },
    'pa2.recoverWarrants': {
        'description': "Half of Perla Alodia and Olivier's crew is in jail.  Recover the crew's warrants from containers in Fort Dundee so they can break them out.",
        'title': 'Crew Warrants' },
    'pa2.visitOlivier': {
        'description': 'Perla Alodia wants your help with one of her businesses she runs with Olivier. Go speak with Olivier as he can tell you more.',
        'stringAfter': 'So, Perla tells me you are here to help?\x07Very well then. Perla and I run a small smuggling ring. We supply the needs of this island that the EITC cannot.\x07Our business requires us to disguise our ships as EITC or Navy at times and we are running low on flags.\x07Recover some flags from EITC and Navy ships. Good luck.',
        'stringBefore': 'The jewelry shop is not exactly my only business. I run a side business with a fellow named Olivier.\x07I would go into detail, but the shop is not the best place to speak of such things.\x07It is a little risky, but if you can help us out, there will be jewelry in it for you.\x07Go speak to Olivier, he is usually out by the docks.',
        'title': 'Spy Trouble' },
    'pa2.visitPerla': {
        'description': 'You have assisted Perla Alodia and Olivier with their smuggling business.  Return to Perla in order to claim your jewelry.',
        'title': 'Claiming Reward' },
    'pc.1visitSam': {
        'description': 'See what Sam Seabones knows about the attack.',
        'stringAfter': "That's right, I was there. But I was attacked as well. I can't say I saw anything he didn't.",
        'stringBefore': "Not long ago, I was the victim of a cowardly sneak attack by a bunch of Navy dogs. \x07I want you to find out who's responsible and make them pay. Sam Seabones was there with me. \x07Talk to him and see what he remembers about it.",
        'title': 'A Favor For P. Chipparr' },
    'pc.2visitPeter': {
        'description': 'Return to Peter and tell him what Sam said.',
        'stringAfter': "So, not much, huh? Guess we'll have to do this the hard way. \x07Go over to the local fort and knock around some officers until one gives up the goods on who staged the attack. \x07Don't come back until you've got a name for me.",
        'title': 'Return to Peter Chipparr' },
    'pc.3QuestionNavyOfficers': {
        'description': 'Rough Up Navy Guys To Find Out Who Attacked Peter Chipparr',
        'stringAfter': "Really, Miller did this? I didn't think he had the nerve. \x07I want you to find that coward and maroon him somewhere far away. I never want to see his ugly face again.",
        'title': 'Interrogate Navy Officers' },
    'pc.5FindNavySwine': {
        'description': 'Attack Navy Ships until you find Officer Miller.',
        'title': 'Find Officer Miller' },
    'pc.6MaroonNavySwine': {
        'description': 'Now that you have Officer Miller, maroon him on a deserted island.',
        'stringAfter': "Thank you for taking care of that for me. I'll remember it.",
        'title': 'Maroon Officer Miller' },
    'pc.7visitPeter3': {
        'description': 'Return to Peter and let him know the good news.',
        'stringAfter': 'Thank you for taking care of that for me. Come back and I might have more work for you.',
        'title': 'Return to Peter Chipparr' },
    'playCards': {
        'description': 'Morris has lost everything at the card tables to cheats. Get some revenge for Morris by winning at the poker and blackjack tables.',
        'stringAfter': "That'll show those swine not to mess around! Good show mate.\x07Maybe one of these days I'll actually win. Be sure to give Adoria Dolores my best!",
        'title': 'Card Game Revenge' },
    'pul5.1visitErasmus': {
        'description': 'Seek out Erasmus, a gunsmith, in his shop on Padres Del Fuego.',
        'stringAfter': "Hello mate.  Needin' a new pistol, ey?  I'm yer man. \x07 But I be needing some help me self.\x07 I've invented a better rapid-fire pistol and it needs a few special parts. \x07 First-hammers from Spanish flintlocks.  Get me some of them from those undead vermin and I'll help get yer pistol.",
        'title': 'Visit Erasmus Grimsditch' },
    'pul5.2acquirePistolParts': {
        'description': 'Spanish Undead are known to inhabit the Cutthroat Island cemetery.  Via Con Dios!',
        'stringAfter': "Excellent work.  Now help me with an old score I gotta settle.\x07 Me friend Delilah Densmore has been sold into indentured servitude\x07 by her former love to a Padres jeweler name of Perla.\x07 Find Delilah and she'll tell ye what she needs to buy her freedom.",
        'title': 'Undead Spanish' },
    'pul5.3visitDelilah': {
        'description': "Delilah Dunsmore is a lovely lass who's serving out her indenture to Perla, the Padres del Fuego jeweler.",
        'stringAfter': "Erasmus sent you?  Oh thank the heavens!\x07I know where some valuable gems are buried inside Beckett's Quarry that'll buy me freedom.\x07 Find 'em,  and defeat the wretch who sold me to pay off his gamblin' debts!\x07 He's an East India Thug named Samuel.  Bring me his brass buttons and you will get your pistol.",
        'title': 'Visit Delilah Dunsmore' },
    'pul5.4defeatFormerLove': {
        'description': "Beckett's Quarry is the mine on Padres del Fuego owned and heavily guarded by the East India Trading Company. Delilah's former love is posted there.",
        'title': "Delilah's Former Love" },
    'pul5.5findGems': {
        'description': "Beckett's Quarry is the mine on Padres del Fuego owned and heavily guarded by the East India Trading Company. Delilah's gems are found there.",
        'stringAfter': "Thanks.  You're as good as they say.\x07 Next...let the fair winds take you to Kingshead and get the musket stocks from 8 Navy officers.\x07 They're made of a rare wood ole Grimsditch needs to make his new invention.\x07 When you're done, return 'em to him.  God speed, friend.",
        'title': "Excavate Delilah's Gems" },
    'pul5.6acquireWoodStocks': {
        'description': 'High level Navy soldiers can be found on the island of Kingshead.',
        'title': 'Wood Stocks' },
    'pul5.7deliverToErasmus': {
        'description': 'Return the components to Erasmus on Padres Del Fuego.',
        'stringAfter': "Ah, the black walnut stocks.  Excellent!  Sorry, mate but I be needing three more items.\x07 Some copper that's found on East India ships. I mix the copper with\x07 bone dust from a huge alligator boss name of Dreadtooth to make invincible bullets.\x07 Then all that's left is some high quality metal from Navy ships for me barrels.\x07Get those and get yerself that pistol.",
        'title': 'Deliver Components' },
    'pul5r1.1acquireCopper': {
        'description': 'Ships of this caliber can be found in the seas surrounding Port Royal.',
        'title': 'Copper' },
    'pul5r1.2acquireGunPowder': {
        'description': 'Ships of this caliber can be found in the seas surrounding Port Royal.',
        'title': 'Gun Powder' },
    'pul5r1.3defeatAlligatorBoss': {
        'description': 'The huge alligator boss, Dreadtooth, is a nasty brute so approach with care!',
        'title': 'Dreadtooth' },
    'pul5r1Tasks': {
        'description': "Acquire the final components at Erasmus' request.",
        'title': 'Final Components' },
    'pv.1visitPirate': {
        'animSetAfter': [
            None,
            65000,
            60657],
        'description': "Sid Tackem needs your help to win Dedrie Dunnam's heart. He can be found on the long dock on Port Royal.",
        'stringAfter': "I do love the lass but I be shy.\x07So me thinks a hand crafted Valentine's gift will win her, ey?\x07Get me the ingredients and... I'll make ye a well-dressed pirate indeed!",
        'stringBefore': "Me mate Sid Tackem fancies this wench, er, lady named Dedrie Dunnam.\x07Help him out and ye will receive a fine new shirt to replace that ragged one of yers.\x07Now be gone 'fore Valentine's Day draws nigh! ",
        'title': 'Find Sid Tackem' },
    'pv.2deliverValentine': {
        'animSetAfter': [
            60654,
            60602,
            65001],
        'description': 'Deliver the valentine to the beautiful Dedrie Dunnam. She can be found in the Faithful Bride tavern on Tortuga.',
        'stringAfter': "Oh, it's...bloody disturbing!\x07Please return to Mr. Tackem with me regards and convey this...\x07...not now, not ever!  Savvy?!",
        'title': 'Deliver A Valentine' },
    'pv.3visitPirate': {
        'animSetAfter': [
            60652,
            65001,
            60657],
        'description': "Let Sid Tackem know about his failed attempt to win Dedrie Dunnam's heart.",
        'stringAfter': 'She said what? Ahhhhh! Me heart has been keelhauled!\x07Go. I needs to be alone with me grief!.\x07Wait matey, return to Erin, ask him how to remedy this situation!',
        'title': 'Return to Sid Tackem' },
    'pv.4visitErin': {
        'animSetAfter': [
            60640,
            60665,
            60657],
        'description': 'See if Erin Amorous has a remedy to the situation. Go to the Rowdy Rooster tavern in Port Royal and talk to Erin.',
        'stringAfter': "Ha, ha! Dedrie's as strong willed as a steel hull, but...\x07I missed the boat on that one, ey? \x07 I've no more counsel on matters of the heart, go ask Scarlet, she'll know.",
        'title': 'Talk to Erin Amorous' },
    'pv.5visitScarlet': {
        'description': 'Talk to Scarlet who stands in front of Faithful Bride tavern on Tortuga. She might know more about the matters of the heart.',
        'stringAfter': "Did he truly give her a heart affixed with a skull and bones?\x07Sid's mind has run aground, it has! \x07Here's what he needs...but first, I be needin' a favor.\x07Pay a small debt I owes to Giladoga. Then I'll help ye solve Sid's dilemma.",
        'title': 'Visit Scarlet' },
    'pv.6bribeGiladoga': {
        'description': 'Pay Giladoga a small debt Scarlet owes him. You can find Giladoga in Ratskellar Tavern on Padres del Fuego.',
        'stringAfter': "From Scarlet?  Thank ye kindly. Never thought I'd see that. \x07Give her me best, ey?",
        'title': 'Bribe Giladoga' },
    'pv.7visitScarlet': {
        'description': 'Report back to Scarlet and get advice from her.',
        'stringAfter': "So here's what he needs...\x07Yes, a simple flower. A rose works best.\x07Now go, ye be boring me!",
        'title': 'Return to Scarlet' },
    'pv.8deliverFlower': {
        'animSetAfter': [
            60602,
            60657,
            60519],
        'description': 'Deliver the rose to Dedrie Dunnam as a gift from Sid Tackem.',
        'stringAfter': "I said not ever!...\x07Ah, a rose. That's...sweet. Return to Mr. Tackem and say...\x07...maybe.",
        'title': 'Deliver Flower' },
    'pv.9collectReward': {
        'description': "Let Sid Tackem know about Dedrie's feelings.",
        'title': 'Return to Sid Tackem' },
    'pvr1.1acquireCrossbones': {
        'description': 'The undead can be found throughout the Caribbean.',
        'title': 'Skeleton Bones' },
    'pvr1.2acquireNavyCoat': {
        'description': 'Navy soldiers can be found around Port Royal and Fort Charles.',
        'title': 'A Navy Coat' },
    'pvr1.3acquireNavyButtons': {
        'description': 'Navy soldiers can be found around Port Royal and Fort Charles.',
        'title': 'Navy Brass Buttons' },
    'pvr1.4acquireGatorSkin': {
        'description': 'Alligators can be found in the swamps of the Caribbean.',
        'title': 'Alligator Hide' },
    'pvr1.5acquireScorpionBlood': {
        'description': 'Scorpions can be found in one of the forests of Tortuga.',
        'title': 'Scorpion Blood' },
    'rc.1visitJack': {
        'description': 'Talk to Jack Sparrow to hear his plan.',
        'dialogAfter': 'rc.1visitJack.after',
        'title': 'Talk To Jack Sparrow' },
    'rc.2sailToRavensCove': {
        'description': "Find the mysterious Raven's Cove island. According to Jack the Cursed Blades of El Patron are hidden somewhere on the island. Only with them can you defeat Jolly Roger.",
        'title': "Journey to Raven's Cove" },
    'rc.3bTalkToEdward': {
        'description': 'Speak with Crazy Ned and find out the clue of what needs to be done next.',
        'title': 'Question Crazy Ned' },
    'rc.3searchForSurvivors': {
        'customTask': "Investigate \x01questObj\x01Raven's Cove\x02 and search for survivors",
        'description': "Uncover the mysteries of Raven's Cove.",
        'dialogAfter': 'rc.edwardBrittle.intro',
        'title': 'Investigate the island' },
    'rc.GhostsOfRavensCove': {
        'description': 'Search the town for ghostly creatures.',
        'dialogAfter': 'rc.GhostsOfRavensCove.after',
        'title': "Ghosts of Raven's Cove" },
    'rc.ghosts.LadyThreadbarren': {
        'description': 'sth about her',
        'title': 'The Ghost of Widow Threadbarren' },
    'rc.ghosts.MadamZigana': {
        'description': "Madame Zigane was a Voodoo priestess living on Raven's Cove. When Jolly attacked she used her voodoo staff to defend the town, but she was no match for Jolly who grabbed the staff and broke over his knee like a twig.\n\nNow her ghost wants your help to fashion a new more powerful staff, for which she'll help you get the mine key from Ned.",
        'dialogAfter': 'rc.ghosts.zigana.brewPotions.after',
        'title': 'The Ghost of Madam Zigana' },
    'rc.ghosts.SenorFantifico': {
        'description': "Se\x0c3\x0b1or Fantifico's name loosely translates to 'Mister Fancy' and in life, everything he did was just that - fancy. From the luxurious style of his clothes to drinking his tea with a proper pinky extended, he did everything with lavish flair.\n\nJolly's troops found him cowering in his cellar and dispatched him. Senior Fantifico will reward you if you find a potion that will bring him back to the fancy life he so loved. ",
        'dialogAfter': 'rc.ghosts.fantifico.deliverPotion.after',
        'title': 'The Ghost of Se\x0c3\x0b1or Fantifico' },
    'rc.ghosts.TheClubhearts': {
        'description': "The Clubhearts owned the Raven's Cove gambling den. After the invasion Jolly Roger forced them into a poker game and cheated taking their gold and their lives.\n\nHelp them by finding the secret skeleton poker game and winning back their gold.",
        'dialogAfter': 'rc.ghosts.clubhearts.undeadPoker.after',
        'title': 'The Ghost of the Clubhearts' },
    'rc.ghosts.ThomasFishmeister': {
        'description': "Thomas Fishmeister was the fisherman of Raven's cove. During the invasion Jolly poisoned the waters and Thomas was unable to supply the town with food.\n\nNow he wants you to catch him some fish so he can fulfil his duty to the town.",
        'dialogAfter': 'rc.ghosts.fishmeister.catchFish.after',
        'title': 'The Ghost of Thomas Fishmeister' },
    'rc.ghosts.WidowThreadbarren': {
        'description': "Widow Threadbarren was the Raven's Cove seamstress. Jolly let her live long enough to repair damaged sails for him, then took her life.\n\nNow she's bent on revenge and wants Jolly's ships sunk and her sails returned. Help Widow Threadbarren and she'll help you get the keys to the mines.",
        'dialogAfter': 'rc.ghosts.threadbarren.RetrieveSails.after',
        'title': 'The Ghost of Widow Threadbarren' },
    'rc.ghosts.clubhearts.disguise': {
        'description': 'Acquire clothes to disguise yourself as a Clubheart.',
        'dialogAfter': 'rc.ghosts.clubhearts.disguise.after',
        'title': 'Disguise Yourself as a Clubheart' },
    'rc.ghosts.clubhearts.undeadPoker': {
        'description': "Beat the undead in their own game to win Clubhearts' favor.",
        'title': 'Play Undead Poker' },
    'rc.ghosts.fantifico.1potionIngredients': {
        'description': 'Twisted Roots are crucial ingredients for a life restoring potion.',
        'title': 'Twisted Roots' },
    'rc.ghosts.fantifico.2potionIngredients': {
        'description': ' Giant alligator bladders are crucial ingredients for a life restoring potion.',
        'title': 'Alligator Bladders' },
    'rc.ghosts.fantifico.3potionIngredients': {
        'description': 'Fat chickens are crucial ingredients for a life restoring potion.',
        'title': 'Fat Chickens' },
    'rc.ghosts.fantifico.PotionIngredients': {
        'description': 'Tia Dalma knows of a special life restoring potion recipe. However, she needs special ingredients to be able to brew one for Se\x0c3\x0b1or Fantifico.',
        'dialogAfter': 'rc.ghosts.fantifico.PotionIngredients.after',
        'title': 'Life Restoring Potion Ingredients' },
    'rc.ghosts.fantifico.deliverPotion': {
        'description': 'Go back to the ghost of Se\x0c3\x0b1or Fantifico and check if the magic potion works.',
        'dialogAfter': 'rc.ghosts.fantifico.deliverPotion',
        'title': 'Deliver Restoring Potion' },
    'rc.ghosts.fantifico.visitTiaDalma': {
        'description': "Se\x0c3\x0b1or Fantifico wants so badly to restore his life as the Fanciest Fellow in the Caribbean that he'll pay a king's ransom for a special gypsy potion made only by Tia Dalma. Get this life-giving potion for him and you're one step closer to getting Edward's mine key.",
        'dialogAfter': 'rc.ghosts.fantifico.visitTiaDalma.after',
        'title': 'Seek Tia Dalma' },
    'rc.ghosts.fishmeister.catchFish': {
        'description': "Get your fishing pole and help Thomas with some serious fishing. Catching lots of fish will get you that much closer to getting Ned's key to the mine.",
        'dialogAfter': 'rc.ghosts.fishmeister.catchFish.after',
        'title': 'Catch Fish' },
    'rc.ghosts.helpAllGhosts': {
        'customTask': "Help \x01questObj\x01Raven's Cove\x02 ghosts",
        'description': "To get Crazy Ned's key to the mine you must search the ruined buildings on Raven's Cove and help the ghosts inside.\n\nHeed Ned's warning and avoid the red ghosts on the streets!",
        'title': 'Visit Ghosts of the Island' },
    'rc.ghosts.threadbarren.1retrieveSails': {
        'description': "Phantom ships carry some of Lady Threadbarren's sails, get them back!",
        'title': 'Phantom Sails' },
    'rc.ghosts.threadbarren.2retrieveSails': {
        'description': "Revenant ships carry some of Lady Threadbarren's sails, get them back!",
        'title': 'Revenant Sails' },
    'rc.ghosts.threadbarren.3retrieveSails': {
        'description': "Storm Reaper ships carry some of Lady Threadbarren's sails, get them back!",
        'title': 'Reaper Sails' },
    'rc.ghosts.threadbarren.RetrieveSails': {
        'description': "Sink ghost ships for Widow Threadbarren to earn her favor and retrieve their sails for her. After you have completed this quest, she'll speak favorably to Crazy Ned about giving you the key to the mine.",
        'dialogAfter': 'rc.ghosts.threadbarren.RetrieveSails.after',
        'title': 'Retrieve Sails' },
    'rc.ghosts.zigana.brewPotions': {
        'description': 'Help Madam Zigana by getting the special potions so she can rebuild her old broken staff. Brew them up and return the potions to Madam Zigana so she can thank you properly.',
        'dialogAfter': 'rc.ghosts.zigana.brewPotions.after',
        'title': 'Potions For Zigana' },
    'rc.le.10lootTreasure': {
        'description': "Take one of El Patron's Cursed Blades.",
        'title': "Loot El Patron's Treasure" },
    'rc.le.1findJournals': {
        'description': "Search the four graves near the skull totems to recover journals from El Patron's crew which contain clues on how to open the door.",
        'dialogAfter': 'rc.le.1findJournals.after',
        'title': 'Find the Journals' },
    'rc.le.2AlureGhosts': {
        'description': 'Lure Devious Ghosts to the watery grave stone and defeat them.',
        'title': 'Lure Devious Ghosts' },
    'rc.le.2LureGhosts': {
        'description': "To claim the first idol you need to exact revenge for the ghost of one of El Patron's officers. Lure a total of ten ghosts to his isolated grave stone and defeat them.",
        'dialogAfter': 'rc.le.2LureGhosts.after',
        'title': 'Lure the Ghosts' },
    'rc.le.2lureGhosts': {
        'description': 'Lure Mutineer Ghosts to the watery grave stone and defeat them.',
        'title': 'Lure Mutineer Ghosts' },
    'rc.le.3defendTraitor': {
        'description': 'Summon a ghost at the highest grave marker and defend him from waves of attacking ghosts.',
        'dialogAfter': 'rc.le.3defendTraitor.after',
        'title': 'Defend the Traitor' },
    'rc.le.4AfindParts': {
        'description': 'Defeat 10 Devious Ghosts to find parts for the dowsing rod.',
        'title': 'Defeat 10 Devious Ghosts' },
    'rc.le.4DowsingRodParts': {
        'description': 'Defeat ghosts around the mine in order to put together the Dowsing Rod.',
        'dialogAfter': 'rc.le.4DowsingRodParts.after',
        'title': 'Find Dowsing Rod Parts' },
    'rc.le.4FindPartsBats': {
        'description': 'Defeat 13 Fire Bats to find parts for the dowsing rod.',
        'title': 'Collect 13 Fire Bat Teeth' },
    'rc.le.4findParts': {
        'description': 'Defeat 10 Mutineer Ghosts to find parts for the dowsing rod.',
        'title': 'Defeat 10 Mutineer Ghosts' },
    'rc.le.5useDowsingRod': {
        'description': "Use the dowsing rod to search through Dr. Bellrog's dig spots. One of them should hide the third idol. ",
        'dialogAfter': 'rc.le.5useDowsingRod.after',
        'title': 'Use the Dowsing Rod' },
    'rc.le.6getLastIdol': {
        'description': 'Defeat four ghosts at once. You may go to the previous three grave markers to recruit ally ghosts. However these ghosts only remain summoned for a minute or two so you must hurry.',
        'dialogAfter': 'rc.le.6getLastIdol.after',
        'title': 'Get the Last Idol' },
    'rc.le.7defeatKudgel': {
        'description': "Defeat Dr. Bellrog's Bodyguard.",
        'dialogAfter': 'rc.le.7defeatKudgel.after',
        'title': 'Defeat Kudgel' },
    'rc.le.8exploreElPatronsShip': {
        'customTask': "Explore El Patron's ship",
        'description': "El Patron's ship is said to have contained lost treasure. Search the ship for weapons. To reach his ship you must travel through the mines.",
        'title': "Explore El Patron's Ship" },
    'rc.le.9defeatElPatron': {
        'description': 'Defeat El Patron to claim a cursed blade. To reach his ship you must travel through the mines.',
        'title': 'Defeat El Patron' },
    'rc.talkToBellrog': {
        'customTask': "Explore the Raven's Cove Mine",
        'description': "Search the Mine of Raven's Cove for a clue to where the blades of El Patron might be.",
        'dialogAfter': 'rc.talkToBellrog.after',
        'title': 'Explore the Mine' },
    'rc.useMineShaft': {
        'description': "Use the mine shaft to get to the top of Raven's Cove.",
        'title': 'Use the Mine Shaft' },
    'rct.findHiddenPieces': {
        'description': "Search crates around the Raven's Cove where ravens might have hidden pieces to a teleport totem.",
        'title': 'The Hidden Pieces' },
    'recoverFamilyHeirloomsFromLand': {
        'description': 'Maggie Rigrage needs you to acquire the rest of her family heirlooms. She suspects they have been picked up by stumps and dread scorpions.',
        'stringAfter': 'Finally we can stop looking!\x07I hope Adoria Dolores and Romany Bev have something special for you to show our thanks.\x07Be sure to give them my best. Return to Romany Bev, she is expecting you.',
        'title': 'Getting the Rest' },
    'recoverFamilyHeirloomsFromShips': {
        'description': 'Maggie Rigrage needs some help gathering her family heirlooms after her ship sunk. Some of the family heirlooms have been picked up by nearby Navy, EITC and Skeleton ships. Recover them for her.',
        'stringAfter': "There's still some missing! I'm starting to think that there was some sabotage behind our shipwreck...\x07The rest of the heirlooms must have been picked up by some of the pests around the area.\x07Recover the rest from dread scorpions and stumps that infest nearby islands.",
        'title': 'Floating Heirlooms' },
    'recoverLorePages': {
        'description': 'Will Turner has discovered that some of the pages from Pirate Lore are hidden on EITC Marauder, Barracuda, Corvette and Sea Viper ships. Recover these pages for him to continue.',
        'stringAfter': "It's all starting to come together. Unfortunately the book remains unfinished.\x07There is only one man I can think to turn to, a pirate named Billy McKidd.\x07He used to search for the text along with me. He gave up on the search years ago.\x07He may be able to help us now that we have most of the book in hand.\x07Go speak to him. He's usually in the La Bodeguita tavern on Cuba.",
        'title': 'Sailing For Lore' },
    'recoverMaterials': {
        'description': 'Isaiah Callecutter needs you to recover rare ingredients in order to make shoes from the EITC designs you recovered.',
        'stringAfter': "Good work mate! I hope none of those pests caused you too much trouble.\x07These designs may just put this shop back on the map. We do have one problem, though.\x07These designs are still being distributing by the EITC. They're going to be tough to compete with to say the least.\x07If we can somehow keep them from selling their shoes, we'll make a fortune!\x07If we can take down enough EITC ships, we'll definitely see a difference.\x07Return to me when you are done. I'll have your shoes ready.",
        'title': 'Fine Shoe Ingredients' },
    'recoverTentacles': {
        'description': 'To finish your boots, Adoria Dolores needs you to gather tentacles from Seabeards, Molusks and Urchinfists.',
        'stringAfter': "I didn't expect to see you mate. Impressive work!\x07I'll take that Eye of Urchinfist. I'm sure it will fetch quite a price at auction.\x07I've heard from Adoria Dolores that she's almost done with your boots. But she's needing those tentacles you've recovered.\x07Deliver the tentacles to her.",
        'title': 'Tentacle Trouble' },
    'recoverVoodooArtifacts': {
        'description': "Some of Romany Bev's voodoo artifacts have been stolen by EITC and Navy ships. Recover them from EITC and Navy ships sailing around the Caribbean.",
        'stringAfter': "Finally! I didn't think I'd see these artifacts again.\x07I'll be sure to tell Adoria Dolores of your progress. I've heard she just started on a coat for you.\x07She needs you to help out another one of our family members.\x07Maggie Rigrage is stranded on Outcast Isle. Go visit her.",
        'title': 'Voodoo Artifacts' },
    'remedyIngredients': {
        'description': 'Olivier needs you to recover rotten meat, fly trap roots and alligator saliva for his remedy.',
        'stringAfter': "Thanks mate! Hopefully I'll be feeling better in no time.\x07I believe Adoria Dolores has your pants ready. Go visit her.",
        'title': "Olivier's Remedy" },
    'rs1.1recovertools': {
        'description': 'Sink ships in order to acquire a set of smithing tools.',
        'stringAfter': 'These tools are perfect. Now that I have the right tools, I need some raw materials. \x07Scavenge me some iron bars.',
        'stringBefore': 'These tools of mine are getting a bit old. \x07Could you perhaps acquire a new set? \x07I ought to have plenty more work for you if you can help with that.',
        'title': 'Acquire Smithing Tools' },
    'rs1.3recoveriron': {
        'description': 'Sink ships in order to acquire iron bars.',
        'stringAfter': 'Thanks. Now I am almost ready to get back to work. \x07All I need now to start back to work is some coal. \x07Can you acquire some for me?',
        'title': 'Acquire Iron Bars' },
    'rs1.5recovercoal': {
        'description': 'Sink ships in order to acquire bags of coal.',
        'stringAfter': "Thanks. You've been a great help.",
        'title': 'Acquire Bags of Coal' },
    'rumForGunner': {
        'description': 'Gunner needs you to get the rest of the rum Adoria Dolores owes him. Gather bottles of rum from high level Navy guards and barrels of rum from EITC ships.',
        'stringAfter': "THAT'LL BE THE LAST TIME I LEND ADORIA SO MUCH OF ME RUM!\x07FER HER SAKE, I HOPE SHE DON'T RUN HER SHOP THE SAME WAY.\x07TELL HER THAT WE BE SQUARE - SHE OWES ME NO MORE.\x07NOW LEAVE ME WITH ME PRECIOUS RUM!",
        'title': 'More Rum for Gunner' },
    'sd1.collectingIngredients': {
        'description': "Solomon O'Dougal needs you to acquire some fine ink for him. As you cannot but it from Lucinda, you are going to have to gather the needed ingredients yourself.",
        'stringAfter': "Found all the ingredients I see? Excellent work.\x07This will cover what's needed to make the ink, but not my services.\x07I have been in the need of some cursed wood and sailing the high seas isn't in my blood.\x07Rumor has it some can be acquired in Royal Caverns in Port Royal, go speak with Jim Wavemonger, he can help.",
        'title': 'Gathering Ingredients' },
    'sd1.deliverFineInk': {
        'description': "Lucinda has crafted a bottle of fine ink out of the ingredients you gathered for her. Bring this to Solomon O'Dougal and see if he has any more for you to do.",
        'stringAfter': "Perfect. My eyes have never seen a bottle of ink of such quality.\x07We'll need a fine tattoo pattern to match the quality of this ink.\x07Go speak with William Turk in the Rowdy Rooster.\x07He should be able to provide you with a tattoo pattern of that quality.",
        'title': "Solomon's Ink" },
    'sd1.deliverTattooPattern': {
        'description': "William Turk has provided you with a rare tattoo pattern Solomon O'Dougal needs. Return it to him so you can claim your reward.",
        'title': 'Special Delivery' },
    'sd1.playBlackjack': {
        'description': 'William Turk has asked you to prove your skills at blackjack before he will help you with a rare tattoo pattern.',
        'title': 'Blackjack Skills' },
    'sd1.playPoker': {
        'description': 'William Turk has asked you to prove your skills at poker before he will help you with a rare tattoo pattern.',
        'title': 'Poker Skills' },
    'sd1.playingCards': {
        'description': 'William Turk has asked you to prove your skills at the card tables before he will help you with a rare tattoo pattern.',
        'stringAfter': "Nice show. Don't wanna be giving out these tattoo patterns to just any ole pirate you know.\x07Take this pattern back to Solomon O'Dougal, I'm sure he'll be pleased.",
        'title': 'Card Skills' },
    'sd1.recoverBlood': {
        'description': "You need to gather blood from bats as one of the ingredients for Solomon O'Dougal's fine ink.",
        'title': 'Blood Ink Ingredient' },
    'sd1.recoverBoneDust': {
        'description': "You need to gather bone dust from skeletons as one of the ingredients for Solomon O'Dougal's fine ink.",
        'title': 'Bone Dust Ink Ingredient' },
    'sd1.recoverCursedWood': {
        'description': 'According to Jim Wavemonger, cursed wood can be found buried around Royal Caverns in Port Royal. They are remnants of an old skeleton camp.',
        'stringAfter': 'Back already? Hope that was not too hard to find, mate\x07Here be the fine ink I promised. Come back soon.',
        'title': 'Buried Cursed Wood' },
    'sd1.recoverGatorSaliva': {
        'description': "You need to gather saliva from alligators as one of the ingredients for Solomon O'Dougal's fine ink.",
        'title': 'Saliva Ink Ingredient' },
    'sd1.recoverNeedle': {
        'description': "You need to gather needles from scorpions as one of the ingredients for Solomon O'Dougal's fine ink.",
        'title': 'Needle Ink Ingredient' },
    'sd1.recoverSulfur': {
        'description': "You need to gather sulfur from wasps as one of the ingredients for Solomon O'Dougal's fine ink.",
        'title': 'Sulfur Ink Ingredient' },
    'sd1.visitJimWavemonger': {
        'description': 'Lucinda needs you to acquire some cursed wood for her. Some can be found in Royal Caverns, a mine in Port Royal, go speak with Jim Wavemonger to find out more.',
        'stringAfter': "W, w, what, who? Cursed wood, indeed, it can be found if ye be motivated enough.\x07The filthy stuff be buried all 'round this cave.\x07Remnants of some old skeleton camp from what I hear. ",
        'title': 'Paying Upfront' },
    'sd1.visitLucinda': {
        'description': "Solomon O'Dougal needs to get his hands on some higher end ink. If you can provide it for him, he will provide you with a tattoo you cannot get anywhere else.",
        'stringAfter': "Fine Ink you say? I've not sold any of that for quite some time.\x07You're going to have to gather the ingredients yourself. Good luck.",
        'stringBefore': 'So, you want something special I gather?\x07The finer inks are hard to come by these days.\x07If you can gather me a supply of fine ink, I will give you a tattoo you cannot get anywhere else.\x07Check with Lucinda to see if she knows where some can be found.',
        'title': 'Special Ink' },
    'sd1.visitWilliamTurk': {
        'description': "Now that Solomon O'Dougal has the ink he needs, he wants you to return with a tattoo pattern of the same quality.\x07William Turk in the Rowdy Rooster should be able to provide such a tattoo.",
        'stringAfter': "Many pirates like yourself ask for my tattoo patterns. Why should I give you one?\x07Maybe if you prove your wits at the card tables, I'll help you out.",
        'title': 'Rare Tattoo Pattern' },
    'sd2.bribeBingham': {
        'description': "Bingham knows the location of Solomon O'Dougal's family portraits. Bribe him in order to get this information.",
        'stringAfter': 'Lovely. These paintings you are looking for, they can be found scattered around several islands.\x07Here is a list of where each stash can be located.',
        'title': "Bingham's Bribe" },
    'sd2.defeatEITC': {
        'description': "Solomon O'Dougal wants to create a distraction for the EITC before going after the paintings. Defeat some EITC guards so that the paintings can be recovered unnoticed.",
        'stringAfter': 'Well done my friend. The eyes of the EITC are surely off of the paintings now.\x07Here is the list of where each stash of paintings is buried, bring them back, hurry!',
        'title': 'EITC Distraction' },
    'sd2.deliverList': {
        'description': "Bingham has provided you with a list of the locations of Solomon O'Dougal's family portraits. Deliver this list to him.",
        'stringAfter': 'I have been to all of these islands. If only I had known these paintings were under my feet.\x07We need to create a distraction for the EITC before we go after them.\x07Take down some EITC guards, that should allow us to recover the paintings unnoticed.',
        'title': 'Painting List' },
    'sd2.deliverPainting': {
        'description': "You have recovered the paintings for Solomon O'Dougal. Deliver one to his cousin, Jim Wavemonger and Solomon O'Dougal will give you a rare tattoo.",
        'title': "Wavemonger's Portrait" },
    'sd2.deliverTattooPattern': {
        'description': "Solomon's family has had some heirlooms stolen by the EITC. He has is a tattoo of the EITC ship containing the heirlooms, bring a copy of to Darby Drydock and see if he recognizes it.",
        'stringAfter': "I have not seen this design in quite some time. It's on an EITC Marauder I finished some years ago.\x07Unfortunately my ship's log has been lost, otherwise I could just look up the owner for you.\x07The log used to be in a crate in front of my shop, but it seems that someone has moved it.\x07Find the crate containing my ship logs and I will tell you who's ship that is.",
        'stringBefore': 'The tattoo on my chest has some meaning behind it.\x07My family got into some conflicts with the EITC, they ended up stealing many of our family heirlooms.\x07All I had was a picture, drawn from memory of the ship that left with my family history.\x07This drawing was then turned into the tattoo you see.\x07If you can help me track down my family heirlooms, I will give you a rare tattoo.\x07Darby Drydock most likely oversaw the building of the ship.\x07Bring this copy of my tattoo to him, he might be able to point us towards the owners.',
        'title': 'Family Valuables' },
    'sd2.findPaintingsA': {
        'description': "One of the stashes of Solomon O'Dougal's paintings is buried on Isla Cangrejos, recover them for him.",
        'title': 'Cangrejos Paintings' },
    'sd2.findPaintingsB': {
        'description': "One of the stashes of Solomon O'Dougal's paintings is buried on Rumrunner's Isle, recover them for him.",
        'title': 'Rumrunner Paintings' },
    'sd2.findPaintingsC': {
        'description': "One of the stashes of Solomon O'Dougal's paintings is buried on Tortuga Island, recover them for him.",
        'title': 'Tortuga Paintings' },
    'sd2.findShipLog': {
        'description': "Darby Drydock's ship logs have been misplaced. They are located in a crate somewhere on Port Royal Island.",
        'stringAfter': 'Here it is, an EITC Marauder that I built a couple years ago.\x07It looks like it should still be in service, that is really all I can tell you though.',
        'title': 'Lost Ship Log' },
    'sd2.recoverFamilyHeirlooms': {
        'description': "Solomon O'Dougal has found out that an EITC ship contains his family heirlooms. Recover these items from an EITC Marauder.",
        'stringAfter': "My family will be pleased, they have been looking for these items for years.\x07Unfortunately the EITC did not store all of my family's heirlooms on ships.\x07A series of paintings of my ancestors were buried across several territories.\x07A Navy guard by the name of Bingham knows the location of these items.\x07If you can find the location of the paintings and recover them, I will reward you well.",
        'title': 'Marauder Hunt' },
    'sd2.visitBingham': {
        'description': "Solomon O'Dougal's family also had a series of paintings stolen from them. Find the location of these painting from a Navy guard named Bingham.",
        'stringAfter': 'I have heard of these paintings. Its a shame for a family to be separated from such things.\x07I am feeling rather generous today, a small bribe should suffice for the information you need.',
        'title': 'Family Portraits' },
    'sd2.visitSolomon': {
        'description': "You have found the identity of the ship containing Solomon O'Dougal's family heirlooms. Give this information to Solomon.",
        'stringAfter': "It's an EITC Marauder? I have always wondered what type of ship it was.\x07I must get the items back from this ship, it has been too long for my family.\x07Take to the sea and bring me back these heirlooms.",
        'title': 'Target Acquired' },
    'spanish.ShipPVPBreadCrumb': {
        'description': 'You have been told that there are challenges to be found in the boundaries of the Caribbean. Go speak to the Shipwright on Isla de la Avaricia to find out more.',
        'stringAfter': "So, you're here to make a name for yourself? Better slow down my friend. Dangerous waters surround you.\x07These seas can be the cruelest of them all, but also the most rewarding for the right pirate.\x07There has been an ongoing battle for control over some islands around here, including this one.\x07Turns out two Pirate Lords got themselves into a battle for the same territory, both stubborn and obnoxious chaps if you ask me.\x07Pierre le Porc heads up the French on Ile d'Etable de Porc and Garcia de la Avaricia leads the Spanish here. Catchy names, don't you think?\x07They are always looking for new pirates to join their fight. I can't lend any advice as to which side to join, though. I just work here...\x07Start off by talking to Garcia de la Avaricia. Maybe he can sway you to his side.",
        'stringBefore': 'A wise pirate can do a lot more with his or her ship than just annoy the local Navy and EITC chaps.\x07With enough courage, a pirate like yourself could establish quite a fine name on the high seas.\x07A fellow Shipwright friend of mine helps out with a little... struggle far out in the Caribbean.\x07If you feel like you are up for a challenge, he might just be able to provide you with one. You can find him on Isla de la Avaricia.',
        'title': 'Caribbean Struggle' },
    'spanish.ShipPVPBreadCrumbLadder': {
        'description': 'You have been told that there are challenges to be found and fame to be had for courageous pirates in the boundaries of the Caribbean.',
        'stringAfter': 'Well, now you understand the little struggle that has been brewing here.\x07I try to stay out of it myself, bad for business.\x07You can return to either Pirate Lord for more work or join the battle as French or Spanish. Good luck my friend.',
        'title': 'Caribbean Struggle' },
    'spanish.ShipPVPFirstTrial': {
        'description': 'To introduce you to his struggle, Garcia de la Avaricia wants you to sink a French ship in the name of the Spanish.',
        'stringAfter': "I hope Garcia de la Avaricia was not too rough on you. He does not always make the best first impression on people.\x07Make sure you give Pierre le Porc a chance as well. He heads up the French struggle and can be found on Ile d'Etable de Porc.\x07Remember to teleport to get to him. Using a dinghy will put you right into battle and you'll only be able to dock here. Good luck.",
        'title': 'For the Spanish!' },
    'spanish.ShipPVPMainLadder': {
        'description': 'Garcia de la Avaricia has accepted you as one of his Spanish recruits. Complete his challenges for you to prove your worth and skill to him.',
        'stringAfter': 'Well, it appears as though there is not much more I can teach you for now.\x07You have proven yourself to be a fine soldier. Spain thanks you dearly.\x07You can now also wear the mark of the Spanish! Go to any Tattoo Artist for a tattoo only my finest pirates have.\x07Check back with me in the future. I may just have more for you to do.',
        'title': 'Fight for the Spanish!' },
    'spanish.ShipPVPSecondTrial': {
        'description': 'To introduce you to his struggle, Pierre le Porc wants you to sink a Spanish ship in the name of the French.',
        'title': 'For the French!' },
    'spanish.ShipPVPTaskA': {
        'description': 'Garcia de la Avaricia wants you to damage French ships as the start of his challenges for you.',
        'stringAfter': "Nice work my friend, these waters can be quite unforgiving.\x07Just dealing plain damage to the French is easy though, I think you are in need of something a bit more challenging.\x07Before, you were not given any restrictions aside from fighting in the name of Spain.\x07This time, I want you to target ships specifically.\x07To make it even more interesting, let's have you do it with your ship and a cannon. Is that enough for you?",
        'stringBefore': "So, I see you think you are good enough to join the fight. The Spanish are proud to have you!\x07Many of my finest soldiers started out as scrappy pirates such as yourself.\x07I put all my fresh recruits through a gauntlet of challenges. Some even make it through to the end.\x07Let's start you off with something light to get your feet wet.\x07Don't forget though, using a dinghy on this island will throw you right into battle and you will only be able to dock at this island.\x07If you have a desire to visit those scurvy French pirates, be sure to teleport to their miserable excuse for an island. ",
        'title': 'Getting Your Feet Wet' },
    'spanish.ShipPVPTaskB': {
        'description': 'As your next challenge, Garcia de la Avaricia wants you to sink French ships using only your ship skills.',
        'title': 'Sailing Skills' },
    'spanish.ShipPVPTaskB_C': {
        'description': 'Garcia de la Avaricia wants to give you a challenge after your first task. Sink French ships using only your ship.',
        'stringAfter': "Excelente! So far I must say you have exceeded my expectations. Unfortunately my next challenge may not be as forgiving.\x07Any of my soldiers can take to the seas and sink a French ship or two eventually.\x07It takes true skill to do it without sinking though. Not much celebrating a pirate can do after sinking you know.\x07Let's see you take down some French ships without sinking that fancy boat of yours.\x07You'll loose credit for French ships sunk if you do. Give the cannon a rest also. Use only your ship for this challenge.",
        'title': 'Specific Targets' },
    'spanish.ShipPVPTaskC': {
        'description': 'As your next challenge, Garcia de la Avaricia wants you to sink French ships using only your cannon skills.',
        'title': 'Cannon Skills' },
    'spanish.ShipPVPTaskD': {
        'description': 'Garcia de la Avaricia wants to see if you can target French pirates using only your ship skills.',
        'title': 'Broadsides For Pirates' },
    'spanish.ShipPVPTaskD_E': {
        'description': 'Garcia de la Avaricia wants to see if you can target French pirates using your ship and cannon skills.',
        'stringAfter': "I can almost hear those scurvy French pirates whimpering. Excelente!\x07So far I must say you have exceeded my expectations. Unfortunately my next challenge may not be as forgiving.\x07Any of my soldiers can take to the seas and sink a French ship or two eventually.\x07It takes true skill to do it without sinking though. Not much celebrating a pirate can do after sinking you know.\x07Let's see you take down some French ships without sinking that fancy rig of yours.\x07You'll loose credit for French ships sunk if you do. Give the cannon a rest also. Use only your ship for this challenge.",
        'title': 'Unlucky French Pirates' },
    'spanish.ShipPVPTaskE': {
        'description': 'Garcia de la Avaricia wants to see if you can target French pirates using only your cannon skills.',
        'title': 'Cannons For Pirates' },
    'spanish.ShipPVPTaskF': {
        'description': 'Garcia de la Avaricia wants you to sink French ships using only your ship skills. He wants you to do this without sinking your ship.',
        'stringAfter': "I bet those French misfits are starting to worry. If only I had more soldiers like you.\x07Keep it up and we will have these islands in no time.\x07I think it is time you dust off that cannon. Let's see you take down some more French ships without sinking.\x07This time though, use only your cannon skills to do it. Good luck.",
        'title': 'Sinking Is Easy' },
    'spanish.ShipPVPTaskG': {
        'description': 'Garcia de la Avaricia wants you to sink French ships using only your cannon skills. He wants you to do this without sinking your ship.',
        'stringAfter': 'Very impressive, amigo. I hear Pierre shaking in his boots as we speak.\x07If we hit them hard now, we might just be able to tip this battle in our favor.\x07Use the skills you have gained to deal a large amount of damage to French ships using your ship and your cannon skills.',
        'title': 'Cannon Streak' },
    'spanish.ShipPVPTaskH': {
        'description': 'Garcia de la Avaricia wants you to defeat French pirates using only your ship skills. He wants you to do this without sinking your ship.',
        'stringAfter': 'Finally, some decent progress being made around here! Nothing like the smell of fresh Spanish gunpowder.\x07I hope you did not wear out a broadside or two. This time I will have you use only your cannon again.\x07Defeat some more French pirates using only your cannon skills and of course, do it without sinking.',
        'title': 'Pirate Broadside Streak' },
    'spanish.ShipPVPTaskI': {
        'description': 'Garcia de la Avaricia wants you to defeat French pirates using only your cannon skills. He wants you to do this without sinking your ship.',
        'stringAfter': 'Very impressive, amigo. I hear Pierre shaking in his boots as we speak.\x07If we hit them hard now, we might just be able to tip this battle in our favor.\x07Use the skills you have gained to deal a large amount of damage to French ships using your ship and your cannon skills.',
        'title': 'Pirate Cannon Streak' },
    'spanish.ShipPVPTaskJ': {
        'description': 'Garcia de la Avaricia wants you to deal a large amount of damage to French ships using only your ship.',
        'title': 'Massive Ship Damage' },
    'spanish.ShipPVPTaskJ_K': {
        'description': 'Garcia de la Avaricia wants you to deal a large amount of damage to French ships using your ship and cannons.',
        'stringAfter': 'At times like this I think this battle will never end. Pierre and his French pirates matched your efforts and more.\x07We need a grand display of destruction if we are to hold this island.\x07Head to the seas. A great deal of ship damage against the French onslaught without sinking should put them back in their place.',
        'title': 'Massive Damage' },
    'spanish.ShipPVPTaskK': {
        'description': 'Garcia de la Avaricia wants you to deal a large amount of damage to French ships using only your cannons.',
        'title': 'Massive Cannon Damage' },
    'spanish.ShipPVPTaskL': {
        'description': 'Garcia de la Avaricia wants you to use your ship to deal a large amount of damage to French ships without sinking.',
        'stringAfter': 'Glorioso! I believe that almost did the job.\x07Each time those French swine launch an attack we need to ensure our response is fitting.\x07Finish our response by dealing more damage to French ships without sinking. This time though, use only your cannon.',
        'title': 'Ship Damage Streak' },
    'spanish.ShipPVPTaskM': {
        'description': 'Garcia de la Avaricia wants you to use your cannons to deal a large amount of damage to French ships without sinking.',
        'stringAfter': 'At last, we are starting to see a difference out there! Your efforts have proven to be one of a well trained soldier.\x07Hopefully next time they attack, I will have you at my disposal.\x07You are nearing the end of my challenges, but as always, I have saved the hardest for last.\x07Show me you are as good as I think you are. Defeat a large amount of French ships. Feel free to use any means to do so.',
        'title': 'Cannon Damage Streak' },
    'spanish.ShipPVPTaskN': {
        'description': 'Garcia de la Avaricia wants you to sink a large amount of French ships. You can use any means to do so.',
        'stringAfter': 'Well amigo, our time together is coming to an end, for now.\x07I have only one more challenge for you, one that I save for my most talented recruits.\x07Accomplish this challenge and you will be forever honored in the hearts of Spaniards everywhere.',
        'title': 'Ships In Bulk' },
    'spanish.ShipPVPTaskN_O': {
        'description': 'Garcia de la Avaricia wants you to defeat a large amount of French ships and French pirates. You can use any means to do so.',
        'stringAfter': 'Well my amigo, our time together is coming to an end, for now.\x07I have only one more challenge for you, one that I save for my most talented recruits.\x07Accomplish this challenge and you will be forever honored in the hearts of Spaniards everywhere.',
        'title': 'Bulking Up' },
    'spanish.ShipPVPTaskO': {
        'description': 'Garcia de la Avaricia wants you to defeat a large amount of French pirates. You can use any means to do so.',
        'title': 'Pirates In Bulk' },
    'spanish.ShipPVPTaskP': {
        'description': 'As your final challenge, Garcia de la Avaricia wants you to deal a large amount of damage to French ships without sinking.',
        'title': 'A True Spaniard' },
    'spanish.ShipPVPVisitLordA': {
        'description': 'Garcia de la Avaricia is a Pirate Lord currently in control of Isla de la Avaricia. Go speak to him about joining his struggle.',
        'stringAfter': "You? Fighting for the Spanish? Well... I cannot say whether or not that will work.\x07You see, I am in great need of talent on this island and I believe we already have someone to clean up after the monkey...\x07I hope that did not come off the wrong way... See these islands are a bit different. They're not your average patch of sand and palm trees.\x07Use a dinghy on this island and you will be thrown right into battle, unable to dock anywhere but this island.\x07The same goes for those French swine and their scrap of an island.\x07If your intentions are to visit the French island, Ile d'Etable de Porc, be sure to teleport and keep your ship safe.\x07Now, how about you prove to me that you can hold your own out there?\x07If you are successful come back and I will have more work for you... that is if you wish to fight for the Spanish.",
        'title': 'Pirate Lord Avaricia' },
    'spanish.ShipPVPVisitLordB': {
        'description': "Pierre le Porc is a Pirate Lord currently in control of Ile d'Etable de Porc. Go speak to him about joining his struggle.",
        'stringAfter': "Listen here. I don't have much time to waste with ye. I run a tight ship here with little room for error.\x07At any moment the tables can turn and that swine Garcia de la Avaricia and his misfits will triumph.\x07If ye feel like making a difference here yer going to have to show me yer worth.\x07Let's see if ye can score one for the French! If so, return to me and I'll have more for ye to do.",
        'title': 'Pirate Lord Le Porc' },
    'tc.1visitJoshamee': {
        'description': 'Gibbs is the First Mate of the Black Pearl. He usually sits in the Faithful Bride tavern on Tortuga.',
        'stringAfter': "Fancy a game of chess?\x07Not much of a player me-self... but I've got me eye on a \x01slant\x01certain\x02 chess set... one made of imperial gold and Turkish silver!\x07Aye! It be treasure I'm talkin' about. But there's a catch, see?\x07Only a person \x01slant\x01handy\x02 in games will be able to find this here treasure. \x07Are you such a person? I'll be needin' a demonstration.",
        'title': 'Visit Joshamee Gibbs' },
    'tc.2poker': {
        'description': 'Play poker to prove your skill with games to Joshamee.',
        'title': 'Win At Poker' },
    'tc2.1deliverChess': {
        'description': 'Deliver the chess set to Joshamee Gibbs in Tortuga.',
        'title': 'Deliver Chess Set' },
    'tf.1visitTia': {
        'description': 'Find Tia Dalma near her home in Pantano River, Cuba.',
        'title': 'Visit Tia Dalma' },
    'tf2.1deliverFigurines': {
        'description': 'Return the figurines to Tia Dalma in Cuba.',
        'title': 'Deliver Figurines' },
    'timed.1test': {
        'description': 'Fiabola tests how fast you can defeat alligators.',
        'stringAfter': "Not bad.\x07Now let's see how fast you can sink ships?",
        'stringBefore': "Let's see if you can defeat those Alligators within the time limit!",
        'title': 'Defeat Alligators Quickly' },
    'timed.2test': {
        'description': 'Fiabola tests how fast you can sink ships.',
        'stringBefore': 'Are you ready to start sinking?',
        'title': 'Sink Ships Quickly' },
    'timed.3test': {
        'description': 'The remedy looses its power quickly so deliver it ASAP.',
        'stringAfter': 'Thanks for saving me!',
        'stringBefore': 'Deliver this remedy as fast as you can cause it expires quickly.',
        'title': 'Deliver Remedy Quickly' },
    'tm.1visitWill': {
        'description': 'Find Will Turner in the warehouse on Port Royal.',
        'title': 'Visit Will Turner' },
    'tm2.1deliverMedals': {
        'description': 'Deliver the Navy medals to Will Turner in the warehouse on Port Royal.',
        'stringAfter': "White gold is really quite beautiful. 'Tis a pity they shaped it so poorly into these crude forms.\x07In order to forge white gold properly, I'll need a reagent.\x07The East India Trading Company will sometimes transport this kind of material by sea.\x07You will know the containers - they are marked with the symbol of the sun.",
        'title': 'Deliver Navy Medals' },
    'tm2.2recoverReagent': {
        'description': 'Recover gold forging reagent from East India Trading Company ships.',
        'title': 'Recover Reagent' },
    'tm2.2recoverReagents': {
        'description': 'Reagents are chemical mixtures added into the melted white gold that give it more strength when it cools.',
        'title': 'Recover Reagents' },
    'tpt.1visitTia': {
        'description': 'Find Tia Dalma to learn the secrets of Teleportation.',
        'stringAfter': 'You want to travel from one island to another...\x07... without a ship, yes?\x07There is a totem that grants this power...\x07... this totem I have. But I demand payment... \x07Bring me some things that I need...\x07... and I will give you what you desire.',
        'stringBefore': "You wanna travel from one island to another in the blink of an eye? \x07The seas of the Caribbean are vast and there's a quicker way to cross them than by ship. \x07You can command winds themselves to carry you 'cross the Caribbean. \x07Seek out \x01slant\x01Tia Dalma\x02 on the island of Cuba. She will show you the way.",
        'title': 'Build Teleport Totem' },
    'tpt.2recoverArtifact': {
        'description': 'Search buried treasure chests for an artifact to create a teleportation totem.',
        'title': 'Recover Artifact From Tortuga' },
    'tptc.1visitTiaDalma': {
        'description': 'Visit Tia Dalma so that she might grant you teleportation access to Cuba.',
        'stringAfter': 'I see that you have returned. Would you like to return here whenever you wish?\x07Get these things for me and I will give you something special..',
        'title': 'Return To Tia Dalma' },
    'tptcPayment': {
        'description': 'Gather items for payment to Tia Dalma',
        'stringAfter': 'Good work!\x07I have created a totem so that you might return here whenever you wish. It is yours, as promised.',
        'title': 'Payment For Tia' },
    'tptcr1.1NavyCoats': {
        'description': 'Defeat Navy to acquire a Navy Coat.',
        'title': 'Acquire A Navy Coat' },
    'tptcr1.2FlyTrapRoots': {
        'description': 'Defeat a Fly Trap to acquire a root.',
        'title': 'Acquire A Fly Trap Root' },
    'tptcr2.1payment': {
        'description': 'Alligator scales are used as a primitive dental floss among island natives - pirates? Not so much since most of them have green, rotting teeth.',
        'title': 'Acquire Scales' },
    'tptcr2.2payment': {
        'description': 'Fly trap root makes for a tasty root beer that Tia sells in the summer months to make extra money.',
        'title': 'Acquire Fly Trap Roots' },
    'tptcr2.Payment': {
        'description': 'Gather items for payment to Tia Dalma',
        'stringAfter': 'Good work!\x07I have created a totem so that you might return here whenever you wish. It is yours, as promised.',
        'title': 'Payment For Tia' },
    'tptpdf.1visitRomany': {
        'description': 'Find Romany Bev in Padres Del Fuego to acquire teleportation access to Padres Del Fuego',
        'stringAfter': 'So, you would like to visit my home by only the whimsy of your thoughts? This is possible. \x07However, before I can grant this request, I must enlist your aid in our struggle \x07against powerful Undead forces that have overrun much of the island. \x07Do your part in our struggle and return to me for your reward.',
        'title': 'Visit Romany Bev' },
    'tptpdf.2FindArtifact': {
        'description': 'Search for buried treasure on Padres Del Fuego to find the Eye of Nabai.',
        'stringAfter': 'Hold the Eye in your hands. I will perform the ritual to release the chains on its power... \x07...I am finished. While you possess the Eye of Nabai, you have the power of teleportation to Padres Del Fuego. \x07Good luck in your travels.',
        'stringBefore': 'Thank you for what you have done. To gain the power you desire, you must find a specific artifact linked to this Isle... \x07...It is the Eye of Nabai, and with it, I can grant your request.',
        'title': 'The Eye of Nabai' },
    'tptpdfPayment': {
        'description': 'As a favor to Romany Bev, you must go and fight the Undead Forces of Padres Del Fuego. \x07They can be found in the interior of the island.',
        'stringAfter': 'Thank you for your efforts. \x07 Retrieve the Jeweled Eye of Nabai and I will adorn your totem with it. \x07Thus will your totem be empowered.',
        'title': 'Fight the Undead of Padres Del Fuego' },
    'tptpdfr1.1FaceWeakUndead': {
        'description': 'Defeat six Undead Brigands',
        'title': 'Defeat Undead Brigands' },
    'tptpdfr1.2FaceStrongerUndead': {
        'description': 'Defeat six Undead Grenadiers.',
        'title': 'Defeat Undead Grenadiers' },
    'tptpdfr1.3FaceStrongUndead': {
        'description': 'Defeat six Undead Gypsies.',
        'title': 'Defeat Undead Gypsies' },
    'tptpdfr2.1payment': {
        'description': 'These Undead Slashers are very vicious fighters that attack innocent people so defeating them makes Romany Bev happy.',
        'title': 'Defeat Undead Slashers' },
    'tptpdfr2.2payment': {
        'description': 'Undead Grenadiers are doing serious damage to Padres with all their bomb throwing and Romany Bev wants them dead!',
        'title': 'Defeat Undead Grenadiers' },
    'tptpdfr2.3payment': {
        'description': "Too many Undead Gypsies can diminish Romany Bev's power and ridding Padres of these is a good start!",
        'title': 'Defeat Undead Gypsies' },
    'tptpdfr2.Payment': {
        'description': 'As a favor to Romany Bev, you must go and fight the Undead Forces of Padres Del Fuego.',
        'stringAfter': 'Thank you for your efforts. \x07Retrieve the Jeweled Eye of Nabai and I will adorn your totem with it. \x07Thus will your totem be empowered.',
        'title': 'Fight the Undead of Padres Del Fuego' },
    'tptpr.1visitLucinda': {
        'description': 'Visit Lucinda so that she might grant you teleportation access to Port Royal.',
        'stringAfter': 'Would you like to add the power of coming to this island at your whim? \x07Then you must prove yourself to me and to the island. \x07First, you must strike a blow against the infestation of undead.',
        'title': 'Teleportation Access to Port Royal' },
    'tptpr.2LucindasTrust': {
        'description': "Gain Lucinda's trust by defeating skeletons.",
        'stringAfter': "I can sense the effect of your efforts fighting the undead infestation. \x07For your next task, you must face another unnaturally large presence on this island.\x07 The Navy's Fort is a detestable presence on the island. Let the Navy know of the island's disapproval.",
        'title': "Gain Lucinda's Trust" },
    'tptpr.2gainLucindaTrust': {
        'description': "Gain Lucinda's trust by defeating skeletons in the wilds of Port Royal.",
        'stringAfter': "I can sense the effect of your efforts fighting the undead infestation. \x07For your next task, you must face another unnaturally large presence on this island.\x07 The Navy's Fort is a detestable presence on the island. Let the Navy know of the island's disapproval.",
        'title': "Gain Lucinda's Trust" },
    'tptpr.3LucindasTrust': {
        'description': "Further gain Lucinda's trust by defeating Navy.",
        'stringAfter': 'You have proven yourself to me and to the island. \x07The artifact you require is buried somewhere on this island.\x07It is the first medal of the first Navy Soldier to set foot here. \x07Find it and bring it to me.',
        'title': "Gain Lucinda's Trust" },
    'tptpr.3gainLucindaTrustAgain': {
        'description': "Further gain Lucinda's trust by defeating Navy.",
        'stringAfter': 'You have proven yourself to me and to the island. \x07The artifact you require is buried somewhere on this island.\x07It is the first medal of the first Navy Soldier to set foot here. \x07Find it and bring it to me.',
        'title': "Gain Lucinda's Trust" },
    'tptpr.4recoverFirstMedal': {
        'description': 'Search amongst the buried treasure in Port Royal to find one of these medals.',
        'stringAfter': 'You have returned. Hand me the medal. \x07Wait while I perform the incantation to join the energies of the medal with the spirit of the island... \x07...It is done. Port Royal is never more than a clear thought away.',
        'title': 'Find Medal' },
    'tptr1.1recoverBat': {
        'description': 'Recover bat wings by defeating cave bats.',
        'title': 'Cave Bat Wings' },
    'tptr1.1tortugaPayment': {
        'description': 'Among Gypsies, Alligator teeth are considered a currency the same as gold or silver.',
        'title': 'Alligator Teeth' },
    'tptr1.2recoverWasp': {
        'description': 'Acquire dire wasp essences by defeating Dire Wasps.',
        'title': 'Essence of the Dire Wasp' },
    'tptr1.2tortugaPayment': {
        'description': 'Alligator tails are highly prized for their curative oils and a material for fine belts.',
        'title': 'Alligator Tails' },
    'tptr1.3recoverLeaf': {
        'description': 'Acquire a Fly Trap Leaf by defeating a Fly Trap.',
        'title': 'Fly Trap Leaves' },
    'tptr1.3tortugaPayment': {
        'description': 'Tia Dalma uses fly trap gizzards in many of her potions.',
        'title': 'Fly Trap Leaves' },
    'tptr2.TortugaPayment': {
        'description': 'Gather items for payment to Tia Dalma.',
        'stringAfter': 'Your payment is made. \x07The totem must be bound to the land...\x07... the land you wanna return to.\x07Go to Tortuga and return with an artifact.\x07With this... we will bind your totem.',
        'title': 'Payment For Tia' },
    'tptr2Payment': {
        'description': 'Gather items for payment to Tia Dalma',
        'stringAfter': 'Your payment is made. \x07The totem must be bound to the land...\x07... the land you wanna return to.\x07Go to Tortuga and return with an artifact.\x07With this... we will bind your totem.',
        'title': 'Payment For Tia' },
    'tr.1visitElizabeth': {
        'description': "Meet with Elizabeth Swann in the Governor's mansion on Port Royal.",
        'stringAfter': "I'm glad you came. I have a potentially lucrative proposition for you.\x07A priceless treasure has resurfaced - it's called \x01slant\x01The Nine Rogues\x02.\x07Nine legendary pirates had their portraits painted by an unknown but soon-to-be famous Dutch artist.\x07These nine brigands mocked each other's appearance on canvas, sparking a brawl that left several of them with serious injuries.\x07It was decided by all present that the paintings should be discarded rather than provoke future incidents...\x07... a decision the Nine Rogues would come to regret! \x07A few years later, the now-famous painter died of consumption, and the portraits are now considered \x01slant\x01priceless\x02.\x07My father was obsessed with The Rogues. He often spoke of going in search of them.\x07Now that he's gone missing, I hold out hope that word of the paintings might lead to news of my father.\x07The portraits were in the possession of the painter's nephew for a time. His name is Luther.\x07Luther was spotted last week sailing with the Royal Navy. If you capture him we may learn where to begin our search...",
        'title': 'Visit Elizabeth Swann' },
    'tr.2captureLuther': {
        'description': 'Capture Luther aboard a Navy ship.',
        'title': 'Capture Luther' },
    'tr.3visitElizabeth': {
        'description': 'Return to Elizabeth Swann in Port Royal.',
        'title': 'Return To Elizabeth' },
    'tr2.1deliverPaintings': {
        'description': 'Return with the Nine Rogues to Elizabeth Swann in Port Royal.',
        'title': 'Return To Elizabeth' },
    'trr.1visitBarbossa': {
        'description': "Meet with Captain Barbossa in the treasure grotto beneath Devil's Anvil island.",
        'title': 'Find Captain Barbossa' },
    'trr2.1deliverRings': {
        'description': "Bring the Rhineworth rings to Captain Barbossa in the treasure grotto on Devil's Anvil island.",
        'stringAfter': "All ten rings? Well done, you beloved barnacle. Now listen close...\x07Not to cast a pall on a scrap of piratin' carried out admirably... \x01slant\x01but\x02...\x07There's another ring! Ten rings for ten fingers, 'cept Rhineworth had more fingers than most...\x07Eleven to be exact! 'Twas the cursed little one that did 'im in, it did.\x07Find me \x01slant\x01that\x02 ring... and you can keep the lot here.\x07Seein' as you haven't grown a beard as long as you are tall, seems the legend of the rings be nothin' but an ol' wive's tale.",
        'title': 'Deliver Rhineworth Rings' },
    'trr2.2recoverRing': {
        'description': 'Plunder the 11th and final Rhineworth ring from skeletons.',
        'title': 'Recover Final Ring' },
    'trr2.2recoverRings': {
        'description': 'Plunder the final Rhineworth rings from the Undead.',
        'title': 'Recover Rings' },
    'tt.1visitJack': {
        'description': "Find Jack Sparrow in the quest to find Rudyard's treasure.",
        'stringAfter': "Today's your lucky day, mate. I've caught wind of one of Rudyard's golden teeth, aye!\x07Not \x01slant\x01too\x02 much wind - ol' Rudyard had breath like the Kraken! \x07Fortunately, said tooth has long parted from the dearly departed, savvy?\x07Don't know Rudyard, aye? A murderous rotten fiend he was... and a first rate pirate!\x07They say he didn't crack a smile when his crew mutinied. Left him for dead on a forsaken spit of an island, they did.\x07But Rudyard had the last laugh. Lacking the trusting nature of non-pirates, he buried the ship's treasure...\x07... and the \x01slant\x01map\x02 to the treasure, he carved into a mouthful of golden teeth. Pulled out his original teeth to make room - true story!\x07They say a single golden molar could finance a feast for an entire Navy fleet... or one gluttonous pirate crew, anyway.\x07One such nugget was spotted in the mouth of a certain skeletal pirate not far from here. \x07Defeat 25 of said skeletons and collect teeth that seem to you like the one. Chances are you will find Rudyard's tooth.",
        'title': 'Visit Jack Sparrow' },
    'tt.2recoverTeeth': {
        'description': "Defeat skeletons to recover Rudyard's golden teeth.",
        'title': 'Recover Golden Teeth' },
    'tt.2recoverTooth': {
        'description': "Defeat skeletons to recover one of Rudyard's golden teeth.",
        'title': 'Recover Golden Tooth' },
    'tt2.1deliverTeeth': {
        'description': "Bring Rudyard's teeth to Jack Sparrow in Tortuga.",
        'stringAfter': "Rudyard's teeth! You found them all, mate. Must have been quite a sight between those rubbery lips of his...\x07... and this map is as crooked as Rudyard's smile. Bring back what's buried at the X... and I'll honor our 40/60 split forthwith!",
        'title': 'Visit Jack Sparrow' },
    'tt2.2recoverGold': {
        'description': "Find and dig up Rudyard's buried treasure on Isla Cangrejos. One would be wise to look far off the beaten path.",
        'title': "Recover Rudyard's Gold" },
    'vdu4.0visitTiaDalma': {
        'description': 'Tia needs your help. Come to her aid and you will be soundly rewarded.',
        'stringAfter': 'Someone has violated my home and taken something of value to me.\x07But who would dare do this? Tia has her suspicions.\x07Speak to Romany Bev in Padres Del Fuego to confirm them.\x07For your assistance, you will be rewarded with a greater Voodoo Doll than you have ever wielded.',
        'title': 'Visit Tia Dalma' },
    'vdu4.1visitRomanyBev': {
        'description': 'Seek Answers From Romany Bev.',
        'stringAfter': 'I know who sent you. She was violated, and seeks answers as to who, and why.\x07I cannot say why she was robbed, but I can say with certainty that Jolly Roger was behind it.\x07Tell Tia this, and help her in whatever way you can.\x07Jolly Roger is a devious, evil creature whose schemes are a threat to us all.',
        'stringBefore': 'DIALOGUE ERROR',
        'title': 'Stolen Relic' },
    'vdu4.2returnToTia': {
        'description': "Deliver Romany's Message To Tia Dalma.",
        'stringAfter': "My suspicions have been confirmed.\x07Gather these spell ingredients for me.\x07Won't you help Tia locate what was taken from her?",
        'title': 'Return To Tia Dalma' },
    'vdu4.4retrieveFirstPieceOfRelic': {
        'description': 'Recover the First Piece of the Relic.',
        'title': 'The First Relic Piece' },
    'vdu4.5retrieveRestOfPiecesOfRelic': {
        'description': 'With the first piece as your guide, recover the remaining pieces of the relic.',
        'stringAfter': "Once again, it is whole. But it is not the same.\x07The relic you have returned to me once contained a piece of the spirit of someone important to me.\x07That spirit shard has been removed, leaving only a worthless husk.\x07My only hope is that the relic's destruction will liberate the spirit shard from whatever prison Jolly Roger has constructed.",
        'title': 'Additional Relic Pieces' },
    'vdu4.6returnToTia': {
        'description': 'Return the Destruction Spell Components to Tia Dalma',
        'title': 'Return Spell Components' },
    'vdu4r1.10acquireCangrejosBattleEarth': {
        'description': 'Defeat something hostile on Isla Cangrejos and take a sample of the ground you fought on.',
        'title': 'Earth of Isla Cangrejos' },
    'vdu4r1.11acquirePerdidaBattleEarth': {
        'description': 'Defeat something hostile on Isla Perdida and take a sample of the ground you fought on.',
        'title': 'Earth of Isla Perdida' },
    'vdu4r1.12acquireCutthroatBattleEarth': {
        'description': 'Defeat something hostile on Cutthroat and take a sample of the ground you fought on.',
        'title': 'Earth of Cutthroat' },
    'vdu4r1.13acquireTormentaBattleEarth': {
        'description': 'Defeat something hostile on Isla Tormenta and take a sample of the ground you fought on.',
        'title': 'Earth of Isla Tormenta' },
    'vdu4r1.14acquireOutkastBattleEarth': {
        'description': 'Defeat something hostile on Outcast and take a sample of the ground you fought on.',
        'title': 'Earth of Outcast' },
    'vdu4r1.15acquireAnvilBattleEarth': {
        'description': "Defeat something hostile on Devil's Anvil and take a sample of the ground you fought on.",
        'title': "Earth of Devil's Anvil" },
    'vdu4r1.1acquireMastsOfSunkenShips': {
        'description': "Sink ships and recover their masts for Tia's Spell.",
        'title': 'Sunken Ship Masts' },
    'vdu4r1.2acquireSkeletonBones': {
        'description': "Defeat Skeletons and take their bones for Tia's Spell.",
        'title': 'Skeleton Bones' },
    'vdu4r1.3acquirePortRoyalBattleEarth': {
        'description': 'Defeat something hostile on Port Royal and take a sample of the ground you fought on.',
        'title': 'Earth of Port Royal' },
    'vdu4r1.4acquireTortugaBattleEarth': {
        'description': 'Defeat something hostile on Tortuga and take a sample of the ground you fought on.',
        'title': 'Earth of Tortuga' },
    'vdu4r1.5acquirePadresDelFuegoBattleEarth': {
        'description': 'Defeat something hostile on Padres Del Fuego and take a sample of the ground you fought on.',
        'title': 'Earth of Padres Del Fuego' },
    'vdu4r1.6acquireKingsheadBattleEarth': {
        'description': 'Defeat something hostile on Kingshead and take a sample of the ground you fought on.',
        'title': 'Earth of Kingshead' },
    'vdu4r1.7acquireCubaBattleEarth': {
        'description': 'Defeat something hostile on Cuba and take a sample of the ground you fought on.',
        'title': 'Earth of Cuba' },
    'vdu4r1.8acquireRumrunnersBattleEarth': {
        'description': "Defeat something hostile on Rumrunner's and take a sample of the ground you fought on.",
        'title': "Earth of Rumrunner's Isle" },
    'vdu4r1.9acquireDriftwoodBattleEarth': {
        'description': 'Defeat something hostile on Driftwood and take a sample of the ground you fought on.',
        'title': 'Earth of Driftwood' },
    'vdu4r2.1retrieveScorpionVenom': {
        'description': 'Acquire venom from defeated scorpions.',
        'title': 'Scorpion Venom' },
    'vdu4r2.2retrieveAlligatorTeeth': {
        'description': 'Acquire teeth from defeated alligators.',
        'title': 'Alligator Teeth' },
    'vdu4r2.3retrieveWaspStinger': {
        'description': 'Acquire stingers from defeated wasps.',
        'title': 'Wasp Stingers' },
    'vdu4r2.4retrieveCrabClaw': {
        'description': 'Acquire claws from defeated crabs.',
        'title': 'Crab Claws' },
    'vdu4r2.5retrieveBatClaw': {
        'description': 'Acquire claws from defeated bats.',
        'title': 'Bat Claws' },
    'vdu4r2.6retrieveBattleSaltWater': {
        'description': 'Sink Skeleton Ships and gather the salt water from the battles.',
        'title': 'Battle-Touched Salt Water' },
    'vdul5.1visitTia': {
        'description': 'Tia calls for your help again. She will upgrade your Voodoo Doll if you assist her.',
        'stringAfter': "You did well on the last quest, and I must trust you with another. And for this help, another doll will be yours.\x07I need to contact my long departed friend.\x07 I fear how a piece of his spirit could be used by Jolly Roger and I need some personal items to talk to his departed soul.\x07Bring me some Spanish armor of the type he once wore,\x07A lock of hair that's found its way on a French ghost ship,\x07 and an earring of his buried at Fort Kingshead.\x07Bring dem here.",
        'stringBefore': '',
        'title': 'Visit Tia Dalma' },
    'vdul5r1.1acquireArmor': {
        'description': "Spanish Armor of the type Tia's friend once wore can be found on undead Spanish Conquistadors on Cutthroat Island.",
        'stringAfter': '',
        'stringBefore': '',
        'title': 'Spanish Armor' },
    'vdul5r1.2acquireHair': {
        'description': 'The lock of hair can be found in a sea chest on a French Ghost Ship.',
        'stringAfter': '',
        'stringBefore': '',
        'title': 'A Lock of Hair' },
    'vdul5r1.3findEarring': {
        'description': "The earring Tia's friend proudly wore is now buried within Fort Kingshead. Venture up through the tree-lined path and into the village. Take friends to watch your back while you search!",
        'stringAfter': '',
        'stringBefore': '',
        'title': 'A Buried Earring' },
    'vdul5r1Heirlooms': {
        'description': "Tia must have her friend's personal items to contact him. Gather them and return to Tia.",
        'stringAfter': "You work fast.  Your spirit is strong.\x07The spell is working.  I can hear him.  He's in pain.  I hear his screams.\x07Jolly Roger must pay!\x07Go to Murky Hollow on Port Royal.  Defeat General Bloodless and his vile witchdoctors.  Then return to me.\x07Jolly Roger will pay for my friend's suffering!",
        'stringBefore': '',
        'title': 'The Heirlooms' },
    'vdul5r2.1defeatUndead': {
        'description': "General Bloodless' minions surround him in Murky Hollow.",
        'stringAfter': '',
        'stringBefore': '',
        'title': "Bloodless' Minions" },
    'vdul5r2.2defeatGeneralBloodless': {
        'description': 'General Bloodless has been seen in the shadows of the Murky Hollow on Port Royal.',
        'stringAfter': '',
        'stringBefore': '',
        'title': 'General Bloodless' },
    'vdul5r2FinalGeneral': {
        'description': 'Defeat General Darkhart and his minions.',
        'stringAfter': '',
        'stringBefore': '',
        'title': 'The Final General' },
    'vdul5r2FirstGeneral': {
        'description': 'Defeat General Bloodless and his minions.',
        'stringAfter': "Good work.  But you are not finished.\x07Destroy General Hex.  He is hiding like a coward in the Misty Mire,  a swamp in Tortuga.\x07But he's protected by many undead,  so be careful man. Watch yer back!",
        'stringBefore': '',
        'title': 'The First General' },
    'vdul5r3.1defeatUndead': {
        'description': "General Hex's minions surround him in Misty Mire.",
        'stringAfter': '',
        'stringBefore': '',
        'title': "Hex's Minions" },
    'vdul5r3.2defeatGeneralHex': {
        'description': 'General Hex haunts the Misty Mire, a swamp in Tortuga. The General is protected by ferocious undead bodyguards!',
        'stringAfter': '',
        'stringBefore': '',
        'title': 'General Hex' },
    'vdul5r3SecondGeneral': {
        'description': 'Defeat General Hex and his minions.',
        'stringAfter': "Tia thanks you.  You brave and gonna become more famous than Sparrow one day.\x07 Find General Sandspine in the Rat's Nest, a villiage overcome by the undead on Tortuga.\x07 The General is strong. Be careful of his protectors; they is a band of cruel undead. Defeat them all.",
        'stringBefore': '',
        'title': 'The Second General' },
    'vdul5r4.1defeatUndead': {
        'description': "General Sandspine's minions surround him in the Rat's Nest.",
        'stringAfter': '',
        'stringBefore': '',
        'title': "Sandspine's Minions" },
    'vdul5r4.2defeatGeneralSandspine': {
        'description': "General Sandspine is no spineless coward but a fierce, devious fighter.  Find him in Rat's Nest, the lost village of Tortuga.",
        'stringAfter': '',
        'stringBefore': '',
        'title': 'General Sandspine' },
    'vdul5r4ThirdGeneral': {
        'description': 'Defeat General Sandspine and his minions.',
        'stringAfter': "I got one last task for you.\x07 Go to the catacombs on Padres del Fuego. There you will find the undead guarding a General name of Darkhart.\x07Destroy him and you get your doll, and my undying gratitude.  Hurry now. Time's a wasting!",
        'stringBefore': '',
        'title': 'The Third General' },
    'vdul5r5.1defeatUndead': {
        'description': "General Darkhart's minions surround him on the far side of Padres.",
        'stringAfter': '',
        'stringBefore': '',
        'title': "Darkhart's Minions" },
    'vdul5r5.2defeatGeneralDarkhart': {
        'description': 'General Darkheart commands undead forces on the far side of Padres. Find yourself some mates before you dare venture so deep into dangerous territory!',
        'stringAfter': '',
        'stringBefore': '',
        'title': 'General Darkhart' },
    'vsu4.0visitTiaDalma': {
        'description': 'Ask Tia about acquiring a more powerful Voodoo Staff.',
        'stringAfter': 'Tia wonders how powerful you want to be.\x07You seek a greater staff. For this, you must seek out another.\x07Find a man named Roland on Padres Del Fuego. He can fashion the weapon you seek.',
        'title': 'Visit Tia Dalma' },
    'vsu4.1visitRoland': {
        'description': 'Seek out a man named Roland Raggart on Padres Del Fuego',
        'stringAfter': "So, you'd like one of my staffs. ey?\x07As it would happen, I desire greater power as well. Quench my thirst, and I shall quench yours.\x07My sources tell me that East India Trading Company has come into possession of a particular orb, a large cloudy blue orb.\x07They can tell by looking at it that it is valuable. However, they do not have the means to tap into its ever-present energies. I, on the other hand, do.\x07Unfortunately, I have no clue where they've hidden it. Retrieve these components, so that I might receive special sight.",
        'stringBefore': 'DIALOGUE ERROR',
        'title': "Roland's Cloudy Orb" },
    'vsu4.3acquireOrb': {
        'description': "Hunt down the ship from Roland's vision and acquire the orb",
        'stringAfter': 'There is such beauty in great power. The Danger. The Temptation. The Potential!\x07You cannot deny it.\x07But, tragically, the energies are still trapped. You will help me set them free. And then a new staff will be yours.',
        'title': 'The Cloudy Blue Orb' },
    'vsu4.5returnToRoland': {
        'description': 'Return to Roland with the spell components.',
        'title': 'Return to Roland' },
    'vsu4r1.1acquireGatorEyes': {
        'description': 'Acquire alligator eyes',
        'title': 'Alligator Eyes' },
    'vsu4r1.2acquireWasps': {
        'description': 'Acquire wasps and their many eyes.',
        'title': 'Wasps' },
    'vsu4r1.3acquireScorpionEyes': {
        'description': 'Acquire scorpion eyes.',
        'title': 'Scorpion Eyes' },
    'vsu4r1.4acquireBatEyes': {
        'description': 'This type of bat can be found in the caves of Padres Del Fuego.',
        'title': 'Bat Eyes' },
    'vsu4r2.1acquireSkeletonRibs': {
        'description': 'Acquire rib bones from skeletons',
        'title': 'Skeleton Ribs' },
    'vsu4r2.2acquireNavyBadges': {
        'description': 'Acquire Navy badges',
        'title': 'Navy Badges' },
    'vsu4r2.3acquireScorpionStingers': {
        'description': 'Acquire stingers from scorpions',
        'title': 'Scorpion Stingers' },
    'vsu4r2.4acquireCrabShells': {
        'description': 'Acquire crab shells',
        'title': 'Crab Shells' },
    'vsu4r3.1acquireStumpBranch': {
        'description': 'Acquire branches from Stumps.',
        'title': 'Stump Branch' },
    'vsu4r3.2acquireFlyTrapRoot': {
        'description': 'Acquire roots from Fly Traps.',
        'title': 'Fly Trap Roots' },
    'vsu4r3.3acquireWritsOfAuthority': {
        'description': 'Acquire writs of authority from powerful EITC men.',
        'title': 'Writs of Authority' },
    'vsu4r3.4acquireStrongerRibs': {
        'description': 'Acquire rib bones from more powerful skeletons.',
        'title': 'More Skeleton Ribs' },
    'vsul5.1visitRoland': {
        'description': 'Rolland Raggart has sent for you. He offers a Voodoo Staff upgrade.',
        'stringAfter': 'For you, I have an even more powerful staff if you once again assist me in achieving my ends.\x07First,  I need to have a conversation with an East India Trading Company Captain named Elliot Ackers.',
        'stringBefore': '',
        'title': 'Visit Roland Raggart' },
    'vsul5.2captureEITCCaptain': {
        'description': 'Captain Ackers helms an EITC vessel.  Sink his ship to capture him. Then, bring him back to Roland.',
        'stringAfter': '',
        'stringBefore': '',
        'title': 'Capture Captain Ackers' },
    'vsul5.3visitRoland': {
        'description': 'Escort Captain Ackers to Roland',
        'stringAfter': "Captain Ackers was very forthcoming.\x07Five Wooden Statuettes found at the same dig site as the Orb are currently being transported via EITC ships.\x07I want those statuettes. But first, find the good Captain a new home. I hear Rumrunner's Isle is lovely this time of year.\x07Then, find those ships carrying the statuettes.",
        'stringBefore': '',
        'title': 'Escort Captain Ackers' },
    'vsul5.4maroonEITCCaptain': {
        'description': "Maroon Captain Ackers by docking on Rumrunner's Isle.",
        'stringAfter': '',
        'stringBefore': '',
        'title': 'Maroon Captain Ackers' },
    'vsul5.5retrieveStatuettes': {
        'description': 'Acquire the statuettes by defeating EITC ships.',
        'stringAfter': 'I can feel the attraction of the statuettes to the Orb!\x07No wonder the EITC separated them.\nQuickly now, bring me bones from the undead. I need them!',
        'stringBefore': '',
        'title': 'Wooden Statuettes' },
    'vsul5.6acquireHighLevelUndeadBones': {
        'description': 'Undead pirates, witchdoctors and worse can be found on the other side of Padres inside Lava Gorge and the gruesome Catacombs.',
        'stringAfter': 'These bones will do nicely. Now, get for me two very rare items; an EITC Gold-Handle Rapier and an EITC Badge.\x07They are possessed by EITC big-wigs in Kingshead. And they will be a challenge. Be wary of them and their allies.',
        'stringBefore': '',
        'title': 'Bones of the Undead' },
    'vsul5r1.1acquireEITCBadge': {
        'description': "Neban peers down upon the rabble working in Beckett's Quarry on Padres.",
        'stringAfter': '',
        'stringBefore': '',
        'title': 'Defeat Neban' },
    'vsul5r1.2acquireGoldHandleRapier': {
        'description': 'Remington can be found deep within the walls of Kingshead.',
        'stringAfter': '',
        'stringBefore': '',
        'title': 'Defeat Remington' },
    'vsul5r1EITCItems': {
        'description': 'Defeat two powerful EITC goons.',
        'stringAfter': 'Listen to me carefully.  Take the Orb.  Seek out EITC soldiers of all shapes and sizes while possessing the Orb and defeat them.\x07It is very important that these men vary in rank and experience.  When you are done,  return to me, here.  Do you understand?',
        'stringBefore': '',
        'title': 'Rare EITC Items' },
    'vsul5r2.1defeatThugs': {
        'description': 'EITC Thugs can be found in the Royal Caverns on Port Royal',
        'stringAfter': '',
        'stringBefore': '',
        'title': 'EITC Thugs' },
    'vsul5r2.2defeatGrunts': {
        'description': 'EITC Grunts can be found in the village in Kingshead.',
        'stringAfter': '',
        'stringBefore': '',
        'title': 'EITC Grunts' },
    'vsul5r2.3defeatHiredGuns': {
        'description': 'EITC Hired Guns can be found upon the barricades of Kingshead.',
        'stringAfter': '',
        'stringBefore': '',
        'title': 'EITC Hired Guns' },
    'vsul5r2.4defeatMercenaries': {
        'description': "EITC Mercenaries can be found in Beckett's Quarry on Padres",
        'stringAfter': '',
        'stringBefore': '',
        'title': 'EITC Mercenaries' },
    'vsul5r2.5defeatAssassins': {
        'description': "EITC Assassins can be found in Beckett's Quarry on Padres",
        'stringAfter': '',
        'stringBefore': '',
        'title': 'EITC Assassins' },
    'vsul5r2VariousEITC': {
        'description': 'Defeat EITC soldiers of all shapes and sizes.',
        'stringAfter': '',
        'stringBefore': '',
        'title': 'Seeking Out The EITC' },
    'wd.1visitTia': {
        'description': 'Find Tia Dalma in Cuba to receive training in a new weapon.',
        'stringAfter': 'You will need each of the following ingredients to make a doll of unearthly powers.',
        'title': 'Visit Tia Dalma' },
    'wdr2.1needMaterials': {
        'description': 'The Navy has the finest straw in the islands, imported from England. Tia needs it for the ideal voodoo doll.',
        'title': 'Navy Straw' },
    'wdr2.1recoverStraw': {
        'description': 'Plunder straw from Navy ships',
        'stringBefore': "We'll need fine straw, so plunder more than you need so we can pick out the finest pieces.",
        'title': 'Plunder Straw',
        'unused': 'That should be... plenty straw. Now fetch the rest.' },
    'wdr2.2needMaterials': {
        'description': 'EITC Vipers are bringing in barrels of pitch to patch their damaged vessels. Deal a blow to the EITC armada and plunder the pitch for your doll.',
        'title': 'EITC Pitch' },
    'wdr2.2recoverPitch': {
        'description': 'Plunder pitch from the Navy barrels in Fort Charles',
        'stringBefore': 'Pitch we need. Many buckets. Them Navy men keep pitch in barrels.',
        'title': 'Plunder Pitch',
        'unused': "We'll be heating the pitch on the fire.\x07Return when you have them other items." },
    'wdr2.3recoverSilk': {
        'description': 'Plunder silk from East India Trading Company ships',
        'stringBefore': "Silk - the finest you can get. Lord Beckett's ships will carry it.",
        'title': 'Plunder Silk',
        'unused': 'Careful with the silk.  What about them other items I asked for?' },
    'wdr2.4recoverWire': {
        'description': 'Plunder spools of wire from Navy crates in Fort Charles',
        'stringBefore': 'We need sturdy wire. The Navy should not miss a few spools.',
        'title': 'Plunder Wire',
        'unused': "We'll use this to bind... good and tight.\x07Come back when you have the other items." },
    'wdr2.NeedMaterials': {
        'description': 'Gather the makings of your voodoo doll',
        'stringAfter': 'Now you have the makings. Dip the straw in the pitch... shape the doll like a man.\x07Good... but what you now hold in your hand, is just a doll.\x07You must go further, much further, to give that doll the power to become... a weapon!\x07The blood... of your enemies.',
        'title': 'Doll Makings' },
    'wdr2Materials': {
        'description': 'Gather the makings of your voodoo doll',
        'stringAfter': 'Now you have the makings. Dip the straw in the pitch...\x07... wrap the silk about the straw... and bind it tight with the wire.\x07Good.\x07That object you now hold in your hand, is just a doll.\x07You must go further, much further, to give that doll the power to become... a weapon!\x07The blood... of your enemies. That is what you must gather now',
        'title': 'Doll Makings' },
    'wdr3.1needBlood': {
        'description': "Blood from the crabs will empower your voodoo doll - but they won't give it up easily!",
        'title': 'Stone Crab Blood' },
    'wdr3.2needBlood': {
        'description': 'Scorpion blood has many medicinal and mystical uses.',
        'title': 'Scorpion Blood' },
    'wdr3.3needBlood': {
        'description': 'Alligator blood will seal your voodoo doll against other Gypsy magic.',
        'title': 'Alligator Blood' },
    'wdr3.NeedBlood': {
        'description': 'Gather the blood of your enemies for the voodoo doll.',
        'stringAfter': 'Your weapon is almost complete. \x07With dis blood, I infuse the doll with life. \x07But I need dis one last ingredient to make it a weapon...\x07...bone dust from the undead.',
        'title': 'The Blood of Your Enemies' },
    'wdr4.1bloodOfRockCrab': {
        'description': 'Acquire the blood of a rock crab',
        'title': 'Rock Crab Blood',
        'unused': 'Good - now get them other types of blood.' },
    'wdr4.1needBoneDust': {
        'description': 'Bandits are lowly scum that frequent graveyards trying to steal souls - defeat them for yourself and the good of the pirates everywhere!',
        'title': 'Undead Bandits' },
    'wdr4.2bloodOfScorpion': {
        'description': 'Acquire the blood of a scorpion',
        'title': 'Scorpion Blood',
        'unused': 'Good - now get them other types of blood.' },
    'wdr4.2needBoneDust': {
        'description': 'There, pirates are NOT your friends but servants of Jolly Roger! Defeat them for enough bone dust to finish the voodoo doll.',
        'title': 'Undead Pirates' },
    'wdr4.3bloodOfAlligator': {
        'description': 'Acquire the blood of a Alligator',
        'title': 'Alligator Blood',
        'unused': 'Good - now get them other blood types.' },
    'wdr4.4bloodOfBat': {
        'description': 'Acquire the blood of a Bat',
        'title': 'Bat Blood',
        'unused': 'Good - now get them other blood types.' },
    'wdr4.5bloodOfWasp': {
        'description': 'Acquire the blood of a Wasp',
        'title': 'Wasp Blood',
        'unused': 'Good - now get them other blood types.' },
    'wdr4.NeedBoneDust': {
        'description': 'Gather the bone dust of your undead enemies for the voodoo doll.',
        'title': 'Bone Dust of Your Enemies' },
    'wdr4blood': {
        'description': 'Gather the blood of your enemies for the Voodoo Doll.',
        'stringAfter': 'Your weapon almost be complete. \x07With this blood, I infuse the doll with life. \x07The object you now hold in your hand remains a doll still, but its power is growing..\x07Bone dust is the final piece of this puzzle. Get this, and a weapon you will have...',
        'title': 'The Blood of Your Enemies' },
    'wdr6.1boneDustOfClod': {
        'description': 'Acquire bone dust from an Undead Gravedigger',
        'title': 'Undead Gravedigger Bone Dust',
        'unused': 'This be the dust I asked for, but where be the rest?' },
    'wdr6.2boneDustOfSludge': {
        'description': 'Acquire bone dust from an Undead Bandit',
        'title': 'Undead Bandit Bone Dust',
        'unused': 'This be the dust I asked for, but where be the rest?' },
    'wdr6.3boneDustOfMire': {
        'description': 'Acquire bone dust from an Undead Pirate',
        'title': 'Undead Pirate Bone Dust',
        'unused': 'This be the dust I asked for, but where be the rest?' },
    'wdr6.4boneDustOfMuck': {
        'description': 'Acquire bone dust from an Undead Witchdoctor',
        'title': 'Undead Witchdoctor Bone Dust',
        'unused': 'This be the dust I asked for, but where be the rest?' },
    'wdr6BoneDust': {
        'description': 'Gather the blood of your enemies for the Voodoo Doll.',
        'stringAfter': 'Brave you have been... and true. Finished is the doll.\x07Use it wisely. Now go!',
        'title': 'The Blood of Your Enemies' },
    'wg.1visitJack': {
        'description': 'Find Jack Sparrow in the Faithful Bride on Tortuga.',
        'stringAfter': "Care to speculate on Captain Jack's preferred ice breaker with undesired undesirables and otherwise undead nasties?\x07Well, I'll tell ye... Boom!\x07That's right... bombs! They're crazy about them in Singapore. Bit tougher to come by in these parts...\x07... but that's where our dear friend \x01slant\x01Ewan\x02 comes in, savvy? He lives in the town on Port Royal.\x07Bring me a week's supply. And tell Ewan I sent you... maybe he'll cut you in on a few for yourself.",
        'title': 'Visit Jack Sparrow' },
    'wg.2visitEwan': {
        'description': 'Find Ewan in a warehouse in Port Royal.',
        'stringAfter': "Whoa! Stand back, mate!\x07Ye nearly blasted us to the moon - that's gunpowder ye just knocked into!\x07Captain Jack sent ye, did he? Well, ye can just tell him I'm done...\x07Shut down, out 'o business as it were.\x07That keg of powder ye nearly set off be me very last, so there's no more fireworks for Captain Sparrow.\x07Those mongrels from the East India Trading Company took it all - said they was collecting taxes...\x07Got me fuses and flints too...\x07Aye, there'll be no boom boom without 'em.\x07Listen, mate, ye go plunder some of me makings back and I'll fix up a batch of Captain Jack's favorites.\x07Let's start by making black powder. Here's what we'll need.",
        'title': 'Visit Ewan' },
    'wg.5recoverTar': {
        'description': 'Plunder tar from any Navy fort.',
        'stringAfter': "Got holes in yer boots? This stuff will fix that too.\x07Now, let's get to the important business of my fee. I don't suppose Captain Sparrow gave ye any form of payment for me, did he?\x07No? Well, in that case, ye'll need to work it off before I hand over the goods.\x07For starters, I'd like a spot of revenge against me brothers in the East India Trading Company.\x07Send some of their ships to Davy Jones and I'll be in a better mood to negotiate with ye.",
        'title': 'Recover Tar' },
    'wg.6sinkShips': {
        'description': 'Sink EITC ships.',
        'stringAfter': "That's be good news, indeed! Well done, mate.\x07Now, I've got a couple of deliveries for ye and then ye can have what you came for.\x07Got one delivery for a bloke in Padres Del Fuego.\x07And I owe a shipment of bombs to a rumrunner.\x07He goes by the name \x01slant\x01Bronze John\x02.\x07Ye can find him at his 'office' on Driftwood Island.",
        'title': 'Sink EITC Ships' },
    'wg.8deliverBombs': {
        'description': 'Deliver a supply of bombs to Jack Sparrow in the Faithful Bride on Tortuga.',
        'title': 'Deliver Bombs' },
    'wgr3.1grenadeMaterialsA': {
        'description': 'The only folks who store large amounts of quality fuses are the Port Royal Navy, but a word of warning... they are heavily guarded.',
        'title': 'Gather Fuses' },
    'wgr3.1recoverSaltpeter': {
        'description': 'Plunder saltpeter from crates in Kingshead.',
        'stringAfter': "That's the stuff we need, mate.",
        'stringBefore': "Saltpeter. I have no idea what it's made of, but the Navy should 'ave crates of it lying about.\x07Trouble is, they keep most of it in Kingshead.\x07Dangerous place, Kingshead. I'd not get caught there if I was ye.",
        'title': 'Saltpeter' },
    'wgr3.2grenadeMaterialsA': {
        'description': 'Navy flints are needed for the hand grenades to spark the fuses.',
        'title': 'Gather Flints' },
    'wgr3.2recoverCharcoal': {
        'description': 'Plunder charcoal by sinking L7+ EITC ships.',
        'stringAfter': 'Can always use a big barrel of charcoal.',
        'stringBefore': "We'll need charcoal - lots of it. East India carries the best stuff by sea.\x07It be heavily guarded, so watch yerself, mate.",
        'title': 'Charcoal' },
    'wgr3.3grenadeMaterialsA': {
        'description': 'The raw materials for the grenade shells are these metal castings found in storage in Fort Charles.',
        'title': 'Gather Castings' },
    'wgr3.3recoverSulfur': {
        'description': 'Plunder sulfur from barrels in Kingshead.',
        'stringAfter': 'I like to bathe with the stuff sometimes. Clears out me sinuses.',
        'stringBefore': "We'll need sulfur too. Smelly stuff, but it sure packs a punch!\x07Navy will have it by the barrelful in Kingshead or me name's not Ewan McCraken.",
        'title': 'Sulfur' },
    'wgr3.GrenadeMaterialsA': {
        'description': 'Gather all the materials Ewan requires to make you some powerful hand grenades.',
        'items': 'Materials',
        'stringAfter': "Aye, that's what I be looking for.\x07Now all that remains is the ingredients for the powder itself.",
        'title': 'Grenade Makings' },
    'wgr3Materials': {
        'description': 'Gather the ingredients to make black powder.',
        'items': 'Ingredients',
        'stringAfter': 'That will make enough black powder to punch holes in some East India ships, hey!\x07Now we be needing some other odds and ends to finish the job.',
        'title': 'Black Powder' },
    'wgr4.1grenadeMaterialsB': {
        'description': "Saltpeter is a prize commodity in the islands for many reasons, but the main reason is that it's essential in making gunpowder!",
        'title': 'Saltpeter' },
    'wgr4.1recoverFuses': {
        'description': 'Plunder fuses from crates in Kingshead.',
        'stringAfter': 'Aye, those are some fine fuses ye have there.',
        'stringBefore': "We'll need scores of fuses, mate. Navy ones burn the brightest.\x07There'll be a few crated up in Kingshead, no doubt.",
        'title': 'Fuses' },
    'wgr4.2grenadeMaterialsB': {
        'description': "Search carefully for the charcoal because the Navy men may be lazy but they can sense if you're up to no good!",
        'title': 'Charcoal' },
    'wgr4.2recoverFlints': {
        'description': 'Plunder flints from Fort Dundee barrels in Padres Del Fuego.',
        'stringAfter': "Careful with those flints. Wouldn't want any sparks flying around here, savvy?",
        'stringBefore': "We need flints, and plenty of 'em.\x07Best flints are mined in Padres Del Fuego. Navy keeps 'em in barrels in the fort there.",
        'title': 'Flints' },
    'wgr4.3grenadeMaterialsB': {
        'description': "Sulfur is kept inside the fortified walls of Kingshead - but a crafty pirate can find it, if you're not jailed during your search!",
        'title': 'Sulfur' },
    'wgr4.3recoverCasings': {
        'description': 'Plunder casings from barrels in Kingshead.',
        'stringAfter': "Those casings aren't the best I've seen, but they'll do in a pinch.",
        'stringBefore': "It all gets wrapped up in casings, so we'll need casings a plenty.\x07Navy has 'em stashed in barrels on Kingshead.",
        'title': 'Casings' },
    'wgr4.GrenadeMaterialsB': {
        'description': 'Gather the ingredients to make black powder.',
        'items': 'Ingredients',
        'stringAfter': 'That will make enough black powder to punch holes in some East India ships, hey!\x07Now we be needing some other odds and ends to finish the job.',
        'title': 'Black Powder' },
    'wgr4Materials': {
        'description': 'Gather bomb-making materials.',
        'stringAfter': "Aye, now we have the makings of some quality explosives, but we've nothin' to hold it all together.\x07Fetch me tar, mate, and be quick about it!\x07Can't have this stuff lyin' about in this state very long.",
        'title': 'Bomb Materials' },
    'wgr5.1grenadeMaterialsC': {
        'description': "Once McCraken's made a batch of gun powder, he'll need several kegs to keep the powder from getting wet.",
        'title': 'Gather Kegs' },
    'wgr5.2grenadeMaterialsC': {
        'description': 'The spools of wire hidden in the storage crates are needed to secure the kegs.',
        'title': 'Gather Wire' },
    'wgr5.3grenadeMaterialsC': {
        'description': 'Tar is used to re-coat the insides of the kegs to keep the powder in and moisture out.',
        'title': 'Gather Tar' },
    'wgr5.GrenadeMaterialsC': {
        'description': 'McCraken needs a few more items to complete the grenades.',
        'items': 'Ingredients',
        'stringAfter': "Well done, mate! We'll make a pirate out of you yet! Now, one other task before you return to Jack.\x07Sink some EITC ships fer me... why?\x07'Cause I loath those bilge rats, that's why!",
        'title': 'Finishing Touches' },
    'wgr6.SinkShips': {
        'description': 'McCraken despises the EITC and would consider it a personal favor to sink at least 5 of their prized ships.',
        'stringAfter': 'Aye, those were the very ones I wanted sunk.\x07Now, take your prize to Jack and be sure to keep a few for yourself!',
        'title': 'Sink EITC Ships' },
    'wgr7.1smuggleBombs': {
        'description': 'Smuggle a package of bombs to Padres Del Fuego.',
        'stringAfter': 'Well done, mate.',
        'stringBefore': "Got a delivery for a bloke in Padres Del Fuego.\x07I'd avoid rough seas when sailing with this lot in your ship's hold, eh?",
        'title': 'Smuggle Bombs' },
    'wgr7.2deliverBombs': {
        'description': 'Deliver a package of bombs to Bronze John on Driftwood Island.',
        'stringAfter': "That John's as crazy as a drunken pelican, but his money's still good.",
        'stringBefore': "I owe a shipment of bombs to a rumrunner. He goes by the name \x01slant\x01Bronze John\x02.\x07Ye can find him at his 'office' on Driftwood Island.",
        'title': 'Deliver Bombs' },
    'wgr7Smuggle': {
        'description': 'Smuggle bombs for Ewan.',
        'items': 'Smuggling Runs',
        'stringAfter': "Okay mate. A deal's a deal. Take this lot to Captain Jack with me compliments.",
        'title': 'Smuggle Bombs' },
    'wk.1visitElizabeth': {
        'description': "Visit Elizabeth Swann in the governor's mansion, Port Royal.",
        'stringAfter': "Knife throwing is a pastime my father would never approve of... so let's just keep this between us.\x07I will teach you what I know of knife-work...\x07... and in return, you will help me.\x07First we need some proper knives. And none of that rot from town... they're not fit to even cook with.\x07Ask Will Turner to forge a set...\x07... and bring them to me.",
        'title': 'Visit Elizabeth Swann' },
    'wk.2visitWill': {
        'description': 'Visit Will Turner in Port Royal.',
        'stringAfter': 'Elizabeth is well? Good.\x07I will forge the blades for you, but we need proper materials.',
        'title': 'Visit Will Turner' },
    'wk.4visitElizabeth': {
        'description': 'Look in on Elizabeth while Will forges the knives.',
        'stringAfter': "I'm glad you're here. There is news of my father.\x07A trusted friend told me the EITC has intercepted a message intended for my father, the governor.\x07It may be the clue I have been searching for.\x07Recover the message, and I will honor our agreement.",
        'title': 'Visit Elizabeth' },
    'wk.5recoverMessage': {
        'description': 'Recover a message for Governor Swann from a powerful EITC ship.',
        'stringAfter': 'Oh thank you! I owe you a great debt.\x07Your knives should be finished. Return with them and I will teach you.',
        'title': 'Recover Message' },
    'wk.6visitWill': {
        'description': 'Visit Will Turner and see if the knives are ready.',
        'stringAfter': "These are some of the finest knives I've ever made. I pray they'll be used in the service of Elizabeth Swann.",
        'title': 'Visit Will Turner' },
    'wk.7deliverKnives': {
        'description': 'Take the knives to Elizabeth Swann.',
        'title': 'Deliver Knives' },
    'wkr3.1daggerMaterialsA': {
        'description': 'Navy Panthers have steel rods that reinforce their masts.',
        'stringAfter': "I won't ask how you came by it.",
        'title': 'Fine Steel Rods' },
    'wkr3.1recoverSteel': {
        'description': 'Recover fine steel rods from East India Trading Company ships (Lvl. 7+).',
        'stringAfter': "I won't ask how you came by it.",
        'stringBefore': 'Throwing knives need balance.  Only the finest steel will do... East India Trading Company steel.',
        'title': 'Fine Steel Rods' },
    'wkr3.2daggerMaterialsA': {
        'description': 'Silver ingots are used to make the daggers not only strong but beautifully shiny!',
        'stringAfter': 'The East India Trading Company controls all the finest silver.',
        'title': 'Sterling Silver Ingots' },
    'wkr3.2recoverSilver': {
        'description': 'Recover sterling silver ingots from East India Trading Company ships (Lvl. 7+).',
        'stringAfter': 'The East India Trading Company controls all the finest silver.',
        'stringBefore': "I'll need silver, for the hilt and for trim.",
        'title': 'Sterling Silver Ingots' },
    'wkr3.3recoverBone': {
        'description': 'Recover polished bone from undead.',
        'stringAfter': 'This will do.',
        'stringBefore': "We need a lightweight material for the hilts. Polished bone will do...\x07... and there's much of it about with Jolly Roger's army on the move.",
        'title': 'Polished Bone' },
    'wkr3.4recoverTongs': {
        'description': 'Recover a pair of Navy tongs from a Navy Guard.',
        'stringAfter': "Those tongs aren't mine, but they will do.",
        'stringBefore': "Navy swine stole my tongs. I'll need those to craft your knives.\x07See if you can get them back for me.",
        'title': 'Tongs' },
    'wkr3.5recoverCoal': {
        'description': 'Recover coal from barrels in Navy Forts.',
        'stringAfter': 'That should be sufficient.',
        'stringBefore': "Knives of precision need a hot fire. We'll need all the coal you can gather.",
        'title': 'Coal' },
    'wkr3.DaggerMaterialsA': {
        'description': 'Gather quality materials for Will Turner to forge you a set of fine daggers.',
        'items': 'Materials',
        'stringAfter': "Well done. That's what I need for the blades, but there's more to gather...",
        'title': 'Gather Materials' },
    'wkr3Materials': {
        'description': 'Gather knife making materials for Will Turner.',
        'items': 'Materials',
        'stringAfter': 'Now we have everything needed. While I forge your knives, look after Elizabeth.',
        'title': 'Gather Materials' },
    'wkr4.1daggerMaterialsB': {
        'description': 'William Turner uses the polished bone from the Undead for the best handles in the Caribbean.',
        'stringAfter': 'This will do.',
        'title': 'Polished Bone' },
    'wkr4.2daggerMaterialsB': {
        'description': 'Navy tongs are a necessity for moving around hot coals from one fire to another.',
        'stringAfter': "Those tongs aren't mine, but they will do.",
        'title': 'Tongs' },
    'wkr4.3daggerMaterialsB': {
        'description': 'Will needs plenty of coal to stoke the fires of his crucible and the best coal is kept by the Undead for their rituals.',
        'stringAfter': 'That should be sufficient.',
        'title': 'Coal' },
    'wkr4.DaggerMaterialsB': {
        'description': 'Gather knife making materials for Will Turner.',
        'items': 'Materials',
        'stringAfter': 'Now we have everything needed. While I forge your knives, look after Elizabeth.',
        'title': 'Gather Materials' },
    'ws.1visitTia': {
        'description': 'Visit Tia Dalma at her home in Cuba.',
        'stringAfter': "Ah yes, you have learned much...\x07... but much there is you still do not know.\x07The doll is strong, yes? But the \x01slant\x01staff\x02... the staff be a weapon of consequence!\x07To be usin' the staff, you must be strong of heart. And I only know one way to test the strength of a heart.\x07This be a test against the elements... earth, air, fire...\x07... and the sea herself!",
        'title': 'Visit Tia Dalma' },
    'ws.3recoverBranch': {
        'description': 'Steal branches from a demonic tree men, but consider taking a crew with you for they are merciless and powerful!',
        'stringAfter': 'A strong branch is not enough alone. The staff needs character as well as a head.\x07A shrunken head gives the staff its...character.\x07Skeleton captains in the service of Jolly Roger carry them as trophies. Bring some back to Tia.\x07And I will complete your staff.',
        'title': 'Acquire Branches' },
    'ws.3recoverStump': {
        'description': 'Steal a branch from a Tree Demon',
        'stringAfter': 'A strong branch is not enough alone. The staff needs character as well as a head.\x07A shrunken head gives the staff its...character.\x07Skeleton captains in the service of Jolly Roger carry them as trophies. Bring one back to Tia.\x07And I will complete your staff.',
        'stringBefore': 'Your heart is strong. You are ready. Go now, and return with a branch...\x07...a branch as sturdy as your desire.',
        'title': 'Acquire A Branch' },
    'ws.4recoverHead': {
        'description': 'Search the high seas and sink a Skeleton Frigate to acquire a shrunken head.',
        'stringAfter': 'Next, give power to your staff by adding the essense of your enemies.',
        'title': 'Acquire A Shrunken Head' },
    'ws.4recoverShrunkenHead': {
        'description': 'The shrunken heads are not only powerful totems but the they also look wicked cool!',
        'stringAfter': 'Next, give power to your staff...\x07You must acquire the essence of your enemies... by defeating them.',
        'title': 'Acquire Shrunken Heads' },
    'ws.5deliverDoll': {
        'description': 'Complete Your Staff by returning to Tia Dalma',
        'title': 'Return to Tia Dalma' },
    'ws.7sinkHarbingers': {
        'description': "Jolly Roger's Black Harbingers hold a mystical essence and sinking them strengthens you and your staff.",
        'title': 'Sink Black Harbingers' },
    'wsr2.1defeatCorpse': {
        'description': 'Defeat the Undead',
        'title': 'Defeat Undead Grenadiers' },
    'wsr2.1proveHeart': {
        'description': 'To prove your courage, Tia Dalma wants to see something real - like real defeated Undead scum!',
        'title': 'Prove Courage' },
    'wsr2.2defeatCarrion': {
        'description': 'Defeat the Undead',
        'title': 'Defeat Undead Gypsies' },
    'wsr2.2proveHeart': {
        'description': 'Tia wants to know that you truly want the Staff - so prove your resolve by defeating the dreaded Undead Gypsies.',
        'title': 'Prove Resolve' },
    'wsr2.3defeatZombie': {
        'description': 'Defeat the Undead',
        'title': 'Defeat Undead Raiders' },
    'wsr2.3proveHeart': {
        'description': "Defeating the gruesome and powerful Undead Raiders will prove that you're strong enough to wield the Voodoo Staff.",
        'title': 'Prove Strength' },
    'wsr2.ProveHeart': {
        'description': 'Defeat terrible enemies to test your strength of heart',
        'stringAfter': 'Your heart be strong. You are ready.\x07Go now and return with a branch...\x07... a branch as sturdy as your desire.',
        'title': 'Prove Your Heart' },
    'wsr2Heart': {
        'description': 'Defeat terrible enemies to test your strength of heart',
        'stringAfter': 'Your heart be strong. You are ready.\x07Go now and return with a branch...\x07... a branch as sturdy as your desire.',
        'title': 'Prove Your Heart' },
    'wsr3.1defeatWasp': {
        'description': 'Be careful fighting this powerful type of wasp.',
        'title': 'Defeat Angry Wasps' },
    'wsr3.2defeatGator': {
        'description': 'Look for Gators in the swamps.',
        'title': 'Defeat Huge Gators' },
    'wsr3.3defeatScorpion': {
        'description': 'Scorpions can often be found on wild islands.',
        'title': 'Defeat Dread Scorpions' },
    'wsr3.4defeatCrab': {
        'description': 'Crabs can often be found on the beaches of wild islands.',
        'title': 'Defeat Giant Crabs' },
    'wsr3.5defeatFlyTrap': {
        'description': 'Fly Traps are found in the swamps.',
        'title': 'Defeat Fly Traps' },
    'wsr3.6defeatBat': {
        'description': 'The best place to find Vampire Bats is in caves.',
        'title': 'Defeat Vampire Bats' },
    'wsr3PowerUp': {
        'description': 'Defeat various enemies to power up your staff.',
        'stringAfter': 'There is only one more thing you must do.\x07The essence of your enemies is only half... the other half be the essence of the Caribbean herself.\x07To capture the essence of the Carribean, you must confront an enemy on every shore...\x07... with the staff in your possession.',
        'title': 'Power Up Your Staff' },
    'wsr4.1defeatPortRoyal': {
        'description': 'Defeat any creature on Port Royal.',
        'title': 'Port Royal' },
    'wsr4.2defeatTortuga': {
        'description': 'Defeat any creature on Tortuga',
        'title': 'Tortuga' },
    'wsr4.3defeatPadresDelFuego': {
        'description': 'Defeat any creature on Padres Del Fuego',
        'title': 'Padres Del Fuego' },
    'wsr4.4defeatCutthroat': {
        'description': 'Defeat any creature on Cutthroat Island',
        'title': 'Cutthroat Island' },
    'wsr4.4defeatDriftwood': {
        'description': 'Defeat any creature on Driftwood Island',
        'title': 'Driftwood Island' },
    'wsr4.4defeatKingshead': {
        'description': 'Defeat any creature on Kingshead Island',
        'title': 'Kingshead Island' },
    'wsr4.5defeatCangrejos': {
        'description': 'Defeat any creature on Isla Cangrejos',
        'title': 'Isla Cangrejos' },
    'wsr4.5defeatCuba': {
        'description': 'Defeat any creature on Cuba',
        'title': 'Cuba' },
    'wsr4.5defeatTormenta': {
        'description': 'Defeat any creature on Isla Tormenta',
        'title': 'Isla Tormenta' },
    'wsr4.6defeatAnvil': {
        'description': "Defeat any creature on Devil's Anvil",
        'title': "Devil'sAnvil" },
    'wsr4.6defeatOutkast': {
        'description': 'Defeat any creature on Outcast Isle',
        'title': 'Outcast Isle' },
    'wsr4.6defeatPerdida': {
        'description': 'Defeat any creature on Isla Perdida',
        'title': 'Isla Perdida' },
    'wsr4.6defeatRumrunners': {
        'description': 'Defeat any creature on Rumrunners Isle',
        'title': 'Rumrunners Isle' },
    'wsr4EveryShore': {
        'description': 'Capture the essence of the Caribbean within your staff.',
        'title': 'The Essence of the Caribbean' },
    'wsr5.1powerUpA': {
        'description': 'Assassins have a strong but wicked essence, defeating them will give you some of their strength but guard yourself against their evil.',
        'title': 'Defeat Assassins' },
    'wsr5.2powerUpA': {
        'description': 'The Navy Dragoon troops are some of the most battle-tested soldiers in the Caribbean.',
        'title': 'Defeat Dragoons' },
    'wsr5.3powerUpA': {
        'description': 'Receive the essence of these Undead Raiders, who once were alive and brave warriors first into a fray!',
        'title': 'Defeat Raiders' },
    'wsr5.PowerUpA': {
        'description': 'Defeat various enemies to power up your staff.',
        'stringAfter': "Now that you've taken the essence of your enemies...\x07You are a mighty Voodoo warrior!\x07Almost. Defeat some of Davy Jones minions to give your staff an even greater power...",
        'title': 'Power Up Your Staff' },
    'wsr6.1powerUpB': {
        'description': "Dregs are the brains behind Davy Jones' dark deeds and defeating them will give your staff the essence of wisdom.",
        'title': 'Defeat Dregs' },
    'wsr6.2powerUpB': {
        'description': 'Defeat the Flotsams to power up your staff with organic matter.',
        'title': 'Defeat Flotsams' },
    'wsr6.3powerUpB': {
        'description': 'Spineskulls do the dirtiest of the dirty work for Davy Jones, defeating them will transfer some of their vile power to your staff.',
        'title': 'Defeat Spineskulls' },
    'wsr6.PowerUpB': {
        'description': "The Voodoo staff's power thrives on defeating the henchmen of Davy Jones.",
        'stringAfter': "There is only one more thing you must do.\x07The essence of your enemies is only half... the other half be the essence of the Jolly Roger himself!\x07To capture the essence you must sink some of Jolly's prized vessels...\x07...Black Harbingers. Good luck. The spirits are with you.",
        'title': 'Power Up Your Staff' },
    'wt1.defeatBigGators': {
        'description': 'In exchange for the locations of the rest of the Pirate Lore pages, Billy McKidd wants you to defeat some big alligators as part of his duties to the Navy.',
        'title': 'Gator Cleanup' },
    'wt1.defeatFlyTraps': {
        'description': 'In exchange for the locations of the rest of the Pirate Lore pages, Billy McKidd wants you to defeat some fly traps as part of his duties to the Navy.',
        'title': 'Fly Trap Cleanup' },
    'wt1.defeatGiantCrabs': {
        'description': 'In exchange for the locations of the rest of the Pirate Lore pages, Billy McKidd wants you to defeat some giant crabs as part of his duties to the Navy.',
        'title': 'Crab Cleanup' },
    'wt1.defeatSkeletons': {
        'description': 'In exchange for the locations of the rest of the Pirate Lore pages, Billy McKidd wants you to defeat some skeletons as part of his duties to the Navy.',
        'title': 'Skeleton Cleanup' },
    'wt1.defeatWasps': {
        'description': 'In exchange for the locations of the rest of the Pirate Lore pages, Billy McKidd wants you to defeat some wasps as part of his duties to the Navy.',
        'title': 'Wasp Cleanup' },
    'wt1.deliverBookOfLore': {
        'description': 'You have pieced together the book of Pirate Lore for Will Turner. Deliver it to him and he will reward you with a new cutlass.',
        'title': 'Finished Pirate Lore' },
    'wt1.deliverMedal': {
        'description': 'All you were able to find was a cruddy medal in Royal Caverns. Return it to Will Turner to see if he can make any sense out of it.',
        'stringAfter': "This is what you found in the Pirate Lore chest?\x07It has EITC markings on it. I can't make much sense of them though.\x07If we are going to get anywhere with this, we need to find ourselves an EITC manual.\x07They give them out to new guards. Explains all of the EITC codes and rules.\x07If we can get our hands on one, it might shed some light on this rubbish.",
        'title': 'Cruddy Medal' },
    'wt1.deliverPirateLorePage': {
        'description': 'Will Turner needs your help acquiring the book of Pirate Lore. Speak to Jim Wavemonger, he works in a mine in Port Royal named Royal Caverns.',
        'stringAfter': 'Scorpions... everywhere! Wha... Oh... Pardon me. Not used to blokes sneaking up on me in here\x07The book of Pirate Lore? These Navy swine have us searching around the clock. Little do they know when we dig one hole, we fill another.\x07I searched the same spot a dozen times this week. At this rate they have a better chance striking gold!\x07Ye look like a decent chap though. With a bit of work, I be sure ye will find something.',
        'stringBefore': 'DIALOGUE ERROR',
        'title': 'Book of Pirate Lore' },
    'wt1.deliverUnfinishedBookOfPirateLore': {
        'description': 'Show the unfinished book of Pirate Lore to Billy McKidd. He may know where to find the rest.',
        'stringAfter': "Now why should I deal with you? Can't you see I be busy watching the card tables?\x07Either put on a show at the card tables or leave. Be gone!",
        'title': 'Unfinished Lore' },
    'wt1.playBlackjack': {
        'description': 'Billy McKidd will not speak to you as he is busy watching card games. Win at blackjack in order to catch his attention.',
        'title': 'Blackjack Attention' },
    'wt1.playPoker': {
        'description': 'Billy McKidd will not speak to you as he is busy watching card games. Win at poker in order to catch his attention.',
        'title': 'Poker Attention' },
    'wt1.recoverChestOfPirateLore': {
        'description': 'Royal Caverns in Port Royal is thought to hold the buried remains of the book of Pirate Lore. Search for a buried chest somewhere in Royal Caverns.',
        'stringAfter': "Bats! Run! Wh... Ye again? I hope waking me up is not going to become a habit.\x07By the looks of this chest, the Navy is wasting their time here. Nothing but a cruddy medal, it is.\x07It's all ye be finding though. Now get lost 'fore the boss notices yer find.",
        'title': 'Buried Lore' },
    'wt1.recoverEITCManual': {
        'description': 'In order to decipher the EITC markings on the medal you found, Will Turner needs you to acquire an EITC manual from an EITC member.',
        'stringAfter': "Interesting... According to the manual, the markings on the medal you found are of EITC ship classes.\x07They must be stashing some of the pages on these ships.\x07Recover these pages for me. Here's a list of the ship types they may be on.",
        'title': 'EITC Training' },
    'wt1.recoverLorePagesA': {
        'description': 'Will Turner has discovered that some of the pages from Pirate Lore are hidden on EITC Marauder ships. Recover these pages.',
        'title': 'Marauder Lore' },
    'wt1.recoverLorePagesB': {
        'description': 'Will Turner has discovered that some of the pages from Pirate Lore are hidden on EITC Barracuda ships. Recover these pages.',
        'title': 'Barracuda Lore' },
    'wt1.recoverLorePagesC': {
        'description': 'Will Turner has discovered that some of the pages from Pirate Lore are hidden on EITC Corvette ships. Recover these pages.',
        'title': 'Corvette Lore' },
    'wt1.recoverLorePagesD': {
        'description': 'Will Turner has discovered that some of the pages from Pirate Lore are hidden on EITC Sea Viper ships. Recover these pages.',
        'title': 'Sea Viper Lore' },
    'wt1.recoverRestOfBookA': {
        'description': 'According to Billy McKidd, part of the book of Pirate Lore can be found buried somewhere on Kingshead Island.',
        'title': 'Kingshead Lore' },
    'wt1.recoverRestOfBookB': {
        'description': "According to Billy McKidd, part of the book of Pirate Lore can be found buried somewhere on Rumrunner's Isle.",
        'title': 'Rumrunner Lore' },
    'wt1.recoverRestOfBookC': {
        'description': 'According to Billy McKidd, part of the book of Pirate Lore can be found buried somewhere on Isla Cangrejos.',
        'title': 'Cangrejos Lore' },
    'wt1.visitWillTurner': {
        'description': 'Seek out Will Turner as he has a new task for you',
        'stringAfter': "I see you've been making some good progress with that cutlass.\x07There is nothing more valuable to a pirate than a quality blade.\x07It may just be about time you stepped up to a better cutlass. You don't want to be outdated, right?\x07We may be able to help each other. I have been consumed lately tracking something down.\x07It is a book of Pirate Lore, thought to be lost in a shipwreck when I was a child.\x07In my entire life I've only been able to recover 1 page of its text, but recent rumors have me hopeful again.\x07A man named Jim Wavemonger works in a mine in Port Royal named Royal Caverns, one of the Navy's many searching grounds for the book.\x07Go speak to him, he may be able to help point us in the right direction.",
        'title': 'Visit Will Turner' } }
NPCNames = {
    '': 'Captain Swain',
    '1110843146.22jubutler': 'Bartender Bob',
    '1110843298.39jubutler': 'the NPC Pirate',
    '1111111111.1mwt': 'Valentina',
    '1120093509.64npavlov': 'Yarr the Barbarian',
    '1120093705.09npavlov': 'Queen of the Seven Seas',
    '1121301373.97dcranall': 'Boatswain Bill',
    '1121480433.94npavlov': 'NPC 1',
    '1121480490.92npavlov': 'Lovely Meg Heartburn',
    '1121487027.3npavlov': 'Lovely Meg Heartburn II',
    '1121487041.72npavlov': 'Pretty Prudence Cabingnasher',
    '1121725426.22Shochet': 'NPC 2',
    '1121725594.36Shochet': 'NPC 3',
    '1121972472.25aholdun': 'NPC 5',
    '1121972725.58aholdun': 'NPC 6',
    '1121975138.93aholdun': 'NPC 7',
    '1121978047.91aholdun': 'NPC 8',
    '1121978217.47aholdun': 'NPC 9',
    '1121978661.83aholdun': 'Ann Ominous',
    '1121978802.8aholdun': 'The Evil One',
    '1121979349.16aholdun': 'Mackarel Maggie',
    '1121979527.5aholdun': 'Nicked Ned',
    '1121980228.66aholdun': 'Zapped Zachary',
    '1121980304.47aholdun': 'Jostling Josh',
    '1121980408.54aholdun': 'Jumpin Jeremiah',
    '1121980440.5aholdun': 'Jellylegs Jill',
    '1121980508.61aholdun': 'Gypsy Helper',
    '1121980551.07aholdun': 'Python Charmer',
    '1121980756.63aholdun': 'Java Addict',
    '1121980921.57aholdun': 'Cryin Carrie',
    '1121980993.43aholdun': 'Toothless Tim',
    '1121981033.35aholdun': 'Shivering Tim Bers',
    '1121981102.16aholdun': 'Sir Swim-a-lot',
    '1121981200.91aholdun': 'Buck-toothed Becky',
    '1121981239.13aholdun': 'the Soothsayer',
    '1121983399.19aholdun': 'Whispering Will',
    '1121983608.0aholdun': 'Stuttering Toto',
    '1121983938.33aholdun': 'Furry-Ear Fred',
    '1121983998.33aholdun': 'Fatty Longlegs',
    '1121984095.0aholdun': 'Logos Connecticus',
    '1121984229.99aholdun': 'Short Shelly',
    '1123266133.38npavlov': 'Logos Connecticus',
    '1123266194.75npavlov': 'Loopy Larry',
    '1124236671.37jubutler': 'Captain Bo Beck',
    '1124304820.4npavlov': 'Cryin Carrie',
    '1125705357.52jubutler': 'Dorbie Danton',
    '1135815579.88dparis': '',
    '1135815788.65dparis': 'Swabby Starpigge',
    '1135816074.16dparis': 'Brimstone Brundy',
    '1135816145.3dparis': 'Davy Dorr',
    '1135816180.19dparis': 'Brimstone Brundy',
    '1135900171.76dparis': 'Brimstone Brundy',
    '1138399108.42dxschafe': 'Dave',
    '1138401436.53dxschafe': 'Angel',
    '1138402195.63dxschafe': 'Goldbeard',
    '1138403440.64dxschafe': 'Jack Seakidd',
    '1138404604.47dxschafe': '',
    '1138664636.88dxschafe': 'Who am I?',
    '1138679435.03jubutler': 'Angel',
    '1138933290.05jubutler': 'Blackbones',
    '1138936296.39jubutler': 'Goldbeard',
    '1138936413.47jubutler': 'Stupid Bartholomew ',
    '1141357391.27sdnaik': 'Blackbones',
    '1141415446.44sdnaik': 'Graham Marsh',
    '1141416648.8sdnaik': 'Graham Marsh',
    '1142321958.13sdnaik': 'Yellow Dan',
    '1146634932.61jubutler': 'Sam Truelee',
    '1146635159.56jubutler': 'Miss Maggie ',
    '1146635362.06jubutler': 'Ned Decktimbers',
    '1146635785.65jubutler': 'Coal Goldwater',
    '1149126183.25MAsaduzz': 'Angel',
    '1149126880.85MAsaduzz': 'Angel',
    '1149126938.35MAsaduzz': 'Angel',
    '1152830677.95jubutler': 'Will Turner',
    '1152839242.37jubutler': 'Billy Plankbite',
    '1152840295.64jubutler': 'Elizabeth Swann',
    '1152841749.39jubutler': 'Darryl Doonan',
    '1153420647.55dzlu': 'Ewan McCraken',
    '1153439632.21darren': 'Captain Bo Beck',
    '1153441310.96darren': 'Cutscene LocalPirate',
    '1154497329.64jubutler': 'Will Turner',
    '1154497344.0jubutler': 'Tia Dalma',
    '1154497344.0jubutlerPR': 'Tia Dalma',
    '1154500954.5jubutler': 'Billy Plankbite',
    '1154574164.57jubutler': 'Sam Seabones',
    '1154731709.64jubutler': 'Doggerel Dan',
    '1155773612.45fxlara': 'Jeweler Smitty',
    '1156978503.22jasyeung': 'Old Will ',
    '1156979153.83jasyeung': 'Dirty  Planklove',
    '1156980166.1jasyeung': 'Lady  Heartsilver',
    '1156986020.6jasyeung': 'Edward Stormhawk',
    '1156986071.78jasyeung': 'Edward Grintley',
    '1156986102.42jasyeung': 'Tobias Bladepratt',
    '1156986135.88jasyeung': 'Barbary Tom',
    '1156986185.83jasyeung': 'Mark Backcrash',
    '1156986248.77jasyeung': 'Darby Drydock',
    '1157048353.58jasyeung': 'Bartholomew Watkins',
    '1157094552.02jasyeung': 'R. Smith, Pewterer',
    '1157097728.52jasyeung': 'Balthasar Bollard',
    '1157097816.67jasyeung': 'Sven Thorhammer',
    '1157097924.52jasyeung': 'Romany Bev',
    '1157097962.5jasyeung': 'Shochett Prymme',
    '1157098037.86jasyeung': 'Ferrera',
    '1157098075.78jasyeung': 'Erasmus Grimsditch',
    '1157098120.05jasyeung': 'Deaf Gunny',
    '1157098184.94jasyeung': 'Powder-Burnt Pete',
    '1157587636.63jasyeung': 'Thomas Stareaston',
    '1158013224.89dparis': 'Miss Maggie ',
    '1158013639.31dparis': 'Sally Gold',
    '1161287533.85MAsaduzz': 'Tom',
    '1165004570.58sdnaik': 'Edward Wildratte',
    '1165199819.22Shochet': "O'Malley",
    '1165199931.31Shochet': 'Fabiola',
    '1168022298.47Shochet': 'Joshamee Gibbs',
    '1168022348.66Shochet': 'Carver',
    '1168052247.45mike': 'Scarlet',
    '1168748251.22joswilso': 'Dockworker Fitz',
    '1169060460.13mike': 'Sgt. Bingham',
    '1169063296.16mike': 'Orinda Le Jeune',
    '1169067906.19mike': 'Tattoo Bonita',
    '1169068641.66mike': 'Doc Grog',
    '1169070429.72mike': 'Karbay Benedek',
    '1169071109.22mike': 'Hendry Cutts',
    '1169075008.52mike': 'Lt. Peter Blakeley',
    '1169075474.72mike': 'Andrew Bowdash',
    '1169075683.22mike': 'June',
    '1169075869.81mike': 'Blacksmith Flinty',
    '1169076109.16mike': 'Butcher Brown',
    '1169076368.97mike': 'Ben Flatts',
    '1169076564.88mike': 'Tomas',
    '1169077081.52mike': 'Seamstress Anne',
    '1169077360.47mike': 'Millie',
    '1169078025.53mike': 'Le Cerdo',
    '1169078309.55mike': 'El Pirato',
    '1169078705.84mike': 'Gunner',
    '1169079172.34sdnaik': 'Ewan McCraken',
    '1169081241.89mike': 'Grundy McMuggin',
    '1169081503.72mike': 'Giladoga',
    '1169081738.45mike': 'Bastien Craven',
    '1169083104.56sdnaik': 'Graham Marsh',
    '1169088062.75mike': 'Johnny McVane',
    '1169094482.66mike': 'John Smith',
    '1169094669.8mike': 'Bronze John',
    '1169151219.8mike': 'Jeweler Smitty',
    '1169190957.44mike': 'Gordon Greer',
    '1170739712.0mike': 'Scary Mary',
    '1170739968.0mike': 'Captain Steadman',
    '1171238953.92MAsaduzz': 'Nell Bilgehayes',
    '1171321221.87MAsaduzz': 'Peter Bluekidd',
    '1171321509.23MAsaduzz': 'Jeffrey Bridgegrin',
    '1171325040.86MAsaduzz': 'Elizabeth Swann',
    '1172276608.0mike': 'Andros Mallet',
    '1172618710.78sdnaik': 'Captain Barbossa',
    '1172630144.0mike': 'Nill Offrill',
    '1172887552.0mike': 'Garrett',
    '1172887552.0mike0': 'Giladoga',
    '1173146624.0mike0': 'Duchamps',
    '1173147520.0mike': 'Morris',
    '1174342784.0dxschafe': 'Althea',
    '1174343680.0dxschafe': 'Wallace',
    '1174344320.0dxschafe': "O'Henry",
    '1174345216.0dxschafe': 'Pickert',
    '1174345984.0dxschafe': 'Captain Archer',
    '1174350464.0dxschafe': 'Alberto',
    '1174351232.0dxschafe': 'Captain Jones',
    '1174351616.0dxschafe': 'Trent',
    '1174352768.0dxschafe': 'Osso Bucco',
    '1174353792.0dxschafe': 'Captain Billington',
    '1174954368.0jubutler': 'Jack Sparrow',
    '1175101824.0dxschafe': 'Woodruff',
    '1175108864.0dxschafe': 'Jehan Carrou',
    '1175117568.0dxschafe0': 'Penrod',
    '1175118080.0dxschafe': 'Jehan Carrou',
    '1175119104.0dxschafe1': 'Collier',
    '1175120896.0dxschafe0': 'Captain Barts',
    '1175282688.00MAsaduzz': 'cs_2_2_td_bg_1',
    '1175283200.00MAsaduzz': 'cs_2_2_td_bg_2',
    '1175283328.00MAsaduzz': 'cs_2_2_td_bg_3',
    '1175316480.0jubutler': 'my testing test person',
    '1175553664.0dxschafe': 'Lucinda',
    '1175554816.0dxschafe': 'Cassandra',
    '1175635584.0dxschafe': 'Daisy',
    '1175650176.0dxschafe': 'Retavick',
    '1175721216.0dxschafe': 'Olivier',
    '1175730944.0dxschafe': 'Pauper Pedro',
    '1175733248.0dxschafe': 'Fernando',
    '1175733376.0dxschafe': 'Rico',
    '1175792768.0dxschafe': 'William Turk',
    '1175800576.0dxschafe': 'Jack Redrat',
    '1176186151.42mike': 'Macomo',
    '1176322304.0mike1': 'Captain Reginald',
    '1176322432.0mike': 'Captain Dennison',
    '1176322432.0mike0': 'Captain Hedley',
    '1176322560.0mike': 'Captain Biggleton',
    '1176322560.0mike0': 'Captain Norman',
    '1176322688.0mike': 'Captain Fitzpatrick',
    '1176322688.0mike0': 'Captain Hamilton',
    '1176322816.0mike': 'Captain Montrose',
    '1176322944.0mike': 'Luther',
    '1176334208.0mike0': 'Black Mack',
    '1176744320.0dxschafe': 'Dockworker Pete',
    '1176765184.0dxschafe': 'Dockworker Jones',
    '1176836096.0dxschafe': 'Leon Bladewash',
    '1177109582.39MAsaduzz': "Jeremiah O'Pigge",
    '1177714944.0mike': 'Valentina',
    '1178233033.58dchiappe': 'Josie McReedy',
    '1178234368.0dchiappe1': 'Josie McReedy',
    '1178320768.0dchiappe': 'Hector Foulbreaker',
    '1178654720.0dchiappe': 'Peter Chipparr',
    '1179186560.0dchiappe': 'Gravedigger Gilbert',
    '1179267456.0dchiappe': 'Adam Goodprice',
    '1179269632.0dchiappe': 'Tori',
    '1179360256.0dchiappe': 'Slim',
    '1179523435.84dchiappe': 'Emma',
    '1179961216.0dchiappe': 'Big Phil',
    '1179966336.0dchiappe': 'April May',
    '1180720000.0dchiappe1': 'Captain Job',
    '1181171584.0dxschafe0': 'John Wallace',
    '1181260288.0dxschafe': 'Philip Fuller',
    '1181260928.0dxschafe': 'Davy Turnbull',
    '1181261824.0dxschafe': 'James MacDougal',
    '1181262976.0dxschafe': 'Nelson Templeton',
    '1181263360.0dxschafe': 'Edward Shackleby',
    '1181264512.0dxschafe': 'Ruth Armstrong',
    '1181267712.0dxschafe': 'Clayton Collard',
    '1181267968.0dxschafe': 'Jonathan Fairbanks',
    '1181348864.0dxschafe': 'Nelson Welch',
    '1181593472.0dxschafe': 'Boatswain Bill',
    '1181605248.0dxschafe': 'Daniel Vallance',
    '1181606272.0dxschafe': 'Alexander Thayer',
    '1181607808.0dxschafe': 'Samuel Wright',
    '1181610880.0dchiappe': 'Christopher Scott',
    '1181610880.0dchiappe0': 'Sean Tones',
    '1181683840.0dchiappe0': 'Myrna',
    '1181684480.0dchiappe0': 'Little Bob',
    '1182823328.56MAsaduzz': 'Tom Sailbreaker',
    '1185244008.29MAsaduzz': 'Mark Plunderscum',
    '1185831040.0dxschafe': 'Enrique Backginty',
    '1185831296.0dxschafe': 'Matthew Hullbowers',
    '1185831680.0dxschafe0': 'Lawrence McShoe',
    '1185832192.0dxschafe1': 'Jim Wavemonger',
    '1185832448.0dxschafe': 'Edward Blastscarlett',
    '1186098688.0dxschafe': 'Anton Levy',
    '1187219584.0dxschafe0': 'Shane McGreeny',
    '1187306240.0dxschafe': 'Simon Hornbow',
    '1187658240.0dxschafe': 'Simon Coalmorrigan',
    '1187658240.0dxschafe0': 'Edgar Chipburn',
    '1187658240.0dxschafe1': 'Samuel Wildbeard',
    '1187658368.0dxschafe': 'Isaiah McPratt',
    '1187658368.0dxschafe0': 'Marc Badmorrigan',
    '1187658368.0dxschafe1': 'Dog Warbones',
    '1187658496.0dxschafe': 'Bart Tackkidd',
    '1187658496.0dxschafe0': 'Thomas Sharkspinner',
    '1187658496.0dxschafe1': 'Jason Calicobutler',
    '1189456447.08kmuller': 'Carlos Cienfuegos',
    '1190420608.0dxschafe1': 'Officer Miller',
    '1190420736.0dxschafe': 'Captain Gentry',
    '1190742400.0dxschafe': 'Davy Dreadbutler',
    '1190743269.78dxschafe': 'Will Wildshot',
    '1190744085.78dxschafe': 'Hector Keelgrin',
    '1190744501.14dxschafe': 'Billy McKidd',
    '1190745256.48dxschafe': 'Enrique Stormbatten',
    '1192230656.0dchiappe': '',
    '1192233344.0dchiappe': '',
    '1192233344.0dchiappe0': '',
    '1192233344.0dchiappe1': '',
    '1192233472.0dchiappe': '',
    '1192233472.0dchiappe0': '',
    '1192233472.0dchiappe1': '',
    '1192233600.0dchiappe': '',
    '1192472192.0dchiappe': '',
    '1192472320.0dchiappe': '',
    '1192472448.0dchiappe0': '',
    '1192472576.0dchiappe0': '',
    '1192474368.0dchiappe': '',
    '1192474496.0dchiappe': '',
    '1192474624.0dchiappe': '',
    '1192474624.0dchiappe0': '',
    '1192491904.0dchiappe': '',
    '1192494848.0dchiappe0': '',
    '1192495488.0dchiappe': '',
    '1192495488.0dchiappe0': '',
    '1192495872.0dchiappe0': '',
    '1192495872.0dchiappe1': '',
    '1192495872.0dchiappe2': '',
    '1192496000.0dchiappe': '',
    '1192496640.0dchiappe': '',
    '1192558464.0dchiappe': '',
    '1192558464.0dchiappe0': '',
    '1192558976.0dchiappe': '',
    '1192558976.0dchiappe0': '',
    '1192561024.0dchiappe': '',
    '1196893440.0dxschafe': 'James Darkvane',
    '1196894976.0dxschafe': 'Grace Truesilver',
    '1196896512.0dxschafe': 'Nathaniel Truehound',
    '1196897792.0dxschafe0': 'Basil Tacktimbers',
    '1196898944.0dxschafe': 'Tobias Pugpratt',
    '1196901888.0dxschafe': 'Hector Daggerflint',
    '1196904064.0dxschafe': 'Isaiah Callecutter',
    '1196907776.0dxschafe0': 'Dajin Ming',
    '1196911744.0dxschafe0': 'Maria Lockspinner',
    '1201025280.0dxschafe': 'Lala Lovel',
    '1201028352.0dxschafe': "Solomon O'Dougal",
    '1201109074.66dxschafe': 'Sarah',
    '1201223902.67dxschafe': 'Engenio Fausto',
    '1201224743.34dxschafe': 'Nina Perpetua',
    '1201225541.73dxschafe': 'Anselmo Flavio',
    '1201226462.13dxschafe': 'Blanca Cruz',
    '1201227181.3dxschafe': 'Adoria Dolores',
    '1201228098.28dxschafe': 'Perla Alodia',
    '1201229350.47dxschafe': 'Cesar Gonzalo',
    '1201230131.11dxschafe': 'Mercedes Corazon',
    '1201548787.04kmuller': 'Veronique Roux',
    '1201821619.0dxschafe': 'Goslin Prymme',
    '1202419919.16akelts': 'Gunpowder Sam',
    '1202519757.13akelts': 'Pierre le Porc',
    '1203449603.97akelts': 'Garcia de la Avaricia',
    '1203451028.89akelts': 'Gabriel De Martillo',
    '1203451240.81akelts': 'Gunpowder Stan',
    '1207073489.41mtucker': 'Roland Raggart',
    '1208537612.06akelts': 'Alain Boniface',
    '1208543583.91akelts': 'Genevieve',
    '1208544322.67akelts': 'Jean Luc Pierpont',
    '1208544716.73akelts': 'William Rousseau',
    '1208545146.78akelts': 'Donatien',
    '1208546953.92akelts': 'Lieutenant Rodolphe',
    '1208548168.92akelts': 'Alejandro Vargas',
    '1208548525.28akelts': 'Lorenzo Medina',
    '1208548943.97akelts': 'Pedro Del Mar',
    '1208549359.09akelts': 'Marcos Hilo De Rosca Verde',
    '1208549913.56akelts': 'Enrique Sordo Del Tono',
    '1208898135.26akelts': 'Billy Prowcutter',
    '1208900438.95akelts': 'Edgar Burndavis',
    '1208908477.73akelts': 'Isaiah Chipmartin',
    '1209749843.55dxschafe': 'Captain Jack Sparrow',
    '1210018399.53akelts': 'Hector Gunfury',
    '1211912448.0WDIG1': 'Will Rigsmythe',
    '1211925120.0WDIG': 'Bart Blastward',
    '1211926144.0WDIG': 'Bart Ropeskull',
    '1211929216.0WDIG1': 'Enrique Dreadgrin',
    '1211929472.0WDIG': 'Hector Hexbain',
    '1212432000.0WDIG1': 'Amelia Sunfellow',
    '1213217861.99aapatel': 'Gerard Truehawk',
    '1213222099.15aapatel': 'Sam Ropevane',
    '1213290094.5aapatel': 'Jamie Helmpaine',
    '1213290386.14aapatel': 'Samuel Rigratte',
    '1213290548.56aapatel': 'Roger Ironbreaker',
    '1213290785.14aapatel': 'Edward Truespinner',
    '1213291115.62aapatel': 'Charles Foulhazzard',
    '1213737632.73aapatel': 'Tobias Hookshot',
    '1213983053.36aapatel': 'Leon Warhawk',
    '1214345458.84WDIG': 'Dog Lockgrim',
    '1214345910.48WDIG': 'Maggie Rigrage',
    '1216249894.26aapatel': 'Bartholomew Pugfury',
    '1216766113.92aapatel': 'Basil Calledougal',
    '1218760328.71mtucker': 'Venom Lash',
    '1218760329.71mtucker': 'Malicioso',
    '1219104942.43mtucker': 'Captain Ackers',
    '1219105162.48mtucker': 'Captain Swain',
    '1219277508.79mtucker': 'Dreadtooth',
    '1219277509.79mtucker': 'Hardtack',
    '1219339266.79mtucker': 'Samuel',
    '1219352693.09mtucker': 'Neban the Silent',
    '1219367627.94mtucker': 'Remington the Vicious',
    '1219426331.38mtucker': 'Bonerattler',
    '1219434293.16mtucker': 'General Sandspine',
    '1219895971.52mtucker': 'Ensign Grimm',
    '1219965016.25mtucker': 'Delilah Dunsmore',
    '1219972782.3mtucker': 'Miguel Montoya',
    '1220039541.89mtucker': 'Miguel Sanchez De Montoya',
    '1220906480.53mtucker': 'General Hex',
    '1222295766.63WDIG': 'Jade Bladefury',
    '1225143157.81caoconno': 'Sid Shufflefoot',
    '1225145929.75caoconno': 'Jenny Jigfiddle',
    '1227583229.75WDIG': 'Grace',
    '1227674362.91WDIG': "Angel O'Bonney",
    '1229139756.35mtucker': 'Dedrie Dunnam',
    '1229141258.23mtucker': 'Sid Tackem',
    '1229145127.43mtucker': 'Erin Amorous',
    '1232061565.89WDIG': 'Rose Seafellow',
    '1232496514.28WDIG': 'Edgar Shipcrash',
    '1234556416.0ian': 'Mych Swain',
    '1234557184.0ian': 'Bran Winds',
    '1236291353.28dxschafe': 'Dog Shoresmythe',
    '1236291541.44dxschafe': 'Chris Bilgemonger',
    '1236294629.2dxschafe': 'Johnny Redparr',
    '1237497701.52piwanow': 'Pelagia',
    '1237499258.14piwanow': 'Heartless Rosaline',
    '1237850626.09piwanow': 'Clemence Basilshot',
    '1238440501.07piwanow': 'General Darkhart',
    '1238441187.46piwanow': 'Undead Timothy Dartan',
    '1238705152.0akelts': 'Peter Chipbutler',
    '1239054611.47piwanow': 'Roman Paine',
    '1240950699.65ian': 'Fletcher Beakman',
    '1241477820.93ian': 'Horatio Fowler',
    '1241909300.25ian': 'Elijah Minor',
    '1241911057.44ian': 'Henry Lowman',
    '1244583168.0jloehrle0': 'Croquettes De Crabe',
    '1244657664.0jloehrle1': 'Devil Root',
    '1244832512.0jloehrle': 'Hive Queen',
    '1244833920.0jloehrle': 'Scatter Snap',
    '1247517440.0jloehrle': 'General Bloodless',
    '1248131584.0jloehrle': 'Edward Blastscarlett',
    '1248132224.0jloehrle': 'Jim Wavemonger',
    '1248132864.0jloehrle': 'Enrique Backginty',
    '1248133504.0jloehrle': 'Lawrence McShoe',
    '1248134144.0jloehrle': 'Matthew Hullbowers',
    '1248199552.0jloehrle': 'Benjamin  Tackparr',
    '1248199936.0jloehrle': 'Nate Pondwallace',
    '1248200320.0jloehrle': 'Gertrude Brawlgrim',
    '1248200576.0jloehrle': 'Solomon Brawlgrim',
    '1248201216.0jloehrle': 'George Burnwash',
    '1248201728.0jloehrle': 'Sven Yellowmartin',
    '1248201856.0jloehrle': 'Henry Chipburn',
    '1248202112.0jloehrle': 'Sarah Chipbonney',
    '1248203967.73jloehrle': 'William Truegrin',
    '1248740960.66piwanow': 'Samuel Shaw',
    '1248741261.66piwanow': 'Captain Ezekiel Rott',
    '1248741262.66piwanow': 'Bill Barrett',
    '1248741263.66piwanow': 'Nathan Gould',
    '1248741264.66piwanow': 'Jeremiah Dedman',
    '1249597696.0jloehrle0': 'David Ropewash',
    '1249599104.0jloehrle': 'Bart Badrage',
    '1249601792.0jloehrle': 'Greasegrin',
    '1249602048.0jloehrle': 'Bess Wildswine',
    '1249602432.0jloehrle': 'Jeremiah Chipvane',
    '1249602688.0jloehrle': 'Jamie Chipvane',
    '1249602944.0jloehrle': 'Ned Tackfoote',
    '1249603200.0jloehrle': 'Redcrash',
    '1249603328.0jloehrle': 'Simon Pondeaston',
    '1251756860.22dxschafe': 'Captain Cromwell',
    '1251763534.81dxschafe': 'Constance Sorrow',
    '1251763835.16dxschafe': 'Old Soot',
    '1251856397.47dxschafe': 'Richard Deckman',
    '1251857290.22dxschafe': 'Juan Miguel Torres',
    '1251913179.72dxschafe': 'Sid Shortwell',
    '1251914925.69dxschafe': "Elizabeth O'Malley",
    '1252090328.12dxschafe': 'Isabelle Flora',
    '1252092367.79dxschafe': 'Beth Daggerskull',
    '1255029860.03dxschafe': 'Msf',
    '1255029876.83dxschafe': 'Mms',
    '1255029886.73dxschafe': 'Mmi',
    '1255029910.67dxschafe': 'Mtp',
    '1255029916.88dxschafe': 'Mtm',
    '1255029948.89dxschafe': 'Mrf',
    '1255029956.77dxschafe': 'Mrs',
    '1255037912.05dxschafe': 'Mri',
    '1255037925.48dxschafe': 'Mrp',
    '1255037932.34dxschafe': 'Mrm',
    '1255038144.3dxschafe': 'Fsf',
    '1255038147.83dxschafe': 'Fms',
    '1255038150.81dxschafe': 'Fmi',
    '1255038153.66dxschafe': 'Ftm',
    '1255038155.14dxschafe': 'Ftp',
    '1255038202.58dxschafe': 'Frm',
    '1255038203.62dxschafe': 'Frf',
    '1255038204.59dxschafe': 'Frp',
    '1255038205.52dxschafe': 'Fri',
    '1255038206.44dxschafe': 'Frs',
    '1258054417.88Admin': 'Old Gregg',
    '1260979741.83Admin': 'Rusty McGinnis',
    '1260981043.51Admin': 'Sven Rigfury',
    '1260985636.31Admin': 'Old Greg',
    '1261093737.49laura': 'Ray Fishlander',
    '1261094727.21laura': 'Sven Hooksilver',
    '1261095633.48laura': 'Ben Callebutler',
    '1261096000.76laura': 'Geoffrey Bridgebreaker',
    '1271974738.71akelts': 'Simon Shipward',
    '1271976250.93akelts': 'James Stormhazzard',
    '1274739846.83gcarranza': "Basil O'Morrigan",
    '1274819841.73gcarranza': 'Crazy Ned',
    '1274825376.01gcarranza': 'Thomas Fishmeister',
    '1274825967.94gcarranza': 'Madam Zigana',
    '1274889994.04gcarranza': 'El Patron',
    '1274890958.87gcarranza': 'Dr. Bellrog',
    '1274892762.3gcarranza': 'Widow Threadbarren',
    '1274894542.99gcarranza': 'Se\xc3\xb1or Fantifico',
    '1274906957.35gcarranza': 'Kudgel',
    '1274908180.63gcarranza': 'Ben Clubheart',
    '1274909359.61gcarranza': 'Sadie Clubheart',
    '1277832852.05dxschafe': 'M_Royal_Musketeer',
    '1277832913.08dxschafe': 'F_Emerald_Duelist',
    '1277832916.36dxschafe': 'F_Merchant_Voyager',
    '1277832917.82dxschafe': 'F_Town_Mayor',
    '1277832921.32dxschafe': 'M_Treasure_Hunter',
    '1277832922.44dxschafe': 'M_Town_Mayor',
    '1277832923.36dxschafe': 'M_Treasure_Hunter_B',
    '1277832924.25dxschafe': 'M_Emerald_Duelist',
    '1277832925.16dxschafe': 'M_Merchant_Voyager',
    '1277832926.05dxschafe': 'M_English_Nobleman',
    '1277832927.1dxschafe': 'F_Royal_Musketeer',
    '1277833028.64dxschafe': 'F_English_Noblewoman',
    '1277833523.94dxschafe': 'M_Crimson_Captain',
    '1277833525.66dxschafe': 'F_Spanish_Adventurer',
    '1277833526.86dxschafe': 'M_Spanish_Adventurer',
    '1277833527.95dxschafe': 'M_Spanish_Conquistador',
    '1277833528.99dxschafe': 'F_Pligim_Explorer',
    '1277833530.07dxschafe': 'M_Pligim_Explorer',
    '1277833531.13dxschafe': 'M_French_Fencer',
    '1277833532.22dxschafe': 'F_Crimson_Captain',
    '1277833533.36dxschafe': 'F_French_Fencer',
    '1277833534.42dxschafe': 'F_Oriental_Merchant',
    '1277833535.72dxschafe': 'F_Spanish_Conquistador',
    '1277833536.83dxschafe': 'M_Oriental_Merchant',
    '1277843620.94dxschafe': 'M_Royal_Musketeer_B',
    '1277845266.38dxschafe': 'F_Royal_Musketeer_B',
    '1277849728.55dxschafe': 'F_Treasure_Hunter',
    '1277850061.07dxschafe': 'F_Treasure_Hunter_B',
    '1277853033.94dxschafe': "F_Raven'scove_Mercenary",
    '1277855750.58dxschafe': "M_Raven'scove_Mercenary",
    '1277924209.84dxschafe': 'M_Mystic',
    '1277925110.22dxschafe': 'F_Mysitc',
    '1277929694.5dxschafe': 'M_Capt_Black',
    '1277929712.11dxschafe': 'F_Blackbeard',
    '1277929716.66dxschafe': 'M_Partyanimal',
    '1277929721.28dxschafe': 'M_Blackbreard',
    '1277929725.03dxschafe': 'F_Partyanimal',
    '1277929728.64dxschafe': 'F_Capt_Black',
    '1277931989.49dxschafe': 'M_Commander',
    '1277932006.26dxschafe': 'F_Helmswoman',
    '1277932013.42dxschafe': 'M_Helmsman',
    '1277932017.96dxschafe': 'M_Surfer',
    '1277932022.68dxschafe': 'F_Surfer',
    '1277932025.9dxschafe': 'F_Commander',
    '1277932153.08dxschafe': 'M_Leader',
    '1277932165.46dxschafe': 'F_Leader',
    '1277932280.91gcarranza': 'Roger Damphogge',
    '1277935279.66dxschafe': 'M_Amethyst',
    '1277935295.31dxschafe': 'F_Amethyst',
    '1277938375.9dxschafe': 'M_Raider',
    '1277938401.4dxschafe': 'F_Raider',
    '1277940155.88dxschafe': 'M_Partyhearty',
    '1277940170.29dxschafe': 'F_Partyhearty',
    '1277941714.21robrusso': 'T-Bones the Bouncer',
    '1279651185.6gcarranza': 'Ramona Vda. De Guerra',
    '1280875709.87dxschafe': 'Mr Santa',
    '1280875871.29dxschafe': 'Mr Mardi Gras',
    '1280876353.51dxschafe': "St Patty's",
    '1280876588.5dxschafe': 'St Valentine',
    '1280877008.52dxschafe': 'Mrs Santa',
    '1280877290.27dxschafe': 'Ms Mardi Gras',
    '1280877636.58dxschafe': "Ms Patty's Day",
    '1280877967.31dxschafe': "Ms Valentine's",
    '1281130350.14dxschafe': 'Scar',
    '1281653252.78dxschafe': 'Jamie Foulcrash',
    '1281653262.7dxschafe': 'Rose Cabinmenace',
    '1285622621.56robrusso': 'Sgt. Scrimmage',
    '1285875480.62kanpatel': 'Kat Repperson',
    '1286922173.8gcarranza': 'Bargain Billy',
    '1286984549.68gcarranza': 'Monger Morton',
    '1286991539.99gcarranza': 'Peddler Phillip',
    '1286991877.14gcarranza': 'Davy Doubloon',
    '1291327895.46jloehrle': 'Foulberto Smasho',
    '1302895055.78jloehrle': 'LaSchafe',
    'Jack Sparrow Tutorial': 'Jack Sparrow',
    'tutorial_chat': 'Captain Bo Beck',
    'tutorial_dan': 'Doggerel Dan',
    'tutorial_stumpy': 'Captain Bo Beck' }
