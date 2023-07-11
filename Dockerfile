FROM nginx:latest 
LABEL "author"="mavrick202@gmail.com "
RUN apt install -y curl nano 
COPY index.html /usr/share/nginx/html/
COPY contact.html /usr/share/nginx/html/
COPY scorekeeper.js /usr/share/nginx/html/
COPY style.css /usr/share/nginx/html/
CMD ["nginx", "-g", "daemon off;"]
