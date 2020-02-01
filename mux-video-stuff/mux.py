import os
import time
import mux_python
from mux_python.rest import ApiException


# Authentication Setup
os.environ['MUX_TOKEN_ID'] = '9e6896bb-bb40-4a1b-bee4-0245d4c117aa'
os.environ['MUX_TOKEN_SECRET'] = 'i5mKOIUKu5Z0uE22BaiYPy6AsQ0qt7RjW2dYdofwXEORbMic92tDKcsm/6bOJc8wVxquO4+io6s'

configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

# API Client Initialization
assets_api = mux_python.AssetsApi(mux_python.ApiClient(configuration))

# Create an asset
video = 'https://r3---sn-a5mlrn7r.googlevideo.com/videoplayback?expire=1580610755&ei=YuA1XvHqMe-AsfIPg5aG0As&ip=2604%3A180%3A3%3A38%3A425%3Aeb45%3A5a0a%3Ae226&id=o-AIRR0_kO0gc8P5jXfDJ5mWFIAt--WZOm4esHLlBvRsKt&itag=43&source=youtube&requiressl=yes&vprv=1&mime=video%2Fwebm&gir=yes&clen=4926708&ratebypass=yes&dur=0.000&lmt=1540519809036402&fvip=3&fexp=23842630&c=WEB&txp=5411222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=ALgxI2wwRgIhANcDsKPQYOqJO6KqBaVZZUyY1spRBEUq7K9qWnDCOdkaAiEAqSLAg7GnyZ2GgJSYLm-EQjkYhc3jsPpHduw0t1kTHUw%3D&redirect_counter=1&cm2rm=sn-o09lk7s&req_id=57fe1430f6d1a3ee&cms_redirect=yes&mip=207.151.53.63&mm=34&mn=sn-a5mlrn7r&ms=ltu&mt=1580588718&mv=u&mvi=2&pl=23&lsparams=mip,mm,mn,ms,mv,mvi,pl&lsig=AHylml4wRgIhALYOUeDJjMe5VHRC2Q3BAZdsFHiyt9584oax-CCWXVUmAiEA7d_3oKAeMf0ZlqOySF-e_0Va29B8FCARf7PibL1pW90%3D'
input_settings = [mux_python.InputSettings(url=video)]
create_asset_request = mux_python.CreateAssetRequest(input=input_settings, playback_policy=[mux_python.PlaybackPolicy.PUBLIC], mp4_support="standard")

create_asset_response = assets_api.create_asset(create_asset_request)
print("Created Asset ID: " + create_asset_response.data.id)

# Wait for the asset to become ready, and then print its playback URL
if create_asset_response.data.status != 'ready':

    print("Waiting for asset to become ready...")
    while True:
        asset_response = assets_api.get_asset(create_asset_response.data.id)
        if asset_response.data.status != 'ready':
            print("Asset still not ready. Status was: " + asset_response.data.status)
            time.sleep(1)
        else:
            print("Asset Ready! Playback URL: https://stream.mux.com/" + asset_response.data.playback_ids[0].id + ".m3u8")
            break
#<video src="https://stream.mux.com/aKtR8TnFzymKtXMV8OlK6r8ZXj8ykM67.m3u8">