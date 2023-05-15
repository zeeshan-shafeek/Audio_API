# Audio Intelligence API

The Audio Intelligence API is a Django-based web application that provides audio analysis and classification functionality for Capella Backend. It allows Client App to submit audio files for analysis, classify them as "infant cry" or not, and retrieve analysis results.

## Installation

1. Clone the repository:
    git clone https://github.com/zeeshan-shafeek/Audio_API.git

2. Install the project dependencies:
    cd Audio_API
    pip install -r requirements.txt


3. Configure the database:
- Set up your PostgreSQL database and update the database settings in `settings.py`.
- Apply the database migrations:
  ```
  python manage.py migrate
  ```

4. Configure cache and Celery:
- Set up the cache backend in `settings.py`, choosing the appropriate backend (e.g., Redis, Memcached).
- Configure Celery settings, including the broker URL and result backend, in `settings.py`.

5. Run the development server:
    py manage.py runserver

## EndPoints

The `SolutionViewSet` is a view set that provides read-only operations for Solution models. It is used by client app to retrieve solution data by making GET requests with the appropriate ID and timestamp.

The `UserAudioViewSet` is a view set that provides both read and write operations to the client app for UserAudio models. It determines the appropriate serializer class to use based on the request method.




## Usage

### SolutionViewSet
To use the `SolutionViewSet`, follow these steps:

1. Make a GET request to the appropriate endpoint with the required parameters.
   - Endpoint: `/solution/{id}/`
   - Parameters:
     - `id` (required): The ID of the solution to retrieve.

2. The server will return a response containing the solution data in JSON format.

Example Request:

    GET /solution/12345/


Example Response:

```json
{
  "id": 12345,
  "timeStamp": "2023-05-15T10:30:00Z",
  "solution_audio": "http://example.com/audio/12345",
  "text": "This is the solution text",
  "Video_content": "http://example.com/video/12345"
}
```

### UserAudioViewSet
To use the `UserAudioViewSet`, follow these steps:

1. Make a request to the appropriate endpoint using the desired HTTP method (GET, POST, PUT, PATCH, DELETE).
   - Endpoint: `/user-audio/`

2. The server will automatically select the appropriate serializer class based on the request method.
   - If the request method is GET, the `UserAudioGetSerializer` will be used to serialize the response.
   - For other methods (POST, PUT, PATCH, DELETE), the `UserAudioPostSerializer` will be used.

Example GET Request:
    GET /user-audio/


Example Response:

```json
{
  "id": 1,
  "timeStamp": "2023-05-15T10:30:00Z",
  "createdAt": "2023-05-15T10:30:00Z",
  "Audio_content": "http://example.com/audio/1"
}
```

Example POST Request:
    POST /user-audio/
    Content-Type: multipart/form-data

Example Response:

```json
 {
        "id": 1,
        "class_distribution": null,
        "Video_content": "http://example.com/video/1",
        "Infant_cry_class_by_model": "",
        "Infant_cry_class_rate": "",
        "Infant_cry_class_by_user": ""
    }
```
