# Wanderly

Wanderly is a platform which helps users manage their own trips. They can create multiple trips, assign itineraries to those trips. Each itinerary has its own activities which the user can create and trip's expenses can be tracked. Each user can see a random inspirational published trip that other users have created so choosing a travelling destionation is even easier now.

## Installation

### 1. Clone the repo

```bash
  git clone https://github.com/IMAbadzhiev19/wanderly.git
```
   
### 2. Install dependencies
```bash
  pip install -r requirements.txt
```

### 3. Create the `.env` file in the root of your project.

#### Example `.env`

```python

# Database setup
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

# Cloudinary setup
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
```

### 4. Run the migrations

```bash
  python manage.py migrate
```

### 5. Run the project

```bash
  python manage.py runserver
```
