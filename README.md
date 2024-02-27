# Django Sports API

This is a simple Django project that serves as an API for managing sports data. The project provides endpoints to list all sports and retrieve, update, or delete details for a specific sport.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

## API Endpoints

### List All Sports

- **URL:** `/sports/`
- **Method:** `GET`
- **Description:** Retrieve a list of all sports.
- **Response Format:** JSON

### Retrieve, Update, or Delete a Specific Sport

- **URL:** `/sports/<int:id>`
- **Methods:**
  - `GET`: Retrieve details for a specific sport.
  - `PUT`: Update details for a specific sport.
  - `DELETE`: Delete a specific sport.
- **Parameters:** `<int:id>` - The unique identifier for the sport.
- **Response Format:** JSON
