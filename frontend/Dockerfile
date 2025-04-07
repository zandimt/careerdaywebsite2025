# Use the official Node.js image
FROM node:18

# Set working directory
WORKDIR /app

# Copy dependencies and install
COPY package.json package-lock.json* ./
RUN npm install

# Copy the rest of the frontend
COPY . .

# Expose port
EXPOSE 3000

# Run the dev server
CMD ["npm", "run", "dev"]
