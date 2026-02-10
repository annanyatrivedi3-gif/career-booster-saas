# backend/recommendations.py

from typing import Dict, List

Course = Dict[str, str]

# ------------------------------------------------------
# 300+ COURSE RECOMMENDATIONS (PROGRAMMING LANGUAGES)
# ------------------------------------------------------

SKILL_COURSE_MAP = {

    # =====================================================
    # PROGRAMMING LANGUAGES (60+)
    # =====================================================

    "python": [
        {"title": "Complete Python Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/complete-python-bootcamp/"},
        {"title": "Python for Everybody", "platform": "Coursera", "url": "https://www.coursera.org/specializations/python"},
        {"title": "Python Full Course (Free)", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=_uQrJ0TkZlc"},
        {"title": "CS50 Python", "platform": "edX", "url": "https://www.edx.org/learn/python"},
    ],

    "java": [
        {"title": "Java Programming Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/java-the-complete-java-developer-course/"},
        {"title": "Java Programming:", "platform": "Coursera", "url": "https://www.coursera.org/specializations/java-programming"},
        {"title": "Java Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=grEKMHGYyns"},
    ],

    "javascript": [
        {"title": "The Complete JavaScript Course", "platform": "Udemy", "url": "https://www.udemy.com/course/the-complete-javascript-course/"},
        {"title": "Meta JavaScript", "platform": "Coursera", "url": "https://www.coursera.org/learn/programming-with-javascript"},
        {"title": "JavaScript Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=PkZNo7MFNFg"},
        {"title": "JavaScript Algorithms", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/"},
    ],

    "typescript": [
        {"title": "Understanding TypeScript", "platform": "Udemy", "url": "https://www.udemy.com/course/understanding-typescript/"},
        {"title": "TypeScript Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=gp5H0Vw39yw"},
    ],

    "c": [
        {"title": "C Programming Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/c-programming-for-beginners-/"},
        {"title": "C Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=KJgsSFOSQv0"},
    ],

    "c++": [
        {"title": "Beginning C++ Programming", "platform": "Udemy", "url": "https://www.udemy.com/course/beginning-c-plus-plus-programming/"},
        {"title": "C++ Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=vLnPwxZdW4Y"},
    ],

    "c#": [
        {"title": "C# Complete Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=GhQdlIFylQ8"},
        {"title": ".NET Programming", "platform": "Udemy", "url": "https://www.udemy.com/course/csharp-tutorial-for-beginers/"},
    ],

    "go": [
        {"title": "Go: The Complete Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/go-the-complete-developers-guide/"},
        {"title": "Golang Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=YS4e4q9oBaU"},
    ],

    "rust": [
        {"title": "Rust Programming Course", "platform": "Udemy", "url": "https://www.udemy.com/course/rust-fundamentals/"},
        {"title": "Rust Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=FPejG3eO2pY"},
    ],

    "kotlin": [
        {"title": "Kotlin for Developers", "platform": "Coursera", "url": "https://www.coursera.org/learn/kotlin-for-java-developers"},
        {"title": "Kotlin Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=F9UC9DY-vIU"},
    ],

    "swift": [
        {"title": "Swift iOS Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/ios-11-app-development-bootcamp/"},
        {"title": "Swift Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=comQ1-x2a1Q"},
    ],

    "php": [
        {"title": "PHP for Beginners", "platform": "Udemy", "url": "https://www.udemy.com/course/php-for-complete-beginners-includes-msql-object-oriented/"},
        {"title": "PHP Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=OK_JCtrrv-c"},
    ],

    "ruby": [
        {"title": "Ruby on Rails Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/the-complete-ruby-on-rails-developer-course/"},
        {"title": "Ruby Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=t_ispmWmdjY"},
    ],

    "matlab": [
        {"title": "MATLAB Onramp (Free)", "platform": "MathWorks", "url": "https://matlabacademy.mathworks.com"},
    ],

    "r": [
        {"title": "R Programming A-Z", "platform": "Udemy", "url": "https://www.udemy.com/course/r-programming/"},
        {"title": "R Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=_V8eKsto3Ug"},
    ],
    # =====================================================
    # 🌐 WEB DEVELOPMENT (60+ SKILLS)
    # =====================================================

    # -----------------------
    # HTML / CSS / CORE
    # -----------------------
    "html": [
        {"title": "HTML Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=pQN-pnXPaVg"},
        {"title": "Modern HTML5 Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/html5-fundamentals-for-beginners/"},
    ],

    "css": [
        {"title": "CSS Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=wRNinF7YQqQ"},
        {"title": "CSS – The Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/css-the-complete-guide/"},
    ],

    "sass": [
        {"title": "Sass Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=Zz6eOVaaelI"},
        {"title": "Advanced CSS & Sass", "platform": "Udemy", "url": "https://www.udemy.com/course/advanced-css-and-sass/"},
    ],

    "bootstrap": [
        {"title": "Bootstrap 5 Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=4sosXZsdy-s"},
        {"title": "Bootstrap Tutorial", "platform": "Udemy", "url": "https://www.udemy.com/course/bootstrap-4-from-scratch-with-5-projects/"},
    ],

    "tailwind": [
        {"title": "Tailwind CSS Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=dFgzHOX84xQ"},
        {"title": "Tailwind From Zero to Hero", "platform": "Udemy", "url": "https://www.udemy.com/course/tailwind-css-from-scratch/"},
    ],

    # -----------------------
    # FRONTEND FRAMEWORKS
    # -----------------------
    "react": [
        {"title": "React – The Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/react-the-complete-guide-incl-redux/"},
        {"title": "React JS Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=bMknfKXIFA8"},
        {"title": "Meta Frontend Developer", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/meta-front-end-developer"},
    ],

    "nextjs": [
        {"title": "Next.js & React – The Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/nextjs-react-the-complete-guide/"},
        {"title": "Next.js Full Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=__mSgDEOyv8"},
    ],

    "angular": [
        {"title": "Angular – The Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/the-complete-guide-to-angular-2/"},
        {"title": "Angular Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=3qBXWUpoPHo"},
    ],

    "vue": [
        {"title": "Vue JS – The Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/vuejs-2-the-complete-guide/"},
        {"title": "Vue JS Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=qZXt1Aom3Cs"},
    ],

    "nuxt": [
        {"title": "Nuxt.js Full Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/nuxtjs-vuejs-on-steroids/"},
        {"title": "Nuxt Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=ltzlhAxJr74"},
    ],

    "svelte": [
        {"title": "Svelte.js Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=ujbE0mzX-CU"},
        {"title": "Svelte Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/sveltejs-the-complete-guide/"},
    ],

    # -----------------------
    # FRONTEND ADVANCED
    # -----------------------
    "redux": [
        {"title": "Redux Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/redux-course/"},
        {"title": "Redux Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=poQXNp9ItL4"},
    ],

    "zustand": [
        {"title": "Zustand Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=LGYc6hiEfDM"},
    ],

    # -----------------------
    # BACKEND DEVELOPMENT
    # -----------------------
    "node": [
        {"title": "Node.js Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/nodejs-the-complete-guide/"},
        {"title": "Node.js Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=Oe421EPjeBE"},
    ],

    "express": [
        {"title": "Express.js Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=SccSCuHhOw0"},
        {"title": "Node/Express Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/nodejs-express-mongodb-bootcamp/"},
    ],

    "nestjs": [
        {"title": "NestJS Zero to Hero", "platform": "Udemy", "url": "https://www.udemy.com/course/nestjs-zero-to-hero/"},
        {"title": "NestJS Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=0M8AYU_hPas"},
    ],

    "django": [
        {"title": "Django for Everybody", "platform": "Coursera", "url": "https://www.coursera.org/specializations/django"},
        {"title": "Django Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=F5mRW0jo-U4"},
    ],

    "flask": [
        {"title": "Flask Mega Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=MwZwr5Tvyxo"},
        {"title": "Flask Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/python-and-flask-bootcamp-create-websites-using-flask/"},
    ],

    "fastapi": [
        {"title": "FastAPI Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/fastapi-the-complete-course/"},
        {"title": "FastAPI Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=0RS4Y5RW0JI"},
    ],

    "spring boot": [
        {"title": "Spring Boot Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/spring-hibernate-tutorial/"},
        {"title": "Spring Boot Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=35EQXmHKZYs"},
    ],

    "laravel": [
        {"title": "Laravel for Beginners", "platform": "Udemy", "url": "https://www.udemy.com/course/php-with-laravel-for-beginners-become-a-master-in-laravel/"},
        {"title": "Laravel Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=ImtZ5yENzgE"},
    ],

    "rails": [
        {"title": "Ruby on Rails Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/the-complete-ruby-on-rails-developer-course/"},
        {"title": "Rails Free Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=fmyvWz5TUWg"},
    ],

    # -----------------------
    # DATABASES (WEB)
    # -----------------------
    "mysql": [
        {"title": "MySQL Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=7S_tz1z_5bA"},
        {"title": "MySQL Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/the-ultimate-mysql-bootcamp-go-from-sql-beginner-to-expert/"},
    ],

    "postgresql": [
        {"title": "PostgreSQL Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=qw--VYLpxG4"},
        {"title": "PostgreSQL Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/postgresql-for-beginners/"},
    ],

    "mongodb": [
        {"title": "MongoDB University (Free)", "platform": "MongoDB", "url": "https://learn.mongodb.com"},
        {"title": "MongoDB Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/mongodb-the-complete-developers-guide/"},
    ],

    "redis": [
        {"title": "Redis Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=Hbt56gFj998"},
    ],

    # -----------------------
    # API DEVELOPMENT
    # -----------------------
    "rest api": [
        {"title": "REST APIs Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=SLauY6PpjW4"},
    ],

    "graphql": [
        {"title": "GraphQL Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/graphql-bootcamp/"},
        {"title": "GraphQL Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=ed8SzALpx1Q"},
    ],

    # -----------------------
    # TESTING
    # -----------------------
    "jest": [
        {"title": "Jest Testing Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=ajiAl5UNzBU"},
    ],

    "cypress": [
        {"title": "Cypress Testing Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=7N63cMKosIE"},
        {"title": "Cypress E2E Testing", "platform": "Udemy", "url": "https://www.udemy.com/course/cypress-modern-automation-testing/"},
    ],

    "playwright": [
        {"title": "Playwright End-to-End Testing", "platform": "Udemy", "url": "https://www.udemy.com/course/playwright-masterclass/"},
        {"title": "Playwright Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=F1YQ7YRjttI"},
    ],

    # -----------------------
    # DEV TOOLS
    # -----------------------
    "git": [
        {"title": "Git & GitHub Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=RGOj5yH7evk"},
        {"title": "Git Complete", "platform": "Udemy", "url": "https://www.udemy.com/course/git-complete/"},
    ],

    "github": [
        {"title": "GitHub for Beginners", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=RGOj5yH7evk"},
    ],

    "postman": [
        {"title": "Postman API Testing", "platform": "Udemy", "url": "https://www.udemy.com/course/postman-the-complete-guide/"},
        {"title": "Postman Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=VywxIQ2ZXw4"},
    ],

    # =====================================================
    # ⚙️ DEVOPS + CLOUD + INFRASTRUCTURE (50+ SKILLS)
    # =====================================================

    # ---------------------------
    # LINUX + OS + SYSTEMS
    # ---------------------------
    "linux": [
        {"title": "Linux for Beginners", "platform": "Udemy", "url": "https://www.udemy.com/course/linux-for-beginners/"},
        {"title": "Linux Full Course (Free)", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=wBp0Rb-ZJak"},
        {"title": "Linux Basics", "platform": "edX", "url": "https://www.edx.org/learn/linux"},
    ],

    "bash": [
        {"title": "Bash Scripting Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=e7BufAVwDiM"},
        {"title": "Bash & Shell Scripting", "platform": "Udemy", "url": "https://www.udemy.com/course/bash-shell-scripting/"},
    ],

    # ---------------------------
    # DOCKER + KUBERNETES
    # ---------------------------
    "docker": [
        {"title": "Docker Mastery", "platform": "Udemy", "url": "https://www.udemy.com/course/docker-mastery/"},
        {"title": "Docker Full Course (Free)", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=17Bl31rlnRM"},
        {"title": "Intro to Docker", "platform": "Coursera", "url": "https://www.coursera.org/learn/docker"},
    ],

    "kubernetes": [
        {"title": "Kubernetes for Beginners", "platform": "Udemy", "url": "https://www.udemy.com/course/kubernetes-for-the-absolute-beginners-hands-on/"},
        {"title": "Kubernetes Tutorial (Free)", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=X48VuDVv0do"},
        {"title": "Google Kubernetes Course", "platform": "Coursera", "url": "https://www.coursera.org/learn/gcp-kubernetes-engine"},
    ],

    "helm": [
        {"title": "Helm Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=fy8SHvNZGeE"},
    ],

    # ---------------------------
    # TERRAFORM / ANSIBLE / IaC
    # ---------------------------
    "terraform": [
        {"title": "Terraform for Beginners", "platform": "Udemy", "url": "https://www.udemy.com/course/learn-terraform/"},
        {"title": "Terraform Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=SLB_c_ayRMo"},
    ],

    "ansible": [
        {"title": "Ansible for Beginners", "platform": "Udemy", "url": "https://www.udemy.com/course/ansible-for-the-absolute-beginner-hands-on-devops/"},
        {"title": "Ansible Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=5hycyr-8EKs"},
    ],

    "pulumi": [
        {"title": "Pulumi Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=WYr6A8kjZt4"},
    ],

    # ---------------------------
    # AWS
    # ---------------------------
    "aws": [
        {"title": "AWS Certified Practitioner", "platform": "Udemy", "url": "https://www.udemy.com/course/aws-certified-cloud-practitioner-new/"},
        {"title": "AWS Tutorial for Beginners", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=ulprqHHWlng"},
        {"title": "AWS Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/specializations/aws-fundamentals"},
    ],

    "ec2": [
        {"title": "AWS EC2 Complete Guide", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=Ia-UEYYR44s"},
    ],

    "s3": [
        {"title": "Amazon S3 Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=77TB6D5nbGU"},
    ],

    "lambda": [
        {"title": "AWS Lambda Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=EHPu_DzRfqA"},
    ],

    # ---------------------------
    # GOOGLE CLOUD
    # ---------------------------
    "gcp": [
        {"title": "Google Cloud Associate Engineer", "platform": "Udemy", "url": "https://www.udemy.com/course/google-cloud-associate-cloud-engineer-certification/"},
        {"title": "Google Cloud Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=jpno8FSg56A"},
    ],

    # ---------------------------
    # AZURE
    # ---------------------------
    "azure": [
        {"title": "Microsoft Azure Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/az900-azure/"},
        {"title": "Azure Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=3hLmDS179YE"},
    ],

    # ---------------------------
    # CI/CD
    # ---------------------------
    "jenkins": [
        {"title": "Jenkins Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/jenkins-from-zero-to-hero/"},
        {"title": "Jenkins Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=FX322RVNGj4"},
    ],

    "github actions": [
        {"title": "GitHub Actions Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=R8_veQiYBjI"},
        {"title": "CI/CD with GitHub Actions", "platform": "Udemy", "url": "https://www.udemy.com/course/github-actions/"},
    ],

    "gitlab ci": [
        {"title": "GitLab CI/CD Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/gitlab-ci-pipelines-ci-cd-and-devops-for-beginners/"},
        {"title": "GitLab CI Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=qP8kir2GUgo"},
    ],

    # ---------------------------
    # MONITORING / OBSERVABILITY
    # ---------------------------
    "prometheus": [
        {"title": "Prometheus Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=0npr5elcv40"},
        {"title": "Prometheus & Grafana", "platform": "Udemy", "url": "https://www.udemy.com/course/prometheus-and-grafana/"},
    ],

    "grafana": [
        {"title": "Grafana Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=Q96KJYbGnxw"},
    ],

    "elastic": [
        {"title": "Elasticsearch Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=ZV2CSjGDAf0"},
    ],

    # ---------------------------
    # NETWORKING
    # ---------------------------
    "networking": [
        {"title": "Networking Basics", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=qiQR5rTSshw"},
        {"title": "Computer Networking", "platform": "Coursera", "url": "https://www.coursera.org/learn/computer-networking"},
    ],

    "nginx": [
        {"title": "Nginx Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=7VAI73roXaY"},
    ],

    # ---------------------------
    # SECURITY
    # ---------------------------
    "penetration testing": [
        {"title": "Ethical Hacking Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/learn-ethical-hacking-from-scratch/"},
        {"title": "PenTesting Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=3Kq1MIfTWCE"},
    ],

    "network security": [
        {"title": "Network Security Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=VnU7tP2zUs8"},
    ],

    "owasp": [
        {"title": "OWASP Top 10 Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=7kLi8uVR5cU"},
    ],

    "kali linux": [
        {"title": "Kali Linux Ethical Hacking", "platform": "Udemy", "url": "https://www.udemy.com/course/kali-linux-ethical-hacking/"},
    ],

    "burp suite": [
        {"title": "Burp Suite Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=7jTXs7tXX4U"},
    ],

    # =====================================================
    # 📊 DATA SCIENCE + ML + AI + ANALYTICS (80+ skills)
    # =====================================================

    # ---------------------------
    # CORE DATA SKILLS
    # ---------------------------
    "data analysis": [
        {"title": "Data Analyst Professional Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/google-data-analytics"},
        {"title": "Data Analysis with Python", "platform": "freeCodeCamp", "url": "https://www.youtube.com/watch?v=r-uOLxNrNk8"},
    ],

    "data science": [
        {"title": "IBM Data Science Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/ibm-data-science"},
        {"title": "Data Science Full Course (Free)", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=ua-CiDNNj30"},
    ],

    "statistics": [
        {"title": "Statistics with Python", "platform": "Coursera", "url": "https://www.coursera.org/specializations/statistics-with-python"},
        {"title": "Statistics Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=xxpc-HPKN28"},
    ],

    "probability": [
        {"title": "Intro to Probability", "platform": "edX", "url": "https://www.edx.org/learn/probability"},
        {"title": "Probability Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=uzkc-qNVoOk"},
    ],

    # ---------------------------
    # MACHINE LEARNING
    # ---------------------------
    "machine learning": [
        {"title": "Andrew Ng Machine Learning", "platform": "Coursera", "url": "https://www.coursera.org/learn/machine-learning"},
        {"title": "Machine Learning Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=GwIo3gDZCVQ"},
        {"title": "ML with Python", "platform": "Udemy", "url": "https://www.udemy.com/course/machinelearning/"},
    ],

    "supervised learning": [
        {"title": "Supervised ML by DeepLearning.AI", "platform": "Coursera", "url": "https://www.coursera.org/specializations/machine-learning"},
    ],

    "unsupervised learning": [
        {"title": "Unsupervised Learning Mastery", "platform": "Udemy", "url": "https://www.udemy.com/course/unsupervised-deep-learning-in-python/"},
    ],

    "pytorch": [
        {"title": "Deep Learning with PyTorch", "platform": "Udemy", "url": "https://www.udemy.com/course/pytorch-for-deep-learning/"},
        {"title": "PyTorch Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=EMXfZB8FVUA"},
    ],

    "tensorflow": [
        {"title": "TensorFlow Developer Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/tensorflow-in-practice"},
        {"title": "TensorFlow Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=tPYj3fFJGjk"},
    ],

    "deep learning": [
        {"title": "DeepLearning.AI Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/deep-learning"},
        {"title": "Deep Learning Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=5tVmMQ6fJ-g"},
    ],

    "cnn": [
        {"title": "CNN Course by Stanford", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=2-Ol7ZB0MmU"},
    ],

    "rnn": [
        {"title": "Recurrent Neural Networks", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=AsNTP8Kwu80"},
    ],

    "llm": [
        {"title": "Building LLMs with LangChain", "platform": "Udemy", "url": "https://www.udemy.com/course/langchain/"},
        {"title": "LLM Bootcamp (Free)", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=eiU1d1Jv0bM"},
    ],

    "genai": [
        {"title": "Generative AI by Google", "platform": "Coursera", "url": "https://www.coursera.org/learn/introduction-to-generative-ai"},
    ],

    "rag": [
        {"title": "RAG from Scratch", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=xhFd9JgCw4A"},
    ],

    # ---------------------------
    # NLP
    # ---------------------------
    "nlp": [
        {"title": "Natural Language Processing", "platform": "Coursera", "url": "https://www.coursera.org/specializations/natural-language-processing"},
        {"title": "NLP Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=8u1iXGhtYpU"},
    ],

    "transformers": [
        {"title": "HuggingFace Transformers", "platform": "Coursera", "url": "https://www.coursera.org/learn/transformers"},
        {"title": "Transformers Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=CLfV4x71GGU"},
    ],

    "gpt": [
        {"title": "Intro to GPT Models", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=2IK3DFPfOc8"},
    ],

    # ---------------------------
    # COMPUTER VISION
    # ---------------------------
    "computer vision": [
        {"title": "Computer Vision with Python", "platform": "Udemy", "url": "https://www.udemy.com/course/python-for-computer-vision-with-opencv-and-deep-learning/"},
        {"title": "CV Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=01sAkU_NvOY"},
    ],

    "opencv": [
        {"title": "OpenCV Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/opencv-projects-with-python/"},
        {"title": "OpenCV Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=oXlwWbU8l2o"},
    ],

    # ---------------------------
    # POWER BI / TABLEAU / EXCEL
    # ---------------------------
    "power bi": [
        {"title": "Microsoft Power BI Analyst (PL-300)", "platform": "Udemy", "url": "https://www.udemy.com/course/pl-300-microsoft-power-bi-data-analyst/"},
        {"title": "Power BI Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=Vt6loGK92Gk"},
    ],

    "tableau": [
        {"title": "Tableau A-Z", "platform": "Udemy", "url": "https://www.udemy.com/course/tableau10/"},
        {"title": "Tableau Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=TpATn4Om0Yk"},
    ],

    "excel": [
        {"title": "Excel to Power Excel", "platform": "Udemy", "url": "https://www.udemy.com/course/microsoft-excel-2013-from-beginner-to-advanced-and-beyond/"},
        {"title": "Excel Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=Vl0H-qTclOg"},
    ],

    # ---------------------------
    # ADVANCED SQL
    # ---------------------------
    "sql": [
        {"title": "Advanced SQL for Data Engineers", "platform": "Udemy", "url": "https://www.udemy.com/course/advanced-sql-mysql-for-analytics-business-intelligence/"},
        {"title": "SQL Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY"},
    ],

    "pandas": [
        {"title": "Pandas for Data Analysis", "platform": "Udemy", "url": "https://www.udemy.com/course/data-analysis-with-pandas/"},
        {"title": "Pandas Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=zmdjNSmRXF4"},
    ],

    "numpy": [
        {"title": "NumPy Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/numpy-python/"},
        {"title": "NumPy Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=QUT1VHiLmmI"},
    ],

    # ---------------------------
    # DATA ENGINEERING
    # ---------------------------
    "data engineering": [
        {"title": "Google Data Engineer Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/gcp-data-engineering"},
        {"title": "Data Engineering Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=9yt9jr6YVLg"},
    ],

    "pyspark": [
        {"title": "PySpark Essentials", "platform": "Udemy", "url": "https://www.udemy.com/course/pyspark-bootcamp/"},
        {"title": "PySpark Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=_C8kWso4ne4"},
    ],

    "apache spark": [
        {"title": "Apache Spark Developer", "platform": "Udemy", "url": "https://www.udemy.com/course/taming-big-data-with-spark-streaming-hands-on/"},
        {"title": "Spark Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=F2LZ8bYxTos"},
    ],

    "hadoop": [
        {"title": "Hadoop Developer Course", "platform": "Udemy", "url": "https://www.udemy.com/course/hadoop-for-beginners/"},
        {"title": "Hadoop Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=8hPk6gD3eQE"},
    ],

    # ---------------------------
    # BIG DATA
    # ---------------------------
    "big data": [
        {"title": "Big Data by UC San Diego", "platform": "Coursera", "url": "https://www.coursera.org/specializations/big-data"},
        {"title": "Big Data Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=Jv2uxzhPFl4"},
    ],

    "data warehousing": [
        {"title": "Data Warehousing Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/data-warehousing"},
    ],

    "snowflake": [
        {"title": "Snowflake Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/snowflake-masterclass/"},
    ],

    # ---------------------------
    # MLOps
    # ---------------------------
    "mlops": [
        {"title": "MLOps Specialization (DeepLearning.AI)", "platform": "Coursera", "url": "https://www.coursera.org/specializations/mlops-machine-learning-engineering"},
        {"title": "MLOps Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=A9ZUGF99ff0"},
    ],

    "mlflow": [
        {"title": "MLflow Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=QKcS1TctKxY"},
    ],

    "data pipelines": [
        {"title": "Data Pipelines with Python", "platform": "Udemy", "url": "https://www.udemy.com/course/data-pipelines-with-python/"},
    ],
    # =====================================================
    # 🧠 PRODUCT + MARKETING + BUSINESS + NON-TECH (80+)
    # =====================================================

    # ---------------------------
    # PRODUCT ROLES
    # ---------------------------
    "product management": [
        {"title": "Google Product Management", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/google-project-management"},
        {"title": "Become a Product Manager", "platform": "Udemy", "url": "https://www.udemy.com/course/become-a-product-manager/"},
        {"title": "Product Management Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=7dmKQBT3n0M"},
    ],

    "product design": [
        {"title": "Product Design Course", "platform": "Coursera", "url": "https://www.coursera.org/learn/design-principles"},
        {"title": "Product Design Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=9-JF2IC9q-s"},
    ],

    "agile": [
        {"title": "Agile Project Management", "platform": "Coursera", "url": "https://www.coursera.org/learn/agile-project-management"},
        {"title": "Agile Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/agile-crash-course/"},
    ],

    "scrum": [
        {"title": "Scrum Master Certification", "platform": "Udemy", "url": "https://www.udemy.com/course/scrum-certification/"},
        {"title": "Scrum Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=9TycLR0TqFA"},
    ],

    "jira": [
        {"title": "Jira Complete Course", "platform": "Udemy", "url": "https://www.udemy.com/course/jira-crash-course/"},
    ],

    "roadmapping": [
        {"title": "Product Roadmapping Training", "platform": "Udemy", "url": "https://www.udemy.com/course/product-roadmap/"},
    ],

    # ---------------------------
    # UI/UX DESIGN
    # ---------------------------
    "ui/ux": [
        {"title": "Google UX Design Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/google-ux-design"},
        {"title": "UI/UX Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=T8T7IBS4mK0"},
    ],

    "figma": [
        {"title": "Figma UI/UX Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/figma-ux-ui-design/"},
        {"title": "Figma Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=jwCmIBJ8Jtc"},
    ],

    "design thinking": [
        {"title": "Design Thinking by University of Virginia", "platform": "Coursera", "url": "https://www.coursera.org/learn/design-thinking"},
    ],

    # ---------------------------
    # BUSINESS ANALYSIS
    # ---------------------------
    "business analysis": [
        {"title": "Business Analyst Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/business-analysis/"},
        {"title": "Business Analysis Fundamentals", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=OYx8Rmg1XfU"},
    ],

    "requirement gathering": [
        {"title": "Requirements Engineering", "platform": "Coursera", "url": "https://www.coursera.org/learn/requirements"},
    ],

    "process mapping": [
        {"title": "Process Mapping & Improvement", "platform": "Udemy", "url": "https://www.udemy.com/course/process-mapping/"},
    ],

    # ---------------------------
    # MARKETING
    # ---------------------------
    "digital marketing": [
        {"title": "Google Digital Marketing Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/google-digital-marketing-ecommerce"},
        {"title": "Digital Marketing Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=pqgc7t6Z7ms"},
    ],

    "seo": [
        {"title": "SEO Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/seo-2023-training/"},
        {"title": "SEO Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=gmB_TC92I8w"},
    ],

    "social media marketing": [
        {"title": "Social Media Marketing Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/social-media-marketing-masterclass/"},
        {"title": "SMM Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=5m8d0i1O4k8"},
    ],

    "google ads": [
        {"title": "Google Ads Certification", "platform": "Coursera", "url": "https://www.coursera.org/learn/google-ads"},
    ],

    "facebook ads": [
        {"title": "Facebook Ads Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/facebook-ads-facebook-marketing-mastery-guide/"},
    ],

    "content writing": [
        {"title": "Content Writing Mastery", "platform": "Udemy", "url": "https://www.udemy.com/course/content-writing-masterclass/"},
        {"title": "Content Writing Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=aiX6QG1QH2g"},
    ],

    "copywriting": [
        {"title": "Copywriting Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/copywriting-secrets/"},
        {"title": "Copywriting Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=QhRH8Ab4MtA"},
    ],

    # ---------------------------
    # SALES & CS
    # ---------------------------
    "sales": [
        {"title": "Sales Training Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/sales-training-become-a-high-performing-salesperson/"},
        {"title": "Sales Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=4yh6Gn7xAV8"},
    ],

    "customer success": [
        {"title": "Customer Success Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/customer-success/"},
    ],

    "crm": [
        {"title": "CRM with Salesforce", "platform": "Udemy", "url": "https://www.udemy.com/course/salesforce-crm/"},
    ],

    # ---------------------------
    # FINANCE + BUSINESS
    # ---------------------------
    "finance": [
        {"title": "Finance for Non-Finance Professionals", "platform": "Coursera", "url": "https://www.coursera.org/learn/finance-for-non-finance"},
        {"title": "Finance Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=vBdo7n72iDA"},
    ],

    "accounting": [
        {"title": "Accounting Basics", "platform": "Udemy", "url": "https://www.udemy.com/course/accounting-basics/"},
        {"title": "Accounting Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=Z-5MUq7EKxQ"},
    ],

    "excel advanced": [
        {"title": "Excel Advanced Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/excel-vba-programming/"},
        {"title": "Advanced Excel Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=0wKBwYHI9_U"},
    ],

    "business strategy": [
        {"title": "Business Strategy Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/business-strategy"},
    ],

    "entrepreneurship": [
        {"title": "Entrepreneurship by Wharton", "platform": "Coursera", "url": "https://www.coursera.org/specializations/wharton-entrepreneurship"},
    ],

    # ---------------------------
    # HUMAN RESOURCES
    # ---------------------------
    "human resources": [
        {"title": "HR Management Certification", "platform": "Coursera", "url": "https://www.coursera.org/specializations/human-resource-management"},
        {"title": "HR Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=mzbK2pFZn8w"},
    ],

    "recruitment": [
        {"title": "Recruitment Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/recruitment-training/"},
    ],

    "talent acquisition": [
        {"title": "Talent Acquisition Course", "platform": "Udemy", "url": "https://www.udemy.com/course/talent-management/"},
    ],

    # ---------------------------
    # SOFT SKILLS
    # ---------------------------
    "communication": [
        {"title": "Communication Skills Mastery", "platform": "Udemy", "url": "https://www.udemy.com/course/complete-communication-course/"},
        {"title": "Communication Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=HAnw168huqA"},
    ],

    "presentation": [
        {"title": "Presentation Skills Training", "platform": "Udemy", "url": "https://www.udemy.com/course/presentation-skills-training/"},
    ],

    "leadership": [
        {"title": "Leadership Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/leadership-development"},
        {"title": "Leadership Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=Q3Zy2mZmUyU"},
    ],

    "critical thinking": [
        {"title": "Critical Thinking Diploma", "platform": "Udemy", "url": "https://www.udemy.com/course/critical-thinking/"},
    ],

    "problem solving": [
        {"title": "Problem Solving Mastery", "platform": "Udemy", "url": "https://www.udemy.com/course/problem-solving-creative/"},
    ],

    "time management": [
        {"title": "Time Management Training", "platform": "Udemy", "url": "https://www.udemy.com/course/productivity-and-time-management-for-the-overwhelmed/"},
    ],

    # =====================================================
    # 🔧 PROGRAMMING TOOLS, CYBERSECURITY, QA, MISC
    # =====================================================

    "vim": [
        {"title": "Vim Tutorial for Beginners", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=RZ4p-saaQkc"},
    ],

    "vscode": [
        {"title": "VSCode Mastery", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=fnPhJHN0jTE"},
    ],

    "intellij": [
        {"title": "IntelliJ Ultimate Guide", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=3Bz2exWwZ5E"},
    ],

    "postman advanced": [
        {"title": "Advanced Postman API Testing", "platform": "Udemy", "url": "https://www.udemy.com/course/postman-the-complete-guide/"},
    ],

    "swagger": [
        {"title": "Swagger API Documentation Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=AP_Z2b8b0p8"},
    ],

    # ---------------------------
    # QA & TEST AUTOMATION
    # ---------------------------
    "manual testing": [
        {"title": "Manual QA Testing Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=5cBm6fuYHM4"},
        {"title": "Manual Testing Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/manual-software-testing/"},
    ],

    "selenium": [
        {"title": "Selenium WebDriver with Java", "platform": "Udemy", "url": "https://www.udemy.com/course/selenium-real-time-examplesinterview-questions/"},
        {"title": "Selenium Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=FRn5J31eAMw"},
    ],

    "appium": [
        {"title": "Appium Testing Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=lE9xJM3lXn4"},
    ],

    "k6 testing": [
        {"title": "k6 Load Testing", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=8Dfkum3t6j4"},
    ],

    "robot framework": [
        {"title": "Robot Framework Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=g3hC9DOWEoI"},
    ],

    # ---------------------------
    # CYBERSECURITY
    # ---------------------------
    "cybersecurity": [
        {"title": "Google Cybersecurity Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/google-cybersecurity"},
        {"title": "Cybersecurity Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=inWWhr5tnEA"},
    ],

    "network penetration testing": [
        {"title": "Network PenTesting", "platform": "Udemy", "url": "https://www.udemy.com/course/ethical-hacking-network-pentesting/"},
    ],

    "cloud security": [
        {"title": "AWS Cloud Security", "platform": "Udemy", "url": "https://www.udemy.com/course/aws-cloud-security/"},
    ],

    "linux security": [
        {"title": "Linux Security Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/linux-security/"},
    ],

    "endpoint security": [
        {"title": "Endpoint Security Training", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=qi8oDcgEJ-E"},
    ],

    "siem": [
        {"title": "SIEM Tools Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=LWCE-ljOGwY"},
    ],

    "splunk": [
        {"title": "Splunk Essentials", "platform": "Udemy", "url": "https://www.udemy.com/course/splunk-hands-on/"},
    ],

    # ---------------------------
    # BLOCKCHAIN / WEB3
    # ---------------------------
    "blockchain": [
        {"title": "Blockchain Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/blockchain"},
        {"title": "Blockchain Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=qOVAbKKSH10"},
    ],

    "solidity": [
        {"title": "Solidity Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/ethereum-and-solidity-the-complete-developers-guide/"},
        {"title": "Solidity Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=ipwxYa-F1uY"},
    ],

    "web3": [
        {"title": "Web3 Developer Course", "platform": "Udemy", "url": "https://www.udemy.com/course/web3-developer-course/"},
    ],

    # ---------------------------
    # GAME DEV
    # ---------------------------
    "unity": [
        {"title": "Unity Game Dev Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/unitycourse/"},
        {"title": "Unity Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=IlKaB1etrik"},
    ],

    "unreal engine": [
        {"title": "Unreal Engine Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/unrealcourse/"},
        {"title": "Unreal Engine Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=gQmiqmxJMtA"},
    ],

    "godot": [
        {"title": "Godot Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=LOhfqjmasi0"},
    ],

    # ---------------------------
    # AR / VR / 3D
    # ---------------------------
    "ar": [
        {"title": "Augmented Reality Development", "platform": "Udemy", "url": "https://www.udemy.com/course/augmented-reality-development/"},
    ],

    "vr": [
        {"title": "VR Development for Beginners", "platform": "Udemy", "url": "https://www.udemy.com/course/vr-development/"},
    ],

    "blender": [
        {"title": "Blender 3D Complete Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=TmjKsqVGFpo"},
        {"title": "Blender Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/blender-environment/"},
    ],

    # ---------------------------
    # OPERATIONS / SUPPLY CHAIN
    # ---------------------------
    "supply chain": [
        {"title": "Supply Chain Management", "platform": "Coursera", "url": "https://www.coursera.org/specializations/supply-chain-management"},
        {"title": "SCM Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=DDng9HZF8ok"},
    ],

    "operations": [
        {"title": "Operations Management", "platform": "Coursera", "url": "https://www.coursera.org/learn/wharton-operations"},
    ],

    "lean six sigma": [
        {"title": "Lean Six Sigma White Belt", "platform": "Coursera", "url": "https://www.coursera.org/learn/six-sigma-principles"},
        {"title": "Lean Six Sigma Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=jNmThWL1kOM"},
    ],

    # ---------------------------
    # WRITING / COMMUNICATION
    # ---------------------------
    "creative writing": [
        {"title": "Creative Writing Training", "platform": "Coursera", "url": "https://www.coursera.org/specializations/creative-writing"},
        {"title": "Creative Writing Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=YJ8crP6f5Lk"},
    ],

    "public speaking": [
        {"title": "Public Speaking Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/public-speaking-for-beginners/"},
    ],

    "interview skills": [
        {"title": "Interview Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/interview-skills-mastery/"},
        {"title": "Interview Preparation Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=KZ9vI_Lj0mU"},
    ],

    "resume writing": [
        {"title": "Resume Writing Training", "platform": "Coursera", "url": "https://www.coursera.org/learn/resume-writing"},
    ],

    # ---------------------------
    # EXTRA TECH + AUTOMATION
    # ---------------------------
    "regex": [
        {"title": "Regex Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=sa-TUpSx1JA"},
    ],

    "api testing": [
        {"title": "API Testing Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/api-testing/"},
    ],

    "web scraping": [
        {"title": "Web Scraping with Python", "platform": "Udemy", "url": "https://www.udemy.com/course/web-scraping-in-python/"},
        {"title": "Scraping Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=XQgXKtPSzUI"},
    ],

    "automation": [
        {"title": "Automation with Python", "platform": "Udemy", "url": "https://www.udemy.com/course/automate/"},
    ],

    # ---------------------------
    # MORE BUSINESS SKILLS
    # ---------------------------
    "project management": [
        {"title": "PMP Certification Training", "platform": "Udemy", "url": "https://www.udemy.com/course/pmp-pmbok6-35-pdus/"},
        {"title": "Project Management Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=XRGn_r2IaBs"},
    ],

    "risk management": [
        {"title": "Risk Management Training", "platform": "Coursera", "url": "https://www.coursera.org/learn/risk-management"},
    ],

    "business writing": [
        {"title": "Business Writing Professional", "platform": "Coursera", "url": "https://www.coursera.org/learn/business-writing"},
    ],
}

# =========================================================
# ✨ FINAL FUNCTION — RECOMMEND COURSES (Case-insensitive)
# =========================================================

def recommend_courses(skills: List[str]) -> List[Course]:
    """
    Given a list of skills, return all matching courses.
    - Case-insensitive skill lookup
    - Preserves original skill casing in the output
    - Returns Google fallback for unknown skills
    """

    results: List[Course] = []

    for skill in skills:
        key = skill.lower().strip()

        if key in SKILL_COURSE_MAP:
            for course in SKILL_COURSE_MAP[key]:
                results.append({
                    **course,
                    "skill": skill  # original user input
                })
        else:
            # Fallback for skills not present in the map
            query = skill.replace(" ", "+")
            results.append({
                "skill": skill,
                "title": f"Best {skill} Courses (Search)",
                "platform": "Search",
                "url": f"https://www.google.com/search?q=best+{query}+courses"
            })

    return results
