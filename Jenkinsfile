pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {

        stage('Clean Workspace') {
            steps {
                sh '''
                echo "Cleaning old reports..."
                rm -rf test-reports dist build
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                pip install --upgrade pip
                pip install -r requirements.txt
                pip install pyinstaller pytest
                '''
            }
        }

        stage('Build Application') {
            steps {
                sh '''
                echo "Building executable..."
                pyinstaller --onefile app.py
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                mkdir -p test-reports
                pytest --junitxml=test-reports/results.xml
                '''
            }
        }

        stage('Manual Approval') {
            steps {
                input "Do you want to proceed with deployment?"
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                echo "Running application..."
                python app.py
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'dist/*', fingerprint: true
            junit 'test-reports/*.xml'
            echo "Pipeline execution completed."
        }

        success {
            echo "Python CI Pipeline SUCCESSFUL!"
        }

        failure {
            echo "Python CI Pipeline FAILED!"
        }
    }
}
