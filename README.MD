# Animal Rescue Web App :dog:

This is a Django REST API backend + React frontend web application. 

## Installation

## API Usage

```bash
animal-rescue: source venv/bin/activate

animal-rescue: python manage.py runserver

```
### Access URLs
url: http://127.0.0.1:8000/api/animal_rescue_api/
http://127.0.0.1:8000/api/animal_rescue_api/update/1
http://127.0.0.1:8000/api/animal_rescue_api/delete/1


## Front End
```bash
animal_rescue_frontend:npm run start
```

## Docker

```bash
docker-compose build

docker-compose up
```

## Testing

```bash
export DJANGO_SETTINGS_MODULE=animal_rescue_app.settings

```




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)