# build_files.sh
echo "Building files...."
pip install -r requirements.txt

echo "Migration...."
python3.9 manage.py makemigrations models  
python3.9 manage.py migrate models

echo "Collectstatic...."
python3.9 manage.py collectstatic