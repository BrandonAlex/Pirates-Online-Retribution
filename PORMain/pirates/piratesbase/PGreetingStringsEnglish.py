from pirates.quest.QuestConstants import NPCIds
from pirates.quest.QuestPrereq import *
from pirates.ai import HolidayGlobals
from pirates.piratesbase import EmoteGlobals as EG

TownfolkGreetings = [
    {
        'strings': [
            ('Hello.', None),
            ('Good day.', None)] }]
TownfolkGoodbyes = [
    {
        'prereqs': [
            IsHoliday(HolidayGlobals.WINTERFESTIVAL)],
        'strings': [
            ('Aye mate, wishing ye a fine holiday season!', EG.EMOTE_WINK),
            ('Farewell, have a great festive season!', EG.EMOTE_WINK),
            ('Happy Holidays!', EG.EMOTE_SMILE),
            ('Goodbye, now back to celebrating...', EG.EMOTE_DANCE_JIG)] },
    {
        'strings': [
            ('Goodbye.', EG.EMOTE_WAVE),
            ('Farewell.', EG.EMOTE_WAVE)] }]
TownfolkEncourage = [
    {
        'strings': [
            ('Keep at it, mate!', None),
            ("Come back when you're finished", None)] }]
TownfolkBrushoff = [
    {
        'prereqs': [
            IsHoliday(HolidayGlobals.WINTERFESTIVAL)],
        'strings': [
            ("Hope you're having a fine, festive season!", EG.EMOTE_YES),
            ("Why are you standing here when there's celebrating to be done?!", EG.EMOTE_DANCE_JIG),
            ('Celebrate that the undead have retreated... for now.', EG.EMOTE_CELEBRATE),
            ('Fire work, all ye pirates for fighting off Jolly - Happy Holidays!', EG.EMOTE_SMILE),
            ("We can still celebrate the season, in spite of Jolly's best efforts, ey?", EG.EMOTE_WINK),
            ('Happy Holidays, mate! Now back to plundering...', EG.EMOTE_LAUGH),
            ("I hear rumor that Jolly's regrouping and will return soon.", EG.EMOTE_YES),
            ('I heard from a friend who heard from an undead scab that Jolly will return.', EG.EMOTE_SCARED),
            ("Don't be fooled by this quiet time - Jolly's not defeated. He's rebuilding.", EG.EMOTE_NO),
            ("The holiday's are so festive... makes me wanna dance the jig!", EG.EMOTE_DANCE_JIG),
            ("Enjoy the festive season mate for it won't last long.", EG.EMOTE_SMILE),
            ("The Caribbean's the best place to endure winter, ey?", EG.EMOTE_WINK),
            ('Fine weather, ey? Poor blokes back in England are freezing their backsides off!', EG.EMOTE_LAUGH),
            ("Celebrate now mates - for soon Jolly will return and it's back to battle!", EG.EMOTE_DANCE_JIG),
            ("Don't stand there gawking, grab some cards and let's make merry, ey?", EG.EMOTE_SMILE),
            ("Glad I'm here instead of jolly old England right now, even with the invasions!", EG.EMOTE_LAUGH),
            ("Don't bother me mate, I'm making merry!", EG.EMOTE_DANCE_JIG),
            ("Take some time off a plunderin' to enjoy the festive season!", None),
            ('Ahoy mate, too much festive-ness, gotta get more sleep!', EG.EMOTE_SLEEP),
            ('I love this festive season... makes me wanna laugh out loud!', EG.EMOTE_LAUGH),
            ("Yes! 'Tis the season to celebrate, mate!", 'emote_celebrate'),
            ("Celebrate the season... while Jolly's off regrouping.", EG.EMOTE_DANCE_JIG),
            ("Hard for me to celebrate when I fear Jolly's return any day now!", EG.EMOTE_NO)] },
    {
        'strings': [
            ("Thought I'd remind you, Peddler merchants offer brand new clothes on the first of every month.", None),
            ('Ahoy there - have ye learned to repair ships yet?', None),
            ("Why're you standing there when you could be making potions?", None),
            ('The Shipwrights need your help repairing ships.', EG.EMOTE_WAVE),
            ('A whole new set of daggers have made their way to the islands. ', EG.EMOTE_SMILE),
            ('Been fishing? Caught anything? If not, try it again. It gets easier, trust me. ', EG.EMOTE_YES),
            ("Blimey, rumors of the Queen Anne's Revenge stalking ships at sea be too much for m'nerves!", EG.EMOTE_SCARED),
            ("Don't stand there chattin' with me, get yourself some throwin' knives! ", None),
            ("Fishing for Legendary fish? Good luck, you'll need it, and a strong fishing reputation! ", None),
            ("Fishing's fun, mate. Try your hand on the docks of Padres, Port Royal or Tortuga. ", None),
            ("Fishmasters can tell a whale of a tale about some of them 'Legendary' fish so go ask them! ", None),
            ('Got any new weapons? Like the Sword of Triton?', EG.EMOTE_SMILE),
            ('Got yer hands on any of them new daggers, mate? ', None),
            ('Have you noticed the gunsmiths have more weapons these days?', EG.EMOTE_YES),
            ('Heard about those new daggers? Rumor has it they once belonged to assassins ', None),
            ('Hello mate, be wary of these new daggers. Deadly things they are. ', None),
            ('I hear sailors telling tales of a mysterious island. ', None),
            ("I hear there are many types of fish for catching. Keep casting 'til you land the biggest and best! ", None),
            ("I hear the Queen Anne's Revenge sails with vast plunder. But only the bravest would dare accept that challenge.", None),
            ('Sabres, Broadswords, Cursed Blades and now the Sword of Triton?', None),
            ("I hear ye can get a throwin' knife by defeatin' undead types.", None),
            ("If I had my sea-legs back, first thing I'd do is buy a fishing boat.", None),
            ("Invasions, Fleets and now the Queen Anne's Revenge! 'Tis a time of great conflict in the Caribbean.", EG.EMOTE_ANGRY),
            ("Legend tells us the Sword of Triton holds special abilities when used against the crew of the Queen Anne's Revenge.", None),
            ('Look lively mate! Treasure Fleets are on the patrol! ', None),
            ('Jolly will NOT stop invading until he rules the islands!', EG.EMOTE_ANGRY),
            ("Keep a look out for those throwing knives! Their good for fightin' the undead.", None),
            ("Legendary fish are ready to be caught, be only by someone's who's fishing reputation is high.", None),
            ('Look lively mate! Get down to the docks of Tortuga, Padres and Port Royal for some fishing! ', None),
            ('Need something to do? Try fishing at the end of the Port Royal, Tortuga and Padres docks! ', None),
            ("Our spies say that Jolly's furious so expect more invasions.", EG.EMOTE_YES),
            ('Pssst - I hear more invasions are coming, sharpen your steel, mate.', EG.EMOTE_SMILE),
            ('Rumor has it that loot can be found in the belly of fish some Pirates are catching. ', None),
            ('Rumor has it that some throwing knives can be purchased from shops. ', None),
            ("Seen Blackbeard's Sword of Triton? Its jeweled hilt is one to admire.", EG.EMOTE_YES),
            ("Talk of throwing knives are on everyone's lips - you found one yet? ", None),
            ("The Undead invasions will only end when Jolly's defeated...permanently.", EG.EMOTE_ANGRY),
            ('Think Jolly will stop invading because he got some Lost Weapons?  No way!', EG.EMOTE_NO),
            ('Tired of fishing from the docks? I hear you can actually buy a fishing boat. ', None),
            ('Truth is mate, if ye wants some throwing knives or daggers, defeat the Undead. ', None),
            ("Wanna try out fishing? Ask the Fishmasters and they'll give you a rod and lure! ", None),
            ('Why are you talking to me when there are Bandits attacking! Get to the Cannon Defense towers! ', None),
            ('Pirates have found the mighty Sword of Triton but the true prize be the ship from which it came.  ', None),
            ('I would not dare challenge the Queen Anne and her mighty crew!', EG.EMOTE_SCARED),
            ("Set foot upon Raven's Cove and it may be the last step you take.", None),
            ("There's an evil at Raven's Cove that even the most bloodthirsty pirates fear.", EG.EMOTE_SCARED),
            ("Dare to go to Raven's Cove while it's day, for nightfall brings untold terror.", None),
            ("I'm not sure the weapons you'll need to survive Raven's Cove... or if any will do.", EG.EMOTE_NO),
            ("Gold's worthless at Raven's Cove... unless you encounter a greedy ghost.", EG.EMOTE_NO),
            ("If you're headed to Raven's Cove, sharpen your weapons 'cause negotiatin' won't help there.", None),
            ("I've heard of phantoms at Raven's Cove. Night ones more fierce than day ones.", None),
            ("Many eyed Raven's Cove seeking fortune, but all they found was death.", EG.EMOTE_SCARED),
            ("Truth about Raven's Cove, watch your back and your front, but mostly your soul!", None),
            ("Curious why it's called Raven's Cove, know a tad bit about omens?", None),
            ("I scrubbed my hands of the rumors surrounding Raven's Cove... but they tend to be true.", None),
            ("You say you don't scare easily, but you've never ventured onto Raven's Cove at night.", None),
            ("The forces of evil at Raven's Cove may play a game of tug-of-war with your immortal soul.", EG.EMOTE_SCARED)] }]
