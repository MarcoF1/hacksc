import os
import time
import mux_python
from mux_python.rest import ApiException
import joblib
from nltk.tokenize import word_tokenize
from sentiment import remove_noise
import random


class EmotionalVideos:

    def __init__(self, category):
        self.token_id = '9e6896bb-bb40-4a1b-bee4-0245d4c117aa'
        self.token_secret = 'i5mKOIUKu5Z0uE22BaiYPy6AsQ0qt7RjW2dYdofwXEORbMic92tDKcsm/6bOJc8wVxquO4+io6s'

        self.procrastination = 'https://r3---sn-a5mekn7k.googlevideo.com/videoplayback?expire=1580619236&ei=hAE2XpSjKIOjkgalmKjQCw&ip=2604%3A180%3A3%3A38%3A425%3Aeb45%3A5a0a%3Ae226&id=o-AO6YcTQo5eeJgH0x94wD0X1NIdt1Qa794E7jHgcUZG9f&itag=43&source=youtube&requiressl=yes&vprv=1&mime=video%2Fwebm&gir=yes&clen=49766235&ratebypass=yes&dur=0.000&lmt=1544824332409978&fvip=3&fexp=23842630&c=WEB&txp=5511222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=ALgxI2wwRQIhANECo_KIGBhOPq0kC-e8yV4buKofbmkC5v4ewRamb0TLAiA6JMMafQUiLSEg3NhDpEXG-xMuxkTim0s9MkkjhC1LYg%3D%3D&rm=sn-o09lz7s&req_id=5439d8a9c8e8a3ee&ipbypass=yes&cm2rm=sn-oxuuvn-a5me7s,sn-a5mdr7s&redirect_counter=3&cms_redirect=yes&mip=207.151.53.63&mm=34&mn=sn-a5mekn7k&ms=ltu&mt=1580597602&mv=m&mvi=2&pl=23&lsparams=ipbypass,mip,mm,mn,ms,mv,mvi,pl&lsig=AHylml4wRAIgaxzSDrqfM2mbyvOcmd6IsNLJKaoqLh3ovKqv4d-B2EYCIGHBGCJbj39mx3rZl-6OvjHx8TJ-8iRIssBy7ifjkXr0'
        self.happy = 'https://r3---sn-a5mlrn7r.googlevideo.com/videoplayback?expire=1580610755&ei=YuA1XvHqMe-AsfIPg5aG0As&ip=2604%3A180%3A3%3A38%3A425%3Aeb45%3A5a0a%3Ae226&id=o-AIRR0_kO0gc8P5jXfDJ5mWFIAt--WZOm4esHLlBvRsKt&itag=43&source=youtube&requiressl=yes&vprv=1&mime=video%2Fwebm&gir=yes&clen=4926708&ratebypass=yes&dur=0.000&lmt=1540519809036402&fvip=3&fexp=23842630&c=WEB&txp=5411222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=ALgxI2wwRgIhANcDsKPQYOqJO6KqBaVZZUyY1spRBEUq7K9qWnDCOdkaAiEAqSLAg7GnyZ2GgJSYLm-EQjkYhc3jsPpHduw0t1kTHUw%3D&redirect_counter=1&cm2rm=sn-o09lk7s&req_id=57fe1430f6d1a3ee&cms_redirect=yes&mip=207.151.53.63&mm=34&mn=sn-a5mlrn7r&ms=ltu&mt=1580588718&mv=u&mvi=2&pl=23&lsparams=mip,mm,mn,ms,mv,mvi,pl&lsig=AHylml4wRgIhALYOUeDJjMe5VHRC2Q3BAZdsFHiyt9584oax-CCWXVUmAiEA7d_3oKAeMf0ZlqOySF-e_0Va29B8FCARf7PibL1pW90%3D'
        self.happy2 = 'https://r1---sn-oxuuvn-a5me.googlevideo.com/videoplayback?expire=1580619389&ei=HQI2XoC4NtaEkgaIsKKQDw&ip=2604%3A180%3A3%3A38%3A425%3Aeb45%3A5a0a%3Ae226&id=o-AMfqgv4XhEMBNaXUK_GAZ7o34KINAwY6hCT-CqM01zFV&itag=18&source=youtube&requiressl=yes&gcr=us&vprv=1&mime=video%2Fmp4&gir=yes&clen=13952988&ratebypass=yes&dur=240.674&lmt=1574969510213381&fvip=5&fexp=23842630,23860862&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=ALgxI2wwRAIgZnL0qRyrpZwNm8a2bJh7YWAemqNDcF5zXLARlbnvsD0CIC6JaNQUVzMY0lvdNWyjf2EY2IWURl10NfAq7CblsiPa&redirect_counter=1&rm=sn-n4vls76&req_id=6809e40d145ea3ee&cms_redirect=yes&ipbypass=yes&mip=207.151.53.63&mm=31&mn=sn-oxuuvn-a5me&ms=au&mt=1580597680&mv=m&mvi=0&pl=23&lsparams=ipbypass,mip,mm,mn,ms,mv,mvi,pl&lsig=AHylml4wRAIgaYhfTSFlzpID6X_HxQ3zElUuWj5iDihMxb9aIa11z8kCIHoQ83EfG9MwCzthQmziRXJ1lzgVlPfvlNbcHdhq1vOw'
        self.nervous = 'https://r2---sn-a5msen7z.googlevideo.com/videoplayback?expire=1580619617&ei=AQM2XtmJFK6CsfIPqf43&ip=2604%3A180%3A3%3A38%3A425%3Aeb45%3A5a0a%3Ae226&id=o-AMiGbT3Lz0RghqzrRcoekWa1H87ylBxzcZOYS5i-DpFx&itag=43&source=youtube&requiressl=yes&vprv=1&mime=video%2Fwebm&gir=yes&clen=56449875&ratebypass=yes&dur=0.000&lmt=1546055831075557&fvip=2&fexp=23842630&c=WEB&txp=5511222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=ALgxI2wwRQIgfpc7wzCKEcn7isVf6TJZDN6B1J7CJXIgNYU8t48ISeUCIQCTMAy1ig-rV6y1sNaxnVNntboGZIkOZm7_XxSTuUfTSQ%3D%3D&redirect_counter=1&cm2rm=sn-n4vll7l&req_id=5a076087ae59a3ee&cms_redirect=yes&mip=207.151.53.63&mm=34&mn=sn-a5msen7z&ms=ltu&mt=1580597757&mv=u&mvi=1&pl=23&lsparams=mip,mm,mn,ms,mv,mvi,pl&lsig=AHylml4wRQIgXxbcsOvl3ozcf7RCIAVbxPY1UAC_YDKzOh9QdGMzDAsCIQCppsSdu38JrDlGEm084zZ4UR2Z9ynWO8yWSWqHXTZnJQ%3D%3D'
        self.sleep = 'https://r1---sn-a5meknlz.googlevideo.com/videoplayback?expire=1580619685&ei=RQM2XqW3A8yFkwb3rr7IBw&ip=2604%3A180%3A3%3A38%3A425%3Aeb45%3A5a0a%3Ae226&id=o-AGRqNqiWIbkZ0lnAf0QkzVx47ZIWGegQVcIhGxhAeM90&itag=43&source=youtube&requiressl=yes&vprv=1&mime=video%2Fwebm&gir=yes&clen=117094888&ratebypass=yes&dur=0.000&lmt=1545884546002844&fvip=1&fexp=23842630&c=WEB&txp=5511222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=ALgxI2wwRQIhAIhlo-UNaejpRInoOGje0OXROBiPUahuypWWtadxTj49AiBS3Lru2x5LCqdRbQ92TexWUqjIGaQ9zEd3VatNT9AZPA%3D%3D&redirect_counter=1&cm2rm=sn-n4vll7e&req_id=905e872457d3a3ee&cms_redirect=yes&mip=207.151.53.63&mm=34&mn=sn-a5meknlz&ms=ltu&mt=1580597757&mv=u&mvi=0&pl=23&lsparams=mip,mm,mn,ms,mv,mvi,pl&lsig=AHylml4wRQIhAMnQJFgsTkJDLxaQ3QpJXYKN6VulBizrJ0lsLC1aDJRPAiBjvzvVXcPpiSSDTTQv0rLP1lb7kcJF07d9fGEoAjH4Zg%3D%3D'

        self.library = {'procrastination': [self.procrastination],
                        'happy': [self.happy, self.happy2],
                        'nervous': [self.nervous],
                        'sleep': [self.sleep]
                        }

        self.list_videos = [self.happy, self.happy2, self.nervous]

        self.category = category

    def setup(self):
        # Authentication Setup
        os.environ['MUX_TOKEN_ID'] = self.token_id
        os.environ['MUX_TOKEN_SECRET'] = self.token_secret

        self.configuration = mux_python.Configuration()
        self.configuration.username = os.environ['MUX_TOKEN_ID']
        self.configuration.password = os.environ['MUX_TOKEN_SECRET']

        # API Client Initialization
        self.assets_api = mux_python.AssetsApi(mux_python.ApiClient(self.configuration))

    def analyze_sentiment(self):
        classifier = joblib.load('sentiment.pkl')

        tokens = remove_noise(word_tokenize(self.category))

        self.classification = classifier.classify(dict([token, True] for token in tokens))

        self.video = random.choice(self.list_videos)


    def create_asset(self):
        # Create an asset

        self.input_settings = [mux_python.InputSettings(url=self.video)]
        self.create_asset_request = mux_python.CreateAssetRequest(input=self.input_settings, playback_policy=[mux_python.PlaybackPolicy.PUBLIC], mp4_support="standard")

        self.create_asset_response = self.assets_api.create_asset(self.create_asset_request)
        #print("Created Asset ID: " + self.create_asset_response.data.id)

    def create_video_link(self):
        self.analyze_sentiment()
        if self.classification == 'Negative':
            self.setup()
            self.create_asset()

            # Wait for the asset to become ready, and then print its playback URL
            if self.create_asset_response.data.status != 'ready':
                #print("Waiting for asset to become ready...")
                while True:
                    self.asset_response = self.assets_api.get_asset(self.create_asset_response.data.id)
                    if self.asset_response.data.status != 'ready':
                        pass
                        #print("Asset still not ready. Status was: " + self.asset_response.data.status)
                    else:
                        #print("Asset Ready! Playback URL: https://stream.mux.com/" + self.asset_response.data.playback_ids[0].id + ".m3u8")
                        return 'https://stream.mux.com/' + self.asset_response.data.playback_ids[0].id + ".m3u8"
        else:
            return "Glad to see that you're doing fine"


if __name__ == '__main__':
    x = EmotionalVideos('i got married but my mom died')
    print(x.create_video_link())






