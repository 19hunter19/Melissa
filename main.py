import sys
import yaml
import speech_recognition as sr
from GreyMatter.SenseCells.tts import tts

##profile = open('profile.yaml')
##profile_data = yaml.safe_load(profile)
##profile.close()

name = 'Dave'
city_name = 'Dallas, TX'


tts('Welcome, ' + name + '. All systems are go. How can I help you?')


def main():

    # GET INPUT
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # PRODUCE OUTPUT
    try:
        speech_text = r.recognize_google(audio).lower().replace("'", "")
        tts('You said, ' + speech_text)

    except sr.UnknownValueError:
        print('Audio not understood')

    except sr.RequestError as e:
        print('Could not request results from GSR service; {0}'.format(e))


##
## R U N   M A I N
##

main()