PirateGreetings = [
    {
        'strings': [
            ('Ahoy!', None),
            ('Ahoy there!', None),
            ('Avast me hearties!', None),
            ('Avast!', None),
            ('Avast, ye landlubber!', None)] }]
PirateGoodbyes = [
    {
        'strings': [
            ('Arrr!', EG.EMOTE_WAVE),
            ('Arrr matey!', EG.EMOTE_WAVE),
            ("Back to plunderin'!", EG.EMOTE_WAVE),
            ('Best be watchin yer back matey!', EG.EMOTE_WINK)] }]
PirateEncourage = [
    {
        'strings': [
            ('Keep at it, mate!', None),
            ("Ye're not done yet", None)] }]
PirateBrushoff = [
    {
        'strings': [
            ('Bother someone else, mate', None),
            ('Nothing here for ye', None),
            ("Bug off mate, I'm busy", None),
            ("Don't stare at the sun, mate, it'll blind ye", None),
            ('Word to the wise -- keep your steel sharp and a sharp eye', None),
            ('Dead men tell no tales, so they say', None)] }]
FormalGreetings = [
    {
        'strings': [
            ('Welcome', None),
            ('Greetings', None),
            ('We meet again.', None),
            ('How may I help you?', None)] }]
FormalGoodbyes = [
    {
        'prereqs': [
            IsHoliday(HolidayGlobals.WINTERFESTIVAL)],
        'strings': [
            ('Goodbye, wishing ye a fine holiday season!', None),
            ('Farewell, have a great festive season!', None),
            ('Happy Holidays and come back soon!', None)] },
    {
        'strings': [
            ('Farewell', None),
            ('Goodbye', None),
            ('Come back again sometime.', None)] }]
