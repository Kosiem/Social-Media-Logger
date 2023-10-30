import FacebookModule
import RedditModule
import LinkedInModule
import InstagramModule
import TikTokModule
import YoutubeModule

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
    RedditModule.LogInTwitter()
elif media == "Youtube":
    YoutubeModule.LogInYoutube()