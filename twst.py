
import requests
from time import sleep


headers =  {
'authority': 'gramfree.today'
,'Accept': '*/*'
,'Origin': 'https://gramfree.today'
,'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'
,'Content-Type': 'application/x-www-form-urlencoded'
,'Referer': 'https://gramfree.today/free'
,'Accept-Encoding': 'gzip, deflate, br'
,'Accept-Language': 'en-US,en;q=0.9'
,'Cookie': 'vapor-session=z1IDgcrAOBLCYcNL4V+wSA==; _ym_uid=1622886026548858304; _ym_d=1622886026; _ga=GA1.2.1573352557.1622886033; __gads=ID=55224fe489c9632c:T=1622886042:S=ALNI_MYtZT7LHmURv10r_gWfCDYAUNRptQ; _gid=GA1.2.351307480.1623226336; _ym_isad=2; _gat_gtag_UA_179935975_1=1; FCCDCF=[["AKsRol8cYdbX8piRB5iN3qKUfHk7q0dIp_Bl08Sho5M734u3OJm12lzX6MZQPdt4sVb7qzhedWuE8J_z6236rDGcl-WuOyg3dhtaqEa25U1RsvCP8V0jnjqv8LISeqn6I91ctITrvFN5jpzyUTVRNKbaa5vwCsm4BQ=="],null,["[[],[],[],[],null,null,true]",1623244356884],null,null]'
}

form_data = {
'isWinWinRoll': 'true'
,'reCaptchaToken':' 03AGdBq24zTSwQvr9pDPQdIonQM7698IlajDSDedPP1sBlLstCMbqBnFRyENP8UkUv2_2lE_ZCbwlD0QF9_Mba5oRaDrk3zKEKoVLNgdB03tNQUyE32At13Ue39PHveZaCVBHgNceaQC3wPsIAIAhgLpo1Xy5Gg_pkzTwUxm-Jy6yIg1cKAmYwANIQYohaVhB8_lW0FHSFftK7Gi_9p3iPCXkFUOHAkX9ZO-SJDJ7P7zqcmxBAKCA4dQA3tFlwaQpf4OjUSaz1Z1GALqH5XNC5DIeMWyNmaatiduuPKTEd5xuF5CogkQEt1ecjymJ-RaM9sZ6WnoWerWuM2glw-obSVn_vw12IIoIh9taSayYAqdwAoaAxggw7aq8cAbpImonI1hRCP86NyGvdzhF9fXDoG-Psjz2Vd7DMol2_41UMDhk4jEBZrVzmRSWHnKTHFOvB3S1Eab_4TaLX'
,
}


while True:
    res = requests.post('https://gramfree.today/roll',headers = headers,data=form_data )
    print(res)
sleep(5)




