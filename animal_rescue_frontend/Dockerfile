FROM node:18.16.0-alpine

WORKDIR /animal_rescue_frontend

COPY package*.json /animal_rescue_frontend/
RUN npm install

COPY . /animal_rescue_frontend/

CMD ["npm", "start"]