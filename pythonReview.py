def create_youtube_video(title, description):
	youtube_video = {"title" : title, "description" : description, "likes" : 0, "dislikes" : 0, "comments" : {}}
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

my_vid = create_youtube_video("How to go get milk (Fathers Edition)", "pls come back dad")
print(my_vid)
print(like(my_vid))
print(dislike(my_vid))
print(comment(my_vid, "xXmissing_fatherXx", "meet me in Belaruse Timmy."))