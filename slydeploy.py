import requests

headers = {
    'X-API-KEY': 'JbZudbZeY3f25X8uRijxBl15R928PgejBuLEyQzJ1FNcMzci994qAyrrINX8mOy6ZG1J4HIC4so0KugVzb6d5rH01yJroL6wVhypSUg6hoYfWanss5ERzZqhzqfR7vPO',
}

files = (
    ('id', (None, '28460')),
    ('data', (None, '{}')),
    ('image', ('mypicture.jpg;type=image/jpeg', open('/Volumes/data/git/demo-self-driving/data/0298.png.jpg', 'rb')))
)

response = requests.post('https://app.supervise.ly/public/api/v3/models.infer', headers=headers, files=files)
print(response.content)
print(response)
