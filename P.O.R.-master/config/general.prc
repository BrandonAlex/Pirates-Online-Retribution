window-title Pirates Online Retribution
icon-filename resources/phase_3/etc/pirates.ico

model-path resources/
model-path resources/phase_2
model-path resources/phase_3
model-path resources/phase_4
model-path resources/phase_5

default-model-extension .bam

# Audio and Graphics
audio-library-name p3fmod_audio
preferences-filename config/preferences.json

texture-anisotropic-degree 16
smooth-lag 0.4

# Networking

dc-file astron/dclass/pirates.dc
dc-file astron/dclass/otp.dc

server-port 6667
server-version retribution-dev

# Force paid status
force-paid-status FULL

# Disable cache
want-cache #t

# Disable tutorial
skip-tutorial 1

# Whitelist
want-whitelist #f

# Notify
default-directnotify-level info
