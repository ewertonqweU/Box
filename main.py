import speech_recognition as sr

# criar reconhecedor
r = sr.Recognizer()

# abrir mic para captura
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('Pode falar que eu vou gravar')
    while True:
        audio = r.listen(source)
        try:
            print(r.recognize_google(audio, language="pt-BR"))
        except:
            print('desculpe nao entendi')
