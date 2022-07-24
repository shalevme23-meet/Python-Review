def create_youtube_video(title, description, tags):
	youtube_video = {"title" : title, "description" : description, "likes" : 0, "dislikes" : 0, "comments" : {}, "hashtag" : tags}
	return youtube_video
def like(vid):
	if "likes" in vid:
		vid["likes"] += 1
	return vid
def dislike(vid):
	if "dislikes" in vid:
		vid["dislikes"] += 1
	return vid
def comment(vid, name, txt):
	vid["comments"][name] = txt
	return vid
def similarity(vid1, vid2):
	percent = 0
	for tag1 in vid1["hashtag"]:
		for tag2 in vid2["hashtag"]:
			if tag1 == tag2:
				percent += 20
	return percent

my_vid1 = create_youtube_video("How to go get milk (Fathers Edition)", "pls come back dad", ["sad", "missingfather", "depression", "forgotthemilk", "nomilk"])
my_vid2 = create_youtube_video("How to ditch a child (Belarus Edition)", "easy and simple, very affordable", ["notimmylife", "missingfather", "belarus", "forgotthemilk", "nomoredad"])
print(my_vid1)
print(like(my_vid1))
print(dislike(my_vid1))
print(comment(my_vid1, "xXmissing_fatherXx", "meet me in Belarus Timmy."))
print(similarity(my_vid1, my_vid2))