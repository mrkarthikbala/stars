import praw,time

def login():
		r = praw.Reddit(user_agent = 'something')
		submissions = r.get_subreddit('IAMA').get_hot(limit =6 )
		J = get_AMA_names(submissions)
		return J
def get_AMA_names(submissions):
		submissionArray = []
		finalnames = []
		for x in submissions:
			submissionArray.append(str(x))
			i = str(x)
			
			finalnames.append(x)
			if '[AMA Request]' not in i:
				numUpvotes = int(i[0: i.find(" ")])
				if numUpvotes > 400:
					finalnames.append(x)
	
		return finalnames


