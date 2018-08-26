if [ "$#" -ne 2 ]; then
    echo "Illegal number of parameters"
fi
find $1  -print0 | xargs -0 -P $2 -I {} python build_phash.py {} | tee phash.txt
sed -i '/^$/d' phash.txt
