virtualenv env
mkdir app_data
call env\scripts\activate
pip install -r requirements.txt
python app.py make_db make_default_user