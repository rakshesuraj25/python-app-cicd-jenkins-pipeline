pipeline {
    agent {
        docker {
            image 'python:3.10'
            args '-u root:root'
        }
    }

    stages {

        stage('Clean Workspace') {
            steps {
                sh '''
                echo "Cleaning workspace..."
                rm -rf test-reports dist build
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                echo "Installing dependencies..."
                pip install --no-cache-dir -r requirements.txt
                pip install --no-cache-dir pyinstaller pytest
                '''
            }
        }

        stage('Build Application') {
            steps {
                sh '''
                echo "Building application..."
                pyinstaller --onefile app.py
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                mkdir -p test-reports
                pytest --junitxml=test-reports/results.xml || true
                '''
            }
        }

        stage('Manual Approval') {
            steps {
                input "Proceed to deployment?"
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
            echo "Archiving artifacts and reports..."
            archiveArtifacts artifacts: 'dist/*', fingerprint: true
            junit allowEmptyResults: true, testResults: 'test-reports/*.xml'
        }

        success {
            echo "✅ Python CI Pipeline SUCCESSFUL"
        }

        failure {
            echo "❌ Python CI Pipeline FAILED"
        }
    }
}
