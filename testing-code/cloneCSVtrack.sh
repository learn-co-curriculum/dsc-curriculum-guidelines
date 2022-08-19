mkdir $1
cd $1
cat ../$1.csv | while IFS="," read -r a; do temp="${a%\"}"; temp="${temp#\"}"; git clone "$temp"; done
