cd Documents/AtCoder
git add *.py
git add *.cpp
git status
read res
if [ "$res" = "y" ]; then
	read comment
	if [ -z "$comment" ]; then
	    comment="daily mission"
	fi
	git commit -m "${comment}"
	git push origin master
fi