GypsyGreetings = [
    {
        'strings': [
            ('Good-day', None),
            ('Greetings', None)] }]
GypsyGoodbyes = [
    {
        'prereqs': [
            IsHoliday(HolidayGlobals.WINTERFESTIVAL)],
        'strings': [
            ('Aye mate, wishing ye a fine holiday season!', None),
            ('Farewell, have a great festive season!', None),
            ('Happy Holidays!', None)] },
    {
        'strings': [
            ('Farewell', None),
            ('Goodbye', None)] }]
GypsyEncourage = [
    {
        'strings': [
            ('Keep trying', None),
            ('You must finish before you return', None)] }]
GypsyBrushoff = [
    {
        'strings': [
            ('I have nothing for you', None),
            ('Try someone else', None)] }]
ShipPVPLordBrushoff = [
    {
        'strings': [
            ("There's no battle yet! Come back when there's a use for you.", None),
            ("Can't you see that I'm busy? I'm planning my attack and I have no work for you yet.", None),
            ("There's no way we'll lose! A fierce battle this will be!", None),
            ("We'll need recruits if you are interested. Check back with me soon.", None),
            ("He'll regret the day he crossed me! The islands will be mine!", None)] }]
StowawayGreetings = [
    {
        'strings': [
            ("Lookin' to steal away to another island quickly, ey?  I am the right man.", None),
            ('Need to get to another port fast?  No worries, mate.  But...it will cost ye.', None),
            ('I can get ye to another place, anyplace in the islands fast...for a fee.', None),
            ('Get somewhere fast, huh?  I can help.  For a fee.', None),
            ("Needin' to leave quickly? I understand.  I'll make it happen...for a price.", None),
            ("I'll get ye to another island, but don't tell a soul about me side business, ey?", None),
            ('Ye need to get out of town, I need some extra gold...we can work something out.', None),
            ("Halo mate, I've got a crate just your size...if ye can offer me a tip, savvy?", None)] }]
