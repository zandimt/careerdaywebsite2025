![Cover Career Day](frontend/public/logos/careerday_wide.svg)

# Authors
* Andi Toader
* Marcus Harald Olof Persson
# Navigation
* [Frontend](frontend/README.md)
* [Backend](backend/README.md)
# Setting up a local instance
0. Set up a local instance of the [Cover website](https://bitbucket.org/cover-webcie/cover-php)

Not required, but needed for full functionality.

1. Clone the repository
```bash
git clone https://github.com/zandimt/careerdaywebsite2025.git
cd careerdaywebsite2025
```
2. Set up environment files [.env](backend/.env)
Create a copy of `.env` and rename it to `.env.local` in the `backend` directory. This file is used to set up the local environment variables for the Django application.
```dotenv
SECRET_KEY='your-secret-key'
DEBUG=False

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASS=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
```
3. Start the Docker containers (and locally run the Cover website)
```bash
docker-compose build
docker-compose up
```
* Frontend: http://localhost:3000
* Backend API: http://localhost:8001/api
* Django Admin: http://localhost:8001/admin
  * Username: admin 
  * Password: adminpass
* Cover: http://localhost:8000

