# Movies @ Mariana Tek

## Overview
Mariana Tek is hosting a series of events called The Movies @ Mariana Tek this summer for camaraderie purposes. This application provides a platform for users to view the schedule of movies, separated by date. Users can filter movies by genre and search for movies by title.

## Installation
1. Clone the repository: `git clone https://github.com/your/repository.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Apply migrations: `python manage.py migrate`
4. Run the development server: `python manage.py runserver`

## URLs

### Movie List View
- **URL:** `/movies/`
- **Description:** Displays the list of movies with filters and search options.
- **Method:** GET
- **Parameters:**
  - `genre` (optional): Filter movies by genre.
  - `search` (optional): Search movies by title.

### Movie Create/List View
- **URL:** `/app_movies/`
- **Description:** Displays the list of movies and allows creating new movies.
- **Method:** 
  - GET: Retrieves the list of movies.
  - POST: Creates a new movie.
- **Parameters:** None

### Movie Update/Delete View
- **URL:** `/app_movies/<int:pk>`
- **Description:** Allows updating and deleting a specific movie by its ID.
- **Method:**
  - GET: Retrieves details of a specific movie.
  - PUT: Updates details of a specific movie.
  - DELETE: Deletes a specific movie.
- **Parameters:**
  - `pk`: ID of the movie to be updated/deleted.