StowawayGoodbyes = [
    {
        'strings': [
            ('Mind the rats, mate!', None),
            ('Stay dry...if you can!', None),
            ('Godspeed, mate.', None),
            ("Hope ye don't sink!", None),
            ('Stay afloat, mate!', None),
            ('Thanks for yer business!', None),
            ('Come again soon.', None),
            ('Fair winds, mate.', None)] }]
StowawayBrushoff = [
    {
        'strings': [
            ('Get along mate, I be busy!', None),
            ("I've no time for idle chatter.  Come back another time.", None),
            ("I've got cargo to handle and EITC rats sniffing around.  Come back later.", None),
            ("I'm busy, come back later.", None),
            ("Can't ye see I'm busy?  Come back later.", None),
            ("Can't talk now, people are watchin'.Come back later.", None)] }]
FishmasterFirstGreeting = "Ahoy, me bucko! Seein' as you're here, I gather you're lookin' to fish. Well, you'll be needin' a rod and lures. Just come back to me if ye need more."
FishmasterUpgradeRod = 'There you go, good as new!'
FishmasterGreetings = [
    {
        'strings': [
            ("I've got rods, lures, and more than one tale to tell.", None)] }]
FishmasterGoodbyes = [
    {
        'strings': [
            ('Farewell', None),
            ('Goodbye', None)] }]
FishmasterEncourage = [
    {
        'strings': [
            ('Keep trying', None),
            ('You must finish before you return', None)] }]
FishmasterBrushoff = [
    {
        'strings': [
            ('I have nothing for you', None),
            ('Try someone else', None)] }]
CannonmasterGreetings = [
    {
        'strings': [
            ("You there, can you man a cannon? Drive off these treasure-stealin' bandits and I'll pay ye well!", None),
            ("The treasure's under attack again! I've an unmanned Navy Cannon for yeh and some coin for yer trouble.", None),
            ("Bandits 're after the treasure! There's coin in 't for the cannoneer who sends 'em down to Davy Jones'!", None)] }]
CannonmasterGoodbyes = [
    {
        'strings': [
            ('Farewell', None),
            ('Goodbye', None)] }]
CannonmasterEncourage = [
    {
        'strings': [
            ('Keep trying', None),
            ('You must finish before you return', None)] }]
CannonmasterBrushoff = [
    {
        'strings': [
            ('The cannons all be manned. Come back later.', None),
            ('The bandits are already being driven off. Try again another time.', None)] }]
ScrimmageMasterGreetings = [
    {
        'strings': [
            ('Feel like you can show us your strength? Come and join the Navy!', None)] }]
ScrimmageMasterGoodbyes = [
    {
        'strings': [
            ('Farewell', None)] }]
ScrimmageMasterEncourage = [
    {
        'strings': [
            ('Keep trying', None)] }]
ScrimmageMasterBrushoff = [
    {
        'strings': [
            ('We have enough men right now. Come back again later!', None)] }]
CustomGreeting = [
    {
        'strings': [
            ()] }]
SamSeabonesGoodbye = [
    {
        'strings': [
            ('Fare thee well.', None)] }]
SamSeabonesBrushoff = [
    {
        'strings': [
            ('Port Royal is for the people.', None)] }]
JosieMcReedyGreeting = [
    {
        'strings': [
            ('Are you in need of some work? I always have plenty.', None)] }]
JosieMcReedyGoodbye = [
    {
        'strings': [
            ('See you soon.', None)] }]
JosieMcReedyBrushoff = [
    {
        'strings': [
            ("I'm busy.", None)] }]
PeterChipparrGreeting = [
    {
        'strings': [
            ('Make it quick.', None)] }]
PeterChipparrGoodbye = [
    {
        'strings': [
            ('Bye.', None)] }]
PeterChipparrBrushoff = [
    {
        'strings': [
            ('Problem, mate?', None)] }]
