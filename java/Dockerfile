# base image
FROM openjdk:17-jdk-alpine

#WORKING DIR

WORKDIR /app

#copy code into container
COPY src/Main.java /app/Main.java

#compile code
RUN javac Main.java

#run

CMD ["java","Main"]
