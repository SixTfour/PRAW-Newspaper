import praw

paper = open("Today's News.txt", 'w')
print(paper)

def main():
    
    r = praw.Reddit(user_agent='R News by u/thelegend64')
    #Searches through the top 12 posts in r/news
    submissions = r.get_subreddit('news').get_hot(limit=12)
    #Formats the posts as follows: post number, headline, web address
    submission_form = "{}) {} <{}> \n"
    count = 1
    paper.write("Reddit'ser: Yesterday's News, Today \n")
    paper.write('-' * 100)
    paper.write("\n")
    for sub in submissions:
        paper.write(submission_form.format(count, sub.title, sub.url))
        print("\n"*2)
        count += 1

main()
paper.close()
