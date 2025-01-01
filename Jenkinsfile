pipeline {
  agent any
  stages {
    stage("STOP") {
      steps {
        sh ''' sudo docker stop date_parser || true '''
      }
    }
    stage("REMOVE") {
      steps {
        sh ''' sudo docker rm date_parser || true '''
      }
    }
    stage("BUILD") {
      steps {
        sh ''' sudo docker build -t date_parser .  '''
      }
    }
    stage("RUN") {
      steps {
        sh ''' sudo docker run --env-file ./xlrt.env --restart always -d -p 8035:8035 --name date_parser date_parser  '''
      }
    }
    
  }
}