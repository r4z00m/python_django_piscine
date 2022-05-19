import sys
import dewiki
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit()
    url = 'https://en.wikipedia.org/w/api.php'

    params = {
        'action': 'parse',
        'page': sys.argv[1],
        'redirects': True,
        'prop': 'wikitext',
        'format': 'json',
    }

    try:
        r = requests.get(url, params=params)
        if not r.ok:
            print('request error')
            sys.exit()
        res = r.json()
        s = dewiki.from_string(res['parse']['wikitext']['*'])
        with open(f"{sys.argv[1]}.wiki", "w") as out_file:
            out_file.write(s)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