BWatkinsGreeting = [
    {
        'strings': [
            ('Keep your voice down, mate.', None)] }]
BWatkinsGoodbye = [
    {
        'strings': [
            ("I don't know you.", None)] }]
BWatkinsBrushoff = [
    {
        'strings': [
            ('We got no business.', None)] }]
ShaneMcGreenyGreeting = [
    {
        'strings': [
            ('Need a bit of help at the poker tables?', None)] }]
ShaneMcGreenyGoodbye = [
    {
        'strings': [
            ('Be careful out there!', None)] }]
ShaneMcGreenyBrushoff = [
    {
        'strings': [
            ('Leave me alone, mate.', None)] }]
TiaDalmaGreeting = [
    {
        'strings': [
            ('Welcome, dear.', None)] }]
TiaDalmaGoodbye = [
    {
        'strings': [
            ('May good spirits guard you!', None)] }]
TiaDalmaEncourage = [
    {
        'strings': [
            ('There is still work for you to be done.', None)] }]
TiaDalmaBrushoff = [
    {
        'strings': [
            ('There is another place you should be.', None)] }]
CrazyNedBrushoff = [
    {
        'prereqs': [
            WithinTimeOfDay(timeFrom = 20, timeTo = 6)],
        'strings': [
            ('The red spirits are after us all!', EG.EMOTE_SCARED),
            ('Me box, have to stay in me box!', EG.EMOTE_NERVOUS),
            ('Beware the Red ghosts!', EG.EMOTE_NERVOUS)] },
    {
        'prereqs': [
            HasQuest('rc.ghosts.helpAllGhosts')],
        'strings': [
            ("Booo! Booo! Finish yee quest or I'll smite yee with me ghostly powers!", None),
            ('Away Mortal! Yee have work to do!', None)] },
    {
        'strings': [
            ("Booo! Booo! Or I'll smite yee with me ghostly powers!", None),
            ('Away Mortal! Yee not be wanted here!', None)] }]
RavensCoveGhostBrushoff = [
    ('It may be too late to decide friend or foe.', None),
    ('A hearty welcome to death, destruction, fear & chaos.', None),
    ("Word to the wise, when the sun goes down...don't be around.", None),
    ("It's no lie, mate, we've seen better days here.", None),
    ('Say, mate, nights around here can be murder...and then some.', None),
    ('I pray you know the terrors involved here.', None),
    ("You may soon be wishin' you're back from whence you came.", None),
    ('Truth be told, it may be too late for your fate to be altered.', None),
    ('If you can survive here, you can survive anywhere!', None),
    ("You may soon wonder if you're among the living or the dead or both!", None),
    ('Ever have your soul haggled over?', None),
    ('I pray for the day the red spirits disappear.', None),
    ("Pssst, mate. Every square inch of Raven's Cove is haunted.", None),
    ('Beware the watchful eyes on you...mine included.', None),
    ("Life is cruel...and you've yet to see all of Raven's Cove.", None),
    ('Welcome to the scariest place on earth, matey!', None),
    ("Few have lived to tell the tale of Raven's Cove.", None),
    ("There be much unfinished business here on Raven's Cove.", None),
    ("You may soon be askin' yerself why you came to this place.", None),
    ("I be thinkin' you may be harboring a death wish, mate.", None)]
ThomasFishmeisterBrushoff = [
    {
        'strings': [
            ('Jolly cursed the seas and caused all the fish to flee.', EG.EMOTE_SAD),
            ("With Jolly's curse there were no fish and the townsfolk all starved.", EG.EMOTE_WAIT),
            ("You'll find no fish here, we've been cursed by Jolly Roger.", EG.EMOTE_NO),
            ('After Jolly Roger, all we have left here is tears.', EG.EMOTE_SAD),
            ('There are no longer fish for my fellow fishermen to catch.', EG.EMOTE_NO)] + RavensCoveGhostBrushoff }]
MadamZiganaBrushoff = [
    {
        'strings': [
            ('My voodoo defense against Jolly Roger came too late.', None),
            ("Voodoo is a risky bet against Jolly Roger's horrors.", None),
            ('I have found power in potions and you may too.', EG.EMOTE_YES),
            ("Keep a keen eye on your soul here at Raven's Cove, friend.", None),
            ("I foresaw Jolly Roger's ghastly attack too late.", None)] + RavensCoveGhostBrushoff }]
