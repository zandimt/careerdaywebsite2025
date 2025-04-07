![Cover Career Day](frontend/public/logos/careerday_wide.svg)

# Authors
* Andi Toader
* Marcus Harald Olof Persson
# Navigation
* [Frontend](frontend/README.md)
* [Backend](backend/README.md)
# Setting up
1. Clone the repository
```bash
git clone https://github.com/zandimt/careerdaywebsite2025.git
cd careerdaywebsite2025
```
2. Set up environment files
```dotenv
DB_NAME=careerday
DB_USER=careeruser
DB_PASSWORD=yourpassword
DB_HOST=db
DB_PORT=5432
```
3. Start the Docker containers
```bash
docker-compose build
docker-compose up
```
* Frontend: http://localhost:3000
* Backend API: http://localhost:8000/api
* Django Admin: http://localhost:8000/admin
  * Username: admin 
  * Password: adminpass

