import os
import platform
import subprocess

try:
    from gtts import gTTS
except ImportError:
    print('gTTS kütüphanesi bulunamadı. Lütfen `pip install gtts` yapın.')
    raise

LANGUAGE_MAP = {
    'turkish': 'tr',
    'turkçe': 'tr',
    'turkce': 'tr',
    'ingilizce': 'en',
    'english': 'en',
    'almanca': 'de',
    'german': 'de',
    'fransızca': 'fr',
    'fransizca': 'fr',
    'french': 'fr',
    'ispanyolca': 'es',
    'spanish': 'es',
    'italyanca': 'it',
    'italian': 'it',
    'japonca': 'ja',
    'japanese': 'ja',
    'korece': 'ko',
    'korean': 'ko',
    'portekizce': 'pt',
    'portuguese': 'pt',
    'rusça': 'ru',
    'rusca': 'ru',
    'russian': 'ru',
    'arapça': 'ar',
    'arapca': 'ar',
    'arabic': 'ar',
    'hindi': 'hi',
    'hintçe': 'hi',
    'hindikçe': 'hi',
    'hindu': 'hi',
    'çince': 'zh-cn',
    'cince': 'zh-cn',
    'chinese': 'zh-cn',
    'ukrainian': 'uk',
    'ukraynaca': 'uk',
    'katalanca': 'ca',
    'catalan': 'ca',
    'svenska': 'sv',
    'swedish': 'sv',
    'dutch': 'nl',
    'hollandaca': 'nl',
}

CHARACTERS = [
    {
        'name': 'Yelda',
        'description': 'Türkçe macOS sesi (Yelda).',
        'type': 'system',
        'voice': 'Yelda',
        'supported_langs': ['tr'],
    },
    {
        'name': 'Fred',
        'description': 'İngilizce macOS sesi (Fred).',
        'type': 'system',
        'voice': 'Fred',
        'supported_langs': ['en'],
    },
    {
        'name': 'Flo',
        'description': 'Genel macOS sesi (Flo). Yabancı diller için Google TTS önerilir.',
        'type': 'system',
        'voice': 'Flo',
        'supported_langs': ['en'],
    },
    {
        'name': 'Google',
        'description': 'Gerçek Google Translate benzeri telaffuz için gTTS.',
        'type': 'gtts',
        'voice': None,
        'supported_langs': None,
    },
    {
        'name': 'Custom',
        'description': 'Özel karakter seçimi: aynı anda tüm diller için Google TTS kullanır.',
        'type': 'gtts',
        'voice': None,
        'supported_langs': None,
    },
]


def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def normalize_language(user_input):
    value = user_input.strip().lower()
    if not value:
        return None

    if value in LANGUAGE_MAP:
        return LANGUAGE_MAP[value]

    normalized = value.replace('_', '-').replace(' ', '-').lower()
    if len(normalized) == 2 or normalized in ('zh-cn', 'zh-tw', 'pt-br', 'pt-pt', 'en-gb', 'en-us'):
        return normalized

    return None


def select_character():
    print('Karakter seçin:')
    for index, character in enumerate(CHARACTERS, start=1):
        print(f"{index}. {character['name']} - {character['description']}")

    while True:
        choice = input('Karakter numarası veya adı: ').strip()
        if not choice:
            continue

        for character in CHARACTERS:
            if choice.lower() == character['name'].lower() or choice == str(CHARACTERS.index(character) + 1):
                return character

        print('Geçersiz seçim. Lütfen listedeki bir karakter numarası veya adını girin.')


def select_language():
    print('\nDil seçin (örnekler: Türkçe, English, Español, de, ru, ja, ko):')
    while True:
        user_input = input('Dil: ').strip()
        lang_code = normalize_language(user_input)
        if lang_code:
            return lang_code
        print('Geçersiz dil. Lütfen geçerli bir dil adı veya kodu girin.')


def play_text_with_system_voice(text, voice_name):
    if platform.system() == 'Darwin':
        subprocess.run(['say', '-v', voice_name, text], check=False)
        return True
    return False


def play_text_with_gtts(text, lang_code, output_file='tts_output.mp3'):
    tts = gTTS(text=text, lang=lang_code)
    tts.save(output_file)

    if platform.system() == 'Darwin':
        subprocess.run(['afplay', output_file], check=False)
    elif platform.system() == 'Windows':
        subprocess.run(['powershell', '-c', f"(New-Object Media.SoundPlayer '{output_file}').PlaySync();"], check=False)
    else:
        subprocess.run(['mpg123', output_file], check=False)

    print(f'Çıktı kaydedildi: {output_file}')


def main():
    clear_screen()
    print('=== Çok Dilli Telaffuz Aracı ===\n')
    character = select_character()

    print(f"\nSeçilen karakter: {character['name']} ({character['description']})")
    language_code = select_language()

    print(f"Seçilen dil kodu: {language_code}\n")
    text = input('Ne dememi istersiniz? ').strip()
    if not text:
        print('Metin boş olamaz. Lütfen tekrar deneyin.')
        return

    use_gtts = True
    if character['type'] == 'system':
        if character['supported_langs'] and language_code.split('-')[0] in character['supported_langs']:
            use_gtts = False
        else:
            print('\nSeçilen karakter bu dili doğrudan desteklemiyor. Google TTS ile gerçek telaffuz kullanılıyor.')

    if use_gtts:
        print('\nGoogle TTS ile oynatılıyor...')
        play_text_with_gtts(text, language_code)
    else:
        print('\nSistem sesi ile oynatılıyor...')
        if not play_text_with_system_voice(text, character['voice']):
            print('Sistem sesi oynatılamadı, Google TTS ile kullanılacak.')
            play_text_with_gtts(text, language_code)

    print('\nTamamlandı.')


if __name__ == '__main__':
    main()
