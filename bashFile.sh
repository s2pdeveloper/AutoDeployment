cat << 'EOF'
echo 'Hello, World!' > output.txt;
uname -a >> output.txt;
df -h >> output.txt;
whoami >> output.txt;
cat output.txt;
EOF

MAIL_USERNAME=poojadabi1804@gmail.com
MAIL_PASSWORD=vncl bggr ovpe dnrk
MAIL_FROM=poojadabi1804@gmail.com
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
MAIL_FROM_NAME=pooja dabi
SECRET_KEY=autodeployhelpes