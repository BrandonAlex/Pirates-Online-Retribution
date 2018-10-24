# File: G (Python 2.4)

from pirates.piratesgui.BorderFrame import *
from pirates.piratesbase import PiratesGlobals
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesgui.RadioButton import *
from pirates.piratesgui.CheckButton import *
from pirates.piratesgui.GuiButton import *
from pirates.piratesgui.OptionMenu import *
from pirates.piratesgui.DialogButton import DialogButton
from direct.directnotify import DirectNotifyGlobal
from direct.gui import DirectGuiGlobals as DGG
from otp.otpgui import OTPDialog
from pirates.piratesgui import PDialog
from pirates.seapatch.Water import Water
from pandac.PandaModules import *

try:
    import embedded
except:
    pass


class GameOptionsGui(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('GameOptions')
    debug = False
    resolution_table = [
        (800, 600),
        (1024, 768),
        (1280, 1024),
        (1600, 1200)]
    widescreen_resolution_table = [
        (1280, 720),
        (1920, 1080)]
    MinimumHorizontalResolution = 800
    MinimumVerticalResolution = 600
    texture_low = 256
    texture_medium = 512
    texture_high = 1024
    texture_maximum = -1
    texture_scale_low = 0.25
    texture_scale_medium = 0.5
    texture_scale_high = 1.0
    texture_scale_maximum = 1.0
    textureScaleOptionList = [
        texture_scale_low,
        texture_scale_medium,
        texture_scale_high,
        texture_scale_maximum]
    textureOptionList = [
        texture_low,
        texture_medium,
        texture_high,
        texture_maximum]

    def __init__(self, gameOptions, title, x, y, width, height, options = None, file_path = None, pipe = None, access = 0, chooser = 0, keyMappings = None):
        self.width = width
        self.height = height
        self.gameOptions = gameOptions
        self.chooser = chooser
        self.pipeMenu = None
        print "x = ", x
        print "y = ", y
        DirectFrame.__init__(self, relief = None, image = loader.loadModel('models/misc/fade'), image_scale = (5, 2, 2), image_color = (0, 0, 0, 0.80000000000000004), image_pos = (0.5, 0, 0.80000000000000004), state = DGG.NORMAL, pos = (x, 0.0, y), sortOrder = 20)
        self.initialiseoptions(GameOptionsGui)
        self.setBin('gui-fixed', 10)
        self.setupUpperFrame()
        self.setupLowerFrame()
        self.setupInterfaceFrame()
        self.setupTutorialFrame()
        self.setupAudioFrame()
        self.setupDisplayFrame()
        self.setupGraphicsFrame()
        self.setupImageFrame()
        if self.gameOptions is not None:
            self.gameOptions.display_identifier = -1

        self.set_options(False)
        self.updateUI('graphics')
        self.updateUI()
        self.defaultDialog = None
        self.restoreDialog = None
        self.showedNoteOnChange = False


    def setupUpperFrame(self):
        gui_main = loader.loadModel('models/gui/gui_main')
        topImage = gui_main.find('**/game_options_panel/top')
        topImage.setPos(0.52000000000000002, 0, -0.14999999999999999)
        gui_main.remove_node()
        x = 0.29999999999999999
        self.upperFrame = DirectFrame(parent = self, relief = None, image = topImage, image_scale = 0.29999999999999999, pos = (x, 0, self.height - 0.26000000000000001 - PiratesGuiGlobals.TextScaleLarge * 7))
        self.upperFrame.setBin('gui-fixed', 15)
        DirectLabel(parent = self.upperFrame, relief = None, text = PLocalizer.GameOptionsTitle, text_align = TextNode.ACenter, text_scale = PiratesGuiGlobals.TextScaleTitleSmall, text_pos = (0.51000000000000001, 0.46500000000000002), text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_font = PiratesGlobals.getInterfaceOutlineFont(), textMayChange = 1)
        x -= 0.099000000000000005
        y = 1.3999999999999999
        self.displayButtonFrame = BorderFrame(parent = self, pos = (x, 0, y), frameSize = (-0.13, 0.13, -0.0625, 0.0625), showBackground = False, borderScale = 0.20000000000000001, modelName = 'general_frame_d')
        self.displayButton = DirectButton(parent = self.displayButtonFrame, text = PLocalizer.GameOptionsDisplay, text_scale = PiratesGuiGlobals.TextScaleLarge, text_fg = (1.0, 1.0, 1.0, 1.0), frameColor = (1.0, 0.0, 1.0, 0), frameSize = self.displayButtonFrame.getInnerFrameSize(), command = self.updateUI, text_pos = (0.019, -0.01), extraArgs = [
            'display'])
        self.displayButton.setBin('gui-fixed', 20)
        y -= 0.080000000000000002
        self.audioButtonFrame = BorderFrame(parent = self, pos = (x, 0, y), frameSize = (-0.13, 0.13, -0.0625, 0.0625), showBackground = False, borderScale = 0.20000000000000001, modelName = 'general_frame_d')
        self.audioButton = DirectButton(parent = self.audioButtonFrame, text = PLocalizer.GameOptionsAudio, text_scale = PiratesGuiGlobals.TextScaleLarge, text_fg = (1.0, 1.0, 1.0, 1.0), frameColor = (1.0, 0.0, 1.0, 0), frameSize = self.audioButtonFrame.getInnerFrameSize(), command = self.updateUI, text_pos = (0.019, -0.01), extraArgs = [
            'audio'])
        self.audioButtonFrame.setBin('gui-fixed', 10)
        y -= 0.080000000000000002
        self.interfaceButtonFrame = BorderFrame(parent = self, pos = (x, 0, y), frameSize = (-0.13, 0.13, -0.0625, 0.0625), showBackground = False, borderScale = 0.20000000000000001, modelName = 'general_frame_d')
        self.interfaceButton = DirectButton(parent = self.interfaceButtonFrame, text = PLocalizer.GameOptionsInterface, text_scale = PiratesGuiGlobals.TextScaleLarge, text_fg = (1.0, 1.0, 1.0, 1.0), frameColor = (1.0, 0.0, 1.0, 0), frameSize = self.interfaceButtonFrame.getInnerFrameSize(), command = self.updateUI, text_pos = (0.019, -0.01), extraArgs = [
            'interface'])
        self.interfaceButtonFrame.setBin('gui-fixed', 10)
        y -= 0.080000000000000002
        self.tutorialButtonFrame = BorderFrame(parent = self, pos = (x, 0, y), frameSize = (-0.13, 0.13, -0.0625, 0.0625), showBackground = False, borderScale = 0.20000000000000001, modelName = 'general_frame_d')
        self.tutorialButton = DirectButton(parent = self.tutorialButtonFrame, text = PLocalizer.GameOptionsTutorial, text_scale = PiratesGuiGlobals.TextScaleLarge, text_fg = (1.0, 1.0, 1.0, 1.0), frameColor = (1.0, 0.0, 1.0, 0), frameSize = self.tutorialButtonFrame.getInnerFrameSize(), command = self.updateUI, text_pos = (0.019, -0.01), extraArgs = [
            'notify'])
        self.tutorialButtonFrame.setBin('gui-fixed', 10)
        parent = self.upperFrame
        x = 0.290
        y = -0.153
        ox = 0.23
        text = PLocalizer.GameOptionsDefault
        self.defaultButton = GuiButton(parent = parent, text = text, pos = (x, 0, y), command = self.defaultButtonCB)
        x += ox
        text = PLocalizer.GameOptionsRestore
        self.restoreButton = GuiButton(parent = parent, text = text, pos = (x, 0, y), command = self.restoreButtonCB)
        x += ox
        text = PLocalizer.GameOptionsSave
        if self.gameOptions is not None:
            command = self.gameOptions.save_button_function
        else:
            command = None
        self.saveButton = GuiButton(parent = parent, text = text, pos = (x, 0, y), command = command)
        main_gui = loader.loadModel('models/gui/gui_main')
        generic_x = main_gui.find('**/x2')
        generic_box = main_gui.find('**/exit_button')
        generic_box_over = main_gui.find('**/exit_button_over')
        main_gui.remove_node()
        x = 1.216
        y = -0.383
        self.button = GuiButton(parent = parent, relief = None, pos = (x, 0, y), image = (generic_box, generic_box, generic_box_over, generic_box), image_scale = 0.40000000000000002, command = self.close)
        self.xButton = OnscreenImage(parent = self.button, image = generic_x, scale = 0.20000000000000001, pos = (-0.25600000000000001, 0, 0.76600000000000001))


    def setupDisplayFrame(self):
        self.displayFrame = DirectFrame(parent = self.upperFrame, relief = None)
        parent = self.displayFrame
        self.displayVar = [
            0]
        x = 0.20000000000000001
        y = 0.28000000000000003
        sx = 0.20000000000000001
        oy = 0.040000000000000001
        self.displayRadios = self.createRadioButtonGroup(parent, x, y, sx, oy, self.displayVar, 0.14999999999999999, [
            PLocalizer.GameOptionsLow,
            PLocalizer.GameOptionsMedium,
            PLocalizer.GameOptionsHigh,
            PLocalizer.GameOptionsCustom], 1.3999999999999999, self.displayRadioButtonCB)
        x = 0.16
        y -= oy * 3
        ox = 0.040000000000000001
        sy = -0.070000000000000007
        if base.appRunner is None or base.appRunner.windowProperties is None:
            y += sy
            self.windowChoices = [
                PLocalizer.GameOptionsWindowedMode,
                PLocalizer.GameOptionsFullscreenMode]
        else:
            base.appRunner.windowProperties.setFullscreen(0)
            self.windowChoices = [
                PLocalizer.GameOptionsWebEmbeddedMode,
                PLocalizer.GameOptionsWindowedMode,
                PLocalizer.GameOptionsFullscreenMode]
        if self.gameOptions.options.getEmbedded():
            self.windowVar = [
                PLocalizer.GameOptionsWebEmbeddedMode]
        elif self.gameOptions.options.getWindowed():
            self.windowVar = [
                PLocalizer.GameOptionsWindowedMode]
        else:
            self.windowVar = [
                PLocalizer.GameOptionsFullscreenMode]
        self.windowModeRadios = self.createRadioButtonGroupVertical(parent, x, y, ox, sy, self.windowVar, 0.12, self.windowChoices, 1.2, self.windowRadioButtonCB)
        if self.gameOptions and self.gameOptions.freeLock:
            subCard = loader.loadModel('models/gui/toplevel_gui')
            fullScreenRadioButton = self.windowModeRadios[-1]
            fullScreenRadioButton['state'] = DGG.DISABLED
            lockPos = fullScreenRadioButton.getPos()
            lockPos[0] -= 0.040000000000000001
            appendMe = DirectFrame(parent = self.displayFrame, relief = None, state = DGG.DISABLED, geom = subCard.find('**/pir_t_gui_gen_key_subscriber'), geom_scale = 0.20000000000000001, geom_pos = lockPos)
            appendMe.setAlphaScale(1.0, 2)
            subCard.remove_node()

        x += 0.29999999999999999
        oy = sy
        text = PLocalizer.GameOptionsEmbeddedRestriction
        self.restrictToEmbeddedMsg = self.create_label(x + 0.050000000000000003, y + oy * len(self.windowChoices), text, parent, 0.90000000000000002, text_align = TextNode.ACenter, color = (0.69999999999999996, 0.69999999999999996, 0.69999999999999996, 1))
        if base.appRunner is not None and base.appRunner.windowProperties is not None:
            y += oy

        text = PLocalizer.GameOptionsWindowedResolutions
        self.windowed_resolutions = []
        if hasattr(base, 'windowed_resolution_table'):
            resolution_table = base.windowed_resolution_table
        else:
            resolution_table = self.resolution_table
        for windowed_resolution in resolution_table:
            self.windowed_resolutions.append(windowed_resolution[0].__repr__() + 'x' + windowed_resolution[1].__repr__())


        def resolution_compare(x, y):
            xs = x.split('x')
            ys = y.split('x')
            if xs[0] == ys[0]:
                return int(xs[1]) - int(ys[1])
            else:
                return int(xs[0]) - int(ys[0])

        self.windowed_resolutions.sort(resolution_compare)
        self.windowedResolutionMenu = OptionMenu(parent = parent, scale = 0.050000000000000003, pos = (x + 0.20000000000000001, 0, y), items = self.windowed_resolutions, command = self.windowedResolutionMenuCB)
        y += oy
        text = PLocalizer.GameOptionsFullscreenResolutions
        fullscreen_resolutions = []
        if hasattr(base, 'fullscreen_resolution_table'):
            resolution_table = base.fullscreen_resolution_table
        else:
            resolution_table = self.resolution_table
        for fullscreen_resolution in resolution_table:
            fullscreen_resolutions.append(fullscreen_resolution[0].__repr__() + 'x' + fullscreen_resolution[1].__repr__())

        fullscreen_resolutions.sort(resolution_compare)
        self.fullscreenResolutionMenu = OptionMenu(parent = parent, scale = 0.050000000000000003, pos = (x + 0.20000000000000001, 0, y), items = fullscreen_resolutions, command = self.fullscreenResolutionMenuCB)
        y -= 2 * oy
        sl = 1.0
        sc = 0.34999999999999998
        enableDynamicPipeSwitching = 0
        if enableDynamicPipeSwitching:
            base.makeAllPipes()
            self.pipe_names = []
            for apipe in base.pipeList:
                self.pipe_names.append(apipe.getInterfaceName())

            self.pipeMenu = OptionMenu(parent = parent, scale = 0.050000000000000003, pos = (x + 0.20000000000000001, 0, y), items = self.pipe_names, command = self.pipeMenuCB)

        if base.config.GetBool('enable-stereo-display', 0):
            if base.appRunner is None or base.appRunner.windowProperties is None:
                x -= 0.40000000000000002

            text = PLocalizer.GameOptionsStereo
            self.create_label(x + 0.14999999999999999, y, text, parent, sl)
            self.stereoCheck = CheckButton(parent = parent, relief = None, scale = sc, pos = (x + 0.10000000000000001, 0, y + 0.014999999999999999), command = self.stereoCheckCB)



    def setupAudioFrame(self):
        self.audioFrame = DirectFrame(parent = self.upperFrame, relief = None)
        parent = self.audioFrame
        x = 0.10000000000000001
        y = 0.23000000000000001
        text = PLocalizer.GameOptionsSoundEffects
        self.create_label(x, y, text, parent, 1.2)
        x += 0.33500000000000002
        self.soundEffectCheck = CheckButton(parent = parent, relief = None, scale = 0.40000000000000002, pos = (x, 0, y + 0.014999999999999999), command = self.soundEffectCheckCB)
        x = 0.25
        y -= 0.050000000000000003
        text = PLocalizer.GameOptionsVolume
        self.create_label(x, y, text, parent)
        x += 0.42999999999999999

        def sound_volume_update_function(value):
            if self.gameOptions is not None:
                self.gameOptions.options.sound_volume = value

            if base.sfxManagerList:
                index = 0
                length = len(base.sfxManagerList)
                while index < length:
                    sfx_manager = base.sfxManagerList[index]
                    sfx_manager.setVolume(value)
                    index += 1


        text = PLocalizer.GameOptionsSoundEffectsVolume
        default_value = 0.5
        resolution = 0.01
        if self.gameOptions is not None:
            self.sound_volume_slider = self.create_slider(sound_volume_update_function, self.gameOptions.options.sound_volume, x, y, resolution, text, parent)
        else:
            self.sound_volume_slider = self.create_slider(sound_volume_update_function, default_value, x, y, resolution, text, parent)
        x = 0.10000000000000001
        y -= 0.10000000000000001
        text = PLocalizer.GameOptionsMusic
        self.create_label(x, y, text, parent, 1.2)
        x += 0.17999999999999999
        self.musicCheck = CheckButton(parent = parent, relief = None, scale = 0.40000000000000002, pos = (x, 0, y + 0.014999999999999999), command = self.musicCheckCB)
        x = 0.25
        y -= 0.050000000000000003
        text = PLocalizer.GameOptionsVolume
        self.create_label(x, y, text, parent)
        x += 0.42999999999999999

        def music_volume_update_function(value):
            if self.gameOptions is not None:
                self.gameOptions.options.music_volume = value

            if base.musicManager:
                base.musicManager.setVolume(value)


        text = PLocalizer.GameOptionsSoundEffectsVolume
        default_value = 0.5
        resolution = 0.01
        if self.gameOptions is not None:
            self.music_volume_slider = self.create_slider(music_volume_update_function, self.gameOptions.options.music_volume, x, y, resolution, text, parent)
        else:
            self.music_volume_slider = self.create_slider(music_volume_update_function, default_value, x, y, resolution, text, parent)


    def setupTutorialFrame(self):
        self.tutorialFrame = DirectFrame(parent = self.upperFrame, relief = None)
        parent = self.tutorialFrame
        x = 0.20000000000000001
        y = 0.29999999999999999
        text = PLocalizer.GameOptionsContextTutPanels
        self.create_label(x, y, text, parent, 1.5)
        y -= 0.10000000000000001
        self.basicCheck = CheckButton(parent = parent, relief = None, scale = 0.40000000000000002, pos = (x, 0, y + 0.014999999999999999), command = self.basicCheckCB)
        text = PLocalizer.GameOptionsBasic
        self.create_label(x + 0.050000000000000003, y, text, parent)
        y -= 0.10000000000000001
        self.intCheck = CheckButton(parent = parent, relief = None, scale = 0.40000000000000002, pos = (x, 0, y + 0.014999999999999999), command = self.intCheckCB)
        text = PLocalizer.GameOptionsIntermediate
        self.create_label(x + 0.050000000000000003, y, text, parent)
        y -= 0.10000000000000001
        self.advCheck = CheckButton(parent = parent, relief = None, scale = 0.40000000000000002, pos = (x, 0, y + 0.014999999999999999), command = self.advCheckCB)
        text = PLocalizer.GameOptionsAdvanced
        self.create_label(x + 0.050000000000000003, y, text, parent)


    def setupInterfaceFrame(self):
        self.interfaceFrame = DirectFrame(parent = self.upperFrame, relief = None)
        parent = self.interfaceFrame
        x = 0.10000000000000001
        y = 0.40000000000000002
        oy = -0.080000000000000002
        sl = 1.0
        sc = 0.34999999999999998
        ox = 0.59999999999999998
        y += oy
        text = PLocalizer.GameOptionsInvertMouseLook
        self.create_label(x, y, text, parent, sl)
        self.invertMouseCheck = CheckButton(parent = parent, relief = None, scale = sc, pos = (x + 0.35999999999999999, 0, y + 0.014999999999999999), command = self.invertMouseCheckCB)
        y += oy
        text = PLocalizer.GameOptionsGUIScale
        self.create_label(x, y, text, parent, sl)

        def gui_scale_update_function(value):
            if self.gameOptions is not None:
                self.gameOptions.options.gui_scale = value


            try:
                gui_manager = localAvatar.guiMgr
            except:
                gui_manager = None

            if gui_manager:
                gui_manager.setUIScale(value * 0.59999999999999998 + 0.69999999999999996)


        resolution = 0.01
        if self.gameOptions is not None:
            self.gui_scale_slider = self.create_slider(gui_scale_update_function, self.gameOptions.options.gui_scale, x + ox, y, resolution, text, parent)
        else:
            self.gui_scale_slider = self.create_slider(gui_scale_update_function, 1.0, x + ox, y, resolution, text, parent)
        y += oy
        text = PLocalizer.GameOptionsChatboxScale
        self.create_label(x, y, text, parent, sl)

        def chatbox_scale_update_function(value):
            if self.gameOptions is not None:
                self.gameOptions.options.chatbox_scale = value

            messenger.send('SetChatBoxWidth', [
                value])

        if self.gameOptions is not None:
            self.chatbox_scale_slider = self.create_slider(chatbox_scale_update_function, self.gameOptions.options.chatbox_scale, x + ox, y, resolution, text, parent)
        else:
            self.chatbox_scale_slider = self.create_slider(chatbox_scale_update_function, 1.0, x + ox, y, resolution, text, parent)
        y += oy
        text = PLocalizer.GameOptionsRotateCompassOnLand
        self.create_label(x, y, text, parent, sl)
        self.rotateCompassOnLandCheck = CheckButton(parent = parent, relief = None, scale = sc, pos = (x + 0.67500000000000004, 0, y + 0.014999999999999999), command = self.landMapRadarAxisCB)
        y += oy
        text = PLocalizer.GameOptionsRotateCompassAtSea
        self.create_label(x, y, text, parent, sl)
        self.rotateCompassAtSeaCheck = CheckButton(parent = parent, relief = None, scale = sc, pos = (x + 0.67500000000000004, 0, y + 0.014999999999999999), command = self.oceanMapRadarAxisCB)


    def setupLowerFrame(self):
        self.lowerFrame = DirectFrame(parent = self, relief = None, pos = (0.29999999999999999, 0, self.height - 0.91000000000000003 - PiratesGuiGlobals.TextScaleLarge * 17))
        gui_main = loader.loadModel('models/gui/gui_main')
        bottomImage = gui_main.find('**/game_options_panel/bottom')
        bottomImage.setPos(0.52000000000000002, 0, 0.90000000000000002)
        gui_main.remove_node()
        self.customFrame = DirectFrame(parent = self.lowerFrame, relief = None, image = bottomImage, image_scale = 0.29999999999999999, frameSize = (0, self.width, 0, PiratesGuiGlobals.TextScaleLarge * 22), pos = (0, 0, 0))
        self.customFrame.setBin('gui-fixed', 15)
        x = -0.099000000000000005
        y = 0.68999999999999995
        self.graphicsButtonFrame = BorderFrame(parent = self.lowerFrame, pos = (x, 0, y), frameSize = (-0.13, 0.13, -0.0625, 0.0625), showBackground = False, borderScale = 0.20000000000000001, modelName = 'general_frame_d')
        self.graphicsButton = DirectButton(parent = self.graphicsButtonFrame, text = PLocalizer.GameOptionsGraphics, text_scale = PiratesGuiGlobals.TextScaleLarge, text_fg = (1.0, 1.0, 1.0, 1.0), frameColor = (1.0, 0.0, 1.0, 0), frameSize = self.graphicsButtonFrame.getInnerFrameSize(), command = self.updateUI, text_pos = (0.019, -0.01), extraArgs = [
            'graphics'])
        self.graphicsButton.setBin('gui-fixed', 20)
        y -= 0.080000000000000002
        self.imageButtonFrame = BorderFrame(parent = self.lowerFrame, pos = (x, 0, y), frameSize = (-0.13, 0.13, -0.0625, 0.0625), showBackground = False, borderScale = 0.20000000000000001, modelName = 'general_frame_d')
        self.imageButton = DirectButton(parent = self.imageButtonFrame, text = PLocalizer.GameOptionsImage, text_scale = PiratesGuiGlobals.TextScaleLarge, text_fg = (1.0, 1.0, 1.0, 1.0), frameColor = (1.0, 0.0, 1.0, 0), frameSize = self.imageButtonFrame.getInnerFrameSize(), command = self.updateUI, text_pos = (0.019, -0.01), extraArgs = [
            'image'])
        self.imageButtonFrame.setBin('gui-fixed', 10)


    def setupGraphicsFrame(self):
        self.graphicsFrame = DirectFrame(parent = self.customFrame, relief = None)
        x = 0.070000000000000007
        y = 0.68999999999999995
        oy = -0.074999999999999997
        parent = self.graphicsFrame
        sl = 1
        sc = 0.34999999999999998
        text = PLocalizer.GameOptionsCharacterDetailLevel
        self.create_label(x, y, text, parent, sl)
        rx = 0.54000000000000004
        sx = 0.20000000000000001
        self.characterDetailVar = [
            0]
        self.characterDetailRadios = self.createRadioButtonGroup(parent, rx, y, sx, 0.029999999999999999, self.characterDetailVar, 0.14999999999999999, [
            PLocalizer.GameOptionsLow,
            PLocalizer.GameOptionsMedium,
            PLocalizer.GameOptionsHigh], 0.80000000000000004, self.characterDetailRadiosCB)
        y += oy
        text = PLocalizer.GameOptionsTerrainDetailLevel
        self.create_label(x, y, text, parent, sl)
        self.terrainDetailVar = [
            0]
        self.terrainDetailRadios = self.createRadioButtonGroup(parent, rx, y, sx, 0.029999999999999999, self.terrainDetailVar, 0.14999999999999999, [
            PLocalizer.GameOptionsLow,
            PLocalizer.GameOptionsMedium,
            PLocalizer.GameOptionsHigh], 0.80000000000000004, self.terrainDetailRadiosCB)
        y += oy
        text = PLocalizer.GameOptionsReflections
        self.create_label(x, y, text, parent, sl)
        self.reflectionsVar = [
            0]
        self.reflectionRadios = self.createRadioButtonGroup(parent, rx, y, sx, 0.029999999999999999, self.reflectionsVar, 0.14999999999999999, [
            PLocalizer.GameOptionsOff,
            PLocalizer.GameOptionsSkyOnly,
            PLocalizer.GameOptionsOn], 0.80000000000000004, self.reflectionRadiosCB)
        y += oy
        text = PLocalizer.GameOptionsSpecialEffectsLevel
        self.create_label(x, y, text, parent, sl)
        self.specialEffectsVar = [
            0]
        self.specialEffectsRadios = self.createRadioButtonGroup(parent, rx, y, sx, 0.029999999999999999, self.specialEffectsVar, 0.14999999999999999, [
            PLocalizer.GameOptionsLow,
            PLocalizer.GameOptionsMedium,
            PLocalizer.GameOptionsHigh], 0.80000000000000004, self.specialEffectsRadiosCB)
        y += oy
        text = PLocalizer.GameOptionsTextureDetailLevel
        self.create_label(x, y, text, parent, sl)
        self.textureDetailVar = [
            0]
        if self.gameOptions is not None and self.gameOptions.options.texture_scale_mode == False:
            sx = 0.13
            self.textureDetailRadios = self.createRadioButtonGroup(parent, rx, y, sx, 0.029999999999999999, self.textureDetailVar, 0.14999999999999999, [
                PLocalizer.GameOptionsLow,
                PLocalizer.GameOptionsMedium,
                PLocalizer.GameOptionsHigh,
                PLocalizer.GameOptionsMaximum], 0.80000000000000004, self.textureDetailRadiosCB)
        else:
            self.textureDetailRadios = self.createRadioButtonGroup(parent, rx, y, sx, 0.029999999999999999, self.textureDetailVar, 0.14999999999999999, [
                PLocalizer.GameOptionsLow,
                PLocalizer.GameOptionsMedium,
                PLocalizer.GameOptionsHigh], 0.80000000000000004, self.textureDetailRadiosCB)
        y += oy
        text = PLocalizer.GameOptionsTextureCompressed
        self.create_label(x, y, text, parent, sl)
        self.compressedTextureCheck = CheckButton(parent = parent, relief = None, scale = sc, pos = (x + 0.41999999999999998, 0, y + 0.014999999999999999), command = self.compressedTextureCheckCB)
        y += oy
        text = PLocalizer.GameOptionsAggressiveMemory
        self.create_label(x, y, text, parent, sl)
        self.aggressiveMemoryCheck = CheckButton(parent = parent, relief = None, scale = sc, pos = (x + 0.62, 0, y + 0.014999999999999999), command = self.aggressiveMemoryCheckCB)
        y += oy
        if self.gameOptions is not None and self.gameOptions.shader_support:
            text = PLocalizer.GameOptionsShaderLevel + ' ' + self.gameOptions.shader_model.__repr__() + ' *'
            self.create_label(x, y, text, parent, sl)
            self.shaderLevelCheck = CheckButton(parent = parent, relief = None, scale = sc, pos = (x + 0.315, 0, y + 0.014999999999999999), command = self.shaderLevelCheckCB)
        else:
            text = PLocalizer.GameOptionsNoShader
            self.create_label(x, y, text, parent, sl * 0.90000000000000002)
            self.shaderLevelCheck = None
        self.smoothEdgesCheck = None
        if base.win.getFbProperties().getMultisamples() > 1 and base.win.getPipe().getInterfaceName() == 'OpenGL':
            y += oy
            text = PLocalizer.GameOptionsSmoothEdges + ' *'
            self.create_label(x, y, text, parent, sl)
            self.smoothEdgesCheck = CheckButton(parent = parent, relief = None, scale = sc, pos = (x + 0.315, 0, y + 0.014999999999999999), command = self.smoothEdgesCheckCB)

        y += oy
        text = PLocalizer.GameOptionsRenderedShadows
        self.create_label(x, y, text, parent, sl)
        self.renderedShadowsCheck = CheckButton(parent = parent, relief = None, scale = sc, pos = (x + 0.38, 0, y + 0.014999999999999999), command = self.renderedShadowsCheckCB)
        text = PLocalizer.GameOptionsRestartRequired
        y += oy + 0.01
        self.create_label(x, y, text, parent, 0.90000000000000002, color = (0.69999999999999996, 0.69999999999999996, 0.69999999999999996, 1))


    def setupImageFrame(self):
        self.imageFrame = DirectFrame(parent = self.customFrame, relief = None)
        x = 0.070000000000000007
        y = 0.68999999999999995
        oy = -0.080000000000000002
        parent = self.imageFrame
        sl = 1.0
        sc = 0.34999999999999998
        ox = 0.59999999999999998
        y += oy
        text = PLocalizer.GameOptionsHardwareGamma
        self.create_label(x, y, text, parent, sl)
        self.hardwareGammaCheck = CheckButton(parent = parent, relief = None, scale = sc, pos = (x + 0.35999999999999999, 0, y + 0.014999999999999999), command = self.hardwareGammaCheckCB)
        y += oy * 0.80000000000000004
        text = PLocalizer.GameOptionsIntensity
        self.create_label(x + 0.20000000000000001, y, text, parent, sl * 0.80000000000000004)

        def gamma_update_function(value):
            if self.gameOptions is not None:
                self.gameOptions.options.gamma = value

            if base.win and base.win.getGsg():
                if self.gameOptions is not None and self.gameOptions.options.gamma_enable:
                    base.win.getGsg().setGamma(self.gameOptions.options.optionsGammaToGamma(self.gameOptions.options.gamma))



        resolution = 0.02
        if self.gameOptions is not None:
            self.gamma_slider = self.create_slider(gamma_update_function, self.gameOptions.options.gamma, x + ox, y, resolution, text, parent)
        else:
            self.gamma_slider = self.create_slider(gamma_update_function, 1.0, x + ox, y, resolution, text, parent)
        if self.gameOptions.enable_hdr:
            y += oy
            text = PLocalizer.GameOptionsHdr
            self.create_label(x, y, text, parent, sl)
            self.hdrCheck = CheckButton(parent = parent, relief = None, scale = sc, pos = (x + 0.80000000000000004, 0, y + 0.014999999999999999), command = self.hdrCheckCB)
            y += oy * 0.80000000000000004
            text = PLocalizer.GameOptionsIntensity
            self.create_label(x + 0.20000000000000001, y, text, parent, sl * 0.80000000000000004)

            def hdr_update_function(value):
                if self.gameOptions is not None:
                    self.gameOptions.options.hdr_factor = value

                if hasattr(base, 'hdr') and base.hdr:
                    if self.gameOptions is not None and self.gameOptions.options.hdr:
                        base.hdr.updateHdrFactor(value)



            resolution = 0.02
            if self.gameOptions is not None:
                self.hdr_factor_slider = self.create_slider(hdr_update_function, self.gameOptions.options.hdr_factor, x + ox, y, resolution, text, parent)
            else:
                self.hdr_factor_slider = self.create_slider(hdr_update_function, 1.0, x + ox, y, resolution, text, parent)
            text = PLocalizer.GameOptionsRestartRequired
            y += oy
            self.create_label(x, y, text, parent, 0.90000000000000002, color = (0.69999999999999996, 0.69999999999999996, 0.69999999999999996, 1))

        if base.config.GetBool('want-cpu-frequency-warning', 0):
            y += oy
            text = PLocalizer.GameOptionsCpuFrequencyWarning
            self.create_label(x, y, text, parent, sl)
            self.cpuFrequencyWarningCheck = CheckButton(parent = parent, relief = None, scale = sc, pos = (x + 0.45000000000000001, 0, y + 0.014999999999999999), command = self.cpuFrequencyWarningCheckCB)
        else:
            self.cpuFrequencyWarningCheck = None


    def createRadioButtonGroup(self, parent, x, y, sx, oy, variable, scale, labels, textScale, cmd = None):
        i = 0
        radioButtons = []
        for label in labels:
            radioButton = RadioButton(parent = parent, variable = variable, value = [
                i], scale = scale, relief = None, pos = (x + i * sx, 0, y), command = cmd)
            radioButtons.append(radioButton)
            i += 1

        for radio in radioButtons:
            radio.setOthers(radioButtons)

        y += oy
        i = 0
        for label in labels:
            self.create_label(x + i * sx, y, label, parent, textScale, TextNode.ACenter)
            i += 1

        return radioButtons


    def createRadioButtonGroupVertical(self, parent, x, y, ox, sy, variable, scale, labels, textScale, cmd = None):
        i = 0
        radioButtons = []
        for label in labels:
            radioButton = RadioButton(parent = parent, variable = variable, value = [
                label], scale = scale, relief = None, pos = (x, 0, y + i * sy - sy / 4), command = cmd)
            radioButtons.append(radioButton)
            i += 1

        for radio in radioButtons:
            radio.setOthers(radioButtons)

        x += ox
        i = 0
        for label in labels:
            self.create_label(x, y + i * sy, label, parent, textScale, TextNode.ALeft)
            i += 1

        return radioButtons


    def create_label(self, x, y, title, parent, scale = 1, text_align = TextNode.ALeft, color = PiratesGuiGlobals.TextFG1):
        label = DirectLabel(parent = parent, relief = None, text = title, text_align = text_align, text_scale = PiratesGuiGlobals.TextScaleLarge * scale, text_pos = (x, y), text_fg = color, text_shadow = PiratesGuiGlobals.TextShadow, text_font = PiratesGlobals.getInterfaceOutlineFont(), textMayChange = 1)
        return label


    def create_slider(self, update_function, default_value, x, y, resolution, label, parent):

        def update_slider(slider, update_function):
            update_function(slider['value'])

        charGui = loader.loadModel('models/gui/char_gui')
        slider = DirectSlider(parent = parent, relief = None, command = update_slider, image = charGui.find('**/chargui_slider_small'), image_scale = (2.1499999999999999, 2.1499999999999999, 1.5), thumb_relief = None, thumb_image = (charGui.find('**/chargui_slider_node'), charGui.find('**/chargui_slider_node_down'), charGui.find('**/chargui_slider_node_over')), pos = (x, 0.0, y + 0.01), text_align = TextNode.ACenter, text_scale = (0.10000000000000001, 0.10000000000000001), text_pos = (0.0, 0.10000000000000001), text_fg = PiratesGuiGlobals.TextFG1, scale = 0.28000000000000003, pageSize = resolution, text = None, value = default_value)
        charGui.remove_node()
        slider.label = label
        slider['extraArgs'] = [
            slider,
            update_function]
        return slider


    def updateUI(self, name = 'display'):
        if name == 'display':
            self.displayButtonFrame.setBin('gui-fixed', 20)
            self.audioButtonFrame.setBin('gui-fixed', 10)
            self.interfaceButtonFrame.setBin('gui-fixed', 10)
            self.tutorialButtonFrame.setBin('gui-fixed', 10)
            self.highlightButton(self.displayButton)
            self.fadeButton(self.audioButton)
            self.fadeButton(self.interfaceButton)
            self.fadeButton(self.tutorialButton)
            self.audioFrame.hide()
            self.interfaceFrame.hide()
            self.tutorialFrame.hide()
            self.displayFrame.show()
            if self.displayVar[0] == 3:
                self.lowerFrame.show()
            else:
                self.lowerFrame.hide()
        elif name == 'audio':
            self.displayButtonFrame.setBin('gui-fixed', 10)
            self.audioButtonFrame.setBin('gui-fixed', 20)
            self.interfaceButtonFrame.setBin('gui-fixed', 10)
            self.tutorialButtonFrame.setBin('gui-fixed', 10)
            self.highlightButton(self.audioButton)
            self.fadeButton(self.displayButton)
            self.fadeButton(self.interfaceButton)
            self.fadeButton(self.tutorialButton)
            self.audioFrame.show()
            self.interfaceFrame.hide()
            self.displayFrame.hide()
            self.tutorialFrame.hide()
            self.lowerFrame.hide()
        elif name == 'interface':
            self.displayButtonFrame.setBin('gui-fixed', 10)
            self.audioButtonFrame.setBin('gui-fixed', 10)
            self.interfaceButtonFrame.setBin('gui-fixed', 20)
            self.tutorialButtonFrame.setBin('gui-fixed', 10)
            self.highlightButton(self.interfaceButton)
            self.fadeButton(self.displayButton)
            self.fadeButton(self.audioButton)
            self.fadeButton(self.tutorialButton)
            self.interfaceFrame.show()
            self.tutorialFrame.hide()
            self.audioFrame.hide()
            self.displayFrame.hide()
            self.lowerFrame.hide()
        elif name == 'notify':
            self.displayButtonFrame.setBin('gui-fixed', 10)
            self.audioButtonFrame.setBin('gui-fixed', 10)
            self.interfaceButtonFrame.setBin('gui-fixed', 10)
            self.tutorialButtonFrame.setBin('gui-fixed', 20)
            self.highlightButton(self.tutorialButton)
            self.fadeButton(self.displayButton)
            self.fadeButton(self.audioButton)
            self.fadeButton(self.interfaceButton)
            self.tutorialFrame.show()
            self.interfaceFrame.hide()
            self.audioFrame.hide()
            self.displayFrame.hide()
            self.lowerFrame.hide()
        elif name == 'graphics':
            self.graphicsButtonFrame.setBin('gui-fixed', 20)
            self.imageButtonFrame.setBin('gui-fixed', 10)
            self.highlightButton(self.graphicsButton)
            self.fadeButton(self.imageButton)
            self.graphicsFrame.show()
            self.imageFrame.hide()
        elif name == 'image':
            self.graphicsButtonFrame.setBin('gui-fixed', 10)
            self.imageButtonFrame.setBin('gui-fixed', 20)
            self.highlightButton(self.imageButton)
            self.fadeButton(self.graphicsButton)
            self.graphicsFrame.hide()
            self.imageFrame.show()



    def disableButton(self, button):
        c = 0.5
        button['state'] = DGG.DISABLED
        button['text_fg'] = (c, c, c, 1.0)


    def fadeButton(self, button):
        if button:
            button['text_fg'] = (1.0, 1.0, 1.0, 1.0)



    def highlightButton(self, button):
        if button:
            button['text_fg'] = (0.20000000000000001, 0.80000000000000004, 0.59999999999999998, 1.0)



    def close(self):

        try:
            localAvatar.guiMgr.profilePage.createBuffer()
        except:
            pass

        if self.gameOptions is None:
            self.hide()
            return None

        self.gameOptions.hide()
        self.xButton.hide()
        self.button.hide()
        self.saveButton.hide()
        self.defaultButton.hide()
        self.restoreButton.hide()
        if self.chooser:
            base.cr.avChoice.avatarListFrame.show()
        base.setLowMemory(self.gameOptions.options.memory)
        if self.orig_texture_scale != self.gameOptions.options.texture_scale or self.orig_textureCompression != self.gameOptions.options.textureCompression:
            self.orig_texture_scale = self.gameOptions.options.texture_scale
            self.orig_textureCompression = self.gameOptions.options.textureCompression
            self.gameOptions.setTextureScale()
            ConfigVariableBool('compressed-textures').setValue(self.orig_textureCompression)
            gsg = base.win.getGsg()
            if gsg:
                gsg.getPreparedObjects().releaseAllTextures()
                messenger.send('texture_state_changed')




    def _GameOptionsGui__loadFeedbackPanel(self):
        FeedbackPanel = FeedbackPanel
        import pirates.piratesgui
        self.close()
        if self.gameOptions is not None:
            FeedbackPanel.FeedbackPanel()



    def initResolutionSettings(self):
        if self.gameOptions is None:
            return None

        if base.inAdFrame:
            self.fullscreenResolutionMenu.updateState(DGG.DISABLED)
            if len(self.windowed_resolutions) > 2:
                self.windowedResolutionMenu['items'] = self.windowed_resolutions[:2]
                self.windowedResolutionMenu.setItems()

            total_modes = embedded.getCountWindowModes()
            current_mode = embedded.getCurrentWindowModeDef()
            for button_index in xrange(total_modes):
                m = embedded.getAtWindowModeDef(button_index)
                if current_mode['want_size_x'] == m['want_size_x'] and current_mode['want_size_y'] == m['want_size_y']:
                    self.windowedResolutionMenu.set(button_index, False)
                    continue

        else:
            self.fullscreenResolutionMenu.updateState(DGG.NORMAL)
            self.windowedResolutionMenu['items'] = self.windowed_resolutions
            self.windowedResolutionMenu.setItems()
            self.windowedResolutionMenu.setByValue('%dx%d' % (self.gameOptions.options.window_width, self.gameOptions.options.window_height), False)
            self.fullscreenResolutionMenu.setByValue('%dx%d' % (self.gameOptions.options.fullscreen_width, self.gameOptions.options.fullscreen_height), False)
        self.displayRadios[self.gameOptions.options.simple_display_option].check()


    def update(self):
        if self.gameOptions is None:
            return None

        self.gameOptions.options.options_to_config()


    def set_options(self, change_display):
        if self.gameOptions is None:
            return None

        if change_display:
            self.gameOptions.set_display(self.gameOptions.options, base.pipe, self.gameOptions.options.getWidth(), self.gameOptions.options.getHeight())

        if base.config.GetBool('enable-stereo-display', 0):
            self.stereoCheck['value'] = self.gameOptions.options.use_stereo

        self.initResolutionSettings()
        if self.gameOptions.options.display.restrict_to_embedded:
            self.restrictToEmbeddedMsg.show()
        else:
            self.restrictToEmbeddedMsg.hide()
        winProps = base.win.getProperties()
        if self.gameOptions.options.getFullscreen():
            self.windowModeRadios[-1].check(False)
            self.fullscreenResolutionMenu.updateState(DGG.NORMAL)
            self.windowedResolutionMenu.updateState(DGG.DISABLED)
            self.restrictToEmbeddedMsg['text_fg'] = (1.0, 0.10000000000000001, 0.10000000000000001, 1)
        elif self.gameOptions.options.getEmbedded():
            self.windowModeRadios[-3].check(False)
            self.fullscreenResolutionMenu.updateState(DGG.DISABLED)
            self.windowedResolutionMenu.updateState(DGG.DISABLED)
            self.restrictToEmbeddedMsg['text_fg'] = (0.69999999999999996, 0.69999999999999996, 0.69999999999999996, 1)
        else:
            self.windowModeRadios[-2].check(False)
            self.fullscreenResolutionMenu.updateState(DGG.DISABLED)
            self.windowedResolutionMenu.updateState(DGG.NORMAL)
            self.restrictToEmbeddedMsg['text_fg'] = (1.0, 0.10000000000000001, 0.10000000000000001, 1)
        if self.pipeMenu is not None:
            self.pipeMenu.setByValue(base.pipe.getInterfaceName(), False)

        self.reflectionRadios[self.gameOptions.options.reflection].check()
        if self.shaderLevelCheck:
            self.shaderLevelCheck['value'] = self.gameOptions.options.shader

        if self.smoothEdgesCheck:
            self.smoothEdgesCheck['value'] = self.gameOptions.options.smoothEdges

        self.renderedShadowsCheck['value'] = self.gameOptions.options.shadow
        self.specialEffectsRadios[self.gameOptions.options.special_effects].check()
        if self.gameOptions.options.texture_scale_mode:
            if self.gameOptions.options.texture_scale in self.textureScaleOptionList:
                self.textureDetailRadios[self.textureScaleOptionList.index(self.gameOptions.options.texture_scale)].check()

            self.orig_texture_scale = self.gameOptions.options.texture_scale
        elif self.gameOptions.options.texture in self.textureOptionList:
            self.textureDetailRadios[self.textureOptionList.index(self.gameOptions.options.texture)].check()

        self.compressedTextureCheck.setQuiet(self.gameOptions.options.textureCompression)
        self.orig_textureCompression = self.gameOptions.options.textureCompression
        self.characterDetailRadios[self.gameOptions.options.character_detail_level].check()
        self.terrainDetailRadios[self.gameOptions.options.terrain_detail_level].check()
        self.aggressiveMemoryCheck['value'] = self.gameOptions.options.memory
        self.soundEffectCheck['value'] = self.gameOptions.options.sound
        self.sound_volume_slider['value'] = self.gameOptions.options.sound_volume
        self.musicCheck['value'] = self.gameOptions.options.music
        self.music_volume_slider['value'] = self.gameOptions.options.music_volume
        self.invertMouseCheck['value'] = self.gameOptions.options.mouse_look
        self.rotateCompassOnLandCheck['value'] = self.gameOptions.options.land_map_radar_axis
        self.rotateCompassAtSeaCheck['value'] = self.gameOptions.options.ocean_map_radar_axis
        self.gui_scale_slider['value'] = self.gameOptions.options.gui_scale
        if self.cpuFrequencyWarningCheck:
            self.cpuFrequencyWarningCheck['value'] = self.gameOptions.options.cpu_frequency_warning

        self.hardwareGammaCheck['value'] = self.gameOptions.options.gamma_enable
        self.gamma_slider['value'] = self.gameOptions.options.gamma
        if self.gameOptions.enable_hdr:
            self.hdrCheck['value'] = self.gameOptions.options.hdr

        self.update()


    def stereoCheckCB(self, val):
        if self.gameOptions is None:
            return None

        if val:
            self.gameOptions.display_stereoOption_dialog()

        self.gameOptions.options.use_stereo = val
        self.gameOptions.options.setRuntimeStereo()


    def landMapRadarAxisCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.options.land_map_radar_axis = val
        self.gameOptions.options.setLandMapRadarAxis()


    def oceanMapRadarAxisCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.options.ocean_map_radar_axis = val
        self.gameOptions.options.setOceanMapRadarAxis()


    def windowRadioButtonCB(self, var):
        if self.gameOptions is None:
            return None

        winProps = base.win.getProperties()
        if self.gameOptions.options.getFullscreen():
            currMode = PLocalizer.GameOptionsFullscreenMode
        elif self.gameOptions.options.getEmbedded():
            currMode = PLocalizer.GameOptionsWebEmbeddedMode
        else:
            currMode = PLocalizer.GameOptionsWindowedMode
        if self.windowVar[0] == currMode:
            return None

        if self.windowVar[0] == PLocalizer.GameOptionsWebEmbeddedMode:
            self.gameOptions.options.fullscreen = 0
            self.gameOptions.options.fullscreen_runtime = 0
            self.gameOptions.options.embedded = 1
            self.gameOptions.options.embedded_runtime = 1
            self.gameOptions.set_display(self.gameOptions.options, base.pipe, self.gameOptions.options.window_width, self.gameOptions.options.window_height)
        elif self.windowVar[0] == PLocalizer.GameOptionsWindowedMode:
            self.gameOptions.options.fullscreen = 0
            self.gameOptions.options.fullscreen_runtime = 0
            self.gameOptions.options.embedded = 0
            self.gameOptions.options.embedded_runtime = 0
            self.gameOptions.set_display(self.gameOptions.options, base.pipe, self.gameOptions.options.window_width, self.gameOptions.options.window_height)
        elif self.windowVar[0] == PLocalizer.GameOptionsFullscreenMode:
            self.gameOptions.options.fullscreen = 1
            self.gameOptions.options.fullscreen_runtime = 1
            self.gameOptions.options.embedded = 0
            self.gameOptions.options.embedded_runtime = 0
            self.gameOptions.set_display(self.gameOptions.options, base.pipe, self.gameOptions.options.fullscreen_width, self.gameOptions.options.fullscreen_height)

        self.set_options(False)


    def windowedResolutionMenuCB(self, val, idx):
        if self.gameOptions is None:
            return None

        index = base.windowed_resolution_table.index((int(val.split('x')[0]), int(val.split('x')[1])))
        if base.inAdFrame:
            self.gameOptions.display_identifier = index
            self.gameOptions.set_display(self.gameOptions.options, base.pipe, base.windowed_resolution_table[index][0], base.windowed_resolution_table[index][1])
            if base.hasEmbedded:
                self.gameOptions.options.resolution = index

        elif self.gameOptions.options.getWindowed():
            self.gameOptions.set_display(self.gameOptions.options, base.pipe, base.windowed_resolution_table[index][0], base.windowed_resolution_table[index][1])

        self.gameOptions.options.window_width = base.windowed_resolution_table[index][0]
        self.gameOptions.options.window_height = base.windowed_resolution_table[index][1]
        if self.gameOptions.options.window_width > self.gameOptions.current_options.window_width and self.gameOptions.options.window_height > self.gameOptions.current_options.window_height:
            self.showNoteOnChange()



    def showNoteOnChange(self):
        if not self.showedNoteOnChange:
            self.gameOptions.display_noteOnChange_dialog()
            self.showedNoteOnChange = True



    def fullscreenResolutionMenuCB(self, val, index):
        if self.gameOptions is None:
            return None

        newX = int(val.split('x')[0])
        newY = int(val.split('x')[1])
        if base.inAdFrame:
            pass
        1
        if self.gameOptions.options.getFullscreen():
            self.gameOptions.set_display(self.gameOptions.options, base.pipe, newX, newY)

        self.gameOptions.options.fullscreen_width = newX
        self.gameOptions.options.fullscreen_height = newY
        if self.gameOptions.options.fullscreen_width > self.gameOptions.current_options.fullscreen_width and self.gameOptions.options.fullscreen_height > self.gameOptions.current_options.fullscreen_height:
            self.showNoteOnChange()



    def pipeMenuCB(self, val, index):
        if self.gameOptions is None:
            return None

        if base.pipeList[index].isValid():
            newX = base.win.getProperties().getXSize()
            newY = base.win.getProperties().getYSize()
            self.gameOptions.set_display(self.gameOptions.options, base.pipeList[index], newX, newY)

        self.update()


    def shaderLevelCheckCB(self, val):
        if self.gameOptions is None:
            return None

        if self.gameOptions.options.shader != val:
            self.gameOptions.display_restart_dialog()

        self.gameOptions.options.shader = val


    def smoothEdgesCheckCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.options.smoothEdges = val
        if self.gameOptions.options.smoothEdges != val:
            self.gameOptions.display_restart_dialog()



    def renderedShadowsCheckCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.options.shadow = val

        try:
            time_of_day_manager = base.cr.timeOfDayManager
        except:
            time_of_day_manager = None

        if time_of_day_manager:
            if val:
                time_of_day_manager.enableAvatarShadows()
            else:
                time_of_day_manager.disableAvatarShadows()



    def reflectionRadiosCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.options.reflection = val[0]
        funcList = [
            Water.all_reflections_off,
            Water.all_reflections_show_through_only,
            Water.all_reflections_on]
        funcList[val[0]]()
        self.update()
        if self.gameOptions.options.reflection > self.gameOptions.current_options.reflection:
            self.showNoteOnChange()



    def specialEffectsRadiosCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.options.special_effects = val[0]
        self.gameOptions.options.setRuntimeSpecialEffects()
        if self.gameOptions.options.special_effects > self.gameOptions.current_options.special_effects:
            self.showNoteOnChange()



    def textureDetailRadiosCB(self, val):
        if self.gameOptions is None:
            return None

        if self.gameOptions.options.texture_scale_mode:
            self.gameOptions.options.texture_scale = self.textureScaleOptionList[val[0]]
            if self.gameOptions.options.texture_scale > self.gameOptions.current_options.texture_scale:
                self.showNoteOnChange()

        else:
            self.gameOptions.options.texture = self.textureOptionList[val]


    def compressedTextureCheckCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.options.textureCompression = val


    def characterDetailRadiosCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.options.character_detail_level = val[0]
        self.gameOptions.options.setRuntimeAvatarDetailLevel(val[0])
        if self.gameOptions.options.character_detail_level > self.gameOptions.current_options.character_detail_level:
            self.showNoteOnChange()



    def terrainDetailRadiosCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.options.terrain_detail_level = val[0]
        self.gameOptions.options.setRuntimeGridDetailLevel(val[0])
        if self.gameOptions.options.terrain_detail_level > self.gameOptions.current_options.terrain_detail_level:
            self.showNoteOnChange()



    def aggressiveMemoryCheckCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.options.memory = val


    def soundEffectCheckCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.options.sound = val
        base.enableSoundEffects(val)
        self.update()


    def musicCheckCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.options.music = val
        base.enableMusic(val)
        if val and base.musicMgr.current:
            volume = base.musicMgr.current.volume
            base.musicMgr.requestCurMusicFadeIn(1.0, volume)

        self.update()


    def invertMouseCheckCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.options.mouse_look = val
        self.update()


    def cpuFrequencyWarningCheckCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.options.cpu_frequency_warning = val
        self.update()


    def hardwareGammaCheckCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.options.gamma_enable = val
        if base.win and base.win.getGsg():
            if self.gameOptions.options.gamma_enable:
                base.win.getGsg().setGamma(self.gameOptions.options.optionsGammaToGamma(self.gameOptions.options.gamma))
            else:
                base.win.getGsg().restoreGamma()

        self.update()


    def hdrCheckCB(self, val):
        if self.gameOptions is None:
            return None

        if self.gameOptions.options.hdr != val:
            self.gameOptions.display_restart_dialog()

        self.gameOptions.options.hdr = val
        self.update()


    def defaultButtonCB(self):
        if self.gameOptions is None:
            return None

        if self.defaultDialog:
            self.defaultDialog.destroy()

        self.defaultDialog = PDialog.PDialog(parent = self, text = PLocalizer.GameOptionsDefaultConfirm, style = OTPDialog.YesNo, giveMouse = False, command = self.defaultDialogCB)
        self.defaultDialog.setPos(0.80000000000000004, 0, 1.0)
        self.defaultDialog.setBin('gui-fixed', 20, 20)


    def defaultDialogCB(self, val):
        self.defaultDialog.destroy()
        del self.defaultDialog
        self.defaultDialog = None
        if val == 1:
            self.gameOptions.default_button_function()
            self.displayRadios[self.gameOptions.options.simple_display_option].check()



    def restoreButtonCB(self):
        if self.gameOptions is None:
            return None

        if self.restoreDialog:
            self.restoreDialog.destroy()

        self.restoreDialog = PDialog.PDialog(parent = self, text = PLocalizer.GameOptionsRestoreConfirm, style = OTPDialog.YesNo, giveMouse = False, command = self.restoreDialogCB)
        self.restoreDialog.setPos(0.80000000000000004, 0, 1.0)
        self.restoreDialog.setBin('gui-fixed', 20, 20)


    def restoreDialogCB(self, val):
        self.restoreDialog.destroy()
        del self.restoreDialog
        self.restoreDialog = None
        if val == 1:
            self.gameOptions.restore_button_function()
            self.displayRadios[self.gameOptions.options.simple_display_option].check()



    def displayRadioButtonCB(self, val):
        self.updateUI()
        if self.gameOptions is None:
            return None


        def handleAggressiveMemoryCheck():
            block_size = 1024 * 1024 * 256
            physical_memory = self.gameOptions.options.getPhysicalMemory(base.pipe)
            if physical_memory > 0:
                blocks = (physical_memory + block_size / 2) / block_size
                if blocks <= 2:
                    self.aggressiveMemoryCheck['value'] = True
                    self.compressedTextureCheck['value'] = True
                else:
                    self.aggressiveMemoryCheck['value'] = False
            else:
                self.aggressiveMemoryCheck['value'] = False

        self.gameOptions.options.simple_display_option = self.displayVar[0]
        if self.displayVar[0] == 0:
            self.characterDetailRadios[0].check()
            self.terrainDetailRadios[0].check()
            self.reflectionRadios[0].check()
            self.specialEffectsRadios[0].check()
            self.textureDetailRadios[0].check()
            if self.shaderLevelCheck:
                self.shaderLevelCheck['value'] = False

            self.renderedShadowsCheck['value'] = False
            handleAggressiveMemoryCheck()
        elif self.displayVar[0] == 1:
            self.characterDetailRadios[1].check()
            self.terrainDetailRadios[1].check()
            self.reflectionRadios[1].check()
            self.specialEffectsRadios[1].check()
            self.textureDetailRadios[1].check()
            if self.shaderLevelCheck:
                self.shaderLevelCheck['value'] = False

            self.renderedShadowsCheck['value'] = False
            handleAggressiveMemoryCheck()
        elif self.displayVar[0] == 2:
            self.characterDetailRadios[2].check()
            self.terrainDetailRadios[2].check()
            self.reflectionRadios[2].check()
            self.specialEffectsRadios[2].check()
            self.textureDetailRadios[2].check()
            if self.shaderLevelCheck:
                self.shaderLevelCheck['value'] = True

            self.renderedShadowsCheck['value'] = True
            handleAggressiveMemoryCheck()

        if self.gameOptions.options.simple_display_option != 3 and self.gameOptions.options.simple_display_option > self.gameOptions.current_options.simple_display_option:
            self.showNoteOnChange()



    def basicCheckCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.tutPanelOptions[0] = val


    def intCheckCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.tutPanelOptions[1] = val


    def advCheckCB(self, val):
        if self.gameOptions is None:
            return None

        self.gameOptions.tutPanelOptions[2] = val


    def setTutPanelOptions(self):
        if self.gameOptions is None:
            return None

        self.basicCheck['value'] = self.gameOptions.tutPanelOptions[0]
        self.intCheck['value'] = self.gameOptions.tutPanelOptions[1]
        self.advCheck['value'] = self.gameOptions.tutPanelOptions[2]
