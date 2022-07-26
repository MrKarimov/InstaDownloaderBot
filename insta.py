def kali(link_in):
    import requests
    import json
 
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"
    querystring = {"url":link_in}

    headers = {
       "X-RapidAPI-Key": "d3217b980emsh92ea048a4a6ed7ap1326e9jsn6297b9bb24f0",
	   "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    result=response.text
    res=json.loads(result)
    return{"media":res['media']}
