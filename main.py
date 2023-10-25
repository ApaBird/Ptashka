from vosk import Model, KaldiRecognizer  # оффлайн-распознавание от Vosk
import pyaudio
import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)
import wave  # создание и чтение аудиофайлов формата wav
import json  # работа с json-файлами и json-строками
import os  # работа с файловой системой


class Ptashka:

    def __init__(self):
        model = Model('vosk-small-ru')
        self.rec = KaldiRecognizer(model, 16000)
        p = pyaudio.PyAudio()
        self.stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        self.stream.start_stream()
        self.check_commands()

    def listen(self):
        while True:
            data = self.stream.read(4000, exception_on_overflow=False)
            if self.rec.AcceptWaveform(data) and len(data) > 0:
                answer = json.loads(self.rec.Result())
                if answer['text']:
                    yield answer['text']

    def check_commands(self):
        folders = [f for f in os.listdir("Module")]
        print(folders)


    def start(self):
        for i in self.listen():
            if i == 'пока':
                quit()
            else:
                print(i)


bird = Ptashka()
bird.start()
