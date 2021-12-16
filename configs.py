# copyright ©️ 2021 nabilanavab
# fileName: configs.py
# Total time wasted ~ 250 hrs



import os
    
    
    
    
    
# Config Variables
class Config(object):
    API_ID = 2171111
    API_HASH = "fd7acd07303760c52dcc0ed8b2f73086"
    API_TOKEN = "5075889854:AAELvW6bgSURT1a3z60pJMaRVGw_P_rQrxQ"
    UPDATE_CHANNEL = "ourclg"
    CONVERT_API = 884329853
    MAX_FILE_SIZE = 100
    OWNER_ID = 1089528685
    BANNED_USER = ""
    PDF_THUMBNAIL = "./IMG_20211216_063728_789.jpg"
    
    
    
    
    
# Message Variables
class Msgs(object):
    
    
    welcomeMsg = """Hey [{}](tg://user?id={})..!! This bot will helps you to do many things with pdf's 🥳

Some of the main features are:
◍ `Convert images to PDF`
◍ `Convert PDF to images`
"""
    
    
    feedbackMsg = """
[Join grp](http://t.me/ourclg)
"""
    
    
    forceSubMsg = """Wait [{}](tg://user?id={})..!!

Due To The Huge Traffic Only Channel Members Can Use 🚶
    
This Means You Need To Join The Below Mentioned Channel Before Using Me!

hit on "retry ♻️" after joining.. 😅
"""
    
    
    foolRefresh = """kek 😐"""
    
    
    fullPdfSplit = """If you want to split a pdf,

you need to send limits too..🙃
"""
    
    
    bigFileUnSupport = """Due to Overload, bot supports only {}mb files

`please Send me a file less than {}mb Size`🙃
"""
    
    
    encryptedFileCaption = """Page Number: {}
key 🔐: `{}`"""
    
    
    imageAdded = """`Added {} page/'s to your pdf..`🤓

/generate to generate PDF 🤞
"""
    
    
    errorEditMsg = """Something went wrong..😐

ERROR: `{}`
"""
    
    
    pdfReplyMsg = """`Total pages: {}pgs`

__Unlike all other bots, this bot start sending images without converting the entire PDF to pages__ 😉

reply:
/extract - __to get entire pages__
/extract `pgNo` - __to get a specific page__
/extract `start:end` - __to get all the images b/w__


/encrypt `password` - to set password
/text - to extract text from pdf

Join Update Channel @ilovepdf_bot, More features soon 🔥
"""
    
    
    aboutDev = """About Dev:

OwNeD By: @s4tyendra 😜
For: @ourclg 😇                                                                

Lang Used: python
"""
    
    
    I2PMsg = """Images to pdf :

        Just Send/forward me some images. When you are finished; use /generate to get your pdf..😉

 ◍ Image Sequence will be considered 🤓
 ◍ For better quality pdfs(send images without Compression) 🤧
 
 ◍ `/delete` - Delete's the current Queue 😒
 ◍ `/id` - to get your telegram ID 🤫                                                            
 
 ◍ RENAME YOUR PDF:
 
    - By default, your telegram ID will be treated as your pdf name..🙂
    - `/generate fileName` - to change pdf name to fileName🤞
    - `/generate name` - to get pdf with your telegram name

"""
    
    
    P2IMsg = """PDF to images:

        Just Send/forward me a pdf file.

 ◍ I will Convert it to images ✌️
 ◍ if Multiple pages in pdf(send as albums) 😌
 ◍ Page numbers are sequentially ordered 😬
 ◍ Send images faster than anyother bots 😋
 ◍ /cancel : to cancel a pdf to image work                                                       

1st bot on telegram wich send images without converting entire pdf to images

"""
    
    
    F2PMsg = """Files to PDF:

        Just Send/forward me a Supported file.. I will convert it to pdf and send it to you..😎

◍ Supported files(.epub, .xps, .oxps, .cbz, .fb2) 😁
◍ No need to specify your telegram file extension 🙄
◍ Only Images & ASCII characters Supported 😪
◍ added 30+ new file formats that can be converted to pdf..
API LIMITS..😕

"""
    
    
    warningMessage = """WARNING MESSAGE ⚠️:

◍ This bot is completely free to use so please dont spam here 🙏

◍ Please don't try to spread 18+ contents 😒

IF THERE IS ANY KIND OF REPORTING, BUGS, REQUESTS, AND SUGGESTIONS PLEASE CONTACT @nabilanavab

"""
    
    
    back2Start = """Hey..!! This bot will helps you to do many things with pdf's 🥳

Some of the main features are:
◍ `Convert images to PDF`
◍ `Convert PDF to images`
◍ `Convert files to pdf`
"""

# please don't try to steel this code,
# god will asks you :(
