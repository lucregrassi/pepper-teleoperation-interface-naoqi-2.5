# -*- encoding: UTF-8 -*-
import sys
import argparse
import qi

script_filename = "sentences.txt"


def main(session):
    al = session.service("ALAutonomousLife")
    # Disable autonomous life before starting so that ALDialog does not interfere
    # al.setState("interactive")
    al.setAutonomousAbilityEnabled("BasicAwareness", True)
    al.setAutonomousAbilityEnabled("AutonomousBlinking", True)
    al.setAutonomousAbilityEnabled("BackgroundMovement", True)
    al.setAutonomousAbilityEnabled("ListeningMovement", False)
    al.setAutonomousAbilityEnabled("SpeakingMovement", False)

    audio_device = session.service("ALAudioDevice")
    audio_device.setOutputVolume(60)

    motion_service = session.service("ALMotion")
    motion_service.wakeUp()
    motion_service.setMoveArmsEnabled(True, True)
    motion_service.setOrthogonalSecurityDistance(0.05)
    motion_service.setTangentialSecurityDistance(0.05)
    behavior = session.service("ALBehaviorManager")

    tts = session.service("ALTextToSpeech")
    animated_speech = session.service("ALAnimatedSpeech")
    configuration = {"bodyLanguageMode": "contextual"}

    # posture_service = session.service("ALRobotPosture")
    # posture_service.goToPosture("StandInit", 0.5)
    try:
        DEF_IMG_APP = "tablet_images"
        TABLET_IMG_DEFAULT = "RICE.png"
        sTablet = session.service("ALTabletService")
        image_dir = "http://%s/apps/%s/img/" % (sTablet.robotIp(), DEF_IMG_APP)
        tablet_image = image_dir + TABLET_IMG_DEFAULT
        sTablet.showImage(tablet_image)
    except RuntimeError:
        pass

    factor = 1
    voice_speed = "\\rspd=90\\"

    with open(script_filename, 'r') as f1:
        script_sentences = f1.readlines()
    with open("pepper_sentences_it.txt", 'r') as f2:
        pepper_sentences_it = f2.readlines()
    with open("pepper_sentences_en.txt", 'r') as f3:
        pepper_sentences_en = f3.readlines()

    chosen_language = str(raw_input("Choose a language:\n1: Italian\n2: English\n"))
    if chosen_language == '1':
        pepper_sentences = pepper_sentences_it
        tts.setLanguage("Italian")
        msg = "Premi un tasto per iniziare:\n"
    else:
        pepper_sentences = pepper_sentences_en
        tts.setLanguage("English")
        msg = "Press a key to start:\n"

    i = 0
    X = 0.0
    Y = 0.0
    Theta = 0.0

    while True:
        key = str(raw_input(msg))
        if key == "":
            if i < len(script_sentences):
                animated_speech.say(voice_speed + script_sentences[i], configuration)
                i = i+1
            else:
                print("The copycat is over!")

        elif key == 'w':
            X = 0.2  # forward
            Y = 0.0
            Theta = 0.0

        elif key == "a":
            X = 0.0
            Y = 0.0
            Theta = 0.2

        elif key == "x":
            X = -0.2
            Y = 0.0
            Theta = 0.0

        elif key == "d":
            X = 0.0
            Y = 0.0
            Theta = -0.2

        elif key == "s":
            X = 0.0
            Y = 0.0
            Theta = 0.0

        elif key == "e":
            factor = factor + 1

        elif key == "c":
            factor = factor - 1

        elif key == "n":
            animated_speech.say("^start(caresses/namaste) Namastee \\pau=3000\\")

        elif key == "h":
            animated_speech.say("^start(caresses/greetingsuk_silent) Ciao \\pau=3000\\")

        elif key == "k":
            animated_speech.say("^start(caresses/leanforwardbowing) Konniciwa \\pau=3000\\")

        elif key == "1":
            animated_speech.say(voice_speed + script_sentences[0], configuration)

        elif key == "2":
            behavior.startBehavior("affectivecommunication/hug")
        elif key == "3":
            behavior.startBehavior("affectivecommunication/handshake")
            #animated_speech.say(voice_speed + script_sentences[2], configuration)

        elif key == "4":
            animated_speech.say(voice_speed + script_sentences[3], configuration)

        elif key == "5":
            animated_speech.say(voice_speed + script_sentences[4], configuration)

        elif key == "6":
            animated_speech.say(voice_speed + script_sentences[5], configuration)

        elif key == "7":
            animated_speech.say(voice_speed + script_sentences[6], configuration)

        elif key == "8":
            animated_speech.say(voice_speed + script_sentences[7], configuration)

        elif key == "9":
            animated_speech.say(voice_speed + script_sentences[8], configuration)

        elif key == "10":
            animated_speech.say(voice_speed + script_sentences[9], configuration)

        elif key == "11":
            animated_speech.say(voice_speed + script_sentences[10], configuration)

        elif key == "12":
            animated_speech.say(voice_speed + script_sentences[11], configuration)

        elif key == "13":
            animated_speech.say(voice_speed + script_sentences[12], configuration)

        elif key == "14":
            animated_speech.say(voice_speed + script_sentences[13], configuration)

        elif key == "15":
            animated_speech.say(voice_speed + script_sentences[14], configuration)

        elif key == "16":
            animated_speech.say(voice_speed + script_sentences[15], configuration)

        elif key == "17":
            animated_speech.say(voice_speed + script_sentences[16], configuration)

        elif key == "18":
            animated_speech.say(voice_speed + script_sentences[17], configuration)

        elif key == "19":
            animated_speech.say(voice_speed + script_sentences[18], configuration)

        else:
            animated_speech.say(key)
        print("Factor: ", factor)

        try:
            motion_service.moveToward(X * factor, Y * factor, Theta * factor)

        except Exception, errorMsg:
            print str(errorMsg)
            print "This example is not allowed on this robot."
            exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default='127.0.0.1',
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    qi_session = qi.Session()
    print("Waiting for the robot to connect...")
    try:
        qi_session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) + ".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(qi_session)