ThreadbarrenBrushoff = [
    {
        'strings': [
            ("I curse the day I was forced to sew sails for Jolly Roger's ships.", None),
            ('I weep for the poor souls who met their fate on account of me.', None),
            ("My soul won't rest until I make amends to those who perished.", None),
            ('I unhappily left this life, driven to death from exhaustion.', EG.EMOTE_SAD),
            ('Fabrics were hard to come by and my labor came at a stiff price.', None)] + RavensCoveGhostBrushoff }]
ClubheartsBrushoff = [
    {
        'strings': [
            ("Pity us. We bet our lives in a game with Jolly Roger's men and lost.", None),
            ("Beware the Skeleton poker game, chances are it's fixed.", None),
            ("We're surprised to find the likes of you here.", None),
            ('Many a folk here are heartless, soulless, penniless and clueless.', None),
            ("Mate, the odds are stacked against you here at Raven's Cove.", None)] + RavensCoveGhostBrushoff }]
FantificoBrushoff = [
    {
        'prereqs': [
            DidQuest('rc.ghosts.SenorFantifico')],
        'strings': [
            ('Cluck, Cluck.', None),
            ('Cluck, Cluck, Cluck?', None)] },
    {
        'strings': [
            ('Is there any way to bring me back to life, mate?', None),
            ('Being dead can sure be a bore around here.', None),
            ("This house is nice and all, but I'm dead for goodness sake.", None),
            ('I hate the fact that I died in the best of health and wealth.', EG.EMOTE_NO),
            ('I lost something here I hope you can help me find. My life!', None)] + RavensCoveGhostBrushoff }]
townfolkHelpText = {
    1: [
        "Ready to fly the French colours on that ship of yers?\x07 Be aware that sailing from an island like this, ye must know a thing or two.\x07First, Pirates who choose to embark from this scrap of an island will be thrown into a battle... whether they be wantin' to or not.\x07Second, be wary of the sail colours around ye. That way a pirate knows who's friend and who's foe.\x07And if ye be needin' to check your score, press the ~ button. That gives a ship's score AND its bounty.\x07Pirates earn both for sinkin' enemy ships. The higher a bounty, the more it's worth.\x07Fair winds and good luck, mate... ye be needin' both!"],
    2: [
        "Ready to fly the Spanish colours on that ship of yers?\x7Be aware that sailing from an island like this, ye must know a thing or two.\x07First, Pirates who choose to embark from this scrap of an island will be thrown into a battle... whether they be wantin' to or not.\x07Second, be wary of the sail colours around ye. That way a pirate knows who's friend and who's foe.\x07And if ye be needin' to check your score, press the ~ button. That gives a ship's score AND its bounty.\x07Pirates earn both for sinkin' enemy ships. The higher a bounty, the more it's worth.\x07Fair winds and good luck, mate... ye be needin' both!"],
    3: [
        "Please excuse me master, Pierre le Porc, he's had a bit of stress lately and isn't feeling so grand.\x07In his... absence, I'll brief ye on the situation and specifics of how the French can use your skills.\x07See, Pirate Lord Le Porc has claimed this island and others as his own.\x07There's only one problem though, he's not the only Pirate Lord lookin' to lay claim on what ain't his, savvy?\x07A Spanish Pirate Lord name of Garcia de la Avaricia thinks he's running these islands too!\x07A pirate like yerself can make earn quite a reputation in this fight and Pierre would be most grateful.\x07So consider yerself a true Frenchmen when ye set sail from this island mate, 'cause the Spanish sure will..."],
    4: [
        "Please excuse me master, Garcia de la Avaricia, he's had a bit of stress lately and isn't feeling so grand.\x07In his... absence, I'll brief ye on the situation and specifics of how the Spanish can use your skills.\x07See, Pirate Lord Avaricia has claimed this island and others as his own.\x07There's only one problem though, he's not the only Pirate Lord looking to lay claim on what ain't his, savvy?\x07A French Pirate Lord name of Le Porc thinks he's running these islands too!\x07A pirate like yerself can make earn quite a reputation in this fight and Garcia would be most grateful.\x07So consider yerself a true Spaniard when ye set sail from this island mate, 'cause the French sure will..."] }
