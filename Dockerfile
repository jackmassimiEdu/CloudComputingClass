FROM openjdk
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN javac dockerProject.java
CMD ["java", "dockerProject"]