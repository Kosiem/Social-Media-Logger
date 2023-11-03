import FacebookModule
import RedditModule
import LinkedInModule
import InstagramModule
import TikTokModule
import YoutubeModule

# Start app and select which social media you want to log in.
# If you choose one of them, module responsible for this will start
media = input("Select social media to log in:\n")
if media == "Facebook":
    FacebookModule.LogInFacebook()
elif media == "Instagram":
    InstagramModule.LogInInstagram()
elif media == "LinkedIn":
    LinkedInModule.LogInLinkedIn()
elif media == "TikTok":
    TikTokModule.LogInTikTok()
elif media == "Reddit":
    RedditModule.LogInReddit()
elif media == "Youtube":
    YoutubeModule.LogInYoutube()
