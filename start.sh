if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/NIHUU/Deletebot /Deletebot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Deletebot
fi
cd /Deletebot
pip3 install -U -r requirements.txt
echo "Starting thomas shelby....🔥"
python3 bot.py
