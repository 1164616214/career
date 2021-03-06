base_url = r'https://kyfw.12306.cn/otn/leftTicket/queryZ'
p1 = r'?leftTicketDTO.train_date=2019-01-31'
p2 = r'&leftTicketDTO.from_station=SHH'
p3 = r'&leftTicketDTO.to_station=OMH'
p4 = r'&purpose_codes=ADULT'
resp = r'''
{
    "data": {
        "flag": "1", 
        "map": {
            "AOH": "上海虹桥", 
            "MAH": "马鞍山", 
            "OMH": "马鞍山东", 
            "SHH": "上海"
        }, 
        "result": [
            "%2BCSaM1dfrms9%2BD2Uhfp1jet54ofQaADOLyyuYeUNcwoCW8wexX1nM8Mvvj%2B9a5IBFKQyWUj9eJGh%0Aj5wGpxzmvgjeytW2v11XNq%2BNT6ag49Fj69A2LW%2F1UPL08Qkcp2H9tMMQLjERmyr47nDogNqWcQ4z%0A7bJ81Y4x45s4gTlY67zlvlQoc34fxw3YVfz0ZPmOZ%2BsiXp4EPjuRToEYq8pH75P83uVAanyorRSk%0ASUKSkJ2o4XqfQ2EVNC9oFpjvT3cibAUMIj5gFvJKLFoj2R%2BgMwXEhkbVv5%2BPVGxvYlJ4yt8aj4t9%0A6xU8N5ySG4s%3D|预订|55000G937200|G9372|SHH|AQH|SHH|OMH|01:49|03:51|02:02|Y|VrOxdUn4ugdoau%2BlGHKQxSc75qu0cychMFWsB4AffJxTniIyDDwtSNNE4XA%3D|20190131|3|H1|01|05|1|0|||||||有||||2|3|8||O090M0O0|O9MO|0|0|null", 
            "P4HeBacOzqTkldXGrqIxaZYcSI0ApiFD%2BgaPn1A4GR5UCszCi86s0j%2BwOjW0OlQxkhC7KJUwZ32I%0AZumDEgMimeomdnU2qmdIuu4Aa3W0SlkNp80Ve5KB%2FFQLQCVqYpFJeWbTkVbmMng8Cc9uHVSvJr3y%0A1HSn7dn0idW8H3vgHS0I3MOcxfL8vLaPxW9EyH92LjNvopwgIpxX4uCwAs%2FQEVWDUujm%2BIK5bXm%2B%0ATkfR5BwYbmnfodHqMYk2py0VKNKaQjY%2FflvOcbSI4lSNYXnXFx9MOm0jTQy82JkFtquYdChT1Oyq%0AAn47ieG09BE%3D|预订|55000G7072A0|G7072|SHH|AQH|SHH|OMH|05:48|08:22|02:34|Y|78tt7SEXFlPTvlmAZw1iFFKOExXToygptBNnwUoaAd7Hk2iTdBCy%2Fl0Xp9w%3D|20190131|3|HZ|01|09|1|0|||||||无||||无|无|2||O090O0M0|O9OM|0|0|null", 
            "RhmLy11iIXNG6clN2jokh42uqUCszCg0N%2B1E2BANC%2FyxOb3Txz4tP6gpS1q2kKXxayJ%2B9Ci3yhun%0AXdC7GjtZzg43xSug3tBC9nJvFPo7LdNnzoSKC8bvbLyUVReI5o90jUwWzT5%2BrE89uQ%2FKCVgeIgen%0Aa7ZInzk0yWIeLEWHxFbmlSdv4YX%2F%2BAjgyUXeGiTkkBrzmEXg%2BYqI7Ug2zoL0FT4swgpw0WKyYeSh%0AIGzjhHIZ3xo79GKdDiLNfuKElVjB0FVTSHBEy1sBn3pdNxamM9k4ydY1Bn2Az8z01KnUa82YTQ8V%0AkBj5J0W%2B6Qw%3D|预订|55000G7076F0|G7076|SHH|AQH|SHH|OMH|06:20|08:52|02:32|Y|odjRweNcwmMSMeDTnh2grxCCAbaPQaE%2FrTK%2Fn8BvZW4zU6NmMC8Ep4KiD%2BI%3D|20190131|3|HZ|01|10|1|0||||||无|1||||无|无|||O0O0M0P0|OOMP|0|0|null", 
            "|预订|55000G927610|G9276|SHH|AQH|SHH|OMH|07:10|09:44|02:34|N|MnLSO%2FRfh59%2BYaY5ckZDXU8vtFoZpxrps7E0KI7J7lBM%2BlMaIXfGG%2Fe91ZQ%3D|20190131|3|H2|01|10|1|0|||||||无||||无|无|无||O090M0O0|O9MO|0|0|null", 
            "|预订|55000G925400|G9254|SHH|WHH|SHH|OMH|07:37|10:22|02:45|N|MnLSO%2FRfh59%2BYaY5ckZDXU8vtFoZpxrps7E0KI7J7lBM%2BlMaIXfGG%2Fe91ZQ%3D|20190131|3|H1|01|10|1|0|||||||无||||无|无|无||O090M0O0|O9MO|0|0|null", 
            "|预订|55000G708001|G7080|SHH|AQH|SHH|OMH|07:44|10:09|02:25|N|vB7k4KF3dSYYuuu%2B6LdTMxb9SfmeEBFYbjc0ciM0bV9VLd1D15RF3pEDPn8%3D|20190131|3|H6|01|08|1|0|||||||无||||无|无|无||O090O0M0|O9OM|0|0|null", 
            "|预订|55000G708481|G7084|SHH|AQH|SHH|OMH|08:37|11:00|02:23|N|sL4v5i7tiuCvlR0Z%2B7wj0zXhriION3odYNL9GOD4xTmU10lm|20190131|3|HZ|01|08|1|0|||||||无||||无|无|||O0M0O0|OMO|0|0|null", 
            "|预订|55000K445810|K4458|SHH|NCW|SHH|MAH|08:40|14:16|05:36|N|SQjUm9CXr1Kt8B8UMGjP%2FSm%2BOcrP%2Bip41fiw5oxiNXWepu78|20190131|3|H1|01|06|0|0|||||无||无|||无|||||101020|112|0|0|null", 
            "|预订|56000G749230|G7492|JBH|AQH|AOH|OMH|09:03|11:28|02:25|N|MnLSO%2FRfh59%2BYaY5ckZDXU8vtFoZpxrps7E0KI7J7lBM%2BlMaIXfGG%2Fe91ZQ%3D|20190131|3|H6|08|15|1|0|||||||无||||无|无|无||O090M0O0|O9MO|0|0|null", 
            "MTkeofC4vWli7QG2C%2FjRRCJD%2FtdrTzBhwUmaHCKJBgRLz1vg8GgLWqSZPW2t%2FyL%2BIQ8dc4eJuFdl%0A1Upm%2F9mvawjyY8sitl%2Bg2SDomxu%2FFFI0FN%2B3%2FNNilqH4SVBNzzzCaSvM1Cb5WunnSFkBmAFPPTUp%0AMEgJ88xY9sSEcu3EfrZnjBGzwHQ71QYhl3XGlbt4B9id8kDzgjaJ6jTS%2B8ho2Lry5%2BzalDUzXYPQ%0Aq5YqTMRpySnUbkxf9Mqil2YdPV95dAXNmcTMjNImovqu4G9eHzxx7GKhDQxekq2%2Bz%2BMgk02a3PAP%0ALPxbDCeDFK7MmENmOptUdw%3D%3D|预订|5l000G7132D1|G7132|AOH|AQH|AOH|OMH|09:41|11:56|02:15|Y|seybQ49lJrwiNNhGSVBNArIzn1efh8efKSSqNIG44WBjYYapNeC1KF5zFqU%3D|20190131|3|HY|01|07|1|0|||||||无||||无|无|6||O090M0O0|O9MO|0|0|null", 
            "|预订|55000K155601|K1556|SHH|NNZ|SHH|MAH|10:21|15:43|05:22|N|MeRB3Vx7cetjvUOCkja27VzMMjj5dv7bDxoAlI54wXUQnsXONr0rd6nKwvI%3D|20190131|3|H2|01|08|0|0||||无|||无||无|无|||||10401030|1413|0|0|null", 
            "|预订|5l000G7136D0|G7136|AOH|AQH|AOH|OMH|10:29|12:53|02:24|N|MnLSO%2FRfh59%2BYaY5ckZDXU8vtFoZpxrps7E0KI7J7lBM%2BlMaIXfGG%2Fe91ZQ%3D|20190131|3|H6|01|08|1|0|||||||无||||无|无|无||O090M0O0|O9MO|0|0|null", 
            "|预订|55000G706080|G7060|SHH|AQH|SHH|OMH|10:40|13:08|02:28|N|MnLSO%2FRfh59%2BYaY5ckZDXU8vtFoZpxrps7E0KI7J7lBM%2BlMaIXfGG%2Fe91ZQ%3D|20190131|3|H1|01|09|1|0|||||||无||||无|无|无||O090M0O0|O9MO|0|0|null", 
            "|预订|55000K115651|K1156|SHH|CDW|SHH|MAH|11:16|16:41|05:25|N|MeRB3Vx7cetjvUOCkja27VzMMjj5dv7bDxoAlI54wXUQnsXONr0rd6nKwvI%3D|20190131|3|H6|01|08|0|0||||无|||无||无|无|||||10401030|1413|0|0|null", 
            "1mL1qjaJi3bigzb1rZPKA%2Bs1rbSx5kC1lWBsFf6uuqVc5hSg12E8AuLUmRUt0TPMLX07AXBiDTdf%0ABiTouNW0X%2BixCbUVyNCZzVJYV6izUmeN0vdZx9KxFrK93ViCFmscD7SoSpsLjgDfaVWXbWX4sq7d%0Ai%2FX1FcBooleZsrh4va09UuaYCWug1CaT2M1%2BK1aRUD12LhlBaro%2FGKgwteOvQ8M0hUzSd6tk4vHr%0A83c77EAyjRS2X4qy1cyIi%2FgPg6oQniUtFu%2BhJjiEAzAb0hTSctOEzb7LIVqnyeU22odcOBApnOvR%0A|预订|55000G728230|G7282|SHH|WHH|SHH|OMH|11:33|13:54|02:21|Y|cDDNdx5cnFzyML3I%2BWYU%2FLoQ1IDgV%2FEtebH3Dm9xh%2FEMNMX7|20190131|3|H6|01|08|1|0|||||||有||||无|无|||O0M0O0|OMO|0|0|null", 
            "|预订|550000K78270|K782|SHH|PXG|SHH|MAH|12:28|18:20|05:52|N|%2FJ2oYsU3iG6VHf7fXfsej3TB3R7wGicdHF0hDxeuQ9nSPsek|20190131|3|H6|01|08|0|0|||||||无||无|无|||||101030|113|0|0|null", 
            "|预订|55000G708861|G7088|SHH|AQH|SHH|OMH|12:54|15:17|02:23|N|vB7k4KF3dSYYuuu%2B6LdTMxb9SfmeEBFYbjc0ciM0bV9VLd1D15RF3pEDPn8%3D|20190131|3|H6|01|07|1|0|||||||无||||无|无|无||O090O0M0|O9OM|0|0|null", 
            "|预订|550000321650|3216|SHH|CDW|SHH|MAH|13:02|18:46|05:44|N|iyrM4q6WU%2BiFMZQbYOvnVlgSY51lSXMK|20190131|0|HZ|01|08|0|0|||||||无|||无|||||1010|11|0|0|null", 
            "iYP6d2hOoJl1l020l%2BH8opTT7LFFyJo7%2BinW8oOwKiK%2B9bqweFNvuMHAzvFBTL5sTaYzbSACaHeP%0A50MZXt4l6%2FvyyFCe%2BcW%2B5ea64cFmn8xccf56l30OYU3S1NyJL2REjQsHPxcOALy1p6%2BsysORA3MR%0AxJR0sMDaw4n%2BpFXpPCZowx%2BF00Tu852TqwaIaejZrZ%2BNFyrXFXhRj7dHkyqmPbmuSS63LrngM0cK%0AhYPDTMwWK2tka67q%2FoVxle69vwYcS3nkna0t6WxQaeO2AEJVR5PfT6pMPfggj8XCHSBdzVcvLk2H%0AheuSUA%3D%3D|预订|5l000G714861|G7148|AOH|WHH|AOH|OMH|13:35|15:56|02:21|Y|MdmQB8zeKUw6P%2F0%2BgNyIwAnhO2Hea6%2F4Xg5pUaYDwu1OV7Sy|20190131|3|H2|01|08|1|0|||||||有||||无|无|||O0M0O0|OMO|0|0|null", 
            "|预订|55000G7092N0|G7092|SHH|AQH|SHH|OMH|13:41|16:11|02:30|N|vB7k4KF3dSYYuuu%2B6LdTMxb9SfmeEBFYbjc0ciM0bV9VLd1D15RF3pEDPn8%3D|20190131|3|H6|01|09|1|0|||||||无||||无|无|无||O090O0M0|O9OM|0|0|null", 
            "|预订|5l000G7140A0|G7140|AOH|AQH|AOH|OMH|15:04|17:26|02:22|N|MnLSO%2FRfh59%2BYaY5ckZDXU8vtFoZpxrps7E0KI7J7lBM%2BlMaIXfGG%2Fe91ZQ%3D|20190131|3|H6|01|08|1|0|||||||无||||无|无|无||O090M0O0|O9MO|0|0|null", 
            "|预订|55000G9246B0|G9246|SHH|AQH|SHH|OMH|15:21|17:46|02:25|N|MnLSO%2FRfh59%2BYaY5ckZDXU8vtFoZpxrps7E0KI7J7lBM%2BlMaIXfGG%2Fe91ZQ%3D|20190131|3|H3|01|07|1|0|||||||无||||无|无|无||O090M0O0|O9MO|0|0|null", 
            "98IkKpnSheUIe5kIzRSo074w%2FscncENUuT%2F96t0nfOSmQnG1s6pg8CRNAVEuMD5OgAUp9lqDh3WA%0Ay%2FzPmcmYWSQMfapHxnAPkVfYlg0qG1u8TDiGMFUgrkBl4rMBy%2BFJtkdvf8v7EZo9dkNFPK7L9FNt%0A%2BHQx4w22JvaDa5%2F1M9QdWlfNq%2BNtf%2Fv0r60dbyn%2FsL1O7f7CXXh6jflNHkHjFmHDIiTFq7lq0KWW%0AVoYug4tK%2BcOBGtOPtaFnDkvf3CRuGPekjc92MWAVh48S78quoMJulPFos4ETRwQdtHgqMA%2B7gdIH%0AT1uXXqiemkI%3D|预订|55000G721850|G7218|SHH|WHH|SHH|OMH|15:29|17:32|02:03|Y|MwgwCk9SAn%2B0dgd3hDAZdKoZp5d8dbxEYdeFXhCvNfUsv%2B%2FUo2FT6WVJLQM%3D|20190131|3|H1|01|05|1|0|||||||2||||3|5|1||O090O0M0|O9OM|0|0|null", 
            "|预订|55000K413841|K4138|SHH|CDW|SHH|MAH|15:39|22:45|07:06|N|G09CazGb1j4lTY%2B%2Fe9nh%2BAUILHX88oS9npiH9Ffji%2B9pm5QY|20190131|3|H1|01|07|0|0||||无|||无|||无|||||101040|114|0|0|null", 
            "EEnEhfGV4V65%2BrvJhckFZCIQi7JqUUdWxXUl2x2M5UkYxDPgGBPYhbdtOSUiTRGXLf7XGcV45vyB%0AZ8x38fF5Wso79%2BywNs842nTZXsoT2Tn5arKECL6yhGH%2F30BqfYnDTzYeits16McRTLZ4fP4bIqc%2F%0AspfoP8E0xXAFVhAfHFAF98GYD6TEOIvqfRqXzan%2FOuLgbNwPXv13293spb7%2FpJ4rmno3epxK6EcT%0A7ycmxfYXCpfbWzG9%2FgzedP4UdHZyhUfGJApE0Iiu1FSC6UPcSK0cxlVkGiramRhPnv104nVNgtbX%0AVOeQFUfmt2OqSfWKZk5Nfw%3D%3D|预订|5l000G715272|G7152|AOH|WHH|AOH|OMH|15:50|18:24|02:34|Y|jKmj0PUDaGMhCs4oVFaezLNOw7aEWkSDPBMQk9PCFq2ZsP14PrGTDekNHf0%3D|20190131|3|H3|01|09|1|0|||||||有||||5|2|5||O090M0O0|O9MO|0|0|null", 
            "|预订|5j000G759212|G7592|VRH|AQH|AOH|OMH|16:25|19:07|02:42|N|MnLSO%2FRfh59%2BYaY5ckZDXU8vtFoZpxrps7E0KI7J7lBM%2BlMaIXfGG%2Fe91ZQ%3D|20190131|3|H6|12|22|1|0|||||||无||||无|无|无||O090M0O0|O9MO|0|0|null", 
            "|预订|5l000G714470|G7144|AOH|AQH|AOH|OMH|17:05|19:38|02:33|N|vB7k4KF3dSYYuuu%2B6LdTMxb9SfmeEBFYbjc0ciM0bV9VLd1D15RF3pEDPn8%3D|20190131|3|H6|01|09|1|0|||||||无||||无|无|无||O090O0M0|O9OM|0|0|null", 
            "|预订|5l000G936410|G9364|AOH|AQH|AOH|OMH|18:18|20:53|02:35|N|sL4v5i7tiuCvlR0Z%2B7wj0zXhriION3odYNL9GOD4xTmU10lm|20190131|3|H1|01|09|1|0|||||||无||||无|无|||O0M0O0|OMO|0|0|null", 
            "|预订|55000G727280|G7272|SHH|AQH|SHH|OMH|18:42|21:04|02:22|N|MnLSO%2FRfh59%2BYaY5ckZDXU8vtFoZpxrps7E0KI7J7lBM%2BlMaIXfGG%2Fe91ZQ%3D|20190131|3|H1|01|08|1|0|||||||无||||无|无|无||O090M0O0|O9MO|0|0|null", 
            "BxZHWSkwHgQQGdSlZDMWn85h8NzNeXLlK6%2F3A5v8ju1XOkVL5CZ5IWDDW9Jz9NnDY9YSluBfRbht%0Axgq1yTZuXtrGRKYctIYE7CZde08tpMewYwgkh6O6onC8b7pSYXTGvsQbnwbRPN7kVkDlTvdlaSd5%0AdX2WV46DvRVf3SaA6aUZ4rp%2F0B%2FNp%2FfwfFd0hVDsKeX825VtK6xWj%2F1sBOuCkRBkK8dd86CLwm8T%0AY3y9%2FEUuK0iOai0RZADaoqbTzHDsIM5m3TvN7Cej83LpiyXLWLYuwEmcEPgD5%2FlBjV0A53ee8haH%0AhgaXGM7076U%3D|预订|55000G7226A0|G7226|SHH|WHH|SHH|OMH|19:37|22:12|02:35|Y|Y8nV1zu31NSWbLl%2BDs6ped46cK4yAHC6BYWmfytaaQ7AcHMktiC58RHu26A%3D|20190131|3|H1|01|09|1|0|||||||有||||15|16|5||O090M0O0|O9MO|0|0|null", 
            "HNIZEIxEagI6b%2FhO1SEX1YbfiGXG8HWP1jv6d1g6n3fNTbnjF4dDsunJY1t%2ByQIBuNAHd96bXhKS%0Aj3LUYCJcsV5DBpxRLrrqAcQyaxjPDZ%2FOaBngkq8een1ZTa28WP%2FIiPEjD4J4wCQQooC1jTpIZNNV%0ALx0Sd7Hx%2BJ%2F9V%2BOa%2FK9xvuj6duW8Q8cggfwEJt799sZ%2Fb9ZPCUTsygANC57%2FqaRuXGW86ttbM8sb%0AXq6PU750E%2BeyRiEGAGHgGURKo2mHwiPK80rJrZjHHNorsXteuDY21gpoewptngKWM5UOQ%2BRPbn%2FX%0A|预订|55000G728610|G7286|SHH|WHH|SHH|OMH|20:35|22:47|02:12|Y|yWmmJeDnlyuVaFRID39o8hwy9GTJmkV8eDyQ1uMkY5KIIvOV|20190131|3|H2|01|07|1|0|||||||有||||17|无|||O0M0O0|OMO|0|0|null", 
            "fSDVfDVnwa1gcUyP1VKq%2BOMEkFG2PCspqky2l%2FSz%2FQfKLrxNNB9h1XfcVFZ13oi4rePjm5JAzYfY%0ALq8O8fuK9RJOVstF9TRtDiV8WBfQcZxNSMykx5HgNnkU1QX2K09sY7Qa5F7VQlpnK8%2BZlgQV8IFs%0ASlv3hvZtR%2FEEtBkPGPlGUtR2yiGuNdiZIeSihv%2B7SbrVIwmEGSiSONo2W%2FFqvTTkyB7mstulfANn%0A2j80snQnyOr2tFG5iN5C2mk90ZbOH9hw6ps9pFhNQD678jra2yl4QdbYDFGkwlYfQVM%2BUYmrbhLy%0A%2F2WEJVLSm60%3D|预订|55000G936820|G9368|SHH|AQH|SHH|OMH|23:58|02:04|02:06|Y|5gVJPtqQ2iTyUCy%2BNRAebQrNNFCMtor5wOYfOQ4fBMevV7YYTRbcuDZB%2FQ8%3D|20190131|3|H3|01|06|1|0|||||||有||||1|1|3||O090M0O0|O9MO|0|0|null"
        ]
    }, 
    "httpstatus": 200, 
    "messages": "", 
    "status": true
}
'''