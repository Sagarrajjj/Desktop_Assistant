# https://www.google.com/search?q=weather+of+patna&oq=weather++of+patna&gs_lcrp=EgZjaHJvbWUqDAgAEAAYRhiAAhiABDIMCAAQABhGGIACGIAEMgcIARAAGIAEMgcIAhAAGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgcIBxAAGIAEMgcICBAAGIAEMgcICRAAGIAE0gEINzc5M2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36
# span id = wob_tm
from requests_html import HTMLSession

import speech_to_text


def weather():
    s = HTMLSession()
    query = "Koramangala"  # Changed the query to Koramangala
    url =f'https://www.google.com/search?q=weather+({query})'
    r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'})
    try:
        temp = r.html.find('#wob_tm', first= True).text
        unit = r.html.find('.vk_bk.wob-unit span[aria-label="°Celsius"]', first= True).text
        desc = r.html.find('#wob_dc', first= True).text
        return temp + "" + unit + "" + desc
    except AttributeError:
        return "Could not retrieve weather information for Koramangala at the moment."
