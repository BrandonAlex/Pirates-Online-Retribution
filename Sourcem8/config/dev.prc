# WINDOW SETTINGS:
window-title Pirates Online Retribution [Dev]

# ACCOUNT DB CONFIG:
# TODO: LOBLAO WILL PROBABLY REWRITE THIS.
backend dev
mongodb-url mongodb://localhost:27017
mongodb-name test
account-bridge-filename astron/databases/account-database.db

# SERVER SETTINGS:
server-version pirates-dev

# RPC SETTINGS:
want-rpc-server #f
rpc-server-endpoint http://localhost:8080/
rpc-server-secret 7456236a45345z4545

# ATTACKING:
want-all-weapons-trained #t
want-all-weapon-skills #t
want-dev-weapons #t
want-easy-combos #t
want-friendly-fire #f
instant-skill-recharge #f

# BATTLE
want-battle #f
cannon-fire-broadside-dist 3500
cannon-fire-dist 3500
skill-recharge-time -1.0
show-attack-calc 0

# BOSS BATTLES
black-pearl-repeat-reward #f

# CUTSCENES
#this is a string config
default-cutscene 1

# DC FILES:
dc-file astron/dclass/pirates.dc
dc-file astron/dclass/otp.dc

# DEVELOPER TOOLS/COMMANDS:
want-dev #f
want-rocketman #t
players-invulnerable #t
show-understandable #f
show-aggro-radius #f
want-invasion-npc-minimap #f
want-early-coderedemption #f
location-kiosk #t

# DOWNLOADER:
fake-downloads #f
fake-download-duration 15.0

# EVENTS:
test-fourth-of-july #f

# INTERACTIVES:
buried-treasure #t

# INVENTORY:
want-clothing-page #t

# MINIGAMES:
want-minigames #t
want-potion-game #t
want-fishing-game #t
want-repair-game #t
want-ship-repair-spots #t
want-show-off-fish #f

# NPC:
want-npcs #t
want-enemies #t
want-battle #f
npcs-auto-target #f
want-npc-notice #f
want-easy-combos #f

# PLAYER
want-hp-check #t
login-location-used-setRetLoc #f
want-run #f
want-pirates-run #f
immortal-mode #f

# PVP/SVS
want-pvp-team-balance #f
force-lookout #f
want-privateering #f
want-land-infamy #t
want-sea-infamy #t

# SAILING:
want-ship-threat #f
ships-follow-water #f
want-wake #f
ocean-visibility 1
infinite-ammo #f
ship-wake-dist 3800
ship-rock-dist 1000
want-seas-closed #t

# TELEPORTATION
teleport-all #t

# BAN
ban-do-ban #f
