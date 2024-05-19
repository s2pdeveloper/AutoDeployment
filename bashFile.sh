cat << 'EOF'
echo 'Hello, World!' > output.txt;
uname -a >> output.txt;
df -h >> output.txt;
whoami >> output.txt;
cat output.txt;
EOF

