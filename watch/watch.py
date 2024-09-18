import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    #Example html
    #<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
    if matches:= re.search(r"^<iframe(?:.*)? src=\"([a-zA-Z0-9:/\.]*)\"(?:.*)?></iframe>$", s):
        url = matches.group(1)
        if matches:= re.search(r"^http(?:s)?://(?:www.)?youtube.com/embed/(.*)$", url):
            video_id = matches.group(1)
            #Example shareable url
            #https://youtu.be/xvFZjo5PgG0
            return "https://youtu.be/" + video_id
    return "None"


if __name__ == "__main__":
    main()
